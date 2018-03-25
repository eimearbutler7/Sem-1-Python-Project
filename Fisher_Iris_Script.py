import statistics
import csv

z = "Petal Length" #row description, change as needed
r = 0 #row index number, chenge in accordance with description
y = [] #this will become the list of entries in the row selected above 
with open('iris.csv') as f: # open iris file
  for line in f:
    iris = line.split(',')[r] # split out each linein iris file
    y.append(iris) # put each entry from eah row back into the y list as a string 

x = [float(i) for i in y] #change the 'y' string list, into a floating number version list called 'x' https://stackoverflow.com/questions/1614236/in-python-how-do-i-convert-all-of-the-items-in-a-list-to-floats

print(x) #optional to see final list 'x' containing floating number versions of the row from the csv file 

a = statistics.mean(x) # Python Standard Library 9.7. statistics — Mathematical statistics functions
a = "%.3f" % a     # round to the nthird decimal point  https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
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
