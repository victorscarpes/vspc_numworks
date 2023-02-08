import glob
from python_minifier import minify
import os


def numworks_minify(source: str, filename: str) -> str:
    return minify(source=source,
                  filename=filename,
                  remove_annotations=True,
                  remove_pass=True,
                  remove_literal_statements=True,
                  combine_imports=True,
                  hoist_literals=True,
                  rename_locals=True,
                  rename_globals=False,
                  remove_object_base=True,
                  convert_posargs_to_args=True,
                  preserve_shebang=False,
                  remove_asserts=True,
                  remove_debug=True)


files = glob.glob("Minified/*")
for f in files:
    os.remove(f)


print("\nFile Name           | Original Size       | Reduced Size        | Reduction")
print("————————————————————|—————————————————————|—————————————————————|——————————————")

for file_name in os.listdir("Source"):
    if file_name.endswith(".py"):
        source_path = "Source\\"+file_name
        source_file = open(source_path, "r")
        source = source_file.read()
        source_file.close()

        minified_path = "Minified\\"+file_name
        minified_source = numworks_minify(source, file_name)
        minified_file = open(minified_path, "w")
        minified_file.write(minified_source)
        minified_file.close()

        source_size = os.path.getsize(source_path)
        minified_size = os.path.getsize(minified_path)
        reduction = round(abs((minified_size-source_size)/source_size)*100)

        print(f"{file_name:<20}| ", end="")
        print(f"{source_size:<10}{'bytes':<10}| ", end="")
        print(f"{minified_size:<10}{'bytes':<10}| ", end="")
        print(f"{reduction}%")
