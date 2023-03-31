function reviewQuestionProcessing() {


    ////////////// Check if all boxes are checked; if not, error message and return.
    // Get all inputs, grouped into arrays by question      [ [q1-a1,q1-a2], [q2-a1,q2-a2], etc. ]
    let answer_groups = document.getElementsByClassName('answer-group');
    let organized_answer_status = [];
    for (answers of answer_groups) {
        let temp_array=[];
        // iterate over specific answers
        for (answer of answers.getElementsByClassName('answer')) {
            let checkbox_input_ele = answer.querySelector('input');
            // get checked status (false if not, true if yes)
            temp_array.push(checkbox_input_ele.checked);
        }
        organized_answer_status.push(temp_array);
    }

    for (a_group of organized_answer_status) {
        if (!a_group.includes(true)) {
            // No answer was selected in this group, so show error and quit function.
            document.getElementById("error-answer-all-questions-message").hidden = false;
            const reflow = document.getElementById("error-answer-all-questions-message").offsetHeight; // Repaint the browser to enable transitions of newly shown element
            document.getElementById("error-answer-all-questions-message").classList.add('smooth-open');
            return
        }
    }
    // Make sure error message is hidden now if shown:
    document.getElementById("error-answer-all-questions-message").hidden = true;
    //////////////




    ////////////// Hide main form button, show Next Steps button
    document.querySelector('div#check-answer-btn-div').hidden=true;
    document.querySelector('div#push-to-next-steps-div').hidden=false;
    const reflow = document.getElementById("push-to-next-steps-div").offsetHeight; // Repaint the browser to enable transitions of newly shown element
    document.getElementById("push-to-next-steps-div").classList.add('smooth-open');
    //////////////

    ////////////// Freeze radio button inputs
    let all_radios = document.querySelectorAll('input[type="radio"]');
    for (radio of all_radios) {
        radio.disabled = true;
        // remove hover on pointer
        radio.style.cursor='none';
    }


    ///////////// Show fa icons for all checked items
    for (answers of answer_groups) {
        for (answer of answers.getElementsByClassName('answer')) {
            let checkbox_input_ele = answer.querySelector('input');
            let checkbox_status = checkbox_input_ele.checked; // true or false checked
            if (checkbox_status) {
                // show this icon
                answer.querySelector('.checkbox-icon').style.visibility = "visible"; 
                let reflow = answer.querySelector(".checkbox-icon").offsetHeight; // Repaint the browser to enable transitions of newly shown element
                answer.querySelector(".checkbox-icon").classList.add('smooth-open');   
            }
        }
    }




    // Hide all info_texts by default to clear them.
    const div_help_text = document.querySelectorAll('div.info_text');
    div_help_text.forEach(explanation_div => {
        // See if the checked answer is right or wrong
        let prepend_html = ''
        let answer_div = document.querySelector('.answers-for-'+explanation_div.id).querySelectorAll('div.answer');
        for (answers of answer_div) {
            // if checked, do analysis of right wrong
            if (answers.querySelector('input').checked) {
                // read status of right / wrong via icon
                if (answers.querySelector('span.checkbox-icon').classList.contains('fa-circle-check')) {
                    // correct
                    prepend_html = '<span class="correct-explain u-text-bold">Correct! </span>';
                }
                else {
                    // incorrect
                    prepend_html = '<span class="incorrect-explain u-text-bold">Incorrect. </span>';
                }
            }
        }

        explanation_div.querySelector('.info_text_preexplination').innerHTML = prepend_html + explanation_div.querySelector('.info_text_preexplination').innerHTML;
        explanation_div.hidden = false;
        let reflow = explanation_div.querySelector('.info_text_preexplination').offsetHeight; // Repaint the browser to enable transitions of newly shown element
        explanation_div.querySelector('.info_text_preexplination').classList.add('smooth-open');
    });
    
}