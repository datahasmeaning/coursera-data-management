# -*- coding: utf-8 -*-
"""
Created on Jan 2017

@author: relbaff
"""
import pandas

# bug fix for display formats to avoid run time errors - put after code for loading data above
pandas.set_option('display.float_format', lambda x:'%f'%x)

# Load data from csv file
original_data = pandas.read_csv('addhealth_pds.csv', low_memory=False)
original_data['H1GI15'] = pandas.to_numeric(original_data['H1GI15'])

# Keep only the observations with value 0 (no) for var H1GI16M
subset_data_min15_not_married = original_data[(original_data['H1GI15'] == 0)]
# copy data
data = subset_data_min15_not_married.copy()

# Print number of observations and vars
print('Addhealth - Number of observations: ' + str(len(data))) # 4428
print('Addhealth - Number of variables: '+ str(len(data.columns))) #2829


# Function that convert the column to numeric, calculates frequencies and display results
def calculate_frequency(column_name, message, is_numeric: bool):

    # Convert data to numeric in case it is numeric
    if is_numeric:
        data[column_name] = pandas.to_numeric(data[column_name])

    # Calculate the frequency of the variable
    frequency_as_count = data[column_name].value_counts(sort=False)
    frequency_as_percentile = data[column_name].value_counts(sort=False, normalize=True)

    # Print results
    print('\n***********************************************')
    print(message)
    print('Frequency in numbers:')
    print(frequency_as_count)
    print('\nFrequency in percentile:')
    print(frequency_as_percentile)
    print('***********************************************')


# Q: How close do you feel to your {MOTHER/ADOPTIVE MOTHER/ STEPMOTHER/ FOSTERMOTHER/etc.}?
# A: 1=Not at all, 2=Very little, 3=somewhat,
#           4=quit a bit, 5=very much, 6=refused, 7=skip-no mom, 8=don't know
description_H1WP9 = 'Q: How close do you feel to your {MOTHER/ADOPTIVE MOTHER/ STEPMOTHER/ FOSTERMOTHER/etc.}?' \
              '\nA: 1=Not at all, 2=Very little, 3=somewhat, 4=quit a bit, 5=very much, 6=refused, ' \
              '7=skip-no mom, 8=don\'t know'
calculate_frequency('H1WP9', description_H1WP9, True)


# Q: How close do you feel to your {FATHER/ADOPTIVE FATHER/STEPFATHER/FOSTERFATHER/etc.}?
# A: 1=Not at all, 2=Very little, 3=somewhat,
#           4=quit a bit, 5=very much, 6=refused, 7=skip-no mom, 8=don't know
description_H1WP13 = 'Q: How close do you feel to your {FATHER/ADOPTIVE FATHER/STEPFATHER/FOSTERFATHER/etc.}?' \
              '\nA: 1=Not at all, 2=Very little, 3=somewhat, 4=quit a bit, 5=very much, 6=refused, ' \
              '7=skip-no dad, 8=don\'t know'
calculate_frequency('H1WP13', description_H1WP13, True)

# Q: Most of the time, your mother is warm and loving toward you.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don't know
description_H1PF1 = 'Q: Most of the time, your mother is warm and loving toward you.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                     '7=skip-no mom, 8=don\'t know \n'
calculate_frequency('H1PF1', description_H1PF1, True)


# Q: Your mother encourages you to be independent.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don't know
description_H1PF2 = 'Q: Your mother encourages you to be independent.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no mom, 8=don\'t know \n'
calculate_frequency('H1PF2', description_H1PF2, True)


# Q: When you do something wrong that is important, your mother talks
#     about it with you and helps you understand why it is wrong.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don't know
description_H1PF3 = 'Q: When you do something wrong that is important, your mother talks ' \
                    'about it with you and helps you understand why it is wrong.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no mom, 8=don\'t know \n'
calculate_frequency('H1PF3', description_H1PF3, True)


# Q: You are satisfied with the way your mother and you communicate
#     with each other.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don't know
description_H1PF4 = 'Q: You are satisfied with the way your mother and you communicate  with each other.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no mom, 8=don\'t know \n'
calculate_frequency('H1PF4', description_H1PF4, True)

# Q: Overall, you are satisfied with your relationship with your mother
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don't know
description_H1PF5 = 'Q: Overall, you are satisfied with your relationship with your mother.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no mom, 8=don\'t know \n'
calculate_frequency('H1PF5', description_H1PF5, True)

# Q: Most of the time, your father is warm and loving toward you.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no father, 8=don't know
description_H1PF23 = 'Q: Most of the time, your father is warm and loving toward you.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no dad, 8=don\'t know \n'
calculate_frequency('H1PF23', description_H1PF23, True)

# Q: You are satisfied with the way your father and you communicate
#     with each other.
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no father, 8=don't know
description_H1PF24 = 'Q: You are satisfied with the way your father and you communicate.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no dad, 8=don\'t know \n'
calculate_frequency('H1PF24', description_H1PF24, True)

# Q: Overall, you are satisfied with your relationship with your father
# A: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,
#           4=disagree, 5=strongly disagree, 6=refused, 7=skip-no father, 8=don't know
description_H1PF25 = 'Q: Overall, you are satisfied with your relationship with your father.' \
                    '\nA: 1=Strongly Agree, 2=agree, 3=neither agree nor disagree,  4=disagree,' \
                    ' 5=strongly disagree, 6=refused, 7=skip-no mom, 8=don\'t know' \
                    '7=skip-no dad, 8=don\'t know \n'
calculate_frequency('H1PF25', description_H1PF25, True)

# IDEAL RELATIONSHIP EXPECTATIONS
# A: 1=card kept (expect it in ideal relationship), 2=card rejected, 6=refused, 8=don't know, 9=not applicable

print('\n\n\n-------------------------------------------------------------------------------------------')
print('-------------------------------------------------------------------------------------------')
print('SECTION: IDEAL RELATIONSHIP EXPECTATIONS')
print('What do you think will happen in an ideal relationship?')
description_H1ID1B = 'Q: I would meet my partner’s parents.' \
                    '\nA: 1=card kept, 2=card rejected, 6=refused, 8=don\'t know, 9=not applicable \n'
calculate_frequency('H1ID1B', description_H1ID1B, True)


description_H1ID1I = 'Q: I would tell my partner that I loved him or her.' \
                    '\nA: 1=card kept, 2=card rejected, 6=refused, 8=don\'t know, 9=not applicable \n'
calculate_frequency('H1ID1I', description_H1ID1I, True)


description_H1ID1J = 'Q: My partner would tell me that he or she loved me.' \
                    '\nA: 1=card kept, 2=card rejected, 6=refused, 8=don\'t know, 9=not applicable \n'
calculate_frequency('H1ID1J', description_H1ID1J, True)

description_H1ID1Q = 'Q: We would get married.' \
                    '\nA: 1=card kept, 2=card rejected, 6=refused, 8=don\'t know, 9=not applicable \n'
calculate_frequency('H1ID1Q', description_H1ID1Q, True)






