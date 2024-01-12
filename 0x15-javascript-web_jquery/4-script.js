// Toggles the class of the header element when the user clicks the
// DIV#toggle_header
// Wait for DOM to be ready
$(document).ready(function() {
    // Attach a click event handler to the DIV#toggle_header
    $('#toggle_header').click(function() {
        // Toggle the class red and green on the element
        $('header').toggleClass('red green');
    });
});