import requests

page = requests.get('https://apptest.perfectcorp.com/service/V2/getSkuTreeByType?country=US&lang=en-US&makeupVer=38.0&platform=iOS&product=YouCam%20M')
print(page.status_code)
if page.status_code==200:
    print('server is ok')
else:
    print('server has some error')