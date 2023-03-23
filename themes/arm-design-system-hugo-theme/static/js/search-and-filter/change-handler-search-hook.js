document.addEventListener("DOMContentLoaded", function () {
    // Assign inputChangeHandler to openfilter boxes (if present)
    const openfilter_search_box = document.getElementById('openfilter-search-box');
    if (openfilter_search_box) {
        openfilter_search_box.inputChangeHandler = searchHandler_OpenFilter;
    }
    

    // Assign inputChangeHandler to search box
    const search_box = document.getElementById('search-box');
    if (document.title.includes('Install Guides') | (document.title=='Arm Learning Paths')) {    // Tools page OR Homepage
        search_box.inputChangeHandler = searchHandler_Tools;    
    }
    else {
        search_box.inputChangeHandler = searchHandler_LearningPaths;
    }

    // Handle search term from URL
    let url_str = window.location.search;
    if (url_str.includes('search=')) {
        let search_string = parseParamsFromURL(url_str);

        // Call search handler to execute
        search_box.setAttribute('search-value',search_string);

        if (document.title.includes('Install Guides')) { searchHandler_Tools(search_string); }
        else {                                           searchHandler_LearningPaths(search_string); }
    }
  });
