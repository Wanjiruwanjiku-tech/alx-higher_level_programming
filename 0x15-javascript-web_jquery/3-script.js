// Wait for the DOM to be ready
$(document).ready(function() {
    // Attach a click event handler to DIV#red_header
    $('#red_header').click(function() {
        // Add the class to the element
        $('header').addClass('red');
    });
});