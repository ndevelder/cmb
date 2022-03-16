# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install smtk
#
# You can edit this file again by typing:
#
#     spack edit smtk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Smtk(CMakePackage):
    """Simulation Modeling Toolkit For Exawind Suite"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.computationalmodelbuilder.org/smtk"
    url      = "https://github.com/Kitware/SMTK/archive/refs/tags/v1.0.0rc1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['ndevelder']

    version('1.0.0rc1', sha256='b0d5ca78d2cdd34dd3ef5a14b5119f81c70e149a106f12a4fa5e7a62c7554b0d')

    # FIXME: Add dependencies if required.
    depends_on('boost')
    depends_on('moab')
    depends_on('opencascade')
    depends_on('python')
    depends_on('py-pybind11')
    #depends_on('qt@5.12.10')
    depends_on('paraview@5.9.1')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
