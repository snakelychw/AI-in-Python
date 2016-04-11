# Hongwei Cheng - hcp598 - 04/03/2016
# Programming Assignment 1 -
# problem 1
def binarySearch(L, v):
    '''Binary search through a list L for the element v'''
    low = 0
    high = len(L)-1
    count = 0
    while low < high:
        mid = low + (high-low)/2 #cut the List in half
        if L[mid] == v:
            return (True, count) #Luckily found v
        if L[mid] < v:
            low = mid+1          #v is in the lower half
        if L[mid] > v:
            high = mid           #v is in the higher half
        count = count + 1
    return (False, count)

#problem 2
def mean(L):
    '''Return the average of a list L'''
    if len(L) == 0:               #escape from empty list
        return
    s = (float)(sum(L))          #s is the sum of elements in L
    num = (float)(len(L))        #num is the # of elements in L
    return s/num                 # return the mean

def median(L):
    '''Return the median of a list L. For a list with an even number of elements, let the median be the average of the two central items.)'''
    length = len(L)
    if length == 0:                   #escape from empty list
        return
    L = sorted(L)                     # to find median, sort first
    if length%2 == 0:
        return (float)(L[length/2-1]+L[length/2])/(float)(2)  # There are a even number of elements in L. Return average of 2 central
    return L[length/2]                   # Odd number of elements. Return central 1

#problem 3
def dfs(tree, elem):
    '''dfs a tree represented by nested lists to search elem'''
    if len(tree) == 0:                      #escape from empty list
        return False
    stack = []                              #use a stack for DFS
    res = False
    print tree[0]
    if tree[0] == elem:
        return True
    if len(tree) > 1:                       #push into stack
        for li in tree[1:]:
            stack.append(li)
    while len(stack) != 0:      #pop out and recursively call dfs
        res = res or dfs(stack.pop(), elem)
        if res:
            return True
    return False
    
def bfs(tree, elem):
    '''bfs a tree represented by nested lists to search elem'''
    if len(tree) == 0:                      #escape from empty list
        return False
    queue = []                              #use a queue for BFS
    queue.append(tree)                      #enqueue root
    while len(queue) != 0:
        temp = queue.pop(0)
        print temp[0]                       # visit nodes in this level
        if temp[0] == elem:
            return True
        if len(temp)>1:                     # enqueue next level
            for li in temp[1:]:
                queue.append(li)
    return False

#problem 4
class TTTBoard:
    '''This is a tic toc toe board game class.'''
    def __init__(self):
        '''initialize the board. set them to * as default value'''
        self.board = list('*'*9)

    def __str__(self):
        '''print the current board in 3*3 form'''
        s = self.board[0] + self.board[1] + self.board[2] + "\n"
        s= s + self.board[3] + self.board[4] + self.board[5] + "\n"
        s= s + self.board[6] + self.board[7] + self.board[8] + "\n"
        return s

    def makeMove(self, player, pos):
        '''make move as given player at given position on the game board'''
        if pos<0 or pos > 8 or self.board[pos]!= '*': # invalid move
            return False
        self.board[pos] = player                      # valid move made
        return True

    def hasWon(self, player):
        '''Returns True if player has won the game, and False if not'''
        if self.board[4] == player:                   # check for wining cases
            if self.board[3] == player and self.board[5] == player:
                return True
            if self.board[0] == player and self.board[8] == player:
                return True
            if self.board[1] == player and self.board[7] == player:
                return True
            if self.board[2] == player and self.board[6] == player:
                return True
        if self.board[0] == player:
            if self.board[1] == player and self.board[2] == player:
                return True
            if self.board[3] == player and self.board[6] == player:
                return True
        if self.board[8] == player:
            if self.board[2] == player and self.board[5] == player:
                return True
            if self.board[6] == player and self.board[7] == player:
                return True
        return False                                 # not wining


    def gameOver(self):
        '''Returns True if someone has won or if the board is full, False otherwise'''
        if self.hasWon('X') or self.hasWon('O'):               # game is over by someone wining
            return True
        for li in self.board:
            if li == '*':
                return False
        return True                                  # game is over by no more space

    def clear(self):
        '''Clears the board to reset the game'''
        self.__init__()                             # reuse constructor




