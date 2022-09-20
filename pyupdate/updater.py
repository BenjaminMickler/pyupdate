from pyupdate import update_list, tools

def update():
    if not tools.internet():
        raise Exception('No internet connection')
    for update_file in update_list.read_update_list('update_list.json'):
        tools.download(update_file['url'], f"{config["DEFAULT"]["CacheDir"]}/{update_file['filename']}")