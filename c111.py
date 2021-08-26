# Results
# Are
# At
# Last
# Mam
# 👇👇👇👇👇

import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/z_test/medium_data.csv')
data = df['reading_time'].to_list()

def random_sets_of_mean(counter):
    data_sets = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        values = data[random_index]
        data_sets.append(values)
    mean_of_sample_data = st.mean(data_sets)

    return mean_of_sample_data


mean_list = []
for i in range(0, 100):
    set_of_means = random_sets_of_mean(30)
    mean_list.append(set_of_means)

standard_deviation = st.stdev(mean_list)
mean = st.mean(mean_list)

file_data_1 = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/z_test/medium_data_1.csv')
data_1 = file_data_1['reading_time'].to_list()

mean_of_sample_1 = st.mean(data_1)
st_dev_of_sample_1 = st.stdev(data_1)

print('Mean of Sampling Distribution : ', mean)
print('Standard Deviation of Sampling Distribution : ', standard_deviation)

first_stdev_start, first_stdev_end = mean - standard_deviation, mean + standard_deviation
second_stdev_start, second_stdev_end = mean - ( 2 * standard_deviation ) , mean + ( 2 * standard_deviation )
third_stdev_start, third_stdev_end = mean - ( 3 * standard_deviation ) , mean + ( 3 * standard_deviation )

figure = ff.create_distplot([mean_list], ['Reading Time'], show_hist = False)
figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.7], mode = 'lines', name = 'MEAN'))
figure.add_trace(go.Scatter(x = [first_stdev_end, first_stdev_end], y = [0, 0.7], mode = 'lines', name = 'STANDARD DEVIATION 1'))
figure.add_trace(go.Scatter(x = [second_stdev_end, second_stdev_end], y = [0, 0.7], mode = 'lines', name = 'STANDARD DEVIATION 2'))
figure.add_trace(go.Scatter(x = [third_stdev_end, third_stdev_end], y = [0, 0.7], mode = 'lines', name = 'STANDARD DEVIATION 3'))
figure.add_trace(go.Scatter(x = [mean_of_sample_1, mean_of_sample_1], y = [0, 0.7], mode = 'lines', name = 'MEAN OF SAMPLE DATA'))

figure.show()

z_score = ( mean_of_sample_1 - mean ) / standard_deviation
print('Z Score : ',z_score)

# Mean of Sampling Distribution :  6.149
# Standard Deviation of Sampling Distribution :  0.652586238823753
# Z Score :  -0.27429324946023514
