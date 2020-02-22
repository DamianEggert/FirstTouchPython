number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#first 0 is row, secend is column
print(number_grid[0][0])

for row in number_grid:
    for column in row:
        print(column)
