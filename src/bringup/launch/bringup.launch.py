from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='test_pkg',
            executable='img_broker',
            name='img_broker',
            output='screen'
        ),
        Node(
            package='sensing',
            executable='usb_cam',
            name='usb_cam',
            output='screen'
        ),
        Node(
            package='perception',
            executable='seg_yolov8s',
            name='seg_yolov8s',
            output='screen'
        ),
    ])

