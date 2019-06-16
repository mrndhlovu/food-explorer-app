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


$('.ui.modal')
    .modal('show');



//  create allergen, instructions or ingredient input field
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


const deskTopFilterAccordion = document.getElementById('noMobileFilter')
const mobileFilterDropdown = document.getElementById('mobileScreen')



// find device type and load recipe filter  
const detectmob = () => {
    if (navigator.userAgent.match(/Android/i) ||
        navigator.userAgent.match(/webOS/i) ||
        navigator.userAgent.match(/iPhone/i) ||
        navigator.userAgent.match(/iPad/i) ||
        navigator.userAgent.match(/iPod/i) ||
        navigator.userAgent.match(/BlackBerry/i) ||
        navigator.userAgent.match(/Windows Phone/i)
    ) {
        return mobileFilterDropdown.style.display = 'block';
    }
    else {
        return deskTopFilterAccordion.style.display = 'block';
    }
}

let userData;

window.onload = () => {
    detectmob();
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

    const recipesFound = document.getElementById('recipeListContainer');
    if (recipesFound) {
        for (let i = 0; i <= recipesFound.childElementCount; i++) {
            const likeButton = document.getElementById(`liked${i}`);
            if (likeButton) {

                likeButton.addEventListener('click', recipeVote, true)
            }

        }

    }

    const username = document.getElementById('onlineUsername');
    if (username) {
        let userRecord = `user-${username.innerHTML}`
        userData = JSON.parse(localStorage.getItem(userRecord)) || {
            username: username.innerHTML,
            userLikes: [],
        };
        localStorage.setItem(userRecord, JSON.stringify(userData))
        userData = JSON.parse(localStorage.getItem(userRecord))
    }
    else {
        return false
    }
};

const recipeVote = e => {

    const { userLikes } = userData;
    const likeButton = e.target;
    let recipesLiked = [];



    if (likeButton.children.item(0) !== null) {
        const recipeId = likeButton.children.item(0).id;
        const likeRecipeButton = likeButton.class
        console.log(likeButton)
        if (userLikes.indexOf(recipeId) >= 0) {
            userLikes.pop(recipeId)
            localStorage.setItem(`user-${userData.username}`, JSON.stringify(userData))
            const updateRecord = JSON.parse(localStorage.getItem(`user-${userData.username}`))

        }
        else {
            userLikes.push(recipeId);
            localStorage.setItem(`user-${userData.username}`, JSON.stringify(userData))
            const updateRecord = JSON.parse(localStorage.getItem(`user-${userData.username}`))

        }


        // if (userLikes) {
        //     userLikes.push(likeId.id);
        //     console.log('Userdata: ', userData)

        //     // console.log('created : ', recipesLiked)
        //     localStorage.setItem('userData', JSON.stringify(userData))
        //     const newFile = JSON.parse(localStorage.getItem('userData'))
        //     console.log('From LocalStorage: ', newFile)


        //     console.log('shold set new recipesLiked array to LS: ', userData)
        // }
        // else {
        //     console.log('You liked this already')
        //     return false
        // }

    }




}









//Show or hide search result bar
$(document).ready(function () {
    if (window.location.href.indexOf("browse_filter") > 1) {
        $("#sortDetails").show();
    }
    else {
        $("#sortDetails").hide();
    }

    if (deskTopFilterAccordion) {
        $('.ui.accordion').accordion();
    }


    $('.dropdown-toggle').dropdown()

});
