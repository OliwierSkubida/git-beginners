"""
src/services.py
Logika biznesowa: wyświetlanie, dodawanie oraz filtrowanie filmów.
"""

from validators import get_non_empty_string, get_int_input, get_float_input


def display_movies(movies: list) -> None:
    """Wyświetla sformatowaną tabelę filmów w konsoli przy użyciu f-stringów."""
    if not movies:
        print("\n[Brak filmów w bazie CineStream]")
        return

    print("\n" + "=" * 85)
    print(f"| {'ID':<3} | {'Tytuł filmu':<30} | {'Gatunek':<12} | {'Rok':<4} | {'Ocena':<5} | {'Platforma':<12} |")
    print("=" * 85)

    for m in movies:
        print(
            f"| {m['id']:<3} | {m['title']:<30} | {m['genre']:<12} | {m['year']:<4} | {m['rating']:<5.1f} | {m['platform']:<12} |")
    print("=" * 85)


def add_movie(movies: list) -> None:
    """Interaktywny formularz dodawania nowego filmu do bazy."""
    print("\n--- DODAWANIE NOWEGO FILMU DO CINESTREAM ---")

    # Wygenerowanie unikalnego ID (maksymalne dotychczasowe ID + 1)
    new_id = max((m["id"] for m in movies), default=0) + 1

    title = get_non_empty_string("Podaj tytuł filmu: ")
    genre = get_non_empty_string("Podaj gatunek (np. Sci-Fi, Dramat): ")
    year = get_int_input("Podaj rok premiery (1900-2030): ", min_val=1900, max_val=2030)
    rating = get_float_input("Podaj ocenę (0.0 - 10.0): ", min_val=0.0, max_val=10.0)
    platform = get_non_empty_string("Podaj platformę VOD (np. Netflix, HBO Max): ")

    new_movie = {
        "id": new_id,
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating,
        "platform": platform
    }

    movies.append(new_movie)
    print(f"\n[Sukces] Film '{title}' został pomyślnie dodany do katalogu (ID: {new_id})!")


def filter_movies_by_genre(movies: list) -> None:
    """Proste filtrowanie filmów po gatunku."""
    if not movies:
        print("\n[Brak filmów do przefiltrowania]")
        return

    search_genre = get_non_empty_string("Podaj gatunek do wyszukania: ").lower()
    filtered = [m for m in movies if search_genre in m["genre"].lower()]

    if not filtered:
        print(f"\n[Informacja] Nie znaleziono filmów dla gatunku: '{search_genre}'")
    else:
        print(f"\n--- Wyniki filtrowania dla gatunku: '{search_genre}' ---")
        display_movies(filtered)