from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction, RegisterEventHandler
from launch.conditions import UnlessCondition
from launch.event_handlers import OnProcessExit
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    PythonExpression,
)
from launch_ros.actions import Node, SetParameter
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Argumentos configurables
    use_sim_time_arg = DeclareLaunchArgument(
        "use_sim_time",
        default_value="True",
        description="Use simulation (Gazebo) clock if true"
    )
    

    use_sim_time = LaunchConfiguration("use_sim_time")
    

    # Spawner para joint_state_broadcaster
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "joint_state_broadcaster",
            "--controller-manager",
            "/controller_manager",
        ],
        output="screen",
    )

    # Spawner para el controlador de ruedas mecanum
    mecanum_controller_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=[
            "mecanum_controller",
            "--controller-manager",
            "/controller_manager"
        ],
        output="screen",
    )

    return LaunchDescription([
        use_sim_time_arg,
        joint_state_broadcaster_spawner,
        mecanum_controller_spawner,
    ])
