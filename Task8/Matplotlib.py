import matplotlib.pyplot as plt
#Line chart
# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the plot
plt.plot(x, y)

# Add a title and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()

#Bar chart
# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 5, 6, 4]

# Create the bar chart
plt.bar(categories, values)

# Add a title and labels
plt.title("Simple Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")

# Show the plot
plt.show()

#Scatter plot

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create the scatter plot
plt.scatter(x, y)

# Add a title and labels
plt.title("Simple Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()


#Histogram
import numpy as np

# Sample data
data = np.random.randint(1000)

# Create the histogram
plt.hist(data, bins=30)

# Add a title and labels
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show the plot
plt.show()

#Pie chart
# Sample data
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

# Create the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Add a title
plt.title("Simple Pie Chart")

# Show the plot
plt.show()