/* Used in learning path navigation view */
/* Used in learning path list view */

function mobileFilterClickedSearch(btn_element) {
    if (btn_element.classList.contains('is-open')) {
        // Close filter options.
        
        btn_element.classList.remove("is-open"); // Edit btn element class
        btn_element.classList.remove("lg:u-show"); 

        btn_element.getElementsByTagName('i')[0].classList.remove('fa-times'); // alter filter icon
        btn_element.getElementsByTagName('i')[0].classList.add('fa-filter');  

        document.getElementById('filters-container').classList.add('u-hide');         // alter u-hide class on id 'filters-container' div to show filters
    }
    else {
        // Open filter options.
        
        btn_element.classList.add("is-open");
        btn_element.classList.add("lg:u-show"); 
        
        btn_element.getElementsByTagName('i')[0].classList.remove('fa-filter'); // alter filter icon
        btn_element.getElementsByTagName('i')[0].classList.add('fa-times');  

        document.getElementById('filters-container').classList.remove('u-hide');         // alter u-hide class on id 'filters-container' div to show filters
    }
}




function mobileFilterClickedContent(btn_element) {
    if (btn_element.classList.contains('is-open')) {
        // Close filter options.
        
        btn_element.classList.remove("is-open"); // Edit btn element class
        btn_element.classList.remove("lg:u-show"); 

        btn_element.getElementsByTagName('i')[0].classList.remove('fa-times'); // alter filter icon
        btn_element.getElementsByTagName('i')[0].classList.add('fa-list');  

        document.getElementById('filters-container').classList.add('u-hide');         // alter u-hide class on id 'filters-container' div to show filters
    }
    else {
        // Open filter options.
        
        btn_element.classList.add("is-open");
        btn_element.classList.add("lg:u-show"); 
        
        btn_element.getElementsByTagName('i')[0].classList.remove('fa-list'); // alter filter icon
        btn_element.getElementsByTagName('i')[0].classList.add('fa-times');  

        document.getElementById('filters-container').classList.remove('u-hide');         // alter u-hide class on id 'filters-container' div to show filters
    }
}