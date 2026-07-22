(function () {
    'use strict';

    var root = document.documentElement;
    var storageKey = 'theme';
    var activeTheme = readStoredTheme() || 'dark';

    function normalizeTheme(theme) {
        return theme === 'light' ? 'light' : 'dark';
    }

    function readStoredTheme() {
        try {
            var storedTheme = window.localStorage.getItem(storageKey);
            return storedTheme === 'light' || storedTheme === 'dark' ? storedTheme : null;
        } catch (_) {
            return null;
        }
    }

    function storeTheme(theme) {
        try {
            window.localStorage.setItem(storageKey, theme);
        } catch (_) {
            // Theme switching still works when storage is unavailable.
        }
    }

    function updateNavigation(theme) {
        var navigation = document.querySelector('arm-top-navigation');

        if (navigation) {
            navigation.setAttribute('theme', theme);
        }

        if (typeof window.CustomEvent === 'function') {
            document.dispatchEvent(new window.CustomEvent('arm-footer-theme', {
                detail: theme === 'light',
            }));
        }
    }

    function notifyThemeChange(theme) {
        if (typeof window.CustomEvent !== 'function') return;

        document.dispatchEvent(new window.CustomEvent('learn-theme-change', {
            detail: { theme: theme },
        }));
    }

    function applyTheme(theme, persist, notify, updateGlobalComponents) {
        activeTheme = normalizeTheme(theme);
        root.setAttribute('theme', activeTheme);
        root.style.colorScheme = activeTheme;

        if (persist) storeTheme(activeTheme);
        if (updateGlobalComponents) updateNavigation(activeTheme);
        if (notify) notifyThemeChange(activeTheme);
    }

    function initializeNavigation() {
        applyTheme(activeTheme, false, false, true);
    }

    applyTheme(activeTheme, false, false, false);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeNavigation);
    } else {
        initializeNavigation();
    }

    document.addEventListener('arm-top-navigation-ready', initializeNavigation);

    document.addEventListener('arm-theme', function (event) {
        applyTheme(event.detail === true ? 'light' : 'dark', true, true, false);
    });

    window.addEventListener('storage', function (event) {
        if (event.key !== storageKey) return;
        applyTheme(event.newValue === 'light' ? 'light' : 'dark', false, true, true);
    });
})();
