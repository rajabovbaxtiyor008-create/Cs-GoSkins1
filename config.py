import os

# ==========================
# Telegram
# ==========================

BOT_TOKEN = os.getenv("BOT_TOKEN")

# ==========================
# Database
# ==========================

DATABASE_NAME = "cs2_shop.db"

# ==========================
# Валюта
# ==========================

CURRENCY = "🪙"

START_BALANCE = 1000

# ==========================
# Кейсы
# ==========================

CASES = {
    "Revolution Case": 250,
    "Kilowatt Case": 300,
    "Dreams & Nightmares Case": 220,
    "Fracture Case": 180,
    "Recoil Case": 200,
    "Snakebite Case": 190,
    "Prisma 2 Case": 170,
    "CS20 Case": 260,
    "Clutch Case": 150,
    "Danger Zone Case": 160
}

# ==========================
# Шансы выпадения
# ==========================

DROP_CHANCES = {
    "Consumer Grade": 35.0,
    "Industrial Grade": 25.0,
    "Mil-Spec": 20.0,
    "Restricted": 10.0,
    "Classified": 6.0,
    "Covert": 3.0,
    "Knife": 0.7,
    "Gloves": 0.3
}

# ==========================
# Продажа
# ==========================

SELL_PERCENT = 0.90

# ==========================
# Администраторы
# ==========================

ADMINS = [
    8287231977  # Замени на свой Telegram ID
]
