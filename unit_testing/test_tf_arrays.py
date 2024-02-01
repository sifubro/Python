import unittest
import tf_arrays
import numpy as np
import tensorflow as tf  


'''
run it as 
python test_tf_arrays.py
'''

class TestTfArrays(unittest.TestCase):

    def test_one_array(self):
        array = np.array([1,2,3])
        result = tf_arrays.create_array()
        tf.debugging.assert_equal(result, array)


if __name__ == '__main__':
    unittest.main()
