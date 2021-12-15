from ghost import *
from user import *
from util import *

class World:
    def __init__(self, user=None, level=0):
        self.user = user
        self.level = level
        self.reset()

    def reset(self):
        self.total_score = 0
        self.total_time = 0
        self.powered = 0

        if self.level == 0:
            self.max_y = 7
            self.max_x = 7
            self.board = [
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL], # center
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL]
            ]

            # create user
            self.user.y = 1
            self.user.x = 3
            self.board[1][3] = USER

            # create ghost
            self.ghost = []
            self.ghost.append(Ghost(1, 1))
            self.board[1][1] = GHOST

        elif self.level == 1:
            self.max_y = 11
            self.max_x = 11
            self.board = [
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL], # center
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
            ]

            # create user
            self.user.y = 4
            self.user.x = 4
            self.board[4][4] = USER

            # create ghost
            self.ghost = []
            self.ghost.append(Ghost(7, 7))
            self.board[7][7] = GHOST
        
        elif self.level == 2:
            self.max_y = 19
            self.max_x = 21
            self.board = [
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL], # center
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
            ]

            # create user
            self.user.y = 17
            self.user.x = 1
            self.board[17][1] = USER

            # create ghost
            self.ghost = []
            self.ghost.append(Ghost(1, 16))
            self.board[1][16] = GHOST
            self.ghost.append(Ghost(13, 13))
            self.board[13][13] = GHOST

            # create power
            self.board[9][1] = POWER
            self.board[9][19] = POWER
        
        elif self.level == 3:
            self.max_y = 19
            self.max_x = 21
            self.board = [
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL], # center
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
            ]

            # create user
            self.user.y = 17
            self.user.x = 1
            self.board[17][1] = USER

            # create ghost
            self.ghost = []
            self.ghost.append(Ghost(1, 1))
            self.board[1][1] = GHOST
            self.ghost.append(Ghost(1, 19))
            self.board[1][19] = GHOST

            # create power
            self.board[9][1] = POWER
        
        elif self.level == 4:
            self.max_y = 19
            self.max_x = 21
            self.board = [
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL], # center
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, WALL, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, WALL, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL, WALL, WALL, ITEM, WALL],
                [WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, ITEM, WALL],
                [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
            ]

            # create user
            self.user.y = 7
            self.user.x = 10
            self.board[7][10] = USER

            # create ghost
            self.ghost = []
            self.ghost.append(Ghost(17, 1))
            self.board[17][1] = GHOST
            self.ghost.append(Ghost(17, 19))
            self.board[17][19] = GHOST

            # create power
            self.board[9][19] = POWER

        # set scores of each cell
        self.score = []
        for y in range(self.max_y):
            temp = []
            for x in range(self.max_x):
                if self.board[y][x] == ITEM:
                    temp.append(SCORE_NORMAL)
                elif self.board[y][x] == POWER:
                    temp.append(SCORE_POWER)
                else:
                    temp.append(0)
            self.score.append(temp)

    def show(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                if self.board[y][x] == BLANK and self.score[y][x] == SCORE_NORMAL:
                    ch = '.'
                else:
                    ch = self.board[y][x]
                print(ch, end='')
            print()
        print('| Score : %d | Time : %d | Ghost : %d |' % (self.total_score, self.total_time, len(self.ghost)))

    def move(self, test=False):
        # first, grab some variables...
        before_board = copy.deepcopy(self.board)
        y, x = self.user.y, self.user.x
        score = self.total_score

        # then, move the user! returns True if finished
        done = self.move_user(test=test)

        # check : eat all items?
        eat_all = True
        for i in range(self.max_y):
            for j in range(self.max_x):
                if self.score[i][j] > 0:
                    eat_all = False
                    break
        if not done:
            # if the game is not finished after the user takes their turn, then move the ghost
            # returns True is it eats the user
            done = self.move_ghost()
        next_y, next_x = self.user.y, self.user.x
        next_score = self.total_score

        if y - 1 == next_y:
            action = 0
        elif x - 1 == next_x:
            action = 1
        elif x + 1 == next_x:
            action = 2
        else:
            action = 3

        if done:
            # user is dead
            self.total_score += SCORE_DEAD
            self.user.update(before_board, action, self.board, SCORE_DEAD)
            return True
        if eat_all:
            # success!
            self.total_score += SCORE_ALIVE
            self.user.update(before_board, action, self.board, SCORE_ALIVE)
            return True
        if self.total_time > self.max_y * self.max_x * 10:
            # timeout
            self.total_score += SCORE_DEAD
            self.user.update(before_board, action, self.board, SCORE_DEAD)
            return True
        self.user.update(before_board, action, self.board, next_score - score)
        if self.powered > 0:
            self.powered -= 1
        self.total_time += 1
        return False

    def move_user(self, test=False):
        # returns the next position depending on the move (v1, v2, v3)
        next_y, next_x = self.user.next_pos(self.board, test=test)  
        if self.board[next_y][next_x] == POWER:
            self.powered = 11
        if self.board[next_y][next_x] == GHOST:
            if self.powered > 0:
                # if the ghost is powered, it can remove the ghost in the (next_y, next_x) position.
                self.total_score += SCORE_CATCH
                self.remove_ghost(next_y, next_x)
            else:
                # if not powered, it returns true, meaning that the game has ended.
                self.board[self.user.y][self.user.x] = BLANK
                self.user.y = next_y
                self.user.x = next_x
                return True

        # score of that board (R) and the score from the action is added tot he total score
        self.total_score += self.score[next_y][next_x] + SCORE_ACTION
        self.score[next_y][next_x] = 0
        self.board[self.user.y][self.user.x] = BLANK
        self.board[next_y][next_x] = PUSER if self.powered > 0 else USER
        self.user.y = next_y
        self.user.x = next_x
        return False

    def move_ghost(self):
        dead = []
        for i in range(len(self.ghost)):
            next_y, next_x = self.ghost[i].next_pos(self.board)
            if self.board[next_y][next_x] in [USER, PUSER]:
                if self.powered > 0:
                    dead.append(i)
                    self.total_score += SCORE_CATCH
                    self.board[self.ghost[i].y][self.ghost[i].x] = BLANK
                    continue
                else:
                    return True
            self.board[self.ghost[i].y][self.ghost[i].x] = BLANK
            if self.score[self.ghost[i].y][self.ghost[i].x] == SCORE_NORMAL:
                self.board[self.ghost[i].y][self.ghost[i].x] = ITEM
            elif self.score[self.ghost[i].y][self.ghost[i].x] == SCORE_POWER:
                self.board[self.ghost[i].y][self.ghost[i].x] = POWER
            self.board[next_y][next_x] = GHOST
            self.ghost[i].y = next_y
            self.ghost[i].x = next_x

        # remove dead ghosts
        temp = []
        for i in range(len(self.ghost)):
            if i in dead:
                continue
            temp.append(self.ghost[i])
        self.ghost = temp
        return False

    def remove_ghost(self, y, x):
        dead = []
        for i in range(len(self.ghost)):
            if self.ghost[i].y == y and self.ghost[i].x == x:
                dead.append(i)
        temp = []
        for i in range(len(self.ghost)):
            if i in dead:
                continue
            temp.append(self.ghost[i])
        self.ghost = temp