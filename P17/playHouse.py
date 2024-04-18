import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.model_selection import train_test_split

class playHouse:
    def __init__(self, file):
        self.data = pd.read_csv(file)
        

    def getHead(self):
        df = self.data
        print(df.head())


    def scatter(self):
        df = self.data
        
        plt.scatter(df['age'], df['charges'])
        plt.ylabel("Charges")
        plt.xlabel("Age")
        plt.show()


    def snsscatter(self):
        df = self.data
        sns.set_context('paper', font_scale=0.8)
        sns.scatterplot(data = df, x='age', y='charges', hue='smoker')
        #sns.jointplot(data = df, x='age', y='charges', kind='kde')
        plt.show()


    def everyThing(self):
        df = self.data
        sns.pairplot(df)
        plt.show()


    def pivot_table(self):
        df = self.data
        print(df.pivot_table(index = 'age', columns = 'bmi', values = 'charges'))


    def testTrain(self):
        df = self.data
        # I need to work on this
        x_train, x_test, y_train, y_test = train_test_split(df.age, df.charges)
        sns.scatterplot(x_train, y_train)
        plt.show()
        # linear_model.LinearRegression()


    def linReg(self):
        df = self.data

        x = df.iloc[:,:1].values
        y = df.iloc[:,-1].values
        
        sexy_data_model = LinearRegression()
        
        #print(df.iloc[:,:1].values)
        #print('###')
        #print(df['age'].values)
        
        
        sexy_data_model.fit(x,y)
        
        charges_pred = sexy_data_model.predict(x)

        plt.scatter(x, y, color = 'b')
        plt.plot(x,charges_pred, color = 'y')
        
        plt.ylabel("Charges")
        plt.xlabel("Age")
        plt.show()

    def reshaoe(self):
        data = self.data
        print(data.dtypes)
        #x = data.iloc[:,0].values
        
        blood_pressure = data['BloodPressure'].values.reshape(-1, 1)
        #print(x.reshape(-1, 1))
        #print(X)
        
        bmi = data['BMI'].values.reshape(-1, 1)
        pregnancies = data['Pregnancies'].values.reshape(-1, 1)
        glucose = data['Glucose'].values.reshape(-1, 1)
        skin_thickness = data['SkinThickness'].values.reshape(-1, 1)
        insulin = data['Insulin'].values.reshape(-1, 1)
        diabetes_pedigree = data['DiabetesPedigreeFunction'].values.reshape(-1, 1)
        age = data['Age'].values.reshape(-1, 1)
        outcome = data['Outcome'].values.reshape(-1, 1)
        
        y = bmi
        
        sexy_data_model = LinearRegression()
        sexy_data_model.fit(outcome,y)

        pressure_perd = sexy_data_model.predict(outcome)

        plt.scatter(outcome, y, color = 'b')
        plt.plot(outcome, pressure_perd, color = 'y')
        plt.show()

    def everything(self):
        data = self.data
        sns.pairplot(data=data)
        plt.show()


    def trainTest(self):
        data = self.data
        x = data.iloc[:,[0,1,2,3,4,5]]
        
def main():
    #f = playHouse('insurance.csv')
    g = playHouse('diabetes_updated.csv')
    
    #f.getHead()
    #f.scatter()
    #f.snsscatter()
    #f.everyThing()
    #f.pivot_table()
    #f.testTrain()
    #f.linReg()

    #g.getHead()
    g.everything()
    #g.reshaoe()

    
if __name__=='__main__':
    main()

# reshape() reshape the array with pd
# jupyter notebook
