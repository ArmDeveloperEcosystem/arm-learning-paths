// Handle search
document.addEventListener('arm-top-nav-search', function(event) {
    console.log('Search fired');
    
    var user_search_query = event.detail;
    console.log('Search Query:', user_search_query, encodeURIComponent(user_search_query));

    // Construct the search URL with the query parameter

    var developer_search_url = 'https://developer.arm.com/search#q=' + encodeURIComponent(user_search_query) + '&f-navigationhierarchiescontenttype=Learning%20Path&numberOfResults=48';

    // Redirect the user to the search results page in a new tab
    window.open(developer_search_url, '_blank');

});
