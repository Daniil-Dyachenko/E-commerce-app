# E-Commerce-app

> Лабораторна робота №2: Автоматизація CI/CD та робота з container registry

---
## 1. CI/CD Pipeline:
Налаштовано GitHub Actions workflow у файлі .github/workflows/pipeline.yml

Нижче видно успішне виконання всього пайплайну (збірка, сканування та тестування):

<img width="977" height="242" alt="image" src="https://github.com/user-attachments/assets/90930cd4-5745-4fc3-b31b-9b3f23f512b2" />

---
## 2. Container Registry:

Образи автоматично публікуються виключно в GitHub Container Registry (ghcr.io).

---

## 3. Іменування образу:

Налаштовано автоматичне приведення імені репозиторію до нижнього регістру. Образ зберігається у форматі ghcr.io/<username>/ecommerce-app

<img width="978" height="188" alt="image" src="https://github.com/user-attachments/assets/2b4bd7aa-56d6-4eaf-84b4-e80f8f812baf" />

---

## 4. Tagging Strategy:

При кожному успішному запуску пайплайну створюються та публікуються два теги: latest та унікальний sha - <git-commit-hash>

<img width="977" height="73" alt="image" src="https://github.com/user-attachments/assets/1213917e-8d09-4ac8-8c25-0097993aa43f" />

<img width="978" height="393" alt="image" src="https://github.com/user-attachments/assets/532957b7-3034-4a7e-b2da-4f5b68f420f3" />

---

## 5. Security Scan і Permissions & Auth:

До пайплайну інтегровано сканер Trivy для автоматичної перевірки Docker-образу на наявність вразливостей перед релізом.
Також було надано права```packages```: ```write``` для ```GITHUB_TOKEN```. Для авторизації в ghcr.io використовується ```docker/login-action```.

---

## 6. Автоматичне оцінювання і GitHub Actions 

Надійність і правильність конфігурації підтверджується скриптом оцінювання lab2_test.sh. Він перевіряє доступність пакету у GHCR через GitHub API, 
наявність обов'язкового тегу latest, а також унікального тегу sha. 

<img width="976" height="336" alt="image" src="https://github.com/user-attachments/assets/14379717-5670-4b7d-875a-ea96371727a3" />


<img width="799" height="81" alt="image" src="https://github.com/user-attachments/assets/79838a05-f9c2-41ee-a57f-e729dac43b38" />

---

## 7. Завантаження та запуск готового образу з GHCR

1. Авторизація в GHCR:
```bash
docker login ghcr.io -u daniil-dyachenko
```

2. Завантаження образу:
```bash
docker pull ghcr.io/daniil-dyachenko/ecommerce-app:latest
```

3. Запуск застосунку:
```bash
docker run -p 8080:8080 ghcr.io/daniil-dyachenko/ecommerce-app:latest
```
---
