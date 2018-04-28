### Sem-1-Python-Project &nbsp;&nbsp;&nbsp;&nbsp; Fisher's Iris Dataset &nbsp;&nbsp;&nbsp;&nbsp; Eimear Butler April 2018

## Who was Ronald Fisher?
Ronald Fisher was a British statistician and biologist who in 1936 published an article on "The use of multiple measurements in taxonomic problems" <sup>4</sup>. Fisher used the Iris dataset as an example of linear discriminant analysis <sup>1</sup>. 

Medical-dictionary.thefreedictionary.com<sup>2</sup> describes discriminant analysis as: 
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/4/46/R._A._Fischer.jpg" width="200">

> *"a form of multivariate analysis in which the objective is to establish a discriminate function. The function (typically a mathematical formula) discriminates between individuals in the population and allocates each of them to a group within the population. The function is established on the basis of a series of measurements or observations made on the individuals."* 

Fisher therefore used this data to demonstrate that features can be combined to characterize two or more classes of objects or events.
 
However, it was Edgar Anderson who had actually made the measurements in an effort to quantify the variation between the three related Iris species. His paper "The irises of the Gaspe Peninsula," published in 1935 outlined his methods for achieving this <sup>3</sup>.  


## What is the Fisher Iris Dataset? 
This dataset contains a 50 samples of each species where 5 attributes of Iris flowers are documented<sup>6</sup>:

- Petal Length 
- Petal Width
- Sepal Length
- Sepal width
- Class

The 3 flower species in scope are<sup>6</sup>: 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Iris setosa* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Iris versicolor* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Iris virginica*

<img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg" width="200">   <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg" width="200">    <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg" width="200">


Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus" <sup>1</sup>.


## Why this data is interesting?

Apart from the linear discriminant analysis model published by Fisher, this dataset is widely used in data analysis examples as it is real, big enough to be interesting and useful yet relatively simple. The size of the dataset also means it fits well visually onto a computer screen so beginers can see what they are working with and all data entries are measurements taken in centimetres so no scaling or transformations are required. 


## Data Investigation
In order to use Python to further examine Fisher's Iris Dataset, the code detailed in the "Fisher_Iris_Script.py" <sup>5</sup> file within this repository, was used to examine the following values for each atribute: 

- mean: the average value
- median: the midpoint
- maximum: the highest value
- minimum: the lowest value
- standard deviation: the value representing the exten of deviation for the group as a whole
- standard variance: the value representing how spread out a data set is

To run this Python script the user must update the iris atribute title (z) and associated data (r) values. 

`z = "Petal Width"` this value changes depending on which Iris atribute we are examining 

`r = 1` the atribute is asociated with a certain column of data we want to extract from the csv File

This then triggers the relevant information to be pulled from the csv file (iris.csv) and entered into a new list (x) as floating point numbers we can then interogate with the following script: 

`y = []`

`with open('iris.csv') as f:` 

`for line in f:`

&nbsp;&nbsp;&nbsp;&nbsp;`iris = line.split(',')[r]` 

&nbsp;&nbsp;&nbsp;&nbsp;`y.append(iris)` 

`x = [float(i) for i in y]`

The "placeholder" function (%s) in Python allowed a script to be written that could be easily replicated for each of the 4 numerical atribute datasets. See comments throughout the "Fisher_Iris_Script.py" file for further information. 

The results were as follows, where x is the relevant dataset<sup>7</sup>: 

| Values  | Function Used  | Petal Length  | Petal Width | Sepal Length  | Sepal Width |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| Mean  | `statistics.mean(x)` | 5.843  | 3.054  | 3.759  | 1.199  |
| Median  | `statistics.median(x)`  | 5.8  | 3.0  | 4.3  | 1.3  |
| Maximum  | `max(x)`  | 7.9  | 4.4  | 6.9 | 2.5  |
| Minimum  | `min(x)`  | 4.3  | 2.0  | 1.0  | 0.1  |
| Standard Deviation  | `statistics.stdev(x)`  | 0.828  | 0.434  | 1.764  | 0.763  |
| Standard Variance  | `statistics.variance(x)`  | 0.686  | 0.188  | 3.113  | 0.582  |


## Data Distribution
In order to investigate the distribution of the data, histograms were constructed from Python using the imported matplotlib plotting library. The resulting histograms, with normalised data and related curve are displayed below for all 4 atributes in all 3 species of Iris (Figures 1-4)<sup>5</sup>. 

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_1.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_2.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_3.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_4.png)

From reviewing the histograms, it appears the data for Petal Length and Width can fit a normal distribution curve reasonably well however there are 2 distinct peaks for the Sepal Length and Width meaning the curve is skewed. Referencing the data, it indicates the *Iris sertosa* data is an outlier to the *Iris virginica* and *Iris versicolor*.

Further histograms were performed on just the Iris virginica* and *Iris versicolor* data (Figures 3a and 4a) and *Iris sertosa* data (Figures 3b and 4b)<sup>5</sup> to confirm this.

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_3a.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_4a.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_3b.png)

![alt text](https://github.com/eimearbutler7/Sem-1-Python-Project/blob/master/zFigure_4b.png)

## Conclusion
The brief analysis of Fisher's Iris data shows the power of Python scripting to interogate the results and using matplotlib, create histograms. The data examination herer inticates that Sepal Length may be an atribute in which the differentiation of *Iris Setosa* may from *Iris virginica* and *Iris versicolor* may be made which is in line with other published studies on the subject. Further work on the script is recommended to see if the the `def` function could be better incorporated. Unfortunately time did not permit this to occur during this project.


# References 

<sup>1</sup> https://en.wikipedia.org/wiki/Iris_flower_data_set

<sup>2</sup> https://medical-dictionary.thefreedictionary.com/Linear+discriminant+analysis

<sup>3</sup> Anderson, Edgar (1935). "The irises of the Gaspe Peninsula," Bulletin of the American Iris Society, 59, 2–5.

<sup>4</sup> Fisher, Ronald A. (1936). "The use of multiple measurements in taxonomic problems." Annals of Eugenics, 7, Part II, 179–188.

<sup>5</sup> https://github.com/eimearbutler7/Sem-1-Python-Project/Fisher_Iris_Script.py

<sup>6</sup> http://archive.ics.uci.edu/ml/datasets/Iris

<sup>7</sup> https://github.com/eimearbutler7/Sem-1-Python-Project/Fisher_Iris_Script_OUTPUT.py
