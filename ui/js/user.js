
function User() {
   
    this.__init__ = function() {
        ajax.call('user', this.get_user)
        return this
    }

    this.get_user = function(data) {
        user.username = data['username']
        user.docdir = data['docdir']
        user.get_documents()
    }
 
    this.list_documents = function(data) {
        var option
        $("#documents").empty()
        for ( var i in data ) {
            option = '<option value="'+data[i]+'">'+data[i]+'</option>'
            $("#documents").append(option)
        }
    }    
 
    this.get_documents = function() {
        ajax.call(this.username, this.list_documents) 
    }
        
    this.get_pages = function() {
        var doc = $("#document_list").val()
        ajax.call(this.username+"/"+doc, this.list_pages)
    }
    
    this.list_pages = function(data) {
        $("#page_list").empty()
        for( var i in data ) {
            var page = data[i]
            var doc = $("#document_list").val()
            var view_url = 'file:///' + escape(page['viewpath'])
            var page_name = page['name']          
 
            $("#page_list").append(
                '<li id="'+page_name+'">'+
                    '<input type="checkbox" value="'+page_name+'" checked="checked"/>'+
                    page_name+
                    ' (<a href='+view_url+'>visualizar</a>)'+
                '</li>')
            ui.set_tooltips()
        }
    }

    this.request_download = function() {
        var doc = $("#document_list").val()
        
        var ordered_pages = []
        $("#page_list li input:checked").each(
            function(){ 
                ordered_pages[ordered_pages.length] = $(this).val() 
            }
        )
        
        var pages = escape(JSON.stringify(ordered_pages)) 
        var lang = 'por'
        var doctitle = escape($("#doctitle").val())

        var args = {
            'pages' : JSON.stringify(ordered_pages),
            'lang': lang,
            'doctitle': $("#doctitle").val(),
        }
    
        var url = user.username+'/download/'+ doc +'.pdf'

        ajax.call(url, user.download, args)
    }
    
    this.download = function(data) {
        window.location.href = 'file:///'+data 
    }
}
