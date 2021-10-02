#!python3

import io
import nbformat
import sys

filepath = "./ProjectPrannayaGuptaDraft.ipynb"

nb = (nbformat.read(filepath, 3))


headings = []
for cell in nb.worksheets[0].cells:
    if cell.cell_type == "markdown":
        headings.extend([line.lstrip().replace("# ", "", 1).replace("\t", " ").replace("#", "\t") for line in cell["source"].split("\n") if line.lstrip().startswith("#")])
        

print(*headings, sep="\n")
