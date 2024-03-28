import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    car_data = pd.read_csv('Cars93.csv', index_col = 0, keep_default_na=False)
    print(car_data.columns)
    print(car_data['Rev.per.mile'].unique())
    print(car_data['Rev.per.mile'].nunique())
    print(car_data['Manufacturer'].unique())
    print(car_data['Manufacturer'].nunique())

    #y_list = [i for i in range(0, car_data['Horsepower'].max(), 10)]
    
    print('##')
    print(car_data['Wheelbase'])

    #print(car_data.groupby('Manufacturer')['Rev.per.mile'].mean())
    #print(car_data[car_data.Manufacturer == 'Audi'].loc[:,'Rev.per.mile'])
    
    Audi = car_data.query("Manufacturer == 'Audi'").loc[:,'Rev.per.mile']
    Hyundai = car_data[car_data.Manufacturer == 'Hyundai'].loc[:,'Rev.per.mile']
    Suzuki = car_data.query("Manufacturer == 'Suzuki'").loc[:,'Rev.per.mile']
    Toyota = car_data[car_data.Manufacturer == 'Toyota'].loc[:,'Rev.per.mile']
    
    #plt.boxplot([Audi, Hyundai, Suzuki, Toyota])
    #plt.xticks([1, 2, 3, 4],['Audi', 'Hyundai', 'Suzuki', 'Toyota'])

    '''
    need lables
    '''
    #plt.hist([car_data['MPG.city'], car_data['MPG.highway']], histtype='bar'])

    
    #plt.plot(car_data['Wheelbase'].sort_values(), car_data['Turn.circle'])
    
    #plt.xlabel('Wheelbase')
    #plt.ylabel('Turn circle')

    #y_list = [i for i in range(0, car_data['Horsepower'].max(), 10)]
    
    y = np.array(['Compact', 'Large', 'Midsize', 'Small', 'Sporty', 'Van'])
    print(car_data.groupby('Type')['Horsepower'].mean())

    plt.bar(y, car_data.groupby('Type')['Horsepower'].mean())

    plt.show()
    
if __name__=='__main__':
    main()
