// Wait for the DOM to be ready
$(document).ready(function() {
    // Attach click event handlers
    $('#add_item').click(function() {
        // Add a new <li> element to UL.my_list
        $('ul.my_list').append('<li>Item</li>');
    });

    $('#remove_item').click(function() {
        // Remove the last <li> element from UL.my_list
        $('ul.my_list li:last-child').remove();
    });

    $('#clear_list').click(function() {
        // Remove all <li> elements from UL.my_list
        $('ul.my_list').empty();
    });
});
