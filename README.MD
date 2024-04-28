# Projekt testowania automatycznego

Projekt testowania automatycznego oparty na frameworkach `pytest` i `playwright` demonstruje testowanie funkcjonalności aplikacji webowej poprzez automatyzację przeglądarek. Zawiera testy dla różnorodnych komponentów aplikacji DEMOQA, takich jak pola tekstowe i przyciski, wykorzystując narzędzie `Allure` do generowania przejrzystych i szczegółowych raportów z wynikami testów.

## Rozpoczęcie pracy

Instrukcje te pomogą Ci skonfigurować projekt na lokalnym komputerze w celach deweloperskich i testowych, umożliwiając szybkie uruchomienie i przetestowanie aplikacji.

### Wymagania wstępne

Potrzebujesz następujących narzędzi do uruchomienia projektu:
- Python 3.12 lub nowszy
- Playwright
- Pytest
- Allure

### Instalacja

Aby przygotować środowisko, wykonaj następujące kroki:

1. Sklonuj repozytorium:
- git clone https://github.com/Oliwia8/testy_automatyczne

2. Przejdź do katalogu projektu i zainstaluj wymagane zależności:
- pip install -r requirements.txt

3. Zainstaluj Allure Report, który jest narzędziem do wizualizacji wyników testów. Wykonaj poniższe polecenia, w zależności od Twojego systemu operacyjnego:

**Dla systemów Linux:**
- sudo apt-get install allure

**Dla systemów macOS:**
- brew install allure

**Dla systemów Windows (z wykorzystaniem Scoop):**
- scoop install allure
- [https://scoop.sh/](https://scoop.sh/)

Po wykonaniu tych kroków będziesz miał/miała zainstalowane wszystkie narzędzia niezbędne do pracy z projektem.

### Uruchamianie testów

Aby uruchomić testy, wykonaj poniższe kroki:
- pytest

Możesz również uruchomić określone testy, używając:
- pytest tests/scenario_1/test_id_01.py

Dla uzyskania raportów Allure:
- pytest --alluredir=results - uruchomienie testów z wygenerowaniem plików raportu Allure. W tym przypadku zostanie utworzony katalog `results`, w którym będą przechowywane pliki wygenerowane przez Allure.
- allure serve results - uruchomienie raportu Allure. W tym przypadku zostaną uruchomione pliki znajdujące się w katalogu `results`.

## Struktura katalogów

- `tests/scenario_1/`: Katalog i podkatalog zawierający pliki testowe związane ze scenariuszem nr 1. W tym katalogu znajdują się pliki `test_id_01.py`, `test_id_02.py`, `test_id_03.py`, `test_id_04.py`, `test_id_05.py`, `test_id_06.py`;
- `tests/scenario_2/`: Katalog i podkatalog zawierający pliki testowe związane ze scenariuszem nr 2. W tym katalogu znajdują się pliki `test_id_01.py`, `test_id_02.py`, `test_id_03.py`;
- `pages/`: Katalog zawierający definicje obiektów strony (`page_objects`), takie jak `base_page_objects.py`, `buttons_page_objects.py`, `text_box_page_objects.py`.

## Opis Page Objects

Page Objects to klasy, które reprezentują strony lub ich komponenty w testach automatycznych. Każda klasa Page Object zawiera metody i lokatory specyficzne dla danej strony lub komponentu, co ułatwia organizację testów i czyni je bardziej przejrzystymi oraz łatwiejszymi w utrzymaniu.

### Przykłady

- `BasePageObject`: Bazowa klasa dla wszystkich Page Objects;
- `ButtonsPageObjects`: Obiekty strony dla testowania przycisków;
- `TextBoxPageObjects`: Obiekty strony dla testowania pól tekstowych.

## Autor

- **Oliwia Partyka** - *Testy automatyczne aplikacji DEMOQA* - [MójGitHub](https://github.com/Oliwia8/testy_automatyczne)

## Licencja

Ten projekt został stworzony jako część zadania akademickiego na uczelni WSB Merito. Nie zawiera on dedykowanego pliku `LICENSE.md`, co oznacza, że wszystkie prawa są zastrzeżone przez autora. Projekt jest udostępniony wyłącznie w celach edukacyjnych i nie może być używany, kopiowany ani modyfikowany bez wyraźnej zgody autora lub w ramach dozwolonego użytku edukacyjnego.

