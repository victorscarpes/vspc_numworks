# vspc_numworks

This repository is my personal collection of python scripts for the Numworks graphing calculator. Considering that this repo contains all my scripts in no particular order, this `README.md` file will not include documentation on individual files, but it will comment 2 fundamental philosophies of this repo.

## Source compression

To be able to fit the maximum ammount of scripts on the calculator, all source files are refactored to minimize the ammount of characters on the files using the `python-minifier` library (available [here](https://dflook.github.io/python-minifier/)).

To compress the files, run the `source_compressor.py` script at the root of the repo. The program will compress all `.py` files on the `Source/` directory and put the outputs on the `Minified/` directory.

The compression of the file may reduce storage memory it uses but, as a consequence, may generate a script that use more RAM. If a given script is already at the calculator's limit, this may cause it to not run properly.

To control if RAM usage is unchanged, the comment `# keep_ram` can be included at the start of the file to force the compression not to create aditionnal variables, keeping RAM usage the same. A caveat of this is that this option has no control over the RAM usage of imported files. To make sure that everything works properly, I am going to experiment with it.

## Global variables naming convention

Some of the files are meant to be imported from a repl shell, defining functions for the user to access. To make that process easier, all global variables, including functions, that do not beging with an underscore are listed when the `var` button is pressed on the calculator. To avoid clutter, all functions and variables not meant to be directly accessed by the user begin with an underscore. That makes it so that all those variables are private and are not added to the namespace with global imports (i.e. `from <module> import *`). To avoid this problem, I simply do not use global imports, always managing the namespace properly.
