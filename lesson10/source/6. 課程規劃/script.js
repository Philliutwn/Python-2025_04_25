document.addEventListener('DOMContentLoaded', function () {
    const tabContainer = document.querySelector('.tab-container');
    // In a real application, you would also have tab panels to show/hide.
    // const tabPanels = document.querySelectorAll('.tab-panel'); // Example

    if (tabContainer) {
        const tabs = tabContainer.querySelectorAll('.tab-item[role="tab"]');

        tabContainer.addEventListener('click', function (event) {
            const clickedTab = event.target.closest('.tab-item[role="tab"]');

            if (!clickedTab || clickedTab.getAttribute('aria-selected') === 'true') {
                return; // Click was not on a tab item or tab is already selected
            }

            // Deactivate all tabs
            tabs.forEach(tab => {
                tab.classList.remove('active');
                tab.setAttribute('aria-selected', 'false');
                // tab.setAttribute('tabindex', '-1'); // Optional: manage focus
            });

            // Activate the clicked tab
            clickedTab.classList.add('active');
            clickedTab.setAttribute('aria-selected', 'true');
            // clickedTab.setAttribute('tabindex', '0'); // Optional: manage focus
            // clickedTab.focus(); // Optional: move focus to the selected tab

            // Here you would typically show the associated tab panel
            // const panelId = clickedTab.getAttribute('aria-controls');
            // document.getElementById(panelId).hidden = false; // Example
        });
    }
});