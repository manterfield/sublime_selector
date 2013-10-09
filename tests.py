import unittest

import replace

class ReplaceTestCase(unittest.TestCase):

    def test_alpha_numeric_is_unchanged(self):
        text = 'abc123'
        output_text = replace.alpha_num('abc123')
        self.assertEqual(text, output_text)