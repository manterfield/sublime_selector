import unittest

import replace

class ReplaceTestCase(unittest.TestCase):

    def test_alpha_numeric(self):
        text = 'abc123'
        output_text = replace.alpha_num(text)
        self.assertEqual(text, output_text)

        text = 'abc 123 **'
        output_text = replace.alpha_num(text)
        self.assertNotEqual(text, output_text)