from selenium.webdriver.common.by import By


class BowserWindowsPageLocators:

    NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'button[id="tabButton"]')
    TITLE_NEW_TAB_BUTTON = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'button[id="windowButton"]')
    TITLE_NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class AlertsPageLocators:
    SEE_ALERT_BUTTON = (By.CSS_SELECTOR,'button[id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.CSS_SELECTOR,'button[id="timerAlertButton"]')
    CONFIRM_BUTTON = (By.CSS_SELECTOR,'button[id="confirmButton"]')
    CONFIRM_BUTTON_RESULT = (By.CSS_SELECTOR,'span[id="confirmResult"]')
    PROMT_BUTTON = (By.CSS_SELECTOR,'button[id="promtButton"]')
    CONFIRM_PROMT_RESULT = (By.CSS_SELECTOR,'span[id="promptResult"]')

class FramePageLocators:
    FRAME_1 = (By.CSS_SELECTOR,'iframe[id="frame1"]')
    FRAME_2 = (By.CSS_SELECTOR,'iframe[id="frame2"]')
    TITLE_FRAME = (By.CSS_SELECTOR, 'h1[id="sampleHeading"]')

class TestNestedFramesPageLocators:
    PARENT_FRAME = (By.CSS_SELECTOR,'iframe[id="frame1"]')
    PARENT_FRAME_TEXT = (By.CSS_SELECTOR,'body')
    CHILD_FRAME = (By.CSS_SELECTOR,'iframe[srcdoc="<p>Child Iframe</p>"]')
    CHILD_FRAME_TEXT =(By.CSS_SELECTOR,'p')

class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showSmallModal"]')
    SMALL_MODAL_BUTTON_CLOSE = (By.CSS_SELECTOR, 'button[id="closeSmallModal"]')
    BODY_SMALL_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"]')
    TITLE_SMALL_MODAL = (By.CSS_SELECTOR, 'div[id="example-modal-sizes-title-sm"]')

    BIG_MODAL_BUTTON = (By.CSS_SELECTOR, 'button[id="showLargeModal"]')
    BIG_MODAL_BUTTON_CLOSE = (By.CSS_SELECTOR, 'button[id="closeLargeModal"]')
    BODY_BIG_MODAL = (By.CSS_SELECTOR, 'div[class="modal-body"] p')
    TITLE_BIG_MODAL = (By.CSS_SELECTOR, 'div[id = "example-modal-sizes-title-lg"]')