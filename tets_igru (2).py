import unittest
from game import Game15

class TestGame15(unittest.TestCase):
    def setUp(self):
        self.igra = Game15()
    def test_nachalnoe_sostoyanie(self):
        pole = self.igra.poluchit_pole()
        self.assertEqual(pole[3][3], 0)
        self.assertEqual(pole[0][0], 1)
    def test_normalnye_hodi(self):
        self.assertTrue(self.igra.hodit('verh'))
        self.assertEqual(self.igra.poluchit_pustuyu_poziciyu(), (2, 3))
    def test_plohie_hodi(self):
        self.assertFalse(self.igra.hodit('niz'))
        self.assertFalse(self.igra.hodit('pravo'))
    def test_pobeda(self):
        igra = Game15()
        self.assertTrue(igra.proverit_pobedu())
        igra.hodit('verh')
        self.assertFalse(igra.proverit_pobedu())
    def test_peremeshat(self):
        self.igra.peremeshat(10)
        self.assertFalse(self.igra.proverit_pobedu())
        self.assertGreater(self.igra.poluchit_schetchik_hodov(), 0)
if __name__ == '__main__':
    unittest.main()