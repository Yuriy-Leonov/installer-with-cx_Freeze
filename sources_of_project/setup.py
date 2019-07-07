"""
Commands
python setup.py bdist_msi -> create installer
"""
import cx_Freeze
import platform


include_files = ["static\some_static_file.png"]


if platform.system() == "Windows":
    import os.path

    # just hardcoded for an example
    # environment variable should be used here
    PYTHON_INSTALL_DIR = "G:\Python\Python36"
    os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl',
                                             'tcl8.6')
    os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

    include_files.append(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'))
    include_files.append(
        os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'))

cx_Freeze.setup(
    name="example",
    options={
        "build_exe": {
            "packages": ["asyncio"],
            "include_files": include_files,
            "replace_paths": [("*", "")]
        },
        "bdist_msi": {
            "upgrade_code": "{492de237-1853-4599-a707-c283d567699f}"
        }
    },
    executables=[cx_Freeze.Executable("main.py")]
)
