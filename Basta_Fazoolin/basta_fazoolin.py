# Making the Menus
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{name} menu available from {start_time} to {end_time}".format(name=self.name, start_time=self.start_time, end_time=self.end_time)

  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
        total_price += self.items[item]
    return total_price

# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu("brunch", brunch_items, 1100, 1600)

# Early_bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu("early_bird", early_bird_items, 1500, 1800)

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu("dinner", dinner_items, 1700, 2300)

# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu("kids", kids_items, 1100, 2100)

print(brunch_menu)
# a breakfast order for one order of pancakes, one order of home fries, and one coffee.
print(brunch_menu.calculate_bill(["pancakes", "home fries", "coffee"]))

# Our last guests ordered the salumeria plate and the vegan mushroom ravioli. 
print(early_bird_menu.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# Creating the Franchises
class Franchise(Menu):
  def __init__(self, address, menus):
    self.addrees = address
    self.menus = menus

  def __repr__(self):
    return "The restaurant is located at {address}".format(address=self.address)
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

# Check available menus
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

# Creating Businesses!
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

new_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Take a'Arepa business
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu("Take a’ Arepa", arepas_items, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

arepas = Business("Take a' Arepa", [arepas_place])

print(arepas.franchises[0].menus[0])