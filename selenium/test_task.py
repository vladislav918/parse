import time
import csv

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from selenium_stealth import stealth

from seleniumwire import webdriver

from bs4 import BeautifulSoup

from environs import Env


env = Env()
env.read_env()


def get_driver_chrome():
    try:
        chrome_options = Options()

        chrome_options.add_extension(env.str("PATH_EXTENSIONS"))

        driver = webdriver.Chrome(
            options=chrome_options,
        )

        stealth(
            driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

        return driver
    except Exception as e:
        print(f"Ошибка при создании драйвера Chrome: {str(e)}")


def connect_vpn(driver):
    try:
        popupPage = "chrome-extension://fcfhplploccackoneaefokcmbjfbkenj/popup.html"
        driver.get(popupPage)

        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if driver.current_url != popupPage:
                driver.close()

        driver.switch_to.window(driver.window_handles[0])

        first_element = driver.find_element(By.XPATH, "(//li)[1]")
        first_element.click()

        time.sleep(5)
    except Exception as e:
        print(f"Ошибка при подключении VPN: {str(e)}")


def navigate_to_page_and_perform_actions(driver):
    try:
        driver.get("https://www.nseindia.com")
        time.sleep(5)

        market_data_element = driver.find_element(By.LINK_TEXT, 'MARKET DATA')
        hover = ActionChains(driver).move_to_element(market_data_element)
        hover.perform()
        time.sleep(2)

        pre_open_market_element = driver.find_element(By.LINK_TEXT, 'Pre-Open Market')
        pre_open_market_element.click()
    except Exception as e:
        print(f"Ошибка при навигации и выполнении действий: {str(e)}")


def parse_data(driver):
    try:
        time.sleep(15)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table')
        rows = table.find_all('tr')[1:]
        extracted_data = []

        for row in rows:
            cells = row.find_all('td') 
            name = cells[1].get_text(strip=True).strip(':').strip() if cells[1].text else ''
            last_price = cells[6].get_text(strip=True).replace(',', '') if cells[6].text else ''
  
            extracted_data.append({
                'name': name,
                'final_price': float(last_price) if last_price else None
            })

        save_to_csv(extracted_data)
    except Exception as e:
        print(f"Ошибка при парсинге данных: {str(e)}")


def save_to_csv(extracted_data):
    with open('market_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'final_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in extracted_data:
            writer.writerow(data)

        print(f"Данные сохранены в файл market_data.csv")


def simulate_user_actions(driver):
    market_data_element = driver.find_element(By.LINK_TEXT, 'MARKET DATA')
    hover = ActionChains(driver).move_to_element(market_data_element)
    hover.perform()
    time.sleep(2)
    
    pre_open_market_element = driver.find_element(By.LINK_TEXT, 'Indices')
    pre_open_market_element.click()
    time.sleep(15)

    table_element = driver.find_element(By.TAG_NAME, "table")
    sectoral_indices = driver.find_element(By.ID, "sectoralindices")

    driver.execute_script("arguments[0].scrollTop = arguments[1];", table_element, sectoral_indices.location['y'])
    time.sleep(16)

    nifty_bank_element = driver.find_element(By.XPATH, "//td[@headers='sectoralindices indexCol']//a[text()='NIFTY BANK']")
    nifty_bank_element.click()
    time.sleep(20)


def main():
    driver = get_driver_chrome()
    connect_vpn(driver)
    navigate_to_page_and_perform_actions(driver)
    parse_data(driver)
    simulate_user_actions(driver)
    driver.quit()


if __name__ == '__main__':
    main()
