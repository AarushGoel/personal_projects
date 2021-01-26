import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_excel("data.xlsx",na_values=['0','###','ABS','AB']) #to fill these values with nan
dataset.columns=['S.No.',
                 'UPTU',
                 'Student',
                 'NAS301',
                 'NEC309',
                 'NCS301',
                 'NCS302',
                 'NHU302',
                 'NCS303',
                 'Th tot. marks',
                 'Th. %age',
                 'Total %age',
                 'Total marks 3rd SEM',
                 'NOE043',           
                 'NEC409' ,
                 'NCS401 ',
                 'NCS402'  ,
                 'NCS403 '     ,
                 'NHU401' ,
                 'No. of CP 4th Sem',
                 'No. of CP 3rd & 4th Sem',
                 '4th Sem Total Theory Marks',
                 '4th Sem Theory %',
                 'Overall 4th Sem %',
                 '4th Sem Total Marks',
                 'NCS501',
'NCS502',
'NCS503',
'NCS504',
'NCS505',
'NHU501',
'No. of CP 5th Sem',
'5th Sem Total Theory Marks',
'5th Sem Theory %',
'Overall 5th Sem %',
'5th Sem Total Marks',
'NCS063',
'NCS066',
'NCS601',
'NCS602',
'NCS603',
'NHU601',
'No. of CP 6th Sem',
'No. of CP 3rd & 4th & 5th Sem',
'6th Sem Total Theory Marks',
'6th Sem Total Marks',
'NOE077',
'NCS071',
'NIT701',
'NCS701',
'NCS702',
'7th Sem Total Theory Marks',
'7th Sem Total Marks',
'NOE081',
'NCS080',
'NCS801',
'NCS085',
'8th Sem Total Theory Marks',
'8th Sem Total Marks',
'Total_marks',
'Total %']


X = dataset.iloc[4:,3:59].values #taking only marks not name, roll no. change it accordingly
dataset2=pd.DataFrame(X)


y = dataset.iloc[:,-1].values


#converting string values to float or int 
dataset2=dataset2.apply(pd.to_numeric)
dataset2=dataset2.astype(float)

from sklearn.impute import SimpleImputer
sim=SimpleImputer()
X[:,:]=sim.fit_transform(X[:,:])

temp=pd.DataFrame(X[:,[2,3,4,5,6,7,8]])

temp[0].values_counts()
temp[1].values_counts()
temp[2].values_counts()
temp[3].values_counts()
temp[4].values_counts()
temp[5].values_counts()
temp[6].values_counts()
temp[7].values_counts()

