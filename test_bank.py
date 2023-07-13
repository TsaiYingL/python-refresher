import unittest
import bank


class Test_bank(unittest.TestCase):
    def test_account(self):
        acc = bank.Bankaccount("Tsai", 1234567, 0)
        bank.Bankaccount.current_balance(acc)
        self.assertNotEqual(
            bank.Bankaccount.deposit(acc, 100), "Tsai has $200 in account."
        )
        self.assertEqual(
            bank.Bankaccount.deposit(acc, 100), "Tsai has $200 in account."
        )
        self.assertEqual(
            bank.Bankaccount.current_balance(acc), "Tsai has $200 in account."
        )


if __name__ == "__main__":
    unittest.main()
