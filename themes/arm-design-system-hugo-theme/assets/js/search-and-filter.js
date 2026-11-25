// filter-learning-paths.js
function updateURLWithFilters(active_tags_by_group) {
    // active_tags_by_group = {'group-subjects': [tag1,tag2], 'group-skill-level': [tag3]}
    // obtain tag name from each tag in each group
    let filters = {};
    for (let group_name in active_tags_by_group) {
        // if group_name not already in filters, add it
        let group = group_name.replace('group-','');
        if (!(group in filters)) {
            filters[group] = [];
        }
        // iterate over tags in this group
        for (let tag of active_tags_by_group[group_name]) {
            let tag_name = tag.id.replace('filter-tag-',''); // tag.id = filter-tag-databases   strip off 'filter-'            
            filters[group].push(tag_name);
        }
    }

    // Get any active searches too
    document.getElementById('search-box').value().then((value) => { 
        if (value) {
            filters['search'] = value;
        }

        // Finish processing filters and update URL
        const queryString = new URLSearchParams(filters).toString();
        const newUrl = `${window.location.pathname}?${queryString}`;
        
        // if newUrl is the same as the current URL, don't pushState
        const currentUrl = window.location.href.replace(window.location.origin, '');
        const newUrlPath = newUrl.replace(window.location.origin, '');
        if (newUrlPath === currentUrl) {
            return;
        }
    
        // This changes the URL in the address bar without reloading the page:
        history.replaceState({ filters }, "", newUrl); //replaceState or pushState if you don't want to keep the back button history
        
    });

  }

