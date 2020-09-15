# Week 5 Activities
# Joyce Woznica

import pandas as pd
import numpy as np

# state date
state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],
              'PostCode':['AL','AK','AZ','AR'],
              'Area':['52,423','656,424','*','53,182'],
              'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
# 1. convert to a dataframe
stateDF = pd.DataFrame(state_data, columns = ['State', 'PostCode', 'Area', 'Pop'])
# 2. show the dataframe
# 3. Index by state (done) - column statement
stateDF
# 4. need to replace the '*' for Arizona Area with a 0
stateDF = stateDF.replace('*', '0')
stateDF

# 5. function to eliminate commas
def repl_comma(df):
    return df.replace(',', '')

# 6. replace commas
stateDF['Area'] = stateDF['Area'].map(repl_comma)
stateDF
stateDF['Pop'] = stateDF['Pop'].map(repl_comma)
stateDF

# 5.3 - Data Stacking and Unstacking
import pandas as pd
import numpy as np

# create a person dataframe
persondict = {'person':['Bob','Alice','Steve'],'age':[32,24,64],'weight':[128,86,95]}
personDF = pd.DataFrame(persondict, columns = ['person', 'age', 'weight'])
# 1. Index by person
personDF = personDF.set_index('person')
personDF

# 2. Stack into a tall object
# sort of like a melt in R (note)
result = personDF.stack()
result.shape
result.index

# 3. reset the index
personTall = result.reset_index()

# 4. rename the columns to 'person', 'attribute', 'value'
personTall.columns = ['person', 'attribute', 'value']
personTall

# 5. convert back to the original using unstack
personOrig = result.unstack()
personOrig

# 6. pivot
personPivot = personTall.pivot('person', 'attribute', 'value')
personPivot


