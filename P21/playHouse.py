import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import seaborn as sns
#from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler
#from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

class playHouse:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        
    #1
    def getHead(self): 
        df = self.data
        print(df.head())
        print(df.isnull().sum())
        print(df.info())

    def wtf(self):
        # Keep in mind
        df = self.data
        print(df.Sex)

    def dummies(self, column):
        self.data = pd.get_dummies(self.data, prefix=column, columns=[column])

    def group(self):
        print(df.grpupby('jk')['smething'].std())
        
  
 
def main():
    # What is load_iris()? Training Wheels! Please let the AI overlords take over.
    '''
    So iris is <class 'sklearn.utils._bunch.Bunch'> and not a df. And does match
    the data I have been given. Fucking egos, what was wrong with df that we all use
    '''
    #iris = load_iris()
    #print(type(iris))
    #print(iris.data[:, ])
    #print(iris)
    #print(iris.target)
    print(range(1, 5))
    
    f = playHouse('titanic.csv')
    #f.getHead()
    #f.wtf()
    f.dummies('Sex')
    f.dummies('Embarked')
    f.getHead()
    # We have null data
    

    
if __name__=='__main__':
    main()

#independent variables and the dependent variable
# independent variable aka manipulated veriable. The variable you change X
# dependent variable aka responding variables. The variable you measure Y
# and there more: "response variable", "regressand", "criterion", "predicted variable", "measured variable", "explained variable", "experimental variable", "responding variable", "outcome variable", "output variable", "target" or "label"
# Control Variables are variables that need to remain constannt
# reshape() reshape the array with pd
# jupyter notebook
