import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 2 "Testowanie reakcji na interakcje z przyciskami"')
@allure.title('Testowanie reakcji na standardowe kliknięcie')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Buttons” https://demoqa.com/buttons\n\n**Cel:** Sprawdzenie działania systemu po standardowym '
                    'kliknięciu przycisku.\n\n**Oczekiwany rezultat:** System powinien wyświetlić komunikat '
                    'potwierdzający wykonanie kliknięcia.')
@allure.tag('2')
def test_ID_01(buttons_page_objects, browser):
    with allure.step('Kroki testowe:'):
        buttons_page_objects.goto()

    with allure.step('1. Kliknij przycisk "Click Me".'):
        try:
            buttons_page_objects.CLICK_ME_BUTTON.find_element_by_role(browser).click()
            expected_text = 'You have done a dynamic click'
            current_text = buttons_page_objects.CLICK_ME_TEXT.find_element_by_text(browser).text_content()

            # Sprawdzenie, czy wyświetli się komunikat potwierdzający wykonanie kliknięcia.
            assert current_text == expected_text

        except TimeoutError:
            assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
        except AssertionError as e:
            raise AssertionError(f'Brak oczekiwanego rezultatu. System nie wyświetlił komunikatu potwierdzającego '
                                 f'wykonanie kliknięcia.\n\n{str(e)}')
