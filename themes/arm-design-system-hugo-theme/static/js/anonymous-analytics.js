
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

        -   facet-interaction
                Attributes tracked:
                    - facet-active-names    --> add comma-seperated facets as they get added, including group. Examples:  'subject:CI-CD'     'subject:CI-CD,subject:ML'      'subject:CI-CD,Operating System:Linux'
                    - search-current-query  --> add current search query; done after blur of search query      
        
        -   search-interaction
                Attributes tracked:
                    - search-current-query  --> add current search query; done after blur of search query    
                    
        -   feedback-interaction
                Attributes tracked:
                    - feedback-type         --> either 'star-rating' or 'reason'
                    - feedback-content      --> specifies the feedback. Star-rating will be 1-5, Reason will be a string (from a limited choice set, not free text) 
        
*/

function trackStarRating(rating) {
    // Send tracking data             
    _satellite.track('feedback-interaction', {   
        'feedback-type' : 'star-rating',
        'feedback-contetn': rating
    }); 
}

function trackChoiceFeedback(feedback_multiple_choice_answer) {
    // Send tracking data                
    _satellite.track('feedback-interaction', {   
        'feedback-type' : 'reason',
        'feedback-contetn': feedback_multiple_choice_answer
    }); 
}


function trackSearchInteraction() {
    // Get current search term
    // Send tracker  

    // Get search query (inside promise, continue the rest of this inside the promise)
    document.getElementById('search-box').value().then((value) => { 
        let current_search = value;

        // Send tracking data                
        _satellite.track('search-interaction', {   
            'search-current-query' : current_search
        }); 
    });
}


function trackFacetInteraction(){
    // Get active filters
    // Get current search term
    // Send tracker

    // Get all active filters, condense into the following str format: 'subject:CI-CD,subject:ML,Operating System:Linux'  
    let formatted_active_filters = ''
    const active_tags = document.getElementsByClassName('filter-facet');
    if (active_tags.length==0) { 
        return false         // Return already if no tags...no firing event neccecary
    }
    else {  
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

        // Send tracking data  
        _satellite.track('facet-interaction', {   
            'facet-active-names'   : formatted_active_filters,
            'search-current-query' : current_search
        }); 
    });
}




function trackHeaderInteraction(type,name){
    // type = 'header-mainnav-clicks' or 'header-subnav-clicks' or 'header-social-clicks' or 'header-other-clicks' or 'header-breadcrumb-clicks'
    // name = like 'Theme change' or 'Discord', etc.
    _satellite.track('content-interaction', {   
        'data-track-type'     : type,
        'data-track-location' : 'global-nav',
        'data-track-name'     : name
    });
}


function doneTyping(search_str) {
    //console.log('send',search_str);

    // Send tracking data   
    _satellite.track('lp_search', {   
        'lp_search_query' : search_str
    }); 
}

