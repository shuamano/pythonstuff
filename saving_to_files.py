from pathlib import Path

contents = "Stuff, getting better at pytnhon\n"
contents += "more lines, the possiblites are truly endless\n"
path = Path('programming.txt')
path.write_text(contents)