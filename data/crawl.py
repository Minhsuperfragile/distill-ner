from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

LINK = "https://fdvn.vn/tong-hop-50-mau-hop-dong-thong-dung-nhat-viet-nam-nam-2024/"
driver = webdriver.Edge()

try:
    driver.get(LINK)
except WebDriverException as e:
    print(f'Error : {e.msg}')

div = "div[class='entry-content --custom']"

div_content = driver.find_element(By.CSS_SELECTOR, div)

ps = div_content.find_elements(By.TAG_NAME, 'p')

links = []
texts = []

for paragraph in ps:
    try:
        a = paragraph.find_element(By.TAG_NAME, 'a')
        link = a.get_attribute('href')
        if "doc" in link[-4:]:
            links.append(link)
        else: continue
        texts.append(a.text)
    except NoSuchElementException as e:
        continue

texts = [text.replace('(', '').replace(')', '').replace(',', '') for text in texts]

import subprocess
files = []
for text, link in zip(texts, links):
    ext = link.split(".")[-1]
    text = text.replace(" ", "_")
    print(" ".join(['wget', '-O', f"{text}.{ext}", link]))
    result = subprocess.run(["powershell", 'wget', '-O', f".\\docs\\{text}.{ext}", link], capture_output=True, text=True)
    files.append(f".\\docs\\{text}.{ext}")

driver.close()