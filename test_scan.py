import unittest
import pdfplumber
import os
import re
from scan import show_aggie_pride, scan_files


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
                m = re.search(r'\d+-\d+', text)
                self.assertTrue(m)

    def test_ssn(self):
        # Walk all files starting from the files directory
        for root, dirs, files in os.walk('files'):
            for name in files:
                # Look for files that should have ssn in them
                if name == 'ss_info.pdf':
                    # open the file
                    with pdfplumber.open(os.path.join(root, name)) as pdf:
                        # loop through each page in the pdf
                        for p in pdf.pages:
                            # extract the text as a str
                            text = p.extract_text()
                            # check for the ssn
                            m = re.search(r'\d{3}-\d{2}-\d{4}', text)
                            self.assertTrue(m)

    def test_scan_files(self):
        # Test to make sure scan_files returns the expected results
        expected_result = ['files/november_statement.pdf',
                           'files/Documents/twitter_info.docx',
                           'files/Documents/Statements/Retirement/ss_info.pdf',
                           'files/Downloads/address_book.xlsx']

        # Make expected_result os safe by checking the seperator
        if os.sep != '/':
            for i in range(len(expected_result)):
                expected_result[i] = expected_result[i].replace('/', os.sep)

        self.assertEqual(scan_files(), expected_result)


if __name__ == '__main__':
    unittest.main()
