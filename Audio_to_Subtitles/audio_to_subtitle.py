import speech_recognition as sr
import os
import pandas as pd 

directory_path = 'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Audio_files\wav_converted_files'

files = os.listdir(directory_path)

# initialize the recognizer
recognizer = sr.Recognizer()

# Audio file --> Audio Data --> Text
data_list = []

try:
    for file in files:
            full_file_path = os.path.join(directory_path, file)
            audio_file = sr.AudioFile(full_file_path)

            with audio_file as source:
                audio_data = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio_data, language = 'ta-IN')
                
                data_dict = {'filename': file,
                            'subtitle': text}
                
                print(data_dict)
                
                data_list.append(data_dict)

                print(len(data_list))
            except:
                print('Error handled')
                pass
except:
    print('An error occured')

finally:
    print('Subtitle obtained Successfully')

df = pd.DataFrame(data = data_list)
df.to_csv(r'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Datasets\final_dataset.csv', index = False)