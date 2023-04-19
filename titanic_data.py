import matplotlib.pyplot as plt
import pandas as pd

train_df = pd.read_csv('data/train.csv')
print(train_df.value_counts())
test_df = pd.read_csv('data/test.csv')

# Cleaning data for Age parameter using median
train_df['Age'].fillna(value=train_df['Age'].median(), inplace=True)


train_df['Pclass'].value_counts().plot(kind='bar')
plt.show()

train_df['Sex'].value_counts().plot(kind='pie')
plt.show()
