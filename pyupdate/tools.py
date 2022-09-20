import sockets
import requests

def download(url, filename):
    with open(filename, 'ab') as f:
        headers = {}
        pos = f.tell()
        if pos:
            headers['Range'] = f'bytes={pos}-'
        response = requests.get(url, headers=headers, stream=True)
        if pos:
            validate_as_paranoid_as_you_want_to_be_(pos, response)
        total_size = int(response.headers.get('content-length'))  
        for data in tqdm(iterable = response.iter_content(chunk_size = 1024), total = total_size//1024, unit = 'KB'):
            file.write(data)

def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False