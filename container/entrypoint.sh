#!/bin/bash

set -e

source /opt/ros/${ROS_DISTRO}/setup.sh
source /ros2_ws/install/local_setup.sh

exec "$@"