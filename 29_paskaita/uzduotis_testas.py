import unittest
from uzduotis import prideti_prie_saraso, ar_lyginis, ar_palindromas, palyginti_sarasus

class TestUzduotis(unittest.TestCase):

    def setUp(self): # duomenų paruošimas visai klasei
        self.sarasas1 = ['c', 'f','z', 'g']
        self.sarasas2 = ['a', 'b']
        self.atsakymas = ['a', 'c', 'f', 'g','z']
        self.ats = [2, 3, 10, 21]
        self.sk_sar = [10, 21, 3]

    def tearDown(self): # duomenų išvalymas
        self.sarasas1 = None
        self.sarasas2 = None
        self.atsakymas = None
        self.sk_sar = None
        self.ats = None


    def test_prideti_prie_saraso(self):
        rezultatas = prideti_prie_saraso(self.sk_sar, 2)
        self.assertEqual(rezultatas, self.ats)

    def test_ar_lyginis(self):
        rezultatas1 = ar_lyginis(5)
        # rezultatas2 = ar_lyginis(10)
        self.assertFalse(rezultatas1)
        # self.assertTrue(rezultatas2)

    def test_ar_palindromas(self):
        tekstas = ar_palindromas('Sėdėk užu kėdės')
        self.assertTrue(tekstas)

    def test_ar_palindromas2(self):
        tekstas = ar_palindromas('Pirmadienis')
        self.assertFalse(tekstas)
        # self.assertEqual(type(tekstas), '')

    def test_palyginti_sarasus(self):
        rezultatas = palyginti_sarasus([1,2,3], [5,6,7])
        # self.assertEqual(True, rezultatas)
        self.assertNotEqual(False, rezultatas)

if __name__ == '__main__':
    unittest.main()