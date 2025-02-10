- [切换语言: 简体中文](/README.md) | - [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al proyecto **README-Automatic-Generation-and-Translation-Tool**! 🎉 Este proyecto tiene como objetivo simplificar la generación y traducción de la documentación de su proyecto en GitHub, haciendo que su archivo README sea más profesional y multilingüe, ¡sin importar dónde esté, podrá atraer fácilmente a más desarrolladores! 🌍✨

## 🚀 Estructura del Proyecto

A continuación se presenta un resumen de la estructura del proyecto:

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
├── config.json       # Archivo de configuración, incluye ajustes y lenguajes de traducción
│
├── requirements.txt   # Librerías requeridas por el proyecto
│
└── tool.py            # Script principal para generar y traducir el README
```

## 📜 Resumen de la Licencia

Nuestro proyecto utiliza la **Licencia Apache 2.0**, lo que significa que puede usar, modificar y distribuir nuestro código libremente, siempre y cuando conserve la licencia original y las declaraciones correspondientes. 📝 ¡Promovamos juntos la colaboración en código abierto! 💪

## ⚙️ Archivo de Configuración

`config.json` es el centro de configuración de su proyecto. Le permite establecer parámetros relevantes, como el nombre del repositorio, información del propietario y los lenguajes de traducción compatibles (chino simplificado, chino tradicional, inglés, español, francés, alemán, japonés), para que pueda cambiar y gestionar fácilmente el contenido multilingüe. 🌐💻

## 📦 Librerías Requeridas

Nuestro proyecto depende de las siguientes bibliotecas para garantizar que pueda configurar su entorno de desarrollo de manera sencilla:

1. **requests** - Biblioteca simple para realizar solicitudes HTTP.
2. **openai** - Biblioteca para interactuar con la API de OpenAI.
3. **GitPython** - Biblioteca para operar con repositorios Git desde Python.

Solo necesita ejecutar el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## ⚙️ Resumen de Funcionalidades

El script `tool.py` ofrece potentes funcionalidades, que incluyen:

1. **Carga de configuración** - Leer los parámetros del proyecto desde el archivo de configuración.
2. **Interacción con el repositorio** - Obtener archivos del repositorio y su contenido a través de la API de GitHub.
3. **Resumen de contenido** - Utilizar la API de OpenAI para resumir el contenido de los archivos del repositorio, generando descripciones concisas.
4. **Generación de README** - Crear un README profesional basado en la estructura de archivos y la información resumida.
5. **Traducción** - Traducir el contenido del README a varios idiomas, manteniendo emojis y estilo vibrante. 😄🎨
6. **Operaciones de Git** - Confirmar el README actualizado y los archivos traducidos en el repositorio.

## 🚀 Comienza tu Aventura

Simplemente inicie manualmente el flujo de trabajo de GitHub Actions, espere unos minutos, y un excelente archivo README será generado y traducido automáticamente, ¡puede disfrutar de todo lo que esto ofrece! ✨

### 🌟 ¡Ven y danos estrellas! Tu apoyo es nuestra motivación para seguir avanzando! 💖

¡Gracias por su atención y apoyo! Si tiene alguna pregunta o sugerencia, no dude en contactarnos en GitHub. ¡Esperamos crear juntos una comunidad de código abierto aún mejor! 🤝