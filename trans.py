import argparse
import wanakana
from googletrans import Translator

def romaji_to_kana(romaji):
    kana = wanakana.to_hiragana(romaji)
    return kana

def translate_to_english(kana):
    translator = Translator()
    translation = translator.translate(kana, src='ja', dest='en')
    return translation.text

def main():
    parser = argparse.ArgumentParser(description="Translate Romaji to Kana and provide English translation.")
    parser.add_argument("text", type=str, help="The Romaji text to translate.")
    
    args = parser.parse_args()
    romaji_text = args.text
    
    # Convert Romaji to Kana
    kana_text = romaji_to_kana(romaji_text)
    
    # Translate Kana to English
    english_translation = translate_to_english(kana_text)
    
    # Output the results
    print(f"Romaji: {romaji_text}")
    print(f"Kana: {kana_text}")
    print(f"English Translation: {english_translation}")

if __name__ == "__main__":
    main()
