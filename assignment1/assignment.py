#############################
univ_id = "0000"           ##
#############################

from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, LEFT, RIGHT, BOTTOM
from Problem import Problem
import random
import sudoku_50 as problem_set

MARGIN = 20  # Pixels around the board
SIDE = 50  # Width of every board cell.
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9  # Width and height of the whole board
DELAY = 0.05  # the delay time makes the changing number visible
#PROBLEM_NUM = problem_set.problem_num

class SudokuUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.__initUI()

    def __initUI(self):
        self.parent.title("AI: Sudoku Solver")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT + 10)
        self.easy_problem = Problem(self.canvas, 0, DELAY, random.randint(0, 1), setting = "easy")
        self.hard_problem = Problem(self.canvas, 0, DELAY, random.randint(0, 1), setting = "hard")

        self.problem = None # Set this by click button
        
        
        # Initialize each cell in the puzzle
        for i in range(1, 10):
            for j in range(1, 10):
                self.item = self.canvas.create_text(
                    MARGIN + (j - 1) * SIDE + SIDE / 2, MARGIN + (i - 1) * SIDE + SIDE / 2,
                    text='', tags="numbers", fill="black", font=("Helvetica", 12)
                )
        self.item = self.canvas.create_text(40, 490, text='Count :', fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(95, 490, text='', fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(170, 490, text='Average :', fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(225, 490, text='',fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(320, 490, text='Ranking :',fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(370, 490, text='', fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(420, 490, text='Total :', fill="black", font=("Helvetica", 13))
        self.item = self.canvas.create_text(460, 490, text='', fill="black", font=("Helvetica", 13))
        self.canvas.pack(fill=BOTH, side=TOP)
        self.start_button1 = Button(self, text="__Hard__", command=self.__start_hard_solver)
        self.start_button2 = Button(self, text="__Easy__", command=self.__start_easy_solver)
        
        self.start_button2.pack(side=LEFT)
        self.start_button1.pack(side=RIGHT)
        #self.start_button2.config(state="disabled")
        self.__draw_grid()

    # Draws 9x9 grid
    def __draw_grid(self):
        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=width)
            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill="black", width=width)
    def __start_easy_solver(self):
      self.problem = self.easy_problem
      self.__start_solver()
      
    def __start_hard_solver(self):
      self.problem = self.hard_problem
      self.__start_solver()
      
      
    def __start_solver(self):
        self.start_button1.config(state="disabled")
        self.start_button2.config(state="disabled")
        for i in range(self.problem.problem_num):
            for m in range(1, 10):
                for n in range(1, 10):
                    if(self.problem.given_number[m-1][n-1] != 0): self.canvas.itemconfig(9 * (m - 1) + n, text=self.problem.given_number[m-1][n-1], tags="numbers", fill="blue")
                    else:self.canvas.itemconfig(9 * (m - 1) + n, text='', tags="numbers", fill="black")
                    
            self.solver_class = solver_class(self.problem)
            self.solver_class.solver()
            if self.problem.finished==0:
                self.problem.fail()
                return
            self.canvas.update()
            
            
            if(i != self.problem.problem_num -1):  self.problem = Problem(self.canvas, self.problem.tk, 0.0, self.problem.temp, setting = self.problem.setting)
        self.problem.update_a()
        #self.start_button2.config(state="active")
        
        #If the problem has finished, this function will display "Finished!"
        self.problem.is_done()
        
    def __submit(self):
        request=self.problem.submit(univ_id, "")
        message=request.split(',')
        if int(message[0]) == 100:
            self.problem.fail_10min()
        elif int(message[0]) == 101:
            self.canvas.update()
            self.canvas.itemconfig(87, text=int(message[1]), tags="numbers", fill="blue")
            self.canvas.itemconfig(89, text=int(message[2]), tags="numbers", fill="blue")
            self.problem.already_done()
        elif int(message[0]) == 102:
            self.canvas.update()
            self.canvas.itemconfig(87, text=int(message[1]), tags="numbers", fill="blue")
            self.canvas.itemconfig(89, text=int(message[2]), tags="numbers", fill="blue")
            self.problem.is_done()
        elif int(message[0]) == 501:
            #   print "501"
            self.problem.wrong_id_pw()

class solver_class():
    def __init__(self, problem):
        self.problem = problem
        self.given_number = problem.given_number    # a list of lists containing original sudoku grid

    def solver(self):
        self.puzzle = []
        new = []
        for i in range(0, 9):
            for j in range(0, 9):
                if(self.given_number[i][j] != 0): new.append(self.given_number[i][j])
                else: new.append(0)
            self.puzzle.append(new)
            new = []
        # self.puzzle is initalized to hold original values


        # TO DO: need to write solver
        # Your code goes here...
        # this is example using for loop
        # you have to improve this code

        """TODO: original code: loop"""
        """
        for i in range(1, 10):
            for j in range(1, 10):
                for k in range(1, 10):  # what to write in the empty slot
                    #print(f"({i},{j},{k})")
                    if self.given_number[i - 1][j - 1] == 0:    # if the slot is empty
                        
                        output = self.problem.checker(i, j, k)  # Try to input 'K' & This increases the number of attempts
                        # all the checker does is check if this is the solution
                        if output == 1:  # if the value is correct, checker will output 1. Otherwise, output is 0.
                            self.puzzle[i-1][j-1]=k
                            break
                    else:
                        break
        """
        
       

        #rows, cols, squares, possible_answers = self.get_possible_answers(self.given_number)

        """
        # TODO: opt1 - using checker function for remaining values : works on EASY
        for i in range(1, 10):
            for j in range(1, 10):
                for k in possible_answers[i-1][j-1]:  # what to write in the empty slot
                    output = self.problem.checker(i, j, k)  # Try to input 'K' & This increases the number of attempts
                    if output == 1:  # if the value is correct, checker will output 1. Otherwise, output is 0.
                        self.puzzle[i-1][j-1]=k
                        break
        """
        # TODO: opt2
        for i in range(9):
            for j in range(9):
                rows, cols, squares, possible_answers = self.get_possible_answers(self.puzzle)
                possible_answer = possible_answers[i][j]
                for k in possible_answer:
                    output = self.problem.checker(i+1, j+1, k)
                    if output == 1:
                        self.puzzle[i][j]=k
                        break
        """
        success = self.recursive_backtracking(0)
        if success:
            for i in range(1, 10):
                for j in range(1, 10):
                    output = self.problem.checker(i, j, self.puzzle[i-1][j-1])  # Try to input 'K' & This increases the number of attempts
                    if output != 0:
                        print(f"error")
        """
    



    def get_possible_answers(self, numbers):
        # first, get the possible values for each position 
        rows = []
        for k in numbers:
            rows.append([e for e in k if e != 0])

        transposed = [list(x) for x in zip(*numbers)]
        cols = []
        for k in transposed:
            cols.append([e for e in k if e != 0])

        squares = []
        for square_i in range(3):
            for square_j in range(3):
                # given_number_list_{square/row/col} holds the existing values
                given_number_rows = numbers[3*square_i : 3*(square_i+1)]
                given_number_list_square = []
                for row in given_number_rows:
                    given_number_list_square.extend(row[3*square_j : 3*(square_j+1)])
                squares.append([e for e in given_number_list_square if e != 0])
        
        #print(f"rows: {rows}")
        #print(f"cols: {cols}")
        #print(f"squares: {squares}")

        # make a list of list of lists that hold possible answers
        possible_answers = []
        for i in range(9):
            possible_answer_row = []
            for j in range(9):
                if numbers[i][j] != 0:
                    possible_answer = [numbers[i][j]]
                else:
                    possible_answer = []
                    square_i = i // 3
                    square_j = j // 3
                    square_index = 3*square_i + square_j
                    for k in range(9):
                        k += 1
                        if k not in rows[i] and k not in cols[j] and k not in squares[square_index]:
                            possible_answer.append(k)
                possible_answer_row.append(possible_answer)
            possible_answers.append(possible_answer_row)
        
        #print(f"possible answers: {possible_answers}")

        return rows, cols, squares, possible_answers

    


    def recursive_backtracking(self, index):
        if index == 80:
            return True
        
        # if not finished
        i = index // 9
        j = index % 9
        val = self.given_number[i][j]
        if val != 0:
            self.recursive_backtracking(index + 1)

        rows, cols, squares, possible_answers = self.get_possible_answers(self.puzzle)
        possible_answer = possible_answers[i][j]

        for e in possible_answer:
            self.puzzle[i][j] = e
            is_finished = self.recursive_backtracking(index+1)
            if is_finished:
                return True
            else:
                self.puzzle[i][j] = 0
        
        return False






if __name__ == "__main__":
    root = Tk()
    SudokuUI(root)
    root.geometry("%dx%d" % (WIDTH, HEIGHT + 40))
    root.mainloop()
