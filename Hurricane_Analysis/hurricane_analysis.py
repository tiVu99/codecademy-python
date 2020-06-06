# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
  updated_list = []
  for cost in damages:
    if 'M' in cost:
     updated_list.append(float(cost.replace('M', ''))*1000000)
    elif 'B' in cost:
     updated_list.append(float(cost.replace('B', ''))*1000000000)
    else:
      updated_list.append(cost)
  return updated_list

#print(update_damages(damages))

updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:
def create_dictionary(names, months, years, max_sustained_winds, areas_affected,updated_damages, deaths):

  hurricanes = dict()
  num_hurricanes = len(names)

  for i in range(num_hurricanes):
    hurricanes[names[i]] = {"Name": names[i],
                          "Month": months[i],
                          "Year": years[i],
                          "Max Sustained Wind": max_sustained_winds[i],
                          "Areas Affected": areas_affected[i],
                          "Damage": updated_damages[i],
                          "Deaths": deaths[i]}
  return hurricanes

# create hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
#print(hurricanes["Cuba I"])

# write your construct hurricane by year dictionary function here:
def year_dictionary(hurricanes):

  hurricanes_by_year = {}

  for cane in hurricanes:
    current_year = hurricanes[cane]["Year"]
    if current_year not in hurricanes_by_year:
      hurricanes_by_year[current_year] = [hurricanes[cane]]
    else:
      hurricanes_by_year[current_year].append(hurricanes[cane])

  return hurricanes_by_year

hurricanes_by_year = year_dictionary(hurricanes)
#print(hurricanes_by_year[1932])

# write your count affected areas function here:
def count_affected_areas(hurricanes):
  areas_dict = {}

  for cane in hurricanes:
    affected_areas = hurricanes[cane]["Areas Affected"]
    for area in affected_areas:
      if area in areas_dict:
        areas_dict[area] += 1
      else:
        areas_dict[area] = 1
  return areas_dict

count_affected_areas = count_affected_areas(hurricanes)
#print(count_affected_areas)

# write your find most affected area function here:
def most_affected_area(count_affected_areas):
  max_area = 'Mexico'
  max_area_count = 0

  for area in count_affected_areas:
    if count_affected_areas[area] > max_area_count:
      max_area = area
      max_area_count = count_affected_areas[area]
  
  return max_area, max_area_count

most_affected_area = most_affected_area(count_affected_areas)
#print(most_affected_area)

# write your greatest number of deaths function here:
def most_deaths(hurricanes):

  most_deaths_cane = "Cuba I"
  most_deaths_count = 0

  for cane in hurricanes:
    if hurricanes[cane]["Deaths"] > most_deaths_count:
      most_deaths_cane = cane
      most_deaths_count = hurricanes[cane]["Deaths"]
  
  return most_deaths_cane, most_deaths_count

most_deaths_cane = most_deaths(hurricanes)
#print(most_deaths_cane)

# write your catgeorize by mortality function here:
def catgeorize_by_mortality(hurricanes):
  mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

  hurricanes_by_mortality = {0:[], 1: [], 2: [], 3: [], 4: [], 5: []}

  for cane in hurricanes:
    num_deaths = hurricanes[cane]["Deaths"]
    if num_deaths == mortality_scale[0]:
       hurricanes_by_mortality[0].append(hurricanes[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
       hurricanes_by_mortality[1].append(hurricanes[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
       hurricanes_by_mortality[2].append(hurricanes[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
       hurricanes_by_mortality[3].append(hurricanes[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
       hurricanes_by_mortality[4].append(hurricanes[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_by_mortality[5].append(hurricanes[cane])
  return hurricanes_by_mortality

hurricanes_by_mortality = catgeorize_by_mortality(hurricanes)
#print(hurricanes_by_mortality[5])

# write your greatest damage function here:
def greatest_damage(hurricanes):

  most_damage_cane = 'Cuba I'
  most_damage_count = 0

  for cane in hurricanes:
    if hurricanes[cane]['Damage'] == "Damages not recorded":
      pass
    elif hurricanes[cane]['Damage'] > most_damage_count:
      most_damage_cane = cane
      most_damage_count = hurricanes[cane]['Damage']

  return most_damage_cane, most_damage_count

greatest_damage_cane = greatest_damage(hurricanes)
#print(greatest_damage_cane)

# write your catgeorize by damage function here:
def catgeorize_by_damage(hurricanes):
  damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

  hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

  for cane in hurricanes:

    damage_cost = hurricanes[cane]["Damage"]

    if damage_cost == "Damages not recorded":
      hurricanes_by_damage[0].append(hurricanes[cane])
    elif damage_cost == hurricanes_by_damage[0]:
       hurricanes_by_damage[0].append(hurricanes[cane])
    elif damage_cost > damage_scale[0] and damage_cost <= damage_scale[1]:
       hurricanes_by_damage[1].append(hurricanes[cane])
    elif damage_cost > damage_scale[1] and damage_cost <= damage_scale[2]:
       hurricanes_by_damage[2].append(hurricanes[cane])
    elif damage_cost > damage_scale[2] and damage_cost <= damage_scale[3]:
       hurricanes_by_damage[3].append(hurricanes[cane])
    elif damage_cost > damage_scale[3] and damage_cost <= damage_scale[4]:
       hurricanes_by_damage[4].append(hurricanes[cane])
    elif damage_cost > damage_scale[4]:
      hurricanes_by_damage[5].append(hurricanes[cane])
  return hurricanes_by_damage

hurricane_by_damage = catgeorize_by_damage(hurricanes)
#print(hurricane_by_damage[5])