cmake_minimum_required(VERSION 3.5)
project(robotnik_sensors_gazebo NONE)
find_package(ament_cmake REQUIRED)

install(DIRECTORY urdf launch rviz
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
