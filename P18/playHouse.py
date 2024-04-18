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
        
    #2
    def copyCat(self):
        data1 = np.genfromtxt('diabetes.csv', delimiter=',')
        data =  self.data
        features = ['age', 'sex', 'body mass index', 'blood pressure', 'serum1', 'serum2', 'serum3', 'serum4', 'serum5', 'serum6']
        print(data.iloc[:,0:10].values)
        print(data1[:,0:10])
        #get the shape
        print(X.shape)
        print(Y.shape)

    #3
    def trainTest():
        # Generate training and test sets comprising
        # 80% and 20% of the data respectively
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    #4
    def minStand(self):
        # What is  MinMaxScaler and StandardScaler
        minmax_scale.fit((data))
        minmax_scale.transform(data) #You can do this as a fit_tranform

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        #take note = pf.DataFrame(data, columns = ["Experinve", "Salary"])

    def makeNumber(self):
        df['smoker'] = df['smiker'].astype('catagory')
        df['smoker'] = df['smiker'].cat.codes
        #think this can be done in one line
 
def main():
    f = playHouse('diabetes.csv')
    f.getHead()
    'f.copyCat()

    
if __name__=='__main__':
    main()

#independent variables and the dependent variable
# independent variable aka manipulated veriable. The variable you change X
# dependent variable aka responding variables. The variable you measure Y
# and there more: "response variable", "regressand", "criterion", "predicted variable", "measured variable", "explained variable", "experimental variable", "responding variable", "outcome variable", "output variable", "target" or "label"
# Control Variables are variables that need to remain constannt
# reshape() reshape the array with pd
# jupyter notebook
