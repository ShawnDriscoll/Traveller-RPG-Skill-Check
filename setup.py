#
# Run the build process by entering 'setup.py' in a console prompt.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, with skillcheck076b.exe being amoung them.


from distutils.core import setup
import py2exe
import glob
import sys

sys.argv.append('py2exe')
  
opts = {'py2exe': {
                   'includes': ['matplotlib.backends',
                                'matplotlib.backends.backend_qt4agg',
                                'matplotlib.figure', 'pylab', 'numpy'],
                                #'matplotlib.backends.backend_tkagg'],
                   'excludes': ['_gtkagg', '_tkagg', '_agg2', 'bsddb', 'curses',
                                'email','pywin.debugger', 'pywin.debugger.dbgcon',
                                'pywin.dialogs', '_cairo', '_cocoaagg', '_fltkagg',
                                '_gtk', '_gtkcairo', 'tcl', 'Tkconstants', 'Tkinter'],
                   'packages': [],
                   'dll_excludes': ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                                    'tcl84.dll', 'tk84.dll']
                  }
        }
 
data_files = [
                  (r'mpl-data', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\*.*')),
                  (r'mpl-data', [r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\matplotlibrc']),
                  (r'mpl-data\images', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\images\*.*')),
                  (r'mpl-data\fonts', glob.glob(r'C:\Python25\Lib\site-packages\matplotlib\mpl-data\fonts\*.*')),
                  (r'phonon_backend', [r'C:\Python25\Lib\site-packages\PyQt4\plugins\phonon_backend\phonon_ds94.dll']),
                  (r'.', [r'C:\windows\system32\MSVCP71.dll']),
                  (r'.', [r'C:\windows\system32\MSVCR71.dll']),
                  (r'.', [r'C:\Python25\MSVCP90.dll']),
                  (r'.', [r'C:\Python25\MSVCR90.dll']),
                  (r'.', [r'sc_icon_16x16.ico']),
                  (r'fonts', [r'fonts\ERASDEMI.TTF']),
                  (r'docs', [r'docs\skill_check_ref.pdf', r'docs\ReadMe.txt'])
              ]

setup(
    
# for console program use "console = [{'script': 'skillcheck076b.py'}]"
# for windows program use "windows = [{'script': 'skillcheck076b.pyw'}]"
      
    console = [{'script': 'skillcheck076b.py'}],

    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = '0.7.6',
    description = 'Die roll tool for Mongoose Traveller',
    name = 'Skill Check (Beta)',
    options = opts,
    data_files = data_files,    
)
