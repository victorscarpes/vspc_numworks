# vspc_numworks

This repository is my personal collection of python scripts for the Numworks graphing calculator. Considering that this repo contains all my scripts in no particular order, this `README.md` file will not include documentation on individual files, but it will document 2 fundamental talking points.

## Source compression

To be able to fit the maximum ammount of scripts on the calculator, all source files are refactored to minimize the ammount of characters on the files using the `python-minifier` library (available [here](https://dflook.github.io/python-minifier/)). To compress the files, run the `source_compressor.py` script at the root of the repo. The program will compress all `.py` files on the `Source/` directory and put the outputs on the `Minified/` directory.

## Global variables naming convention

Some of the files are meant to be imported from a repl shell, defining functions for the user to access. To make that process easier, all global variables, including functions, that do not beging with an underscore are listed when the `var` button is pressed on the calculator. To avoid clutter, all functions and variables not meant to be directly accessed by the user begin with an underscore. That makes it so that all those variables are private and are not added to the namespace when `from <module> import *`, demanding all imports of non built-in modules to be either `import <module>`, `import <module> as <alias>` or, if few variables are needed, `from <module> import <variable1>, <variable2>`.
