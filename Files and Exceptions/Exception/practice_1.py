from pathlib import Path

def count_words(filenames):
    try:
        file_content = filenames.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        file_location = Path(filenames)
        file_content_length = len(file_content)
        print(f"\n The file {filenames} has about {file_content_length} words")

filenames = ["alicewonderland.txt", "camping.txt", "money_mind.txt", "trending.txt"]
for filename in filenames:
    file_location = Path(filename)
    count_words(file_location)