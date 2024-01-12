// Updates the text of the header element
// Wait untill DOM is ready
$(document).ready(function() {
    // Attack a click event handler for DIV#update_header
    $('#update_header').click(function() {
        // Create a variable to hold the new text
        let newHeaderText = 'New Header!!!';
        // Update the header element
        $('header').text(newHeaderText);
    });
});