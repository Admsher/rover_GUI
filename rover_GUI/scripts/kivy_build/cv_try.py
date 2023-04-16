#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image as img
from kivy.app import App
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton

from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
from cv_bridge import CvBridge
import cv2

os.system("gnome-terminal -- bash -c 'source ~/catkin_ws/devel/setup.bash;rosrun urc2022 videofeed1 0'&")

def callback(msg):
    global frame

    # rospy.loginfo("recieving...")
    bridge = CvBridge()
    frame = bridge.imgmsg_to_cv2(msg)

class MyApp(App):
    def build(self):
        self.v=0
        layout = BoxLayout(orientation='vertical')
        self.image=Image()
        layout.add_widget(self.image)
        # layout = BoxLayout(spacing=10)
        btn1 = Button(text='camfeed',pos_hint={'centre_x':1,'centre_y':.5}, size_hint=(None,None))
        btn1.bind(on_press=self.cam_state)

        btn2 = Button(text='off',pos_hint={'centre_x':1,'centre_y':.5}, size_hint=(None,None))
        btn2.bind(on_press=self.cam_off)

        layout.add_widget(btn1)
        layout.add_widget(btn2)

        # self.capture=cv2.VideoCapture(0)
        # Clock.schedule_interval(self.loadVideo,1.0/60.0)
        return layout
    
    def loadVideo(self,*args):
        # ret ,frame=self.capture.read()
        # self.image_frame=frame
        buffer=cv2.flip(frame,0).tostring()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer,colorfmt='bgr',bufferfmt='ubyte')
        self.image.texture=texture

    def cam_state(self,*args):
        Clock.schedule_interval(self.loadVideo,1.0/60.0)

    def cam_off(self,*args):
        Clock.unschedule(self.loadVideo)


            

        




if __name__ == "__main__":
    rospy.init_node('seeing_me')
    sub = rospy.Subscriber('video_frame1/image',img, callback)
    MyApp().run()
    rospy.spin()