from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    map_file = LaunchConfiguration("map")

    nav2_params = PathJoinSubstitution([
        FindPackageShare("diff_drive_robot"),
        "config",
        "nav2_params.yaml"
    ])

    nav2_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("nav2_bringup"),
                "launch",
                "bringup_launch.py"
            ])
        ),
        launch_arguments={
            "map": map_file,
            "use_sim_time": "True",
            "params_file": nav2_params,
            "autostart": "True",
            "slam": "False"
        }.items(),
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            "map",
            default_value=PathJoinSubstitution([
                FindPackageShare("diff_drive_robot"),
                "maps",
                "my_map.yaml"
            ]),
            description="Path to map yaml"
        ),

        nav2_bringup,
    ])
