function filter_LearningPath_card(card) {
    let to_hide = true;             // set as true by default; change to false if conditions apply

    // iterate over all active filters in the dom area; if this card matches ALL of the tags, keep shown
    const active_tags = document.getElementsByClassName('filter-facet');
    if (active_tags.length==0) { return false }        // Return already if no tags...no filtering neccecary 

    // create dictionary, grouping together tags by group
    // gropued_active_tags = {'group-subjects': [tag1,tag2], 'group-skill-level': [tag3]}
    // group_status        = {'group-subjects': true, 'group-skill-level': true}
    let grouped_active_tags = {};
    let group_status = {};

    for (tag of active_tags) {
        let all_tag_classes = tag.classList;
        for (c of all_tag_classes) {
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
        for (tag of grouped_active_tags[group_name]){
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
                // uncheck it. NOT WORKING
                //>>>>????????????????????????????????????????????????????? ADS issue
                checkbox_element.removeAttribute('checked');
            }
        });

    // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             results_to_hide = applySearchAndFilters(all_path_cards, value, 'paths'); // apply active search & filter terms to the specified divs
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

     display_tag = element.name;
     
     document.querySelector('#current-tag-bar').insertAdjacentHTML(
         'beforeend',
         `
         <ads-tag href="#" class="filter-facet u-margin-left-1/2 u-margin-top-1/2 u-margin-bottom-1/2 `+filter_group+`" id="filter-${tag}">
             <span class="u-flex u-flex-row u-align-items-center u-gap-1/2">
                 ${display_tag}
                 <a onclick="removeFacet('${tag}')">
                     <span class="fal fa-times-circle"></span>
                 </a>
             </span>
         </ads-tag>
         `
     );

     // Apply search and filters to current parameters
        // deal with ads promise
        document.getElementById('search-box').value().then((value) => { 
             results_to_hide = applySearchAndFilters(all_path_cards, value, 'paths'); // apply active search & filter terms to the specified divs
             hideElements(all_path_cards,results_to_hide);
             updateShownNumber();                  // Update UI telling how many are displayed
            },
        );
}






function scrollToTopIfApplicable(element) {
    // If OPEN expansion (has group tag) then scroll up to the top of the page softly
    for (c of element.className.split(' ')) {
        if (c == 'to-page-top') {
            // soft scroll up to the top of the page
            //document.body.scrollTop = 0; // For Safari
            //document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
            window.scrollTo({top: 0, behavior: 'smooth'});
            console.log(c)
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
                if (radio_btn.id != element.id) {
                    let tag = 'tag-'+radio_btn.id;
                    if (document.getElementById('filter-'+tag)) {
                        removeFacet('tag-'+radio_btn.id);
                    }
                }
            }
        }