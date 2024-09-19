import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CompressedImage
from rclpy.qos import QoSProfile, QoSReliabilityPolicy
import numpy as np
import cv2
import time
from cv_bridge import CvBridge, CvBridgeError


class USBcam(Node):
    def __init__(self):
        super().__init__('usb_cam')
        
        qos_profile = QoSProfile(depth=1)
        qos_profile.reliability = QoSReliabilityPolicy.RELIABLE

        self.publisher_rgb = self.create_publisher(CompressedImage, 'rgb_image', qos_profile)
        timer_period = 0.1 # About 10 frames per sec. It is not bad for driving a Turtlebot3.
        self.timer = self.create_timer(timer_period, self.publish_rgb_msg)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        self.cap.set(cv2.CAP_PROP_FPS, 10)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # 카메라 버퍼 크기 감소

        self.bridge = CvBridge()

        self.last_time = time.time()
        self.fps = 0.0

    def publish_rgb_msg(self):
        current_time = time.time()
        delta_time = current_time - self.last_time
        self.last_time = current_time

        if delta_time > 0:
            self.fps = 1.0 / delta_time

        self.get_logger().info(f"FPS: {self.fps:.2f}")

        if self.cap.isOpened():
            _, frame = self.cap.read()

            encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]
            ret, encimg = cv2.imencode('.jpg', frame, encode_param)
            if ret:
                msg_rgb = CompressedImage()
                msg_rgb.header.stamp = self.get_clock().now().to_msg()
                msg_rgb.format = "jpeg"
                msg_rgb.data = encimg.tobytes()
                self.publisher_rgb.publish(msg_rgb)

                del encimg
                del frame
            else:
                self.get_logger().info('Error: Camera is ready but something happend')
        else:
            self.get_logger().info('Error: Camera is not ready')

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
