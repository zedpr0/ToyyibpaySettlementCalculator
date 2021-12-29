from compute import *
computed_sum = compute_settlement_sum(settlement_data)


def bill_count():
    if len(computed_sum) == 1:
        print(f"There is {len(computed_sum)} campaign in the settlement file provided.\n")
    elif len(computed_sum) < 1:
        print(f"There are no campaigns in the settlement file provided.\n")
    else:
        print(f"There are {len(computed_sum)} campaigns in the settlement file provided.\n")



def bill_total():
    for key in computed_sum:
        print(f"Alhamdulillah, Campaign \"{key}\" has a current total of RM{computed_sum[key]} in donations.")


def print_new_line():
    print('')
