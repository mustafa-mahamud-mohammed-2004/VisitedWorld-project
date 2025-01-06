document.addEventListener('DOMContentLoaded', function () {
    const toggleSwitch = document.getElementById('night-mode-toggle'); // Get the toggle switch
    const body = document.body; // Reference to the body element
    const logo = document.getElementById('logo'); // Reference to the logo element

    // Function to toggle dark mode
    const toggleDarkMode = () => {
        body.classList.toggle('dark-mode'); // Toggle the dark-mode class on body
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('dark-mode', 'enabled'); // Store preference in localStorage
        } else {
            localStorage.setItem('dark-mode', 'disabled'); // Store preference in localStorage
        }
    };

    // Check localStorage when the page loads
    if (localStorage.getItem('dark-mode') === 'enabled') {
        body.classList.add('dark-mode'); // Apply dark mode class if saved in localStorage
        toggleSwitch.checked = true; // Set the toggle to checked
    }

    // Event listener for the toggle switch
    toggleSwitch.addEventListener('change', toggleDarkMode);
});
