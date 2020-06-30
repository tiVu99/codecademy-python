import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# Analyzing Ad Sources
# print(ad_clicks.head())

views_platform = ad_clicks.groupby('utm_source').user_id.count().reset_index()
# print(views_platform) # the most views came from google ad platform

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
# print(ad_clicks.head())

# the percent of people who clicked on ads from each source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
# print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
# print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])*100
print(clicks_pivot)
# Not much difference between sources, Facebook and Google approximately the same

# Analyzing an A/B Test

ad_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
# print(ad_group) # the same number of people shown both adds

clicks_by_group = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
# print(clicks_by_group) 
clicks_by_group_pivot = clicks_by_group.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
clicks_by_group_pivot['percent_clicked'] = clicks_by_group_pivot[True] / (clicks_by_group_pivot[True] + clicks_by_group_pivot[False])*100
print(clicks_by_group_pivot) # a greater percentage of users clicked on Ad A

a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]
# print(a_clicks.head())
# print(b_clicks.head())

a_clicks_by_day = a_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# print(a_clicks_by_day)
b_clicks_by_day = b_clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
# print(b_clicks_by_day)

a_clicks_by_day_pivot = a_clicks_by_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
a_clicks_by_day_pivot['percent_clicked'] = a_clicks_by_day_pivot[True] / (a_clicks_by_day_pivot[True] + a_clicks_by_day_pivot[False])*100
print(a_clicks_by_day_pivot)

b_clicks_by_day_pivot = b_clicks_by_day.pivot(columns='is_click', index='day', values='user_id').reset_index()
b_clicks_by_day_pivot['percent_clicked'] = b_clicks_by_day_pivot[True] / (b_clicks_by_day_pivot[True] + b_clicks_by_day_pivot[False])*100
print(b_clicks_by_day_pivot)

# Throughout the week, Ad A has higher click rate than Ad B except for Tuesday.
# Ad A has its peak on Thursday of 40.5% while Ad B has its peak on Tuesday of 37.8%
# Overall, recommend that your company should use Ad A