function filter_LearningPath_card(card) {
    let to_hide = true;             // set as true by default; change to false if conditions apply

    // iterate over all active filters in the dom area; if this card matches ALL of the tags, keep shown
    const active_tags = document.getElementsByClassName('filter-facet');
    if (active_tags.length==0) { 
        updateURLWithFilters({}); // clear filters from URL
        return false 
    }        // Return already if no tags...no filtering neccecary 

    // create dictionary, grouping together tags by group
    // gropued_active_tags = {'group-subjects': [tag1,tag2], 'group-skill-level': [tag3]}
    // group_status        = {'group-subjects': true, 'group-skill-level': true}
    let grouped_active_tags = {};
    let group_status = {};

    for (let tag of active_tags) {
        let all_tag_classes = tag.classList;
        for (let c of all_tag_classes) {
            if (c.includes('group-')) {
                let group_name = c;
                if (group_name in grouped_active_tags) {
                    // add tag to existing dict list
                    grouped_active_tags[group_name].push(tag);
                }
                else {
                    // create new dict list (and initalize group_status)
                    grouped_active_tags[group_name] = [tag];
                    group_status[group_name] = true;
                }
            }
        }
    }
    for (let group_name in grouped_active_tags) {
        // iterate over tags in this group
        for (let tag of grouped_active_tags[group_name]){
            // If card's classList contains any tag in this group (OR behavior), then don't hide
            let active_tag_name   = tag.id.replace('filter-',''); // tag.id = filter-tag-databases   strip off 'filter-'
            if (card.classList.contains(active_tag_name)) {
                // Don't hide, it matches a tag in this category (and we can break as we already know we're set in this group)
                group_status[group_name] = false;
                break
            }
        }
      }
    
    // If there are any trues, that means that this path should be hidden. If all falses, then it should be shown (to_hide = false)
    if(!Object.values(group_status).includes(true)){ to_hide = false; }

    // Send to URL
    updateURLWithFilters(grouped_active_tags);

    /* OLD implementation of ANDS only
    for (tag of active_tags) {
        let active_tag_name   = tag.id.replace('filter-',''); // tag.id = filter-tag-databases   strip off 'filter-'
        if (card.classList.contains(active_tag_name)) {
            // DO NOT hide this card as it matches an active tag!
            to_hide = false;
        }        
        else { // If here, this tag isn't in the card's classlist (not a match)
            // If the same group is present, OR behavior applies, so don't hide it.
                // CARD:   tag-ci-cd   tag-web        tag-linux
                // TAG:    tag-ci-cd   group-subjects
            
            //Return true, meaning hide it
            return true
        }
    }
    */

    return to_hide
}
function removeFacet(tag) {
    const all_path_cards = document.querySelectorAll('div.search-div');
     //////// Remove Facet
     document.getElementById('filter-'+tag).remove();

    ////////// Uncheck checkbox if applicable
        // get status of checkbox (true for checked, false for unchecked)
        const checkbox_element = document.querySelectorAll('ads-checkbox.'+tag)[0]
        checkbox_element.value().then((value) => { 
            if (value === true) {
                checkbox_element.checked = false;
                checkbox_element.checked = undefined;  // Fix came from ADS team, resolving this issue. Not sure why it works, but it does!
            }
        });

    // Remove 'clear filters' command if no filters left 
    let active_facets = document.querySelectorAll('ads-tag.filter-facet');
    if (active_facets.length === 0) {
        document.getElementById('tag-clear-btn').hidden = true;
    }

    // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             let results_to_hide = applySearchAndFilters(all_path_cards, value, 'paths'); // apply active search & filter terms to the specified divs
             hideElements(all_path_cards,results_to_hide);
             updateShownNumber();                  // Update UI telling how many are displayed
            },
        );

}
function addFacet(element) {
    const all_path_cards = document.querySelectorAll('div.search-div');

     //////// Add Facet
     // Get 'tag' and 'display_tag' and filter_group
     let tag = null;
     let filter_group = null;

     const tags = element.classList.values();
     for (let t of tags) {
         if (t.includes('tag')) {
             tag = t;
             break;
         }
     };
     for (let t of tags) {
        if (t.includes('group')) {
            filter_group = t;
            break;
        }
    };


    // Make sure that this tag doesn't already exist (issue with ADS checkboxes, need to verify here otherwise we get repeating facets appearing)
    if (document.querySelectorAll('ads-tag#filter-'+tag).length > 0) {
        return //if it does, just leave without doing anything (no need, already exists)
    }


     let display_tag = element.name;
     document.querySelector('#current-tag-bar').insertAdjacentHTML(
         'beforeend',
         `
         <ads-tag href="#" class="filter-facet u-margin-left-1/2 u-margin-top-1/2 u-margin-bottom-1/2 `+filter_group+`" id="filter-${tag}">
             <span class="u-flex u-flex-row u-align-items-center u-gap-1/2">
                 <div class="filter-facet-display-name">${display_tag}</div>
                 <a onclick="removeFacet('${tag}')">
                     <span class="fal fa-times-circle"></span>
                 </a>
             </span>
         </ads-tag>
         `
     );

     // Show 'clear filters' command (if already shown this command does nothing.)
     document.getElementById('tag-clear-btn').hidden = false;


     

     // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             let results_to_hide = applySearchAndFilters(all_path_cards, value, 'paths'); // apply active search & filter terms to the specified divs
             hideElements(all_path_cards,results_to_hide);
             updateShownNumber();                  // Update UI telling how many are displayed
            },
        );
}
function turnOnFilters(filters_list) {
    // parse incoming list
    // try to get checkbox element matching the incoming filter request
    // addFacets for all relevent filters


    // parse list
    for (let filter of filters_list) {
        let filter_group = filter.split('=')[0];
        let filter_name = filter.split('=')[1];

        // get checkbox elements to check (mobile and desktop apperance) by 'data-urlized-name'
        let checkbox_elements = document.querySelectorAll("ads-checkbox[data-urlized-name='"+filter_name+"']");
        // if checkbox_elements are inside the correct group (via class  'group-os' or similar) verify the elements are in the group
        for (let element of checkbox_elements) {
            if (element.classList.contains("group-"+filter_group)) {
                // check the checkbox (ISSUES WITH ADS)
                element.checked = true;
                // add a facet
                addFacet(element);
            }
        }
    }

}
function clearAllFilters() {
    // call removeFacet on each tag
    let active_facets = document.querySelectorAll('ads-tag.filter-facet');
    for (let facet of active_facets) {
        let tag  = facet.id.replace('filter-',''); // tag.id = filter-tag-databases   strip off 'filter-'
        removeFacet(tag);
    }
}
function scrollToTopIfApplicable(element) {
    // If OPEN expansion (has group tag) then scroll up to the top of the page softly
    for (let c of element.className.split(' ')) {
        if (c == 'to-page-top') {
            // soft scroll up to the top of the page
            //document.body.scrollTop = 0; // For Safari
            //document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
            window.scrollTo({top: 0, behavior: 'smooth'});
            break
        }
    }
}
function filterHandler_LearningPaths(element) {
    /*      Called from ads-checkbox components themselves, triggered from a user press on checkbox        
                Update facets to appear
                Apply only updated filter to search results (show what isn't that matches & vice versa)
    */
        const all_path_cards = document.querySelectorAll('div.search-div');
       

    
        // get status of checkbox (true for checked, false for unchecked)
        element.value().then((value) => {
            if (value === true) {
                // add 'checked' value to html
               addFacet(element,all_path_cards);

               // scroll to page top if applicable
               scrollToTopIfApplicable(element);
            }
            else {
                //?????????????????????????????????????????????????????????????????????????
                // This is being called when there is no facet. Strange behaivor with checkbox value being set strangely
                // ADS team to fix this problem.
                let tag = null;
                const tags = element.classList.values();
                for (let t of tags) {
                    if (t.includes('tag')) {
                        tag = t;
                        break;
                    }
                };
               removeFacet(tag);
            }
        });
}
function filterHandler_radio_LearningPaths(element) {
    /*      Called from 'input' components themselves, triggered from a user press on radio
                Add Facet for correct one
                Remove all other facets
    */
        const all_path_cards = document.querySelectorAll('div.search-div');
        
        // Add facet
        addFacet(element,all_path_cards);

        // Remove all other subject facets
        const all_radio_btns_with_same_group = document.querySelectorAll('input.radio-group-'+element.name);
        for (let radio_btn of all_radio_btns_with_same_group) {
            if (radio_btn.id != element.getAttribute('data-urlized-name')) {
                let tag = 'tag-'+radio_btn.id;
                if (document.getElementById('filter-'+tag)) {
                    removeFacet('tag-'+radio_btn.id);
                }
            }
        }
}


