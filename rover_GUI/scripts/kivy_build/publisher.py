#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image as img
from kivy.graphics.texture import Texture
from kivy.clock import Clock




class Nodo(object):
    def __init__(self):
        # Params
        self.image = None
        self.br = CvBridge()
        # Node cycle rate (in Hz).
        self.loop_rate = rospy.Rate(1)

        # Publishers
        self.pub = rospy.Publisher('/imagetimer', Image,queue_size=10)

        # Subscribers
        rospy.Subscriber("video_frame1/image",Image,self.callback)

    def callback(self, msg):
        br=CvBridge()
        rospy.loginfo('Image received...')
        self.frame = self.br.imgmsg_to_cv2(msg)


    def start(self):
        rospy.loginfo("Timing images")
        #rospy.spin()
        while not rospy.is_shutdown():
            rospy.loginfo('publishing image')
            br = CvBridge()
            if self.image is not None:
                self.pub.publish(br.cv2_to_imgmsg(self.image))
            self.loop_rate.sleep()

    class MyApp(App):
        def build(self):
            layout = BoxLayout(orientation='vertical')
            self.image=img()
            layout.add_widget(self.image)
            # layout = BoxLayout(spacing=10)
            btn1 = Button(text='Hello',pos_hint={'centre_x':1,'centre_y':.5}, size_hint=(None,None))
            btn1.bind(on_press=self.loadVideo)

            # layout.add_widget(btn1)
            # self.capture=cv2.VideoCapture(0)
            Clock.schedule_interval(self.loadVideo,1.0/30.0)
            return layout
        
        def loadVideo(self,*args):
            # ret ,frame=self.capture.read()
            image_frame=self.frame
            buffer=cv2.flip(self.frame,0).tostring()
            texture=Texture.create(size=(self.frame.shape[1],self.frame.shape[0]), colorfmt="bgr")
            texture.blit_buffer(buffer,colorfmt="bgr",bufferfmt='ubyte')
            self.image.texture=texture


if __name__ == '__main__':
    rospy.init_node("imagetimer111", anonymous=True)
    my_node = Nodo()
    my_node.MyApp().run()
    my_node.start()
    # rospy.spin()