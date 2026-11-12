import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# titanic_data = pd.read_csv("C:/Users/72857/PycharmProjects/solutions/Titanic/train.csv")
titanic_data = pd.read_csv("train.csv")


print(titanic_data.head())


# sns.countplot(
#     data=titanic_data,
#     x='Sex',
#     hue='Survived'
# )

sns.regplot(x=titanic_data['Fare'], y=titanic_data['Survived'])

plt.show()
