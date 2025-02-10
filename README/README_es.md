<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al proyecto de **Generación y Traducción Automática de README**! 🎉 Este proyecto tiene como objetivo proporcionar a los desarrolladores y mantenedores de proyectos una forma conveniente de generar, optimizar y traducir archivos README con facilidad. ¡No importa si eres principiante o experto, en solo unos simples pasos podrás obtener un documento README profesional y atractivo! 🚀

## 📂 Estructura del Proyecto

```plaintext
./
└── workflows/
│   ├── generate.yml      # Flujo de trabajo para la generación automática de archivos README
│   ├── optimize.yml      # Flujo de trabajo para la optimización automática de documentos README
│   └── translate.yml      # Flujo de trabajo para la traducción automática de documentos README
└── LICENSE                # Archivo de licencia Apache
└── README.md              # Archivo de descripción del proyecto
└── config.json            # Archivo de configuración que define parámetros del proyecto
└── requirements.txt       # Lista de dependencias de Python
└── tool.py                # Herramienta de procesamiento automático
```

## ⚙️ Descripción de Archivos

### `.github/workflows/generate.yml`
Este flujo de trabajo genera automáticamente el archivo README del proyecto a través de GitHub Actions. Después de ser activado manualmente, realiza los siguientes pasos:
1. Extrae el código del proyecto;
2. Configura el entorno Python 3.8;
3. Instala las dependencias necesarias (`requests`, `openai`, `GitPython`);
4. Ejecuta el script `tool.py generate` para generar el archivo README.

### `.github/workflows/optimize.yml`
Este flujo de trabajo se utiliza para optimizar automáticamente el archivo README. Después de la activación manual, se realizan los siguientes pasos:
1. Extrae el código;
2. Configura el entorno Python 3.8;
3. Instala las dependencias necesarias;
4. Ejecuta `tool.py optimize` para procesar la optimización a través de la API de OpenAI.

### `.github/workflows/translate.yml`
Este flujo de trabajo se utiliza para traducir automáticamente el archivo README del proyecto, iniciándose también por activación manual. Los pasos incluyen:
1. Extrae el código;
2. Configura el entorno Python 3.8;
3. Instala las dependencias;
4. Ejecuta `tool.py translate` para realizar la traducción.

### `LICENSE`
Este archivo contiene la Licencia Apache, versión 2.0, que permite a los usuarios utilizar, modificar y distribuir este proyecto libremente, siempre que cumplan con las condiciones correspondientes, protegiendo así los derechos del autor y de los contribuyentes.

### `config.json`
Este archivo de configuración define varios parámetros necesarios para la ejecución del proyecto, incluyendo información sobre el repositorio, la URL base de la API, el modelo, así como los idiomas disponibles para la traducción.

### `requirements.txt`
Lista de los paquetes de Python requeridos por el proyecto, incluyendo:
- `requests`: Para manejar las solicitudes HTTP y simplificar las interacciones en red.
- `openai`: Para interactuar con la API de OpenAI y realizar llamadas a modelos de IA.
- `GitPython`: Para proporcionar soporte en la operación de repositorios Git.

### `tool.py`
El script principal utilizado para el procesamiento automático del README, con funciones clave que incluyen:
1. Cargar la configuración;
2. Obtener contenido del repositorio;
3. Generar contenido del README;
4. Completar y traducir el README;
5. Confirmar cambios;
6. Proporcionar interfaz de línea de comandos.

## 🌸 ¿Cómo Usar?

Puedes optar por hacer Fork de este proyecto y utilizar `GitHub Actions`, o clonarlo localmente para su uso. A continuación, se explicará el primer método; para el segundo, la configuración queda a tu cargo.

1. Primero, añade `PAT` y `OPENAI_API_KEY` a los Secrets.
2. A continuación, edita `config.json` para configurar los parámetros relevantes.
3. Para generar el README, activa manualmente el flujo de trabajo `generate`.
4. Para optimizar el README, activa manualmente el flujo de trabajo `optimize`.
5. Para traducir el README, activa manualmente el flujo de trabajo `translate`.

## 🌟 ¡Comencemos!

¡No esperes más! Utiliza esta herramienta para mejorar la calidad de la documentación de tu proyecto y atraer a más colaboradores y atención. Si consideras que este proyecto te es útil, ¡danos un 💖 Star! ¡Trabajemos juntos para hacer la comunidad de código abierto aún mejor! 🌈

## 📄 Licencia

Este proyecto utiliza la Licencia Apache; para más detalles, consulta el archivo [LICENSE](LICENSE).

¡Bienvenido a unirte a nosotros y hacer que los README sean más simples y eficientes! 🚀