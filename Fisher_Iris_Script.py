import statistics #ensures Python has all the capabilities to identify and execute statistic functions e.g. statistics.mean()
import csv #ensures python has all the capabiliites to open and work with csv files 

print ("Fisher's Iris Data, Sem-1-Python-Project, Eimear Butler April 2018") #print title

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

print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,)) #print title replacing %s with z (Iris species name)
print("The mean of %s is: %s" %(z, a)) #print results replacing %s with first z (Iris atribute) then a (value of calculation rounded to 3 decimal places above)
print("The median of %s is: %s" %(z, b)) #repeat for all functions
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()


z = "Petal Width" #z now changes to next Iris atribute 
r = 1 #new atribute is asociated with next row


print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,)) #the same code as row 38-45 can now be used to print results for the new Iris atribute
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()


z = "Sepal Length" 
r = 2 


print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
print()


z = "Sepal Width" 
r = 3 


print("From Fisher's Iris Data, the %s has been interrogated as follows:" %(z,))
print("The mean of %s is: %s" %(z, a))
print("The median of %s is: %s" %(z, b))
print("The maximum of %s is: %s" %(z, c))
print("The minimum of %s is: %s" %(z, d))
print("The standard deviation of %s is: %s" %(z, e))
print("The standard variance of %s is: %s" %(z, f))
