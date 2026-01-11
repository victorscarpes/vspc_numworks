# vspc_numworks

This repository is my personal collection of python scripts for the Numworks graphing calculator. Considering that this repo contains all my scripts in no particular order, this `README.md` file will not include documentation on individual files, but it will comment 2 fundamental philosophies of this repo.

## Source compression

To be able to fit the maximum ammount of scripts on the calculator, all source files are refactored to minimize the ammount of characters on the files using the `python-minifier` library (available [here](https://dflook.github.io/python-minifier/)).

To compress the files, run the `source_compressor.py` script at the root of the repo. The program will compress all `.py` files on the `Source/` directory and put the outputs on the `Minified/` directory.

### RAM optimization

Sometimes, when long literal expressions are used often, one way to reduce the size of the script is to assign those literals to a variable with a short name and just use that instead. This allows the file to use less characters. The problem is that now that literal is stored in RAM. If the program is already close to the RAM usage limit, the compression can render the script unusable. By default, this type of optmization is not done, but in cases where RAM is not an issue, including the comment `# optmize_ram` anywhere on the script will tell the compressor that this type of optimization can be done.

## Global variables naming convention

Some of the files are meant to be imported from a repl shell, defining functions for the user to access. To make that process easier, all global variables, including functions, that do not begin with an underscore are listed when the `var` button is pressed on the calculator. To avoid clutter, all functions and variables not meant to be directly accessed by the user begin with an underscore. That makes it so that all those variables are private and are not added to the namespace with global imports (i.e. `from <module> import *`). To avoid this problem, I simply do not use global imports, always managing the namespace properly.
