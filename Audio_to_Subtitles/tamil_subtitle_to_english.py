from deep_translator import GoogleTranslator
import pandas as pd

df = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Datasets\subtitle_data(tamil).csv')

# Create a Translator object
translator = GoogleTranslator(source='ta', target='en')

data = []

for filename, text in zip(df['filename'], df['subtitle']):
    # Translate the text from Tamil to English
    translated_text = translator.translate(text)
    data_dict = {'filename': filename,
                 'Tamil_subtitle': text,
                 'English_subtitle':translated_text}
    data.append(data_dict)
    print(len(data))

new_df = pd.DataFrame(data = data)
new_df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Datasets\final_dataset.csv', index = False)