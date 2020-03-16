import pandas as pd
import numpy as np


dataset = pd.DataFrame()
dataset['outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy',
                      'sunny', 'overcast', 'overcast', 'rainy']

dataset['temp'] = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild', 'mild', 'mild',
                   'hot', 'mild']
dataset['humidity'] = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal', 'high', 'normal', 'normal',
                       'normal', 'high', 'normal', 'high']
dataset['windy'] = ['false', 'true', 'false', 'false', 'false', 'true', 'true', 'false', 'false', 'false',
                    'true', 'true', 'false', 'true']
dataset['play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes',
                    'yes', 'yes', 'yes', 'no']
print(dataset)
"""
def computentropy():

    print(len(dataset['play']))
    print(len(dataset[dataset['play'] == 'yes']))

    total = len(dataset['play'])
    numofyes = len(dataset[dataset['play'] == 'yes'])
    numofno = len(dataset[dataset['play'] == 'no'])
    probabilityofyes = numofyes / total
    probabilityofno = numofno / total
    print(probabilityofyes)
    print(probabilityofno)

    entropy = -(probabilityofyes) * np.log2(probabilityofyes) - (probabilityofno) * np.log2(probabilityofno)
    return entropy


print("The entropy is", computentropy())
"""


def Informationgain():

    print("Lenght of Outlook is ", len(dataset['outlook']))
    print("Total Rainy", len(dataset[dataset['outlook'] == 'rainy']))
    print("Total Overcast", len(dataset[dataset['outlook'] == 'overcast']))
    print("Total Sunny", len(dataset[dataset['outlook'] == 'sunny']))
    total = len(dataset['outlook'])
    print("Length of Play is", len(dataset['play']))
    print("Total Yes", len(dataset[dataset['play'] == 'yes']))
    print("Total No", len(dataset[dataset['play'] == 'no']))
    total = len(dataset['play'])
    totalofsunny = len(dataset[dataset['outlook'] == 'sunny']) / total
    totalofrainy = len(dataset[dataset['outlook'] == 'rainy']) / total
    totalofovercast = len(dataset[dataset['outlook'] == 'overcast']) / total
    print("Probability of Sunny", totalofsunny)
    print("Probability of Overcast", totalofovercast)
    print("Probability of Rainy", totalofrainy)



    #entropysunny = -(totalofsunny) * np.log2(totalofsunny ) - (probabilityofno) * np.log2(probabilityofno)
Informationgain()