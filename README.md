# project description

## NN Parameters:
Note that all of these are parameters for each nation.

Each parameter is a `float` value from 0 to 1 inclusive.

- cares_about
    - Represents how much the nation cares about the contention in question (e.g. human resources in country, oil imports)
    - Low values for little interest, high values for high interest (and more willing to protect/attack)


- no_nukes
    - Represents how many nuclear weapons the nation has
    - Exponential / Logarithmic scale to fit 0 to 1 scale


- aggression
    - Represents how willing a country is to attack with weapons or go to war
    - Based on past history of the country (as a description when converted to text)


- international_rep
    - Represents how much international support a country has
    - Affects if other countries would help this nation (e.g. catalytic effect)


- population 
    - Represents the population for the nation
    - Exponential / Logarithmic scale to fit 0 to 1 scale

