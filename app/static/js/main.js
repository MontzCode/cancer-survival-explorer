document.addEventListener('DOMContentLoaded', function () {
    const spinner = document.createElement('div');
    spinner.className = 'spinner-overlay';
    spinner.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(spinner);

    const links = document.querySelectorAll('nav a, a.card');
    links.forEach(function (link) {
        link.addEventListener('click', function () {
            spinner.style.display = 'flex';
        });
    });

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function () {
            spinner.style.display = 'flex';
        });
    }
});