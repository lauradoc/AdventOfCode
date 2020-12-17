"""
The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.

For example, consider just the first seven characters of FBFBBFFRLR:

Start by considering the whole range, rows 0 through 127.
F means to take the lower half, keeping rows 0 through 63.
B means to take the upper half, keeping rows 32 through 63.
F means to take the lower half, keeping rows 32 through 47.
B means to take the upper half, keeping rows 40 through 47.
B keeps rows 44 through 47.
F keeps rows 44 through 45.
The final F keeps the lower of the two, row 44.
The last three characters will be either L or R; these specify exactly one of the 8 columns of seats on the plane (numbered 0 through 7). The same process as above proceeds again, this time with only three steps. L means to keep the lower half, while R means to keep the upper half.

For example, consider just the last 3 characters of FBFBBFFRLR:

Start by considering the whole range, columns 0 through 7.
R means to take the upper half, keeping columns 4 through 7.
L means to take the lower half, keeping columns 4 through 5.
The final R keeps the upper of the two, column 5.
So, decoding FBFBBFFRLR reveals that it is the seat at row 44, column 5.

Every seat also has a unique seat ID: multiply the row by 8, then add the column. In this example, the seat has ID 44 * 8 + 5 = 357.

Here are some other boarding passes:

BFFFBBFRRR: row 70, column 7, seat ID 567.
FFFBBBFRRR: row 14, column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
"""

# FFBBFFFLRL

def reset_variables():

    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7

    return min_row, max_row, min_col, max_col

inputfile = open('day5.txt', 'r')
data = [line.strip() for line in inputfile.readlines()]
print(data)
def find_passport(data):

    min_row = 0
    max_row = 127
    min_col = 0
    max_col = 7
    seat_id = 0
    max_seat_id = 0

    for line in lines:
        while min_row < max_row:

            pivot = int((min_row + max_row)/2)

            for char in line[:7]:
                if char == "F":
                    max_row = pivot
                    pivot = int((min_row + max_row)/2)
                if char == "B":
                    min_row = pivot + 1
                    pivot = int((min_row + max_row)/2)
            
            print('min row: ', min_row)

        while min_col < max_col:

            pivot = int((min_col + max_col)/2)

            for char in line[7:]:
                if char == "L":
                    max_col = pivot
                    pivot = int((min_col + max_col)/2)
                if char == "R":
                    min_col = pivot + 1
                    pivot = int((min_col + max_col)/2)
                if min_col == max_col:
                    print('min row: ', min_row, 'min col: ', min_col)
                    seat_id = (min_row * 8) + min_col
                    if seat_id > max_seat_id:
                        max_seat_id = seat_id
                    reset_variables()
            
            print('max col: ', max_col)

    return max_seat_id

print(find_passport(data))



