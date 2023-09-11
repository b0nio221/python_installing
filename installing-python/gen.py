from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


username = "31urbo748"
passwd = "pfhmm"


browser = webdriver.Chrome()


browser.get('https://instaling.pl/teacher.php?page=login')


username_input = browser.find_element(By.ID, "log_email")
password_input = browser.find_element(By.ID, "log_password")
submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")


username_input.send_keys(username)
password_input.send_keys(passwd)

submit_button.click()

browser.implicitly_wait(10)

start_sesji = browser.find_element(By.PARTIAL_LINK_TEXT, 'sesj')
start_sesji.click()

kont_sesji = browser.find_element(By.ID, "continue_session_button")
zacz_sesji = browser.find_element(By.ID, "start_session_button")
if kont_sesji.is_displayed():
    kont_sesji.click()
if zacz_sesji.is_displayed():
    zacz_sesji.click()
with open('slowa.json', 'r') as f:
    data1 = json.loads(f.read())

#slowo polskie ktore zczytujemy

pl_word = browser.find_element(By.CLASS_NAME, "translations")
pl1_word = pl_word.text
word_found = False
for element in data1:
    if pl1_word in str(element.values()):
        word_found = True
        break

#jezeli znajdzie slowo

if word_found:
    print("git")
    answer_input = browser.find_element(By.ID, "answer")
    check = browser.find_element(By.ID, "check")
    check.click()

#jezeli nie znajdzie slowa

else:
    print("zle")
    slowo = []
    slowo.append({"pl_word": pl1_word, })
    with open('slowa.json','w') as e:
        json.dump(slowo, f)
    check = browser.find_element(By.ID, "check")
    check.click()
    time.sleep(100)



