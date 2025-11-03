def main():

    athletes = []

    while True:
        name = input("Enter athlete's name: ")

        gender = input("Enter athlete's gender (male/female): ")

        grade = input(
            "Enter athlete's grade (Beginner, Intermediate, Elite): ")

        weight = float(input("Enter athlete's current weight (kg): "))

        weight_category = input(
            "Enter athlete's competition weight category (Heavyweight, Light-Heavyweight, Middleweight, Light-Middleweight, Lightweight, Flyweight): ")

        competitions = int(
            input("Enter number of competitions entered this month: "))

        coaching_hours = int(
            input("Enter number of private coaching hours (0-5): "))

        if coaching_hours < 0 or coaching_hours > 5:
            print("Invalid input! Please enter a number between 0 and 5.")
            continue

        if grade == "Beginner":
            training_cost = 25.00
        elif grade == "Intermediate":
            training_cost = 30.00
        elif grade == "Elite":
            training_cost = 35.00
        else:
            print("Invalid grade level!")
            continue

        coaching_cost = coaching_hours * 9.50

        if grade == "Intermediate" or grade == "Elite":
            competition_cost = competitions * 22.00
        else:
            competition_cost = 0

        weight_limits = {
            "Heavyweight": 100,
            "Light-Heavyweight": 100,
            "Middleweight": 90,
            "Light-Middleweight": 81,
            "Lightweight": 73,
            "Flyweight": 66,
        }

        if weight_category not in weight_limits:
            print("Invalid weight category!")
            continue


        category_limit = weight_limits[weight_category]
        if weight > category_limit:
            weight_comparison = "over the limit"
        else:
            weight_comparison = "under the limit"

        total_cost = training_cost + coaching_cost + competition_cost

        athlete_data = {
            "name": name,
            "training_cost": training_cost,
            "coaching_cost": coaching_cost,
            "competition_cost": competition_cost,
            "total_cost": total_cost,
            "weight_comparison": weight_comparison
        }

        athletes.append(athlete_data)

        print("\nAthlete: ", name)
        print("Itemized Costs:")
        print("Training Plan Cost: £", format(training_cost, ".2f"))
        print("Coaching Cost: £", format(coaching_cost, ".2f"))
        print("Competition Fees: £", format(competition_cost, ".2f"))
        print("Total Monthly Cost: £", format(total_cost, ".2f"))
        print("Weight Comparison: Your weight is", weight_comparison,
              "for the", weight_category, "category.\n")


        another = input("Do you want to add another athlete? (y/n): ")
        if another.lower() != "y":
            break

main()



