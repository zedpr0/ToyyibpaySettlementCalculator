from xlsx import *
from file_name import *

settlement_data = read_settlement(request_file_name())


def compute_settlement_sum(settlement_list):
    settlement_dict = dict()
    for key, value in settlement_list:
        if key in settlement_dict:
            settlement_dict[key] = settlement_dict[key] + value
        else:
            settlement_dict[key] = value
    return settlement_dict
