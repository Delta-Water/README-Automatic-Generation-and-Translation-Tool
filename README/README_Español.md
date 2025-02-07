[Back to main language README](README.md)

# README - Herramienta de Generación y Traducción Automática de README 🚀

## Introducción del Proyecto 📜
Este proyecto se llama **README-Automatic-Generation-and-Translation-Tool**, desarrollado por **Delta-Water**. Su objetivo es automatizar la generación y traducción de archivos README en repositorios de GitHub. Utilizando la API de GitHub y los servicios de OpenAI, esta herramienta puede extraer de manera eficiente el contenido de los archivos, generar texto README y traducirlo a múltiples idiomas, para que usuarios de todo el mundo puedan entenderlo y usarlo fácilmente.

## Licencia 📄
Este proyecto sigue la Licencia Apache, versión 2.0. Esta licencia describe los términos y condiciones para el uso, copia y distribución del software y otras obras, además de definir varios términos clave, como "licenciante", "usted", "obra", "obras derivadas" y "contribuciones". Se le otorgará un derecho perpetuo, de alcance global, no exclusivo y libre de regalías para usar este proyecto y sus obras derivadas. Para obtener más información sobre la licencia, consulte el archivo `LICENSE`.

## Preparación del Entorno ⚙️

Antes de comenzar a usar esta herramienta, debe asegurarse de que tiene instaladas las dependencias necesarias. Este proyecto depende de las siguientes bibliotecas:

1. **requests** - Una biblioteca popular para realizar solicitudes HTTP de manera sencilla.
2. **openai** - Una biblioteca para acceder a los servicios y modelos de OpenAI, que ayuda a integrar capacidades avanzadas de inteligencia artificial.
3. **GitPython** - Una biblioteca para interactuar programáticamente con repositorios Git, facilitando las operaciones de control de versiones.

Puede instalar estas dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Instrucciones de Uso 📚

1. **Carga de Configuración**: La herramienta cargará la configuración desde el archivo `config.json`, y deberá modificar este archivo según sea necesario. La información básica incluye la URL base de la API y el índice del idioma principal, entre otros.

2. **Interacción con GitHub**: La herramienta utilizará la API de GitHub para recuperar el contenido de los archivos del repositorio especificado.

3. **Integración con OpenAI**: Aprovechando la API de OpenAI, resumirá el contenido del archivo, generará el texto README y realizará los procesos de traducción.

4. **Gestión de Traducciones**: Esta herramienta admite la traducción de los documentos README generados a múltiples idiomas, y formateará los resultados de traducción.

5. **Actualización del README**: La herramienta construirá el README principal y añadirá enlaces a las versiones traducidas, y finalmente, enviará los cambios al repositorio original.

6. **Manejo de Errores**: Incluye manejo de errores, pudiendo imprimir mensajes en diversas etapas de operación para detectar problemas de manera temprana.

## Guía de Contribución 💡

¡Te invitamos a contribuir a este proyecto! Si tienes ideas o sugerencias, sigue estos pasos para participar en la contribución:

1. Haz un fork de este repositorio.
2. Realiza modificaciones en tu rama.
3. Envía un Pull Request.

Asegúrate de seguir las normas de codificación y el proceso de contribución del proyecto. Tu contribución será revisada con seriedad y ayudará a mejorar la funcionalidad y usabilidad de esta herramienta.

## Contáctanos 📫

Si tienes preguntas o comentarios, no dudes en contactarnos a través de GitHub Issues o directamente con el autor **Delta-Water**.

¡Gracias por elegir **README-Automatic-Generation-and-Translation-Tool**, esperamos tus comentarios y contribuciones! 🌟