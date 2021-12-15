from util import *

class Ghost:
    def __init__(self, y=0, x=0):
        self.y = y
        self.x = x

    def random_cand(self, state):
        cand_pos = []
        if state[self.y - 1][self.x] != WALL:
            cand_pos.append((self.y - 1, self.x))
        if state[self.y][self.x - 1] != WALL:
            cand_pos.append((self.y, self.x - 1))
        if state[self.y][self.x + 1] != WALL:
            cand_pos.append((self.y, self.x + 1))
        if state[self.y + 1][self.x] != WALL:
            cand_pos.append((self.y + 1, self.x))
        return cand_pos
    
    def follow_cand(self, state):
        cand_pos = []
        top = self.bfs(state, self.y - 1, self.x)
        left = self.bfs(state, self.y, self.x - 1)
        right = self.bfs(state, self.y, self.x + 1)
        bottom = self.bfs(state, self.y + 1, self.x)
        if top <= left and top <= right and top <= bottom:
            cand_pos.append((self.y - 1, self.x))
        elif left <= top and left <= right and left <= bottom:
            cand_pos.append((self.y, self.x - 1))
        elif right <= top and right <= left and right <= bottom:
            cand_pos.append((self.y, self.x + 1))
        else:
            cand_pos.append((self.y + 1, self.x))
        return cand_pos

    def next_pos(self, state):
        if self.bfs(state, self.y, self.x) < 4:
            cand_pos = self.follow_cand(state)
        else:
            cand_pos = self.random_cand(state)
        return random.choice(cand_pos)

    def bfs(self, state, y, x):
        if state[y][x] == WALL:
            return 99999
        visit = set()
        q = deque([(y, x, 0)])
        while len(q) > 0:
            y, x, size = q.popleft()
            if (y, x) in visit:
                continue
            visit.add((y, x))
            if state[y][x] in [USER, PUSER]:
                return size
            if state[y - 1][x] != WALL:
                q.append((y - 1, x, size + 1))
            if state[y][x - 1] != WALL:
                q.append((y, x - 1, size + 1))
            if state[y][x + 1] != WALL:
                q.append((y, x + 1, size + 1))
            if state[y + 1][x] != WALL:
                q.append((y + 1, x, size + 1))
        return 99999