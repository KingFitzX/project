LOREM_IPSUM = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas convallis hendrerit felis, ut porttitor felis facilisis ac. Aliquam aliquet ultricies odio, sit amet varius nibh. Fusce congue est ut tempus feugiat. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam tincidunt lacus quis quam sollicitudin congue. Donec tristique dignissim fringilla. Quisque posuere, orci nec tristique lobortis, nunc leo imperdiet tellus, quis porttitor tortor lectus sit amet nisi. Aliquam tristique auctor ipsum ultricies ultrices.

Donec pulvinar volutpat neque sed varius. Etiam vulputate ante ac sapien laoreet, ut feugiat mauris varius. Nulla ut placerat libero, ac mollis nisl. Pellentesque placerat ex libero, nec consectetur velit ultricies eget. Vivamus massa sapien, finibus et vulputate vel, venenatis vitae augue. Interdum et malesuada fames ac ante ipsum primis in faucibus. In posuere sapien vitae ante pellentesque eleifend. Quisque mattis massa non maximus suscipit. In in lectus nec libero malesuada malesuada. Donec vitae dui vel elit venenatis vulputate. Duis tincidunt ut leo fermentum fringilla. Proin lacinia metus id tincidunt vestibulum.'''

def gen_scenario():
    return {
        "scenario": LOREM_IPSUM,
        "parameters": {
            "country_alpha": randomise_paramters(),
            "country_beta": randomise_paramters()
        }
    }

def randomise_paramters():
    return {
        "cares_about": 0.,
        "no_nukes": 0.,
        "agression": 0.,
        "international_rep": 0.,
        "population": 0.
    }
