# Voices of Bollywood
## CWL 207 Honors Projecy
### By: Abhinav Tekulapally and Teagan Mathur

## Introduction
This project is to help visualize the distribution of artists in Indian Cinema.
We found that relatively few artists end up singing in the majority of the movies.

We made a wordpress site to help illustrate this point which can be found at https://publish.illinois.edu/voicesofbollywood/.

## How we made it
To begin we compiled information from Box Office India to get a list of top movies within each decade. https://web.archive.org/web/20120626143254/http://www.boxofficeindia.com:80/showProd.php?itemCat=121&catName=MTk0MC0xOTQ5

We compiled a list of movies and put it in the files movies.txt

We then made a python script that reads every entry in this file and queries wikipedia for the top result with that name.

If Wikipedia has an article for that movie the script automatically loads the article and retrieves the Artist for that movie.

The script creates a directory called output and outputs a csv corresponding each film name to the artists for the film. Additionally, the script outputs a csv for each decade and corressponds each artists to the number of films they were in in that decade.

## Running the script

Running script locally using Python:

1. Have Python3 and Pip installed
2. Install the dependecies
```
pip install -r requirements.txt
```
3. Run the script with optional command line argument which is the path to the movies.txt file
```
python3 run.py [path/to/movies.txt]
```

Using the pre-packaged binary (Only tested on MacOS):

Run the command in a terminal
```
./run [path/to/movies.txt]
```
