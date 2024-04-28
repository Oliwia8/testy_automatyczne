class Locator:
    def __init__(self, by, locator):
        self.locator = locator
        self.by = by

    def find_element_by_role(self, page):
        return page.get_by_role(self.by, name=self.locator, exact=True)

    def find_element_by_locator(self, page):
        return page.locator(self.locator)

    def find_element_by_text(self, page):
        return page.get_by_text(self.locator)

    def find_element_by_placeholder(self, page):
        return page.get_by_placeholder(self.locator)


class BasePageObject:
    def __init__(self, page):
        self.page = page

    @property
    def default_url(self):
        raise NotImplementedError

    def goto(self):
        self.page.goto(self.default_url)


