import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 25, 30, 50]
plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='--', color='b')
plt.title("Trend Over Time")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")
plt.grid(True)
plt.show()

# 2. Bar Graph
students = ['John', 'Jane', 'Alice', 'Bob']
marks = [75, 85, 60, 90]
plt.bar(students, marks, color=['red', 'blue', 'green', 'orange'])
plt.title("Student Marks")
plt.show()

# 3. Pie Chart
regions = ['North America', 'Europe', 'Asia', 'Others']
revenue = [45, 25, 20, 10]
explode = (0.1, 0, 0, 0) # Explode the 1st slice (North America)
plt.pie(revenue, labels=regions, autopct='%1.1f%%', explode=explode, shadow=True)
plt.title("Revenue Distribution")
plt.show()

# 4. Histogram
random_data = np.random.randint(1, 101, 1000)
plt.hist(random_data, bins=20, color='purple', edgecolor='black')
plt.title("Frequency Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()