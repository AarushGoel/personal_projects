


import pandas as pd

import seaborn as sns



dataset=pd.read_csv('student.csv')
dataset.columns=['gender',
                 'race','ped','lunch',
                 'test',
                 'math','reading','writing']


dataset.info()
dataset.describe()

pd.plotting.scatter_matrix(dataset)
sns.pairplot(dataset)


sns.barplot(dataset['gender'].value_counts().index,
            dataset['gender'].value_counts(),
            hue=['female','male'])


sns.barplot(dataset['race'],dataset['math'])
sns.barplot(dataset['ped'],dataset['math'],hue=dataset['gender'])
sns.barplot(dataset['lunch'],dataset['math'],hue=dataset['gender'])
sns.barplot(dataset['test'],dataset['math'],hue=dataset['gender'])
sns.boxplot(dataset['math'],y=dataset['gender'],hue=dataset['gender'])




sns.barplot(dataset['race'],dataset['reading'],hue=dataset['gender'])
sns.barplot(dataset['ped'],dataset['reading'],hue=dataset['gender'])
sns.barplot(dataset['lunch'],dataset['reading'],hue=dataset['gender'])
sns.barplot(dataset['test'],dataset['reading'],hue=dataset['gender'])
sns.boxplot(dataset['reading'],dataset['gender'],hue=dataset['gender'])


sns.barplot(dataset['race'],dataset['writing'],hue=dataset['gender'])
sns.barplot(dataset['ped'],dataset['writing'],hue=dataset['gender'])
sns.barplot(dataset['lunch'],dataset['writing'],hue=dataset['gender'])
sns.barplot(dataset['test'],dataset['writing'],hue=dataset['gender'])
sns.boxplot(dataset['writing'],dataset['gender'],hue=dataset['gender'])



