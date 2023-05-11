function applySearchAndFilters(all_path_cards, search_string, page) {
    console.log('DEBUG: in applySearchAndFilters. page: ',page);
    
    // Skip search bits if no search string
    let skip_search = false;
    if ((typeof search_string) == 'undefined') {
        search_string='';
        skip_search=true; 
    }

    // Filter search term
    const search_word_array = search_string.toLowerCase().split(" ");   // 'MongoDB Arm Neoverse-N1' --> ['mongodb','arm','neoverse-n1']

    // store results to hide based on certain parameters
    let results_to_hide = [];

    for (let card of all_path_cards) {

        ////////////////////////////////////////////////////////////////
        // SEARCH
        if (!skip_search) {
            if (page=='paths') {
                if (searchByTitle(card,search_word_array)) { 
                    results_to_hide.push(card); // set card to be hidden
                }
            }

            if (page=='openfilter') {
                if (searchByTitle(card,search_word_array)) { 
                    results_to_hide.push(card); // set card to be hidden
                }
            }

            // Tool-based search only
            if (page=='tools') {
                console.log('DEBUG: in applySearchAndFilters. in tools area, searching array: ',search_word_array);
                if (searchByTitle(card,search_word_array) && searchByAdditionalSearchTerm(card,search_word_array)) { 
                    results_to_hide.push(card); // set card to be hidden
                }
            }
        }

        ////////////////////////////////////////////////////////////////
        // FILTER
        if (page=='paths' | null) { // page may be undefined, handel for that if coming from learning pahts area
            if (filter_LearningPath_card(card)) { // if we get back non-null from function, the card should be hidden
                results_to_hide.push(card); // set card to be hidden
            }
        }

    }
    return results_to_hide
}


function sanitizeInput(potentially_unsafe_str) {
    // Sanitize the input by only allowing the following characters through, replacing all others with nothing:
        // a-z
        // A-Z
        // 0-9 digits
        // special characters: .-=
            // - very common in code
            // = needed for param filtering to work easily in parseParamsFromURL
    let sanitized_str = potentially_unsafe_str.replaceAll(/[^a-z A-Z 0-9 .=-]+/g, "");

    return sanitized_str
}


function searchHandler_LearningPaths(search_string,filters_from_url_only) {
    // HANDLE if coming from ads search box (event.value) or URL (string)
    if (! (typeof search_string === 'string')) {
        search_string = search_string.value;
    }
    console.log('DEBUG: in searchHandler_LPs. Search_string: ',search_string,sanitizeInput(search_string));


    // if getting filters from URL, activate the filters instantly before any other processing
    if (filters_from_url_only) {
        turnOnFilters(filters_from_url_only);
    }
    
    // Sanitize the input
    search_string = sanitizeInput(search_string);

    const all_path_cards = document.querySelectorAll('div.search-div');
    // Apply search and filters to current parameters
    results_to_hide = applySearchAndFilters(all_path_cards, search_string,'paths'); // apply active search & filter terms to the specified divs
   
    // Hide specified elements
    hideElements(all_path_cards,results_to_hide);

    // Update UI telling how many are displayed
    updateShownNumber();
}



function searchHandler_Tools(search_string) {
    // HANDLE if coming from ads search box (event.value) or URL (string)
    if (! (typeof search_string === 'string')) {
        search_string = search_string.value;
    }
    console.log('DEBUG: in searchHandler_Tools. Search_string: ',search_string,sanitizeInput(search_string));

    
    // Sanitize the input
    search_string = sanitizeInput(search_string);

    const all_path_cards = document.querySelectorAll('div.search-div');
    // Apply search and filters to current parameters
    results_to_hide = applySearchAndFilters(all_path_cards, search_string,'tools'); // apply active search & filter terms to the specified divs
   
    // Hide specified elements
    hideElements(all_path_cards,results_to_hide);

    // Update UI telling how many are displayed
    updateShownNumber();
}


function searchHandler_OpenFilter(search_string) {
    // HANDLE if coming from ads search box (event.value) or URL (string)
    if (! (typeof search_string === 'string')) {
        search_string = search_string.value;
    }

    // Sanitize the input
    search_string = sanitizeInput(search_string);

    const all_filter_boxes = document.querySelectorAll('div.openfilter-search-div'); 

    // Apply search and filters to current parameters
    results_to_hide = applySearchAndFilters(all_filter_boxes, search_string,'openfilter'); // apply active search & filter terms to the specified divs
   
    // Hide specified elements
    hideElements(all_filter_boxes,results_to_hide);

    // Update UI telling how many are displayed
    updateShownNumber('openfilter-');
    
}



function searchSubmit_Tools(evt) {
    if (evt.value == null){
        window.location.href = "/install-guides/?search=";
    }
    else {
        const safe_search_string = sanitizeInput(evt.value);
        const safe_formatted_search_string = encodeURIComponent(safe_search_string);
        window.location.href = "/install-guides/?search="+safe_formatted_search_string;
    }
}
