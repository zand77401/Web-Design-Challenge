import pandas as pd 
import os

file = os.path.join("..", "Resources", "cities.csv")

df = pd.read_csv(file, encoding="ISO-8859-1")

df.head()