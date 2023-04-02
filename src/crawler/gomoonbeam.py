import time
import src.config as config
from src.crawler.core import driver
from selenium.webdriver.common.by import By


def sign_in(url: str,
            email: str,
            password: str) -> None:
    driver.get(url)

    time.sleep(15)

    try:
        email_address_box = driver.find_element(by=By.NAME,
                                                value='identifier')
        email_address_box.send_keys(email)

        password_box = driver.find_element(by=By.NAME,
                                           value='password')
        password_box.send_keys(password)
    except:
        return

    continue_button = driver.find_element(by=By.XPATH,
                                          value='//*[@id="__next"]/div/div/div/div/div[3]/form/button[2]')
    continue_button.click()

    time.sleep(25)


def navigate_user_to_templates(url: str) -> None:
    driver.get(url)

    time.sleep(10)


def select_essay_writer() -> None:
    essay_button = driver.find_element(by=By.XPATH,
                                       value='//*[@id="modal-root"]/div[1]/div/div/div[2]/div/div/div[2]/div/button[1]')
    essay_button.click()

    time.sleep(20)


def fill_essay_with_custom_input_step_1(title: str,
                                        description: str,
                                        keywords: list) -> None:
    title_box = driver.find_element(by=By.XPATH,
                                    value='//*[@id="modal-root"]/div[1]/div/div/div[1]/div[2]/div/h1')
    title_box.send_keys(title)

    description_box = driver.find_element(by=By.XPATH,
                                          value='//*[@id="modal-root"]/div[1]/div/div/div[1]/div[3]/div')
    description_box.send_keys(description)

    keywords_box = driver.find_element(by=By.XPATH,
                                       value='//*[@id="modal-root"]/div[1]/div/div/div[1]/div[4]/div/ul/li/p')
    keywords_box.send_keys(', '.join(keywords))

    scroll_down()

    time.sleep(15)

    generate_essay_button = driver.find_element(by=By.XPATH,
                                                value='//*[@id="modal-root"]/div[1]/div/div/div[2]/button')

    time.sleep(15)

    generate_essay_button.click()

    time.sleep(15)


def fill_essay_with_custom_input_step_2() -> None:
    scroll_down()

    time.sleep(15)

    create_point_button = driver.find_element(by=By.XPATH,
                                              value='//*[@id="modal-root"]/div[1]/div/div/div[2]/button')

    time.sleep(15)

    create_point_button.click()

    time.sleep(15)


def fill_essay_with_custom_input_step_3() -> None:
    scroll_down()

    time.sleep(15)

    finish_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="modal-root"]/div[1]/div/div/div[2]/div[2]/button')

    time.sleep(20)

    finish_button.click()

    time.sleep(15)


def fill_essay_with_custom_input_step_4():
    scroll_down()

    time.sleep(15)

    with open(config.BASE_DIR + "/result/index.html", "w") as file:
        file.write(driver.page_source)

    time.sleep(10)


def scroll_down():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
