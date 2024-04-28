import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Testowanie pola tekstowego (Text Box)')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Weryfikacja funkcjonalności pola tekstowego.'
                    '\n\n**Oczekiwany rezultat:** Dane powinny zostać wysłane, a odpowiedź powinna zawierać prawidłowo '
                    'wprowadzone informacje.')
@allure.tag('1')
def test_ID_01(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Wpisz imię i nazwisko w pole "Full Name".'):
            name = 'Oliwia Partyka'
            full_name_input = text_box_page_objects.FULL_NAME_INPUT.find_element_by_placeholder(browser)
            full_name_input.fill(name)

        with allure.step('2. Wpisz e-mail w pole "Email".'):
            email = 'oliwia_partyka@gmail.com'
            email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)
            email_input.fill(email)

        with allure.step('3. Wpisz aktualny adres w pole "Current Address".'):
            current_address = 'ul. Żeromskiego 9, 50-321 Wrocław'
            current_address_textarea = text_box_page_objects.CURRENT_ADDRESS_TEXTAREA.find_element_by_placeholder(browser)
            current_address_textarea.fill(current_address)

        with allure.step('4. Wpisz stały adres w pole "Permanent Address".'):
            permanent_address = 'ul. Jedności Narodowej 20, 50-260 Wrocław'
            permanent_address_textarea = text_box_page_objects.PERMANENT_ADDRESS_TEXTAREA.find_element_by_locator(browser)
            permanent_address_textarea.fill(permanent_address)

        with allure.step('5. Kliknij przycisk "Submit".'):
            submit_button = text_box_page_objects.SUBMIT_BUTTON.find_element_by_role(browser)
            submit_button.click()

        name_input_result = text_box_page_objects.NAME_INPUT_RESULT.find_element_by_locator(browser).text_content()
        email_input_result = text_box_page_objects.EMAIL_INPUT_RESULT.find_element_by_locator(browser).text_content()
        current_address_textarea_result = (text_box_page_objects.CURRENT_ADDRESS_TEXTAREA_RESULT.
                                           find_element_by_locator(browser).text_content())
        permanent_address_textarea_result = (text_box_page_objects.PERMANENT_ADDRESS_TEXTAREA_RESULT.
                                             find_element_by_locator(browser).text_content())

        # Sprawdzenie, czy dane zostaną wysłane i czy odpowiedź zawiera prawidłowo wprowadzone informacje.
        assert (name in name_input_result and email in email_input_result and current_address in
                current_address_textarea_result and permanent_address in permanent_address_textarea_result)

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError as e:
        raise AssertionError(f'Brak oczekiwanego rezultatu. Dane nie zostały wysłane lub odpowiedź nie zawiera '
                             f'prawidłowo wprowadzonych informacji.\n\n{str(e)}')




