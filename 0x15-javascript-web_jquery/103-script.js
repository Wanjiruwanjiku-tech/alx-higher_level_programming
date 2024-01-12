// Wait for the DOM to be ready
$(document).ready(function() {
    // Attach click event handler to INPUT#btn_translate
    $('#btn_translate').click(translate);

    // Attach keypress event handler to INPUT#language_code
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            // If ENTER key is pressed, fetch translation
            translate();
        }
    });

    function translate() {
        // Fetch translation from API based on language code
        var languageCode = $('#language_code').val();
        var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;
        
        $.ajax({
            url: apiUrl,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                // Update the text of DIV#hello with the fetched translation
                $('#hello').text(response.hello);
            },
            error: function() {
                // Handle errors if any
                $('#hello').text('Error fetching translation');
            }
        });
    }
});