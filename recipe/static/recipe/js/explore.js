// Querying elements from  the DOM
const arrowRight = document.querySelector('.arrow__right');
const arrowLeft = document.querySelector('.arrow__left');
const directionButton = document.querySelector('.direction__button');
const navSide = document.querySelector('.side-nav');
const mainDiv = document.querySelector('.page-main');
const body = document.body;
const navSideLinks = document.querySelectorAll('.pagenav__link');
const allRecipeLinks = document.querySelectorAll('.recipe__link');


// When the document loads
document.addEventListener('DOMContentLoaded', () => {
    navSide.style.height = `${mainDiv.clientHeight - 10}px`;
    // add an event listener for the button
    // For the hover even
    directionButton.addEventListener('mouseover', () => {
        directionButton.querySelectorAll('svg').forEach(svg => {
            svg.style.transform = 'scale(1.2)';
        });
    });
    directionButton.addEventListener('mouseout', () => {
        directionButton.querySelectorAll('svg').forEach(svg => {
            svg.style.transform = 'scale(1)';
        });
    });

    // For asigning the recipe link style classes dynamicalling
    for (let i = 0; i < allRecipeLinks.length; i++) {
        if (i % 2 == 0) {
            allRecipeLinks[i].classList.add('background-secondary');
        } else {
            allRecipeLinks[i].classList.add('background-primary');
        }
    }

    // Listening to the query
    directionButton.addEventListener('click', (event) => {
        body.style.overflow = body.style.overflow === 'hidden' ? 'auto' : 'hidden';
        let first_child = directionButton.children[0];      // Very poor approach
        let second_child = directionButton.children[1];
        if (first_child.classList.contains('hidden')) {
            first_child.classList.remove('hidden');
            first_child.classList.add('show');
            navSide.style.left = '-100%';
            directionButton.classList.remove('open');
            directionButton.classList.add('closed');
            second_child.classList.remove('show');
            second_child.classList.add('hidden');
        } else {
            first_child.classList.remove('show');
            first_child.classList.add('hidden');
            navSide.style.left = '0';
            directionButton.classList.remove('closed');
            directionButton.classList.add('open');
            second_child.classList.remove('hidden');
            second_child.classList.add('show');
        }
    });

    // For the links that have been clicked
    navSideLinks.forEach(link => {
        link.addEventListener('click', () => {
            link.style.fontWeight = '700';
        });
    })
});