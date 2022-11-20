import random
from . import text_gen
from . import csv_parser

def gen_scenario():
    random_params = randomise_both_country_parameters()
    scenario_text = text_gen.full_scenario_html(random_params)

    return {
        "scenario": scenario_text,
        "parameters": random_params
    }

def get_attr_description(attr_name):
    tempObj = csv_parser.DescriptionParser(attr_name)
    return tempObj.generate_descriptions()

def attr_descriptions():
    return {
        "cares_about": get_attr_description("cares_about"),
        "no_nukes": get_attr_description("no_nukes"),
        "aggression": get_attr_description("aggression"),
        "international_rep": get_attr_description("international_rep"),
        "population": get_attr_description("population"),
        "provocation": get_attr_description("provocation")
    }

def randomise_both_country_parameters():
    return {
        "country_alpha": randomise_country_parameter(provocation=True),
        "country_beta": randomise_country_parameter()
    }

def randomise_country_parameter(provocation=False):
    temp_dict = {
        "cares_about": random.random(),
        "no_nukes": random.random(),
        "agression": random.random(),
        "international_rep": random.random(),
        "population": random.random()
    }

    if provocation:
        temp_dict["provocation"] = random.random()

    return temp_dict

