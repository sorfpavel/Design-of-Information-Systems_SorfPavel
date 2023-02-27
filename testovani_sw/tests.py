import unittest

from main import Route

class TestRouteMethods(unittest.TestCase):

    def test_set_points(self):
        output = test_route.set_points(test_points)
        self.assertTrue(output[0] == complex(*test_points[0]))
        self.assertTrue(len(output) == len(test_points))

    def test_get_points(self):
        output = test_route.get_points()
        self.assertTrue(test_points[0][0] == output[0][0])
        self.assertTrue(len(output) == len(test_points))

    def test_get_total_distance(self):
        output = test_route.get_total_distance()
        self.assertAlmostEqual(output, 14.142135623730951)
        self.assertTrue(type(output) == float)

    def test_get_aerial_distance(self):
        output = test_route.get_aerial_distance()
        self.assertAlmostEqual(output, 2.8284271247461903)
        self.assertTrue(type(output) == float)

    def test_input_corrupted_data_str(self):
        with self.assertRaises(IndexError):
            corrupted_data = "asfasdf"
            Route(corrupted_data)

    def test_input_corrupted_data_number(self):
        with self.assertRaises(TypeError):
            corrupted_data = -1.1
            Route(corrupted_data)

    def test_input_corrupted_data_str_in_tuple(self):
        with self.assertRaises(TypeError):
            corrupted_data = ["fadafsd", (1, 1)]
            Route(corrupted_data)


test_points = [(1, 1), (5, 5), (-1, -1)]
test_route = Route(test_points)

if __name__ == '__main__':
    unittest.main()