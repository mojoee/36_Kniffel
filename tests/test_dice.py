import unittest
import sys
sys.path.append('..')
from dice import Wuerfel

class TestWuerfel(unittest.TestCase):

    def test_range(self):
        test_wuerfel=Wuerfel(6,1, 6)
        for i in range(100):
            self.assertIn(test_wuerfel.roll(),list(range(1,6+1)), \
                "Result is not in range 1-6") 

    def test_range_list(self):     
        test_wuerfel=Wuerfel(6,1,8)
        self.assertEqual(test_wuerfel.results, list(range(1,9)))



if __name__=="__main__":
    unittest.main()