// search-logic.js
// Tokenization, language aliases, 3-char prefix matching, and -term / NOT term
// exclusions aligned with assets/search-lab/engine.mjs.
const SEARCH_STOP_WORDS = new Set('a an and are at be can do for from how i in is it me my of on or the to using what with'.split(' '));
const SEARCH_ALIASES = new Map([['cpp', 'c++'], ['csharp', 'c#']]);

function tokenizeSearchText(text) {
    const tokens = String(text).toLowerCase().match(/[\p{L}\p{N}]+(?:[.+#-][\p{L}\p{N}+#]+)*#?/gu) || [];
    return tokens.map(token => SEARCH_ALIASES.get(token) || token);
}

function parseSearchQuery(raw_query) {
    if (!raw_query || !raw_query.trim()) {
        return { terms: [], excluded: [] };
    }
    // Parse exclusion operators before tokenizing the positive query.
    // Supports: -term and uppercase NOT term (lowercase "not" stays a literal word).
    const excludedRaw = [];
    const cleanQuery = raw_query
        .replace(/(^|\s)-(\S+)/g, (_, sp, w) => { excludedRaw.push(w); return sp; })
        .replace(/(^|\s)NOT\s+(\S+)/g, (_, sp, w) => { excludedRaw.push(w); return sp; })
        .replace(/(^|\s)NOT\s*$/g, '')
        .replace(/\s+/g, ' ')
        .trim();

    const excluded = [...new Set(tokenizeSearchText(excludedRaw.join(' ')).filter(Boolean))];
    const rawPositive = [...new Set(tokenizeSearchText(cleanQuery).filter(Boolean))];
    const filteredPositive = rawPositive.filter(t => !SEARCH_STOP_WORDS.has(t));
    // Fall back to raw positive tokens if the user only typed stop words (e.g. mid-typing).
    const terms = filteredPositive.length > 0 ? filteredPositive : rawPositive;

    return { terms, excluded };
}

function getCardTokens(card) {
    if (!card._searchTokenCache) {
        const titleEl = card.querySelector('.search-title');
        const searchTextEl = card.querySelector('[data-search-text]');
        const combined = (titleEl ? titleEl.textContent : '') + ' ' + (searchTextEl ? searchTextEl.dataset.searchText : '');
        const uniqueTokens = [...new Set(tokenizeSearchText(combined))];
        card._searchTokenCache = {
            set: new Set(uniqueTokens),
            list: uniqueTokens
        };
    }
    return card._searchTokenCache;
}

function isCardExcluded(card, excluded) {
    if (!excluded || excluded.length === 0) {
        return false;
    }
    const { set: tokenSet } = getCardTokens(card);
    // Exclusions always use exact token matching (no prefix expansion).
    return excluded.some(ex => tokenSet.has(ex));
}

function searchByTitle(card, parsed) {
    // Search the card title and the data-search-text attribute (if present).
    // data-search-text is set by path-ads-card.html (description, who_is_this_for,
    // learning_objectives, prerequisites, author) and install-guides/list.html
    // (description, author).
    // - Exclusions (-term / NOT term): exact token match hides the card.
    // - Positive terms (AND behaviour): 1-2 char tokens require exact match
    //   (so "go" does not match "good"); 3+ char tokens allow exact or prefix match.
    if (!parsed || (parsed.terms.length === 0 && parsed.excluded.length === 0)) {
        return false; // show it
    }

    if (isCardExcluded(card, parsed.excluded)) {
        return true; // hide it
    }

    const { set: tokenSet, list: tokenList } = getCardTokens(card);
    const allMatched = parsed.terms.every(term => {
        if (tokenSet.has(term)) {
            return true;
        }
        if (term.length >= 3) {
            return tokenList.some(token => token.startsWith(term));
        }
        return false;
    });

    return !allMatched; // true = hide it, false = show it
}
function searchByAdditionalSearchTerm(card,search_word_array) {
    if (!search_word_array || search_word_array.length === 0) {
        return true;
    }
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
        // Parse URL query params using URLSearchParams so spaces (+) and encoded
        // characters like C++ (%2B%2B) decode accurately.
        const urlParams = new URLSearchParams(url_str);
        let search_str = '';
        let filters = [];
        for (const [key, value] of urlParams.entries()) {
            if (key === 'search') {
                search_str = sanitizeInput(value);
            }
            else if (value) {
                value.split(',').forEach(val => {
                    filters.push(sanitizeInput(`${key}=${val}`));
                });
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

// search-handling.js
function applySearchAndFilters(all_path_cards, search_string, page) {    
    // Skip search bits if no search string
    let skip_search = false;
    if ((typeof search_string) == 'undefined') {
        search_string='';
        skip_search=true; 
    }

    // Parse search query once (handles tokenization, aliases, stop words, and - / NOT exclusions)
    const parsed_query = parseSearchQuery(search_string);

    // store results to hide based on certain parameters
    let results_to_hide = [];

    for (let card of all_path_cards) {

        ////////////////////////////////////////////////////////////////
        // SEARCH
        if (!skip_search) {
            if (page=='paths') {
                if (searchByTitle(card,parsed_query)) { 
                    results_to_hide.push(card); // set card to be hidden
                }
            }

            if (page=='openfilter') {
                if (searchByTitle(card,parsed_query)) { 
                    results_to_hide.push(card); // set card to be hidden
                }
            }

            // Tool-based search only
            if (page=='tools') {
                if (isCardExcluded(card, parsed_query.excluded)) {
                    results_to_hide.push(card); // exclusions always take precedence
                }
                else if (searchByTitle(card,parsed_query) && searchByAdditionalSearchTerm(card,parsed_query.terms)) { 
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
    // Sanitize the input by only allowing safe query/filter characters through:
        // a-z, A-Z, 0-9, spaces
        // special characters: .=-+#_/ (supports C++, g++, C#, llama.cpp, -exclusions, AI/ML, perf_event_open, filter=value)
    let sanitized_str = potentially_unsafe_str.replaceAll(/[^a-zA-Z0-9 .=\-+#_/]+/g, "");

    return sanitized_str
}
function searchHandler_LearningPaths(search_string,filters_from_url_only) {
    // HANDLE if coming from ads search box (event.value) or URL (string)
    if (! (typeof search_string === 'string')) {
        search_string = search_string.value;
    }


    // if getting filters from URL, activate the filters instantly before any other processing
    if (filters_from_url_only) {
        turnOnFilters(filters_from_url_only);
    }
    
    // Sanitize the input
    search_string = sanitizeInput(search_string);

    const all_path_cards = document.querySelectorAll('div.search-div');
    // Apply search and filters to current parameters
    let results_to_hide = applySearchAndFilters(all_path_cards, search_string,'paths'); // apply active search & filter terms to the specified divs
   
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
    
    // Sanitize the input
    search_string = sanitizeInput(search_string);

    const all_path_cards = document.querySelectorAll('div.search-div');
    // Apply search and filters to current parameters
    let results_to_hide = applySearchAndFilters(all_path_cards, search_string,'tools'); // apply active search & filter terms to the specified divs
    // Update url
    updateURLWithFilters({})

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
    let results_to_hide = applySearchAndFilters(all_filter_boxes, search_string,'openfilter'); // apply active search & filter terms to the specified divs
   
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

// change-handler-search-hook.js
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
    else if (document.title.includes('Learning Paths') && !(document.title.includes('Home'))) {
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