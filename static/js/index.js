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
    closeIcon.setAttribute('onclick', 'removeAllergen({{ loop.index0 }})')

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
    closeIcon.setAttribute('onclick', 'removeIngredient({{ loop.index0 }})')

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

const inputContainer = document.getElementById("addAllergen");
const ingredientContainer = document.getElementById("addIngredient");

const removeIngredient = id => {
    const removeItem = document.getElementById(`ingredientsContainer${id}`);
    ingredientContainer.removeChild(removeItem)
};



const removeAllergen = id => {
  const removeItem = document.getElementById(`inputContainer${id}`);
    inputContainer.removeChild(removeItem)
};
