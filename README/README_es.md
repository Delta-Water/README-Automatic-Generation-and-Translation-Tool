<div align="center">

[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al proyecto de **Herramienta de Generación y Traducción Automática de README**! 🎉 Este proyecto tiene como objetivo proporcionar a desarrolladores y mantenedores de proyectos una forma conveniente de generar, optimizar y traducir archivos README con facilidad. ¡No importa si eres principiante o experto, solo sigue unos simples pasos y obtén un documento README profesional y atractivo! 🚀

## 📂 Estructura del Proyecto

```plaintext
./
└── workflows/
│   ├── generate.yml      # Flujo de trabajo para la generación automática de archivos README
│   ├── optimize.yml      # Flujo de trabajo para la optimización automática del archivo README
│   └── translate.yml      # Flujo de trabajo para la traducción automática del archivo README
└── LICENSE                # Archivo de licencia Apache
└── README.md              # Archivo de descripción del proyecto
└── config.json            # Archivo de configuración que define los parámetros del proyecto
└── requirements.txt       # Lista de paquetes de Python necesarios
└── tool.py                # Herramienta de procesamiento automatizado
```

## ⚙️ Descripción de los Archivos

### `.github/workflows/generate.yml`
Este flujo de trabajo genera automáticamente el archivo README del proyecto mediante GitHub Actions. Una vez activado manualmente, ejecuta los siguientes pasos:
1. Clona el código del proyecto;
2. Configura el entorno de Python 3.8;
3. Instala las dependencias necesarias (`requests`, `openai`, `GitPython`);
4. Ejecuta el script `tool.py generate` para generar el archivo README.

### `.github/workflows/optimize.yml`
Este flujo de trabajo se utiliza para optimizar automáticamente el archivo README. Una vez activado manualmente, realiza los siguientes pasos:
1. Clona el código;
2. Configura el entorno de Python 3.8;
3. Instala las dependencias necesarias;
4. Ejecuta `tool.py optimize` para optimizar mediante la API de OpenAI.

### `.github/workflows/translate.yml`
Este flujo de trabajo se utiliza para traducir automáticamente el archivo README del proyecto, también activado manualmente. Los pasos incluyen:
1. Clona el código;
2. Configura el entorno de Python 3.8;
3. Instala las dependencias;
4. Ejecuta `tool.py translate` para traducir.

### `LICENSE`
Este archivo contiene la licencia Apache 2.0, que permite a los usuarios utilizar, modificar y distribuir este proyecto bajo ciertas condiciones, protegiendo así los derechos del autor y los contribuyentes.

### `config.json`
Este archivo de configuración define varios parámetros necesarios para la ejecución del proyecto, incluyendo información del repositorio, URL base de la API, modelo y lenguajes de traducción soportados.

### `requirements.txt`
Lista los paquetes de Python requeridos por el proyecto, incluyendo:
- `requests`: para manejar solicitudes HTTP, simplificando la interacción en red.
- `openai`: para interactuar con la API de OpenAI y realizar llamadas a modelos de IA.
- `GitPython`: que proporciona soporte para operaciones en repositorios Git.

### `tool.py`
El script central utilizado para el procesamiento automatizado del README, cuyas principales funciones son:
1. Cargar la configuración;
2. Obtener contenido del repositorio;
3. Generar contenido para el README;
4. Mejorar y traducir el README;
5. Enviar cambios;
6. Proporcionar una interfaz de línea de comando.

## 🌸 ¿Cómo Usar?

Puedes optar por hacer un fork de este proyecto y utilizar `GitHub Actions`, o clonarlo localmente para su uso. A continuación, se describen los pasos para el primer caso; para el segundo, configúralo por tu cuenta.

1. Primero, agrega `PAT` y `OPENAI_API_KEY` a Secrets.
2. Luego, ingresa a `config.json` para configurar los parámetros relevantes.
3. Para generar el README, activa manualmente el flujo de trabajo `generate`.
4. Para optimizar el README, activa manualmente el flujo de trabajo `optimize`.
5. Para traducir el README, activa manualmente el flujo de trabajo `translate`.

## 🌟 ¡Comencemos!

¡No esperes más! Usa esta herramienta para mejorar la calidad de la documentación de tu proyecto y atraer más colaboración y atención. Si consideras que este proyecto te ha sido útil, ¡dános un 💖 Star! ¡Trabajemos juntos para hacer que la comunidad de código abierto sea aún mejor! 🌈

## 📄 Licencia

Este proyecto está bajo la licencia Apache. Para más detalles, consulta el archivo [LICENSE](LICENSE).

¡Únete a nosotros y hagamos que los README sean más simples y eficientes! 🚀