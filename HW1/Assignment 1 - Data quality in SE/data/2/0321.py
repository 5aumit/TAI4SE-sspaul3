from spack import *
from spack.util.environment import is_system_path
import os,re


class Stitched(CMakePackage):
    homepage = "https://github.com/cms-sw/stitched.git"
    url = "https://github.com/cms-sw/stitched.git"

    version('master', git='https://github.com/cms-sw/Stitched.git',
            branch="master")
    
    resource(name='cmaketools', git='https://github.com/gartung/cmaketools.git',
              placement="cmaketools")
 
    depends_on('md5-cms')
    depends_on('boost')
    depends_on('python')
    depends_on('py-pybind11', type=('link', 'run', 'test'))
    depends_on('tinyxml2@6.2.0')
    depends_on('root ~opengl cxxstd=17')
    depends_on('fmt+pic cxxstd=17')
    depends_on('xrootd')
    depends_on('clhep@2.4.1.3')
    depends_on('intel-tbb-oneapi')
    depends_on('cppunit', type=('link', 'test'))
    depends_on('xerces-c')
    depends_on('catch2', type=('link', 'test'))
    depends_on('googletest', type=('link', 'test'))
    depends_on('benchmark@1.4.1', type=('link', 'test'))


    def cmake_args(self):
        cxxstd = self.spec['root'].variants['cxxstd'].value
        args = ['-DCMakeTools_DIR=%s/cmaketools' % self.stage.source_path]
        args.append('-DCLHEP_ROOT_DIR=%s' % self.spec['clhep'].prefix)
        args.append('-DBOOST_ROOT=%s' % self.spec['boost'].prefix)
        args.append('-DTBB_ROOT_DIR=%s' % self.spec['intel-oneapi-tbb'].prefix.tbb.latest)
        args.append('-D_TBB_COMPILER=gcc4.8')
        args.append('-DTINYXML2_ROOT_DIR=%s' % self.spec['tinyxml2'].prefix)
        args.append('-DCMSMD5ROOT=%s' % self.spec['md5-cms'].prefix)
        args.append('-DCMAKE_CXX_STANDARD=%s'% cxxstd)
        args.append('-DXROOTD_INCLUDE_DIR=%s/xrootd' % self.spec['xrootd'].prefix.include)
        args.append('-DCATCH2_INCLUDE_DIRS=%s/catch2' % self.spec['catch2'].prefix.include)
        args.append('-DBUILDTEST=BOOL:True') 
        return args

    def setup_build_environment(self, env):
        # This hack is made necessary by a header name collision between
        # md5-cms and libmd md5.h
        # But dependencies without CMake defined includes need to be added back
        def prepend_include_path(dep_name):
            include_path = self.spec[dep_name].prefix.include
            if not is_system_path(include_path):
                env.prepend_path('SPACK_INCLUDE_DIRS', include_path)
        prepend_include_path('md5-cms')
