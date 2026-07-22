import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const scriptPath = new URL('../../themes/arm-design-system-hugo-theme/static/js/theme-preference.js', import.meta.url);
const script = await readFile(scriptPath, 'utf8');

function createElement() {
    const attributes = new Map();

    return {
        style: {},
        getAttribute(name) {
            return attributes.has(name) ? attributes.get(name) : null;
        },
        setAttribute(name, value) {
            attributes.set(name, String(value));
        },
    };
}

function createEnvironment(options = {}) {
    const root = createElement();
    const navigation = createElement();
    const documentListeners = new Map();
    const windowListeners = new Map();
    const dispatchedEvents = [];
    const storedValues = new Map();
    const shadowElements = new Map();

    if (options.hasNavigationShadow) {
        navigation.shadowRoot = {
            appendChild(element) {
                shadowElements.set(element.id, element);
            },
            querySelector(selector) {
                return selector.startsWith('#') ? shadowElements.get(selector.slice(1)) || null : null;
            },
        };
    }

    if (options.storedTheme !== undefined) storedValues.set('theme', options.storedTheme);

    const document = {
        documentElement: root,
        readyState: options.readyState || 'complete',
        addEventListener(name, handler) {
            documentListeners.set(name, handler);
        },
        dispatchEvent(event) {
            dispatchedEvents.push(event);
        },
        createElement() {
            return createElement();
        },
        querySelector(selector) {
            return selector === 'arm-top-navigation' ? navigation : null;
        },
    };

    const localStorage = {
        getItem(key) {
            if (options.throwOnRead) throw new Error('Storage read blocked');
            return storedValues.has(key) ? storedValues.get(key) : null;
        },
        setItem(key, value) {
            if (options.throwOnWrite) throw new Error('Storage write blocked');
            storedValues.set(key, String(value));
        },
    };

    class CustomEvent {
        constructor(type, init) {
            this.type = type;
            this.detail = init.detail;
        }
    }

    const window = {
        CustomEvent,
        localStorage,
        addEventListener(name, handler) {
            windowListeners.set(name, handler);
        },
    };

    vm.runInNewContext(script, { document, window });

    return {
        dispatchedEvents,
        documentListeners,
        navigation,
        root,
        shadowElements,
        storedValues,
        windowListeners,
    };
}

test('defaults to dark when no preference exists', () => {
    const environment = createEnvironment();

    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.equal(environment.root.style.colorScheme, 'dark');
    assert.equal(environment.navigation.getAttribute('theme'), 'dark');
});

test('restores an explicit light preference', () => {
    const environment = createEnvironment({ storedTheme: 'light' });

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.root.style.colorScheme, 'light');
    assert.equal(environment.navigation.getAttribute('theme'), 'light');
});

test('restores an explicit dark preference', () => {
    const environment = createEnvironment({ storedTheme: 'dark' });

    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.equal(environment.storedValues.get('theme'), 'dark');
});

test('native navigation event updates the theme and preference', () => {
    const environment = createEnvironment();

    environment.documentListeners.get('arm-theme')({ detail: true });

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.storedValues.get('theme'), 'light');
    assert.equal(environment.dispatchedEvents.at(-1).detail.theme, 'light');
});

test('restricted storage does not block native theme switching', () => {
    const environment = createEnvironment({ throwOnRead: true, throwOnWrite: true });

    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.doesNotThrow(() => environment.documentListeners.get('arm-theme')({ detail: true }));
    assert.equal(environment.root.getAttribute('theme'), 'light');
});

test('navigation hydration reapplies the active theme', () => {
    const environment = createEnvironment({ storedTheme: 'light' });

    environment.root.setAttribute('theme', 'dark');
    environment.navigation.setAttribute('theme', 'dark');
    environment.documentListeners.get('arm-top-navigation-ready')();

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.navigation.getAttribute('theme'), 'light');
});

test('navigation hydration uses only the public theme attribute', () => {
    const environment = createEnvironment({ hasNavigationShadow: true, storedTheme: 'light' });

    assert.equal(environment.navigation.getAttribute('theme'), 'light');
    assert.equal(environment.shadowElements.size, 0);
});

test('storage events synchronize theme changes between tabs', () => {
    const environment = createEnvironment();

    environment.windowListeners.get('storage')({ key: 'theme', newValue: 'light' });

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.navigation.getAttribute('theme'), 'light');
    assert.equal(environment.dispatchedEvents.at(-1).detail.theme, 'light');
});
