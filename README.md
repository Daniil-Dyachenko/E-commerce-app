# E-Commerce-app

> Лабораторна робота №1: Контейнеризація та локальна оркестрація

---
## 1. Технологічний стек

| Компонент          |           Назва         |
|--------------------|-------------------------|
| `Backend`          | `FastAPI (Python 3.10)` |
| `Database`         | `PostgreSQL 15`         |
| `ORM`              | `SQLAlchemy + Alembic`  |
| `Containerization` | `Docker, Docker Compose`|
| `CI/CD`            | `GitHub Actions`        |


## 2. Запуск інфраструктури

Для запуску потрібно мати встановлений Docker та Docker Compose.

Виконайте команду для збірки та запуску:

```bash
docker compose up -d --build
```

Нижче видно успішний запуск контейнерів. База даних переходить у стан healthy, після чого стартує застосунок (контейнер app), який теж показує статус Up.

<img width="744" height="108" alt="image" src="https://github.com/user-attachments/assets/698c1584-6d6f-41e0-987c-e5c296440cb9" />

---
## 3.Змінні оточення

Застосунок зчитує всі налаштування бази даних зі змінних оточення.

| Змінна         | Значення за замовчуванням |
|----------------|---------------------------|
| `DB_HOST`      | `db`                      |
| `DB_PORT`      | `5432`                    |
| `DB_NAME`      | `ecommerce_db`            |
| `DB_USER`      | `postgres`                |
| `DB_PASSWORD`  | `postgres`                |

---

## ️4.Контейнеризація (Dockerfile)
Використано Multi-stage build для оптимізації розміру фінального образу.
Базовий образ — python:3.10-slim.
Застосунок запускається від не-root користувача.

---

## ️5.Оркестрація (Docker Compose)
Описано два сервіси: app (FastAPI) та db (PostgreSQL).
Налаштовано внутрішню мережу ecommerce-network для ізоляції контейнерів.
Використано depends_on з condition: service_healthy для коректного порядку запуску.

---

## 6.Стійкість та Health Check

Реалізовано ендпоінт /health, який перевіряє реальний стан з'єднання з БД.
Якщо база даних недоступна, сервіс повертає статус 503 Service Unavailable.

### Успішний статус (200 OK):
```bash
$ curl -i http://localhost:8080/health
```
<img width="978" height="221" alt="image" src="https://github.com/user-attachments/assets/1eb90866-1f07-4257-9861-b9768edc55c1" />


### Статус помилки при вимкненій БД (503 Service Unavailable):

Після зупинки PostgreSQL:

<img width="978" height="314" alt="image" src="https://github.com/user-attachments/assets/7b95757b-7807-41ae-9f88-5d6a0f37664b" />

---

## 7. Структуроване логування в JSON

Впроваджено JSON-логування для стандартного потоку виводу (STDOUT). з обов'язковими полями: `timestamp`, `level`, `message`.

<img width="977" height="77" alt="image" src="https://github.com/user-attachments/assets/6001adfa-8142-4186-8a96-f3d7549e64bb" />

---

## 8. Автоматичне оцінювання і GitHub Actions 

Надійність і правильність конфігурації підтверджується скриптом оцінювання lab1_test.sh. Проєкт містить налаштований пайплайн .github/workflows/lab1.yml. 
При кожному push у репозиторій, GitHub Actions автоматично збирає та запускає контейнери через ```docker compose``` , після цього очікує готовність системи,
тобто коли все підтягнеться і налаштується, після чого запускає скрипт tests/lab1_test.sh, за допомогою якого перевіряється правильність виконання даної Лабораторної роботи.

<img width="1543" height="465" alt="image" src="https://github.com/user-attachments/assets/577af682-e886-4135-87bf-2c471aed3255" />

---