function attachPageFindSearchTracker() {
    let main_search_bar = document.getElementById('search');
    let search_input = main_search_bar.querySelector('input[type="text"]')

    var typingTimer;
    var doneTypingInterval = 2000; // Time in ms (2 seconds)
    
    // Add timer-based listener on main search bar
    main_search_bar.addEventListener('input', function() {
        clearTimeout(typingTimer); // Clear the previous timer
        typingTimer = setTimeout(() => doneTyping(search_input.value), doneTypingInterval);
    });


    // Add click-based listener on results using event deligation 
    main_search_bar.addEventListener('click', function(event) {
        if (event.target.classList.contains('pagefind-ui__result-link')) {
            //console.log('send',search_input.value,event.target.href)
            
            // Send tracking data                
            _satellite.track('lp_search_result_click', 
                {
                    lp_search_query : search_input.value,       // search string value
                    lp_search_result_name: event.target.href    // URL of page we are going to
                }
            );
        }
    });

    /* document.getElementById('search').addEventListener('hover', function(event) {
        if (event.target.classList.contains('pagefind-ui__result-link')) {
            // Get the search input value
            console.log('Result clicked for search value: ', search_input.value);
    
            // Perform your desired actions
        }
    });
    */

}


    // Go page by page, and assign the analytics tracker event component to appropriate ares.


    // wait for all DOM elements to be loaded first, then can assign event listeners to them.
    document.addEventListener("DOMContentLoaded", function() {  
        let current_path = window.location.pathname;
        let depth_of_path= current_path.split('/').length - 1 // Get number of '/' in the string; will help identify where we are in the heirarcy


        //
        //  Header 
        //  ===================
        // breadcrumbs
        let breadcrumbs  = document.getElementById('breadcrumb-element');
        for (let crumb of breadcrumbs.children) {
            let crumb_name = crumb.innerText;
            crumb.addEventListener("click", () => {   trackHeaderInteraction('header-breadcrumb-clicks',crumb_name);        });    
        }




        //
        //  Homepage
        //  ===================
        if (current_path == '/') {
            /* Assign to the following components:
                    0. Contribute button
                    1. Each main LP category card
                    2. Search bar
            */

            // 0) Contribute button 
            let contribute_btn = document.getElementById('contribute-btn');
            contribute_btn.addEventListener("click", () => {
                _satellite.track('content-interaction', {   
                    'data-track-type'     : 'Homepage CTAs',
                    'data-track-location' : 'CTA',
                    'data-track-name'     : 'contribute-btn'
                });
            });


            // 1) Learning Path category card
            let main_category_cards = document.getElementsByClassName('main-topic-card');
            for (let card of main_category_cards) {
                let category_name = card.id;
                card.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'Homepage Categories',
                        'data-track-location' : 'list-card',
                        'data-track-name'     : category_name
                    });
                });
            }

            // 2) Search bar
            // This takes place in the attachPageFindSearchTracker function, as it must 
            //   be called after the pagefind UI component is created dynamically.
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
            for (let facet of filter_facet_elements) {
                facet.addEventListener("click", () => {
                    trackFacetInteraction();                            
                });
            }


            // 3) Learning Path cards
            let learning_path_card = document.querySelectorAll('.path-card:not(.global-nav-path-card)');        // Exclude global nav cards, if existant.
            for (let card of learning_path_card) {
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



        //
        //  Learning Path page
        //  ===================
        else if ( ( (depth_of_path == 4) | (depth_of_path == 5) ) & (current_path.includes('/learning-paths/')) ) {
            /* Assign to the following components:
                    0. Onload detection
                    1. Tags (on Intro page)
                    2. Feedback (on Next Steps page)
                    3. Share (on Next Steps page)
                    4. CTAs (on Next Steps page)
                    5. Further Reading links (on Next Steps page)
            */
            
                    
           // 0) onload digital data setting
           let lp_title = document.getElementById('learning-path-title').innerText;
           let lp_step = document.getElementById('learning-path-step-active').innerText.trim();
           let lp_step_num = document.getElementById('learning-path-step-active').getAttribute('data-step-num');
           let lp_category = current_path.split('/')[2];

            // specific to intro page only; 
            if (document.getElementById('skill-level')) {
                let lp_skill_level = document.getElementById('skill-level').innerText.trim();
                let lp_reading_time = document.getElementById('reading-time').innerText.trim();
                let lp_last_updated = document.getElementById('last-updated').innerText.trim();
                let lp_author = document.getElementById('author').innerText.trim();
                let lp_tag_elements = document.querySelectorAll('#tags-for-content ads-tag');
                let lp_tags = ''
                for (let ele of lp_tag_elements) {
                     lp_tags = lp_tags + ',' + ele.innerText.trim()
                }
                lp_tags = lp_tags.replaceAll(',,',''); // remove extra ,,


                // send digital data
                digitalData.learningPath = {
                    pageInfo: {
                        learningPathName: lp_title, 
                        learningTabName: lp_step,
                        pageNumber: "page " +lp_step_num,
                        learningPathCategory: lp_category,
                        skillLevel: lp_skill_level,
                        readingTime: lp_reading_time,
                        lastUpdated: lp_last_updated,
                        learningPathAuthor: lp_author,
                        learningPathTags: lp_tags
                    }
                };
            }
            else {
                // send smaller digital data
                digitalData.learningPath = {
                    pageInfo: {
                        learningPathName: lp_title, 
                        learningTabName: lp_step,
                        pageNumber: "page " +lp_step_num,
                        learningPathCategory: lp_category
                    }
                };
            }



            


            // 1) Tags
            let tag_elements = document.querySelectorAll('ads-tag');  
            for (let tag of tag_elements) {
                tag.addEventListener("click", () => {
                    let tag_name = (tag.innerText || tag.textContent).trim();
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'page-tag-clicks',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : tag_name
                    });
                });
            }

            // REMOVED NOW THAT REVIEW PAGE IS REMOVED. SAFE TO TAKE OUT.
            // 2) Review check answer btn and answers
            /*
            let check_answer_btn = document.getElementById('check-answer-btn'); 
            if (check_answer_btn) {
                // check answer button
                check_answer_btn.addEventListener("click", () => {
                    // button was pressed
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-review-check-answer-button',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : 'Review - Check Answer button'
                    });

                    // current checked answers
                    let selected_answers = '';
                    let checked_boxes = document.querySelectorAll('input:checked');
                    for (let box of checked_boxes) {
                        // what question?
                        let question_number = box.getAttribute('name'); // question-1

                        // what answer?
                        let id_to_name = box.getAttribute('id');
                        let answer = document.querySelector('label[for="'+id_to_name+'"]').innerText;

                        // right or wrong?
                        let correct_or_not = 'incorrect'
                        if (box.parentElement.classList.contains('correct')) {
                            correct_or_not = 'correct'
                        }
                        selected_answers = selected_answers+',,'+   question_number+'::'+answer+'__'+correct_or_not;
                    }
                    // selected_answers = ,,question-1::False__correct,,question-2::False__incorrect
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-review-check-answer-checkboxes',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : selected_answers
                    });
                });
            } 
            */


            // 2) Feedback on Next Steps page
            // trackStarRating
            let stars = document.querySelectorAll('input[name=rating]');
            for (let star of stars) {
                star.addEventListener("click", () => {
                    trackStarRating(star.value);
                });
            }
                // trackChoiceFeedback
            let feedback_form = document.getElementById('feedback-choice-form');
            if (feedback_form) {
                feedback_form.addEventListener("submit", () => {
                    let feedback = document.querySelector('input[name="feedback-choice"]:checked').value;
                    trackChoiceFeedback(feedback);
                });
            } 

            // 3) Share         on Next Steps page
            let share_a = document.getElementsByClassName('share-button');
            for (let share_link of share_a) {
                share_link.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : 'share',
                        'data-track-name'     : share_link.getAttribute('name')     // will be 'LinkedIn' or 'Facebook' or 'Email' or similar.
                    });
                });
            }

            // 4) CTAs             on Next Steps page
            let cta_links = document.querySelectorAll('.next-step-cta');
            for (let cta of cta_links) {
                console.log('ctalink',cta);
                cta.addEventListener("click", () => {                   
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : cta.getAttribute('name'),               // either 'Event', 'DevProg', or 'Developer.arm.com'
                        'data-track-name'     : cta.getAttribute('data-event-name')     // if Event, gives event name, otherwise, null.
                    }); 
                })
            }

            // 5) Further Reading links on Next Steps page  
            let further_reading_links = document.querySelectorAll('#further-reading-div a');
            for (let link of further_reading_links) {
                link.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : 'further-reading-link'
                    });
                });
            }


                // metadata marking for similar learning paths, further reading, next learning path.
            /* All obsolete in new design
            let next_learning_path_link = document.getElementById('next-learning-path');
            if (next_learning_path_link) {
                next_learning_path_link.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : 'next-learning-path'
                    });
                });
            }

            let similar_lp_links = document.querySelectorAll('#similar-lp-div a');
            for (let link of similar_lp_links) {
                link.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : 'similar-learning-path-link'
                    });
                });
            }

            let explore_tag_links = document.querySelectorAll('#explore-tags-div ads-tag');
            for (let link of explore_tag_links) {
                link.addEventListener("click", () => {
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'learning-path-next-steps',
                        'data-track-location' : 'metadata',
                        'data-track-name'     : 'explore-tags-tag'
                    });
                });
            }
            */


            // 4a) Navitaion from navbar
            let in_learning_path_nav_bar_elements = document.getElementsByClassName('inner-learning-path-navbar-element');  
            for (let nav_bar_element of in_learning_path_nav_bar_elements) {
                nav_bar_element.addEventListener("click", () => {
                    let all_ele_classes = nav_bar_element.classList;
                    for (c of all_ele_classes) {
                        if (c.includes('-weight')) {
                            let weight = parseInt(c.replace('-weight',''))+1; // add 1 to index from 1, not 0
                            let human_name = (nav_bar_element.innerText || nav_bar_element.textContent).trim();
                            let track_str = 'page_number:'+weight+','+'page_name:'+human_name; 
                            _satellite.track('content-interaction', {   
                                'data-track-type'     : 'Learning Path navbar',
                                'data-track-location' : 'learning-path-nav',
                                'data-track-name'     : track_str
                            });
                            break // move to next element
                        }
                    }
                });
            }


            // 4b) Navigation forward/back on buttons
            let in_learning_path_nav_btn_elements = document.getElementsByClassName('inner-learning-path-navbtn-element');  
            for (let nav_btn_element of in_learning_path_nav_btn_elements) {
                nav_btn_element.addEventListener("click", () => {
                    let all_ele_classes = nav_btn_element.classList;
                    for (let c of all_ele_classes) {
                        if (c.includes('-weight')) {
                            let weight = parseInt(c.replace('-weight',''))+1; // add 1 to index from 1, not 0
                            let human_name='Introduction' // default name to Introduction, change if not 1st index
                            if (weight != 1) {
                                human_name = nav_btn_element.getAttribute('name'); // get human readable name
                            }
                            let track_str = 'page_number:'+weight+','+'page_name:'+human_name; 
                            _satellite.track('content-interaction', {   
                                'data-track-type'     : 'Learning Path navbtn',
                                'data-track-location' : 'learning-path-nav',
                                'data-track-name'     : track_str
                            });
                            break // move to next element
                        }
                    }
                });
            }
        }
        //
        //  Install Guide list page
        //  ===================
        else if ( (depth_of_path == 2) & (current_path.includes('/install-guides/')) ) {
            /* Assign to the following components:
                    1. Search box -> On deselect (left search bar, including clicking on content) or after 5 sec inactivity (scrolling down page, keep typing in search or delete search)
                    2. Install Guide cards
            */

            // 1) Search box
            let search_box = document.getElementById('search-box');
            search_box.addEventListener('blur', () => {
                trackSearchInteraction();
            });

            // 2) Install Guide cards
            let install_guide_card = document.querySelectorAll('.tool-card');
            for (let card of install_guide_card) {
                card.addEventListener("click", () => {
                    let card_title = card.querySelector('.search-title').innerHTML;
                    _satellite.track('content-interaction', {   
                        'data-track-type'     : 'Install Guide result card',
                        'data-track-location' : 'list-card',
                        'data-track-name'     : card_title 
                    });
                });
            }
        }
        //
        //  Install Guide page
        //  ===================
        else if ( ( (depth_of_path == 3) | (depth_of_path == 4) ) & (current_path.includes('/install-guides/')) ) {
            
            /* Assign to the following components:
                    1. Official Docs click
                    2. Feedback (on Next Steps page)
            */





           // 0) onload digital data setting, only on pages with metadata table
           if (document.getElementById('reading-time')) {
            let ig_title = document.getElementById('install-guide-title').innerText;
            let ig_reading_time = document.getElementById('reading-time').innerText.trim();
            let ig_last_updated = document.getElementById('last-updated').innerText.trim();
            let ig_author = document.getElementById('author').innerText.trim();
 
            digitalData.installGuide = {
                 pageInfo: {
                     installGuideName: ig_title, 
                     readingTime: ig_reading_time,
                     learningPathAuthor: ig_author,
                     lastUpdated: ig_last_updated
                }
            };

            // 1) Official Docs click
            let offical_doc_link = document.getElementById('official-doc-link');
            offical_doc_link.addEventListener("click", () => {
                _satellite.track('content-interaction', {   
                    'data-track-type'     : 'install-guide-next-steps',
                    'data-track-location' : 'metadata',
                    'data-track-name'     : 'official-docs-link'
                });
            });


            // 2) Feedback on Next Steps page
                // trackStarRating
            let stars = document.querySelectorAll('input[name=rating]');
            for (let star of stars) {
                star.addEventListener("click", () => {
                    trackStarRating(star.value);
                });
            }
                // trackChoiceFeedback
            let feedback_form = document.getElementById('feedback-choice-form');
            if (feedback_form) {
                feedback_form.addEventListener("submit", () => {
                    let feedback = document.querySelector('input[name="feedback-choice"]:checked').value;
                    trackChoiceFeedback(feedback);
                });
            }
        } 
    }
});

    

    
