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
