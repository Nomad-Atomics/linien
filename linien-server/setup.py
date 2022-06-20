# Copyright 2018-2022 Benjamin Wiegand <benjamin.wiegand@physik.hu-berlin.de>
# Copyright 2022 Bastian Leykauf <leykauf@physik.hu-berlin.de>
#
# This file is part of Linien and based on redpid.
#
# Linien is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Linien is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Linien.  If not, see <http://www.gnu.org/licenses/>.

import re

import setuptools
from setuptools import find_packages

VERSIONFILE = "linien_server/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setuptools.setup(
    name="linien-server",
    version=verstr,
    author="Benjamin Wiegand",
    author_email="highwaychile@posteo.de",
    maintainer="Bastian Leykauf",
    maintainer_email="leykauf@physik.hu-berlin.de",
    description="Server of linien that runs on RedPitaya.",
    long_description="Have a look at the 'linien' package for installation instructions.",  # noqa: E501
    long_description_content_type="text/x-rst",
    url="https://github.com/linien-org/linien",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "rpyc>=4.0,<5.0",
        "myhdl>=0.11",
        "click>=7.1.2",
        "cma>=3.0.3",
        "plumbum>=1.6.9",
        "pylpsd>=0.1.4",
        "numpy>=1.11.0",
        "scipy>=0.17.0",
        "linien-common=={}".format(verstr),
    ],
    scripts=[
        "linien_server/server.py",
        "linien_server/linien_start_server.sh",
        "linien_server/linien_stop_server.sh",
        "linien_server/linien_install_requirements.sh",
        "linien_server/linien_start_ethernet_blinking.sh",
        "linien_server/linien_stop_ethernet_blinking.sh",
    ],
    package_data={
        "": [
            "linien.bin",
            "linien_start_server.sh",
            "linien_stop_server.sh",
            "linien_start_ethernet_blinking.sh",
            "linien_stop_ethernet_blinking.sh",
            "linien_install_requirements.sh",
        ]
    },
)