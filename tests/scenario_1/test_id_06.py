import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Testowanie reakcji na puste pola')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Weryfikacja zachowania systemu przy braku '
                    'danych wejściowych.\n\n**Oczekiwany rezultat:** System powinien wymagać wypełnienia wymaganych '
                    'pól.')
@allure.tag('1')
def test_ID_06(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Pozostaw wszystkie pola tekstowe puste.'):
            with allure.step('2. Kliknij przycisk "Submit".'):
                submit_button = text_box_page_objects.SUBMIT_BUTTON.find_element_by_role(browser)
                submit_button.click()

        email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)

        # Sprawdzenie, czy system będzie wymagał wypełnienia wymaganych pól. Ze względu na to, że waliduje się tylko
        # pole "Email", to pole bierzemy pod uwagę przy weryfikacji zachowania systemu.
        assert 'error' in email_input.get_attribute('class')

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError:
        raise AssertionError('Brak oczekiwanego rezultatu. System nie wymaga wypełnienia wymaganych pól.')

