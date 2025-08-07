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


"""Xacro test module."""

import os
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from ament_index_python.packages import get_package_share_directory

import pytest


def check_meshes(urdf_file):
    """Check that all meshes in the URDF file exist."""
    # Parse URDF file
    root = ET.parse(urdf_file).getroot()
    # Find all mesh elements
    meshes = root.findall('.//mesh')
    # List of all failed meshes [filename: reason]
    failed_meshes = []
    # Check that all meshes exist
    for mesh in meshes:
        filename = mesh.get('filename')
        if filename.startswith('package://'):
            package_name, _, package_path = filename[10:].partition('/')
            package_share_path = get_package_share_directory(package_name)
            if not os.path.exists(f'{package_share_path}/{package_path}'):
                failed_meshes.append(f'{filename}: file does not exist')
        else:
            failed_meshes.append(f'{filename}: not a package:// path')

    assert not failed_meshes, f'Failed meshes:\n{failed_meshes}'


# List of all sensors
sensors = [
    'intel_realsense_d435',
    'intel_realsense_d435i',
    'orbbec_astra',
    'stereolabs_zed2',
    'stereolabs_zed2i',
    'azure_kinect',
    'sick_microscan3',
    'sick_nanoscan3',
    'sick_outdoorscan3',
    'sick_s300',
    'sick_s3000',
    'sick_tim551',
    'sick_tim571',
    'hokuyo_urg04lx',
    'hokuyo_ust10lx',
    'hokuyo_ust20lx',
    'hokuyo_utm30lx',
    'velodyne_vlp16',
    'robosense_bpearl',
    'robosense_helios_16p',
    'ouster',
    'livox_mid_360',
    'sick_multiscan_100',
    'vectornav',
    'myahrs',
    'pixhawk',
    'gps',
    'gps_with_mast',
    'ublox',
    'ublox_with_mast',
    'axis_m5013',
    'axis_m5074',
    'axis_m5525',
    'axis_m5526',
]


@pytest.mark.parametrize('sensor', sensors)
@pytest.mark.parametrize('ignition', [False, True])
def test_xacro_file(sensor, ignition):
    """Test xacro file generation."""
    (fd, tmp_urdf_output_file) = tempfile.mkstemp(suffix='.urdf')
    os.close(fd)

    current_path = os.path.dirname(os.path.realpath(__file__))
    description_path = os.path.join(
        current_path, 'test.xacro',
    )

    xacro_path = shutil.which('xacro')
    assert xacro_path, 'xacro is not installed'

    check_urdf_path = shutil.which('check_urdf')
    assert check_urdf_path, 'check_urdf is not installed'

    xacro_command = (
        f"{shutil.which('xacro')}"
        f' {description_path}'
        f' model:={sensor}'
        f' name:=sensor_name'
        f' namespace:=sensor_namespace'
        f' gazebo_ignition:={"true" if ignition else "false"}'
        f' -o {tmp_urdf_output_file}'
    )
    check_command = (
        f"{shutil.which('check_urdf')}"
        f' {tmp_urdf_output_file}'
    )

    try:
        # Generate URDF file
        print(f'running: {xacro_command}')
        xacro_process = subprocess.run(
            xacro_command, capture_output=True, text=True, shell=True
        )
        assert xacro_process.returncode == 0, (
            f'> xacro failed: {xacro_process.stderr}'
        )
        assert os.path.exists(tmp_urdf_output_file), (
            f'> xacro failed, output file not found: {tmp_urdf_output_file}'
        )

        # Check URDF file
        print(f'running: {check_command}')
        check_process = subprocess.run(
            check_command, capture_output=True, text=True, shell=True
        )
        assert check_process.returncode == 0, (
            f'> check_urdf failed: {check_process.stderr}'
        )

        # Check meshes
        check_meshes(tmp_urdf_output_file)

    finally:
        os.remove(tmp_urdf_output_file)
