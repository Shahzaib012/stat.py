import statistics

# data = [1, 2, 2, 3,3,3,3, 4,4, 5, 5]

# # Mean (average)
# mean = statistics.mean(data)
# print(f"Mean: {mean}")

# # Median (middle value)
# median = statistics.median(data)
# print(f"Median: {median}")

# # Mode (most frequent value)
# mode = statistics.mode(data)
# print(f"Mode: {mode}")


import numpy as np 
# data = np.array([1,2,2,3,3,3,3,4,4,4,4,5,5])
# unique , counts = np.unique(data,return_counts=True)

# for a, b in zip(unique , counts):
#     print(f"Value : {a} , Count {b}")
    
# mean_value = np.mean(data)
# print(f"Mean {mean_value}")

# median_value = np.median(data)
# print(f"Median  : {median_value}")

# mode_value = statistics.mode(data)
# print(f"Mode : {mode_value}")   



# data = np.array([10,11,12,13,14,14,15,15,16,17,18,19,20])
# unique , counts = np.unique(data,return_counts=True)

# for a, b in zip(unique , counts):
#     print(f"Value : {a} , Count {b}")
    
# mean_value = np.mean(data)
# print(f"Mean {mean_value}")

# median_value = np.median(data)
# print(f"Median  : {median_value}")

# mode_value = statistics.mode(data)
# print(f"Mode : {mode_value}")   

data =np.array([10,11,12,13,14,14,15,15,16,17,18,19,20])
unique1 , counts = np.unique(data,return_counts=True)

for a,b in zip(unique1,counts):
    print(f"Value : {a} , Counts {b}")
    
mean_value = np.mean(data)
print(f"Mean : {mean_value}")

median_value = np.median(data)
print(f"Median is {median_value}")

mode_value = statistics.mode(data)
print(f"Mode is {mode_value}")  
