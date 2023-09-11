# Copyright (c) 2023, Robotnik Automation S.L.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the Robotnik nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.


"""Spawns the robot in Gazebo and loads the controllers"""

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch import LaunchDescription

from launch.actions import IncludeLaunchDescription, GroupAction
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node, PushRosNamespace
from launch_ros.descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource

from robotnik_common.launch import AddArgumentParser, RewrittenYaml, ExtendedArgument


def generate_launch_description():
    """Returns the launch description"""

    ret_ld = LaunchDescription()
    add_to_launcher = AddArgumentParser(ret_ld)

    add_to_launcher.add_arg(
        ExtendedArgument(
            name="robot_id",
            description="ID of the robot",
            default_value="",
            use_env=True,
            environment="ROBOT_ID",
        )
    )

    add_to_launcher.add_arg(
        ExtendedArgument(
            name="sensor_type",
            description="Name of the sensor",
            default_value="orbbec_astra",
            use_env=True,
            environment="SENSOR_TYPE",
        )
    )

    add_to_launcher.add_arg(
        ExtendedArgument(
            name="sensor_name",
            description="Name of the sensor",
            default_value="front_sensor",
            use_env=True,
            environment="SENSOR_NAME",
        )
    )

    params = add_to_launcher.process_arg()

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            PathJoinSubstitution(
                [
                    FindPackageShare("robotnik_sensors_gazebo"),
                    "urdf",
                    "default.urdf.xacro",
                ]
            ),
            " sensor_type:=",
            params["sensor_type"],
            " sensor_name:=",
            params["sensor_name"],
            " sensor_ns:=",
            params["robot_id"],
        ]
    )
    robot_description_content = ParameterValue(
        robot_description_content, value_type=str
    )

    ret_ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [
                        FindPackageShare("gazebo_ros"),
                        "launch",
                        "gzserver.launch.py",
                    ]
                )
            ),
            launch_arguments={
                "verbose": "true",
                "init": "true",
                "factory": "true",
                "force_system": "true",
            }.items(),
        ),
    )

    ret_ld.add_action(
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution(
                    [
                        FindPackageShare("gazebo_ros"),
                        "launch",
                        "gzclient.launch.py",
                    ]
                )
            ),
            launch_arguments={"verbose": "true"}.items(),
        ),
    )

    ret_ld.add_action(
        GroupAction(
            [
                PushRosNamespace(params["robot_id"]),
                Node(
                    package="robot_state_publisher",
                    executable="robot_state_publisher",
                    name="robot_state_publisher",
                    output="screen",
                    parameters=[
                        {
                            "use_sim_time": True,
                            "robot_description": robot_description_content,
                            "publish_frequency": 100.0,
                            "frame_prefix": [params["robot_id"], "/"],
                            "ignore_timestamp": False,
                        }
                    ],
                ),
                Node(
                    package="gazebo_ros",
                    executable="spawn_entity.py",
                    arguments=[
                        "-entity",
                        "sensor",
                        "-topic",
                        "robot_description",
                    ],
                ),
                Node(
                    package="rviz2",
                    executable="rviz2",
                    arguments=[
                        "-d",
                        PathJoinSubstitution(
                            [
                                FindPackageShare("robotnik_sensors_gazebo"),
                                "rviz",
                                "default.rviz",
                            ]
                        ),
                    ],
                ),
                # Node(
                #     package="rqt_tf_tree",
                #     executable="rqt_tf_tree",
                # )
            ]
        )
    )

    return ret_ld
