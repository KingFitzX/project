from . import csv_parser, filter
import random

def substitute_values(string, values):
    for place_holder, new_value in values.items():
        string = string.replace("{" + place_holder + "}", new_value)

    return string

def get_single_country_row(value, params):
    cp_object = csv_parser.CSVParser(value)
    filter_list = filter.single_country_filter(params)

    random_row = cp_object.pick_random_filtered(filter_list)
    return random_row

def single_country_sub(string, country_name):
    return substitute_values(string, {"A": country_name})

def get_both_country_row(value, params):
    cp_object = csv_parser.CSVParser(value)
    filter_list = filter.both_country_filter(params)

    random_row = cp_object.pick_random_filtered(filter_list)
    return random_row

def both_country_sub(string, country_alpha, country_beta):
    return substitute_values(string, {"A": country_alpha, "B": country_beta})

def get_single_country_text(value, params, country_name):
    row = get_single_country_row(value, params)
    string = single_country_sub(row["text"], country_name)

    return string

def get_both_country_text(value, params, country1_name, country2_name):
    row = get_both_country_row(value, params)
    string = both_country_sub(row["text"], country1_name, country2_name)

    return string

