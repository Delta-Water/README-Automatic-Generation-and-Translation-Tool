[Back to main language README](README.md)

# README: Herramienta de Generación y Traducción Automática de README 📄🌍

## Introducción al Proyecto ✨

¡Bienvenido al proyecto **README-Automatic-Generation-and-Translation-Tool**! Esta herramienta está diseñada para simplificar el proceso de generación y traducción de archivos README en repositorios de GitHub. Al combinar la API de GitHub y la API de OpenAI, nuestra herramienta puede generar automáticamente documentación README completa y soportar traducciones en varios idiomas, haciendo que su proyecto sea más accesible y comprensible para usuarios de todo el mundo.

## Características 🚀

- **Gestión de configuración automatizada**: Carga de configuraciones desde un archivo de configuración.
- **Interacción con la API de GitHub**: Obtiene el contenido de archivos de repositorios de GitHub específicos.
- **Integración de la API de OpenAI**: Utiliza la API de OpenAI para resumir el contenido del archivo y generar texto README atractivo y traducciones.
- **Soporte multilenguaje**: Genera versiones traducidas según configuraciones de idiomas predefinidas.
- **Gestión de README**: Construye un archivo README que incluye una descripción del proyecto, pasos de instalación y más, enlazando las versiones traducidas.
- **Control de versiones**: Después de generar el README y su traducción, envía automáticamente los cambios al repositorio de GitHub, manteniendo el control de versiones.

## Pasos de Instalación ⚙️

Antes de comenzar a usar esta herramienta, asegúrese de tener instaladas las siguientes dependencias:

1. **Clonar este repositorio**:
   ```bash
   git clone https://github.com/Delta-Water/README-Automatic-Generation-and-Translation-Tool.git
   cd README-Automatic-Generation-and-Translation-Tool
   ```

2. **Instalar dependencias**:
   Use `pip` para instalar las bibliotecas necesarias para el proyecto:
   ```bash
   pip install -r requirements.txt
   ```

3. **Archivo de configuración**: Cree o edite el archivo `config.json` en el directorio raíz del proyecto, configurando la URL de la API y otros elementos de configuración.

4. **Configurar la clave de GitHub**: En la sección de "Secrets" de GitHub, configure su token de acceso personal para que la herramienta pueda acceder a su repositorio de GitHub.

## Instrucciones de Uso 📋

1. **Configuración**: Asegúrese de que el archivo `config.json` esté correctamente configurado con la URL base de la API, la rama principal y el índice del lenguaje de programación principal.

2. **Ejecutar la herramienta**: Ejecute el siguiente comando para iniciar la herramienta:
   ```bash
   python tool.py
   ```

3. **Activar manualmente GitHub Actions**: También puede ejecutar manualmente GitHub Actions o configurarlo para que se ejecute automáticamente con nuevos envíos.

## Guía de Contribución 🤝

¡Agradecemos cualquier forma de contribución! Siga estos pasos:
1. **Haga un fork de este repositorio**.
2. **Cree su rama de función**:
   ```bash
   git checkout -b feature/MyFeature
   ```
3. **Realice su cambio**:
   ```bash
   git commit -m "Add some feature"
   ```
4. **Empuje a la rama**:
   ```bash
   git push origin feature/MyFeature
   ```
5. **Envíe una solicitud de extracción**.

¡Gracias por su apoyo a este proyecto! Si tiene alguna pregunta o sugerencia, por favor cree un problema o contacte a los mantenedores del proyecto. 🙏

## Licencia 📜

Este proyecto sigue la **Licencia Apache, Versión 2.0**. Consulte los documentos relevantes para obtener los términos y condiciones detallados, asegurando la legalidad y la equidad en la colaboración y uso.

---

¡Gracias por usar **README-Automatic-Generation-and-Translation-Tool**! ¡Juntos hacemos el código abierto más accesible y colaborativo! 💪