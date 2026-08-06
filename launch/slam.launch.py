from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution


def generate_launch_description():

    slam_params = PathJoinSubstitution([
        FindPackageShare("diff_drive_robot"),
        "config",
        "slam.yaml"
    ])

    slam = Node(
        package="slam_toolbox",
        executable="async_slam_toolbox_node",
        name="slam_toolbox",
        output="screen",
        parameters=[slam_params],
    )

    return LaunchDescription([
        slam
    ])
