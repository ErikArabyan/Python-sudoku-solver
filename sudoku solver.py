board = [[".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

M = 9

def puzzle(board):
    for x in range(9):
        for y in range(9):
            board[x][y] = str(board[x][y])

    for i in range(9):
        print(board[i])


def solve(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False
        
    for x in range(9):
        if board[x][col] == num:
            return False
        
    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
            
    return True


def Suduko(board, row, col):
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j] == '.':
                board[i][j] = '0'
            board[i][j] = int(board[i][j])

    if row == M - 1 and col == M:
        return True
    
    if col == M:
        row += 1
        col = 0

    if board[row][col] > 0:
        return Suduko(board, row, col + 1)
    
    for num in range(1, M + 1, 1): 
        if solve(board, row, col, num):
            board[row][col] = num
            if Suduko(board, row, col + 1):
                return True
        board[row][col] = 0
        
    return False


if (Suduko(board, 0, 0)):
    puzzle(board)



# board= [[".",".","9","7","4","8",".",".","."],
#         ["7",".",".",".",".",".",".",".","."],
#         [".","2",".","1",".","9",".",".","."],
#         [".",".","7",".",".",".","2","4","."],
#         [".","6","4",".","1",".","5","9","."],
#         [".","9","8",".",".",".","3",".","."],
#         [".",".",".","8",".","3",".","2","."],
#         [".",".",".",".",".",".",".",".","6"],
#         [".",".",".","2","7","5","9",".","."]]

# y = ['1','2','3','4','5','6','7','8','9']
# for angam in range(81):
#     for tox in range(9):
#         for syun in range(9):
#             if board[tox][syun] == '.':
#                 if 0<=tox<=2:
#                     if 0<=syun<=2:
#                         for tox1 in range(3):
#                             for syun1 in range(3):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 3<=syun<=5:
#                         for tox1 in range(3):
#                             for syun1 in range(3,6):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 6<=syun<=8:
#                         for tox1 in range(3):
#                             for syun1 in range(6,9):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                 elif 3<=tox<=5:
#                     if 0<=syun<=2:
#                         for tox1 in range(3,6):
#                             for syun1 in range(3):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 3<=syun<=5:
#                         for tox1 in range(3,6):
#                             for syun1 in range(3,6):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 6<=syun<=8:
#                         for tox1 in range(3,6):
#                             for syun1 in range(6,9):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                 elif 6<=tox<=8:
#                     if 0<=syun<=2:
#                         for tox1 in range(6,9):
#                             for syun1 in range(3):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 3<=syun<=5:
#                         for tox1 in range(6,9):
#                             for syun1 in range(3,6):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                     elif 6<=syun<=8:
#                         for tox1 in range(6,9):
#                             for syun1 in range(6,9):
#                                 if board[tox1][syun1] != '.':
#                                     y.remove(board[tox1][syun1])
#                 for horizontal in board[tox]:
#                     if horizontal != '.':
#                         try:
#                             y.remove(horizontal)
#                         except:
#                             continue
#                 for vertikal in range(9):
#                     try:
#                         y.remove(board[vertikal][syun])
#                     except:
#                         continue
#                 if len(y) == 1:
#                     board[tox][syun] = y[0]
#                     y = ['1','2','3','4','5','6','7','8','9']
#                 else:
#                     y = ['1','2','3','4','5','6','7','8','9']
# for pat in range(9):
#     print(board[pat])


# board= [[".",".","9","7","4","8",".",".","."],
#         ["7",".",".",".",".",".",".",".","."],
#         [".","2",".","1",".","9",".",".","."],
#         [".",".","7",".",".",".","2","4","."],
#         [".","6","4",".","1",".","5","9","."],
#         [".","9","8",".",".",".","3",".","."],
#         [".",".",".","8",".","3",".","2","."],
#         [".",".",".",".",".",".",".",".","6"],
#         [".",".",".","2","7","5","9",".","."]]
# M = 9
# def puzzle(a):
#     newGrid = [[], [], [], [], [], [], [], [], []]
#     for x in range(9):
#         for y in range(9):
#             v = str(a[x][y])
#             newGrid[x].append(v)
#     for i in range(9):
#         print(newGrid[i])
# def solve(board, row, col, num):
#     for x in range(9):
#         if board[row][x] == num:
#             return False
#     for x in range(9):
#         if board[x][col] == num:
#             return False
#     startRow = row - row % 3
#     startCol = col - col % 3
#     for i in range(3):
#         for j in range(3):
#             if board[i + startRow][j + startCol] == num:
#                 return False
#     return True
# def Suduko(board, row, col):
#     for i in range(0, len(board)):
#         for j in range(0, len(board[i])):
#             if board[i][j] == '.':
#                 board[i][j] = '0'
#             board[i][j] = int(board[i][j])
#     if row == M - 1 and col == M:
#         return True
#     if col == M:
#         row += 1
#         col = 0
#     if board[row][col] > 0:
#         return Suduko(board, row, col + 1)
#     for num in range(1, M + 1, 1): 
#         if solve(board, row, col, num):

#             board[row][col] = num
#             if Suduko(board, row, col + 1):
#                 return True
#         board[row][col] = 0
#     return False
# if (Suduko(board, 0, 0)):
#     puzzle(board)
# else:
#     print("Solution does not exist:( ")

# x = [[1],[2],[3]]
# print(len(x))
# print([i for i in x])
# for i in x:
#     for j in i:
#         print(j)
# for i in range(3):
#     print(*x[i])





# n = int(input())
# a = 1
# b = 0
# z = 0
# while True:
#     for i in range(a):
#         b += 1
#         if i>z:
#             z = i
#         if b == n:
#             break
#     a+=1
#     if b == n:
#         break
# if 1 <= z <= 2**31 - 1:
#     print(z+1)
# elif z > 2**31 - 1:
#     print(2**31-1)
# elif z >1:
#     print(1)

# a = 0
# b = 0
# while True:
#     a+=1
#     b+=a
#     if b>=n:
#         b-=n
#         break
# print(a)

# while True:
#     a+=1
#     for i in range(1,a):
#         print(i)
#         if i == n:
#             break
#     if i == n:
#         break
        #kopekneric enqana astichani tox hanum minchev a ic aveli poqr chstacvi

# n = int(input())
# k = n
# a = 0
# for i in range(1,n+1):
#     if k>i:
#         k-=i
#     if i>=k:
#         a = i
#         break
# if k==0:
#     if a-1 <= 2**31 - 1:
#         print(2**31 - 1) 
#     print(a-1)
# elif k!=0:
#     if a <= 2**31 - 1:
#         print(2**31 - 1) 
#     print(a)

# n=int(input('-->>'))
# i=0
# k=0
# while True:
#     i+=1
#     n-=i
#     if n<0:
#         k=i-1
#         break
#     if n==0:
#         k=i
#         break
# if k>2**31-1:
#     print(2**31-1)
# else:
#     print(k)

# def arrange(n: int) -> int:
#         row = 0
#         while True:
#                 row += 1
#                 if n // 2 > row:
#                         return row
# print(arrange(3))

# from time import time


# n = int(input())
# start = time()
# i=0
# k=0
# while True:
#     i+=1
#     n-=i
#     if n<0:
#         k=i-1
#         break
#     if n==0:
#         k=i
#         break
# print(k)
# end = time()
# print(end - start)

# n = int(input())
# start = time()
# i = 1
# a = 0
# k = 0
# while a<=n:
#         k = a
#         a+=i
#         i+=1
# z = a-k-1  
# print(z)
# end = time()
# print(end - start)
 
# import json
# player1 = {
# 'name': 'Aram', 
# 'age': 18,
# 'height':180, 
# 'awards':['master',3,2,1]
# }
# player2 = {
# 'name': 'Ani',  
# 'age': 14,
# 'height':178, 
# 'awards':[3,2,1]
# }
# myplayers = [player1,player2]
# with open('file_name', 'w') as file: 
#         json.dump(myplayers, file)
#         print(file)

# file = open('file_name')
# json_data = json.load(file) 
# for data in json_data:
#         print(data)
# for data in json_data:
#         print('\nPlayer name is', data['name']) 
#         print('Player age is', data['age']) 
#         print('Player height is', data['height']) 
#         print('Player awards is', data['awards'])

# file_name = 'about_users.txt'
# try:
#         with open(file_name) as file:
#                 user = json.load(file) 
#                 print('Hello',user)
# except:
#         username = input('what is your name? ') 
#         with open(file_name, 'w') as file:
#                 user = json.dump(username, file) 
#                 print('Hello',username)

# import json
# player1 = {
# 'name': 'Aram', 
# 'age': 18,
# 'height':180, 
# 'awards':['master',3,2,1]
# }
# player2 = {
# 'name': 'Ani',  
# 'age': 14,
# 'height':178, 
# 'awards':[3,2,1]
# }
# myplayers = [player1,player2]
# with open('file_name', 'w') as file: 
#         json.dump(myplayers, file)
#         # print(myplayers)
# file1 = open('file_name')
# json_data = json.load(file1) 
# # for data in json_data:
#         # print(json_data)
# for data in json_data:
#         print('\nPlayer name is', data['name']) 
#         print('Player age is', data['age']) 
#         print('Player height is', data['height']) 
#         print('Player awards is', data['awards'])

# import json
# file_name = 'about_users.txt'
# try:
#         with open(file_name) as file: 
#                 user = json.load(file) 
#                 print('Hello',user)
# except:
#         username = input('what is your name? ') 
#         with open(file_name, 'w') as file:
#                 user = json.dump(username, file) 
#                 print('Hello',username)

# import json
# info = 'userdata.txt'
# try:
#         with open(info, 'r') as file:
#                 for i in file:
#                         print('username is:', i['name'])
#                         print('age is:', i['age'])
# except:
#         name = input()
#         age = input()
#         with open(info, 'w') as file:
#                 username = json.dump(name, file)
#                 userage = json.dump(age, file)
# print(file)
        
# import json
# x = """{"name":"Erik",
#         "age":"22",
#         "heigh":"180"
# }"""
# with open('y.json','w') as y:
#         k = json.loads(x)
# y = open('y.json','r')
# print(k)

# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# n = 0
# m = 0
# for i in range(len(height)):
#         if height[i]>0 and height[i+1]<height[i]:
#                 n = height[i]
#                 for j in range(i+1,-1):
#                         if height[j]>=height[n]:
#                                 m = height[j]

# board= [["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]

# y = ['1','2','3','4','5','6','7','8','9']
# for tox in range(9):
#     for syun in range(9):
#         if board[tox][syun]== '.':
#             if 0<=tox<=2:
#                 if 0<=syun<=2:
#                     for tox1 in range(3):
#                         for syun1 in range(3):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 3<=syun<=5:
#                     for tox1 in range(3):
#                         for syun1 in range(3,6):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 6<=syun<=8:
#                     for tox1 in range(3):
#                         for syun1 in range(6,9):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#             elif 3<=tox<=5:
#                 if 0<=syun<=2:
#                     for tox1 in range(3,6):
#                         for syun1 in range(3):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 3<=syun<=5:
#                     for tox1 in range(3,6):
#                         for syun1 in range(3,6):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 6<=syun<=8:
#                     for tox1 in range(3,6):
#                         for syun1 in range(6,9):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#             elif 6<=tox<=8:
#                 if 0<=syun<=2:
#                     for tox1 in range(6,9):
#                         for syun1 in range(3):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 3<=syun<=5:
#                     for tox1 in range(6,9):
#                         for syun1 in range(3,6):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#                 elif 6<=syun<=8:
#                     for tox1 in range(6,9):
#                         for syun1 in range(6,9):
#                             if board[tox1][syun1] != '.':
#                                 y.remove(board[tox1][syun1])
#             for horizontal in board[tox]:
#                 if horizontal != '.':
#                     try:
#                         y.remove(horizontal)
#                     except:
#                         continue
#             for vertikal in range(9):
#                 try:
#                     y.remove(board[horizontal][syun])
#                 except:
#                     continue
#             if len(y) == 1:
#                 board[tox][syun] = y
#                 y = ['1','2','3','4','5','6','7','8','9']
#             else:
#                 y = ['1','2','3','4','5','6','7','8','9']
# for pat in range(9):
#     print(board[pat])