import pandas as pd
import copy
import random
from . import constants
from . import filter

def get_modified_dict_from_dataframe(dataframe):
    out_list = []

    for _, row in dataframe.iterrows():
        temp_dict = {key: row[key] for key in dataframe.keys()}
        out_list.append(temp_dict)

    return out_list

def get_file_name_if_not(name):
    if name[-4:] == ".csv":
        return name
    else:
        return f"{name}.csv"

class CSVParser:
    def __init__(self, file_name) -> None:
        file_name = get_file_name_if_not(file_name)

        csv_file = pd.read_csv(f"./scenarios/csv_files/{file_name}")
        self.__dict = get_modified_dict_from_dataframe(csv_file)

    def filter_with(self, filters: list[filter.Filter]):
        out_dict = copy.deepcopy(self.__dict)
        
        for filter in filters:
            out_dict = filter.filter(out_dict)

        return out_dict 

    def pick_random_filtered(self, filters):
        out_dict = self.filter_with(filters)

        if len(out_dict) == 0:
            raise LookupError

        return random.choice(out_dict)

    
        