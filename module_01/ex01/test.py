from game import Stark
from unittest import TestCase
from unittest.mock import patch
from io import StringIO


class TestStark(TestCase):
    def test_stark(self):
        stark = Stark("Arya")
        self.assertEqual(stark.first_name, "Arya")
        self.assertEqual(stark.is_alive, True)
        self.assertEqual(stark.family_name, "Stark")
        self.assertEqual(stark.house_words, "Winter is Coming")
        stark.die()
        self.assertEqual(stark.is_alive, False)

    def test_stark_no_first_name(self):
        with self.assertRaises(AssertionError):
            Stark()

    def test_stark_no_is_alive(self):
        with self.assertRaises(AssertionError):
            Stark("Arya", "Alive")

    @patch("sys.stdout", new_callable=StringIO)
    def test_stark_print_house_words(self, mock_stdout):
        stark = Stark("Arya")
        stark.print_house_words()
        self.assertEqual(mock_stdout.getvalue(), "Winter is Coming\n")

    def test_stark_die(self):
        stark = Stark("Arya")
        stark.die()
        self.assertEqual(stark.is_alive, False)


test = TestStark()

test.test_stark()
test.test_stark_no_first_name()
test.test_stark_no_is_alive()
test.test_stark_print_house_words()
test.test_stark_die()
