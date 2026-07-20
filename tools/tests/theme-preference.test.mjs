import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const scriptPath = new URL('../../themes/arm-design-system-hugo-theme/static/js/theme-preference.js', import.meta.url);
const script = await readFile(scriptPath, 'utf8');

function createElement() {
    const attributes = new Map();
    const listeners = new Map();

    return {
        style: {},
        title: '',
        textContent: '',
        addEventListener(name, handler) {
            listeners.set(name, handler);
        },
        getAttribute(name) {
            return attributes.has(name) ? attributes.get(name) : null;
        },
        setAttribute(name, value) {
            attributes.set(name, String(value));
        },
        trigger(name) {
            const handler = listeners.get(name);
            if (handler) handler();
        },
    };
}

function createEnvironment(options = {}) {
    const root = createElement();
    const toggle = createElement();
    const icon = createElement();
    const label = createElement();
    const documentListeners = new Map();
    const windowListeners = new Map();
    const dispatchedEvents = [];
    const storedValues = new Map();

    if (options.storedTheme !== undefined) storedValues.set('theme', options.storedTheme);

    toggle.querySelector = (selector) => {
        if (selector === '[data-theme-toggle-icon]') return icon;
        if (selector === '[data-theme-toggle-label]') return label;
        return null;
    };

    const document = {
        documentElement: root,
        readyState: options.readyState || 'complete',
        addEventListener(name, handler) {
            documentListeners.set(name, handler);
        },
        dispatchEvent(event) {
            dispatchedEvents.push(event);
        },
        getElementById(id) {
            return id === 'theme-toggle' ? toggle : null;
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
        document,
        documentListeners,
        icon,
        label,
        root,
        storedValues,
        toggle,
        windowListeners,
    };
}

test('defaults to dark when no preference exists', () => {
    const environment = createEnvironment();

    assert.equal(environment.root.getAttribute('data-theme-enabled'), 'true');
    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.equal(environment.root.style.colorScheme, 'dark');
    assert.equal(environment.toggle.getAttribute('aria-pressed'), 'true');
    assert.equal(environment.toggle.getAttribute('aria-label'), 'Switch to light mode');
    assert.equal(environment.icon.textContent, '☀');
    assert.equal(environment.label.textContent, 'Light mode');
});

test('restores an explicit light preference', () => {
    const environment = createEnvironment({ storedTheme: 'light' });

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.root.style.colorScheme, 'light');
    assert.equal(environment.toggle.getAttribute('aria-pressed'), 'false');
    assert.equal(environment.toggle.getAttribute('aria-label'), 'Switch to dark mode');
});

test('restores an explicit dark preference', () => {
    const environment = createEnvironment({ storedTheme: 'dark' });

    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.equal(environment.storedValues.get('theme'), 'dark');
});

test('toggle updates the theme, preference, and accessible state', () => {
    const environment = createEnvironment();

    environment.toggle.trigger('click');

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.storedValues.get('theme'), 'light');
    assert.equal(environment.toggle.getAttribute('aria-pressed'), 'false');
    assert.equal(environment.toggle.getAttribute('aria-label'), 'Switch to dark mode');
    assert.equal(environment.icon.textContent, '☾');
    assert.equal(environment.label.textContent, 'Dark mode');
    assert.equal(environment.dispatchedEvents.at(-1).detail.theme, 'light');
});

test('restricted storage falls back to dark without blocking switching', () => {
    const environment = createEnvironment({ throwOnRead: true, throwOnWrite: true });

    assert.equal(environment.root.getAttribute('theme'), 'dark');
    assert.doesNotThrow(() => environment.toggle.trigger('click'));
    assert.equal(environment.root.getAttribute('theme'), 'light');
});

test('navigation hydration reapplies the active theme', () => {
    const environment = createEnvironment({ storedTheme: 'light' });

    environment.root.setAttribute('theme', 'dark');
    environment.documentListeners.get('arm-top-navigation-ready')();

    assert.equal(environment.root.getAttribute('theme'), 'light');
});

test('storage events synchronize theme changes between tabs', () => {
    const environment = createEnvironment();

    environment.windowListeners.get('storage')({ key: 'theme', newValue: 'light' });

    assert.equal(environment.root.getAttribute('theme'), 'light');
    assert.equal(environment.dispatchedEvents.at(-1).detail.theme, 'light');
});
