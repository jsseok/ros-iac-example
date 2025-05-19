import rclpy
import os
import cv2

from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from rclpy.qos import QoSProfile, ReliabilityPolicy

class ImageBroker(Node):

    def __init__(self):
        super().__init__('img_broker')
        self.bridge = CvBridge()
        self.flag = "rgb"

        self.seg_message_delay_time = None
        self.class_message_delay_time = None

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.select_img)

        qos_profile_best_effort  = QoSProfile(depth=1, reliability=ReliabilityPolicy.BEST_EFFORT)

        # sub & Image processing
        self.sub_rgb = self.create_subscription(
            Image,
            'rgb_image',
            self.subscribe_rgb_image,
            qos_profile=qos_profile_best_effort
        )

        self.sub_class = self.create_subscription(
            Image,
            'class_image',
            self.subscribe_class_image,
            qos_profile=qos_profile_best_effort
        )

        self.sub_seg = self.create_subscription(
            Image,
            'seg_image',
            self.subscribe_seg_image,
            qos_profile=qos_profile_best_effort
        )

        # pub
        self.pub_per_img = self.create_publisher(Image, 'perception_image', 1)


    def subscribe_rgb_image(self, msg):
        if self.flag == "rgb":
            self.pub_per_img.publish(msg)

    def subscribe_class_image(self, msg):
        self.class_message_delay_time = self.get_clock().now()
        if self.flag == "class":
            self.pub_per_img.publish(msg)

    def subscribe_seg_image(self, msg):
        self.seg_message_delay_time = self.get_clock().now()
        if self.flag == "seg":
            self.pub_per_img.publish(msg)

    def select_img(self):
        time_now = self.get_clock().now()

        if self.seg_message_delay_time is not None:
            seg_diff = time_now - self.seg_message_delay_time
            if seg_diff.nanoseconds < 10**9:
                if self.flag != "seg":
                    self.flag = "seg"
                return

        if self.class_message_delay_time is not None:
            class_diff = time_now - self.class_message_delay_time
            # self.get_logger().info(f'diff_time: {class_diff.nanoseconds}')
            if class_diff.nanoseconds < 10**9:
                if self.flag != "class":
                    self.flag = "class"
                return

        if self.flag != "rgb":
            self.flag = "rgb"

        # self.get_logger().info(f'Current flag : {self.flag}')

def main(args=None):
    rclpy.init(args=args)
    node = ImageBroker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt (SIGINT)')
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()