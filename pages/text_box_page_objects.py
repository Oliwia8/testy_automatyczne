from pages.base_page_objects import BasePageObject, Locator


class TextBoxPageObjects(BasePageObject, Locator):

    @property
    def default_url(self):
        return 'https://demoqa.com/text-box'

    FULL_NAME_INPUT = Locator(None, 'Full Name')
    EMAIL_INPUT = Locator(None, 'name@example.com')
    CURRENT_ADDRESS_TEXTAREA = Locator(None, 'Current Address')
    PERMANENT_ADDRESS_TEXTAREA = Locator(None, '#permanentAddress')
    SUBMIT_BUTTON = Locator('button', 'Submit')

    NAME_INPUT_RESULT = Locator(None, "xpath=//p[@id='name']")
    EMAIL_INPUT_RESULT = Locator(None, "xpath=//p[@id='email']")
    CURRENT_ADDRESS_TEXTAREA_RESULT = Locator(None, "xpath=//p[@id='currentAddress']")
    PERMANENT_ADDRESS_TEXTAREA_RESULT = Locator(None, "xpath=//p[@id='permanentAddress']")


