from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("the file cant be found.") #you can also just write 'pass' to do nothing
    else:
        words = contents.split()
        number_of_words = len(words)
        print(f"The file {path} has {number_of_words} words.")


count_words(Path('text_files/treasure_island.txt'))
