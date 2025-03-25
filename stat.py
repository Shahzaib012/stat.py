# Data Science
# 1- Python
# 2- Statistics (The study of collection, analysis and interpretation of data)
# 1.	Descriptive Statistics (Describe or summarize main features of a dataset)
# •	Measure of frequency (The number of times the value occurs or present in data)
# •	Measure of central tendency (Describe the center point of your dataset) includes:
# •	Mean (The average value in a dataset)
# 	Mean = sum of all values / total of all values
# o	Note:
# 	If no outliers, use mean
# •	Median (The middle value in a dataset)
# o	Note:
# 	If outliers, use median 
# •	Mode (The most frequently value in a dataset)
# o	Mode is used when we give result in categorical (Yes or not) data form.
# •	Measure of dispersion 
# •	Measure of position
# 2.	Inferential Statistics ()
# •	Basic Statistics & its types
# •	Probability
# 3- Mathematics

import statistics

data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Mean (average)
mean = statistics.mean(data)
print(f"Mean: {mean}")

# Median (middle value)
median = statistics.median(data)
print(f"Median: {median}")

# Mode (most frequent value)
mode = statistics.mode(data)
print(f"Mode: {mode}")


import numpy as np

data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Mean
mean = np.mean(data)
print(f"Mean: {mean}")

# Median
median = np.median(data)
print(f"Median: {median}")

# mod = np.mode(data)
# print(f"Median: {mod}")


data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

# Mean
mean = sum(data) / len(data)
print(f"Mean: {mean}")

# Median
sorted_data = sorted(data)
n = len(sorted_data)
median = (sorted_data[n//2] if n % 2 != 0 
          else (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2)
print(f"Median: {median}")

# Mode
frequency = {}
for value in data:
    frequency[value] = frequency.get(value, 0) + 1
mode = max(frequency, key=frequency.get)
print(f"Mode: {mode}")