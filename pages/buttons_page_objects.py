from pages.base_page_objects import BasePageObject, Locator


class ButtonsPageObjects(BasePageObject, Locator):

    @property
    def default_url(self):
        return 'https://demoqa.com/buttons'

    CLICK_ME_BUTTON = Locator("button", 'Click Me')
    CLICK_ME_TEXT = Locator(None, "You have done a dynamic click")

    RIGHT_CLICK_ME_BUTTON = Locator("button", "Right Click Me")
    RIGHT_CLICK_ME_TEXT = Locator(None, "You have done a right click")

    DOUBLE_CLICK_ME_BUTTON = Locator("button", "Double Click Me")
    DOUBLE_CLICK_ME_TEXT = Locator(None, "You have done a double click")
