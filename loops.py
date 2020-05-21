#While loop

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset -= 1
    print(offset)

offset_2 = -6

# Code the while loop
while offset_2 != 0 :
    print("correcting...")
    if offset_2 > 0:
        offset_2 -= 1
    else:
      offset_2 += 1
    print(offset_2)

#For loop
fam = [1.73,1.68,1.71,1.89]

for index,height in enumerate(fam):
    print('index' + str(index) + ": " + str(height))

#start at index 1
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index+1) + ": " + str(area))

#Numpy array
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])

meas = np.array([np_height,np_weight])

#To get each item
for val in np.nditer(meas):
    print(val)

#Iterating over a dictionary

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

# Iterate over europe
for key,value in europe.items():
    print('the capital of ' + str(key) + ' is ' + str(value))

#Iterating in pandas dataframe
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab,row in cars.iterrows():
    print(lab)
    print(row)
