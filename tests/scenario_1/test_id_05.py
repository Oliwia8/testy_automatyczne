import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Testowanie długości pola - wprowadzenie 100 znaków')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Sprawdzenie zachowania systemu przy '
                    'wprowadzeniu 100 znaków do pól tekstowych.\n\n**Oczekiwany rezultat:** System powinien prawidłowo '
                    'przetwarzać bardzo długie wpisy, o ile nie przekraczają ustawionych ograniczeń.')
@allure.tag('1')
def test_ID_05(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Wprowadź bardzo długi tekst składający się ze 100 znaków w każde pole tekstowe.'):
            name = 'n' * 100
            full_name_input = text_box_page_objects.FULL_NAME_INPUT.find_element_by_placeholder(browser)
            full_name_input.fill(name)

            email = 'm' * 100 + '@gmail.com'
            email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)
            email_input.fill(email)

            current_address = 'j' * 100
            current_address_textarea = text_box_page_objects.CURRENT_ADDRESS_TEXTAREA.find_element_by_placeholder(browser)
            current_address_textarea.fill(current_address)

            permanent_address = 'a' * 100
            permanent_address_textarea = text_box_page_objects.PERMANENT_ADDRESS_TEXTAREA.find_element_by_locator(browser)
            permanent_address_textarea.fill(permanent_address)

        with allure.step('2. Kliknij przycisk "Submit".'):
            submit_button = text_box_page_objects.SUBMIT_BUTTON.find_element_by_role(browser)
            submit_button.click()

        name_input_result = text_box_page_objects.NAME_INPUT_RESULT.find_element_by_locator(browser).text_content()
        email_input_result = text_box_page_objects.EMAIL_INPUT_RESULT.find_element_by_locator(browser).text_content()
        current_address_textarea_result = (text_box_page_objects.CURRENT_ADDRESS_TEXTAREA_RESULT.
                                           find_element_by_locator(browser).text_content())
        permanent_address_textarea_result = (text_box_page_objects.PERMANENT_ADDRESS_TEXTAREA_RESULT.
                                             find_element_by_locator(browser).text_content())

        # Sprawdzenie, czy system prawidłowo przetworzy tak długie wpisy.
        assert (name in name_input_result and email in email_input_result and current_address
                in current_address_textarea_result and permanent_address in permanent_address_textarea_result)

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError:
        raise AssertionError('Brak oczekiwanego rezultatu. System nie przetwarza prawidłowo tak długich wpisów.')
