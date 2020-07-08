import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Funnel for Cool T-Shirts Inc.

print(visits.head()) # lists all of the users who have visited the website
print(cart.head()) # lists all of the users who have added a t-shirt to their cart
print(checkout.head()) # lists all of the users who have started the checkout
print(purchase.head()) # lists all of the users who have purchased a t-shirt

visits_cart = pd.merge(visits, cart, how='left')
# print(visits_cart.head()) # [2052 rows x 3 columns]

null_cart_time = visits_cart[visits_cart.cart_time.isnull()]
# print(null_cart_time) # checkout without adding to cart

# percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart
percent_visits_cart = float(len(null_cart_time)) / float(len(visits_cart)) * 100
print(percent_visits_cart)

cart_checkout = pd.merge(cart, checkout, how='left')
# print(cart_checkout.head())
null_checkout_time = cart_checkout[cart_checkout.checkout_time.isnull()]
# print(null_checkout_time) 

# percentage of users put items in their cart, but did not proceed to checkout
percent_cart_checkout = float(len(null_checkout_time)) / float(len(cart_checkout)) * 100
print(percent_cart_checkout)

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
# print(all_data.head())

percent_checkout_purchase = float(len(all_data[all_data.purchase_time.isnull()])) / float(len(all_data)) * 100
print(percent_checkout_purchase)

# cart step of the funnel is the weakest (the highest percentage of users not completing it), users visited the website, but did not proceed to add items to cart.

# Average Time to Purchase

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time
# print(all_data.time_to_purchase)

# the average time to purchase
print(all_data.time_to_purchase.mean())

print(all_data.info())