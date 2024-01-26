import requests
import pandas as pd 

df = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Datasets\scraped_data.csv')

for i, url in enumerate(df['audio_url']):
    audio_content = requests.get(url).content

    with open(f'F:\\GUVI_DATA_SCIENCE\\Project\\Extraction-of-Audios-Subtitles\\Audio_files\\audio{i+1}.mp3', 'wb') as f:
        f.write(audio_content)
    
    print('Audio_dowloaded_successfully : ', i+1)