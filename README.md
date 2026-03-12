# ☸️ Kubernetes Stream Processing

Sistema de streaming en tiempo real con Kafka y Spark Streaming.

---

## ✅ Descripcion

Genera eventos simulados, los envia a Kafka y los procesa en tiempo real con Spark.

### ¿Que hace este proyecto?

- **Data Producer**: Genera eventos de sensores
- **Kafka**: Broker de mensajeria
- **Spark Streaming**: Analitica en tiempo real
- **Resultados**: Conteos por sensor en consola

---

## ✨ Caracteristicas Principales

| Caracteristica | Descripcion |
|----------------|-------------|
| **Streaming** | Datos en tiempo real |
| **Kafka** | Cola distribuida |
| **Spark** | Procesamiento en streaming |
| **Kubernetes** | Despliegue escalable |

---

## 🛠️ Stack Tecnologico

- **Python**
- **Apache Kafka**
- **Apache Spark**
- **Docker / Kubernetes**

---

## 📦 Instalacion y Uso

### Probar con Docker Compose

```bash
docker compose up --build
```

### Probar con Kubernetes

1) Construir imagenes:

```bash
docker build -t data-producer:latest -f docker/producer.Dockerfile .
docker build -t spark-stream:latest -f docker/spark-stream.Dockerfile .
```

2) Aplicar manifests:

```bash
kubectl apply -f k8s/kafka.yaml
kubectl apply -f k8s/producer.yaml
kubectl apply -f k8s/spark-stream.yaml
```

---

## 🗂️ Estructura del Proyecto

```
kubernetes-stream-processing
├── producer
├── spark-stream
├── kafka
├── k8s
├── docker
├── docker-compose.yml
└── README.md
```

---

© 2026 Isaac Esteban Haro Torres - Todos los derechos reservados.

