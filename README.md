# UMIC_controls

Clone this repo in a ws, then catkin_make. Then in terminal, type
roslaunch hexbot_moveit_config_3 demo.launch

This will launch the rviz  sim of gripper. In another terminal, type 
rosrun hexbot moveit_laser_try.py

Now, follow instructions on the terminal to see the robot moving. 

PS: if u don't want to see the animation of every motion again and again, uncheck the loop-animation option under Planned Path tab in rviz.
