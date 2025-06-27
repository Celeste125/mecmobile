from launch import LaunchDescription
from launch.actions import TimerAction, IncludeLaunchDescription,DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch.conditions import IfCondition, UnlessCondition

import os

def generate_launch_description():
    pkg_share = os.path.join(os.getenv('HOME'), 'mec_ws', 'install', 'mec_bot_bringup', 'share', 'mec_bot_bringup')

    use_slam = LaunchConfiguration("use_slam")

    use_slam_arg = DeclareLaunchArgument(
        "use_slam",
        default_value="false"
    )

    spawn_launch= IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'bringup.launch.py')
        )
    )
    convert= Node(
            package='mec_bot_bringup',
            executable='odom_tf_publisher.py',
            name='odom_tf_publisher',
            output='screen'
        )

    # Aquí agregas el relay node
    relay = Node(
        package="topic_tools",
        executable="relay",
        name="cmd_vel_relay",
        arguments=["/cmd_vel", "/mecanum_controller/cmd_vel_unstamped"],
        output="screen",
    )




    slam = IncludeLaunchDescription(
        os.path.join(
            get_package_share_directory("mec_bot_mapping"),
            "launch",
            "slam.launch.py"
        ),
        condition=IfCondition(use_slam)
    )
    rviz_slam = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(
                get_package_share_directory("mec_bot_mapping"),
                "rviz",
                "slam.rviz"
            )
        ],
        output="screen",
        parameters=[{"use_sim_time": True}],
        condition=IfCondition(use_slam)
    )

    

    return LaunchDescription([
        use_slam_arg,
        spawn_launch,
        relay,   # <-- este es el que te soluciona todo
        convert,
        slam,
        #rviz_slam,
    ])
