import pandas as pd
import matplotlib.pyplot as plt

class playHouse:
    def __init__(self, file):
        self.data = pd.read_csv(file)

    def getHead(self):
        print(self.data.head())

    def columnNames(self):
        print(self.data.dtypes)

    def pClass(self):
        #print(self.data.query("Pclass == 1").loc[:,'Survived'])
        #print(self.data.query("Pclass == 2").loc[:,'Survived'])
        #print(self.data.query("Pclass == 3").loc[:,'Survived'])

        #frstC = self.data.query("Pclass == 1")
        #scndC = self.data.query("Pclass == 2")
        #thrdC = self.data.query("Pclass == 3")

        first_class, second_class, thired_cass = self.data.groupby('Pclass')['Survived'].mean()
        print(first_class/thired_cass)


    def sex(self, age):
        print(self.data.groupby('Sex')['Survived'].mean())
        print(self.data[self.data['Age'] >= age].groupby('Sex')['Survived'].mean())
        #print(self.data.query("Age >=" + age).groupby('Sex')['Survived'].mean())


    def age(self, age):
        print(self.data[self.data['Age'] < age]['Age'].head())
        print(self.data[self.data['Age'] < age]['Survived'].mean())

    def survival(self, age):
        female, male = self.data.groupby('Sex')['Survived'].mean()
        first_class, second_class, thired_cass = self.data.groupby('Pclass')['Survived'].mean()
        child = self.data[self.data['Age'] < age]['Survived'].mean()
        adult = self.data[self.data['Age'] >= age]['Survived'].mean()
        c_emb, q_emb, s_emb = self.data.groupby('Embarked')['Survived'].mean()
        
        print(self.data.groupby('Parch')['Survived'].mean())

    def barG(self):
        a,b,c,d,e,f,g = self.data.groupby('Parch')['Survived'].mean()
        plt.bar(["0", "1", "2", "3", "4", "5", "6"],[a,b,c,d,e,f,g])
        plt.ylabel("Survived %")
        plt.xlabel("Parents/Children")
        plt.show()
        
    def ageRange(self):
        df = self.data
        age_bins = [0, 10, 17, 34, 55, 150]
        age_labels = ['0-10','11-17','18-34','35-54','55+']
        df['age_groups'] = pd.cut(df['Age'], bins = age_bins, labels = age_labels)
        #age_groups = age_groups.value_counts(normalize=True, sort=False)

        print(df.groupby('age_groups')['Survived'].mean())
    

        plt.bar(age_labels, df.groupby('age_groups')['Survived'].mean())
        plt.ylabel("Survived %")
        plt.xlabel("Age Groups")
        plt.show()

def main():
    
    f = playHouse('Titanic.csv')

    f.columnNames()
    #f.pClass()
    #f.sex(18)
    #f.survival(18)
    #f.barG()
    f.ageRange()


    
    # The Education Act of 1892
    # First piece of legislation to make school attendance compulsory between the ages of 11 and 17
    # Birkenhead drill


if __name__=='__main__':
    main()
