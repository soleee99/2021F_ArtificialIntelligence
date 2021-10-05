
import random
import time
#import Problem_100
#import urllib2
import sudoku_50 as problem_set
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

#PROBLEM_NUM = problem_set.problem_num

class Problem:

    def __init__(self, canvas, num, delay, temp, setting = "easy"):
        self.canvas = canvas
        self.tk = num
        self.DELAY = delay
        self.finished = 0
        self.setting = setting
        self.problem_num = 0
        
        if(self.setting == "easy"):
          self.problem_num = problem_set.easy_problem_num
          self.temp = (temp + 1) % self.problem_num
        elif(self.setting == "hard"):
          self.problem_num = problem_set.hard_problem_num
          self.temp = (temp + 1) % self.problem_num   

        self.init_problem()
        

    def init_problem(self):
        self.check_array = []
        new = []
        for i in range(0, 9):
            for j in range(0, 9):
                new.append(False)

            self.check_array.append(new)
            new = []

        
        
        self.sol = []
        self.given_number = []
        new = []
        new_ = []
        for i in range(0, 9):
            for j in range(0, 9):
                new.append(0)
                new_.append(0)

            self.sol.append(new)
            self.given_number.append(new_)
            new = []
            new_ = []

        for i in range(0, 9):
            for j in range(0, 9):
                index = 9 * i + j
                #self.sol[i][j] = int(Problem_100.abc[temp * 81 + index])
                
                if(self.setting == "easy"):
                  self.sol[i][j] = int(problem_set.easy_solution[self.temp * 81 + index])
                  self.given_number[i][j] = int(problem_set.easy_problem[self.temp * 81 + index])
                elif(self.setting == "hard"):
                  self.sol[i][j] = int(problem_set.hard_solution[self.temp * 81 + index])
                  self.given_number[i][j] = int(problem_set.hard_problem[self.temp * 81 + index])

        
        
        for i in range(0, 9):
            for j in range(0, 9):
                if(self.given_number[i][j] != 0):
                    self.update_given_text(i, j, self.given_number[i][j])
                    self.check_array[i][j] = True
        

        #print("init: ", sum(x.count(True) for x in self.check_array))
        
        
    def checker(self, x, y, value):
        self.tk += 1
        self.update_text(x, y, value)
        if self.sol[x - 1][y - 1] == value:
            self.check_array[x - 1][y - 1] = True
            if sum((x.count(True) for x in self.check_array)) == 81:
                self.finished = 1
            return 1
        else:
            return 0
            
    def update_given_text(self, i, j, k):
        self.canvas.update()
        self.canvas.itemconfig(9 * (i - 1) + j, text=k, tags='numbers', fill='black')
        self.check_array[i - 1][j - 1] = True
        self.canvas.update()


    def update_text(self, i, j, k):
        time.sleep(self.DELAY)
        self.canvas.update()
        self.canvas.itemconfig(9 * (i - 1) + j, text=k, tags='numbers', fill='black')
        self.canvas.update()
        self.canvas.itemconfig(83, text=self.tk, tags='numbers', fill='blue')
        self.canvas.update()

    def update_a(self):
        self.canvas.update()
        self.canvas.itemconfig(85, text= round(self.tk / self.problem_num), tags='numbers', fill='blue')

    def is_done(self):
        x0 = y0 = MARGIN + SIDE * 2
        x1 = y1 = MARGIN + SIDE * 7
        self.canvas.create_oval(x0, y0, x1, y1, tags='done', fill='blue', outline='blue')
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y - 30, text='Submitted', tags='done', fill='white', font=('Arial', 32))
        self.canvas.create_text(x, y + 30, text='successfully!', tags='done', fill='white', font=('Arial', 32))

    def already_done(self):
        x0 = y0 = MARGIN + SIDE * 1
        x1 = y1 = MARGIN + SIDE * 9
        self.canvas.create_oval(x0, y0, x1, y1, tags='done', fill='red', outline='red')
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y - 30, text='You already submit', tags='done', fill='white', font=('Arial', 32))
        self.canvas.create_text(x, y + 30, text='the same result.', tags='done', fill='white', font=('Arial', 32))

    def fail(self):
        x0 = y0 = MARGIN + SIDE * 1
        x1 = y1 = MARGIN + SIDE * 8
        self.canvas.create_oval(x0, y0, x1, y1, tags='done', fill='red', outline='red')
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y - 30, text='You fail to', tags='done', fill='white', font=('Arial', 32))
        self.canvas.create_text(x, y + 30, text='solve it !', tags='done', fill='white', font=('Arial', 32))

    def wrong_id_pw(self):
        x0 = y0 = MARGIN + SIDE * 1
        x1 = y1 = MARGIN + SIDE * 8
        self.canvas.create_oval(x0, y0, x1, y1, tags='done', fill='red', outline='red')
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y - 30, text='Wrong user name', tags='done', fill='white', font=('Arial', 32))
        self.canvas.create_text(x, y + 30, text='or password !', tags='done', fill='white', font=('Arial', 32))

    def fail_10min(self):
        x0 = y0 = MARGIN + SIDE * 1
        x1 = y1 = MARGIN + SIDE * 8
        self.canvas.create_oval(x0, y0, x1, y1, tags='done', fill='red', outline='red')
        x = y = MARGIN + 4 * SIDE + SIDE / 2
        self.canvas.create_text(x, y - 30, text='Try to submit', tags='done', fill='white', font=('Arial', 32))
        self.canvas.create_text(x, y + 30, text='in 10 min!', tags='done', fill='white', font=('Arial', 32))

    def submit(self, uid, pw):
        print("Write report~")
        """
        t1 = ''
        urlSudoku = t1 + 'yonsei.ac.kr' + ''
        self.uid = uid
        self.pw = pw
        try:
            url = urlSudoku + ''
            url += 'uid=' + str(uid) + '&pw=' + str(pw) + '&cnt=' + str(self.tk / 100)
            resp = urllib2.urlopen(url)
            contents = resp.read()
        except urllib2.HTTPError as error:
            contents = error.read()

        return contents
        """