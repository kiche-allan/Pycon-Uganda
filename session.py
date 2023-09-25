# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(Country,  Sales, Discounts, Profit, Units Sold, Sale Price, COGS, Product)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import matplotlib.pyplot as plt

x = dataset['Country']
y = dataset['Sum of Sales']
y2 = dataset['Sum of Discounts']
y3 = dataset['Sum of Profit']

plt.plot(x,y1, 'o-',color = 'green')
plt.plot(x,y2, '--o',color = 'tomato')
plt.plot(x,y3, '^',color ='blue')

plt.show()