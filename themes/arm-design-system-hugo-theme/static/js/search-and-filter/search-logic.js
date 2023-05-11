function searchByTitle(card,search_word_array) {   
    // Title of learning path --> title must include ALL search terms (any order or case)
    let card_title = card.querySelector('.search-title').innerHTML.toLowerCase();
    var title_serach_match = search_word_array.every(item => card_title.includes(item));
    if (!title_serach_match) {
        return true // hide it
    }
    else {
        return false // show it
    }
}

function searchByAdditionalSearchTerm(card,search_word_array) {
    console.log('DEBUG: in searchByAdditionalSearchTerm. in tools area, searching array: ',search_word_array);
    let result = true;
    
    let search_word_dash = search_word_array.join("-")
    let card_classes = card.classList;

    card_classes.forEach(function (term, i) {    
        if (term.startsWith('term-')) {
            if (search_word_dash == term.replace('term-','')) {
                result=false; //show it
            }
        }
    });
    return result
}


function parseParamsFromURL(url_str) {
        // Split by & and get search string ('search=') and filters ('filter-')
        let url_params = url_str.split('&');

        // iterate over all url_params and get search / filter params. Sanitize and decode them.
        let search_str = '';
        let filters = [];
        for (let param of url_params)
        {
            if (param.includes('search=')) {
                search_str = sanitizeInput(decodeURIComponent(param.replace('?','').replace('search=','')));
            }
            else if (param.includes('-filter=')) {
                filters.push(sanitizeInput(decodeURIComponent(param.replace('?','').replace('-filter=','='))));
            }
        }

        return [search_str,filters]
}


function hideElements(all_path_cards,results_to_hide) {

    // Hide elements in array (and actively show all OTHER elements)
    for (let card of all_path_cards) {
        if (results_to_hide.includes(card)) { 
            // Hide card
            card.setAttribute('hidden',true);
        }
        else {
            // Show card
            card.removeAttribute('hidden');
        }
    }
}


function updateShownNumber(prepend_id_string) {
    // prepend_id_string helps handle when there are 2 or more of these components on the same screen; can route to the correct place.
    if (prepend_id_string == null){     // if null or undefined, as with most situations (not openfilter)
        prepend_id_string = ''
    }

    // Update UI telling how many are displayed
    let current_num = document.getElementById(prepend_id_string+'currently-shown-number').innerHTML;
    let total_num = document.getElementById(prepend_id_string+'total-shown-number').innerHTML;
    var hidden_paths = document.querySelectorAll('div.'+prepend_id_string+'search-div[hidden]:not([hidden=""])');

    // adjust string length when open filter (not sure why needed currently)
    let paths_hidden = hidden_paths.length;
    if (prepend_id_string == 'openfilter-') {
        paths_hidden = hidden_paths.length /2;
    }

    document.getElementById(prepend_id_string+'currently-shown-number').innerHTML = parseInt(total_num) - paths_hidden;
}


