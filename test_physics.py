import unittest
import physics


class TestPhysics(unittest.TestCase):
    def test_buoyancy(self):
        self.assertEqual(
            physics.calculate_buoyancy(10),
            f"the buoyancy is {10*1000*9.81} Newtons",
        )
        self.assertNotEqual(
            physics.calculate_buoyancy(30), f"the buoyancy is {10*1000*9.81} Newtons"
        )


if __name__ == "__main__":
    unittest.main()
