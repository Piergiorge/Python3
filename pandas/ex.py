import pandas as pd
import seaborn as srn
import statistics as sts
from sklearn import datasets
# Load and return the boston house-prices dataset (regression).
data = datasets.load_boston()
toy = pd.DataFrame(data["data"], columns=data["feature_names"])
display(toy)
print(toy.shape)
agrupado = toy.groupby(['AGE'])

agrupado = toy.groupby(['AGE']).size()
display(agrupado)
toy['AGE'].describe()
srn.distplot(toy['AGE']).set_title('AGE')

# outliers
toy.loc[(toy['AGE'] < 0) | (toy['AGE'] > 120)]

# NA
toy.isnull().sum()
