### Sem-1-Python-Project &nbsp;&nbsp;&nbsp;&nbsp; Fisher's Iris Dataset &nbsp;&nbsp;&nbsp;&nbsp; Eimear Butler April 2018

## Who was Ronald Fisher?
Ronald Fisher was a British statistician and biologist who in 1936 published an article on "The use of multiple measurements in taxonomic problems" <sup>4</sup>. Fisher used the Iris dataset as an example of linear discriminant analysis <sup>1</sup>. 

Medical-dictionary.thefreedictionary.com describes discriminant analysis as: 
<img align="right" src="https://upload.wikimedia.org/wikipedia/commons/4/46/R._A._Fischer.jpg" width="200">

*"a form of multivariate analysis in which the objective is to establish a discriminate function. The function (typically a mathematical formula) discriminates between individuals in the population and allocates each of them to a group within the population. The function is established on the basis of a series of measurements or observations made on the individuals."* <sup>2</sup>

Fisher therefore used this data to demonstrate that features can be combined to characterize two or more classes of objects or events.
 
However, it was Edgar Anderson who had actually made the measurements in an effort to quantify the variation between the three related Iris species. His paper "The irises of the Gaspe Peninsula," published in 1935 outlined his methods for achieving this <sup>3</sup>.  


## What is the Fisher Iris Dataset? 
This dataset contains a 50 samples where 5 attributes of Iris flowers are examined:

- Petal Length 
- Petal Width
- Sepal Length
- Sepal width
- Class

The 3 flower species in scope are: 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Iris setosa* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Iris versicolor* &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; *Iris virginica*

<img src="https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg" width="200">   <img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg" width="200">    <img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg" width="200">


Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus" <sup>1</sup>.


## Why this data is interesting?

Apart from the linear discriminant analysis model published by Fisher, this dataset is widely used in data analysis examples as it is real, big enough to be interesting and useful yet relatively simple. The size of the dataset also means it fits well visually onto a computer screen so beginers can see what they are working with and all data entries are measurements taken in centimetres so no scaling or transformations are required. 


## Data Investigation
In order to use Python to further examine Fisher's Iris Dataset, I used the code detailed in the "Fisher_Iris_Script.py" <sup>5</sup> file within this repository to examine the following values for each atribute: 

- mean, the average value
- median, the lowest value
- maximum, the highest value
- minimum, the lowest value
- standard deviation, the value representing the exten of deviation for the group as a whole
- standard variance, the value representing how spread out a data set is

The "placeholder" function (%s) in Python allowed me to write a script that could be easily replicated for each of the 4 numerical atribute datasets. See comments throuhout the "Fisher_Iris_Script.py" file for further information. 

The results were as follows, where x is the relevant dataset: 

| Function Used  | Petal Length  | Petal Width | Sepal Length  | Sepal Width |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| `statistics.mean(x)` | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| `statistics.median(x)`  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| `max(x)`  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| `min(x)`  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| `statistics.stdev(x)`  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |
| `statistics.variance(x)`  | Content Cell  | Content Cell  | Content Cell  | Content Cell  |



# References 

<sup>1</sup> https://en.wikipedia.org/wiki/Iris_flower_data_set

<sup>2</sup> https://medical-dictionary.thefreedictionary.com/Linear+discriminant+analysis

<sup>3</sup> Anderson, Edgar (1935). "The irises of the Gaspe Peninsula," Bulletin of the American Iris Society, 59, 2–5.

<sup>4</sup> Fisher, Ronald A. (1936). "The use of multiple measurements in taxonomic problems." Annals of Eugenics, 7, Part II, 179–188.

<sup>5</sup> https://github.com/eimearbutler7/Sem-1-Python-Project/Fisher_Iris_Script.py
