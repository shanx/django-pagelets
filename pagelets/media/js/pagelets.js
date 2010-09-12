function setEditor(popup) {
    var value = popup.find('>:selected').val();
    var parent_form = popup.parents('form');
    var content_field_name = popup.attr('name').replace(/type$/, 'content');
    var content_field = parent_form.find('textarea[name=' + content_field_name + ']');
    $('body').trigger('pagelets-change', [value, content_field]);
}

jQuery(function() {
    function install_editor(popup) {
        var empty_form = $(popup).parents('div.empty-form');
        if (empty_form.length == 0) {
            setEditor($(popup));
        }
    }
    $('select[name$=type]').live('change', function() {
        install_editor($(this));
    }).each(function (i) {
        install_editor($(this));
    });
});
