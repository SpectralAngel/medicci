$(document).bind('mobileinit',function(){
    $.mobile.selectmenu.prototype.options.nativeMenu = false;
});
$(document).ready( function () {
    if (Modernizr.input.placeholder) {
        $("input").each(function(index, element) {
            var placeholder = $("label[for=" + element.id + "]").hide().text();
            $(element).addClass("ui-input-text-placeholder")
                .attr("placeholder", placeholder);
        });
    }
    
    /* mostly this is just sample code for how to trigger code for each page */
    $('div:jqmData(role=\'page\')').live('pagecreate',function(event){
        var page = $(this);
        page.find( '.field-wrapper' ).each( function() {
            var wrapper = $(this);
            var text = wrapper.find( '.field-help' );
            if (text.length) {
                var hidden = true;
                page.find( 'button.help-trigger' ).each( function () {
                   var trigger = $(this); 
                    trigger.click( function(event) {
                        text.toggle();
                        event.stopPropagation();
                        return false;
                    });
                });
                text.hide();
            }
        });
    });
});
