##  cliff detectioin code for testing 

import pycozmo

def on_robot_state(cli, msg):
    # Get the raw cliff sensor data
    cliff_detected = msg.cliff_sensor_raw < 100  # Adjust the threshold as needed
    
    if cliff_detected:
        print("Cliff detected! Stopping and moving back.")
        
        # Stop the robot when a cliff is detected
        cli.stop_all_motors()
        
        # Reverse by 5 cm (approx. adjust duration based on speed)
        cli.drive_wheels(lwheel_speed=-50, rwheel_speed=-50, duration=0.5)  # Move back for 0.5 seconds
        
        # Stop after reversing
        cli.stop_all_motors()

with pycozmo.connect() as cli:
    cli.add_handler(pycozmo.event.EvtRobotStateUpdated, on_robot_state)
    cli.start()
    cli.wait_for_robot()
    
    # Drive forward until cliff is detected
    cli.drive_wheels(lwheel_speed=50, rwheel_speed=50, duration=5)
