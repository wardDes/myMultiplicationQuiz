import random as rand, time
from datetime import datetime, timedelta

corr = 0
tries = 0
questnum = 0
while True:
    for i in range(10):
        num1 = rand.randint(0,9)
        num2 = rand.randint(0,9)
        stopgap = timedelta(seconds=8)
        stoptime = datetime.now() + stopgap
        questnum += 1
        for a in range(3):
            print('%s# %s x %s = ' % (questnum, num1, num2))
            answer = input()
            if datetime.now() > stoptime:
                print('Out of time')
                tries = 0
                break
            if answer == str(num1* num2):
              print('Correct!')
              corr += 1
              time.sleep(1)
              break
            else:
              tries += 1
              if tries != 3:
                  print('Incorrect!')
              elif tries == 3:
                  print('Incorrect!')
                  print('Out of tries')
                  tries = 0
                  break
              else:
                  continue
    break
print('You got %s out of %s right.' % (corr, 10))
