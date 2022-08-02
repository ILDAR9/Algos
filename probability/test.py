import math
import numpy

if __name__ == '__main__':
    # import pandas as pd
    # data = {
    #     'Country': ['a', 'b', 'a','c','b'],
    #     'Count': [5,1,12,5,12]
    # }
    
    # df = pd.DataFrame(data)
    # df = df.sort_values(by = 'Country')
    # df['sum'] = df.groupby(['Country'])['Count'].cumsum()
    # y = df.iloc[1]['sum']
    # print(y)
    # nums = [0.33, 0.33, 0.33, 0]
    # nums = [0.4, 0.3, 0.2, 0.1]
    # nums = [0.25, 0.25, 0.25, 0.25]
    nums = [0.1, 0.85, 0.025, 0.025]
    s = sum(nums * 1/numpy.log(nums))
    print(s)