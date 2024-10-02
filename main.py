"""
Your Name
Your Student Number
Assignment 1
Date
"""

def food_choice_program():
    name = "Your Name"
    student_number = "Your Number"
    
    # Prompt for the food category
    food_choice = int(input("Choose a food category:\n1 for Fruits\n2 for Vegetables\n3 for Meat\n"))

    if food_choice < 0:
        print("Negative food choice not allowed")
        print(f"{name}, {student_number}")
        return
    elif food_choice not in [1, 2, 3]:
        print("Invalid food choice")
        print(f"{name}, {student_number}")
        return

    # Food category selection
    if food_choice == 1:  # Fruits
        fruit_choice = int(input("Choose a fruit:\n1 for Apples\n2 for Oranges\n"))
        if fruit_choice < 0:
            print("Negative fruit choice not allowed")
            print(f"{name}, {student_number}")
            return
        elif fruit_choice not in [1, 2]:
            print("Invalid fruit choice")
            print(f"{name}, {student_number}")
            return
        food_type = "Apples" if fruit_choice == 1 else "Oranges"
        
    elif food_choice == 2:  # Vegetables
        veg_choice = int(input("Choose a vegetable:\n1 for Cucumbers\n2 for Lettuce\n"))
        if veg_choice < 0:
            print("Negative vegetable choice not allowed")
            print(f"{name}, {student_number}")
            return
        elif veg_choice not in [1, 2]:
            print("Invalid vegetable choice")
            print(f"{name}, {student_number}")
            return
        food_type = "Cucumbers" if veg_choice == 1 else "Lettuce"
        
    elif food_choice == 3:  # Meat
        meat_choice = int(input("Choose a meat:\n1 for Chicken\n2 for Pork\n"))
        if meat_choice < 0:
            print("Negative meat choice not allowed")
            print(f"{name}, {student_number}")
            return
        elif meat_choice not in [1, 2]:
            print("Invalid meat choice")
            print(f"{name}, {student_number}")
            return
        food_type = "Chicken" if meat_choice == 1 else "Pork"

    # Size selection
    size_choice = int(input("Choose a size:\n1 for Small\n2 for Medium\n3 for Large\n"))
    if size_choice < 0:
        print("Negative size choice not allowed")
        print(f"{name}, {student_number}")
        return
    elif size_choice not in [1, 2, 3]:
        print("Invalid size choice")
        print(f"{name}, {student_number}")
        return

    # Final output of what user choosed
    size = "Small" if size_choice == 1 else "Medium" if size_choice == 2 else "Large"
    print(f"{size} {food_type}")

# Run's the whole program
food_choice_program()