import json
'''
One thing you have to have rememember in the json file you have to write " " double
-quotes only + in the json there are no comments. And the json data stroes from
   .json    . Now the json.loads() parsed the data.
'''
data = '{"var1":"krishna","var2":17}'
# print(data ['var1'])  # You cannot run this 
parsed=json.loads(data)
print(parsed ['var1'])

data1={"Human":["male","female"],
"Animals":("lion","tiger","cheetah"),
"Birds":["Butterfly","Peacock"],
"isbad":False}

jsoncomp= json.dumps(data1)
print(jsoncomp)

# What is json.load  in python
'''
load() takes a file object and returns the json object. It is used to read 
JSON encoded data from a file and convert it into a Python dictionary and
 deserialize a file itself i.e. it accepts a file object.
'''

# what is sort_keys parameter in dumps
'''
It is used to convert the array of JSON objects into a sorted JSON object. 
The value of the sort_keys argument of the dumps() function will require to
set True to generate the sorted JSON objects from the array of 
 JSON objects.
'''