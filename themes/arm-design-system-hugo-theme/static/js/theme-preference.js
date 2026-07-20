(function () {
    'use strict';

    var root = document.documentElement;
    var storageKey = 'theme';
    var activeTheme = readStoredTheme() || 'dark';

    root.setAttribute('data-theme-enabled', 'true');

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

    function updateToggle(theme) {
        var toggle = document.getElementById('theme-toggle');
        if (!toggle) return;

        var isDark = theme === 'dark';
        var icon = toggle.querySelector('[data-theme-toggle-icon]');
        var label = toggle.querySelector('[data-theme-toggle-label]');

        toggle.setAttribute('aria-pressed', String(isDark));
        toggle.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
        toggle.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';

        if (icon) icon.textContent = isDark ? '☀' : '☾';
        if (label) label.textContent = isDark ? 'Light mode' : 'Dark mode';
    }

    function notifyThemeChange(theme) {
        if (typeof window.CustomEvent !== 'function') return;

        document.dispatchEvent(new window.CustomEvent('learn-theme-change', {
            detail: { theme: theme },
        }));
    }

    function applyTheme(theme, persist, notify) {
        activeTheme = normalizeTheme(theme);
        root.setAttribute('theme', activeTheme);
        root.style.colorScheme = activeTheme;
        updateToggle(activeTheme);

        if (persist) storeTheme(activeTheme);
        if (notify) notifyThemeChange(activeTheme);
    }

    function initializeToggle() {
        var toggle = document.getElementById('theme-toggle');
        if (!toggle || toggle.getAttribute('data-theme-toggle-ready') === 'true') return;

        toggle.setAttribute('data-theme-toggle-ready', 'true');
        updateToggle(activeTheme);
        toggle.addEventListener('click', function () {
            applyTheme(activeTheme === 'dark' ? 'light' : 'dark', true, true);
        });
    }

    applyTheme(activeTheme, false, false);

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeToggle);
    } else {
        initializeToggle();
    }

    document.addEventListener('arm-top-navigation-ready', function () {
        applyTheme(activeTheme, false, false);
    });

    window.addEventListener('storage', function (event) {
        if (event.key !== storageKey) return;
        applyTheme(event.newValue === 'light' ? 'light' : 'dark', false, true);
    });
})();
