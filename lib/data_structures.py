spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

new_food = {
    'name': 'Griot',
    'cuisine': 'Haitian',
    'heat_level': 10,
}

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food) 
    return spicy_foods 

updated_spicy_foods = create_spicy_food(spicy_foods, new_food)

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        chili_peppers = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_peppers}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"].lower() == cuisine.lower():  
            return food
    return None  

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  
    for food in spiciest_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        chili_peppers = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_peppers}")

def get_average_heat_level(spicy_foods):
    if not spicy_foods:  
        return 0  

    total_heat = sum(food["heat_level"] for food in spicy_foods)  
    average_heat = total_heat // len(spicy_foods)  # Keep this if you want an integer result
    return average_heat

