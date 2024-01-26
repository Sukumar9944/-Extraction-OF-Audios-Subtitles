from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd


# To prevent the browser from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Define a Driver
driver = webdriver.Chrome(options=options)

# To maximize the window
driver.maximize_window()

data_list = []

driver.get('https://www.freetamilringtones.com/tamil-movie-dialogues-ringtones-free-download/category/175-tamil-dialogue-mp3-ringtones-free-download')

time.sleep(10)

actors_list = ['- Ajith', '- Dhanush', '- Kamal Haasan', '- Rajini-Kanth', '- Simbu', '- Sivakarthikeyan', '- Surya', '- Vijay', '- Vijay Sethupathi']

try:
    for actor in actors_list:
        actors_dropdown_locater = driver.find_element(By.ID, 'cat_list')
        actors_dropdown_selector = Select(actors_dropdown_locater)
        actors_dropdown_selector.select_by_visible_text(actor)

        audio_url_locater = driver.find_elements(By.CLASS_NAME, 'sm2_link')

        category_locater = driver.find_element(By.CLASS_NAME, 'jd_files_subheader_title')

        try:
            for i in audio_url_locater:
                audio_href = i.get_attribute('href')
                
                data = {'Category': category_locater.text,
                        'audio_url': audio_href}
                
                data_list.append(data)

        except:
            print('Error Handled')
            pass
        
        print('Number of elements located : ', len(audio_url_locater))
        print('Data Extracted Successfully')
        
except:
    print('An Error Occured')

            
finally:
    driver.close()


df = pd.DataFrame(data = data_list)
df.to_csv('F:\GUVI_DATA_SCIENCE\Project\Extraction-of-Audios-Subtitles\Datasets\scraped_data.csv', index = False)