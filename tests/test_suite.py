import unittest
from tests.registeration.registeration_tests import Registeration_Page
from tests.new_job_post.post_job_tests import Post_Job_Page


# Get tests from test classes
test_case1 = unittest.TestLoader().loadTestsFromTestCase(Registeration_Page)
test_case2 = unittest.TestLoader().loadTestsFromTestCase(Post_Job_Page)

#Create Test Suite
AutomationTests = unittest.TestSuite([test_case1, test_case2])

unittest.TextTestRunner(verbosity=2).run(AutomationTests)