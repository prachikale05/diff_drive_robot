from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import SetRemap
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare("nav2_bringup"),
                "launch",
                "bringup_launch.py"
            ])
        ),
        launch_arguments={
            "slam": "False",
            "use_sim_time": "True",
            "map": PathJoinSubstitution([
                FindPackageShare("diff_drive_robot"),
                "maps",
                "my_map.yaml"
            ]),
            "params_file": PathJoinSubstitution([
                FindPackageShare("diff_drive_robot"),
                "config",
                "nav2_params.yaml"
            ])
        }.items()
    )

    return LaunchDescription([
        SetRemap(
            src="/cmd_vel",
            dst="/diff_drive_controller/cmd_vel_unstamped"
        ),
        nav2
    ])
