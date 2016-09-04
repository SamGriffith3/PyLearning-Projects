def new_matrix():
    return [[1 for _ in range(3)] for _ in range(3)]

p1_matrix = new_matrix()



def column_sum(column_num):

    data = p1_matrix
    x = sum(row[column_num] for row in data)



for i in range(3):
    column_sum(i)
    y = 0
    y = y + x  #  How to use x in func() and in for loop?
    print(y)








