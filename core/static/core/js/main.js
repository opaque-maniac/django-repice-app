// Query Selectors for elements on the DOM
const menuIcon = document.querySelector('#menu-icon');
const xIcon = document.querySelector('#x-icon');
const navbar = document.querySelector('.navbar');

// Event listener for the menu icon
menuIcon.addEventListener('click', () => {
    menuIcon.classList.add('hidden');
    xIcon.classList.remove('hidden');
    navbar.style.top = '93px';
});

// Event listener for the x icon
xIcon.addEventListener('click', () => {
    xIcon.classList.add('hidden');
    menuIcon.classList.remove('hidden');
    navbar.style.top = '-100%';
});
