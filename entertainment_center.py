import fresh_tomatoes
import media
Venom = media.Movie(
             "Venom",
             """Development of a Venom film, a spin-off from the Spider-Man
             film franchise""",
             "Venom_official_teaser_poster.jpg",
             "https://www.youtube.com/watch?v=dzxFdtWmjto")

Hindi_Medium = media.Movie(
                    "Hindi Medium",
                    """Raj and Mita yearn to get Pia their daughter educated
                    from a reputed school.When they learn that their
                    background is holding her back, they are willing to go
                    to any lengths to change her fate.""",
                    "Hindi_Medium_Poster.jpg",
                    "https://www.youtube.com/watch?v=GjkFr48jk68")

A_Wrinkle_in_Time = media.Movie(
                    "A Wrinkle in Time",
                    """After learning her astrophysicist father Alex is being
                    held captive on a distant planet deep in the grip of a
                    universe-spanning evil, Meg Murry works with her highly
                    intelligent younger brother, her new friend and fellow
                    student Calvin O'Keeffe, and three astral travelers,
                    Mrs. Which, Mrs. Whatsit and Mrs.
                    Who to save him.""",
                    "AWrinkleInTimeTeaser.jpg",
                    "https://www.youtube.com/watch?v=E4U3TeY2wtM")

Boss_Baby = media.Movie(
                "Boss Baby",
                """The plot follows a baby who is a secret agent in the war
                for adult's love between babies
                and puppies.""",
                "The_Boss_Baby_poster.jpg",
                "https://www.youtube.com/watch?v=WGNwOoWnOMw")

Skyscraper = media.Movie(
                  "Skyscraper",
                  """Skyscraper is an upcoming American action thriller film
                  directed and written by Rawson M. Thurber.""",
                  "Skyscraper_(2018)_film_poster.png",
                  "https://www.youtube.com/watch?v=r-b7Fy_CXpQ")

H_T3 = media.Movie(
                    "Hotel Transylvania 3",
                    """The story centers on Dracula, Mavis, Johnny and the
                    rest of their family, both human and monster, and
                    friends as they take a vacation on a luxury Monster
                    Cruise Ship, where Dracula falls head-over-heels in love
                    with the ship's mysterious captain, Ericka, who is
                    secretly the descendant of Abraham Van Helsing, the
                    notorious monster slayer and Dracula's ancient
                    archenemy.""",
                    "Hotel_Transylvania_3_(2018)_Poster.jpg""",
                    "https://www.youtube.com/watch?v=d5exSS74Lh0")


movies = [Venom, Hindi_Medium, A_Wrinkle_in_Time, Boss_Baby, Skyscraper, H_T3]


fresh_tomatoes.open_movies_page(movies)
