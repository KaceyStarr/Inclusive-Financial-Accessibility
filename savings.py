import math 
# calculates balance from number specified by user
def calc_perc():
    try: 
        balance = float(input("Enter balance: "))

        saving_perc = float(input("How much do you want to save? (e.g., 20 for 20%): "))

        saving_bal = (saving_perc / 100) * balance

        print(f"{saving_bal}% of {balance} is {saving_bal:.2f}")

    except ValueError:
        print("Please enter a valid number.")
# Runs function 
calc_perc()