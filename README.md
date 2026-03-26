# 🚀 Dev Backups Orchestrator

> **Misión:** Sistema automatizado para la gestión, rotación y orquestación de backups multiplataforma con integración en la nube.
> **Nivel de Ingeniería:** Senior Full-Stack (Alineado con Playbook de Ingeniería v7).

---

## 🏛️ Estándares de Ingeniería
Este repositorio sigue principios de arquitectura limpia y automatización:

* **Arquitectura:** Modular (Separación de lógica de compresión, orquestación y transporte).
* **Documentación de Decisiones (ADR):** Registro de decisiones técnicas en `/docs/adr`.
* **Commits:** Bajo norma **Conventional Commits** (`feat:`, `fix:`, `chore:`).
* **Seguridad:** Gestión de credenciales mediante variables de entorno (`.env`).

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.12+
* **Linter/Formateador:** Ruff (Configurado en pre-commit).
* **Dependencias:** Boto3 (AWS), Google Cloud Storage SDK (Opcional).
* **Automatización:** Git Hooks con Husky / Lint-staged.

---

## 🚀 Guía de Inicio Rápido (Local)

### 1. Preparación del Entorno
```bash
# Clonar el repositorio
git clone [https://github.com/javierbrega/dev-backups-orchestrator.git](https://github.com/javierbrega/dev-backups-orchestrator.git)
cd dev-backups-orchestrator

# Configurar aislamiento (Recomendado)
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt