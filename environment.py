import RPi.GPIO as gpio
from ai import Dqn
import time

gpio.setmode(gpio.BOARD)

gpio.setup(11,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(12,gpio.OUT)

gpio.output(11,True)
gpio.output(12,True)
gpio.output(13,False)
gpio.output(15,False)

trig=31
echo=33
trig_left=37
echo_left=36
trig_right=40
echo_right=35
last_reward=0

#straight
def action1():

   gpio.output(11,True)
   gpio.output(12,True)
   gpio.output(13,False)
   gpio.output(15,False)
   time.sleep(1)
#right
def action2():
   gpio.output(11,True)
   gpio.output(13,False)
   gpio.output(15,True)
   gpio.output(12,False)
   time.sleep(1)
#left
def action3():
   gpio.output(11,False)
   gpio.output(13,True)
   gpio.output(15,False)
   gpio.output(12,True)
   time.sleep(1)

gpio.setup(trig,gpio.OUT)
gpio.output(trig,0)
gpio.setup(echo,gpio.IN)

gpio.setup(trig_left,gpio.OUT)
gpio.output(trig_left,0)
gpio.setup(echo_left,gpio.IN)

gpio.setup(trig_right,gpio.OUT)
gpio.output(trig_right,0)
gpio.setup(echo_right,gpio.IN)

brain=Dqn(3,3,0.9)
count=0

def act(last_reward,last_signal):

   gpio.output(trig,1)
   time.sleep(0.00001)
   gpio.output(trig,0)

   while gpio.input(echo)==0:
        pass
   start=time.time()
   while gpio.input(echo)==1:
        pass
   stop=time.time()
   dist_straight=((stop-start)*17000)-2
   #        print dist_straight

   while(dist_straight<15):
        gpio.output(11,False)
        gpio.output(13,False)
        gpio.output(15,False)
        gpio.output(12,False)
        time.sleep(0.1)
        gpio.output(trig,1)
        time.sleep(0.00001)
        gpio.output(trig,0)
#        time.sleep(0.1)
        while gpio.input(echo)==0:
             pass
        start=time.time()
        while gpio.input(echo)==1:
             pass
        stop=time.time()
        dist_straight=((stop-start)*17000)-2

   gpio.output(trig_left,1)
   time.sleep(0.00001)
   gpio.output(trig_left,0)

   while gpio.input(echo_left)==0:
        pass
   start1=time.time()
   while gpio.input(echo_left)==1:
        pass
   stop1=time.time()
   dist_left=(stop1-start1)*17000
    #       print dist_left

   while(dist_left<15):
        gpio.output(11,False)
        gpio.output(13,False)
        gpio.output(15,False)
        gpio.output(12,False)
        time.sleep(0.1)
        gpio.output(trig_left,1)
        time.sleep(0.00001)
        gpio.output(trig_left,0)
#        time.sleep(0.1)
        while gpio.input(echo_left)==0:
             pass
        start=time.time()
        while gpio.input(echo_left)==1:
             pass
        stop=time.time()
        dist_left=((stop-start)*17000)-2

   gpio.output(trig_right,1)
   time.sleep(0.00001)
   gpio.output(trig_right,0)
   while gpio.input(echo_right)==0:
        pass
   start2=time.time()
   while gpio.input(echo_right)==1:
        pass
   stop2=time.time()

   dist_right=(stop2-start2)*17000
    #      print dist_right

   while(dist_right<15):
        gpio.output(11,False)
        gpio.output(13,False)
        gpio.output(15,False)
        gpio.output(12,False)
        time.sleep(0.1)
        gpio.output(trig_right,1)
        time.sleep(0.00001)
        gpio.output(trig_right,0)
#        time.sleep(0.1)
        while gpio.input(echo_right)==0:
             pass
        start=time.time()
        while gpio.input(echo_right)==1:
             pass
        stop=time.time()
        dist_right=((stop-start)*17000)-2


   last_signal=[dist_straight,dist_left,dist_right]

   action=brain.update(last_reward,last_signal)
   print(last_reward)
   print(last_signal)
   print(action)

   if(action==0):
     action1()
   if(action==1):
     action3()
   if(action==2):
     action2()
   last_reward = 0

brain.load()
try:
   time.sleep(0.1)
   while(True):
        time.sleep(0.1)
        gpio.output(trig,1)
        time.sleep(0.00001)
        gpio.output(trig,0)

        while gpio.input(echo)==0:
             pass
        start=time.time()

        while gpio.input(echo)==1:
             pass
        stop=time.time()
        dist_straight=((stop-start)*17000)-2
#        print dist_straight
        time.sleep(0.1)
        gpio.output(trig_left,1)
        time.sleep(0.00001)
        gpio.output(trig_left,0)

        while gpio.input(echo_left)==0:
             pass
        start1=time.time()
        while gpio.input(echo_left)==1:
             pass
        stop1=time.time()
        dist_left=(stop1-start1)*17000
 #       print dist_left
        time.sleep(0.1)
        gpio.output(trig_right,1)
        time.sleep(0.00001)
        gpio.output(trig_right,0)

        while gpio.input(echo_right)==0:
             pass
        start2=time.time()
        while gpio.input(echo_right)==1:
             pass
        stop2=time.time()

        dist_right=(stop2-start2)*17000

        last_signal=[dist_straight,dist_left,dist_right]
        action=brain.update(last_reward,last_signal)

        print(action)
        if(action==0):
          action1()
        if(action==1):
          action3()
        if(action==2):
          action2()


        if(dist_straight<30):
          if(action==0):
            last_reward=-1

        act(last_reward,last_signal)
        c=max(last_signal)

        if(c==dist_left):
          if(action==1):
            last_reward=1
          else:
              last_reward=-0.5

        act(last_reward,last_signal)

        if(c==dist_right):
          if(action==2):
            last_reward=1
          else:
              last_reward=-0.5

        act(last_reward,last_signal)

        if(c==dist_straight):
          if(action==0):
            last_reward=1
          else:
              last_reward=-0.5

        act(last_reward,last_signal)


        if(dist_left<30):
          if(action==1):
            last_reward=-1
          elif(action==0):
              last_reward=-1

        act(last_reward,last_signal)


        if(dist_right<30):
          if(action==2):
            last_reward=-1
          elif(action==0):
              last_reward=-1

        act(last_reward,last_signal)

        if(dist_left<40):
          last_reward=-0.2
        elif(dist_right<40):
            last_reward=-0.2

        act(last_reward,last_signal)
        print("saving brain...")

        brain.save()
except KeyboardInterrupt:
      pass



print("saving brain...")
time.sleep(2)
brain.save()
print(count)
gpio.cleanup()
