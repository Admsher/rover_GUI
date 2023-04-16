#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


if __name__=='__main__':
    rospy.init_node("Q1")
    pub=rospy.Publisher("/new",String,queue_size=10)
    rate=rospy.Rate(4)
    sr_no=0
    hello_str = "hello world"

    while not rospy.is_shutdown():
        pub.publish(str(sr_no)+".) "+hello_str)
        sr_no+=1
        rate.sleep()