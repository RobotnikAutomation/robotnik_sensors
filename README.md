# Robotnik sensors

This package contains the description of the sensors used in Robotnik robots.

The types of sensors available are:
- 2D LiDAR
- 3D LiDAR
- Camera
- Depth Camera
- GPS
- IMU

You can find the list of available sensors at the [Sensors section](#sensors).

## Installation

Download this repository and use the default devel branch: jazzy-devel

```bash
git clone https://github.com/RobotnikAutomation/robotnik_sensors.git -b jazzy-devel
```

## Usage

The entrypoint of the package is the file [robotnik_sensors/urdf/all_sensors.urdf.xacro](robotnik_sensors/urdf/all_sensors.urdf.xacro). This file includes all the sensor description of the sensors.

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
| gazebo_ignition	| boolean to additional information for Gazebo Ignition simulation                              |
| topic_prefix   	| prefix added to the topic name                                                	|
| gpu             | boolean to use the GPU for the sensor (only available for 2d and 3d lidar)      |


#### Example

This example shows how to include a SICK S300 2D LiDAR in a robot description:

```sh
  <xacro:include
    filename="$(find robotnik_sensors)/urdf/all_sensors.urdf.xacro" />
  
  <xacro:sensor_sick_s300
    frame_prefix="$(arg prefix)front_laser_"
    parent="$(arg prefix)chassis_link"
    node_namespace="$(arg namespace)"
    node_name="front_laser"
    gazebo_ignition="$(arg gazebo_ignition)">
    <origin xyz="${front_laser_offset_x} ${front_laser_offset_y} ${front_laser_offset_z}" rpy="0 ${-PI} ${-3/4*PI}" />
  </xacro:sensor_sick_s300>
```

### Contributing

All files must be formatted using [Prettier](https://prettier.io/) with the configuration found in [.github/.prettierrc.json](.github/.prettierrc.json).

Install npm, prettier and prettier/plugin-xml:

```bash
sudo apt install npm
sudo npm install -g prettier @prettier/plugin-xml
```

To format the files, run:

```bash
prettier --plugin=$(npm root -g)/@prettier/plugin-xml/src/plugin.js --config .github/.prettierrc.json --write "robotnik_sensors/urdf/**/*.{xml,xacro,urdf}"
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

### Depth Camera

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