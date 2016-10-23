import cube
import unittest

class TestCube(unittest.TestCase):
	def test_0(self):
		self.assertEqual(cube.cube(0), 0)

	def test_1(self):
		self.assertEqual(cube.cube(1), 1)

	def test_2(self):
		self.assertEqual(cube.cube(2), 8)

	def test_3(self):
		self.assertEqual(cube.cube(3), 27)

if __name__ == '__main__':
	unittest.main()
