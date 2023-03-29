calculations_to_unit = 20 * 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(num_of_days, custom_message):

    print(f"{num_of_days} days are {num_of_days * calculations_to_unit} {name_of_units}")
    print(custom_message)


days_to_units(35, "Awesome!")
