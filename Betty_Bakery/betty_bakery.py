import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])

recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

eggs = recipes[:, 2]

print(eggs == 1)

cookies = np.array([2.75, 1.5, 1, 0, 1])

double_batch = cupcakes * 2

grocery_list = cookies + double_batch
print(grocery_list)