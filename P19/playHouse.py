import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler
#from sklearn.model_selection import train_test_split

class playHouse:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        
    #1
    def getHead(self): 
        df = self.data
        print(df.head())
        print(df.dtypes)
        print(df.isnull().sum())
        #groupby needs work
        print(df.groupby(['Species']).sum())

    
    
 
def main():
    f = playHouse('Iris.csv')
    f.getHead()
    

    
if __name__=='__main__':
    main()

#independent variables and the dependent variable
# independent variable aka manipulated veriable. The variable you change X
# dependent variable aka responding variables. The variable you measure Y
# and there more: "response variable", "regressand", "criterion", "predicted variable", "measured variable", "explained variable", "experimental variable", "responding variable", "outcome variable", "output variable", "target" or "label"
# Control Variables are variables that need to remain constannt
# reshape() reshape the array with pd
# jupyter notebook
