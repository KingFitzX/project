def substitute_values(string, values):
    for place_holder, new_value in values.items():
        string = string.replace("{" + place_holder + "}", new_value)

    return string
