# 🧠 Cerebro Digital

Sistema inteligente adaptativo diseñado para gestionar información, aprendizaje y automatización mediante una arquitectura moderna, modular y escalable.

El objetivo de **Cerebro Digital** es construir una plataforma capaz de organizar información, gestionar memoria digital y crear una base tecnológica preparada para sistemas inteligentes adaptativos.

---

# 🚀 Estado del proyecto

Actualmente en desarrollo.

## Implementado ✅

### Infraestructura

* ✅ Estructura inicial del proyecto
* ✅ Backend desarrollado con FastAPI
* ✅ Configuración mediante variables de entorno
* ✅ Entorno virtual de Python
* ✅ Dockerización de servicios
* ✅ Docker Compose configurado
* ✅ PostgreSQL ejecutándose en contenedor
* ✅ Redis ejecutándose en contenedor
* ✅ PgAdmin configurado para administración de base de datos

### Backend

* ✅ Arquitectura modular basada en capas
* ✅ Configuración centralizada
* ✅ Conexión entre FastAPI y PostgreSQL
* ✅ SQLAlchemy ORM configurado
* ✅ Sistema de sesiones de base de datos
* ✅ Migraciones con Alembic
* ✅ Modelo inicial de usuarios
* ✅ Endpoints REST para usuarios
* ✅ Documentación automática con Swagger/OpenAPI

### Base de datos

* ✅ PostgreSQL 17
* ✅ Primera migración creada con Alembic
* ✅ Tabla `users`
* ✅ Persistencia de datos comprobada

---

# 🏗️ Arquitectura actual

```
Cerebro Digital
│
├── backend
│   │
│   ├── app
│   │   │
│   │   ├── api
│   │   │   └── users.py
│   │   │
│   │   ├── core
│   │   │   └── config.py
│   │   │
│   │   ├── db
│   │   │   ├── database.py
│   │   │   ├── session.py
│   │   │   └── base.py
│   │   │
│   │   ├── models
│   │   │   └── user.py
│   │   │
│   │   ├── schemas
│   │   │   └── user.py
│   │   │
│   │   └── services
│   │       └── user_service.py
│   │
│   ├── alembic
│   │   └── migrations
│   │
│   ├── Dockerfile
│   └── requirements.txt
│
├── docker-compose.yml
│
├── database
│
├── mobile
│   └── (futuro cliente móvil)
│
└── docs
```

---

# 🛠️ Tecnologías utilizadas

## Backend

* Python 3.13
* FastAPI
* SQLAlchemy 2
* Pydantic
* Alembic
* Uvicorn

## Base de datos

* PostgreSQL 17
* Redis 8

## Infraestructura

* Docker
* Docker Compose
* PgAdmin

## Control de versiones

* Git
* GitHub

---

# 🗄️ Modelo actual

## User

El sistema cuenta con una entidad inicial de usuarios preparada para futuras funcionalidades.

Actualmente almacena:

* Identificación personal
* Nombre y apellido
* Fecha de nacimiento
* Email único
* Estado de cuenta
* Configuración regional
* Fecha de creación
* Auditoría básica

---

# 🔌 API disponible

## Usuarios

### Crear usuario

```
POST /users/
```

Ejemplo:

```json
{
  "first_name": "Wilmer",
  "last_name": "Siguencia",
  "email": "wilmer@test.com",
  "password": "123456",
  "birth_date": "2003-01-01"
}
```

### Obtener usuarios

```
GET /users/
```

---

# 🐳 Servicios Docker

Servicios actuales:

| Servicio   | Puerto |
| ---------- | ------ |
| PostgreSQL | 5432   |
| Redis      | 6379   |
| PgAdmin    | 5050   |

---

# ⚙️ Instalación y ejecución

## Clonar proyecto

```bash
git clone <repository-url>
```

## Crear entorno virtual

```bash
python -m venv .venv
```

Activar entorno:

```bash
source .venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

---

# Ejecutar infraestructura

```bash
docker compose up -d
```

Verificar servicios:

```bash
docker ps
```

---

# Ejecutar backend

Desde la carpeta `backend`:

```bash
uvicorn app.main:app --reload
```

Documentación API:

```
http://127.0.0.1:8000/docs
```

---

# 🧬 Migraciones de base de datos

Crear migración:

```bash
alembic revision --autogenerate -m "descripcion"
```

Aplicar migraciones:

```bash
alembic upgrade head
```

Consultar versión actual:

```bash
alembic current
```

---

# 🧭 Roadmap

## Etapa 1 - Infraestructura ✅

* [x] Docker
* [x] PostgreSQL
* [x] Redis
* [x] FastAPI
* [x] Alembic
* [x] Arquitectura inicial

---

## Etapa 2 - Sistema de usuarios 🔄

* [x] Modelo User
* [x] Crear usuarios
* [x] Consultar usuarios
* [ ] Hash seguro de contraseñas
* [ ] Autenticación JWT
* [ ] Roles y permisos
* [ ] Recuperación de cuenta

---

## Etapa 3 - Cerebro Adaptativo 🧠

* [ ] Sistema de memoria digital
* [ ] Registro de eventos
* [ ] Procesamiento de información
* [ ] Aprendizaje personalizado
* [ ] Motor de adaptación

---

# 📌 Filosofía del proyecto

Cerebro Digital nace con la visión de construir una arquitectura capaz de almacenar, organizar y utilizar información de manera inteligente.

Cada etapa del proyecto busca crear una base sólida que permita evolucionar desde una aplicación tradicional hacia un sistema adaptativo capaz de aprender y mejorar con el tiempo.