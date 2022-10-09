import numpy as np 
import pandas as pd 


#Reading of all the cities around Bordeaux 
base = pd.read_excel("data_logistic\donneesRDLF.xlsx")
Distance = pd.read_csv("data_logistic\driving_distances.csv")



#Building of the meterics 

def distance_cities(vect):
    cities = vect["Ville"]
    matrix = pd.DataFrame(0,columns = cities, index = cities)
    return matrix 

dist_matrix = distance_cities(base)

print(base)
print(dist_matrix)