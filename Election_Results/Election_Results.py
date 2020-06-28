import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = survey_responses.count('Ceballos')
print(total_ceballos)

# percentage of people in the survey who voted for Ceballos
survey_responses_length = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos/survey_responses_length
print(percentage_ceballos)

possible_surveys = np.random.binomial(survey_responses_length, 0.54, size=10000) / survey_responses_length

plt.hist(possible_surveys, bins=20, range=(0, 1))
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print(ceballos_loss_surveys) # about 20% of the time a survey output would predict Kerrigan winning

large_survey = np.random.binomial(float(7000), 0.54, size=10000) / float(7000)

plt.hist(large_survey, bins=20, range=(0, 1))
plt.show()

ceballos_loss_new = np.mean(large_survey < 0.5)
print(ceballos_loss_new) # 0% of surveys that would have an outcome of Ceballos losing