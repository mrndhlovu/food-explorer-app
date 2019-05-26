// intitialise global variables

$(document).ready(function() {

    $('.activating.element')
        .popup();

    $('.ui.dropdown')
        .dropdown();
    $('.example .menu .browse')
        .popup({
            inline: true,
            hoverable: true,
            position: 'bottom left',
            delay: {
                show: 300,
                hide: 800
            }
        });
});


const addAllergen = () => {
    const inputSegment = document.getElementById('addAllergen');
    let inputContainer = document.createElement("div");
    let inputField = document.createElement("input");
    let closeIcon = document.createElement('i')

    closeIcon.className = 'icon delete label';
    closeIcon.setAttribute('onclick', 'removeInputField()')

    inputField.setAttribute('id', 'allergens');
    inputField.setAttribute('type', 'text');
    inputField.setAttribute('name', 'allergens');
    inputField.setAttribute('placeholder', 'Allergen')

    inputContainer.className = "ui input focus";
    inputContainer.setAttribute('id', 'inputContainer')
    inputContainer.appendChild(inputField);
    inputContainer.append(closeIcon)


    inputSegment.appendChild(inputContainer);
};

const addIngredient = () => {
    const inputSegment = document.getElementById('addIngredient');
    let inputContainer = document.createElement("div");
    let inputField = document.createElement("input");
    let closeIcon = document.createElement('i')

    closeIcon.className = 'icon delete label';
    closeIcon.setAttribute('onclick', 'removeInputField()')
    
    inputField.setAttribute('id', 'ingredient');
    inputField.setAttribute('type', 'text');
    inputField.setAttribute('name', 'ingredient');
    inputField.setAttribute('placeholder', 'Ingredient');

    inputContainer.className = "ui input focus";
    inputContainer.appendChild(inputField);
    inputContainer.setAttribute('id', 'inputContainer')
    inputContainer.append(closeIcon)

    inputSegment.appendChild(inputContainer);
};

const removeInputField = () => {
    const deleteField = document.getElementById("addIngredient");
    const inputField = document.getElementById("IngredientsContainer");
    while (deleteField) {
       deleteField.parentNode.removeChild(inputField);
    }
};



const removeAllergen = () => {
    const deleteField = document.getElementById("addAllergen");
    const deleteInput = deleteField.lastElementChild
    while (deleteField) {
        deleteField.removeChild(deleteInput);
    }
};

const removeIngredient = () => {
    const deleteField = document.getElementById("addIngredient");
    const deleteInput = deleteField.lastElementChild
    while (deleteField) {
        deleteField.removeChild(deleteInput);
    }
};
