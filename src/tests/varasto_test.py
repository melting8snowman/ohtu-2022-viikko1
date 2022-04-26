import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)


    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)


    def test_txt(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")


    def test_uudella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_negat_lisays_nollaa_saldoa(self):
        self.varasto.lisaa_varastoon(-18)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liika_lisays_max_tilavus(self):
        self.varasto.lisaa_varastoon(1000)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negat_ottaminen_nolla(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(saatu_maara, 0)

    def test__ottaminen_enemman_kuin_mahd(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(1000)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_negat_alkusaldo(self):
        var = Varasto(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)


    def test_negat_alkutilavuus(self):
        var = Varasto(-2)
        self.assertAlmostEqual(self.varasto.tilavuus, 10)


    def test_negat_alkusaldo(self):
        var = Varasto(-2, alku_saldo = -30)
        self.assertAlmostEqual(self.varasto.saldo, 0)
