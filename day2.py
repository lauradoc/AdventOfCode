# import requests

# url = "https://adventofcode.com/2020/day/2/input"

# payload={}
# headers = {
#   'Cookie': '_ga=GA1.2.492482864.1607448368\'_gid=GA1.2.1448719921.1607448368;session=53616c7465645f5f9a88e5bfb018935096ff5ec20a1be2a56610bb48da4880475d04861b7afc5e8e307c622e401738cc'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)

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

def valid_password():

    with open('day2.txt') as f:
        lines = f.readlines() # list containing lines of file

        counter = 0

        for line in lines:
            line_list = line.strip(' ').split(' ')
            counters = line_list[0].split('-')
            min_val = int(counters[0])
            max_val = int(counters[1])
            char = line_list[1][0]
            password = line_list[2]
            if char in password:
                values = password.count(char)
                if values >= min_val and values <= max_val:
                    counter += 1

        return counter

print(valid_password())

"""
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
"""

def valid_password2():
            
    with open('day2.txt') as f:
        lines = f.readlines() # list containing lines of file

        counter = 0

        for line in lines:
            line_list = line.strip(' ').split(' ')
            counters = line_list[0].split('-')
            min_val = int(counters[0])
            max_val = int(counters[1])
            char = line_list[1][0]
            password = line_list[2]
            if password[min_val - 1] == char and password[max_val - 1] != char:
                counter += 1
            elif password[min_val -1] != char and password[max_val - 1] == char:
                counter += 1

        return counter

print(valid_password2())


