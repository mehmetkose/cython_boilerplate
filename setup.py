from setuptools import setup, Extension
from Cython.Distutils import build_ext

NAME = "cython_boilerplate"
VERSION = "0.1"
DESCR = "cython_boilerplate"
URL = "http://mehmetkose.github.io"
REQUIRES = ['cython']

AUTHOR = "Mehmet Köse"
EMAIL = "mehmet@linux.com"

LICENSE = "Apache 2.0"

SRC_DIR = "cython_boilerplate"
PACKAGES = [SRC_DIR]

ext_1 = Extension(SRC_DIR + ".wrapped", [SRC_DIR + "/wrapped.pyx"], libraries=[], include_dirs=[])

EXTENSIONS = [ext_1]

if __name__ == "__main__":
    setup(install_requires=REQUIRES,
          packages=PACKAGES,
          zip_safe=False,
          name=NAME,
          version=VERSION,
          description=DESCR,
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license=LICENSE,
          cmdclass={"build_ext": build_ext},
          ext_modules=EXTENSIONS
    )
