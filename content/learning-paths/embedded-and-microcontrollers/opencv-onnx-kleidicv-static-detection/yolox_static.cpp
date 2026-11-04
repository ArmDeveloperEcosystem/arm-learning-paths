#include <algorithm>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>

#include <opencv2/core.hpp>
#include <opencv2/dnn.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>

namespace
{

constexpr int kInputWidth = 640;
constexpr int kInputHeight = 640;

using Clock = std::chrono::steady_clock;

struct GridAndStride
{
    int gridX;
    int gridY;
    int stride;
};

struct Detection
{
    cv::Rect box;
    float score;
    int classId;
};

struct StageTimes
{
    double resizeMs = 0.0;
    double paddingMs = 0.0;
    double colorConversionMs = 0.0;
    double typeConversionMs = 0.0;
    double blobMs = 0.0;
    double inferenceMs = 0.0;
    double postprocessMs = 0.0;
    double renderMs = 0.0;

    double preprocessingMs() const
    {
        return resizeMs + paddingMs + colorConversionMs + typeConversionMs +
               blobMs;
    }

    double totalMs() const
    {
        return preprocessingMs() + inferenceMs + postprocessMs + renderMs;
    }
};

struct Summary
{
    double mean;
    double minimum;
    double standardDeviation;
};

double elapsedMilliseconds(Clock::time_point start, Clock::time_point end)
{
    return std::chrono::duration<double, std::milli>(end - start).count();
}

std::vector<std::string> loadLabels(const std::string& path)
{
    std::ifstream input(path);
    if (!input)
    {
        throw std::runtime_error("Unable to open label file: " + path);
    }

    std::vector<std::string> labels;
    std::string label;
    while (std::getline(input, label))
    {
        if (!label.empty())
        {
            labels.push_back(label);
        }
    }

    if (labels.size() != 80)
    {
        throw std::runtime_error("Expected 80 COCO labels, found " +
                                 std::to_string(labels.size()));
    }
    return labels;
}

std::vector<GridAndStride> generateGridAndStrides()
{
    const std::vector<int> strides = {8, 16, 32};
    std::vector<GridAndStride> gridAndStrides;

    for (int stride : strides)
    {
        const int gridWidth = kInputWidth / stride;
        const int gridHeight = kInputHeight / stride;
        for (int gridY = 0; gridY < gridHeight; ++gridY)
        {
            for (int gridX = 0; gridX < gridWidth; ++gridX)
            {
                gridAndStrides.push_back({gridX, gridY, stride});
            }
        }
    }
    return gridAndStrides;
}

cv::Size calculateResizedSize(const cv::Mat& image, float& scale)
{
    scale = std::min(kInputWidth / static_cast<float>(image.cols),
                     kInputHeight / static_cast<float>(image.rows));

    return cv::Size(
        std::max(1, static_cast<int>(std::round(image.cols * scale))),
        std::max(1, static_cast<int>(std::round(image.rows * scale))));
}

std::vector<Detection> postprocess(
    const std::vector<cv::Mat>& outputs,
    const std::vector<GridAndStride>& gridAndStrides,
    const cv::Size& originalSize,
    float scale,
    float confidenceThreshold,
    float nmsThreshold)
{
    if (outputs.empty())
    {
        throw std::runtime_error("The network returned no output tensors");
    }

    cv::Mat output = outputs.front();
    if (!output.isContinuous())
    {
        output = output.clone();
    }
    if (output.depth() != CV_32F || output.dims < 2)
    {
        throw std::runtime_error("Unexpected YOLOX output type or dimensions");
    }

    const int dimensions = output.size[output.dims - 1];
    if (dimensions != 85)
    {
        throw std::runtime_error("Expected 85 values per YOLOX proposal, found " +
                                 std::to_string(dimensions));
    }

    const int proposalCount = static_cast<int>(output.total() / dimensions);
    if (proposalCount != static_cast<int>(gridAndStrides.size()))
    {
        throw std::runtime_error("YOLOX output proposal count does not match the 640x640 grid");
    }

    const cv::Mat proposals(proposalCount, dimensions, CV_32F, output.ptr<float>());
    std::vector<cv::Rect> candidateBoxes;
    std::vector<float> candidateScores;
    std::vector<int> candidateClassIds;

    for (int row = 0; row < proposalCount; ++row)
    {
        const float* values = proposals.ptr<float>(row);
        const float objectness = values[4];
        if (objectness <= 0.0F)
        {
            continue;
        }

        int classId = 0;
        float classScore = values[5];
        for (int candidateClass = 1; candidateClass < 80; ++candidateClass)
        {
            if (values[5 + candidateClass] > classScore)
            {
                classScore = values[5 + candidateClass];
                classId = candidateClass;
            }
        }

        const float score = objectness * classScore;
        if (score < confidenceThreshold)
        {
            continue;
        }

        const GridAndStride& grid = gridAndStrides[row];
        const float centerX = (values[0] + grid.gridX) * grid.stride;
        const float centerY = (values[1] + grid.gridY) * grid.stride;
        const float width = std::exp(values[2]) * grid.stride;
        const float height = std::exp(values[3]) * grid.stride;

        candidateBoxes.emplace_back(
            static_cast<int>(std::round(centerX - width * 0.5F)),
            static_cast<int>(std::round(centerY - height * 0.5F)),
            static_cast<int>(std::round(width)),
            static_cast<int>(std::round(height)));
        candidateScores.push_back(score);
        candidateClassIds.push_back(classId);
    }

    std::vector<int> retained;
    cv::dnn::NMSBoxesBatched(candidateBoxes, candidateScores, candidateClassIds,
                             confidenceThreshold, nmsThreshold, retained);

    const cv::Rect imageBounds(0, 0, originalSize.width, originalSize.height);
    std::vector<Detection> detections;
    detections.reserve(retained.size());

    for (int index : retained)
    {
        const cv::Rect& modelBox = candidateBoxes[index];
        cv::Rect originalBox(
            static_cast<int>(std::round(modelBox.x / scale)),
            static_cast<int>(std::round(modelBox.y / scale)),
            static_cast<int>(std::round(modelBox.width / scale)),
            static_cast<int>(std::round(modelBox.height / scale)));
        originalBox &= imageBounds;
        if (originalBox.area() > 0)
        {
            detections.push_back(
                {originalBox, candidateScores[index], candidateClassIds[index]});
        }
    }
    return detections;
}

cv::Mat renderDetections(
    const cv::Mat& image,
    const std::vector<Detection>& detections,
    const std::vector<std::string>& labels)
{
    cv::Mat rendered = image.clone();
    for (const Detection& detection : detections)
    {
        cv::rectangle(rendered, detection.box, cv::Scalar(0, 255, 0), 2);

        const std::string text =
            labels.at(detection.classId) + cv::format(" %.2f", detection.score);
        int baseline = 0;
        const cv::Size textSize =
            cv::getTextSize(text, cv::FONT_HERSHEY_SIMPLEX, 0.55, 1, &baseline);

        const int textX = detection.box.x;
        const int textY = std::max(textSize.height + 4, detection.box.y);
        const cv::Rect background(
            textX,
            textY - textSize.height - 4,
            std::min(textSize.width + 6, rendered.cols - textX),
            textSize.height + baseline + 6);

        cv::rectangle(rendered, background, cv::Scalar(0, 255, 0), cv::FILLED);
        cv::putText(rendered, text, cv::Point(textX + 3, textY),
                    cv::FONT_HERSHEY_SIMPLEX, 0.55, cv::Scalar(0, 0, 0), 1,
                    cv::LINE_AA);
    }
    return rendered;
}

StageTimes runPipeline(
    cv::dnn::Net& network,
    const cv::Mat& image,
    const std::vector<GridAndStride>& gridAndStrides,
    const std::vector<std::string>& labels,
    float confidenceThreshold,
    float nmsThreshold,
    std::vector<Detection>& detections,
    cv::Mat& rendered)
{
    StageTimes times;
    float scale = 1.0F;
    const cv::Size resizedSize = calculateResizedSize(image, scale);

    auto start = Clock::now();
    cv::Mat resized;
    cv::resize(image, resized, resizedSize, 0.0, 0.0, cv::INTER_LINEAR);
    auto end = Clock::now();
    times.resizeMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    cv::Mat padded;
    cv::copyMakeBorder(
        resized, padded, 0, kInputHeight - resized.rows, 0,
        kInputWidth - resized.cols, cv::BORDER_CONSTANT, cv::Scalar::all(114));
    end = Clock::now();
    times.paddingMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    cv::Mat rgb;
    cv::cvtColor(padded, rgb, cv::COLOR_BGR2RGB);
    end = Clock::now();
    times.colorConversionMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    cv::Mat floatImage;
    rgb.convertTo(floatImage, CV_32F);
    end = Clock::now();
    times.typeConversionMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    cv::Mat blob = cv::dnn::blobFromImage(
        floatImage, 1.0, cv::Size(), cv::Scalar(), false, false, CV_32F);
    end = Clock::now();
    times.blobMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    network.setInput(blob);
    std::vector<cv::Mat> outputs;
    network.forward(outputs, network.getUnconnectedOutLayersNames());
    end = Clock::now();
    times.inferenceMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    detections = postprocess(outputs, gridAndStrides, image.size(), scale,
                             confidenceThreshold, nmsThreshold);
    end = Clock::now();
    times.postprocessMs = elapsedMilliseconds(start, end);

    start = Clock::now();
    rendered = renderDetections(image, detections, labels);
    end = Clock::now();
    times.renderMs = elapsedMilliseconds(start, end);
    return times;
}

Summary summarize(const std::vector<double>& values)
{
    const double sum = std::accumulate(values.begin(), values.end(), 0.0);
    const double mean = sum / values.size();
    const double minimum = *std::min_element(values.begin(), values.end());

    double squaredDifferenceSum = 0.0;
    for (double value : values)
    {
        const double difference = value - mean;
        squaredDifferenceSum += difference * difference;
    }
    return {mean, minimum, std::sqrt(squaredDifferenceSum / values.size())};
}

void printSummary(const std::string& name, const std::vector<double>& values)
{
    const Summary summary = summarize(values);
    std::cout << std::left << std::setw(20) << name
              << " mean=" << std::right << std::fixed << std::setprecision(3)
              << std::setw(9) << summary.mean
              << " ms  min=" << std::setw(9) << summary.minimum
              << " ms  stddev=" << std::setw(9) << summary.standardDeviation
              << " ms\n";
}

} // namespace

