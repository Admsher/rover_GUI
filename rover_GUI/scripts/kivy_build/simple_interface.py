#!/usr/bin/env python3.8
import rospy
from kivy.lang import Builder
from kivy.app import App
from std_msgs.msg import Int8
from sensor_msgs.msg import Image as img
from geometry_msgs.msg import Twist
import cv2
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics.texture import Texture
from cv_bridge import CvBridge
import os
from kivy.clock import Clock

os.system("gnome-terminal -- bash -c 'source ~/catkin_ws/devel/setup.bash;rosrun urc2022 videofeed2 2'&")
os.system("gnome-terminal -- bash -c 'source ~/catkin_ws/devel/setup.bash;rosrun urc2022 videofeed1 4'&")

# os.system("gnome-terminal -- bash -c 'ssh ishangokhale@192.168.240.245'")


def callback(msg):
    global frame
    # rospy.loginfo("recieving...")
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg)

def callback2(msg):
    global frame2
    # rospy.loginfo("recieving...")
    bridge = CvBridge()
    frame2 = bridge.imgmsg_to_cv2(msg)



class WindowManager(ScreenManager):
    pass


class Menu(Screen):
    pass


class WorkingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.schedule = None
        self.i=0
        self.p=0

    def on_enter(self, *args):
        self.schedule = Clock.schedule_interval(self.load_video, 1.0 / 30.0)

    def load_video(self, *args):
        buffer = cv2.flip(frame, 0).tobytes()
        self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        self.texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.img_frame=frame2
        buffer2 = cv2.flip(frame2, 0).tobytes()
        self.texture2 = Texture.create(size=(frame2.shape[1], frame2.shape[0]), colorfmt='bgr')
        self.texture2.blit_buffer(buffer2, colorfmt='bgr', bufferfmt='ubyte')

        if self.p%2==0:
            self.ids.video.texture = self.texture
            self.ids.camera.text="cam_1"
        else:
            self.ids.video.texture = self.texture2
            self.ids.camera.text="cam_2"
        # self.ids.video1.texture = self.texture2  # id video is defined in kv
        
    def capture(self,*args):
        image_name="take_"+str(self.i)+".png"
        cv2.imwrite(image_name,self.img_frame)
        self.i+=1

    def ssh(self,*args):
        # os.system("ssh ishangokhale@192.168.240.245 &roscore")
        pass
    
    def switch(self):
        self.p+=1

    def function(self,*args):
        self.ids.video1.texture = None
        if self.schedule:       
            self.schedule.cancel()
            self.schedule = None

    def on_leave(self, *args):
        self.function()


