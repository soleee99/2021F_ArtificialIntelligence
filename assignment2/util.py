import copy
import hashlib
import matplotlib.pyplot as plt
import random
from collections import deque

WALL = '#'
GHOST = 'G'
POWER = 'P'
ITEM = '.'
BLANK = ' '
USER = 'u'
PUSER = 'U'
SCORE_NORMAL = 10
SCORE_ACTION = -1
SCORE_POWER = 100
SCORE_CATCH = 200
SCORE_DEAD = -500
SCORE_ALIVE = 500
TOTAL_EPISODE = 100
TEST_STEP = 1