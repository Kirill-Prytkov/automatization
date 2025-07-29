import random
import time

from locators.alerts_frame_windows_page_locatoirs import BowserWindowsPageLocators, AlertsPageLocators, \
    FramePageLocators, TestNestedFramesPageLocators, ModalDialogsPageLocators
from pages.base_page import BasePage


class BrowserWindowsPage(BasePage):

    locators = BowserWindowsPageLocators

    def check_opened_new_tab(self):
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB_BUTTON).text
        return text_title

    def check_opened_new_window(self):
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB_BUTTON).text
        return text_title

class AlertsPage(BasePage):

    locators = AlertsPageLocators

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(6)
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def check_alert_confirm(self):
        self.element_is_visible(self.locators.CONFIRM_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_BUTTON_RESULT).text
        return text_result

    def check_promt_alert(self):
        text = f"autotest{random.randint(0,9999)}"
        self.element_is_visible(self.locators.PROMT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.CONFIRM_PROMT_RESULT).text
        return text, text_result

class FramePage(BasePage):

    locators = FramePageLocators

    def check_frames(self, frame_num):
       if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FRAME_1)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.driver.switch_to.frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [text, width,height]

       if frame_num == 'frame2':
           frame = self.element_is_present(self.locators.FRAME_2)
           width = frame.get_attribute('width')
           height = frame.get_attribute('height')
           self.driver.switch_to.frame(frame)
           text = self.element_is_present(self.locators.TITLE_FRAME).text
           return [text, width, height]

class TestNestedFramesPage(BasePage):

    locators = TestNestedFramesPageLocators

    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.element_is_present(self.locators.PARENT_FRAME_TEXT).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.driver.switch_to.frame(child_frame)
        child_text = self.element_is_present(self.locators.CHILD_FRAME_TEXT).text
        return parent_text, child_text

class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators

    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small = self.element_is_visible(self.locators.BODY_SMALL_MODAL).text
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON_CLOSE).click()
        self.element_is_visible(self.locators.BIG_MODAL_BUTTON).click()
        title_big = self.element_is_visible(self.locators.TITLE_BIG_MODAL).text
        body_big = self.element_is_visible(self.locators.BODY_BIG_MODAL).text
        self.element_is_visible(self.locators.BIG_MODAL_BUTTON_CLOSE)
        return [title_small, len(body_small)], [title_big, len(body_big)]




