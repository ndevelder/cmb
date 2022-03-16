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
#     spack install cmb
#
# You can edit this file again by typing:
#
#     spack edit cmb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cmb(CMakePackage):
    """Computational Model Builder By Kitware"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.computationalmodelbuilder.org"
    url      = "https://gitlab.kitware.com/cmb/cmb/-/archive/master/cmb-master.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers = ['ndevelder']

    # FIXME: Add proper versions and checksums here.
    # version('1.2.3', '0123456789abcdef0123456789abcdef')

    # FIXME: Add dependencies if required.
    depends_on('smtk')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
