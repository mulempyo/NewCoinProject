from pandas import Series
from pandas import DataFrame
data = {"open": [737,750], "high":[750,780], "low": [700,710], "close":[750,770]}
df = DataFrame(data)
s = Series([300,400])
df["volume"] = s
print(df)