from setuptools import find_packages, setup

package_name = 'test_pkg'

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
    maintainer='dbko',
    maintainer_email='dbko112@etri.re.kr',
    description='This is a test package to verify the sdi pipeline',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'helloworld_publisher = test_pkg.publisher.helloworld_publisher:main',
            'helloworld_subscriber = test_pkg.subscriber.hellowrold_subscriber:main',
        ],
    },
)
