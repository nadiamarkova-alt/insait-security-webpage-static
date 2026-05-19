document.addEventListener('DOMContentLoaded', function () {
    var navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    var observer = new IntersectionObserver(
        function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
    );

    document.querySelectorAll('.animate-on-scroll').forEach(function (el) {
        observer.observe(el);
    });

    var yearDividers = document.querySelectorAll('.year-divider');
    yearDividers.forEach(function (divider) {
        divider.classList.add('animate-on-scroll');
        observer.observe(divider);
    });

    var themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            var current = localStorage.getItem('theme') || 'v1';
            var next = current === 'v2' ? 'v1' : 'v2';
            localStorage.setItem('theme', next);
            var link = document.getElementById('theme-style');
            if (link) {
                var isV2 = next === 'v2';
                link.href = isV2
                    ? 'static/css/style-v2.css'
                    : 'static/css/style.css';
            }
        });
    }

    var savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'v2') {
        var link = document.getElementById('theme-style');
        if (link) {
            link.href = 'static/css/style-v2.css';
        }
    }
});