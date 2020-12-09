import requests

#api endpoint
URL = "https://adventofcode.com/2020/day"

#defining params dict for the parameters to be sent to the API
PARAMS = {'day':day, 'input':input_data}

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

# extracting data in json format 
data = r.json()

print(data)
"""
To try to debug the problem, they have created a list (your puzzle input) of passwords (according 
to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy indicates the lowest 
and highest number of times a given letter must appear for the password to be valid. For example, 
1-3 a means that the password must contain a at least 1 time and at most 3 times.
>>> valid_password(
    [1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc])
2
"""

# def valid_password(list):