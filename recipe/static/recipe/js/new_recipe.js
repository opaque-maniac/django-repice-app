// Query for the input[type="image"] element
const imageInput = document.querySelector('input[type="file"]');
const title = document.querySelector('input[name="title"]');
const allInputFields = document.querySelectorAll('input');
const submitButton = document.querySelector('button[type="submit"]');

// Find the parent element of the image input
const parentElement = imageInput.parentElement;

// Function to create an image element with the source and value entered by the user
function createImageElement(source, value) {
    const imageElement = document.createElement('img');
    imageElement.src = source;
    imageElement.alt = value;
    return imageElement;
}

document.addEventListener('DOMContentLoaded', (event) => {
    // disable the submit button when page loads
    submitButton.setAttribute('disabled', '');

    // If all the input fields are empty, disable submit button, else, enebale it
    allInputFields.forEach(field => {
        field.addEventListener('input', () => {
            if (field.value != '') {
                submitButton.removeAttribute('disabled');
            } else {
                submitButton.setAttribute('disabled', '');
            }
        })
    })


    // To create an image preview
    imageInput.addEventListener('change', () => {
        let file = event.target.file[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                const source = e.target.result;
                const value = title.value;
                let new_image = createImageElement(source, value);
                parentElement.append(new_image);
            }
        }
    })
})