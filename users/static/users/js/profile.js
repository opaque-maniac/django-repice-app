// Querying elements from the DOM
const image = document.querySelector('img');

// When the page loads
document.addEventListener('DOMContentLoaded', () => {
    // hover event listener for the profile image
    image.addEventListener('mouseover', () => {
        image.style.transform = 'scale(1.1)';
    });
    image.addEventListener('mouseout', () => {
        image.style.transform = 'scale(1)';
    });
});
