# Simple Text to MP3
with openai API

## Setup
Python > 3.10
### Libraries
- openai
- python-dotenv
- tqdm

### OpenAI Key
Setup your openai Key as ENV Variable or in a .env file.
https://platform.openai.com/docs/quickstart/step-2-setup-your-api-key

## Usage
main.py 
Speech model, Speaker and speed can be adjusted

    mp3 = tts(text, "tts-1-hd", "nova", 1)
### Text to be converted
data_in/text.csv

- First column is the file name to bne created.
- Second column is the Text to be sopken.


    welcome_de;Willkommen, ich hoffe du hast Spaß beim Lernen.
    welcome_en;Welcome, I hope you have fun while learning.
    welcome_fr;Bienvenue, j'espère que tu prendras plaisir à étudier.
    welcome_it;Benvenuto, spero che ti piaccia imparare.
    welcome_pl;Witaj, mam nadzieję, że spodoba ci się nauka.

### MP3
Will be created in data_out as .mp3 files.

## Examples

The data_out folder has five example mp3s which were generated with the text.csv from the data_in folder.