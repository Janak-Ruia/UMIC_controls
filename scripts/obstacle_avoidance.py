#! /usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

pub = None

def clbk_laser(msg):
	n = len(msg.ranges)
	ranges = {
		'right': min(msg.ranges[0:n//3]),
		'front': min(msg.ranges[n//3:2*n//3]),
		'left': min(msg.ranges[2*n//3:n]),
	}
	take_action(ranges)
	#rospy.loginfo(ranges)

def take_action(regions):
	msg = Twist()
	linear_x = 0
	angular_z = 0
	state_description = ''

	f= regions['front']
	r = regions['right']
	l = regions['left']
	if f>1:
		state_description = 'case 1 - nothing'
		linear_x = 0.6
		angular_z = 0
	else:
		if r>1:
			state_description = 'right is free'
			angular_z = -0.3
			linear_x = 0.05	


		else:
			state_description = 'moving on the spot'
			angular_z = -0.5
			linear_x = 0
			'''
			if l>1:
				state_description = 'obs in front ,right'	
				angular_z = 0.3
			else:
				state_description='stuck'
				angular_z = 0.5
			'''

	rospy.loginfo(state_description)
	msg.linear.x = linear_x
	msg.angular.z = angular_z
	pub.publish(msg)


def main():
	global pub

	rospy.init_node('reading_laser')
	pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
	sub = rospy.Subscriber('/m2wr/laser/scan', LaserScan, clbk_laser)

	rospy.spin()

if __name__ == '__main__':
	main()