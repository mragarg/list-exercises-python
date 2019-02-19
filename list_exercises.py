list_of_numbers = [1, 2, 3, 4]
list_of_numbers2 = [5, 6, 7, 8]

#Function returns the sum of all numbers in list
def sum_list(num_list):
    sum = 0
    for i in num_list:
        sum += i
    return sum

#Functions returns the largest number in list
def largest_number(num_list):
    max = num_list[0]
    for i in num_list:
        if(max < i):
            max = i
    return max

#Function returns the smallest number in list
def smallest_number(num_list):
    min = num_list[0]
    for i in num_list:
        if(min > i):
            min = i
    return min

#Function returns a list of even numbers from list
def even_number(num_list):
    result = []
    for i in num_list:
        if(i%2 == 0):
            result.append(i)
    return result
    
#Function returns the positive numbers from list
def positive_number(num_list):
    for i in num_list:
        if(i >= 0):
            print(i)

#Function returns all numbers from list as positive numbers
def positive_number2(num_list):
    result = []
    for i in num_list:
        result.append(abs(i))
    return result

#Function returns a list that's multiplied by a factor
def multi_list(num_list, factor):
    result = []
    for i in num_list:
        result.append(i * factor)
    return result

#Function returns two lists multiplied by each other
def multi_vector(list1, list2):
    result = []
    count = 0
    while(count < len(list1)):
        result.append(list1[count] * list2[count])
        count += 1
    return result

matrix1 = [ [1, 2] ,
            [3, 4] ]

matrix2 = [ [5, 6] ,
            [7, 8] ] 

#function adds two Matrices of 2x2
def matrix_addition(list1, list2):
    x = 0
    y = 0
    result = [ [0, 0] ,
                [0 , 0] ]
    while(x < len(list1)):
        while(y < len(list1)):
            result[x][y] = list1[x][y] + list2[x][y]
            y += 1
        y = 0
        x += 1
    return result

#Function returns two matrices added together of any size
def matrix_addition2(list1, list2):
    result = [[list1[x][y] + list2[x][y] for y in range(len(list1[0]))] for x in range(len(list1))]
    return result

dup_list = [1, 1, 2, 3, 4, 5, 5, 6]

#Function returns a list with duplicate entries removed
def de_dup(list1):
    result = []
    for i in list1:
        if i in result:
            pass
        else:
            result.append(i)
    return result

#Function returns two Matrixes multipled with a size of 2x2
def matrix_multi(list1, list2):
    result = [ [0, 0] , 
                [0, 0] ]
    #iterate through rows of list1
    for i in range(len(list1)):
        #iterate through columns of list2
        for j in range(len(list2[0])):
            #iterate through rows of list2
            for k in range(len(list2)):
                result[i][j] += list1[i][k] * list2[k][j]

    return result
    
    # new_matrix = []
    # for i in range(len(matrix1)):   #for each row in matrix 1
    #     inside_array = []
    #     #get each value
    #     rowlen = len(matrix1[0])    #number columns in 1st matrix
    #     row2len = len(matrix2[0])      #number columns in  2nd matrix
    #     x=0
    #     for j in range(row2len):        #for each columns in matrix 2
    #         for k in range(rowlen):
    #             # print("%d * %d" % (matrix1[i][k],matrix2[k][j]))
    #             x += (matrix1[i][k] * matrix2[k][j])
    #         inside_array.append(x)
    #         x=0
    #         # print(inside_array)
    #     new_matrix.append(inside_array)
    # return new_matrix

print(matrix_multi(matrix1, matrix2))