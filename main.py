from urllib.request import urlopen
import pyautogui as pya
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def Zapychacz(x):
    time.sleep(x)

def Polacz():
    url = webdriver.Chrome()
    url.get('https://6obcy.org/rozmowa')
    assert "6obcy.org" in url.title
    inputChe = url.find_element(By.CLASS_NAME, "caper-solution-input")
    inputChe.clear()
    inputChe.send_keys(Input())
    inputChe.send_keys(Keys.RETURN)

    ButtonChe = url.find_element(By.XPATH, '//button[contains(text(),"Zatwierdź")]')
    ButtonChe.click()

    Zapychacz(3)
    Napisz(url,  "box-interface-input", "Hej, jestem P.E.A.C.O.C.K (Paw). Taki sobie, nikomu nie szkodzący bocik. Proszę cię popisz ze mną")
    Zapychacz(5)
    lit = 0
    while True:
        if lit==0:
            if Pobierz(url).lower() == "m":
                Napisz(url, "box-interface-input", "k")
                lit+=1
            else:
                Pisarz(url)
                tempX = Pobierz(url)
                lit+=1
                print(Pobierz(url))
        if lit==1:
            if tempX!=Pobierz(url):
                print(Pobierz(url))
                lit-=1


    Zapychacz(120)

    assert "No results found." not in url.page_source

def Konwerter(x):
    x = x.lower()

    x = x.replace("e", "u")
    x = x.replace("w", "g")

    x = x[::-1]

    return x

def Pobierz(url):
    y = url.find_elements(By.CLASS_NAME, "log-stranger")
    x = y[len(y)-1].find_element(By.XPATH, ".//span[@class='log-msg-text']").text
    return str(x)


def Napisz(url, name, text):
    TextInput = url.find_element(By.ID, name)
    TextInput.send_keys(text)
    TextInput.send_keys(Keys.ENTER)
    pass

def Pisarz(url):
    Napisz(url, "box-interface-input", Konwerter(Pobierz(url)))

def Input():
    x = input("Podaj Sentencje:")
    return x

Polacz()