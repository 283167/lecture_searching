from pathlib import Path
import json


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


def main(file_name, field):
    data = read_data(file_name, field)
    return data


if __name__ == "__main__":
    print(main("sequential.json", "ordered_numbers"))
