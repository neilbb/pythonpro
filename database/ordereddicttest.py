import unittest
import ordereddict




class DictTests(unittest.TestCase):
	def test_one_plus_five(self):
		assert (1 + 5) == 6

	def test_one_plus_one(self):
		assert not (1 + 1) == 5



if __name__ == "__main__":
	unittest.main()