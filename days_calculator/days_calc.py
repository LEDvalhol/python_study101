calculations_to_units = 20 * 24 * 60 * 60
name_of_units = "seconds"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_units}"


user_input = input("Hey user, enter number of days and I will convert it for you!\n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)
