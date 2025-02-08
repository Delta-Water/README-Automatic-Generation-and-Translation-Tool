- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - Herramienta de Generación y Traducción Automática 🌟

¡Bienvenido al proyecto **README-Herramienta-de-Generación-y-Traducción-Automática**! 🚀

Nos dedicamos a proporcionar a los desarrolladores una herramienta automática para generar y traducir fácilmente los archivos README de proyectos en GitHub, ¡haciendo que la documentación de tu proyecto sea más atractiva y profesional!💕 

## Estructura del Proyecto 📂

A continuación se muestra la estructura actual del proyecto, con descripciones de los diferentes archivos:

```
├── .github
│   └── workflows
│       └── main.yml     # Archivo de configuración del flujo de trabajo de GitHub Actions
├── LICENSE                # Archivo de licencia del proyecto
├── README.md              # Documentación principal del proyecto
├── README
│   ├── README_Deutsch.md  # Archivo README en alemán
│   ├── README_English.md  # Archivo README en inglés
│   ├── README_Español.md  # Archivo README en español
│   ├── README_Français.md # Archivo README en francés
│   ├── README_日本語.md    # Archivo README en japonés
│   └── README_繁体中文.md   # Archivo README en chino tradicional
├── config.json            # Archivo de configuración del proyecto
├── requirements.txt       # Lista de bibliotecas de dependencias de Python
└── tool.py                # Script para generar y actualizar automáticamente el archivo README
```

## Resumen de Archivos 📄

### 1. `.github/workflows/main.yml`
Este archivo de configuración del flujo de trabajo de GitHub Actions nos ayuda a automatizar la generación y traducción de archivos README. Se ejecuta en el entorno de la última versión de Ubuntu y realiza los siguientes pasos:

- **Chequeo del código**: Obtener el código más reciente.
- **Configuración de Python**: Configurar Python 3.8 como entorno.
- **Instalación de dependencias**: Actualizar pip e instalar los paquetes de Python necesarios (requests, openai, GitPython).
- **Ejecutar script**: Ejecutar el script de Python (tool.py), utilizando las credenciales de la API de GitHub y OpenAI para generar el README.

### 2. `LICENSE`
Este archivo contiene la versión 2.0 de la licencia Apache, que describe los términos y condiciones para el uso, copia y distribución de software y otras obras. La licencia proporciona un marco legal que fomenta el desarrollo de software de código abierto y protege los derechos de los contribuyentes y usuarios.

### 3. `config.json`
Este archivo de configuración define los parámetros importantes del proyecto, como: nombre del repositorio, propietario, URL básica de la API y rama por defecto (main). Soporta la generación y traducción automática del archivo README.

### 4. `requirements.txt`
Lista las bibliotecas de dependencias necesarias para el proyecto de Python, que incluyen:

- **requests**: Biblioteca popular para simplificar solicitudes HTTP.
- **openai**: Biblioteca para interactuar con la API de OpenAI.
- **GitPython**: Biblioteca para operar e interactuar con repositorios de Git directamente desde Python.

### 5. `tool.py`
Este script automatiza la generación y actualización de archivos README en repositorios de GitHub y sus traducciones. Sus funciones clave incluyen:

1. **Configuración y ajustes**: Cargar la configuración y obtener las variables de entorno necesarias.
2. **Gestión de archivos**: Acceder al repositorio de GitHub para obtener la estructura y contenido de los archivos.
3. **Generación de README**: Utilizar la API de OpenAI para generar un README detallado.
4. **Creación de traducciones**: Traducir el README generado a múltiples idiomas.
5. **Integración de enlaces y estructura**: Mejorar la navegabilidad.
6. **Confirmar y enviar**: Subir los archivos actualizados al repositorio de GitHub.

## Comenzar Rápido 🚀

¿Quieres participar? ¡Haz clic en la ⭐ en la esquina superior derecha para disfrutar de nuestro proyecto! 💖 

Con esta herramienta, ayudamos a que cada desarrollador pueda mantener fácilmente la documentación de su proyecto, mejorando el nivel de internacionalización del mismo. ¡No importa si tu proyecto es grande o pequeño, te ayudamos a deshacerte de las preocupaciones en la documentación y a construir juntos un mejor ecosistema de código abierto! 🌍👩‍💻👨‍💻

Si tienes alguna pregunta o sugerencia, ¡no dudes en contactarnos! ¡feliz codificación! 🎉