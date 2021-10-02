#!python3

import io
import nbformat
import sys

#Word counter for jupyter notebooks! 

filepath = "Light Pollution - How Far Has It Gone.ipynb"

nb = (nbformat.read(filepath, 3))


number_of_words = 0
for cell in nb.worksheets[0].cells:
    if cell.cell_type == "markdown":
        number_of_words += len(cell['source'].replace('#', '').lstrip().split(' '))

print(number_of_words)
