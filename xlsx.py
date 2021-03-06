import openpyxl


def read_settlement(xlsx_file_location):
    settlement_file = openpyxl.load_workbook(xlsx_file_location)
    sheet = settlement_file.active
    column_a = list()
    column_l = list()
    for cell in sheet['A']:
        column_a.append(cell.value)
    for cell in sheet['L']:
        column_l.append(cell.value)
    settlement_list = list(zip(column_a[1:], column_l[1:]))
    return settlement_list


