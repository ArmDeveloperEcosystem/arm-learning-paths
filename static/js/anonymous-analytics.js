
/* These analytics are implemented to track 100% anonymous clicks, and will be used for improving the product ONLY.*/
/*

        What is tracked:

        -   content-interaction
                Attributes tracked:
                    - data-track-type       --> organizes by content type. All learning path cards have the same type, so to should 'futher reading' links, etc.
                    - data-track-location   --> organizes by location of click. Should be split into these categories only:
                        - global-nav        --> navigation links on the top bar should have this, as should footer components
                        - list-card         --> learning path and tool list cards should have these types
                        - learning-path-nav --> navigation buttons in the application: 'next' button, 'prev' button, left-hand navigation
                        - metadata          --> any metadata links; above LPs and installs, and in 'next steps' page
                        - content           --> all links from user-generated markdown should have this. the 'render-link.html' should implement this tracker
                    - data-track-name       --> specific name of the element, human readable to link behavior. A click on a learning path should render its title, etc. This is dynamic

        -   search-interaction
                Attributes tracked:
                    - facet-active-names    --> add comma-seperated facets as they get added, including group. Examples:  'subject:CI-CD'     'subject:CI-CD,subject:ML'      'subject:CI-CD,Operating System:Linux'
                    - search-current-query  --> add current search query; done after blur of search query      

*/


function trackSearchInteraction(){
    // Get active filters
    // Get current search term
    // Send tracker

    // Get all active filters, condense into the following str format: 'subject:CI-CD,subject:ML,Operating System:Linux'  
    let formatted_active_filters = ''
    const active_tags = document.getElementsByClassName('filter-facet');
    if (!(active_tags.length==0)) {  
        for (tag of active_tags) {
            let all_tag_classes = tag.classList;
            for (c of all_tag_classes) {
                if (c.includes('group-')) {
                    let group_name = c.replace('group-','');
                    //let facet_name = tag.id.replace('filter-tag-','');
                    let facet_name = tag.querySelector('.filter-facet-display-name').innerHTML;
                    formatted_active_filters = formatted_active_filters+','+group_name+':'+facet_name;
                    break // move to next tag
                }
            }
        }
    }
    formatted_active_filters = formatted_active_filters.replace(/^,/, ''); // replace first , with empty, if present

    // Get search query (inside promise, continue the rest of this inside the promise)
    document.getElementById('search-box').value().then((value) => { 
        let current_search = value;


        console.log(formatted_active_filters);
        console.log(current_search);

        // Send tracking data                
        _satellite.track('search-interaction', {   
            'facet-active-names'   : formatted_active_filters,
            'search-current-query' : current_search
        }); 
    });


}


    // Go page by page, and assign the analytics tracker event component to appropriate ares.


    // wait for all DOM elements to be loaded first, then can assign event listeners to them.
    document.addEventListener("DOMContentLoaded", function() {  
        let current_path = window.location.pathname;

        let depth_of_path= current_path.split('/').length - 1 // Get number of '/' in the string; will help identify where we are in the heirarcy
        console.log(current_path,depth_of_path);
        
        //
        //  Homepage
        //  ===================
        if (current_path == '/') {
            /* Assign to the following components:
                    1. Each main LP category card
                    2. Tool install search box
                    3. Tool install 'see all' link         
            */

            // 1) Learning Path category card
            let main_category_cards = document.getElementsByClassName('main-topic-card');
            for (card of main_category_cards) {
                card.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'Homepage Categories',
                        'data-track-location' : 'list-card',
                        'data-track-name'     : card.id 
                    });
                });
            }
        }



        //
        //  Learning Path list page
        //  ===================
        else if ( (depth_of_path == 3) & (current_path.includes('/learning-paths/')) ) {
            /* Assign to the following components:
                    1. Search box -> On deselect (left search bar, including clicking on content) or after 5 sec inactivity (scrolling down page, keep typing in search or delete search)
                    2. Facet boxes
                    3. Learning Path cards
                    4. Get started alert area        
            */

            // 1) Search box 
            let search_box = document.getElementById('search-box');
            search_box.addEventListener('blur', () => {
                trackSearchInteraction();
            });

            // 2) Facet boxes
            let filter_facet_elements = document.querySelectorAll('ads-checkbox');            
            for (facet of filter_facet_elements) {
                facet.addEventListener("click", () => {
                    trackSearchInteraction();
                });
            }


            // 3) Learning Path cards
            let learning_path_card = document.querySelectorAll('.path-card:not(.global-nav-path-card)');        // Exclude global nav cards, if existant.
            for (card of learning_path_card) {
                card.addEventListener("click", () => {
                    let card_title = card.querySelector('.search-title').innerHTML;
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'Learning Path result card',
                        'data-track-location' : 'list-card',
                        'data-track-name'     : card_title 
                    });
                });
            }
        }
      });




