import pandas as pd
import copy
import random

IGNORE_CHARS = ["-", ""]

def attr_le_pre(row, attr_name, value):
    return attr_name[row] in IGNORE_CHARS or attr_le(row, attr_name, value)

def attr_ge_pre(row, attr_name, value):
    return attr_name[row] in IGNORE_CHARS or attr_ge(row, attr_name, value)

def attr_le(row, attr_name, value):
    return value <= row[attr_name]

def attr_ge(row, attr_name, value):
    return value >= row[attr_name]

def get_attr_min(attr):
    return f"{attr}_min"

def get_attr_max(attr):
    return f"{attr}_max"

def get_modified_dict_from_dataframe(dataframe):
    out_list = []

    for _, row in dataframe.iterrows():
        temp_dict = {key: row[key] for key in dataframe.keys()}
        out_list.append(temp_dict)

    return out_list
    
def filter_on_predicate(predicate, dict):
    return [row for row in dict if predicate(row)]

class CSVParsing:
    def __init__(self, file_name) -> None:
        csv_file = pd.read_csv(file_name)
        self.__dict = get_modified_dict_from_dataframe(csv_file)

    def filter_with(self, attributes):
        out_dict = copy.deepcopy(self.__dict)

        for attr_name, attr_value in attributes:
            minv = get_attr_min(attr_name)
            maxv = get_attr_max(attr_name)

            out_dict = filter_on_predicate(
                lambda row: attr_ge_pre(row, minv, attr_value),
                out_dict
            )

            out_dict = filter_on_predicate(
                lambda row: attr_le_pre(row, maxv, attr_value),
                out_dict
            )
        
        return out_dict

    def pick_random_filtered(self, attributes):
        out_dict = self.filter_with(attributes)
        return random.choice(out_dict)

    
        