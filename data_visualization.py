import matplotlib.pyplot as plt

year = [1950,1970,1990,2010]

pop = [2.519,3.692,5.263,6.972]

plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population')
plt.yticks([0,2,4,6,8,10],
           ['0','2B','4B','6B','8B','10B'])
plt.show() #must be called to show the graph

#Clear the graph
plt.clf()

#Histograms
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]

plt.hist(values,bins=3)
plt.show()

#Dictionaries
#Keys are immutable

#Dictionary within dictionary

europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome','population':59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)

#Build a dataframe from a Dictionary
# Pre-defined lists

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

#Accessing data within pandas

#Brackets

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

#By index
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out first 3 observations
print(cars[:4])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

#Loc and iLoc

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

# Print out drives_right value of Morocco
print(cars.iloc[[4,5],[1,2]])

# Print sub-DataFrame
print(cars.iloc[4],[2])

# Print out drives_right column as Series
print(cars.iloc[:, 2])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])

#Working with operators in Numpy arrays

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5,my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))


#Pandas operations with booleans
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)

#One liner
# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100,cpc < 500)
medium = cars[between]

# Print medium
print(medium)
