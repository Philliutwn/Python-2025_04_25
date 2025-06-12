document.addEventListener('DOMContentLoaded', function () {
    const accordionItems = document.querySelectorAll('.accordion-item');
    accordionItems.forEach(item => {
        const header = item.querySelector('.accordion-header');
        if (!header) { return; }
        header.addEventListener('click', () => {
            const isOpen = item.classList.contains('is-open');
            item.classList.toggle('is-open');
            header.setAttribute('aria-expanded', String(!isOpen));
        });
        if (item.classList.contains('is-open')) {
            header.setAttribute('aria-expanded', 'true');
        } else {
            header.setAttribute('aria-expanded', 'false');
        }
    });
});