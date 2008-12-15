
function __init__() {
    ajax = new Ajax().__init__("http://localhost:4040")
    scanner = new Scanners().__init__()
    user = new User().__init__()
    ui = new UI().__init__()

    // Triggers:
    $("#document_list").bind("change", ui.doclist_changed)
    $("#update_scanners").bind("click", scanner.show_available_devices)
    $("#scan_page").bind("click", scanner.scan)
    $("#download_doc").bind("click", user.download)
}

$(document).ready(__init__)
