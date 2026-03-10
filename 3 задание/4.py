from typing import List, Union

# Базовый класс "Товар"
class Product:
    tax_rate: float = 0.20          # налог 20%
    available_formats: List[str] = ["physical", "digital"]

    def __init__(self, title: str, price: float, publisher: str):
        self.title = title
        self.price = price
        self.publisher = publisher

    def __str__(self) -> str:
        return f"{self.title} (изд. {self.publisher}) - {self.price} руб."

    def apply_discount(self, percent: float) -> None:
        if percent < 0 or percent > 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")
        self.price *= (1 - percent / 100)

    def is_expensive(self, threshold: float = 5000) -> bool:
        return self.price > threshold


# Дочерний класс "Игра для PS5"
class PS5Game(Product):
    platform: str = "PS5"
    allowed_ratings: List[str] = ["0+", "6+", "12+", "16+", "18+"]   # возрастные рейтинги

    def __init__(self, title: str, price: float, publisher: str,
                 genre: str, year: int, rating: str, disk_type: str = "Blu-ray"):
        super().__init__(title, price, publisher)
        self.genre = genre
        self.year = year
        self.rating = rating
        self.disk_type = disk_type

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base} | Жанр: {self.genre}, {self.year} г., рейтинг: {self.rating}, диск: {self.disk_type}"

    def is_rated_for_age(self, age: int) -> bool:
        rating_num = int(self.rating.replace('+', ''))
        return age >= rating_num

    def update_rating(self, new_rating: str) -> None:
        if new_rating not in PS5Game.allowed_ratings:
            raise ValueError(f"Недопустимый рейтинг. Разрешены: {PS5Game.allowed_ratings}")
        self.rating = new_rating

    def check_genre(self, genre_list: List[str]) -> bool:
        return self.genre in genre_list


# Создание нескольких объектов
game1 = PS5Game("God of War Ragnarök", 4999, "Sony",
                "Action", 2022, "18+")
game2 = PS5Game("Ratchet & Clank: Rift Apart", 3999, "Sony",
                "Platformer", 2021, "12+", "Blu-ray")
game3 = PS5Game("Horizon Forbidden West", 4499, "Sony",
                "RPG", 2022, "16+")

print(game1)
print(game2)
print(game3)

print(f"\n{game1.title} дорогая? {game1.is_expensive(4000)}")
game2.apply_discount(15)
print(f"После скидки 15%: {game2}")

age = 14
print(f"{game3.title} подходит для {age} лет? {game3.is_rated_for_age(age)}")

game1.update_rating("16+")
print(f"Новый рейтинг {game1.title}: {game1.rating}")

if game3.check_genre(["RPG", "Adventure"]):
    print(f"{game3.title} - это RPG!")