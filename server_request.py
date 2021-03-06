import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("/Users/hyde/practice/venv/lib/python3.9/site-packages")
import unittest
import requests
from nose.tools import assert_true


class MyTestCase(unittest.TestCase):
    def test_getskutree(self):
        page = requests.get('https://apptest.perfectcorp.com/service/V2/getSkuTreeByType?country=US&lang=en-US&makeupVer=38.0&platform=iOS&product=YouCam%20Makeup&skuFormatVer=4.0&type=blush&version=1.0&versiontype=for%20iOS')
        assert_true(page.ok)
        if page.status_code==200:
            print('getskutreeAPI is ok')
        else:
            print('getskutreeAPI has error')

if __name__ == '__main__':
    unittest.main()

