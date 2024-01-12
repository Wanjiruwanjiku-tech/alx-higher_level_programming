// Wait for the DOM to be ready
$(document).ready(function() {
    // Make an AJAX request to fetch movie data
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        dataType: 'json',
        success: function(response) {
            // Loop through each movie and add its title to the list
            $.each(response.results, function(index, movie) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function() {
            // Handle errors if any
            $('#list_movies').append('<li>Error fetching movie data</li>');
        }
    });
});