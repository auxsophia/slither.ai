'''
Reinforcement learning for slither.io

@author Auxsophia
@license GNU v3
'''
import random
print('Importing pyautogui...')
import pyautogui as pyg
print('Done importing.')

# Get screen size.
print(pyg.size())

def main():
    pyg.moveTo(400, 400, 0)
    pyg.click()
    pyg.PAUSE = 0.1   # Pause after each command

    for COUNTER in range(1000):
        left = random.uniform(0,1)
        right = random.uniform(0,1)
        up = random.uniform(0,1)

        if left > 0.5:
            pyg.keyDown('left')
        else:
            pyg.keyUp('left')

        if right > 0.5:
            pyg.keyDown('right')
        else:
            pyg.keyUp('right')

        if up > 0.5:
            pyg.keyDown('up')
        else:
            pyg.keyUp('up')

        if COUNTER % 100 == 0:
            print(COUNTER)

    print('Done.')

if __name__ == '__main__':
    main()
