import cx_Freeze
import sys
base = None
if sys.platform == "win32":
    base = "Win32GUI"
shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Blast Cloud Word Game",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]\PygameWordgame.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # Icon
     None,  # IconIndex
     None,  # ShowCmd
     "TARGETDIR",  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}

executables = [cx_Freeze.Executable(script="PygameWordgame.py",icon='cc.ico',base=base)]

cx_Freeze.setup(
    version="1.0",
    description="Pygame BLast Cloud Game",
    author="ForCodeCoder",
    name="Blast Cloud Word Game",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":['cc.ico','jj.png','1.png','2.png','clipart984165.png','explosion1.gif','bgmuisc.wav','boom.wav','loss1.wav']},
             "bdist_msi": bdist_msi_options,
             },
    executables = executables

    )
