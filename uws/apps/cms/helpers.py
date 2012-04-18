import requests

def convert_bytes(bytes):
    bytes = int(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%i' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%i' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%i' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%i' % kilobytes
    else:
        size = '%i' % bytes
    return size

if __name__ == "__main__":
    url = "http://youngrobots.com/media/ultrawizardsword/48_bones_-_hog_wild_12232011.mp3"
    r = requests.get(url)
    print convert_bytes(r.headers['content-length'])
