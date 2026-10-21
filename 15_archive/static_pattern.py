"""Input: matrix = [[1,2,3,4],
                [5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,
         9,5,6,7,
         8,12,11,10]
    """



def generatepattern(matrix):
    print()
    c = 1
    top = 0
    bottom = len(matrix)-1
    left = 0
    right = len(matrix[0])-1
    # for i in range(top,):
    #     for j in range(left,right+1):
    #         print(matrix[i][j],end="")
    #     print()

    for row in matrix:
        for value in row:
            print(value,end="")
        print() 

    result=[]
    for i in range(len(matrix)):
        row=[]
        for j in range(top,bottom+1):
            row.append(matrix[i][right])
        result.append(row)

    print(result)
    

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]
        ]
generatepattern(matrix)
