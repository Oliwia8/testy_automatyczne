# Projekt testowania automatycznego

Projekt testowania automatycznego oparty na `pytest` i `playwright` demonstruje testowanie funkcjonalności stron internetowych poprzez automatyzację przeglądarek. Zawiera testy dla różnych komponentów strony, takich jak pola tekstowe i przyciski, oraz używa `Allure` do raportowania wyników testów.

## Rozpoczęcie pracy

Instrukcje te pomogą Ci skonfigurować projekt na lokalnym komputerze do celów deweloperskich i testowych.

### Wymagania wstępne

Potrzebujesz następujących narzędzi do uruchomienia projektu:
- Python 3.8 lub nowszy
- Playwright
- Pytest
- Allure

### Instalacja

Aby przygotować środowisko, wykonaj następujące kroki:

1. Sklonuj repozytorium:
- git clone https://github.com/Oliwia8/testy_automatyczne

2. Przejdź do katalogu projektu i zainstaluj wymagane zależności:
- pip install -r requirements.txt

3. Zainstaluj Allure Report, który jest narzędziem do wizualizacji wyników testów. Wykonaj poniższe polecenia w zależności od Twojego systemu operacyjnego:

**Dla systemów Linux:**
- sudo apt-get install allure

**Dla systemów macOS:**
- brew install allure

**Dla systemów Windows (z wykorzystaniem Scoop):**
- scoop install allure

Po wykonaniu tych kroków będziesz miał zainstalowane wszystkie narzędzia niezbędne do pracy z projektem.

### Uruchamianie testów

Aby uruchomić testy, wykonaj poniższe kroki:
- pytest

Możesz również uruchomić określone testy, używając:
- pytest tests/test_id_01.py

Dla uzyskania raportów Allure:
- pytest --alluredir=/path/to/results - uruchomienie testów z wygenerowaniem plików raportu Allure
- allure serve /path/to/results - uruchomienie raportu Allure


## Struktura katalogów

- `tests/`: Katalog zawierający pliki testowe `test_id_01.py`, `test_id_02.py`, ..., `test_id_06.py`.
- `pages/`: Katalog zawierający definicje obiektów strony (`page_objects`) takie jak `base_page_objects.py`, `buttons_page_objects.py`, `text_box_page_objects.py`.

## Opis Page Objects

Page Objects to klasy, które reprezentują strony lub komponenty strony w testach. Każda klasa Page Object zawiera metody i lokatory specyficzne dla danej strony, co ułatwia organizację testów i czyni je bardziej przystępnymi.

### Przykłady

- `BasePageObject`: Bazowa klasa dla wszystkich Page Objects.
- `ButtonsPageObjects`: Obiekty strony dla testowania przycisków.
- `TextBoxPageObjects`: Obiekty strony dla testowania pól tekstowych.

## Autor

- **Oliwia Partyka** - *NAZWA TWOJEGO PROJEKTU* - [MójGitHub](https://github.com/Oliwia8/testy_automatyczne)

## Licencja

Ten projekt został stworzony jako część zaliczenia akademickiego na uczelni WSB Merito. Nie zawiera on dedykowanego pliku `LICENSE.md`, co oznacza, że wszystkie prawa są zastrzeżone przez autora. Projekt jest udostępniony wyłącznie w celach edukacyjnych i nie może być używany, kopiowany ani modyfikowany bez wyraźnej zgody autora lub w ramach dozwolonego użytku edukacyjnego.

