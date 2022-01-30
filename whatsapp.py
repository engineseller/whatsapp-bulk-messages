#!/bash/python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import pandas

excel_data = pandas.read_excel('receiver.xlsx', sheet_name='Receivers')

count = 0

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')

input("Press ENTER after login into Whatsapp Web and your chats are visible.")

for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + str(excel_data['Contact'][count]) + '&text=' + excel_data['Message'][0]
        sent = False

        driver.get(url)

        try:
            click_btn = WebDriverWait(driver, 35).until(EC.element_to_be_clickable((By.CLASS_NAME, '_4sWnG')))
        except Exception as e:
            print("Message could not sent to " + str(excel_data['Contact'][count]) + str(e))
        else:
            sleep(2)
            click_btn.click()
            sent = True
            sleep(5)
            print('Message sent to: ' + str(excel_data['Contact'][count]))

        count = count + 1
    except Exception as e:
        print('Failed to send message to ' + str(excel_data['Contact'][count]) + str(e))

driver.quit()

print("The script executed successfully.")
