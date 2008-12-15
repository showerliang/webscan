
function Ajax() {
    this.__init__ = function(base_url) {
        this.base_url = base_url
        return this
    }

    this.call = function(url, jsoncallback, data, options) {
        if(!data) { data = {} }
        if(!options) { options = {} }

        this.__start__(data['start_msg'])

        options['success'] = jsoncallback       
        options['complete'] = this.__complete__ 
        options['success'] = jsoncallback       
        options['url'] = this.base_url + '/' + url
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
    }
}
