from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    if state == 0:
        mycontroller.drive_forwards()
        if mycontroller.left_odom.get_count()>=1000 and mycontroller.right_odom.get_count() >=1000:
            state = 1
            mycontroller.left_odom.reset_count()
            mycontroller.right_odom.reset_count()


    elif state == 1:
        mycontroller.raft.led_on()

        mycontroller.custom_left_turn(45)

        turns_made += 1
        if turns_made > 7:
            state = 2
        else:
            state = 0
        
    elif state == 2:
        mycontroller.stop()