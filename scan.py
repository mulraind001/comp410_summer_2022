import os
import re


def scan_files():
    # supported file types
    supported_files = ['.docx', '.pdf', '.xlsx']

    # list of files found
    found_list = []

    # Walk all files starting from the files directory
    for root, dirs, files in os.walk('files'):
        # look for supported file types
        for name in files:
            file, ext = os.path.splitext(name)
            # if the file extension is in the supported list
            # add it to the found list.  Handle case sensitivity
            if ext.lower() in supported_files:
                found_list.append(os.path.join(root, name))
    return found_list


def show_aggie_pride():
    slogan_list = ['Aggie Pride - Worldwide']

    return slogan_list


if __name__ == '__main__':
    print(show_aggie_pride())
    print('---')
    print(scan_files())
