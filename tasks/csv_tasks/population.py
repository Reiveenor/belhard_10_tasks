"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""

import pandas as pd


def max_delta():
    r_file = pd.read_csv('world_population.csv', delimiter=',')

    max_value = r_file['ChangePerc'].max()
    for key, value in r_file['ChangePerc'].items():
        if value == max_value:
            return f"Наибольший прирост населения был в {r_file['Year'][key]} году и составил {max_value}%"


if __name__ == '__main__':
    print(max_delta())
