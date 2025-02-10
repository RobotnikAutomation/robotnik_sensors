# Robotnik sensors

This package contains the description of the sensors used in Robotnik robots.

## Installation

Download this repository and use the branch ros2-devel

```sh
git clone https://github.com/RobotnikAutomation/robotnik_sensors.git -b ros2-devel
```

## Sensors

The available sensors in the package are:

### 2D LiDAR

- hokuyo_urg04lx
- hokuyo_ust10lx
- hokuyo_ust20lx
- hokuyo_utm30lx
- sick_microscan3
- sick_nanoscan3
- sick_outdoorscan3
- sick_s300
- sick_s3000
- sick_tim551
- sick_tim571

### 3D LiDAR

- livox_mid_360
- ouster
- robosense_bpearl
- robosense_helio_16p
- velodyne_vlp16

### Camera

- axis_m5013
- axis_m5074
- axis_m5525
- axis_m5526

### Depth

- azure_kinect
- intel_realsense_d435
- intel_realsense_d435i
- orbbec_astre
- stereolabs_zed2
- stereolabs_zed2i

### GPS

- gps
- gps_with_mast
- ublox

### IMU

- myahrs
- pixhawk
- vectornav


## Usage

This repository contains 2 packages *robotnik_sensors* and *robotnik_sensors_gazebo*. The first package includes all the URDF files with the macros and the second includes an example of usage in a URDF file and launch for Gazebo classic.

All the sensors are included in a file, [all_sensors.urdf.xacro](robotnik_sensors/urdf/all_sensors.urdf.xacro). This is the main file that must be included in URDF robots files to call the sensors description.

The sensors macros have the following arguments:

| Arguments      	| Description                                                                   	|
|----------------	|-------------------------------------------------------------------------------	|
| frame_prefix   	| prefix added to the frame                                                     	|
| parent         	| parent link of the sensor                                                     	|
| origin         	| origin block for the position and orientation of the sensor                   	|
| simulation     	| boolean to determine if the sensor will be used for simulation or not         	|
| node_name      	| name used for the plugin node in Gazebo                                       	|
| node_namespace 	| namespace of the plugin                                                       	|
| topic_prefix   	| prefix added to the topic name                                                	|
| gpu            	| boolean to determine if the gpu will be used for the plugins of Gazebo or not 	|

You can find an example of the usage in the [default.urdf.xacro](robotnik_sensors_gazebo/urdf/default.urdf.xacro) file in robotnik_sensors_gazebo.

```sh
  <xacro:include filename="$(find robotnik_sensors)/urdf/all_sensors.urdf.xacro" />
  <xacro:call
      macro="sensor_$(arg sensor_type)"
      frame_prefix="$(arg sensor_name)_"
      parent="world"
      simulation="true"
      node_namespace="$(arg sensor_ns)"
      node_name="$(arg sensor_name)"
      topic_prefix="~/">
    <origin xyz="0.0 0.0 0.1" rpy="0.0 0.0 0.0"/>
  </xacro:call>
```

The macro names are sensor_ + the name of the sensor described above. For example:

- sensor_intel_realsence_d435
- sensor_vectornav

## Cameras Configuration

In the case of the axis cameras, the URDF description of it includes some revolut joints to point the camera in the available directions. To use it in Gazebo, some controllers have to be used. By default it is used the joint_trajectory_controller. The file is found in the package [robotnik_sensors_gazebo](robotnik_sensors_gazebo/config/camera/).