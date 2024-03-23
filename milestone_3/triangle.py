import sys

how_many_rows = int(sys.argv[1])
def get_row(row):
    result = []
    for i in range( len(row) + 1 ):
        if i == 0 or i == len(row):
            num = 1
        else:
            num = row[i - 1] + row[ i ]
        result.append(num)
    return result

def get_triangle(num_of_rows):
    result = [[1]]
    for i in range( num_of_rows-1 ):
        result.append(get_row(result[i]))

    return result

def prety_print(row, length):
    num_of_spaces = length-len(row)
    result = (' ' * num_of_spaces)
    for i in row:
        result += ' '+str(i)
    print (result)

for i in get_triangle(how_many_rows):
    prety_print( i, how_many_rows )
    # print(i)
