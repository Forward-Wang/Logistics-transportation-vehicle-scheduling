import pandas as pd

vehicles = pd.read_excel(r'E:\Logistics-transportation-vehicle-scheduling\res\input_vehicle_type.xlsx')
# format： remove spaces from column names
vehicles = vehicles.rename(columns=lambda x: x.replace(" ", ""))
# add cost items to vehicles
vehicles['vehicle_cnt'] = 0
vehicles['driving_distance'] = 0
vehicles['waiting_time'] = 0
vehicles['charging_time'] = 0


def calculate_cost_items():
    # according to the route, calculate the cost items

    for index in vehicles.index:
        # calculate the vehicle_cnt
        # TODO
        # calculate the driving_distance
        # TODO
        # calculate the waiting_time
        # TODO
        # calculate the charging_time
        # TODO
        return


def calculate_costs():
    # calculate the costs

    # declare and initialize variables
    unit_waiting_cost = 24
    unit_charging_cost = 100
    costs = {'fixed_cost': 0, 'transportation_cost': 0, 'waiting_cost': 0, 'charging_cost': 0}
    total_cost = 0

    # calculate 4 costs
    for index in vehicles.index:
        # calculate the fixed cost
        costs['fixed_cost'] += vehicles['vehicle_cnt'][index] * vehicles['vehicle_cost'][index]
        # calculate the transportation cost
        costs['transportation_cost'] += vehicles['unit_trans_cost'][index] * vehicles['driving_distance'][index]
        # calculate the waiting cost
        costs['waiting_cost'] += unit_waiting_cost * vehicles['waiting_time'][index]
        # calculate the charging cost
        costs['charging_cost'] += unit_charging_cost * vehicles['charging_time'][index]

    # calculate the total cost
    for cost_item in costs:
        total_cost += costs[cost_item]

    return total_cost


def main():
    calculate_cost_items()
    print(calculate_costs())


if __name__ == '__main__':
    main()