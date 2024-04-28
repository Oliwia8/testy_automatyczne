import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Testowanie długości pola - wprowadzenie jednego znaku')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Sprawdzenie zachowania systemu przy '
                    'wprowadzeniu jednego znaku do pól tekstowych.\n\n**Oczekiwany rezultat:** System powinien '
                    'prawidłowo przetwarzać bardzo krótkie wpisy.')
@allure.tag('1')
def test_ID_04(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Wprowadź tekst składający się z 1 znaku w każde pole tekstowe.'):
            name = 'a'
            full_name_input = text_box_page_objects.FULL_NAME_INPUT.find_element_by_placeholder(browser)
            full_name_input.fill(name)

            email = 'a@gmail.com'
            email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)
            email_input.fill(email)

            current_address = 'd'
            current_address_textarea = text_box_page_objects.CURRENT_ADDRESS_TEXTAREA.find_element_by_placeholder(browser)
            current_address_textarea.fill(current_address)

            permanent_address = 'c'
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

        # Sprawdzenie, czy system przetwarza prawidłowo krótkie wpisy.
        assert (name in name_input_result and email in email_input_result and current_address
                in current_address_textarea_result and permanent_address in permanent_address_textarea_result)

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError as e:
        raise AssertionError(f'Brak oczekiwanego rezultatu. System nie przetwarza prawidłowo bardzo krótkich '
                             f'wpisów.\n\n{str(e)}')
