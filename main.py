"""
src/main.py
Główny punkt wejścia do aplikacji CineStream (Event Loop z match-case).
"""

from data import MOVIES_CATALOG
from validators import get_int_input
from services import display_movies, add_movie, filter_movies_by_genre

def print_menu() -> None:
    """Wyświetla główne menu konsolowe aplikacji."""
    print("\n" + "=" * 40)
    print("      CINESTREAM - MENADŻER VOD      ")
    print("=" * 40)
    print("1. Wyświetl katalog filmów")
    print("2. Dodaj nowy film")
    print("3. Filtruj filmy po gatunku")
    print("4. Wyjście z programu")
    print("-" * 40)

def handle_menu_choice(choice: str, movies: list) -> bool:
    """Obsługuje routing opcji menu za pomocą konstrukcji match-case."""
    match choice.strip():
        case "1":
            display_movies(movies)
        case "2":
            add_movie(movies)
        case "3":
            filter_movies_by_genre(movies)
        case "4" | "q" | "exit":
            print("\nZamykanie systemu CineStream. Do widzenia!")
            return False
        case _:
            print("\n[Błąd] Nieznana opcja. Wybierz wartość od 1 do 4.")
    return True

def main():
    """Główna funkcja sterująca działaniem aplikacji."""
    running = True
    while running:
        print_menu()
        user_choice = input("Wybierz opcję [1-4]: ")
        running = handle_menu_choice(user_choice, MOVIES_CATALOG)

if __name__ == "__main__":
    main()