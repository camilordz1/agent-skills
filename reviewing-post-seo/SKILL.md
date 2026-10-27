---
name: reviewing-post-seo
description: Revisa los básicos de SEO de un artículo de blog en Markdown (título, descripción, slug, encabezados, imágenes y enlaces) y devuelve un informe con errores y avisos. Úsala cuando el usuario pida revisar, auditar o dejar listo para publicar un post, aunque no mencione "SEO".
license: MIT
metadata:
  version: "1.0"
---

# Revisión SEO básica de un post

## Pasos

1. Localiza el archivo `.md` del post. Si el usuario no lo indica, pregunta cuál es.
2. Ejecuta el script con la ruta del archivo:

   ```bash
   python3 scripts/check_post.py ruta/al/post.md
   ```

3. Lee el informe. Cada línea empieza por `ERROR` (hay que corregirlo) o `AVISO` (conviene revisarlo).
4. Resume al usuario los hallazgos, del más grave al menos grave, y propone una corrección concreta para cada uno. No reescribas el post si no te lo piden.
5. Si el script termina con código 2, el archivo no se pudo leer o no tiene front matter: díselo al usuario y no inventes un informe.

## Reglas

- Los umbrales (60 caracteres de título, 70 a 160 de descripción) son convenciones editoriales, no reglas de Google. Si el usuario usa otros, edita `references/umbrales.md` y las constantes del script.
- El script solo revisa lo que se puede medir. No juzgues la calidad del contenido ni la intención de búsqueda salvo que te lo pidan.
- No modifiques el archivo del post durante la revisión.

## Más detalle

Para saber por qué existe cada regla y cómo cambiarla, lee `references/umbrales.md`.
