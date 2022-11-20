from . import text_gen_helper
import random

def get_random_country_name():
    with open("scenarios/country_names.txt") as names:
        possible_names = [name.strip() for name in names]

    return random.choice(possible_names)        
            
def get_text_no_nuke(s_params, name):
    return text_gen_helper.get_single_country_text("no_nuke", s_params, name)

def get_text_cares_about(s_params, name):
    return text_gen_helper.get_single_country_text("cares_about", s_params, name)

def get_text_population(s_params, name):
    return text_gen_helper.get_single_country_text("population", s_params, name)
    
def get_text_aggression(s_params, name):
    return text_gen_helper.get_single_country_text("aggression", s_params, name)

def full_scenario_from_params(params):
    user_country = "your country"
    enemy_country = get_random_country_name()

    


