import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code
from selenium.webdriver import Keys
import data

class UrbanRoutesPage:

     # Addresses
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')
     #Tariff
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    TAXI_ICON_LOCATOR = (By.XPATH, '//*[@id="root"]/div[3]/div[1]/div[2]/div[3]/img')
    CALL_A_TAXI_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
    SUPPORTIVE_PLAN_LOCATOR = (By.XPATH, "//div[text()='Supportive]")
     #Phone Number
    PHONE_LOCATOR = (By.CLASS_NAME, 'np-text')
    PHONE_NUMBER_FIELD_LOCATOR = (By.XPATH, '//div[text()="Phone number"]')
    PHONE_NUMBER = (By.XPATH, '/[div@class="np_button"//div[contains(text)(),"Phone number)]')
    PHONE_FIELD_LOCATOR = (By.ID, "phone")
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    PHONE_CODE_LOCATOR = (By.ID, 'code')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Confirm"]')
     #Credit Card
    PAYMENT_METHOD_LOCATOR = (By.CSS_SELECTOR, 'div.pp-value-text')
    ADD_CARD_LOCATOR = (By.XPATH, '//div[contains(text(), "Add card")]')
    CARD_NUMBER_LOCATOR = (By.ID, 'number')
    CARD_CODE_LOCATOR = (By.CSS_SELECTOR, '#code.card-input')
    LINK_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, '//*[@id=root"]/div/div[2]/div[2]/div[1]/button')
    DRIVER_MESSAGE_FIELD_LOCATOR = (By.ID, 'comment')
    MODAL_WINDOW_LOCATOR_LOCATOR = (By.CLASS_NAME, 'modal')
     #Order
    BLANKET_HANDKERCHIEF_LOCATOR = (By.XPATH, '(//span@class="slider round"])[1]')
    ICE_CREAM_LOCATOR = (By.CLASS_NAME, '//div@class= "r-counter-label"]//div[text(), "Ice cream"]')
    ICE_CREAM_PLUS_BUTTON_LOCATOR = (By.CLASS_NAME, 'counter-plus')
    ICE_CREAM_COUNTER_VALUE_LOCATOR = (By.XPATH, '//div[@class="counter-value"]')
    ICE_CREAM_BUCKET_BUTTON_LOCATOR = (By.XPATH, '//div[text()="Ice Cream Bucket"]')
    ORDER_BUTTON_LOCATOR = (By.XPATH, '//span[@class="smart-button-main"]')
    IS_PLAN_SELECTED = (By.CSS_SELECTOR, "tcard.active .tcard-title")
    BLANKET_HANDKERCHIEF_CHECK_LOCATOR = (By.CLASS_NAME, "switch-input")
    MODAL_WINDOW_LOCATOR = (By.XPATH, "//div[text()='Car search']")



    def __init__(self, driver):
        self.driver = driver

    def enter_from_address(self, from_address):
         self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_address(self, to_address):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_address(self):
         return self.driver.find_element(*self.FROM_FIELD).get_attribute('value')

    def get_to(self):
         return self.driver.find_element(*self.TO_FIELD).get_attribute('value')

    def get_selected_plan(self):
        return self.driver.find_element(*self.IS_PLAN_SELECTED).text

    def click_custom_option(self):
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_taxi_icon(self):
        self.driver.find_element(*self.TAXI_ICON_LOCATOR).click()

    def click_call_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON_LOCATOR).click()

    def select_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).click()

    def get_current_selected_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_LOCATOR).text

    def set_phone(self, phone_number):
        self.click_phone_number_field()
        self.driver.find_element(*self.PHONE_FIELD_LOCATOR).send_keys(phone_number)
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()
        self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(retrieve_phone_code(self.driver))
        self.driver.find_element(*self.CONFIRM_BUTTON_LOCATOR).click()

    def click_phone_number_field(self):
        self.driver.find_element(*self.PHONE_NUMBER_FIELD_LOCATOR).click()

    def enter_phone_number(self):
         self.driver.find_element(*self.PHONE_NUMBER_INPUT).send_keys(data.PHONE_NUMBER)

    def get_phone(self):
        return self.driver.find_element(*self.PHONE_LOCATOR).text

    def click_next_button(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).send_keys()

    def enter_phone_code(self):
        code = retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_CODE_LOCATOR).send_keys(code)

    def click_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).click()

    def click_add_card(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.ADD_CARD_LOCATOR)).click()

    def enter_card_number(self, CARD_NUMBER):
        self.driver.find_element(*self.CARD_NUMBER_LOCATOR).send_keys(CARD_NUMBER)

    def enter_card_code(self, CARD_CODE):
        self.driver.find_element(*self.CARD_CODE_LOCATOR).send_keys(CARD_CODE)

    def click_link_button(self):
        self.driver.find_element(*self.LINK_BUTTON_LOCATOR).click()

    def click_close_button(self):
        self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR).click()

    def get_payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).get_property('value')

    def click_driver_message_field(self):
        self.driver.find_element(*self.DRIVER_MESSAGE_FIELD_LOCATOR).click()

    def set_message_for_driver(self,message):
        self.driver.find_element(*self.DRIVER_MESSAGE_FIELD_LOCATOR).send_keys(message)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.DRIVER_MESSAGE_FIELD_LOCATOR).get_attribute('value')

    def enter_driver_message(self):
        message_field = self.driver.find_element(*self.DRIVER_MESSAGE_FIELD_LOCATOR)
        message_field.send_keys(message)

    def get_modal_window(self):
        modal = self.driver.find_element(*self.MODAL_WINDOW_LOCATOR)
        return 'displayed' if modal.is_displayed() else 'not displayed'

    def click_blanket_handkerchiefs(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.BLANKET_HANDKERCHIEF_LOCATOR)).click()

    def get_blanket_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_LOCATOR).get_attribute('value')

    def set_ice_cream_counter(self, AMOUNT):
        ice_cream_counter_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.ICE_CREAM_PLUS_BUTTON_LOCATOR))
        for _ in range(amount):
            ice_cream_counter_button.click()

    def get_ice_cream_counter(self):
        counter_value = self.driver.find_element(*self.ICE_CREAM_COUNTER_VALUE_LOCATOR).text
        return int(counter_value)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_LOCATOR).click()

    def set_route(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()

    def get_from(self):
         return self.driver.find_element(*self.FROM_LOCATOR).get_attribute("value")

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute("value")


def set_card(self, card, cvv):
    self.click_payment_method()
    self.click_add_card()
    self.enter_card_number(card)
    self.enter_card_code(cvv)
    self.enter_card_code(Keys.TAB)
    self.click_link_button()

    def get_current_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_LOCATOR).text

    def get_blanket_and_handkerchief_option(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEF_CHECK_LOCATOR).get_property("checked")