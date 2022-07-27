from scan import scan_files, get_file_text
import re


# https://developers.google.com/edu/python/regular-expressions
# https://regex101.com/
def find_us_phone_numbers(text):
    match = re.search(r'(\(?\d{3}\)?(\s{1}|[-.])\d{3}[-.]\d{4})', text)
    if match:
        return True
    return False

def find_us_street_address(text):
    matchLong = re.search(r'(\d{3,4}\s{1}[a-zA-z\s]*,\s{1}[a-zA-z\s-]*,\s{1}[A-Z]{2},\s{1}(\d{5}-\d{4}|\d{5}))', text)
    matchShort = re.search(r'\d{3,4}\s{1}[a-zA-Z]*\s((\d{1,3}[a-zA-Z]*\s?)*|[a-zA-Z\s]*)(Street|Terrace|Lane|Lanes|Drive|Alley|Circle|Avenue|Boulevard){1}', text)

    if matchLong or matchShort:
        return True
    return False

def find_credit_card_number(text):
    match = re.search(r'\d{4}[- ]\d{4}[- ]\d{4}[- ]\d{4}', text)
    if match:
        return True
    return False

def find_twitter_handle(text):
    match = re.search(r'\B@\w*([A-Za-z0-9_]+)\w*', text)
    if match:
        return True
    return False

def find_bank_acc_number(text):
    match = re.search(r'^(\d{10}|\d{12})$', text)
    if match:
        return True
    return False

def find_email_address(text):
    match = re.search(r'^([\w!-#+$&~?*=]+@[\w.]+)$', text)
    if match:
        return True
    return False

# def find_us_social_secruity(text):
#     match = re.search(r'', text)
#     if match:
#         return True
#     return False