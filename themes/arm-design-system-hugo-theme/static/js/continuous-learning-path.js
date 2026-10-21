(function () {
    function init() {
        var sections = Array.from(document.querySelectorAll('.learning-path-section'));
        var links = Array.from(document.querySelectorAll('.continuous-learning-path .left-nav-pane a.a-tab, .continuous-learning-path a.content-individual-a-mobile'));
        if (!sections.length) return;

        function activate(id) {
            document.querySelectorAll('.continuous-learning-path #learning-path-step-active').forEach(function (heading) {
                heading.removeAttribute('id');
            });
            links.forEach(function (link) {
                var active = link.hash === '#' + id;
                link.querySelectorAll('.tab-row, .tab-right-card, .content-individual-mobile, .content-individual-txt-mobile').forEach(function (item) {
                    item.classList.toggle('active', active);
                    item.classList.toggle('inactive', !active);
                });
                if (active) {
                    link.setAttribute('aria-current', 'location');
                    var heading = link.querySelector('.tab-right-card-header');
                    if (heading) heading.id = 'learning-path-step-active';
                }
                else link.removeAttribute('aria-current');
            });
        }

        function update() {
            var current = sections[0];
            var threshold = Math.min(180, window.innerHeight * 0.3);
            sections.forEach(function (section) {
                if (section.getBoundingClientRect().top <= threshold) current = section;
            });
            activate(current.id);
        }

        var scheduled = false;
        function schedule() {
            if (scheduled) return;
            scheduled = true;
            requestAnimationFrame(function () {
                scheduled = false;
                update();
            });
        }
        window.addEventListener('scroll', schedule, { passive: true });
        window.addEventListener('resize', schedule);
        window.addEventListener('hashchange', schedule);
        function scrollToSection(id) {
            var section = document.getElementById(id);
            if (!section || !sections.includes(section)) return false;
            section.scrollIntoView({ behavior: 'smooth', block: 'start' });
            activate(id);
            return true;
        }

        // Keep the Learning Path URL stable for navigation and page-view analytics.
        window.scrollToLearningPathSection = scrollToSection;
        links.forEach(function (link) {
            link.addEventListener('click', function (event) {
                if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
                var id = decodeURIComponent(link.hash.slice(1));
                if (!document.getElementById(id)) return;
                event.preventDefault();
                scrollToSection(id);
            });
        });

        // Existing step URLs redirect with a fragment. Scroll there, then show
        // the canonical Learning Path URL without adding another history entry.
        if (window.location.hash) {
            var initialId = decodeURIComponent(window.location.hash.slice(1));
            if (scrollToSection(initialId)) {
                window.history.replaceState(window.history.state, '', window.location.pathname + window.location.search);
            }
        }
        update();
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
    else init();
})();
