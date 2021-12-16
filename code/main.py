from world import *
import random
random.seed(900)
user = User(move='v3')

level = 0
world = World(user=user, level=level)
TEST_STEP = 101
# train
score_list = []
for episode in range(TOTAL_EPISODE):
    world.reset()
    while True:
        done = world.move(test=False)
        if done:
            break
    print('EPI : %d / %d' % (episode + 1, TOTAL_EPISODE), end='\r', flush=True)
    # test
    if (episode + 1) % TEST_STEP == 0:
        world.reset()
        while True:
            done = world.move(test=True)
            if done:
                break
        score_list.append(world.total_score)

print()
plt.bar(range(len(score_list)), score_list, color='blue')
plt.show()

# test
world.reset()
while True:
    world.show()
    input('...')
    done = world.move(test=True)
    if done:
        break
print('========== Finish ==========')
print('Total score : %d' % world.total_score)
print('Total time : %d' % world.total_time)
