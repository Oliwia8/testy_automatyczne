import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Weryfikacja walidacji poprawnych danych wejściowych')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Sprawdzenie, czy pole "Email" akceptuje '
                    'poprawnie sformatowany adres e-mail.\n\n**Oczekiwany rezultat:** System powinien akceptować '
                    'poprawny adres e-mail.')
@allure.tag('1')
def test_ID_02(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Wprowadź poprawny adres e-mail do pola "Email" (np. "example@example.com").'):
            email = 'oliwia_partyka@gmail.com'
            email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)
            email_input.fill(email)

        with allure.step('2. Kliknij przycisk "Submit".'):
            submit_button = text_box_page_objects.SUBMIT_BUTTON.find_element_by_role(browser)
            submit_button.click()

        email_input_result = text_box_page_objects.EMAIL_INPUT_RESULT.find_element_by_locator(browser).text_content()

        # Sprawdzenie, czy system akceptuje poprawny adres e-mail.
        assert email in email_input_result

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError as e:
        raise AssertionError(f'Brak oczekiwanego rezultatu. System nie akceptuje poprawnego adresu e-mail.\n\n{str(e)}')
