- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Herramienta de Generación y Traducción Automática de README

¡Bienvenido al proyecto **README-Automatic-Generation-and-Translation-Tool**! 🎉 Este proyecto tiene como objetivo simplificar la generación y traducción de la documentación de su proyecto en GitHub, haciendo que su archivo README sea más profesional y multilingüe, ¡para que pueda atraer fácilmente a más desarrolladores sin importar dónde se encuentre! 🌍✨

## 🚀 Estructura del Proyecto

A continuación se muestra una visión general de la estructura del proyecto:

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
├── config.json       # Archivo de configuración que incluye ajustes y lenguajes de traducción
│
├── requirements.txt   # Dependencias necesarias para el proyecto
│
└── tool.py            # Script principal para la generación y traducción automática de README
```

## 📜 Resumen de la Licencia

Nuestro proyecto utiliza la **Licencia Apache 2.0**, lo que significa que puede usar, modificar y distribuir nuestro código libremente, pero debe mantener la licencia original y las declaraciones correspondientes. 📝 ¡Promovamos juntos la colaboración en código abierto! 💪

## ⚙️ Archivo de Configuración

`config.json` es el centro de configuración de su proyecto. Le permite establecer parámetros relevantes, como el nombre del repositorio, la información del propietario y los idiomas de traducción soportados (chino simplificado, chino tradicional, inglés, español, francés, alemán, japonés), lo que le permite cambiar y gestionar fácilmente el contenido multilingüe. 🌐💻

## 📦 Dependencias

Nuestro proyecto depende de las siguientes bibliotecas, asegurando que pueda preparar su entorno de desarrollo sin complicaciones:

1. **requests** - Biblioteca simple para realizar peticiones HTTP.
2. **openai** - Biblioteca para interactuar con la API de OpenAI.
3. **GitPython** - Biblioteca para operar repositorios Git a través de Python.

Solo necesita ejecutar el siguiente comando para instalar las dependencias:

```bash
pip install -r requirements.txt
```

## ⚙️ Resumen de Funciones

El script `tool.py` ofrece potentes funciones, incluyendo:

1. **Carga de Configuración** - Leer parámetros del proyecto desde el archivo de configuración.
2. **Interacción con Repositorio** - Obtener archivos y contenidos del repositorio a través de la API de GitHub.
3. **Resumen de Contenidos** - Usar la API de OpenAI para resumir el contenido de los archivos del repositorio y generar descripciones concisas.
4. **Generación de README** - Generar archivos README profesionales basados en la estructura de archivos y la información resumida.
5. **Traducción** - Traducir el contenido del README a varios idiomas, conservando emojis y estilo vibrante. 😄🎨
6. **Operaciones de Git** - Confirmar los archivos README y de traducción actualizados en el repositorio.

## 🚀 Comienza tu Viaje

Solo necesita iniciar manualmente el flujo de trabajo de GitHub Actions y esperar unos minutos; un excelente archivo README se generará automáticamente y estará traducido para que pueda disfrutar de todo lo hermoso que esto trae. ✨

### 🌟 ¡Ven y danos estrellas! ¡Su apoyo es lo que nos impulsa a seguir adelante! 💖

¡Gracias por su atención y apoyo! Si tiene alguna pregunta o sugerencia, no dude en contactarnos en GitHub. ¡Esperamos crear juntos una comunidad de código abierto aún mejor! 🤝