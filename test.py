import bubble
import unittest

class TestSequenceFunctions(unittest.TestCase):
    

    def test_bsort(self):
        assert (bubble.sort([4,3,2,1]) == [1,2,3,4])

if __name__ == '__main__':
    unittest.main()
