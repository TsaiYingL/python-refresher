import unittest
import physics
import numpy as np


class TestPhysics(unittest.TestCase):
    def test_buoyancy(self):
        self.assertEqual(physics.calculate_buoyancy(10), 10 * 1000 * 9.81)
        self.assertNotEqual(physics.calculate_buoyancy(30), 10 * 1000 * 9.81)
        self.assertEqual(physics.calculate_buoyancy(-10), "error")
        self.assertNotEqual(physics.calculate_buoyancy(-10), -10 * 1000 * 9.81)

    def test_will_it_float(self):
        self.assertEqual(physics.will_it_float(100, 1), True)
        self.assertEqual(physics.will_it_float(1, 1001), False)
        self.assertNotEqual(physics.will_it_float(100, 1), False)

    def test_calculate_pressure(self):
        self.assertEqual(physics.calculate_pressure(100), 1000 * 100 * 9.81 + 101324)
        self.assertNotEqual(physics.calculate_buoyancy(100), 1000 * 90 * 9.81 + 101324)

    def test_calculate_acceleration(self):
        self.assertEqual(physics.calculate_acceleration(100, 10), 10)
        self.assertEqual(physics.calculate_acceleration(-100, -10), "error")
        self.assertNotEqual(physics.calculate_acceleration(-100, -10), 10)

    def test_calculate_angular_acceleration(self):
        self.assertEqual(physics.calculate_angular_acceleration(100, 10), 10)
        self.assertEqual(physics.calculate_angular_acceleration(100, -10), "error")
        self.assertNotEqual(physics.calculate_angular_acceleration(100, -10), 10)

    def test_calculate_torque(self):
        self.assertEqual(physics.calculate_torque(10, 90, 10), 100 * np.sin(np.pi / 2))
        self.assertEqual(
            physics.calculate_torque(30.555, 90, 10.555),
            10.555 * 30.555 * np.sin(np.pi / 2),
        )
        self.assertEqual(physics.calculate_torque(10, 90, 0), "error")
        self.assertEqual(
            physics.calculate_torque(10.5, 78, 10), 10.5 * np.sin(78 * np.pi / 180) * 10
        )

    def test_calculate_moment_of_inertia(self):
        self.assertEqual(physics.calculate_moment_of_inertia(10.5, 10.5), 10.5**3)
        self.assertEqual(physics.calculate_moment_of_inertia(0, 10), 0)
        self.assertEqual(physics.calculate_moment_of_inertia(-1, 10), "error")
        self.assertEqual(physics.calculate_moment_of_inertia(10, 0), "error")
        self.assertNotEqual(physics.calculate_moment_of_inertia(-1, 10), -10)

    def test_calculate_auv_acceleration(self):
        self.assertEqual(physics.calculate_auv_acceleration(10, np.pi / 2), (0, 0.1))
        self.assertNotEqual(physics.calculate_auv_acceleration(10, np.pi / 2), 0.1)

    def test_calculate_auv_angular_acceleration(self):
        pass

    def test_calculate_auv2_acceleration(T: np.ndarray, alpha: int or float, mass=100):
        pass


if __name__ == "__main__":
    unittest.main()

# can use self.assertraise to check
