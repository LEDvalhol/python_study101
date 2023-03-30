calculations_to_units = 20 * 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_units}")


days_to_units(20)
days_to_units(30)


