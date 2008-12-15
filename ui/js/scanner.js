
function Scanners() {
    
    this.__init__ = function() {
        this.show_available_devices()
        return this
    }
    
    this.list = function(data, textStatus) {
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
        ajax.call("scanner", this.list)
    }
    
    this.scan = function() { 
        var scanner_id = $("#scanner_list").val()
        var img_name = $("#img_name").val()
        var img_group = $("#document_list").val()
        if (img_group == "new") 
            img_group = $("#docname").val() 
        var scan = "scanner/" + scanner_id + "/scan/" + img_group + "/" + img_name + "/" 
        ajax.call(scan, scanner.scan_callback)
    }

    this.scan_callback = function(data){
        $("#img_name").val('')
        var doc = $("#document_list").val()
        if ( doc == "new" ) {
            doc = $('#docname').val()   
            $('#docname').val('')
            var option = '<option value="'+doc+'">'+doc+'</option>'
            $("#documents").append(option)
            $("#document_list").val(doc)
            $("#document_list").trigger('change')
        }
        $("#document_list").trigger('change')
    }
}


