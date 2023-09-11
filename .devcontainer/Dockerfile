FROM robotnik/ros:humble-builder

# Install cyclonedds
USER root

# Change to mirror
#RUN sed -i 's/packages.ros.org/ros.mirror.robotnik.ws/' /etc/apt/sources.list.d/ros-latest.list

# Install dependencies
RUN apt-get update && apt-get install -y \
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-rqt* \
    ros-$ROS_DISTRO-gazebo* \
    unzip \
    && rm -rf /var/lib/apt/lists/*

USER ${USER_NAME}

RUN wget https://codeload.github.com/osrf/gazebo_models/zip/refs/heads/master -O models.zip \
    && mkdir -p ${USER_HOME}/.gazebo/models/ \
    && unzip models.zip -d ${USER_HOME}/.gazebo/models/ \
    && mv ${USER_HOME}/.gazebo/models/gazebo_models-master/* ${USER_HOME}/.gazebo/models/ \
    && rm -rf ${USER_HOME}/.gazebo/models/gazebo_models-master/ \
    && rm models.zip

ENV ROS_SETUP_FILES="${USER_WORKSPACE}/install/local_setup.bash"
