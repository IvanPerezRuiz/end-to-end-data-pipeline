En el sector tecnológico e internacional, tener el **`README.md` en inglés** es el estándar de oro y multiplica el impacto ante reclutadores y empresas que buscan perfiles técnicos.

Aquí tienes un `README.md` profesional, con *badges* (insignias), diagramas visuales, explicación de la arquitectura Medallion y las instrucciones de despliegue para que cualquiera pueda levantar el proyecto en su máquina.

Puedes copiar este contenido directamente en el archivo `README.md` de vuestro repositorio en GitHub:

---

```markdown
<div align="center">

# 🚲 Urban Mobility & Environmental Data Platform
### *End-to-End Modern Data Stack (ELT) Pipeline*

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-2.8+-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white)](https://airflow.apache.org/)
[![dbt](https://img.shields.io/badge/dbt-Core-FF694B?style=for-the-badge&logo=dbt&logoColor=white)](https://www.getdbt.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![MinIO](https://img.shields.io/badge/MinIO-S3%20Compatible-C72C48?style=for-the-badge&logo=minio&logoColor=white)](https://min.io/)
[![Metabase](https://img.shields.io/badge/Metabase-Analytics-509EE3?style=for-the-badge&logo=metabase&logoColor=white)](https://www.metabase.com/)

<p align="center">
  A production-ready, containerized ELT data pipeline analyzing the correlation between weather conditions, air pollution, and public bike-sharing mobility.
</p>

</div>

---

## 📌 Project Overview

Urban micro-mobility systems (like shared public bicycles) are heavily influenced by environmental conditions. This project builds a fully automated, scalable data platform that extracts data from three heterogeneous public APIs, stores raw data in a local Data Lake, applies dimensional transformations using **dbt**, and serves aggregated business metrics on an interactive **Metabase** dashboard.

### 🎯 Key Business Question:
> *"How do real-time weather variations (rain, temperature, wind) and air pollution levels (NO2, PM10, AQI) affect public bicycle availability and usage patterns across city stations?"*

---

## 🏗️ System Architecture

The pipeline follows the **Medallion Architecture (Bronze $\rightarrow$ Silver $\rightarrow$ Gold)** and is orchestrated on a scheduled basis via **Apache Airflow**:

```text
 ┌────────────────────────────────────────────────────────────────────────┐
 │                           DATA SOURCES (APIs)                          │
 │  1. CityBikes (Mobility)  │ 2. Open-Meteo (Weather) │ 3. Air Quality   │
 └──────────────────────┬───────────────────┬───────────────────┬─────────┘
                        │                   │                   │
                        ▼                   ▼                   ▼
              [ Python Extraction Scripts (REST API with Retries) ]
                                    │
                                    ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                      BRONZE LAYER (RAW DATA LAKE)                      │
 │                  MinIO (S3-Compatible Object Storage)                  │
 │                  - Immutable Raw Parquet / JSON Files                  │
 └──────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                   SILVER LAYER (DATA WAREHOUSE / DB)                   │
 │                     PostgreSQL / DuckDB + dbt Core                     │
 │          - Deduplication, Type Casting, Schema Normalization           │
 └──────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │                       GOLD LAYER (BUSINESS MARTS)                      │
 │                   Star Schema (Fact & Dimension Tables)                │
 │                  - Unified Temporal & Spatial Aggregates               │
 └──────────────────────────────────┬─────────────────────────────────────┘
                                    │
                         ┌──────────┴──────────┐
                         ▼                     ▼
             [ Metabase Dashboards ]   [ Automated dbt Tests ]
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Ingestion** | `Python 3.10+`, `Requests` | Modular extraction scripts with metadata lineage and retry logic |
| **Orchestration** | `Apache Airflow` | Scheduled DAGs, failure alerts, and task dependency management |
| **Data Lake** | `MinIO` | Local S3-compatible object storage for immutable raw files |
| **Data Warehouse** | `PostgreSQL` / `DuckDB` | Relational analytics engine for structured data storage |
| **Transformation** | `dbt (data build tool)` | Modular SQL modeling, lineage tracking, and schema documentation |
| **Data Quality** | `dbt tests` | Automated uniqueness, non-null, and referential integrity assertions |
| **Visualization** | `Metabase` | Interactive BI dashboards for mobility and environmental insights |
| **Infrastructure** | `Docker & Docker Compose` | Fully reproducible local development environment |

---

## 📂 Project Structure

```text
end-to-end-data-pipeline/
├── dags/                     # Apache Airflow DAG definitions
│   ├── dag_mobility.py
│   ├── dag_weather.py
│   └── dag_air_quality.py
├── dbt/                      # dbt transformation project
│   ├── models/
│   │   ├── staging/          # Silver Layer: Cleaned source models
│   │   └── marts/            # Gold Layer: Fact & Dimension tables (Star Schema)
│   ├── tests/                # Custom data quality tests
│   └── dbt_project.yml
├── src/                      # Core Python source code
│   ├── extraction/           # API ingestion logic
│   └── utils/                # S3/MinIO helpers & DB connectors
├── assets/                   # Architecture diagrams and dashboard screenshots
├── docker-compose.yml        # Multi-container service definitions
├── .env.example              # Environment variables template
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🚀 Quick Start (Run Locally in 3 Steps)

### Prerequisites
* [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
* [Git](https://git-scm.com/) installed.

### 1. Clone the repository
```bash
git clone https://github.com/IvanPerezRuiz/end-to-end-data-pipeline.git
cd end-to-end-data-pipeline
```

### 2. Configure environment variables
```bash
cp .env.example .env
```

### 3. Launch the platform with Docker Compose
```bash
docker compose up -d
```

---

## 🌐 Service Endpoints

Once the containers are up and running, you can access the following web UIs:

| Service | URL | Default Credentials |
| :--- | :--- | :--- |
| **Airflow UI** | [http://localhost:8080](http://localhost:8080) | `admin` / `admin` |
| **MinIO Console** | [http://localhost:9001](http://localhost:9001) | `minioadmin` / `minioadmin` |
| **Metabase (BI)** | [http://localhost:3000](http://localhost:3000) | *Set up on first login* |
| **PostgreSQL** | `localhost:5432` | Defined in `.env` |

---

## 🧪 Data Quality & Testing

Data reliability is enforced at every layer using automated tests:
* **Schema Validation:** Enforcing non-null primary keys and foreign key relationships.
* **Domain Assertions:** Checking for valid ranges (e.g., non-negative bike availability, valid meteorological bounds).
* **dbt Test Execution:**
  ```bash
  docker compose run --rm dbt dbt test
  ```

---

## 👥 Contributors

This project was collaboratively developed by:

* **Iván Pérez Ruiz** - [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/IvanPerezRuiz) • [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/)
* **David Pascual Ferré** - [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/) • [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/)
* **Carlos Alberto Ruiz Blanco** - [![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/) • [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/)

*Computer Science Engineering Students — Universidad de Granada (UGR)*

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
```

---

### Un par de detalles para cuando lo peguéis:
1. En la sección **Contributors**, cambiad `[Name Teammate 2]` y `[Name Teammate 3]` por los nombres reales de tus compañeros y poned vuestros enlaces a LinkedIn y GitHub.
2. Más adelante, podéis añadir una captura o diagrama en una carpeta `assets/` para que la cabecera quede aún más visual.
