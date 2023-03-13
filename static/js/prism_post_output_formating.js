window.addEventListener('DOMContentLoaded', (event) => {
    let all_code_elements = document.getElementsByClassName('output-lines');
    if (all_code_elements) { // Only process if there are elements that need to be processed.
        // span to indicate line is an output, and should be ignored by the 'copy' button
        let output_marker = "<span class='hidden-output-text'>__output__</span>";

        for (let codeblock of all_code_elements) {
            let html = codeblock.innerHTML.split('\n');
            let new_html = "";
            for (line of html) {
                let new_line = line;

                ///////////////// Case 1: makes entire codeblock formated as output (__output__ put in by render-codeblock.html)
                if (codeblock.classList.contains('language-output')) {
                    new_line = output_marker+"<span class='token output'>" + line + "</span>";
                }
                ///////////////// Case 2: output-lines for any language (__output__ put in by render-codeblock.html)
                else if (line.includes('__output__')) {         
                    new_line = output_marker+"<span class='token output'>" + line.replace('__output__','') + "</span>";
                }
                ///////////////// Case 3: command-line output (put in __output__ to be ignored by copy command, via prism.js)
                else if (line.includes('<span class="token output">')) {
                    new_line = output_marker + line;
                }

                new_html = new_html+new_line+'\n';
            }
            codeblock.innerHTML = new_html
            
        }
    }
});