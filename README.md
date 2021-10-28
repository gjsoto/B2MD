# B2MD
Converts entries in a bib file to markdown language for my website

## Requirements

Make sure your Python environment has the [bibtexparser](https://bibtexparser.readthedocs.io/en/master/) package installed. 

## Usage

In a terminal or command prompt, navigate to the "B2MD" directory. Typical call would be:
  > python   parser.py   filepath   author

The call to the script takes in two arguments: `filepath` and `author`. Both are strings; the former is the filepath to the bib file, the latter is the name of the main author (e.g. "Soto, G. J." which is formatted as *Last Name*, *First Name* with optional middle initial).

The data in the .bib file entries is formatted into the Markdown language. The final formatted entries are written to a .txt file with the same name as the .bib file in the `/outputs` directory. 
