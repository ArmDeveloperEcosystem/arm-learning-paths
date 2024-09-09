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
            findFiles(filePath, fileList);  // recursive look into directory
        } else if (file === 'index.html' && path.basename(path.dirname(filePath)) === '_demo') {
            fileList.push(filePath); // Check if the file is 'index.html' directly under a '_demo' directory
        }
    });

    return fileList;
}

// Function to uglify the JavaScript within the last script tag
function uglifyLastScriptTag(filePath) {
    let htmlContent = fs.readFileSync(filePath, 'utf8');

    const scriptTags = [...htmlContent.matchAll(/<script>([\s\S]*?)<\/script>/g)];     // Regex to find all script tags

    if (scriptTags.length > 0) {
        const lastScriptContent = scriptTags[scriptTags.length - 1][1];         // Get the last script tag content (demo script info will be here)
        const uglifiedContent = uglifyJS.minify(lastScriptContent).code;        // Uglify the content
        htmlContent = htmlContent.replace(lastScriptContent, uglifiedContent);  // Replace the last script content with the uglified version
        fs.writeFileSync(filePath, htmlContent, 'utf8');                        // Write the updated HTML back to the file
        console.log(`Uglified last <script> in ${filePath}`);                   // Report back
    } else {
        console.log(`No <script> tags found in ${filePath}`);
    }
}

// Find all relevant index.html files and uglify them
const filesToUglify = findFiles(baseDir);
filesToUglify.forEach(uglifyLastScriptTag);