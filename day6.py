

def count_yes_answers():

    with open('day6.txt') as f:
        lines = f.read().split('\n\n')

        counter = 0

        for line in lines:
            counter += len(set(line.replace('\n', '')))

        return counter
            

# print(count_yes_answers())

def count_yes_answers_2():

    with open('day6.txt') as f:
        lines = f.read().split('\n\n')
        # print(lines)
        counter = 0

        for line in lines:

            count = line.count('\n')
            print('line = ', line, 'count = ', count)
            

            for char in set(line):
                if line.count(char) == count + 1:
                    
                    print('char =', char, 'char_count = ', line.count(char))
                    counter += 1

        return counter
            
print(count_yes_answers_2())
