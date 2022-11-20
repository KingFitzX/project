import pandas as pd
import copy
import random
from . import constants
from . import filter
from . import text_gen_helper

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

def wrap(val):
    return "{" + val + "}"

def flip(val):
    val = val.replace(wrap("A"), wrap("C"))
    val = val.replace(wrap("B"), wrap("A"))
    val = val.replace(wrap("C"), wrap("B"))

    return val

def flip_key_name(key):
    if key[:2] == "a_":
        return f"b_{key[2:]}" 

    if key[:2] == "b_":
        return f"a_{key[2:]}" 

    return key

def flip_if(key, val):
    if filter.is_ignore_char(val) or key != "text":
        return val
    else:
        return flip(val)


def flip_and_merge_conflicts(in_dict):
    out_dict = []

    for row in in_dict:
        if filter.is_ignore_char(row["user"]):
            out_dict.append(
                {key: val for key, val in row.items() if key != "user"}
            )

            out_dict.append(
                {flip_key_name(key): flip_if(key, val) for key, val in row.items() if key != "user"}
            )

    return out_dict

class CSVParser:
    def __init__(self, name) -> None:
        self.name = name
        file_name = get_file_name_if_not(name)
        csv_file = pd.read_csv(f"./scenarios/csv_files/{file_name}")
        self.dict = get_modified_dict_from_dataframe(csv_file)

        if file_name == "conflicts.csv":
            self.dict = flip_and_merge_conflicts(self.__dict)

    def filter_with(self, filters: list[filter.Filter]):
        out_dict = copy.deepcopy(self.dict)
        
        for filter in filters:
            out_dict = filter.filter(out_dict)

        return out_dict 

    def pick_random_filtered(self, filters):
        out_dict = self.filter_with(filters)

        if len(out_dict) == 0:
            raise LookupError

        return random.choice(out_dict)

class DescriptionParser(CSVParser):
    def __init__(self, file_name):
        super().__init__(file_name)

    def generate_descriptions(self):
        return [{
            "min": row[filter.FilterBetween.get_attr_min(self.name)],
            "max": row[filter.FilterBetween.get_attr_max(self.name)],
            "description": text_gen_helper.single_country_sub(row["text"], "this country")
        } for row in self.dict]


    
        