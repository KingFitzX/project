import random
from . import csv_parser

LOREM_IPSUM = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas convallis hendrerit felis, ut porttitor felis facilisis ac. Aliquam aliquet ultricies odio, sit amet varius nibh. Fusce congue est ut tempus feugiat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam tincidunt lacus quis quam sollicitudin congue. Donec tristique dignissim fringilla. Quisque posuere, orci nec tristique lobortis, nunc leo imperdiet tellus, quis porttitor tortor lectus sit amet nisi. Aliquam tristique auctor ipsum ultricies ultrices.

Donec pulvinar volutpat neque sed varius. Etiam vulputate ante ac sapien laoreet, ut feugiat mauris varius. Nulla ut placerat libero, ac mollis nisl. Pellentesque placerat ex libero, nec consectetur velit ultricies eget. Vivamus massa sapien, finibus et vulputate vel, venenatis vitae augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. In posuere sapien vitae ante pellentesque eleifend. Quisque mattis massa non maximus suscipit. In in lectus nec libero malesuada malesuada. Donec vitae dui vel elit venenatis vulputate. Duis tincidunt ut leo fermentum fringilla. Proin lacinia metus id tincidunt vestibulum.'''

def gen_scenario():
    return {
        "scenario": LOREM_IPSUM,
        "parameters": randomise_both_country_parameters()
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
    }

def randomise_both_country_parameters():
    return {
        "country_alpha": randomise_parameters(provocation=True),
        "country_beta": randomise_parameters()
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

