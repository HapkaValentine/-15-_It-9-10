import unittest
from game import Game15

class TestGame15(unittest.TestCase):
    def setUp(self):
        self.g = Game15()
    def test_start_pole(self):
        pole = self.g.poluchit_pole()
        self.assertEqual(pole[3][3], 0)
        self.assertEqual(pole[0][0], 1)
    def test_hod_up(self):
        ok = self.g.hodit("verh")
        self.assertTrue(ok)
        now = self.g.poluchit_pustuyu_poziciyu()
        self.assertEqual(now, (2, 3))
    def test_plohie_hodi(self):
        res1 = self.g.hodit("niz")
        res2 = self.g.hodit("pravo")
        self.assertFalse(res1)
        self.assertFalse(res2)
    def test_pobedka(self):
        game2 = Game15()
        self.assertTrue(game2.proverit_pobedu())
        game2.hodit("verh")
        self.assertFalse(game2.proverit_pobedu())
    def test_mix(self):
        self.g.peremeshat(10)
        self.assertFalse(self.g.proverit_pobedu())
        c = self.g.poluchit_schetchik_hodov()
        self.assertGreater(c, 0)
if __name__ == "__main__":
    unittest.main()

