# string concatenation

# name = "Rakib Hasan"

#concate different ways 

# print("My name is "+name)
# print("My name is {}".format(name))
# print(f"My name is {name}")

country_name = input("Name of the country: ")
situated = input("Where: ")
country_1 = input("Neighbour country: ")
country_2 = input("Neighbour country: ")
live_in = input("People live in: ")
how_is_bangladesh = input("How is Bangladesh: ")

madlibs = f"""{country_name}, officially the people's Republic of Bangladesh is a country in {situated}. Bangladesh share land with {country_1} and {country_2}. Most of the people here live in {live_in}. It's a {how_is_bangladesh} country."""
        
print(madlibs)