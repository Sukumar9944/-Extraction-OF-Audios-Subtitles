from pydub import AudioSegment
import os

directory_path = 'F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Audio_files'

files = os.listdir(directory_path)

for i, file in enumerate(files):
    full_file_path = os.path.join(directory_path, file)
    
    sound = AudioSegment.from_mp3(full_file_path)
    sound.export(f'F:\\GUVI_DATA_SCIENCE\\Project\Extraction-of-Audios-Subtitles\\Audio_files\\wav_converted_files\\audio{i+1}.wav', format = 'wav')
    
    print('Audio_converted_successfully : ', i+1)