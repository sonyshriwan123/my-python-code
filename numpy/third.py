import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import matplotlib.pyplot as plt
import numpy as np

# python is a collection of cuntions that make matplotlib work like

# x =[ 1,2,3,4,5]
# y= [ 10,20,15,25,30]
# plt.plot(x,y)
# plt.show()


#   ########======================== Customize chart =========
# plt.figure(figsize=(4,3))
# plt.plot(x,y, color = "red" , marker = "o" , linestyle = "dashed" , linewidth = 2 , markersize = 12)
# plt.title( " The Titile is : Bahut pitoge" )
# plt.xlabel("x- Axis label is here")
# plt.ylabel(" y- Axis label is here")
# plt.show()

# plt.figure(figsize=(2,5))
# plt.plot(x,y, color = "red" , marker = "o" , linestyle = "dashed" , linewidth = 2 , markersize = 12)
# plt.title( " The Titile is : Dhurandha Sale 2026" )
# plt.xlabel("x- Axis label is here")
# plt.ylabel(" y- Axis label is here")
# plt.show()


# x =[ 1,2,3,4,5]
# y1= [ 10,20,25,35,45]
# y2=[ 20,30,35,45,55]

# plt.plot(x, y1, label = " Sales 2024")
# plt.plot(x, y2, label = " Sales 2025")
# plt.title( " Dhurandar Sales Comparision 2024 & 2025 ")

# plt.xlabel("Months")
# plt.ylabel("Sales")

# plt.legend()
# plt.show()



# x =[ "maths," , "Hindi" ,"English" , " physics" , "Gramer" ]
# y1= [ 10,20,25,35,45]
# y2= [ 20,30,35,45,55]

# plt.plot(x, y1, label = " Marks 2024" , marker="o")
# plt.plot(x, y2, label = " Marks 2025" , marker="s")

# plt.title( "Marks of Student 2024 & 2025")

# plt.xlabel("subject")
# plt.ylabel("marks")

# plt.legend()
# plt.show()


#======================= Bar Chart===================

# x= [1,2, 3,4,5]
# y= [ 10,20,25,35,45]
# plt.bar(x,y)
# plt.title( "Bar Chart")
# plt.show()


# x= ["Ayush" , "JK" , "elon bhai" , "ambani bhai" , "modi bhai" , "amit kaka bhai" , "ajit Bhai" , "larry page" , "bill hates", " warren bhai"]

# y= [ 10,20,25,35,45,55,66,77,88,100]
# colour = [ "red" , "orange" , "pink", "pink","pink","pink","pink","pink","pink", "green"]


# plt.bar(x,y, color = colour)
# plt.title( "Bar Chart")
# plt.xlabel("students")
# plt.ylabel("scores")
# plt.show()


## HISTOGRAM 
# data = [ random.randint(1,100) for i in range (100)]

# plt.hist(data, bins= 5)
# plt.title (" Histogram Example")
# plt.show()

# Pie Chart Example

# categories = ["A","B", "C", "D", "E"]

# sales = [ 10,20, 55 ,35 ,45 ]

# plt.pie(sales,labels = categories,autopct= "%1.1f%%")
# plt.title("pie chart example")
# plt.show()

#  Scatter Plot
 
# y1 = [10,20,25,35,45]
# y2 = [20,30,35,45,55]
 
# plt.scatter(y1, y2)
# plt.title("Scatter Plot Examole")
# plt.show()

# data  - 1

# categories = [ "monday", "tuesday" ,"wednesday", "thursday", "friday"]
# sales =[ 10, 20, 55, 35, 45]

# # data  - 2
# y1 = [10,20,25,35,45]
# y2 = [20,30,35,45,55]

# plt.figure(figsize=(4,6))

# ## first plot - ba chart
# plt.subplot(1,2,1) 

# plt.bar(categories, sales)
# plt.title("Daily Sales")
# plt.xlabel("Week Days")
# plt.ylabel("Sales")



# ## Second Plot  - Scatter Chart
# plt.subplot(1,2,2)  # row , colums , position

# plt.scatter (y1,y2)
# plt.title("User Example")
# plt.xlabel("User 1")
# plt.ylabel("User 2")
# plt.show()



# Introducting the Grids


# x = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
# y = np.array([ 10,15,20,25,30,35,40,45,50,55,60,65,70,75,80])
# plt. title( " West Bangal VS Tamil Nadu Polls")
# plt.xlabel("Months")
# plt.ylabel("Polls")
# plt.plot( x, y , marker = "o" , linestyle = "dashed" , color = "purple" , linewidth = 2 , markersize = 5 )
# plt.grid(color ="green", linestyle = "--" , linewidth =  0.5) # it will show the grid in the chart
# plt.show()


# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()


# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y, s=sizes)

# plt.show()