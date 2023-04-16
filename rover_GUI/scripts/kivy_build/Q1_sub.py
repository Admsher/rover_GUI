#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(msg):
    # rospy.loginfo(msg.data)
    print(msg.data)

if __name__=='__main__':
    rospy.init_node('topic_subscriber')

    sub = rospy.Subscriber('/new', String, callback)
  
    rospy.spin()