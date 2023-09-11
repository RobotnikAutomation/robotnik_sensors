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


def check_xacro_file(name: str):
    """Check if the xacro file is valid."""
    current_path = os.path.dirname(os.path.realpath(__file__))
    description_path = os.path.join(
        current_path,
        "test.xacro",
    )

    _, urdf_file = tempfile.mkstemp(suffix=".urdf")
    xacro_command = (
        f"{shutil.which('xacro')}"
        f" {description_path}"
        f" sensor_type:={name}"
        f" > {urdf_file}"
    )
    urdf_command = f"{shutil.which('check_urdf')}" f" {urdf_file}"

    try:
        xacro_process = subprocess.run(
            xacro_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            check=False,
        )

        if xacro_process.returncode != 0:
            print(xacro_process.stdout.decode("utf-8"))
            print(xacro_process.stderr.decode("utf-8"))

        assert xacro_process.returncode == 0, "Xacro process failed!"

        urdf_process = subprocess.run(
            urdf_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            check=False,
        )

        if urdf_process.returncode != 0:
            print(urdf_process.stdout.decode("utf-8"))
            print(urdf_process.stderr.decode("utf-8"))

        assert urdf_process.returncode == 0, "URDF process failed!"

    finally:
        os.remove(urdf_file)


def test_xacro_intel_realsense_d435():
    """Test xacro default."""
    check_xacro_file("intel_realsense_d435")


def test_xacro_orbbec_astra():
    """Test xacro default."""
    check_xacro_file("orbbec_astra")


def test_xacro_stereolabs_zed2():
    """Test xacro default."""
    check_xacro_file("stereolabs_zed2")


def test_xacro_sick_microscan3():
    """Test xacro default."""
    check_xacro_file("sick_microscan3")


def test_xacro_sick_nanoscan3():
    """Test xacro default."""
    check_xacro_file("sick_nanoscan3")


def test_xacro_sick_outdoorscan3():
    """Test xacro default."""
    check_xacro_file("sick_outdoorscan3")


def test_xacro_sick_s300():
    """Test xacro default."""
    check_xacro_file("sick_s300")


def test_xacro_sick_s3000():
    """Test xacro default."""
    check_xacro_file("sick_s3000")


def test_xacro_sick_tim551():
    """Test xacro default."""
    check_xacro_file("sick_tim551")


def test_xacro_sick_tim571():
    """Test xacro default."""
    check_xacro_file("sick_tim571")


def test_xacro_robosense_bpearl():
    """Test xacro default."""
    check_xacro_file("robosense_bpearl")


def test_xacro_velodyne_vlp16():
    """Test xacro default."""
    check_xacro_file("velodyne_vlp16")


if __name__ == "__main__":
    test_xacro_intel_realsense_d435()
    test_xacro_orbbec_astra()
    test_xacro_stereolabs_zed2()

    test_xacro_sick_microscan3()
    test_xacro_sick_nanoscan3()
    test_xacro_sick_outdoorscan3()
    test_xacro_sick_s300()
    test_xacro_sick_s3000()
    test_xacro_sick_tim551()
    test_xacro_sick_tim571()
