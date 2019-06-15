// Semantics UI jQuery Functions
$('.activating.element')
    .popup();

$('.ui.dropdown')
    .dropdown();



// Semantic ui form validation
$('.ui.form')
    .form({
        fields: {
            name: {
                identifier: 'name',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter your name'
                }]
            },
            username: {
                identifier: 'username',
                rules: [{
                    type: 'empty',
                    prompt: 'Please enter a username'
                }]
            },
            password: {
                identifier: 'password',
                rules: [{
                        type: 'empty',
                        prompt: 'Please enter a password'
                    },
                    {
                        type: 'minLength[2]',
                        prompt: 'Your password must be at least {ruleValue} characters'
                    }
                ]
            },
        }
    });

$('.ui.form').form({
    fields: {
        color: {
            identifier: 'color',
            rules: [{
                type: 'regExp',
                value: /rgb\((\d{1,3}), (\d{1,3}), (\d{1,3})\)/i,
            }]
        }
    }
});


$('.ui.modal')
    .modal('show');



//  add allergen, instructions or ingredient input field
const addField = e => {
    e.stopImmediatePropagation();

    let fieldId = '';
    let field = '';

    let targetElement = e.target;
    if (targetElement.type !== 'button') {
        if (targetElement.parentElement.type !== 'button') {
            return false;
        }
        targetElement = targetElement.parentElement;
    }

    if (targetElement.classList.contains('addAllergen')) {
        fieldId = 'addAllergen';
        field = 'allergens'
    }
    else if (targetElement.classList.contains('addInstruction')) {
        fieldId = 'addInstruction';
        field = 'directions'
    }
    else if (targetElement.classList.contains('addIngredient')) {
        fieldId = 'addIngredient'
        field = 'ingredient'
    }
    const inputSegment = document.getElementById(fieldId);
    let inputContainer = document.createElement("div");
    let inputField = document.createElement("input");
    let closeIcon = document.createElement('i');
    closeIcon.className = `icon delete red label deleteIcon ${field}`;
    closeIcon.setAttribute('id', `deleteIcon`)

    inputField.setAttribute('id', ` ${ field }`);
    inputField.setAttribute('type', 'text');
    inputField.setAttribute('name', `${ field }`);
    inputField.setAttribute('placeholder', `${ field }`)
    inputField.setAttribute('className', "focus")


    inputContainer.className = 'ui input focus inputField fluid ';
    inputContainer.setAttribute('id', 'inputContainer');
    inputContainer.appendChild(closeIcon)
    inputContainer.appendChild(inputField);
    closeIcon.addEventListener('click', removeField);

    inputSegment.appendChild(inputContainer);


};


// Delete allergen, instructions or ingredient input fields
const removeField = e => {
    console.log('should remove')
    const allergenContainer = document.getElementById("addAllergen");
    const ingredientContainer = document.getElementById("addIngredient");
    const instructionsContainer = document.getElementById("addInstruction");

    const targetElement = e.target;
    const targetParentElemet = targetElement.parentElement;


    if (targetElement.classList.contains('allergens')) {

        allergenContainer.removeChild(targetParentElemet)
    }
    if (targetElement.classList.contains('ingredient')) {
        ingredientContainer.removeChild(targetParentElemet)
    }
    if (targetElement.classList.contains('directions')) {
        instructionsContainer.removeChild(targetParentElemet)
    }


};


var filterAccordion = document.getElementById('noMobileFilter')
var mobileDropdown = document.getElementById('mobileScreen')

const detectmob = () => {
    if (navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i)
    ) {
        console.log('mobile view')
        return mobileDropdown.style.display = 'block';
    }
    else {
        console.log('desktop view')
        return filterAccordion.style.display = 'block';
    }
}

detectmob();

window.onload = function () {
    const addAllergenButton = document.getElementById('addAllergenButton');
    if (addAllergenButton) {
        addAllergenButton.addEventListener('click', addField);

        const editAllergen = document.getElementById('addAllergen').childElementCount;
        for (let i = 0; i <= editAllergen; i++) {
            let deleteIcon = document.getElementById(`deleteAllergen${i}`);
            if (editAllergen && deleteIcon) {
                deleteIcon.addEventListener('click', removeField);
            }

        }

    }
    const addIngredientButton = document.getElementById('addIngredientButton');
    if (addIngredientButton) {
        addIngredientButton.addEventListener('click', addField);

        const editIngredient = document.getElementById('addIngredient').childElementCount;
        for (let i = 0; i <= editIngredient; i++) {
            let deleteIcon = document.getElementById(`deleteIngredient${i}`);
            if (editIngredient && deleteIcon) {
                deleteIcon.addEventListener('click', removeField);
            }
        }

    }
    const addInstructionButton = document.getElementById('addInstructionButton');
    if (addInstructionButton) {
        addInstructionButton.addEventListener('click', addField);

        const editInstruction = document.getElementById('addInstruction').childElementCount;
        for (let i = 0; i <= editInstruction; i++) {
            let deleteIcon = document.getElementById(`deleteInstruction${i}`);
            if (editInstruction && deleteIcon) {
                deleteIcon.addEventListener('click', removeField);
            }
        }
    }
};




//  hidden accordion if mobile screen
// if (screen.width <= 640) {

// }
// else {

// }



//Show or hide search result bar
$(document).ready(function () {
    if (window.location.href.indexOf("browse_filter") > 1) {
        $("#sortDetails").show();
    }
    else {
        $("#sortDetails").hide();
    }

    if (filterAccordion) {
        $('.ui.accordion').accordion();
    }


    $('.dropdown-toggle').dropdown()


});

$('.message .close')
    .on('click', function () {
        $(this)
            .closest('.message')
            .transition('fade');
    });

$('.ui.dropdown')
    .dropdown({
        allowCategorySelection: true
    });
