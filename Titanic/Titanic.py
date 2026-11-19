import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# titanic_data = pd.read_csv("C:/Users/72857/PycharmProjects/solutions/Titanic/train.csv")
titanic_data = pd.read_csv("train.csv")


print(titanic_data.head())


# X data to use Pclass, sex, age, fare, parch, SibSp
# y survived
cols_to_use = ['Pclass', 'Sex', 'Age', 'Fare', 'Parch', 'SibSp', 'Embarked']
X = titanic_data[cols_to_use].copy()

y = titanic_data.Survived


# Get average total age, for passengers with missing age
X['Age'] = X['Age'].fillna(X['Age'].mean())

# convert text to numbers for sex
X['Sex'] = X['Sex'].map({
    'male': 0,
    'female': 1
})

# convert text to numbers for embarked
X['Embarked'] = X['Embarked'].map({
    'S': 0,
    'C': 1,
    'Q': 2
})


# split data, and designate valudation amount
train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.2, random_state=0)

# model
forest_model = RandomForestClassifier(random_state=0)
forest_model.fit(train_X, train_y)

# predictions
titan_preds = forest_model.predict(val_X)
print(accuracy_score(val_y, titan_preds))


#
test_data = pd.read_csv("test.csv")

test_X = test_data[cols_to_use].copy()

test_X['Age'] = test_X['Age'].fillna(X['Age'].mean())

# convert text to numbers for sex
test_X['Sex'] = test_X['Sex'].map({
    'male': 0,
    'female': 1
})

# convert text to numbers for embarked
test_X['Embarked'] = test_X['Embarked'].map({
    'S': 0,
    'C': 1,
    'Q': 2
})

test_y = forest_model.predict(test_X)

submission = pd.DataFrame({"PassengerId": test_data["PassengerId"], "Survived": test_y})

submission.to_csv("submission.csv", index=False)


"""
ajust values
new model
add feature
"""



# sns.countplot(
#     data=titanic_data,
#     x='Embarked',
#     hue='Survived'
# )

# sns.regplot(x=titanic_data['SibSp'], y=titanic_data['Survived'])

# plt.show()


# missing values age, cabins