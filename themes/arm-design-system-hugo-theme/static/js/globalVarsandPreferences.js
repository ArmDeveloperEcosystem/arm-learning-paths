var digitalData = {};


(() => {
    function hasStoredPreference(name) {
        try {
            return localStorage.getItem(name) !== null;
        } catch (_) {
            return false;
        }
    }

    if (hasStoredPreference('smallerWidth')) {
        const main = document.getElementById('main');
        const content = document.getElementById('all-content-div-margined');

        if (main) main.classList.remove('is-full-width');
        if (content) {
            content.classList.remove('u-margin-left-2');
            content.classList.remove('u-margin-right-2');
        }
    }

    if (hasStoredPreference('fullHeight')) {
        const globalNavigation = document.getElementById('global-nav-example-default');
        const expandedMasthead = document.getElementById('expanded-masthead');
        const footer = document.getElementById('arm-footer');
        const breadcrumbMasthead = document.getElementById('only-breadcrumb-masthead');

        if (globalNavigation) {
            globalNavigation.contextualData = [];
            globalNavigation.contextualIcons = [];
        }
        if (expandedMasthead) expandedMasthead.setAttribute('hidden', true);
        if (footer) footer.setAttribute('hidden', true);
        if (breadcrumbMasthead) breadcrumbMasthead.removeAttribute('hidden');
    }
})();


