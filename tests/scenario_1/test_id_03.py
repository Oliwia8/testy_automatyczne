import allure
from playwright.sync_api import TimeoutError


@allure.suite('SCENARIUSZ NR 1 "Weryfikacja walidacji danych wejściowych w polu tekstowym"')
@allure.title('Weryfikacja walidacji niepoprawnych danych wejściowych')
@allure.description('**Autor:** Oliwia Partyka\n\n**Środowisko:** Windows 11 Pro, Google Chrome Wersja 124.0.6367.61 '
                    '(Oficjalna wersja) (64-bitowa)\n\n**Warunki wstępne:** Użytkownik znajduje się na podstronie '
                    '„Text Box” https://demoqa.com/text-box\n\n**Cel:** Sprawdzenie, czy pole "Email" nie akceptuje '
                    'niepoprawnego adresu e-mail.\n\n**Oczekiwany rezultat:** System nie powinien pozwolić na wysłanie '
                    'formularza z niepoprawnym adresem e-mail.')
@allure.tag('1')
def test_ID_03(text_box_page_objects, browser):
    try:
        with allure.step('Kroki testowe:'):
            text_box_page_objects.goto()

        with allure.step('1. Wprowadź niepoprawny adres e-mail do pola "Email" (np. example.com).'):
            email = 'oliwia.o2.pl'
            email_input = text_box_page_objects.EMAIL_INPUT.find_element_by_placeholder(browser)
            email_input.fill(email)

        with allure.step('2. Kliknij przycisk "Submit".'):
            submit_button = text_box_page_objects.SUBMIT_BUTTON.find_element_by_role(browser)
            submit_button.click()

        expected_class = 'mr-sm-2 field-error form-control'

        # Sprawdzenie, czy system nie pozwoli na wysłanie formularza z niepoprawnym adresem e-mail.
        assert expected_class in email_input.get_attribute('class')

    except TimeoutError:
        assert False, 'Timeout: Strona nie została załadowana lub element nie został znaleziony na stronie.'
    except AssertionError as e:
        raise AssertionError(f'Brak oczekiwanego rezultatu. System pozwala na wysłanie formularza z niepoprawnym '
                             f'adresem e-mail.\n\n{str(e)}')
