// Functionality: Change the color of the menu icons when the mouse is over them
const menuIcons = document.querySelectorAll('.menu__icon');

menuIcons.forEach((menuIcon) => {
    menuIcon.addEventListener('mouseover', () => {
        menuIcon.querySelector('path').style.fill = '#000';
    });
    menuIcon.addEventListener('mouseout', () => {
        menuIcon.querySelector('path').style.fill = '#fff';
    });

});

// Changing menu icon when the menu is open and closed
const menuIcon = document.querySelector('#menu-icon');
const xIcon = document.querySelector('#x-icon');

menuIcon.addEventListener('click', () => { 
    menuIcon.style.display = 'none';
    xIcon.style.display = 'block';
});

xIcon.addEventListener('click', () => {
    xIcon.style.display = 'none';
    menuIcon.style.display = 'block';
});