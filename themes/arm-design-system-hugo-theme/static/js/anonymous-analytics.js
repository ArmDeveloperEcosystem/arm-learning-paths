
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
        console.log(formatted_active_filters,current_search);              
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


    // Go page by page, and assign the analytics tracker event component to appropriate ares.


    // wait for all DOM elements to be loaded first, then can assign event listeners to them.
    document.addEventListener("DOMContentLoaded", function() {  
        let current_path = window.location.pathname;
        let depth_of_path= current_path.split('/').length - 1 // Get number of '/' in the string; will help identify where we are in the heirarcy
        
        //
        //  Homepage
        //  ===================
        if (current_path == '/') {
            /* Assign to the following components:
                    0. Contribute button
                    1. Each main LP category card
                    2. Tool install search box
                    3. Tool install 'see all' link         
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



        //
        //  Learning Path page
        //  ===================
        else if ( ( (depth_of_path == 4) | (depth_of_path == 5) ) & (current_path.includes('/learning-paths/')) ) {
            /* Assign to the following components:
                    0. Onload detection
                    1. Tags (only for intro and next step pages)
                    2. Review ('check answer' button)
                    2.5. Review (if all correct, add trigger for analytics somehow)
                    3. Feedback (on Next Steps page)
            */

                    
           // 0) onload digital data setting
           let lp_title = document.getElementById('learning-path-title').innerText;
           let lp_step = document.getElementById('learning-path-step-active').innerText;
           let lp_step_num = document.getElementById('learning-path-step-active').getAttribute('data-step-num');
          
           digitalData.learningPath = {
                pageInfo: {
                    learningPathName: lp_title, 
                    learningTabName: lp_step,
                    pageNumber: "page " +lp_step_num
                }
            };
            


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

            // 2) Review check answer btn and answers
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


            // 3) Feedback on Next Steps page
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
                    for (c of all_ele_classes) {
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



    });

    

    
    
    //
    //  Header (takes forever to load in client-side JS)
    //  ===================
    window.addEventListener('load', () => {
        //console.log('All site loaded.');
        let armTopNav = document.querySelector('arm-top-navigation');
        let globalNav = document.getElementById('global-nav-example-default');
        let breadcrumbs  = document.getElementById('breadcrumb-element');


        // top left header
        // let top_left_logo  = globalNav.shadowRoot.querySelector('.c-navigation-logo');
        // top_left_logo.addEventListener("click", () => {   trackHeaderInteraction('header-mainnav-clicks','hub-logo');        });   
        let logo_primary = armTopNav.shadowRoot.querySelector('.c-logo-arm-primary');
        let logo_secondary = armTopNav.shadowRoot.querySelector('.c-logo-arm-secondary');
        logo_primary.addEventListener("click", () => { trackHeaderInteraction('header-mainnav-clicks','arm-logo'); });
        logo_secondary.addEventListener("click", () => { trackHeaderInteraction('header-mainnav-clicks','hub-logo'); });


        // theme button
        //let theme_btn  = globalNav.shadowRoot.getElementById('global-nav-example-default:tab:theme');
        //theme_btn.addEventListener("click", () => {   trackHeaderInteraction('header-other-clicks','theme-change');        });   


        // contribute button
        // let contribute_btn  = document.getElementById('contribute-btn');
        // contribute_btn.addEventListener("click", () => {   trackHeaderInteraction('header-other-clicks','contribute-on-github');        });   


        // subnav buttons
        // let LP_categories  = globalNav.shadowRoot.getElementById('global-nav-example-default:tab:category1');
        // LP_categories.addEventListener("click", () => {   trackHeaderInteraction('header-subnav-clicks','learning-path-categories');        });   

        // let install_guides  = globalNav.shadowRoot.getElementById('global-nav-example-default:tab:category2');
        // install_guides.addEventListener("click", () => {   trackHeaderInteraction('header-subnav-clicks','install-guides');        });   

        
        // social links desktop
        let discord = armTopNav.shadowRoot.querySelector('.icon-discord');
        discord.addEventListener("click", () => { trackHeaderInteraction('header-social-clicks','discord'); });
        let reddit = armTopNav.shadowRoot.querySelector('.icon-reddit');
        reddit.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','reddit'); });
        let github = armTopNav.shadowRoot.querySelector('.icon-github');
        github.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','github'); });
        let twitter = armTopNav.shadowRoot.querySelector('.icon-twitter');
        twitter.addEventListener("click", () => { trackHeaderInteraction('header-social-clicks','twitter'); });
        let youtube = armTopNav.shadowRoot.querySelector('.icon-youtube');
        youtube.addEventListener("click", () => { trackHeaderInteraction('header-social-clicks','youtube'); });
        
        // social links mobile
        let mDiscord = armTopNav.shadowRoot.querySelector('.icon-mobile-discord');
        mDiscord.addEventListener("click", () => { trackHeaderInteraction('header-social-clicks','discord'); });
        let mReddit = armTopNav.shadowRoot.querySelector('.icon-mobile-reddit');
        mReddit.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','reddit'); });
        let mGithub = armTopNav.shadowRoot.querySelector('.icon-mobile-github');
        mGithub.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','github'); });
        let mTwitter = armTopNav.shadowRoot.querySelector('.icon-mobile-twitter');
        mTwitter.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','twitter'); });
        let mYoutube = armTopNav.shadowRoot.querySelector('.icon-mobile-youtube');
        mYoutube.addEventListener("click", () => {  trackHeaderInteraction('header-social-clicks','youtube'); });


        // breadcrumbs
        for (crumb of breadcrumbs.children) {
            let crumb_name = crumb.innerText;
            crumb.addEventListener("click", () => {   trackHeaderInteraction('header-breadcrumb-clicks',crumb_name);        });    
        }
    });
