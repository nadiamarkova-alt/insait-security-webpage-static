document.addEventListener('DOMContentLoaded', function () {
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
    );

    document.querySelectorAll('.animate-on-scroll').forEach((el) => {
        observer.observe(el);
    });

    const yearDividers = document.querySelectorAll('.year-divider');
    yearDividers.forEach((divider) => {
        divider.classList.add('animate-on-scroll');
        observer.observe(divider);
    });

    const themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const current = getCookie('theme') || 'v1';
            const next = current === 'v2' ? 'v1' : 'v2';
            document.cookie = 'theme=' + next + '; path=/; max-age=' + 60 * 60 * 24 * 365;
            const link = document.getElementById('theme-style');
            if (link) {
                const isV2 = next === 'v2';
                link.href = isV2
                    ? '/static/css/style-v2.css'
                    : '/static/css/style.css';
            }
        });
    }

    function getCookie(name) {
        const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
        return match ? match[2] : null;
    }

    const savedTheme = getCookie('theme');
    if (savedTheme === 'v2') {
        const link = document.getElementById('theme-style');
        if (link) {
            link.href = '/static/css/style-v2.css';
        }
    }
});