int main(int argc, char** argv)
{
    const cv::String keys =
        "{help h usage ? |      | Print this message }"
        "{model          |      | Path to the YOLOX ONNX model }"
        "{image          |      | Path to the input image }"
        "{labels         |      | Path to the COCO label file }"
        "{output         |result.jpg| Path to the output image }"
        "{build-name     |unspecified| Label printed with the results }"
        "{confidence     |0.35  | Confidence threshold }"
        "{nms            |0.50  | Non-maximum suppression threshold }"
        "{warmup         |5     | Number of warm-up iterations }"
        "{iterations     |20    | Number of measured iterations }"
        "{threads        |0     | OpenCV thread count; 0 keeps the default }";

    cv::CommandLineParser parser(argc, argv, keys);
    parser.about("Run and benchmark YOLOX static-image detection with OpenCV DNN");
    if (parser.has("help"))
    {
        parser.printMessage();
        return 0;
    }
    const std::string modelPath = parser.get<std::string>("model");
    const std::string imagePath = parser.get<std::string>("image");
    const std::string labelPath = parser.get<std::string>("labels");
    const std::string outputPath = parser.get<std::string>("output");
    const std::string buildName = parser.get<std::string>("build-name");
    const float confidenceThreshold = parser.get<float>("confidence");
    const float nmsThreshold = parser.get<float>("nms");
    const int warmupIterations = parser.get<int>("warmup");
    const int measuredIterations = parser.get<int>("iterations");
    const int threads = parser.get<int>("threads");

    if (!parser.check())
    {
        parser.printErrors();
        return 1;
    }

    if (modelPath.empty() || imagePath.empty() || labelPath.empty())
    {
        std::cerr << "The --model, --image, and --labels arguments are required\n";
        return 1;
    }
    if (warmupIterations < 0 || measuredIterations <= 0 || threads < 0)
    {
        std::cerr << "Use non-negative warm-up and thread values, and at least one iteration\n";
        return 1;
    }

    try
    {
        if (threads > 0)
        {
            cv::setNumThreads(threads);
        }

        const cv::Mat image = cv::imread(imagePath, cv::IMREAD_COLOR);
        if (image.empty())
        {
            throw std::runtime_error("Unable to read input image: " + imagePath);
        }

        const std::vector<std::string> labels = loadLabels(labelPath);
        const std::vector<GridAndStride> gridAndStrides = generateGridAndStrides();

        cv::dnn::Net network = cv::dnn::readNetFromONNX(modelPath);
        network.setPreferableBackend(cv::dnn::DNN_BACKEND_OPENCV);
        network.setPreferableTarget(cv::dnn::DNN_TARGET_CPU);

        std::vector<Detection> detections;
        cv::Mat rendered;
        for (int iteration = 0; iteration < warmupIterations; ++iteration)
        {
            runPipeline(network, image, gridAndStrides, labels,
                        confidenceThreshold, nmsThreshold, detections, rendered);
        }

        std::vector<double> resizeTimes;
        std::vector<double> paddingTimes;
        std::vector<double> colorConversionTimes;
        std::vector<double> typeConversionTimes;
        std::vector<double> blobTimes;
        std::vector<double> inferenceTimes;
        std::vector<double> postprocessTimes;
        std::vector<double> renderTimes;
        std::vector<double> preprocessingTimes;
        std::vector<double> totalTimes;
        resizeTimes.reserve(measuredIterations);
        paddingTimes.reserve(measuredIterations);
        colorConversionTimes.reserve(measuredIterations);
        typeConversionTimes.reserve(measuredIterations);
        blobTimes.reserve(measuredIterations);
        inferenceTimes.reserve(measuredIterations);
        postprocessTimes.reserve(measuredIterations);
        renderTimes.reserve(measuredIterations);
        preprocessingTimes.reserve(measuredIterations);
        totalTimes.reserve(measuredIterations);

        for (int iteration = 0; iteration < measuredIterations; ++iteration)
        {
            const StageTimes times =
                runPipeline(network, image, gridAndStrides, labels,
                            confidenceThreshold, nmsThreshold, detections, rendered);
            resizeTimes.push_back(times.resizeMs);
            paddingTimes.push_back(times.paddingMs);
            colorConversionTimes.push_back(times.colorConversionMs);
            typeConversionTimes.push_back(times.typeConversionMs);
            blobTimes.push_back(times.blobMs);
            inferenceTimes.push_back(times.inferenceMs);
            postprocessTimes.push_back(times.postprocessMs);
            renderTimes.push_back(times.renderMs);
            preprocessingTimes.push_back(times.preprocessingMs());
            totalTimes.push_back(times.totalMs());
        }

        if (!cv::imwrite(outputPath, rendered))
        {
            throw std::runtime_error("Unable to write output image: " + outputPath);
        }

        std::cout << "Build label: " << buildName << '\n';
        std::cout << "OpenCV version: " << CV_VERSION << '\n';
        std::cout << "OpenCV threads: " << cv::getNumThreads() << '\n';
        std::cout << "Warm-up iterations: " << warmupIterations << '\n';
        std::cout << "Measured iterations: " << measuredIterations << '\n';
        std::cout << "Detections: " << detections.size() << '\n';
        printSummary("Resize:", resizeTimes);
        printSummary("Padding:", paddingTimes);
        printSummary("BGR to RGB:", colorConversionTimes);
        printSummary("Uint8 to float32:", typeConversionTimes);
        printSummary("Tensor packing:", blobTimes);
        printSummary("Preprocessing:", preprocessingTimes);
        printSummary("DNN inference:", inferenceTimes);
        printSummary("Postprocessing:", postprocessTimes);
        printSummary("Rendering:", renderTimes);
        printSummary("End-to-end:", totalTimes);
        std::cout << "Output image: " << outputPath << '\n';
    }
    catch (const cv::Exception& error)
    {
        std::cerr << "OpenCV error: " << error.what() << '\n';
        return 1;
    }
    catch (const std::exception& error)
    {
        std::cerr << "Error: " << error.what() << '\n';
        return 1;
    }

    return 0;
}
