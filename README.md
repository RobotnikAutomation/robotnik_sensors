# Robotnik sensors description

This package contains the description of the sensors used in Robotnik robots.

# Build status

Version | Main status | Devel Status
------ | ------ | ------
ROS1 | ![Build Status](https://github.com/RobotnikAutomation/robotnik_sensors/actions/workflows/build.yaml/badge.svg?branch=ros) | ![Build Status](https://github.com/RobotnikAutomation/robotnik_sensors/actions/workflows/build.yaml/badge.svg?branch=ros-devel)
ROS2 | ![Build Status](https://github.com/RobotnikAutomation/robotnik_sensors/actions/workflows/build.yaml/badge.svg?branch=ros2) | ![Build Status](https://github.com/RobotnikAutomation/robotnik_sensors/actions/workflows/build.yaml/badge.svg?branch=ros2-devel)

# dependencies

To use Gazebo GPU accelerated simulation: https://github.com/RobotnikAutomation/velodyne_simulator

# view models

You can view each model with the following command:

` roslaunch robotnik_sensors view_sensor.launch sensor:=SENSOR_NAME `

Example:

` roslaunch robotnik_sensors view_sensor.launch sensor:=intel_d435 `
