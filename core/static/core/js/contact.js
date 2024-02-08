const contactLinks = document.querySelectorAll('.contact-link');
const allInputFields = document.querySelectorAll('.form__input');
const submitButton = document.querySelector('button[type="submit"]');  

document.addEventListener('DOMContentLoaded', () => {

    // Event listener for the contact links
    contactLinks.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.querySelector('path').style.fill = '#333';
            link.querySelector('svg').style.transform = 'scale(1.1)';
        });

        link.addEventListener('mouseout', () => {
            link.querySelector('path').style.fill = 'initial';
            link.querySelector('svg').style.transform = 'scale(1)';
        });
    });

    // Event listener for the input fields
    submitButton.setAttribute('disabled', '');

    allInputFields.forEach(field => {
        field.addEventListener('input', () => {
            if (field.value !== '') {
                submitButton.removeAttribute('disabled');
            } else {
                submitButton.setAttribute('disabled', '');
            }
        });
    });
});