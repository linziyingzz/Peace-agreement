# Neccessary import
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

file_2017 = pd.read_csv("2017.csv")
file_2018 = pd.read_csv("2018.csv")
file_2019 = pd.read_csv("2019.csv")

final_data = pd.concat([file_2017, file_2018, file_2019], axis=0)

