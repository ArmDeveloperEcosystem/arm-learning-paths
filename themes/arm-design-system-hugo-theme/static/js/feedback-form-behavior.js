function starRatingGiven(element) {
    // Hide Stars div and surface radio buttons
    document.getElementById('feedback-1-stars').hidden = true;

    // Show Radio button feedback depending on value
    document.getElementById('specific-stars').innerHTML = ' of '+element.value+' stars';
    document.getElementById('feedback-2-choice').hidden = false;
    if (parseInt(element.value) < 4) {
        document.getElementById('1-2-3-star-options').hidden = false;
    }
    else {
        document.getElementById('4-5-star-options').hidden = false;
    }
    const reflow = document.getElementById('feedback-2-choice').offsetHeight; // Repaint the browser to enable transitions of newly shown element
    document.getElementById('feedback-2-choice').classList.add('smooth-open');


}

function choiceFeedbackGiven() {     
    // if nothing checked, error
    if (document.querySelector('input[name="feedback-choice"]:checked')==null) {
        document.getElementById("choice-select-option-error").hidden = false;
        document.getElementById('choice-select-option-error').style.display = "inline-block";
        const reflow = document.getElementById('choice-select-option-error').offsetHeight; // Repaint the browser to enable transitions of newly shown element
        document.getElementById('choice-select-option-error').classList.add('smooth-open');
        return
    }

    // Hide Radio button feedback
    document.getElementById('feedback-2-choice').hidden = true;

    // Show Thanks 
    document.getElementById('feedback-3-thanks').hidden = false;
    const reflow = document.getElementById('feedback-3-thanks').offsetHeight; // Repaint the browser to enable transitions of newly shown element
    document.getElementById('feedback-3-thanks').classList.add('smooth-open');

}
