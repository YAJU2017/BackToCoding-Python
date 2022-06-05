calculation_to_units = 24
name_of_unit = "hours"


def day_to_unit(days):
    return f"{days} days are {days * calculation_to_units} {name_of_unit}"


def validate_execute_1():
    if user_input.isdigit():
        if int(user_input) > 0:
            x = day_to_unit(int(user_input))
            print(x)
        elif int(user_input) == 0:
            print(f"days value entered is {user_input}, it can not be zero")
    else:
        print("Invalid input")


def validate_execute(number_of_days):
    try:
        if int(number_of_days) > 0:
            x = day_to_unit(int(number_of_days))
            print(x)
        elif int(number_of_days) == 0:
            print(f"days value entered is {number_of_days}, it can not be zero")
        else:
            print("can accpet negative number")
    except ValueError:
        print("Invalid input")




if __name__ == "__main__":
    user_input = ""
    while user_input != "exit":
        user_input = input("Please provide the num of days as a commma separated list  to convert to hours\n")
        print(type(user_input))
        for num in user_input.split(","):
            validate_execute(num)
