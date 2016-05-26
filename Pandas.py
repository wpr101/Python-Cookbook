import numpy as np
import pandas as pd

df = pd.DataFrame([10,20,30,40], columns=['numbers'],
                  index=['a', 'b', 'c', 'd'])

print(df)
print(df.index)
print(df.columns)
print(df.sum)
print(df.apply(lambda x: x ** 2))
