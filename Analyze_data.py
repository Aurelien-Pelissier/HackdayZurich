import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 20})


### Milk the sun
### Centrifuge.io


df = pd.read_csv('energy-cooperatives-switzerland_data.csv', sep=';')
print(df)

# Indentify possible design criterai
# WHat elements are important ?
# FInd from the data
questions = []
questions += ['1_5'] # current number of members
questions += ['1_8'] # age group of the majority of today's members?
questions += ['1_9_1'] # Is membership in your cooperative linked to any special conditions
#questions += [('2_3_%s_1' % i) for i in range(1,17)] # In which areas is your cooperative currently active
questions += ['3_2'] #type of system
questions += ['3_5'] #How did you sell the generated electricity and ecological added value
questions += ['5_1'] #starting capital
questions += ['5_10_1'] #more than 50% owned by one person
#questions += [('7_1_%s' % i) for i in range(1,14)]  #Purpose of cooperative

question_label = []
question_label += ['Current number of members']
question_label += ["Age group of the majority of today's members"]
question_label += ["Is membership in your cooperative linked to any special conditions"]
#question_label += []
question_label += ['Type of system']
question_label += ['How did you sell the generated electricity and ecological added value']
question_label += ['Starting capital [CHF]']
question_label += ['More than 50% owned by one person ?']
question_label += ['Purpose of cooperative']

print(questions)


for label in df.columns:
    QQ = label.replace('@','')
    if QQ in questions:
        index = np.where(np.array(questions) == QQ)[0][0]
        data = df[[label]].to_numpy().reshape(-1)
        data = np.array([x for x in data if x!=' '])
        try:
            data = data.astype(int)
        except:
            pass

        plt.figure(figsize=(8,4))
        if label == '@1_5' or label == '@5_1':
            data[data==0]=1
            plt.hist(np.log(data), rwidth=0.9, color='black')
            labels_ = set(data)
            labels = np.sort(list(labels_))
            
            labels = np.linspace(np.log(np.min(labels)), np.log(np.max(labels)), 10)
            
            plt.xticks(labels, np.exp(labels).astype(int), rotation = 90)
            
        else:
            plt.hist(data, rwidth=0.9, color='black', bins=len(set(data)))
            labels_ = set(data)
            labels = np.sort(list(labels_))
            plt.xticks(labels, labels)
            
        print(data)
        plt.title(question_label[index])    
        plt.show()