//# jQuery
$(document).ready(function() {
    $('.itemInput').focus();

    //# Adding to list, click on box, append entered value with a checkbox
    $(document).on('click', '.aList', function() {
        var addItem = $('input[name="itemInput"]').val().trim();
        if ( addItem ) {
            $('.items').append('<div class="input"><input type="checkbox" name="item" class="item" value="' + addItem + '" /> '+ addItem +'</div>');
        }
        $('.itemInput').val('').focus();
    });
    
    //# Removing from list, checkbox clicked and fade out on removal
    $(document).on('change', '.item', function() {
        if ( $(this).is(':checked') ){
            var delItem = $(this).parent();
            delItem.fadeOut(500, function() {
                delItem.remove();
            });
        }
    });
    
    //# prevents empty form
    $('.listForm').submit(function(e) {
        e.preventDefault();
    });
    
    //# jQuery UI makes list drag and sort ready
    $('.items').sortable();
    
    
});