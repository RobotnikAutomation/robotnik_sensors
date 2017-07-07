^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package robotnik_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.1.1 (2016-12-16)
------------------
* Merge indigo to kinetic
* 1.0.5
* updated changelog
* 1.0.4
* update changelog
* MOD: Fixed problem with rotations
* --amend
* standarized all sensors: frames, joints, topics and params
* reduced rate drift and associated gaussian noise
* 1.0.3
* updated changelog
* Contributors: Jose Rapado, Marc Bosch-Jorge, carlos3dx, rguzman1

1.1.0 (2016-09-01 08:19:07 +0200)
---------------------------------
* updated changelog
* Contributors: carlos3dx

1.0.5 (2016-12-16 10:29:20 +0100)
---------------------------------
* updated changelog
* 1.0.4
* update changelog
* MOD: Fixed problem with rotations
* --amend
* standarized all sensors: frames, joints, topics and params
* reduced rate drift and associated gaussian noise
* Contributors: Jose Rapado, Marc Bosch-Jorge, carlos3dx, rguzman1

1.0.3 (2016-09-01 08:12:30 +0200)
---------------------------------
* updated changelog
* modified xmls:xacro
* Merge branch 'indigo-devel' of https://github.com/RobotnikAutomation/robotnik_sensors into indigo-devel
* Modified .xacro files
* corrected name of orientation parameters
* updated gps and imu_hector parameters
* resolved conflict
* added ueye camera
* Added rplidar to all_sensors
* Contributors: Marc Bosch-Jorge, carlos3dx, summit

1.0.2 (2016-07-12 07:30:38 +0200)
---------------------------------
* updated changelog
* Setting TIM571 params
* Added Sick Tim571 sensor
* New collision model for s3000
* Merge branch 'indigo-devel' of https://github.com/RobotnikAutomation/robotnik_sensors into indigo-devel
* adding the rplidar sensor
* sick_s300: changed collision model
* kinectv2: added model with no base and corrected bounding box of collision
* Merge remote-tracking branch 'origin/indigo-devel' into indigo-devel
* asus_xtrion_pro: corrected typo
* orbbec_astra: now calls the correct gazebo sensor
* Contributors: Jose Rapado, Marc Bosch-Jorge, RomanRobotnik, carlos3dx

1.0.1 (2016-06-27 09:13:11 +0200)
---------------------------------
* Adding CHANGELOG
* Setting build & run dependencies
* adding .gitignore
* Removed author
* Removing run dependencies and adding mantainers
* corrected angular resolution
* updated s300 standard sensor params
* added sick s300
* changed scale to 1 as the meshes were updated to scale 1
* added imu_hector_plugin.urdf.xacro, that seems to work better in sim
* reduced gps drift for rtk tests
* changed scale in asus_xtion_pro.urdf.xacro for new dae
* Merge branch 'indigo-devel' of https://github.com/RobotnikAutomation/robotnik_sensors into indigo-devel
* updated asus_xtion_pro_live.dae
* fixing 'scale' variable name. It was colliding between asus_xtion and orbec_astra sensors
* changed cam_link to have a reference frame for mounting in robot, not very useful at al...
* orbbec_astra frames updated to be compatible with gazebo plugin
* corrected scale and positions of optical frames
* added orbbec to all_sensors.urdf.xacro
* minor change names
* Merge branch 'indigo-devel' of https://github.com/RobotnikAutomation/robotnik_sensors into indigo-devel
  locally added orbbec astra sensor
* added orbecc_astra sensor
* minor change in collision box
* axis sensor: corrected pan tilt joints positions
* Added optical frame and modified parameters to axis_m5013.urdf.xacro
* axis_m5013 collision pos corrected
* changed collision box of ust10
* Merging master with indigo-devel to add the Sick S3000 laser
* Sicks3000
* malformed stl error rviz corrected by meshlab edit
* robotnik_sensors: adding min and max angle params to hokuyo sensors
* robotnik_sensors: removed collision model of the utm30lx sensor (it was colliding with itself)
* Adding new sensor SICKS3000
* corrected mesh file link
* renamed file, new sensor in all_sensors.urdf.xacro
* added hokuyo_ust_10lx model
* added latest stl of kinectv2. Note that dae was rotated 270ºZ from stl to be compliant with rest of rgbd devices tf
* added kinectv2 urdf (to be improved)
* added kinectv2
* Merge branch 'indigo-devel' of https://github.com/RobotnikAutomation/robotnik_sensors into indigo-devel
* added pointCloudCutoffMax param
* Change reference coordinates and topic name
* Setting hokuyo3d.dae path correctly
* compliant with new tag hardwareInterface requirement in joint
* removed dependancy from rbcar, modified sensor links and samples
* added gps_with_mast
* First commit. Compiles in indigo
* Initial commit
* Contributors: Dani Carbonell, ElenaFG, Jorge Arino, Marc Bosch-Jorge, RomanRobotnik, carlos3dx, mcantero, rguzman
