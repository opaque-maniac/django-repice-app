const recipeLinks = document.querySelectorAll('.recipe__link');

// When the page loads
document.addEventListener('DOMContentLoaded', () => {
    // If there are any recipes
    if (recipeLinks.length != 0) {
        // Assigning each recipe a different class name to change style dynamically
        for (let i = 0; i < recipeLinks.length; i++) {
            if (i % 2 == 0) {
                recipeLinks[i].classList.add('background-normal');
            } else {
                recipeLinks[i].classList.add('background-alternative');
            }

            let image = recipeLinks[i].querySelector('img');

            // Event handlers for the hover event for recipe items
            recipeLinks[i].addEventListener('mouseover', () => {
                image.style.transform = 'scale(1.03)';  // Enlargens the image slightly
            });

            recipeLinks[i].addEventListener('mouseout', () => {
                image.style.transform = 'scale(1)';
            })
        }
    }


})