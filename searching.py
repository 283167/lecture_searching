from pathlib import Path
import json
import generators
import time

from generators import ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open(file_path, "r") as file:
        data = json.load(file)
        result = data[field]
        if field == "dna_sequence":
            return result
        elif type(result[0]) is int:
            return result
        else:
            return None


def linear_search(data, number):
    count_number = 0
    indexes = []
    i = 0
    for data[i] in data:
        if data[i] == number:
            count_number += 1
            indexes.append(i)
        i += 1
    result = {"positions": indexes, "count": count_number}
    return result


def binary_search(data, number):
    start = 0
    end = len(data)
    number_found = False
    while not number_found:
        mid = int((end + start) / 2)
        if data[mid] > number:
            end = mid
        elif data[mid] == number:
            return mid
        elif (start+1) == end:
            break
        else:
            start = mid
    if number_found == False:
        return None


def main(file_name, field, number, search_type):
    data = read_data(file_name, field)
    if search_type == "linear":
        search = linear_search(data, number)
    elif search_type == "binary":
        search = binary_search(data, number)
    return search


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    linear_times = []
    binary_times = []
    for size in sizes:
        data = ordered_sequence(size)
        start = time.perf_counter()
        linear_search(data, 8)
        end = time.perf_counter()
        duration = end - start
        linear_times.append(duration)
        start = time.perf_counter()
        binary_search(data, 8)
        end = time.perf_counter()
        duration = end - start
        binary_times.append(duration)
    print(linear_times, binary_times)

