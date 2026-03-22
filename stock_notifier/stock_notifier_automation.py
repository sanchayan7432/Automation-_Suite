from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import yagmail

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("--headless")  # Run in headless mode for background execution

    # Automatically download the correct version
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
     
    return driver

def get_rate():
    driver = get_driver()
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    time.sleep(2) 
    #element = driver.find_element(By.CSS_SELECTOR, ".stock-trend.trend-grow")

    element=driver.find_element(By.CLASS_NAME, "stock-trend").text
    element=float(element.replace('−', '-').replace(',', '').replace('%', '').strip())

    # Wait for the page to load completely
  #  element = driver.find_element(By.XPATH, "/html/body/div[1]/div/section[1]/div/div/div[2]/span[2]")  
    return element

def send_email(rate):
    sender_email = "ghoshsanchayan485@gmail.com"

    receiver_email = "sanchayan7432@gmail.com"

    subject = "Current Stock Rate Notification"

    content=f"""
    The current stock rate is {rate}%.
    This is an automated notification sent using yagmail.

    """

    yag = yagmail.SMTP(user=sender_email, password="Enter app password")

    print("Waiting for 60 seconds before sending the email...")
    time.sleep(60)  # Wait for 60 seconds
    yag.send(to=receiver_email, subject=subject, contents=content)
    print("Email sent successfully!")
          
def main():
    rate = get_rate()
    print(f"Current stock rate: {rate}%")
    if rate==0.06:
        send_email(rate)
main()