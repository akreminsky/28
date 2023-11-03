import unittest

from main import ConquestCampaign


class ConquestTests(unittest.TestCase):
    def test_conq_small(self):
        self.assertEqual(ConquestCampaign(3, 2, 2, [2, 2]), 3)
        self.assertEqual(ConquestCampaign(2, 2, 2, [2, 2, 1, 1]), 2)
        self.assertEqual(ConquestCampaign(1, 1, 2, [1, 1]), 1)

    def test_conq_large_batallions(self):
        self.assertEqual(ConquestCampaign(2, 2, 2, [1, 1, 1, 2, 2, 1, 2, 2]), 1)
        self.assertEqual(ConquestCampaign(2, 2, 2, [1, 2, 2, 1, 2, 2]), 2)
