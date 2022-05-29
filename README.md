# Learning About Qt For Python

I have much professional experience with Qt from its native C++, but have never attempted Qt from Python.

The Qt Company's official adoption of the [PySide project][QP01] provides an attractive licensing alternative to the long-standing [PyQt product][QP02].

These are my personal investigations of [Qt for Python][QP03], learning by hand-crafting small, tested desktop applications.

[QP01]: https://en.wikipedia.org/wiki/PySide
        "Wikipedia entry for PySide"
[QP02]: https://en.wikipedia.org/wiki/PyQt
        "Wikipedia entry for PyQt"
[QP03]: https://doc.qt.io/qtforpython/
        "Qt for Python"


## Exercises

This is a brief summary of the exercises. Click the links above for more information. For example, link `1_hello_world` has all details for the first exercise.

1. Hello World

   A trivial application, useful for discovering the configuration details.


## Configuration

These exercises use Qt 6.3.0, the latest at the time of writing.

The corresponding PySide6 [installation instructions][CO01] worked well, mostly.

[CO01]: https://wiki.qt.io/Qt_for_Python
        "Qt for Python: PySide6"

```
~ % mkdir QtForPython

~ % cd QtForPython

QtForPython % python3 -m venv env

QtForPython % source env/bin/activate

(env) QtForPython % pip3 install PySide6

(env) QtForPython % python3

>>> import PySide6

>>> PySide6.__version__
'6.3.0'
```

I had one error at the install step. It had helpful advice to upgrade pip in the Python virtual environment, as follows.

```
(env) QtForPython % pip3 install PySide6
ERROR: Could not find a version that satisfies the requirement PySide6 (from versions: none)
ERROR: No matching distribution found for PySide6
WARNING: You are using pip version 20.2.3; however, version 22.1.1 is available.
You should consider upgrading via the '/Users/ifisher/QtForPython/env/bin/python3 -m pip install --upgrade pip' command.

(env) QtForPython % python3 -m pip install --upgrade pip
```

For now, I use QtCreator to configure, build, and run. That is fine for these personal learning exercises. A more production-like environment would require standalone build scripts and run scripts.

Ensure QtCreator is using the Python virtualenv with the PySide6 installation.

- In each fresh shell, activate the virtualenv, as shown above
- Launch QtCreator from the command line
- Open an application's .pyproject file
- Check the project build and run settings and set the interpreter to the virtual environment version


