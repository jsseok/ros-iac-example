import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from rclpy.qos import qos_profile_sensor_data
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError


class USBcam(Node):
    def __init__(self):
        super().__init__('usb_cam')
        self.publisher_rgb = self.create_publisher(Image, 'rgb_image', 10)
        timer_period = 0.1 # About 10 frames per sec. It is not bad for driving a Turtlebot3.
        self.timer = self.create_timer(timer_period, self.publish_rgb_msg)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.bridge = CvBridge()


    def publish_rgb_msg(self):
        # Create a messge instance
        msg_rgb = Image()

        if self.cap.isOpened():
            # Image read from usb_cam
            ret, frame = self.cap.read()

            if ret:
                # Sending message
                # Using ros bridge is faster than handling byte processing manually with toByte() function. 
                self.publisher_rgb.publish(self.bridge.cv2_to_imgmsg(frame, "bgr8"))
                # self.get_logger().info('Publishing images')
            
            else:
                self.get_logger().info('Error: Camera is ready but something happend')
        else:
            self.get_logger().info('Error: Camera is not ready')
        
        #cv2.waitKey(100)
    
def main(args=None):
    rclpy.init(args=args)
    node = USBcam()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.cap.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
