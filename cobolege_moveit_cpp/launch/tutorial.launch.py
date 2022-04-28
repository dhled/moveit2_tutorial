import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition, UnlessCondition
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():

    db_arg = DeclareLaunchArgument("db", default_value="False", description="Database flag")


def generate_launch_description():
    moveit_config = (
        MoveItConfigsBuilder("cobolege")
        .robot_description(file_path="config/cobolege.urdf.xacro")
        .robot_description_semantic(file_path="config/cobolege_v0.srdf")
        .robot_description_kinematics(file_path="config/kinematics.yaml")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .to_moveit_configs()
    )

    # MoveGroupInterface demo executable
    move_group_demo = Node(
        name="move_group_interface_tutorial",
        package="cobolege_moveit_cpp",
        executable="move_group_interface_tutorial",
        output="screen",
        parameters=[
            moveit_config.robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
        ],
    )

    return LaunchDescription([move_group_demo])
