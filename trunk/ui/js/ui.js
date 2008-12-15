
function UI() 
{
    this.__init__ = function() {
                $("#page_list").sortable({opacity: 0.3, placeholder: "webscan-placeholder"})
        $("#page_list").hide()
        return this
    }
    
    this.set_tooltips = function() {
        var doc = $("#document_list").val()
        var thumb_url = 'http://localhost:4040/'+user.username+'/'+doc+'/thumb/'
        $("#page_list li").tooltip({
            bodyHandler: function() {
                return $("<img/>").attr("src", thumb_url+ $(this).attr("id")+".png")
            }
        })
    }
    
    this.doclist_changed = function() {
        var doc = $("#document_list").val()
        if (doc == "new") {
            $("#page_list").hide()
            $("#newdoc").show()
        } else { 
            $("#page_list").show()
            $("#newdoc").hide()
            user.get_pages()
        }
    }
}
