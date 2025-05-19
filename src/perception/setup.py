import sys
import os
import json 
from setuptools import find_packages, setup

package_name='perception'

entry_nodes = [
    'seg_yolov8s = perception.seg_yolov8s.main:main',
    'class_yolov8s = perception.class_yolov8s.main:main'
]

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='worker',
    maintainer_email='worker@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': entry_nodes,
    },
)

