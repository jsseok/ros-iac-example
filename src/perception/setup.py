from setuptools import find_packages, setup

package_name = 'perception'

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
        'console_scripts': [
            'seg_yolov8 = perception.seg_yolov8s.main:main',
            #'class_yolov8 = perception.class_yolov8.main:main',
        ],
    },
)