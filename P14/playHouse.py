import pandas as pd

def missindData(data):
    print(data.isnull().sum())


def missing(data):
    print('d')
    newData = data[data['department'].isna()]
    print('d')
    print(newData)
    

def main():
    print('Hello World')
    store_income = pd.read_csv("store_income_data_task.csv")
    print(store_income.head())

    
    missindData(store_income)    

    missing(store_income)

if __name__=='__main__':
    main()
