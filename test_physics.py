import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10), 10 * 1000 * 9.81)
        self.assertNotEqual(physics.calculate_buoyancy(30), 10 * 1000 * 9.81)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100, 1), True)
        self.assertEqual(physics.will_it_float(1, 1001), False)
        self.assertNotEqual(physics.will_it_float(100, 1), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(100), 1000 * 100 * 9.81 + 101324)
        self.assertNotEqual(physics.calculate_buoyancy(100), 1000 * 90 * 9.81 + 101324)


if __name__ == "__main__":
    unittest.main()

# can use self.assertraise to check
