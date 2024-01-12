// Wait for DOM to be ready
$(document).ready(function() {
    // Attach a click event handler to the DIV#add_item
    $('#add_item').click(function() {
        // Create a new list item with the value Item
        let newListItem = $('<li>Item</li>');
        // Append the new item to UL.my_list
        $('ul.my_list').append(newListItem);
    });
});