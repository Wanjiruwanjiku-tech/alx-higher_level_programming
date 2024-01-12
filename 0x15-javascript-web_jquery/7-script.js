// Wait for the DOM to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch character data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            // Update the text of DIV#character with the character name
            $('#character').text(response.name);
        },
        error: function() {
            // Handle errors if any
            $('#character').text('Error fetching character data');
        }
    });
});