import pandas as pd

# Answer Customer Emails
inventory = pd.read_csv('inventory.csv')
# print(inventory.head(10))

staten_island = inventory.iloc[:10]
# print(staten_island)

product_request = staten_island['product_description']

seed_request = inventory[(inventory['location'] == "Brooklyn") & (inventory['product_type'] == "seeds")]

# Inventory
inventory['in_stock'] = inventory.quantity.apply(lambda x: True if x > 0 else False)
# print(inventory.head())

inventory['total_value'] = inventory.price * inventory.quantity
# print(inventory.head())

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory.head())