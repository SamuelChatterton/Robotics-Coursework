import cozmo
from cozmo.util import degrees
import time

def cozmo_program(robot: cozmo.robot.Robot):
    
    while True:
        robot.drive_wheels(50, 50,duration=2.0) #Move forward for 2 seconds
        robot.turn_in_place(degrees(90)).wait_for_completed() #Turn 90 degrees left
        robot.drive_wheels(50, 50,duration=3.0) #Move forward for 3 seconds

        #Check for cliff
        if robot.is_cliff_detected:
            print("Cliff detected! Reversing and turning right.")
            robot.drive_wheels(-50, -50, duration=2.0)  #Reverse for 2 seconds
            robot.turn_in_place(degrees(-90)).wait_for_completed()  #Turn 90 degrees right
            continue  #Repeat from start of a while loop
        else:
            print("No cliff detected. going straight")
            continue


#Start program
cozmo.run_program(cozmo_program)
