<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al mundo de la **Herramienta de Generación y Traducción Automática de README**! 🎉 Este proyecto tiene como objetivo proporcionar a desarrolladores y mantenedores de proyectos una solución eficiente y conveniente para generar, optimizar y traducir archivos README, brindando documentación profesional y atractiva para el código. ¡Ya seas principiante o un desarrollador experimentado, aquí encontrarás las herramientas que necesitas! 🌟

## 🛠️ Estructura del Proyecto

A continuación, se presenta la estructura básica del proyecto, clara y fácil de usar:

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # Flujo de trabajo para generar automáticamente el archivo README
│       ├── optimize.yml      # Flujo de trabajo para optimizar el archivo README
│       └── translate.yml      # Flujo de trabajo para traducir el archivo README
├── LICENSE                   # Licencia del proyecto
├── README.md                 # Archivo de descripción del proyecto
├── config.json               # Archivo de configuración de la herramienta
├── requirements.txt          # Lista de dependencias
└── tool.py                   # Script de automatización
```

## ✨ Funciones Principales

1. **Generación Automática de README**: Con la ayuda de los flujos de trabajo de GitHub Actions, genera archivos README profesionales automáticamente a partir del código del proyecto.
2. **Función de Optimización**: A través de la API de OpenAI, logra optimizaciones impulsadas por IA para mejorar la calidad de los documentos README existentes.
3. **Capacidad de Traducción**: Traduce automáticamente el archivo README a varios idiomas, ayudando a que una audiencia más amplia pueda acceder fácilmente a tu proyecto.👌

## ⚙️ Flujos de Trabajo

### 1. `generate.yml`
- Activación manual mediante `workflow_dispatch` para generar el archivo README.
- Se ejecuta en un entorno Ubuntu, instalando las dependencias necesarias (`requests`, `openai`, `GitPython`).
- Finalmente, ejecuta el script `tool.py generate` para generar un README profesional.

### 2. `optimize.yml`
- Activación manual para optimizar automáticamente el archivo README existente.
- Incluye pasos para la revisión del código, configuración del entorno de Python e instalación de dependencias.
- Ejecuta el script `tool.py optimize` para mejorar la legibilidad del README.

### 3. `translate.yml`
- Activación manual para traducir automáticamente el archivo README.
- Después de extraer el código, configurar el entorno de Python e instalar las dependencias requeridas, se ejecuta el script de traducción.

## 📝 Descripción de la Configuración

El archivo `config.json` contiene la configuración y las opciones básicas de la herramienta, incluyendo:
- Nombre y propietario del repositorio
- URL base de la API y modelo de lenguaje utilizado
- Idiomas a traducir y sus abreviaturas
- …

Asegúrate de configurar correctamente este archivo para garantizar el funcionamiento adecuado de la herramienta. 🔑

## 📦 Dependencias

En `requirements.txt`, puedes encontrar las dependencias necesarias para el proyecto:
- **requests**: Biblioteca de solicitudes HTTP fácil de usar.
- **openai**: Biblioteca para interactuar con la API de OpenAI.
- **GitPython**: Biblioteca de Python para interactuar con repositorios Git.

¡Asegúrate de instalar estas dependencias para ejecutar el proyecto sin problemas! 🚀

## 🖥️ Detalle de Funciones Clave

El script `tool.py` es el núcleo de este proyecto, ofreciendo las siguientes funciones:
- Carga automáticamente el archivo de configuración y gestiona la configuración del proyecto.
- Obtiene de forma interactiva archivos del repositorio y genera resúmenes de archivos.
- Crea, optimiza y traduce archivos README, enviándolos luego a través de operaciones de Git.

¡También puedes ejecutar comandos específicos a través de la interfaz de línea de comandos para satisfacer diferentes necesidades! 🎈

## 🌸 ¿Cómo Usar?

Puedes optar por hacer un fork de este proyecto, usar `GitHub Actions`, o clonarlo localmente. A continuación, se presenta un ejemplo utilizando `GitHub Actions`:

1. Agrega `PAT` y `OPENAI_API_KEY` a los secretos.
2. Configura los parámetros necesarios en `config.json`.
3. Activa manualmente el flujo de trabajo que desees ejecutar.

Ten en cuenta que `optimize.yml` y `translate.yml` requieren que ya exista un archivo README en el repositorio objetivo para poder ejecutarse.

## 📜 Licencia

Este proyecto se rige por la licencia **Apache License 2.0**, consulta el archivo `LICENSE` para más detalles.

## 🤝 Contribuciones y Soporte

¡Te damos una cálida bienvenida a tus contribuciones! Si crees que esta herramienta puede serte de ayuda, por favor, ¡déjanos una ⭐️! ¡Tu apoyo es la motivación que nos impulsa a seguir adelante! 💪

---

A través de esta herramienta, puedes crear fácilmente documentación profesional y fácil de leer. ¡Inténtalo y ahorra tiempo y esfuerzo, este proyecto merece estar en tus marcadores! 🌟