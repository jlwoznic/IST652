# Pandas Activity
# Repeat the activity that we just went through in the lecture to read the data from the provided State Data. Transform the data.
#
# state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],'PostCode':['AL','AK','AZ','AR'],'Area':['52,423','656,424','*','53,182'],'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
# 1. Create a dataframe using pd.DataFrame(state_data, columns=['State','PostCode','Area','Pop'].
# 2. Display the table.
# 3. Index the table by 'State'.
# 4. Replace the '*' with '0'.
# 5. Define a function to replace ',' with ''.
# 6. Use this function to replace the commas in 'Area' and 'Pop'.

import pandas as pd
import numpy as np

# state date
state_data = {'State':['Alabama','Alaska','Arizona','Arkansas'],
              'PostCode':['AL','AK','AZ','AR'],
              'Area':['52,423','656,424','*','53,182'],
              'Pop':['4,040,587','550,043','3,665,228','2,350,750']}
# 1. convert to a dataframe
stateDF = pd.DataFrame(state_data, columns = ['State', 'PostCode', 'Area', 'Pop'])
## 2. show the dataframe
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

# You did steps 1-6 in the async - so grab someone's code and then continue with these steps:
# 7.  Convert Area and Populations to float type numbers
stateDF["Area"] = pd.to_numeric(stateDF["Area"], downcast="float")
stateDF["Pop"] = pd.to_numeric(stateDF["Pop"], downcast="float")
stateDF
# 8.  Find the mean of the area
aMean = stateDF["Area"].mean()
# 9.  Replace any 0 entries in the Area column with the mean
stateDF = stateDF.replace(0, aMean)
stateDF
# 10.  Display the first 2 rows of the table
stateDF[0:2]
# 11.  Display the last 2 rows of the table.
stateDF[2:4]

