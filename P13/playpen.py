import pandas as pd
import numpy as np
from datetime import date

def ColumnsName(data):
    print(data.dtypes)

def uniqueCountry(data):
    data['country'] = data['country'].str.lower()
    data['country'] = data['country'].str.strip(' ./')
    
    # pattan matching
    patten_mapping = {}
    for i in data['country']:
        if type(i) == float:
            pass
        elif i == 'united states' or i == 'u.s' or 'america' in i:
            patten_mapping.update({i: 'United States'})
        elif i == 'united kingdom' or i == 'uk' or i == 'u.k' or i == 'britain' or i == 'england':
            patten_mapping.update({i: 'United Kingdom'})
        elif i == 'sa' or i == 's.a' or 'africasouth' in i:
            patten_mapping.update({i: 'South Africa'})
        else:
            patten_mapping.update({i: np.nan})
                
    data['country'] = data['country'].replace(patten_mapping)
    
    print(data['country'].unique())
    
def calumnDaysAgo(data):
    
    time_stamp = pd.Timestamp(date.today())
    data['days_ago'] = (time_stamp - pd.to_datetime(data['date_measured'], dayfirst=True))
    
    print(data['days_ago'].head())


def main():
    url = 'https://raw.githubusercontent,com/mwasjom/deaborn-data/master.iris'
    print(url)
    df = pd.read_csv('store_income_data_task.csv', skipinitialspace = True)
    ColumnsName(df)
    uniqueCountry(df)
    calumnDaysAgo(df)

if __name__=='__main__':
    main()
