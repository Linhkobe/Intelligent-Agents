#################################
### a stateful reflex agent ### 
#################################

import matplotlib.pyplot as plt
import numpy as np
random import

## User will enter the number of rows and columns he wants
L = int(input("Number of rows?"))
C = int(input("Number of columns?"))

## Money coordinates
x = np.random.randint(0,L)
y = np.random.randint(0,C)
coor = [x,y]
print("The initial money position: ",coor)

## Creating a grid
matrix = np.random.randint(2, size=(L, C))
matrix = matrix.reshape((L, C))
print("Grid as a matrix of 0 and 1, \n '0' represents light cells \n '1' represents dark cells ")
print(matrix)
row_labels = range(L)

## Function to draw the grid using matplotlib
def renderMatrix(matrix, x, y):
     plt. ticks(range(L), row_labels)
     plt.imshow(matrix, 'Oranges')
     plt.plot(y, x, 'or')
     plt.title("The reflex agent with the state")
     plt.show(block=False)
     plt.pause(0.3)
     plt.clf() ## To display each agent step/movement, comment out this line

## Agent function
def simpleReflexAgent(x, y):
     if matrix[x][y] == 1:
         matrix[x][y] = 0
         return True
     else:
         return False

def main():
     overall x
     overall y
     global coordinator
     total_moves = 0
     color_changes = 0
     whileTrue:
         dark_cells = np.argwhere(matrix == 1)
         if len(dark_cells) == 0:
             break
         dark_cell = dark_cells[0]
         x_new, y_new = dark_cell
         x, y = x_new, y_new
         if simpleReflexAgent(x, y):
             renderMatrix(matrix, x, y)
             color_changes += 1
         coor=[x,y]
         print("Agent's position is:", coor)
         total_moves += 1

     print("Number of cleanings:", color_changes)
     print("Number of total moves: ",total_moves)
     print("Agent performance is:", round(color_changes/total_moves,2)*100,"%")
     print("Done")
     plt.show()

if __name__ == "__main__":
   main()
