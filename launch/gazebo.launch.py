from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare

from launch.substitutions import Command, PathJoinSubstitution

import os


def generate_launch_description():

    pkg_gazebo_ros = FindPackageShare("gazebo_ros")

    world = PathJoinSubstitution([
        FindPackageShare("diff_drive_robot"),
        "worlds",
        "my_world.world"
    ])

    robot_description = Command([
        "xacro ",
        PathJoinSubstitution([
            FindPackageShare("diff_drive_robot"),
            "urdf",
            "robot.xacro"
        ])
    ])
    
    controller_config = PathJoinSubstitution([
        FindPackageShare("diff_drive_robot"),
        "config",
        "controllers.yaml"
    ])

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                pkg_gazebo_ros.find("gazebo_ros"),
                "launch",
                "gazebo.launch.py"
            )
        ]),
        launch_arguments={
            "world": world
        }.items()
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{
            "robot_description": ParameterValue(
                robot_description,
                value_type=str
            )
            
        }],
        output="screen"
    )
    
    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster"
        ],
        output="screen"
    )
    
    diff_drive_controller = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "diff_drive_controller"
        ],
        output="screen"
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "diff_drive_robot",
            "-topic", "robot_description"
        ],
        output="screen"
    )

    return LaunchDescription([
    gazebo,
    robot_state_publisher,
    spawn_robot,

    TimerAction(
        period=10.0,
        actions=[
            joint_state_broadcaster,
            diff_drive_controller
        ]
    )
])
