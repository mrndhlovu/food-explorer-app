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


//  add ingredient or allergen input field
const addField = e => {
    e.preventDefault();
    let fieldId = '';
    let field = '';
    if (e.target.classList.contains('addAllergen')) {
        fieldId = 'addAllergen';
        field = 'allergens'
    }
    else {
        fieldId = 'addIngredient'
        field = 'ingredient'
    }
    const inputSegment = document.getElementById(fieldId);
    let inputContainer = document.createElement("div");
    let inputField = document.createElement("input");
    let closeIcon = document.createElement('i')

    closeIcon.className = `icon delete label deleteIcon ${field}`;
    closeIcon.setAttribute('id', 'deleteIcon')

    inputField.setAttribute('id', `${field}`);
    inputField.setAttribute('type', 'text');
    inputField.setAttribute('name', `${field}`);
    inputField.setAttribute('placeholder', `${field}`)

    inputContainer.className = "ui input focus";
    inputContainer.setAttribute('id', 'inputContainer')
    inputContainer.appendChild(inputField);
    inputContainer.append(closeIcon)

    inputSegment.appendChild(inputContainer);
    document.getElementById('deleteIcon').addEventListener('click', removeField)

};



// Delete allergen or ingredient input fields
const removeField = e => {
    e.stopPropagation();
    const allergenContainer = document.getElementById("addAllergen");
    const ingredientContainer = document.getElementById("addIngredient");

    if (e.target.classList.contains('ingredient')) {
        const field = e.target.parentElement
        ingredientContainer.removeChild(field)
    }
    else {
        const field = e.target.parentElement
        allergenContainer.removeChild(field)
    }
};


window.onload = function() {
    document.getElementById('addAllergenButton').addEventListener('click', addField)
    document.getElementById('addIngredientButton').addEventListener('click', addField)
    $("#plusIcon").attr('disabled', 'disabled');
    $("#plusIcon2").attr('disabled', 'disabled');

};
