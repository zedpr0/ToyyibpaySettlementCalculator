import os


def request_file_name():
    file_name = (input("\nPlease enter filename to compute settlement amount: ")).rstrip()
    if os.name != 'nt':
        file_name = file_name.replace('\u005C ', ' ')
    else:
        file_name = file_name.replace('\u0022 ', '')
    return file_name
