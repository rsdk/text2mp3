import csv
from tqdm import tqdm

from tts import tts


def load_texts(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        texts = [tuple(row) for row in reader]
    return texts


def save_mp3file(filename, mp3_bytes):
    with open(f"data_out/{filename}.mp3", "wb") as f:
        f.write(mp3_bytes)


def create_all(filepath):
    texts = load_texts(filepath)
    for filename, text in tqdm(texts):
        mp3 = tts(text, "tts-1-hd", "nova", 1)
        save_mp3file(filename, mp3)


if __name__ == '__main__':
    create_all("data_in/text.csv")
