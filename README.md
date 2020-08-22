# UMIC_controls

Clone this repo in a ws, then catkin_make. Then in terminal, type
roslaunch hexbot_moveit_config_4 demo.launch

This will launch the rviz  sim of gripper. Wait for the loading to complete. In another terminal, type 
rosrun hexbot moveit_pose.py

Now, follow instructions on the terminal to see the robot moving. i've written list of poses on slack channel under today's (22nd) thread. just type the pose and hit enter. 

PS: if u don't want to see the animation of every motion again and again, uncheck the loop-animation option under Planned Path tab in rviz.

