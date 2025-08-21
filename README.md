# 🤖 Mecmobile
**Mecanum Mobile & SLAM**

The project focuses on the development of a **Mecanum wheel robot** capable of moving autonomously from point A to point B.  
The initial position can be selected, and from there the robot uses advanced localization algorithms to determine and update its position in the environment.

Specifically, the system integrates:
- **Monte Carlo Localization (MCL):** particle filter-based estimation of the robot’s position.  
- **Global Localization:** enabling the robot to localize itself without prior knowledge of its starting point.  
- **Local Localization:** ensuring real-time correction and improved accuracy during navigation.  

With these functionalities, the robot can not only reach defined target positions but also adapt to different navigation scenarios with high precision.

---

## 🚀 Features
- ✅ Omnidirectional movement with **Mecanum wheels**  
- ✅ **Monte Carlo Localization (MCL)** for robust position estimation  
- ✅ **Global & local localization**  
- ✅ Integration with **SLAM** for mapping  
- ✅ Autonomous **point-to-point navigation**  

---
## 🎥 Demo
[Video.webm](https://github.com/user-attachments/assets/469913b1-51a5-4534-82cc-99b841a54635)

## 🔧 Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/tuusuario/Mecmobile.git
cd Mecmobile
# install dependencies
pip install -r requirements.txt
# run with ROS2 launch
ros2 launch mecmobile bringup.launch.py


