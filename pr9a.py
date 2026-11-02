# Rule-Based Recommendation System - CinemiX Movie Recommendation System
# Rules: filter movies by genre, language and minimum rating given by the user.

movies = [
    {"name": "Inception",        "genre": "scifi",   "lang": "english", "rating": 8.8},
    {"name": "Interstellar",     "genre": "scifi",   "lang": "english", "rating": 8.6},
    {"name": "The Dark Knight",  "genre": "action",  "lang": "english", "rating": 9.0},
    {"name": "War",              "genre": "action",  "lang": "hindi",   "rating": 6.5},
    {"name": "3 Idiots",         "genre": "comedy",  "lang": "hindi",   "rating": 8.4},
    {"name": "Hera Pheri",       "genre": "comedy",  "lang": "hindi",   "rating": 8.2},
    {"name": "The Conjuring",    "genre": "horror",  "lang": "english", "rating": 7.5},
    {"name": "Stree",            "genre": "horror",  "lang": "hindi",   "rating": 7.5},
    {"name": "Titanic",          "genre": "romance", "lang": "english", "rating": 7.9},
    {"name": "Dilwale Dulhania Le Jayenge", "genre": "romance", "lang": "hindi", "rating": 8.0},
]

print("=== Welcome to CinemiX ===")
genre = input("Genre (action/comedy/scifi/horror/romance): ").lower().strip()
lang = input("Language (english/hindi): ").lower().strip()
min_rating = float(input("Minimum rating (e.g. 7.0): "))

results = []
for m in movies:
    if m["genre"] == genre and m["lang"] == lang and m["rating"] >= min_rating:   # rule
        results.append(m)

print("\nRecommended movies:")
if results:
    for m in sorted(results, key=lambda x: x["rating"], reverse=True):
        print(f"- {m['name']} (Rating: {m['rating']})")
else:
    print("No exact match. Try lowering the rating or changing the language.")