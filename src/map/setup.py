from setuptools import find_packages, setup
import json

package_name = 'map'

entry_nodes = []

with open('../../list_of_nodes.yaml', 'r', encoding='utf-8') as f:
    data = json.load(f)
    node_list = data.get(package_name, [])
    if(len(node_list) > 0):
        entry_nodes = [f"{node['node_name']} = {package_name}.{node['node_name']}.main:main" for node in node_list]

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
