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
    e.stopImmediatePropagation();
    let fieldId = '';
    let field = '';
    if (e.target.classList.contains('addAllergen')) {
        fieldId = 'addAllergen';
        field = 'allergens'
    }
    else if (e.target.classList.contains('addInstruction')) {
        fieldId = 'addInstruction';
        field = 'directions'
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
    inputField.setAttribute('className', "focus")

    inputContainer.className = 'ui input focus inputField fluid ';
    inputContainer.setAttribute('id', 'inputContainer')
    inputContainer.appendChild(inputField);
    inputContainer.appendChild(closeIcon)

    inputSegment.appendChild(inputContainer);
    document.getElementById('deleteIcon').addEventListener('click', removeField)

};


// Delete allergen or ingredient input fields
const removeField = e => {
    e.stopPropagation();
    const allergenContainer = document.getElementById("addAllergen");
    const ingredientContainer = document.getElementById("addIngredient");
    const instructionsContainer = document.getElementById("addInstruction");

    if (e.target.classList.contains('allergens')) {
        const field = e.target.parentElement
        allergenContainer.removeChild(field)
    }
    if (e.target.classList.contains('ingredient')) {
        const field = e.target.parentElement
        ingredientContainer.removeChild(field)
    }
    if (e.target.classList.contains('directions')) {
        const field = e.target.parentElement
        instructionsContainer.removeChild(field)
    }
};


window.onload = function() {
    document.getElementById('addAllergenButton').addEventListener('click', addField)
    document.getElementById('addIngredientButton').addEventListener('click', addField)
    document.getElementById('addInstructionButton').addEventListener('click', addField)
};

$(document).ready(function() {
    const summaryContainer = document.getElementById('sortDetails')
    if (window.location.href.indexOf("browse_filter") > 1) {
        $("#sortDetails").show();
    }
    else {
         $("#sortDetails").hide();
    }
});
