import unittest
from HTMLReport import TestRunner
from server_request import MyTestCase
import os
import sys
sys.path.append(os.environ['WORKSPACE'])

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
