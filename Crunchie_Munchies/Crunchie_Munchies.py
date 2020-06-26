import codecademylib
import numpy as np

calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats_sorted)
print(median_calories)

first_quarter = np.percentile(calorie_stats_sorted, 25)
third_quarter = np.percentile(calorie_stats_sorted, 75)
interquartile = third_quarter - first_quarter
print(interquartile)

nth_percentile = np.percentile(calorie_stats_sorted, 4)
print(nth_percentile)

more_calories = np.mean(calorie_stats_sorted > 60)
print(more_calories)

calorie_std = np.std(calorie_stats_sorted)
print(calorie_std)

# most cereals have around 110 calories while there are 60 calories per serving of CrunchieMunchies