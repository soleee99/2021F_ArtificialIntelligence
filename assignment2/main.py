from world import *

user = User(move='v2')

level = 0
world = World(user=user, level=level)

# Currently, total episode is 100, test step is 1
print(f"total episode: {TOTAL_EPISODE}, test step: {TEST_STEP}")    
# train
score_list = []
for episode in range(TOTAL_EPISODE):
    # training TOTAL_EPISODE number of times
    world.reset()
    while True:
        done = world.move(test=False)
        if done:
            break
    print('EPI : %d / %d' % (episode + 1, TOTAL_EPISODE), end='\r', flush=True)
    
    # testing after every step
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
