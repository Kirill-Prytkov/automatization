from pages.alerts_frame_windows_page import BrowserWindowsPage, AlertsPage, FramePage, TestNestedFramesPage, \
    ModalDialogsPage


class TestAlertsFrameWindow:

    class TestBrowserWindows:
        def test_new_tab(self,driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_result = browser_window_page.check_opened_new_tab()
            assert text_result == "This is a sample page"


        def test_new_window(self,driver):
            browser_window_page = BrowserWindowsPage(driver, "https://demoqa.com/browser-windows")
            browser_window_page.open()
            text_windows_result = browser_window_page.check_opened_new_window()
            assert text_windows_result == "This is a sample page"

    class TestAlertsPage:

        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == "You clicked a button"

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds"

        def test_alert_confirm(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_confirm()
            assert alert_text == "You selected Ok"

        def test_alert_promt(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, alert_text = alert_page.check_promt_alert()
            assert text in alert_text

class TestFrames:

    def test_frames(self, driver):
        frame_page = FramePage(driver, 'https://demoqa.com/frames')
        frame_page.open()
        result_frame_1 = frame_page.check_frames('frame1')
        result_frame_2 = frame_page.check_frames('frame2')
        #assert result_frame_1 == ['This is a sample page', '500px', '350px']
        #assert result_frame_2 == ['This is a sample page', '100px', '100px']
        assert result_frame_1 != result_frame_2

class TestNestedFrames:

        def test_nested_frames(self, driver):
            nested_frame_page = TestNestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == "Parent frame"
            assert child_text == "Child Iframe"

class TestModalDialogs:
    def test_modal_dialogs(self, driver):
        modal_dialog_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
        modal_dialog_page.open()
        small, large = modal_dialog_page.check_modal_dialogs()
        assert small[1] < large[1]
        assert small[0] == 'Small Modal'
        assert large[0] == 'Large Modal'