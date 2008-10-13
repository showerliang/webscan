function Ajax() {
    this.__init__ = function(base_url) {
        this.base_url = base_url
        return this
    }

    this.call = function(url, jsoncallback, data, options) {
        if(!data) { data = {} }
        if(!options) { options = {} }

        this.__start__(data['start_msg'])

        if(data['callback']) {
            throw('The name "callback is reserved" use another name.')
        }
        data['callback'] = jsoncallback
        
        options['url'] = this.base_url + '/' + url +'/?jsoncallback=?'
        options['data'] = data
        options['dataType'] = 'jsonp'
        options['global'] = true
        options['async'] = true
        $.ajax(options) 
    }
    
    this.__error__ = function(data) {
        $('#notification').empty()
        $('#notification').append(data['error_msg'])
    }
     
    this.__complete__ = function(data) {
        $('input').attr('disabled', false)
        $('select').attr('disabled', false)
    }
    
    this.__start__ = function(start_msg) {
        $('input').attr('disabled', true)
        $('select').attr('disabled', true) 
        $('#notification').empty()
        $('#notification').append(start_msg)
        console.debug(start_msg)
    }
}

function Scanners() {
    
    this.__init__ = function() {
        this.show_available_devices()
        return this
    }
    
    this.list = function(data) {
        $("#scanner_list").empty()
        var id  
        var name
        var manufacturer
        var option
        for ( var i in data ) {
            id = data[i]['id']
            name = data[i]['name']
            manufacturer  = data[i]['manufacturer']
            option = '<option value="'+id+'">'+manufacturer+' - '+name+'</option>'
            $("#scanner_list").append(option)
        }
    }
    
    this.show_available_devices = function() {
        ajax.call("scanner", "scanner.list")
    }
    
    this.scan = function() { 
        var scanner_id = $("#scanner_list").val()
        var img_name = $("#img_name").val()
        var img_group = $("#document_list").val()
        data = {'img_name': img_name, 'img_group': img_group, 'start_msg': 'Scanning...'}
        ajax.call("scanner/"+scanner_id+"/scan", "scanner.scan_callback", data)
    }

    this.scan_callback = function(data){ 
        user.get_pages()
        var img_name = $("#img_name").val()
        var img_group = $("#document_list").val()
        $('#notification').empty()
        $('#notification').append('Image "'+img_name+'.tif" added to document "'+img_group+'"')
    }
}

function User() {
   
    this.__init__ = function() {
        ajax.call('user', 'user.check_login', {'async': false, 'global': false})
        return this
    }

    this.check_login = function(data) {
        if(data['auth']) {
            this.username = data['username']
            $("#username").empty()
            $("#username").append(this.username)
            this.get_documents()
        }
    }
 
    this.list_documents = function(data) {
        $("#document_list").empty()
        for ( var i in data ) {
            option = '<option value="'+data[i]+'">'+data[i]+'</option>'
            $("#document_list").append(option)
        }
        this.get_pages()
    }    
 
    this.get_documents = function() {
        ajax.call("user/"+this.username,"user.list_documents") 
    }
        
    this.get_pages = function() {
        var doc = $("#document_list").val()
        ajax.call("user/"+this.username+"/"+doc,'user.list_pages')
    }
    
    this.list_pages = function(data) {
        $("#page_list").empty()
        $("#page_list").append('<tr><th>Use</th><th>Image Name</th><th>Preview</th></tr>')
        for( var i in data ) {
            var doc = $("#document_list").val()
            var url = 'http://localhost/webscan/user/'+this.username+'/'+doc+'/'+data[i]
            $("#page_list").append('<tr><td><input type="checkbox" value="'+data[i]+'"></td><td>'+data[i]+'</td><td><a href="'+url+'">Preview</td></tr>')
        }
    }
}

function __init__() {
    ajax = new Ajax().__init__("http://localhost/webscan")
    scanner = new Scanners().__init__()
    user = new User().__init__()
}
$(document).ready(__init__)

