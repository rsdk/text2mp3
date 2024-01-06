import time

from openai import OpenAI
from dotenv import load_dotenv
from openai import RateLimitError
from time import sleep

load_dotenv()
client = OpenAI()


def tts(text, model="tts-1", voice="nova", speed=1) -> bytes:
    """
    Text to speech

    https://platform.openai.com/docs/api-reference/audio/createSpeech
    https://platform.openai.com/docs/guides/text-to-speech
    languages: Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.
       You can generate spoken audio in these languages by providing the input text in the language of your choice.

    models: tts-1, tts-1-hd
    voices: alloy, echo, fable, onyx, nova, and shimmer
    formats: mp3, opus, aac, and flac

    :param text:
    :return:
    """
    try:
        speech = client.audio.speech.create(
            input=text,
            model=model,
            voice=voice,
            response_format="mp3",
            speed=speed  # 0.25 to 4.0
        )
    except RateLimitError as e:
        print(f" Rate Limit Exceeded. Trying again in 30 seconds... ({e})")
        time.sleep(30)
        return tts(text, model=model, voice=voice)
    return speech.content
