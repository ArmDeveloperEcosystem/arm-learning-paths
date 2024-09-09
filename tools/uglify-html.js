const fs = require('fs');
const path = require('path');
const uglifyJS = require('uglify-js');

const baseDir = path.join(__dirname, '..', 'public', 'learning-paths');

// Recursively find all index.html files under _demo directories
function findFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            // If it's a directory, recurse into it
            findFiles(filePath, fileList);
        } else if (file === 'index.html' && path.basename(path.dirname(filePath)) === '_demo') {
            // Check if the file is 'index.html' directly under a '_demo' directory
            fileList.push(filePath);
        }
    });

    return fileList;
}

// Function to uglify the JavaScript within the last script tag
function uglifyLastScriptTag(filePath) {
    let htmlContent = fs.readFileSync(filePath, 'utf8');

    // Regex to find all script tags
    const scriptTags = [...htmlContent.matchAll(/<script>([\s\S]*?)<\/script>/g)];

    if (scriptTags.length > 0) {
        // Get the last script tag content
        const lastScriptContent = scriptTags[scriptTags.length - 1][1];

        // Uglify the content
        const uglifiedContent = uglifyJS.minify(lastScriptContent).code;

        // Replace the last script content with the uglified version
        htmlContent = htmlContent.replace(lastScriptContent, uglifiedContent);

        // Write the updated HTML back to the file
        fs.writeFileSync(filePath, htmlContent, 'utf8');

        console.log(`Uglified last <script> in ${filePath}`);
    } else {
        console.log(`No <script> tags found in ${filePath}`);
    }
}

// Find all relevant index.html files and uglify them
const filesToUglify = findFiles(baseDir);


filesToUglify.forEach(uglifyLastScriptTag);
