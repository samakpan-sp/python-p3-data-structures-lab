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
# 1: get_names()
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
name_ofS = get_names(spicy_foods)
print(name_ofS)
print("ANS: 1 ++++++++")
# 2: get_spiciest_foods()
def get_spiciest_foods(spicy_foods):
    return [k for k in spicy_foods if k["heat_level"] >= 5]
    
heat_level = get_spiciest_foods(spicy_foods)
print(heat_level)
print("ANS: 2 ++++++++")

pass
# 3: print_spicy_foods()
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]

        # Create a string of "🌶" emojis based on the heat level
        heat_emojis = "🌶" * heat_level

        #Format and print the spicy food information
        print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

# Example usage:
print_spicy_foods(spicy_foods)
print("ANS: 3 ++++++++")

# 4: get_spicy_food_by_cuisine()

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
  result = [spicy_food for spicy_food in spicy_foods if spicy_food["cuisine"] == cuisine]
  if not result:
      return None
  
  return result[0]

result = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result)
pass

# 5: print_spiciest_foods()
print("ANS: 4 ++++++++")
def print_spiciest_foods(spicy_foods):
    for spicy in spicy_foods:
        if spicy["heat_level"] >= 5:
            name = spicy["name"]
            cuisine = spicy["cuisine"]
            heat_level = spicy["heat_level"]
            heat_emojis = "🌶" * heat_level
            print(f"{name} ({cuisine}) | Heat Level: {heat_emojis}")

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6},
]

print_spiciest_foods(spicy_foods)

# def print_spiciest_foods(spicy_foods):
#     for spicy in spicy_foods:
#         if spicy["heat_level"] >= 5:
#             name = spicy["name"]
#             cuisine = spicy["cuisine"]
#             heat_level = spicy["heat_level"]
#             heat_emojis = "🌶" * heat_level
#             print(f"{name} ({cuisine}) | Heat Level:{heat_emojis}")
       
# result = print_spiciest_foods(spicy_foods)
# print(result)

pass
print("ANS: 5 ++++++++")
# 6: et_average_heat_level()
def get_average_heat_level(spicy_foods):
    count = 0
    total_heat = 0

    for spicy_food in spicy_foods:
        if "heat_level" in spicy_food:
            total_heat += spicy_food["heat_level"]
            count += 1
    
    if count == 0:
        return 0
    
    average_h = total_heat / count
    return round(average_h)

av_h_l = get_average_heat_level(spicy_foods)
print(av_h_l)

print("ANS: 6 ++++++++")
pass



def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
new_spicy_food = {
    'name': 'namree',
    'cuisine':'makne',
    'heat_level': 'kil'
}
updatedspass = create_spicy_food(spicy_foods, new_spicy_food)
print(updatedspass)
