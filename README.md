# E-Commerce-app

> Підготовка застосунку — Readiness & Standardization

---

## 1.Збірка та запуск

Для локального розгортання застосунку необхідно мати встановлені **Python** та **Docker** (для запуску бази даних).

**Крок 1. Запуск бази даних PostgreSQL у Docker:**
```bash
docker start my-postgres
```

**Крок 2. Встановлення залежностей:**
```bash
pip install -r requirements.txt
```

**Крок 3. Запуск сервера:**
```bash
uvicorn src.main:app --port 8080
```
**Крок 4. Запустити юніт-тести:**
```bash
pytest
```

## 2.Конфігурація через середовище (12-Factor App)

Застосунок зчитує всі налаштування бази даних зі змінних оточення. Жодні чутливі дані не захардкоджені в сирцевому коді.

| Змінна         | Значення за замовчуванням |
|----------------|---------------------------|
| `DB_HOST`      | `127.0.0.1`               |
| `DB_PORT`      | `5433`                    |
| `DB_NAME`      | `ecommerce_db`            |
| `DB_USER`      | `postgres`                |
| `DB_PASSWORD`  | `postgres`                |

---

## ️3.Автоматичне керування схемою БД

При запуску застосунок автоматично перевіряє та застосовує всі наявні міграції до бази даних за допомогою інструменту Alembic.

Ручний запуск SQL-скриптів **не потрібен**.

<img width="930" height="152" alt="image" src="https://github.com/user-attachments/assets/71c0bc92-4dfb-4c14-89c9-179d3216b1a7" />

---

## 4."Глибока" перевірка стану (Dependency-Aware Health Checks)

**Ендпоінт:** /health перевіряє не лише роботу самого сервера, а й доступність бази даних PostgreSQL.

### Успішний статус (200 OK):
```bash
$ curl -i http://localhost:8080/health
```
<img width="832" height="203" alt="image" src="https://github.com/user-attachments/assets/8bfb541a-da28-487f-917d-287693b8951d" />


### Статус помилки при вимкненій БД (503 Service Unavailable):

Після зупинки PostgreSQL:

<img width="818" height="198" alt="image" src="https://github.com/user-attachments/assets/53828f6b-981a-4078-990b-175795205d7a" />

---

## 5. Структуроване логування в JSON

Під час запуску застосунку в **STDOUT** виводяться JSON-об'єкти з обов'язковими полями: `timestamp`, `level`, `message`.

<img width="930" height="152" alt="image" src="https://github.com/user-attachments/assets/ed5c42ee-b468-4f0c-af4a-4febae20deb2" />

---

## 6. Плавне завершення роботи (Graceful Shutdown)
Застосунок коректно обробляє сигнал SIGTERM/SIGINT (Ctrl+C). Він завершує обробку поточних запитів та безпечно закриває всі з'єднання з базою даних.

<img width="936" height="51" alt="image" src="https://github.com/user-attachments/assets/f829c573-c8e9-4331-820e-3e1c84ad22d1" />


## 7.Юніт-тести

Завдяки налаштованому файлу pytest.ini, усі CRUD операції та перевірка стану (health check) перевіряються однією стандартною командою:
```bash
pytest
```

<img width="978" height="432" alt="image" src="https://github.com/user-attachments/assets/389b566a-febb-430f-b68a-93dbb9f70e83" />


---
