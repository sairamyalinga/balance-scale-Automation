import time
import ast
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Function to press reset 
def reset_button():
    driver.find_element(By.XPATH, "//*[text()='Reset']").click()

# Function to get equation of balance scale
def get_equation(n):
    eq = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//ol//li[{n}]")))
    return eq.text

# Function to add gold bar to the balance scale
def add_element(id, key):
    driver.find_element(By.ID, id).send_keys(key)

# Function to click the result button
def result(ans):
    div_coins = driver.find_element(By.CLASS_NAME, "coins")
    button = div_coins.find_element(
                    By.XPATH, f".//button[text()='{ans}']")
    button.click()
    write_to_file(ans)

# Function to write to the output.txt file 
def write_to_file(ans):
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    time.sleep(5)
    alert.accept()
    with open('output.txt', 'w') as f:
        f.write(alert_text + '\n')
        f.write(f'The fake gold bar is number {ans}\n')
        weighings = driver.find_elements(By.XPATH, "//ol//li")
        f.write(f'Number of weighing is {len(weighings)}\n')
        for index, item in enumerate(weighings, start=1):
            f.write(f"Weighing {index}: {item.text}\n")
    driver.quit()

try:
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("http://sdetchallenge.fetch.com/")  
    add_element("left_0", 0)
    add_element("left_1", 1)
    add_element("left_2", 2)
    add_element("right_0", 3)
    add_element("right_1", 4)
    add_element("right_2", 5)
    weigh = driver.find_element(By.ID, "weigh")
    weigh.click()
    tt = get_equation(1)
    if "=" in tt:
        reset_button()
        add_element("left_0", 6)
        add_element("right_0", 7)
        weigh.click()
        ntt = get_equation(2)   
        if "=" in ntt:
            result(8)
        if "<" in ntt:
            result(6)
        if ">" in ntt:
            result(7)

    if "<" in tt:
        expressions = tt.split("<")
        lhs = expressions[0].strip()
        lhs = ast.literal_eval(lhs)
        reset_button()
        add_element("left_0", lhs[0])
        add_element("right_0", lhs[1])
        weigh.click()
        ntt =get_equation(2)
        if "=" in ntt:
            result(lhs[2])
        if "<" in ntt:
            result(lhs[0])
        if ">" in ntt:
           result(lhs[1])
    if ">" in tt:
        expressions = tt.split(">")
        rhs = expressions[1].strip()
        print(rhs)
        rhs = ast.literal_eval(rhs)
        reset_button()
        add_element("left_0", rhs[0])
        add_element("right_0", rhs[1])
        weigh.click()
        ntt = get_equation(2)
        if "=" in ntt:
            result(rhs[2])    
        if "<" in ntt:
            result(rhs[0])
        if ">" in ntt:
            result(rhs[1])
            
except Exception as e:
    logging.error(f"An error occurred: {str(e)}")

