import unittest
from HTMLReport import TestRunner
from server_request import MyTestCase
import os,sys
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir)
sys.path.append("/Users/hyde/Y4B_autotest/venv/lib/python3.9/site-packages")

if __name__ == '__main__':
    suite = unittest.TestSuite()

    # test case order
    tests = [
        MyTestCase("test_getskutree")
    ]

    suite.addTests(tests)

    runner = TestRunner(
        report_file_name="test_report",
        output_path="reports",
        title="测试报告",
        description="check getskutree API", )

    runner.run(suite)
    unittest.main()
