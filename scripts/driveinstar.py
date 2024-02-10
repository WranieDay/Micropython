from util.drivecontrol import Controller

mycontroller = Controller()
mycontroller.start()

state = 0
turns_made = 0

while True:
    if state == 0:
        mycontroller.drive_forwards()
        if mycontroller.left_odom.get_count()>=2000 and mycontroller.right_odom.get_count() >=2000:
            state = 1
            if turns_made %2 == 1:
                mycontroller.left_odom.reset_count()
            else:
                mycontroller.right_odom.reset_count()


    elif state == 1:
        mycontroller.custom_left_turn(108)

        turns_made += 1
        if turns_made > 9:
            state = 3
        else:
            state = 0

    
    elif state == 2:
        mycontroller.custom_right_turn(328)

        turns_made =+ 1
        if turns_made > 9:
            state =3
        else:
            state = 0

    if state == 3:
        mycontroller.stop()