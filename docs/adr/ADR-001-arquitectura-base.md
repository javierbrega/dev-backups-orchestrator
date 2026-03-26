# ADR 001: Arquitectura del Orquestador de Backups

**Estado:** Aceptado
**Fecha:** 2026-03-26
**Arquitecto:** Javier

## Contexto
Necesitamos un sistema que automatice el respaldo de carpetas de proyectos locales para evitar pérdida de datos de forma segura y profesional.

## Decisión
Hemos decidido utilizar **Python 3** con una estructura modular por las siguientes razones:
1. **Seguridad:** Uso de archivos `.env` para proteger rutas privadas del sistema.
2. **Portabilidad:** Uso de entornos virtuales (`venv`) para mantener limpia la computadora.
3. **Trazabilidad:** Nombramiento de archivos con marcas de tiempo (*timestamps*) automáticos.

## Consecuencias
- El sistema es fácil de escalar (podemos agregar subida a la nube después).
- Se requiere mantener el archivo `.env` actualizado localmente.