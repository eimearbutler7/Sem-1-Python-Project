import statistics #ensures Python has all the capabilities from the Python Standard Library to identify and execute statistic functions e.g. statistics.mean()
import csv        #ensures python has all the capabiliites from the Python Standard Library to open and work with csv files
import matplotlib.pyplot as plt #ensures Python has the capabilities from the Python Standard Library to create a Histogram
import matplotlib.mlab as mlab #ensures Python has the capabilities from the Python Standard Library to create a Histogram


print ("Fisher's Iris Data, Sem-1-Python-Project, Eimear Butler April 2018") #print title
print() #space
print ("Petal Length ", "Petal Width ", "Sepal Length ", "Sepal Width") #print row headers 

with open ("iris.csv") as f:
  for line in f:
    print ("{:>7} {:>12} {:>13} {:>12}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
print() #print full list of data in clear format, removing commas and spacing nicely

z = "Petal Length" #row description, change as needed
r = 0 #row index number, chenge in accordance with description
y = [] #this will become the list of entries in the row selected above 
with open('iris.csv') as f: # open iris file, week 5 GMIT lecture
  for line in f:
    iris = line.split(',')[r] # split out each line in iris file, week 5 GMIT lecture
    y.append(iris) # put each entry from each row back into the y list as a string 

x = [float(i) for i in y] #change the 'y' string list, into a floating number version list called 'x' https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats

#print(x) #optional to see final list 'x' containing floating number versions of the row from the csv file 

a = statistics.mean(x) # Python Standard Library 9.7. statistics — Mathematical statistics functions
a = "%.3f" % a     # round to the third decimal point  https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
b = statistics.median(x)
b = "%.1f" % b
c = max(x)
c = "%.1f" % c
d = min(x)
d = "%.1f" % d
e = statistics.stdev(x)
e = "%.3f" % e
f = statistics.variance(x)
f = "%.3f" % f

#print results of calculations in rows 28 - 39 in a suitable format 
print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()
print("A histogram (Figure %s) representing %s distribution has also printed using the matplotlib function" %(r+1, z))
print()

#create a normalised (normed=1) Hitogram of this atribute using: 
# matplotlib imported functionality (see also row 3 and 4)
# # x = same x set created above mon line 24
mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 #number of bars in Histogram
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) #ref: https://plot.ly/matplotlib/histogram facecolour = colour of bars , alpha = increasing in values of 

plt.xlabel('%s' %(z)) #x axis name
plt.ylabel('Frequency') #y azis name
plt.title('Histogram of %s'%(z)) #Histogram Title 
plt.axis([4, 8, 0, 1]) #X axis min and Max, Y axis min and max
y = mlab.normpdf(bins, mu, sigma) #create histogram data
plt.plot(bins, y, 'r--') #plot histogram

plt.show() #print plot

z = "Petal Width" #z now changes to next Iris atribute 
r = 1 #new atribute is asociated with next row #all the rest of this script for Petal Width remains the same except the histogram parameter adjustments which were done manually to ensure best representation of data
y = []  
with open('iris.csv') as f: 
  for line in f:
    iris = line.split(',')[r] 
    y.append(iris)  

x = [float(i) for i in y] 


a = statistics.mean(x) 
a = "%.3f" % a     
b = statistics.median(x)
b = "%.1f" % b
c = max(x)
c = "%.1f" % c
d = min(x)
d = "%.1f" % d
e = statistics.stdev(x)
e = "%.3f" % e
f = statistics.variance(x)
f = "%.3f" % f

