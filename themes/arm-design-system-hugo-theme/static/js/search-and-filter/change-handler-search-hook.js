document.addEventListener("DOMContentLoaded", function () {
    // Assign inputChangeHandler to openfilter boxes (if present)
    const openfilter_search_box = document.getElementById('openfilter-search-box');
    if (openfilter_search_box) {
        openfilter_search_box.inputChangeHandler = searchHandler_OpenFilter;
    }
    

    // Assign inputChangeHandler to search box
    const search_box = document.getElementById('search-box');
    if (document.title.includes('Install Guides')) {
        search_box.inputChangeHandler = searchHandler_Tools;    
    }
    else {
        search_box.inputChangeHandler = searchHandler_LearningPaths;
    }

    // Handle search term from URL
    let url_str = window.location.search;
    if (url_str.includes('?')) {
        let params = parseParamsFromURL(url_str);
        let search_string = params[0]
        let filters_list  = params[1]
        // Call search handler to execute
        search_box.setAttribute('search-value',search_string);

        if (document.title.includes('Install Guides')) {     searchHandler_Tools(search_string); }
        else {                                               searchHandler_LearningPaths(search_string,filters_list); }
    }
  });
