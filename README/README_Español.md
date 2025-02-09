- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Herramienta de Generación y Traducción Automática de README 🛠️✨

¡Bienvenido al proyecto de **Herramienta de Generación y Traducción Automática de README**! Esta herramienta está diseñada para simplificar y mejorar la gestión y traducción de archivos README en repositorios de GitHub. ¡Ya seas un mantenedor del proyecto o un nuevo usuario, te ayudará a hacer tu flujo de trabajo más eficiente y agradable! 😄

## Estructura del Proyecto 🗂️

A continuación se presenta la estructura del directorio, para que puedas comprender rápidamente la finalidad de cada archivo y carpeta:

```
.github
└── workflows
    ├── generate.yml         # Flujo de trabajo para generar automáticamente el archivo README
    ├── optimize.yml         # Flujo de trabajo para optimizar automáticamente el archivo README
    └── translate.yml        # Flujo de trabajo para traducir automáticamente el archivo README

LICENSE                        # Archivo de licencia del proyecto
README.md                     # Archivo README principal del proyecto
README
├── README_Deutsch.md        # README en alemán
├── README_English.md        # README en inglés
├── README_Español.md        # README en español
├── README_Français.md       # README en francés
├── README_日本語.md         # README en japonés
└── README_繁体中文.md      # README en chino (tradicional)

config.json                   # Archivo de configuración
requirements.txt              # Archivo de dependencias de Python
tool.py                       # Script de la herramienta automatizada
```

## Resumen del Flujo de Trabajo 🚀

### 1. `generate.yml`
Este flujo de trabajo de GitHub Actions se utiliza para generar y actualizar automáticamente el archivo README. Los pasos principales incluyen:

- Clonar el código
- Configurar el entorno de Python 3.8
- Instalar las dependencias necesarias (`requests`, `openai`, `GitPython`)
- Ejecutar el script (`tool.py generate`) para generar o actualizar el archivo README
- Configurar Git y enviar el archivo README actualizado

¡Este proceso simplifica el mantenimiento del archivo README, permitiéndote concentrarte en asuntos más importantes! 😎

### 2. `optimize.yml`
Este flujo de trabajo optimiza automáticamente el archivo README, que también puede ser activado manualmente a través del evento `workflow_dispatch`. Los pasos clave incluyen:

- Clonar el código
- Configurar el entorno de Python 3.8
- Instalar las dependencias
- Ejecutar el script (`tool.py optimize`) para mejorar el contenido del README
- Hacer un commit y enviar el archivo README actualizado

¡Mejoramos la calidad del contenido juntos! 💪

### 3. `translate.yml`
Este flujo de trabajo traduce automáticamente el archivo README, asegurando que tu proyecto llegue a una audiencia más amplia. Los pasos incluyen:

- Clonar el código
- Configurar el entorno de Python 3.8
- Instalar las dependencias
- Ejecutar el script de traducción (`tool.py`)

¡Es tu asistente definitivo en la era multilingüe! 🌍

## Licencia 📄
Este proyecto está bajo la Licencia Apache 2.0, que te permite utilizar, modificar y distribuir el código, mientras se protegen tus derechos y obligaciones.

## Gestión de Configuración 🛠️
El archivo `config.json` define configuraciones importantes, como el punto final de la API y los idiomas de traducción admitidos, para asegurar el funcionamiento fluido de la herramienta y apoyar características multilingües. 🤓

## Gestión de Dependencias 🐍
El archivo `requirements.txt` enumera los paquetes de Python necesarios, incluyendo:

- **requests**: Simplifica las solicitudes HTTP
- **openai**: Acceso a la API de OpenAI para diversas operaciones
- **GitPython**: Interactuar con repositorios de Git en Python

¡Asegúrate de instalar estas dependencias para garantizar el correcto funcionamiento de la herramienta! 🌟

## ¿Cómo Usar?

Puedes optar por hacer un fork de este proyecto y utilizar `GitHub Actions`, o clonarlo localmente para su uso.

Aquí tienes un ejemplo de uso con GitHub Actions:

1. Agrega `PAT` y `OPENAI_API_KEY` en los Secrets de GitHub.
2. Edita el archivo `config.json` para configurar los parámetros relevantes.
3. Si deseas generar y traducir el archivo README:
   - Ejecuta manualmente el flujo de trabajo `generate`, lo que generará un archivo `.README.md` en el directorio raíz del repositorio.
   - Revisa y modifica ese archivo antes de hacer un commit.
   - Activa manualmente el flujo de trabajo `translate`, la herramienta añadirá el README editado al repositorio objetivo y generará versiones traducidas.

¡Listo! 🎉

Si ya tienes un archivo README y solo deseas traducirlo:
- Sube el archivo al archivo `.README.md` del repositorio de la herramienta.
- Activa manualmente el flujo de trabajo `translate`.

¡Listo! 🎉

## Comentarios y Contribuciones 🙌
¡Agradecemos tus comentarios y sugerencias! No dudes en dar un "me gusta"⭐️ a este proyecto y participar en él, ¡juntos mejoramos la calidad y usabilidad del proyecto!

¡Gracias por tu interés y apoyo! ¡Unámonos para hacer los archivos README más vibrantes y divertidos! 🎉