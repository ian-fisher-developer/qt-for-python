# Learning About Qt For Python

My employer heavily uses Qt from its native C++. The Qt Company's adoption of the PySide project provides LGPL Python APIs.

These are my personal investigations of Qt For Python, learning by hand-crafting small, tested desktop applications.


## Exercises

In progress...more to come.


## Configuration

Installation instructions are at https://wiki.qt.io/Qt_for_Python

It went smoothly, except for some helpful advice to upgrade pip in the Python virtual environment.

```
~ % mkdir QtForPython

~ % cd QtForPython

QtForPython % python3 -m venv env

QtForPython % source env/bin/activate

(env) QtForPython % pip3 install PySide6
ERROR: Could not find a version that satisfies the requirement PySide6 (from versions: none)
ERROR: No matching distribution found for PySide6
WARNING: You are using pip version 20.2.3; however, version 22.1.1 is available.
You should consider upgrading via the '/Users/ifisher/QtForPython/env/bin/python3 -m pip install --upgrade pip' command.

(env) QtForPython % python3 -m pip install --upgrade pip
Collecting pip
  Downloading pip-22.1.1-py3-none-any.whl (2.1 MB)
     |████████████████████████████████| 2.1 MB 156 kB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.2.3
    Uninstalling pip-20.2.3:
      Successfully uninstalled pip-20.2.3
Successfully installed pip-22.1.1

(env) QtForPython % pip3 install PySide6                                                   
Collecting PySide6
  Downloading PySide6-6.3.0-cp36-abi3-macosx_10_9_universal2.whl (65 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 65.8/65.8 kB 1.6 MB/s eta 0:00:00
Collecting PySide6-Essentials==6.3.0
  Downloading PySide6_Essentials-6.3.0-cp36-abi3-macosx_10_9_universal2.whl (130.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 130.0/130.0 MB 5.2 MB/s eta 0:00:00
Collecting PySide6-Addons==6.3.0
  Downloading PySide6_Addons-6.3.0-cp36-abi3-macosx_10_9_universal2.whl (212.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 212.5/212.5 MB 3.2 MB/s eta 0:00:00
Collecting shiboken6==6.3.0
  Downloading shiboken6-6.3.0-cp36-abi3-macosx_10_9_universal2.whl (374 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 374.5/374.5 kB 1.8 MB/s eta 0:00:00
Installing collected packages: shiboken6, PySide6-Essentials, PySide6-Addons, PySide6
Successfully installed PySide6-6.3.0 PySide6-Addons-6.3.0 PySide6-Essentials-6.3.0 shiboken6-6.3.0

(env) QtForPython % python3
Python 3.8.9 (default, Oct 26 2021, 07:25:54) 
[Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.

>>> import PySide6

>>> PySide6.__version__
'6.3.0'
```