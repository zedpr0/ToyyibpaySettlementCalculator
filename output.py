from compute import *
computed_sum = compute_settlement_sum(settlement_data)


def bill_count():
    print(f"There are {len(computed_sum)} bills in the settlement file provided.\n")


def bill_total():
    for key in computed_sum:
        print(f"Alhamdulillah, Campaign \"{key}\" has a current total of RM{computed_sum[key]} in donations.")


def print_new_line():
    print('')
