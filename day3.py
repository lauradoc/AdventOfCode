"""
The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?

"""

def count_trees():

    with open('day3.txt') as f:
        lines = f.readlines() # list containing lines of file

        counter = 0
        x = 0
        y = 0

        while x < (len(lines)-1):
            line_length = len(lines[y]) - 2
            x += 1
            y += 3
            if y > line_length:
                y = y - line_length - 1
            tracker = lines[x][y]
            if tracker == '#':
                counter += 1
            
        return counter

print(count_trees())

"""
Determine the number of trees you would encounter if, for each of the following slopes, 
you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; 
multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of 
the listed slopes?
"""

def count_trees_2():
    
    with open('day3.txt') as f:
        lines = f.readlines() # list containing lines of file

        x = 0
        y = 0
        counter = 0

        while x < (len(lines)-1):
            line_length = len(lines[y]) - 2
            x += 1
            y += 1
            if y > line_length:
                y = y - line_length - 1
            tracker = lines[x][y]
            if tracker == '#':
                counter += 1
        
        return counter

print(count_trees_2())


def count_trees_3():
    with open('day3.txt') as f:
        lines = f.readlines() # list containing lines of file

        x = 0
        y = 0
        counter = 0

        while x < (len(lines)-1):
            line_length = len(lines[y]) - 2
            x += 1
            y += 5
            if y > line_length:
                y = y - line_length - 1
            tracker = lines[x][y]
            if tracker == '#':
                counter += 1
        
        return counter

print(count_trees_3())


def count_trees_4():

    with open('day3.txt') as f:
        lines = f.readlines() # list containing lines of file

        x = 0
        y = 0
        counter = 0

        while x < (len(lines)-1):
            line_length = len(lines[y]) - 2
            x += 1
            y += 7
            if y > line_length:
                y = y - line_length - 1
            tracker = lines[x][y]
            if tracker == '#':
                counter += 1
        
        return counter

print(count_trees_4())


def count_trees_5():

    with open('day3.txt') as f:
        lines = f.readlines() # list containing lines of file

        x = 0
        y = 0
        counter = 0

        while x < (len(lines)-1):
            line_length = len(lines[y]) - 2
            x += 2
            y += 1
            if y > line_length:
                y = y - line_length - 1
            tracker = lines[x][y]
            if tracker == '#':
                counter += 1
        
        return counter

print(count_trees() * count_trees_2() * count_trees_3() * count_trees_4() * count_trees_5())




