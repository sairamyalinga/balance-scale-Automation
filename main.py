from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import ast

try:
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("http://sdetchallenge.fetch.com/")

    
    driver.find_element(By.ID, "left_0").send_keys(0)
    driver.find_element(By.ID, "left_1").send_keys(1)
    driver.find_element(By.ID, "left_2").send_keys(2)
    driver.find_element(By.ID, "right_0").send_keys(3)
    driver.find_element(By.ID, "right_1").send_keys(4)
    driver.find_element(By.ID, "right_2").send_keys(5)
    
    
    weigh = driver.find_element(By.ID, "weigh")
    weigh.click()
    eq = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//ol//li[1]"))
    )
    print(eq.text)
    tt = eq.text

    print(driver.find_element(By.ID, "reset"))
    driver.find_element(By.ID, "reset").click()

    if "=" in tt:
        driver.find_element(By.XPATH, "//*[text()='Reset']").click()
        driver.find_element(By.ID, "left_0").send_keys(6)
        driver.find_element(By.ID, "right_0").send_keys(7)
        weigh.click()
        neweq = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//ol//li[2]")))
        if neweq:
            ntt = neweq.text
            if "=" in ntt:
                div_coins = driver.find_element(By.CLASS_NAME, "coins")
                button = div_coins.find_element(
                        By.XPATH, ".//button[text()='8']")
                button.click()
            else:
                if "<" in ntt:
                    div_coins = driver.find_element(By.CLASS_NAME, "coins")
                    button = div_coins.find_element(
                        By.XPATH, ".//button[text()='6']")
                    button.click()
                if ">" in ntt:
                    div_coins = driver.find_element(By.CLASS_NAME, "coins")
                    button = div_coins.find_element(
                        By.XPATH, ".//button[text()='7']")
                    button.click()
        else:
            print("None found")
            driver.quit()
    if "<" in tt:
        expressions = tt.split("<")
        lhs = expressions[0].strip()
        lhs = ast.literal_eval(lhs)
        driver.find_element(By.XPATH, "//*[text()='Reset']").click()
        driver.find_element(By.ID, "left_0").send_keys(lhs[0])
        driver.find_element(By.ID, "right_0").send_keys(lhs[1])
        weigh.click()
        neweq = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ol//li[2]")))
        ntt = neweq.text
        if "=" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{lhs[2]}']")
            button.click()
        if "<" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{lhs[0]}']")
            button.click()
        if ">" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{lhs[1]}']")
            button.click()
    if ">" in tt:
        expressions = tt.split(">")
        rhs = expressions[1].strip()
        print(rhs)
        rhs = ast.literal_eval(rhs)
        driver.find_element(By.XPATH, "//*[text()='Reset']").click()
        driver.find_element(By.ID, "left_0").send_keys(rhs[0])
        driver.find_element(By.ID, "right_0").send_keys(rhs[1])
        weigh.click()
        neweq = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//ol//li[2]")))
        ntt = neweq.text
        if "=" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{rhs[2]}']")
            button.click()
        if "<" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{rhs[0]}']")
            button.click()
        if ">" in ntt:
            div_coins = driver.find_element(By.CLASS_NAME, "coins")
            button = div_coins.find_element(
                By.XPATH, f".//button[text()='{rhs[1]}']")
            button.click()


except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    time.sleep(100)
    print(driver.title)
    print(driver.current_url)
    driver.quit()
