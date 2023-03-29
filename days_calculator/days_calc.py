""" THIS IS THE GLOBAL SCOPE """
calculations_to_unit = 20 * 24 * 60 * 60
name_of_units = "seconds"

""" THIS IS THE LOCAL SCOPE """


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculations_to_unit} {name_of_units}")
    print(custom_message)


def scope_check(num_of_days):
    my_var = "a variable inside function"
    print(name_of_units)
    print(num_of_days)
    print(my_var)


days_to_units(35, "Awesome!")
scope_check(20)
