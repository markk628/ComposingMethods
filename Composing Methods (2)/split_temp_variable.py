# NY Burger
patty = 70 # [gr]
pickle = 20 # [gr]
tomatoes = 25 # [gr]
lettuce = 15 # [gr]
buns = 95 # [gr]

# Seoul Kimchi Burger
kimchi = 30 # [gr]
mayo = 5 # [gr]
golden_fried_onion = 20 # [gr]

def get_ny_burger_weight():
    return (2 * patty + 4 * pickle + 3 * tomatoes + 2 * lettuce + 2 * buns)

def get_seoul_kimchi_burger_weight():
    return (2 * patty + 4 * pickle + 3 * tomatoes + kimchi + mayo + golden_fried_onion + 2 * buns)

ny_burger_weight = get_ny_burger_weight() 
print("NY Burger Weight", ny_burger_weight)

seoul_kimchi_burger_weight = get_seoul_kimchi_burger_weight()
print("Seoul Kimchi Burger Weight", seoul_kimchi_burger_weight)