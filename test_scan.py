import unittest
import pdfplumber
import os
import re
from scan import show_aggie_pride


class ScanTests(unittest.TestCase):
    def test_aggie_pride(self):
        slogans = show_aggie_pride()

        self.assertIn('Aggie Pride - Worldwide', slogans)

    def test_pdf_parse(self):
        # get a platform safe path to a test pdf file
        pdf_file = os.path.join('files', 'november_statement.pdf')

        # open the file
        with pdfplumber.open(pdf_file) as pdf:
            # loop through each page in the pdf
            for p in pdf.pages:
                # extract the text as a str
                text = p.extract_text()

                # Check for the name that should be in this PDF
                self.assertIn('Name: John Smith', text)

                # Check for the account number
                self.assertIn('Account Number: 3942-29992', text)

                # Regex match on the account number
                self.assertRegexpMatches(text, r'\d+-\d+')


if __name__ == '__main__':
    unittest.main()
