#Ques : Write a regex to extract all the numbers with orange color background from the below text in italics.


#{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}


# straight forward approach
import pandas as pd
json = {"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable(153)"}]}
df = [pd.json_normalize(json['orders'])['id'].tolist(),[pd.json_normalize(json['errors'])['code'][0]]]
df_list = [item for sublist in df for item in sublist] # using list comprehension
df_list
#output = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 648, 649, 650, 651, 652, 653, 3]

# Using re approach
import re
import json
import pandas as pd

pattern = input("Enter Pattern: "); # the pattern eg. any number from the input (10)
load = input("Enter text: ") # the json input

json_text = json.loads(load)

df =  [pd.json_normalize(json_text['orders'])['id'].tolist(),[pd.json_normalize(json_text['errors'])['code']]]

dfl = ' '.join([str(elem) for elem in df])
result = re.findall(pattern, dfl)
if result:
    print(result)
else:
    print("No match Found")
