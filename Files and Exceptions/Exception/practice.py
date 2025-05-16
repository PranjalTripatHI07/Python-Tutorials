from pathlib import Path

def Count_words(filename):
    """This Function Count the total number of words in a file."""

    try:
        file_content = filename.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"\n  Sorry {filename} file is not found.")

    else:
        file_content_length = len(file_content)
        print(f"\n The file {filename} has about {file_content_length} words")

#Now for multiple files
filenames= ["camping.txt", "money_mind.txt", "trending.txt", "alicewonderland.txt"]

for filename in filenames:
    file_path = Path(filename)
    Count_words(file_path)
