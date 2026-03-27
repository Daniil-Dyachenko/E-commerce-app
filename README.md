# E-Commerce-app

> Лабораторна робота №3: Kubernetes Deployment Essentials

---
## 1. Кластеризація

Використовується KinD (Kubernetes in Docker) для локального тестування та в CI/CD пайплайні.

---
## 2.Kubernetes Primitives:

```Deployment```: Налаштовано розгортання застосунку на 2 репліки.

```Service```: Створено сервіс типу ClusterIP для внутрішньокластерної комунікації.

```ConfigMap``` та ```Secret```: Змінні оточення, включаючи ```DB_HOST``` та ```DB_PASSWORD```,
безпечно передаються в контейнери через конфігураційні файли.

---
## 3. Self-healing(Відмовостійкість):

Налаштовано ```livenessProbe``` та ```readinessProbe```, які періодично опитують ендпоінт /health для контролю стану застосунку.

---
## 4.Automated Quality Gate(Автоматичне оцінювання):

CI/CD пайплайн ```.github/workflows/lab3.yml``` автоматично піднімає KinD кластер, розгортає маніфести 
```kubectl apply -f k8s/``` та запускає валідаційний скрипт перевірки tests/lab3_test.sh

<img width="977" height="262" alt="image" src="https://github.com/user-attachments/assets/58261f21-1180-4db1-8df5-6bdf85941675" />
<img width="833" height="97" alt="image" src="https://github.com/user-attachments/assets/65d9c683-6cad-445e-bde8-4b398d5fa3ac" />

---
## 5. Завантаження та запуск локально в KinD

1. Створення кластеру:
```bash
kind create cluster --name ecommerce-cluster
```

2. Застосування маніфестів:
```bash
kubectl apply -f k8s/
```

3. Перевірка статусу розгортання:
```bash
kubectl get pods
kubectl get svc
```

4. Прокидання порта для доступу до API:
```bash
kubectl port-forward service/ecommerce-app-service 8080:80
```

---
