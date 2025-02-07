# Herramienta Automática de Generación y Traducción

¡Bienvenido a la **Herramienta Automática de Generación y Traducción**! 🌟 Esta herramienta innovadora está diseñada para facilitar la creación y traducción automática de textos para proyectos de software alojados en GitHub. Al aprovechar APIs avanzadas y una configuración amigable, puedes generar fácilmente archivos README profesionales y traducirlos a varios idiomas. 📄🌍

## Tabla de Contenidos
- [Introducción al Proyecto](#introducción-al-proyecto)
- [Características](#características)
- [Pasos de Instalación](#pasos-de-instalación)
- [Instrucciones de Uso](#instrucciones-de-uso)
- [Configuración](#configuración)
- [Guías de Contribución](#guías-de-contribución)
- [Licencia](#licencia)

## Introducción al Proyecto

La Herramienta Automática de Generación y Traducción simplifica el proceso de crear archivos README pulidos y multilingües para repositorios de software. 🎉 Al entender y resumir el contenido de tus archivos de proyecto, no solo genera un README atractivo, sino que también lo traduce a múltiples idiomas, ¡haciendo que tu proyecto sea más accesible a una audiencia global! 🌐

## Características

- **Gestión de Configuración**: Simplifica tu configuración con un archivo de configuración JSON que define parámetros esenciales del repositorio. 🛠️
- **Recuperación de Archivos**: Recupera automáticamente archivos de tu repositorio de GitHub utilizando la API de GitHub. 📥
- **Generación de Contenido**: Genera un README profesional con detalles claros del proyecto, pasos de instalación, instrucciones de uso y más, utilizando la API de OpenAI. 📘
- **Soporte de Traducción**: Traduce el contenido del README a múltiples idiomas para atender a una audiencia diversa. 🌈
- **Actualizaciones Amigables**: Comete fácilmente cambios al README principal y crea archivos README traducidos separados. ✏️

## Pasos de Instalación

Para comenzar con la Herramienta Automática de Generación y Traducción, sigue estos pasos:

1. **Clona el Repositorio:**
   ```bash
   git clone https://github.com/username/repo.git
   ```

2. **Navega al Directorio del Proyecto:**
   ```bash
   cd repo
   ```

3. **Instala Dependencias:**
   Asegúrate de tener Python instalado. Luego, instala los paquetes requeridos usando pip:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la Herramienta:**
   Edita el archivo `config.json` para incluir la URL de tu repositorio de GitHub, información de la rama y los idiomas de traducción preferidos. ⚙️

## Instrucciones de Uso

Para utilizar la Herramienta Automática de Generación y Traducción, ejecuta el script de Python de la siguiente manera:

```bash
python tool.py
```

Este comando leerá el archivo de configuración, recuperará los archivos necesarios del repositorio de GitHub especificado, generará el contenido del README, lo traducirá y comprometerá los cambios de vuelta al repositorio. 🚀

### Ejemplo de Configuración

Aquí hay un ejemplo de cómo debería verse tu `config.json`:

```json
{
    "repo_url": "https://github.com/username/repo",
    "branch": "main",
    "main_language_index": 0,
    "api_token": "YOUR_GITHUB_API_TOKEN",
    "target_languages": ["es", "fr", "de"]
}
```

Asegúrate de reemplazar `"YOUR_GITHUB_API_TOKEN"` con tu token de API real de GitHub. 🔑

## Guías de Contribución

¡Damos la bienvenida a las contribuciones para mejorar la funcionalidad de la Herramienta Automática de Generación y Traducción! Aquí hay algunas formas en las que puedes contribuir:

1. **Haz un Fork del Repositorio**: Crea tu propio fork para trabajar en tus cambios. 🍴
2. **Envía un Pull Request**: Una vez que hayas realizado tus cambios y los hayas probado, envía un pull request para revisión. 📩
3. **Reporta Problemas**: Si encuentras algún error o tienes sugerencias, no dudes en abrir un problema en el repositorio. ⚠️

## Licencia

Este proyecto está licenciado bajo los términos de la [Licencia Apache, Versión 2.0](https://www.apache.org/licenses/LICENSE-2.0). Esta licencia permisiva te permite usar, reproducir y distribuir el software mientras protege los derechos de los colaboradores. 📜

---

¡Gracias por usar la Herramienta Automática de Generación y Traducción! Esperamos que mejore la accesibilidad y el compromiso de tu proyecto. ¡Feliz codificación! 💻✨

[Back to main language README](README.md)