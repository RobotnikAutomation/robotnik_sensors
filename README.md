# Robotnik sensors

This package contains the description of the sensors used in Robotnik robots.

## Installation

Download this repository and use the branch ros2-devel

```bash
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

This repository contains a package *robotnik_sensors* which includes the URDF description of the sensors.

The entrypoint of the package is the file [robotnik_sensors/urdf/sensors.urdf.xacro](robotnik_sensors/urdf/sensors.urdf.xacro). This file includes all the sensors macros and the description of the sensors.

The sensors macros have the following arguments:

| Arguments      	| Description                                                                   	|
|----------------	|-------------------------------------------------------------------------------	|
| frame_prefix   	| prefix added to the frame                                                     	|
| parent         	| parent link of the sensor                                                     	|
| origin         	| origin block for the position and orientation of the sensor                   	|

For simulation, the following arguments are also available:

| Arguments      	| Description                                                                   	|
|----------------	|-------------------------------------------------------------------------------	|
| node_namespace 	| namespace of the plugin                                                       	|
| node_name      	| name used for the plugin node in Gazebo                                       	|
| gazebo_ignition	| boolean to include the plugin for Gazebo Ignition                               |
| topic_prefix   	| prefix added to the topic name                                                	|
| gpu             | boolean to use the GPU for the sensor (only available for 2d and 3d lidar)      |

You can find an example of the usage in the [default.urdf.xacro](robotnik_sensors_gazebo/urdf/default.urdf.xacro) file in robotnik_sensors_gazebo.

```sh
  <xacro:include filename="$(find robotnik_sensors)/urdf/all_sensors.urdf.xacro" />
  <xacro:call
      macro="sensor_$(arg sensor_type)"
      frame_prefix="$(arg sensor_name)_"
      parent="world"
      node_namespace="$(arg sensor_ns)"
      node_name="$(arg sensor_name)"
      gazebo_ignition="true"
      topic_prefix="~/">
    <origin xyz="0.0 0.0 0.1" rpy="0.0 0.0 0.0"/>
  </xacro:call>
```

The macro names are sensor_ + the name of the sensor described above. For example:

- sensor_intel_realsence_d435
- sensor_vectornav