print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()
print("A histogram (Figure %s) representing %s distribution has also printed using the matplotlib function" %(r+1, z))
print()

 
mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s'%(z))  
plt.axis([2, 5, 0, 2]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show() 

z = "Sepal Length" #z now changes to next Iris atribute 
r = 2 #new atribute is asociated with next row #all the rest of this script for Petal Width remains the same except the histogram parameter adjustments which were done manually to ensure best representation of data
y = [] 
with open('iris.csv') as f: 
  for line in f:
    iris = line.split(',')[r] 
    y.append(iris) 

x = [float(i) for i in y] 


a = statistics.mean(x) 
a = "%.3f" % a     
b = statistics.median(x)
b = "%.1f" % b
c = max(x)
c = "%.1f" % c
d = min(x)
d = "%.1f" % d
e = statistics.stdev(x)
e = "%.3f" % e
f = statistics.variance(x)
f = "%.3f" % f

print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()
print("A histogram (Figure %s) representing %s distribution has also printed using the matplotlib function" %(r+1, z))
print()

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s'%(z))  
plt.axis([0, 7, 0, 1]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show() 

#additional histograms created to separate Iris-versicolor and Iris-virginica data from Iris-setosa as from reviewing the first histogram for Sepal Length, it appears there may be 2 distinct curves
x = (x[50:]) #x now becomes just the data for Iris-versicolor and Iris-virginica i.e. data from index 50 to the end

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s for Iris-versicolor and Iris-virginica Only'%(z))  
plt.axis([0, 7, 0, 1]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show()

x = (x[:49]) #x now becomes just the data for Iris-setosa i.e. the first 50 data points - from index 0 to 49

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s for Iris-setosa Only'%(z))  
plt.axis([0, 7, 0, 4]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show()

print("Two further Histograms are also printed representing %s distribution for just Iris-versicolor and Iris-virginica (Figure %sa) and Iris-setosa (Figure %sb) " %(z, r+1, r+1))
print()

z = "Sepal Width" #z now changes to next Iris atribute 
r = 3 #new atribute is asociated with next row #all the rest of this script for Petal Width remains the same except the histogram parameter adjustments which were done manually to ensure best representation of data
y = []  
with open('iris.csv') as f: 
  for line in f:
    iris = line.split(',')[r] 
    y.append(iris)  

x = [float(i) for i in y] 


a = statistics.mean(x) 
a = "%.3f" % a    
b = statistics.median(x)
b = "%.1f" % b
c = max(x)
c = "%.1f" % c
d = min(x)
d = "%.1f" % d
e = statistics.stdev(x)
e = "%.3f" % e
f = statistics.variance(x)
f = "%.3f" % f

print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()
print("A histogram (Figure %s) representing %s distribution has also printed using the matplotlib function" %(r+1, z))
print()

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s'%(z)) 
plt.axis([0, 3, 0, 4]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r--') 

plt.show() 

#additional histograms created to separate Iris-versicolor and Iris-virginica data from Iris-setosa as from reviewing the first histogram for Sepal Width, it appears there may be 2 distinct curves
x = (x[50:]) #x now becomes just the data for Iris-versicolor and Iris-virginica i.e. data from index 50 to the end

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s for Iris-versicolor and Iris-virginica Only'%(z))  
plt.axis([0, 3, 0, 5]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show()

x = (x[:49]) #x now becomes just the data for Iris-setosa i.e. the first 50 data points - from index 0 to 49

mu = statistics.mean(x)
sigma = statistics.stdev(x)
bins = 50 
n, bins, patches = plt.hist(x, bins, normed=1, facecolor='g', alpha=0.1) 

plt.xlabel('%s' %(z)) 
plt.ylabel('Frequency') 
plt.title('Histogram of %s for Iris-setosa Only'%(z))  
plt.axis([0, 3, 0, 15]) #X axis min and Max, Y axis min and max have been MANUALLY adjusted to ensure best representation of data including if normal transformation was needed. I did try to use min (d) and max (c) but this did not work well enough
y = mlab.normpdf(bins, mu, sigma) 
plt.plot(bins, y, 'r--') 

plt.show()

print("Two further Histograms are also printed representing %s distribution for just Iris-versicolor and Iris-virginica (Figure %sa) and Iris-setosa (Figure %sb) " %(z, r+1, r+1))
print()