class something(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.schedule=None
        self.current_i = 0
        self.current_j = 0
        self.current_k = 0
    
    # def on_enter(self):

    # def on_leave(self, *args):
    #     self.function()
    def update(self):
        self.schedule=Clock.schedule_interval(self.actuators,3)

    def updatee(self):
        self.schedule=Clock.schedule_interval(self.motor,3)

    def driver(self):
        self.schedule=Clock.schedule_interval(self.dv,3)

    # def drive_test(self):
    #     if self.current_k==0:
    #         self.ids.d1.color=(0,1,0,1)
    #     elif self.current_k==1:
    #         self.ids.d2.color=(0,1,0,1)
    #     elif self.current_k==2:
    #         self.ids.d3.color=(0,1,0,1) 
    #     else:
    #         self.schedule.cancel()
    #         self.current_k=0
    #         self.schedule = None

    #     self.current_k+=1
        # velocity=Twist()
        # time_period = 0.3
        # # fwd
        # velocity.linear.x=0.14
        # velocity.angular.z=0

        # for i in range(10):
        #     pub_drive.publish(velocity)
        #     rospy.sleep(time_period)
        # # back
        # velocity.linear.x=-0.14
        # velocity.angular.z=0
        
        # for i in range(10):
        #     pub_drive.publish(velocity)
        #     rospy.sleep(time_period)
        # # CW
        # velocity.linear.x=0
        # velocity.angular.z=0.14

        # for i in range(10):
        #     pub_drive.publish(velocity)
        #     rospy.sleep(time_period)

        # # CCW
        # velocity.linear.x=0
        # velocity.angular.z=-0.14

        # for i in range(10):
        #     pub_drive.publish(velocity)
        #     rospy.sleep(time_period)


    
    def manual_drive(self):
        os.system("gnome-terminal -- bash -c 'source ~/catkin_ws/devel/setup.bash;roslaunch urc2022 manual_control.launch'&")

    def roscore(self):
        pass

    # def update1(self):
    #     self.schedule=Clock.schedule_interval(self.other_motors,2)
        
    # def other_motors(self):
    #     # self.ids.a1.text=str(self.current_i)
    #     if self.current_i==0:
    #         self.ids.m1.color=(0,1,0,1)
    #     elif self.current_i==1:
    #         self.ids.m2.color=(0,1,0,1)
    #     elif self.current_i==2:
    #         self.ids.m3.color=(0,1,0,1)
    #     elif self.current_i==3:
    #         self.ids.m4.color=(0,1,0,1)  
    #     else:
    #         self.schedule.cancel()
    #         self.current_i=0
    #         self.schedule = None

    #     self.current_i+=1 
        # self.ids.m1.text=str(self.current_i)
   
        # time_period = 0.3

        # for i in range(10):#othermotor_topic
        #     pub_arm.publish(5)#base
        #     rospy.sleep(time_period)


        # for i in range(10):
        #     pub_arm.publish(-5)
        #     rospy.sleep(time_period)
      


        # for i in range(10):
        #     pub_arm.publish(-7)#bevel CCW
        #     rospy.sleep(time_period)
        

        # for i in range(10):
        #     pub_arm.publish(7)#bevel CW
        #     rospy.sleep(time_period)

        

        # for i in range(10):
        #     pub_arm.publish(8)#bevel pitch up
        #     rospy.sleep(time_period)
        
        # for i in range(10):
        #     pub_arm.publish(-8)#bevel pitch down
        #     rospy.sleep(time_period)

        
        # for i in range(10):
        #     pub_arm.publish(4)#gripper open
        #     rospy.sleep(time_period)
        
        # for i in range(10):
        #     pub_arm.publish(-4)#gripper open
        #     rospy.sleep(time_period)
        
    def dv(self,*args):
        # self.ids.m1.text=str(self.current_i)
        if self.current_k==0:
            self.ids.d1.color=(0,1,0,1)
        elif self.current_k==1:
            self.ids.d3.color=(0,1,0,1)
        # elif self.current_k==2:
        #     self.ids.d3.color=(0,1,0,1)  
        else:
            self.current_k=0
            self.schedule.cancel()
            self.schedule = None
          


        self.current_k+=1
# # actuators

    def motor(self,*args):
        # self.ids.m1.text=str(self.current_i)
        if self.current_j==0:
            self.ids.m1.color=(0,1,0,1)
        elif self.current_j==1:
            self.ids.m2.color=(0,1,0,1)
        elif self.current_j==2:
            self.ids.m3.color=(0,1,0,1)
        elif self.current_j==3:
            self.ids.m4.color=(0,1,0,1)  
        else:
            self.current_j=0
            self.schedule.cancel()
            self.schedule = None
          


        self.current_j+=1


    def actuators(self,*args):
        # self.ids.m1.text=str(self.current_i)
        if self.current_i==0:
            self.ids.a1.color=(0,1,0,1)
        elif self.current_i==1:
            self.ids.a2.color=(0,1,0,1)
        elif self.current_i==2:
            self.ids.a3.color=(0,1,0,1)
        elif self.current_i==3:
            self.ids.a4.color=(0,1,0,1)  
        else:
            self.schedule.cancel()
            self.current_i=0
            self.schedule = None

        self.current_i+=1          
        # time_period=0.3
        # for i in range(10):
        #     pub_act.publish(7)#$ 4inch retract
        #     rospy.sleep(time_period)
        #     # self.ids.m1.color=(0,1,0,1)

        # for i in range(10):
        #     pub_act.publish(-7)#$ 4inch retract
        #     rospy.sleep(time_period)

        # for i in range(10):
        #     pub_act.publish(8)#$ 6inch retract
        #     rospy.sleep(time_period)

        # for i in range(10):
        #     pub_act.publish(-8)#$ 6inch retract
        #     rospy.sleep(time_period)

        # for i in range(10):
        #     pub_act.publish(5)#$ stepper on
        #     rospy.sleep(time_period) 

        # for i in range(10):
        #     pub_act.publish(5)#$ stepper on
        #     rospy.sleep(time_period) 

        # for i in range(10):
        #     pub_act.publish(3)#$ servo
        #     rospy.sleep(time_period) 

        # for i in range(10):
        #     pub_act.publish(4)#$ other servo
        #     rospy.sleep(time_period) 
    

    def arm(self):
        os.system("gnome-terminal -- bash -c 'sudo chmod a+rw /dev/ttyACM*'")
        # msg=5
        # pub_arm.publish(msg)
        


class MyMainApp(App):
    def build(self):
        return Builder.load_file("/home/ninaad/catkin_ws/src/rover_GUI/scripts/kivy_build/my.kv")
    

if __name__=='__main__':
    rospy.init_node('rover_ui')
    pub_drive=rospy.Publisher("/cmd_vel",Twist,queue_size=1)
    pub_arm=rospy.Publisher("/other_motors",Int8,queue_size=1)
    pub_act=rospy.Publisher("/actuators",Int8,queue_size=1)
    sub = rospy.Subscriber('video_frame1/image',img, callback)   
    sub2 = rospy.Subscriber('video_frame2/image',img, callback2)   

    MyMainApp().run()
    