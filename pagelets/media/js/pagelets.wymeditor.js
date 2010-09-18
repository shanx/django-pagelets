jQuery(function() {
    $(document).bind('pagelets-change', function(e, name, content_field) {
        if (name == 'wymeditor') {
            content_field.wymeditor({
                updateSelector: "input:submit",
                updateEvent: "click",
            });
        } else {
            jQuery.each(WYMeditor.INSTANCES, function() {
              if(this._element.attr('name') == content_field.attr('name')){
                  this.update();
                  $(this._box).remove();
                  $(this._element).show();
                  $(this._options.updateSelector).unbind(this._options.updateEvent);
                  delete this;
              }
            });
            content_field.siblings('div.wym_box').remove();
            content_field.css('display', 'inline');
        }
    });
});
