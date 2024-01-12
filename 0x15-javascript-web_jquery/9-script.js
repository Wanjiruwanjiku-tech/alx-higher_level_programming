// Wait for the DOM to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch the translation
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        dataType: 'text',
        success: function(response) {
            // Update the text of DIV#hello with the fetched translation
            $('#hello').text(response);
        },
        error: function() {
            // Handle errors if any
            $('#hello').text('Error fetching translation');
        }
    });
});