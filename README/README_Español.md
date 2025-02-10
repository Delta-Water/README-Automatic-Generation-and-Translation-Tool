[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) | [English](/README/README_en.md) | [Français](/README/README_fr.md) | [Deutsch](/README/README_de.md) | [日本語](/README/README_ja.md)

- [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al proyecto **README-Automatic-Generation-and-Translation-Tool**! 🎉 Este proyecto está diseñado para simplificar la generación y traducción de la documentación de su proyecto en GitHub, haciendo que su archivo README sea más profesional y multilingüe, ¡para que pueda atraer fácilmente a más desarrolladores sin importar dónde se encuentre! 🌍✨

## 🚀 Estructura del Proyecto

A continuación se muestra un resumen de la estructura del proyecto:

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # Archivo de flujo de trabajo de GitHub Actions
│
├── LICENSE            # Licencia Apache 2.0
│
├── README.md          # Archivo README principal del proyecto
│
├── README/
│   ├── README_Deutsch.md     # README en alemán 
│   ├── README_English.md      # README en inglés 
│   ├── README_Español.md      # README en español 
│   ├── README_Français.md     # README en francés 
│   ├── README_日本語.md        # README en japonés 
│   └── README_繁体中文.md      # README en chino tradicional 
│
├── config.json       # Archivo de configuración, incluyendo parámetros y lenguajes de traducción
│
├── requirements.txt   # Bibliotecas necesarias para el proyecto
│
└── tool.py            # Script principal para la generación y traducción automáticas de README
```

## 📜 Resumen de la Licencia

Nuestro proyecto utiliza la **Licencia Apache 2.0**, lo que significa que puede usar, modificar y distribuir nuestro código libremente, siempre que se mantenga la licencia original y las declaraciones correspondientes. 📝 ¡Promovamos juntos la colaboración en código abierto! 💪

## ⚙️ Archivo de Configuración

`config.json` es el centro de configuración de su proyecto. Permite establecer parámetros relevantes, como el nombre del repositorio, la información del propietario y los lenguajes de traducción admitidos (chino simplificado, chino tradicional, inglés, español, francés, alemán, japonés), lo que le permite cambiar y gestionar fácilmente el contenido multilingüe. 🌐💻

## 📦 Bibliotecas Necesarias

Nuestro proyecto depende de las siguientes bibliotecas, asegurando que pueda configurar su entorno de desarrollo fácilmente:

1. **requests** - Biblioteca sencilla para solicitudes HTTP.
2. **openai** - Biblioteca para interactuar con la API de OpenAI.
3. **GitPython** - Biblioteca para operar repositorios Git mediante Python.

Solo necesita ejecutar el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## ⚙️ Resumen de Funciones

El script `tool.py` ofrece potentes funciones, que incluyen:

1. **Carga de configuración** - Lee los parámetros del proyecto desde el archivo de configuración.
2. **Interacción con el repositorio** - Obtiene archivos y su contenido del repositorio a través de la API de GitHub.
3. **Resumen de contenido** - Utiliza la API de OpenAI para resumir el contenido de los archivos del repositorio y generar descripciones concisas.
4. **Generación de README** - Genera un archivo README profesional basado en la estructura de los archivos y la información resumida.
5. **Traducción** - Traduce el contenido del README a varios idiomas, ¡manteniendo emojis y estilos llamativos! 😄🎨
6. **Operaciones de Git** - Envía los archivos README y traducciones actualizados al repositorio.

## 🚀 Comienza Tu Viaje

Solo necesita iniciar manualmente el flujo de trabajo de GitHub Actions, esperar unos minutos, y un excelente archivo README se generará y traducirá automáticamente, ¡así podrá disfrutar de todo su esplendor! ✨

### 🌟 ¡Ven a darnos una estrella! ¡Su apoyo es nuestra motivación para seguir adelante! 💖

¡Gracias por su atención y apoyo! Si tiene alguna pregunta o sugerencia, no dude en contactarnos en GitHub. ¡Esperamos crear juntos una mejor comunidad de código abierto! 🤝