from . import text_gen_helper
import random
import markdown

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

def gen_section(heading, *args):
    out_string = f"##{heading}"

    for part in args:
        out_string += f"\n{part}"

    return out_string

def full_scenario_from_params_md(params):
    user_country = "your country"
    enemy_country = get_random_country_name()

    scenario_text = text_gen_helper.get_both_country_text("conflicts", params, user_country, enemy_country)

    user_no_nukes = text_gen_helper.get_single_country_text("no_nukes", params["country_alpha"], user_country)
    user_cares_about = text_gen_helper.get_single_country_text("cares_about", params["country_alpha"], user_country)
    user_aggression = text_gen_helper.get_single_country_text("aggression", params["country_alpha"], user_country)
    user_international_rep = text_gen_helper.get_single_country_text("international_rep", params["country_alpha"], user_country)
    user_population = text_gen_helper.get_single_country_text("population", params["country_alpha"], user_country)

    enemy_no_nukes = text_gen_helper.get_single_country_text("no_nukes", params["country_beta"], enemy_country)
    enemy_cares_about = text_gen_helper.get_single_country_text("cares_about", params["country_beta"], enemy_country)
    enemy_aggression = text_gen_helper.get_single_country_text("aggression", params["country_beta"], enemy_country)
    enemy_international_rep = text_gen_helper.get_single_country_text("international_rep", params["country_beta"], enemy_country)
    enemy_population = text_gen_helper.get_single_country_text("population", params["country_beta"], enemy_country)

    nuke_sec = gen_section("Nukes", user_no_nukes, enemy_no_nukes)
    cares_sec = gen_section("Conflict Significance", user_cares_about, enemy_cares_about)
    aggression_sec = gen_section("Historic Aggression", user_aggression, enemy_aggression)
    rep_sec = gen_section("International Reputation and Backing", user_international_rep, enemy_international_rep)
    population_sec = gen_section("Population", user_population, enemy_population)
    

    return f"#The Situation\n{scenario_text}\n\n{nuke_sec}\n\n{cares_sec}\n\n{aggression_sec}\n\n{rep_sec}\n\n{population_sec}"

def full_scenario_html(params):
    return markdown.markdown(full_scenario_from_params_md(params))