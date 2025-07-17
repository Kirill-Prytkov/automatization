import time

from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_forms()
            assert full_name == output_name, "full_name incorrect"
            assert email == output_email, "email incorrect"
            assert current_address == output_cur_addr, "cur_adr incorrect"
            assert permanent_address == output_per_addr, "per adr incorrect"