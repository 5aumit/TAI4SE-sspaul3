from distutils.core import setup
import py2exe


# Dependencies are automatically detected, but it might need fine tuning.
#buildOptions = {"packages": [], "excludes": [""]}

# GUI applications require a different base on Windows (the default is for a
# console application).
#



#expectstub = Target(
#    script="expectstub.py"
#    )




setup(name="name",
      # console based executables
      console=['winpexpect_test.py'],

      # windows subsystem executables (no console)
      windows=[],

      # py2exe options
      zipfile=None,
#      options={"py2exe": py2exe_options},
      )