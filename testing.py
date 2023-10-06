import unittest
import mainfunc

# create class to test and couple methods for test
class TestMain(unittest.TestCase):
    # create method for test
    def test_our_func(self):
        # declare some test parameter
        test_param = 10
        # call our function with test parameter
        result = mainfunc.addfunc(test_param)
        # here is the test itself:
        # method below i just check that 2 outputs are equal:
        self.assertEqual(result, 15)
    #create 2nd test
    def test_our_func2(self):
        '''Test for some gibberish instead of int number'''
        test_param = 'sm_gibberish'
        result = mainfunc.addfunc(test_param)
        # and now we want to test if output will be a ValueError:
        self.assertTrue(isinstance(result,ValueError))
        # Note that we use here isinstance because the output is actually an instance of ValueError class
        
# to run test we use just following:
if __name__ == '__main__':
    unittest.main()