# Umbrales del informe

| Comprobación | Nivel | Regla por defecto | Motivo |
| --- | --- | --- | --- |
| Título presente | ERROR | `title` no vacío | Sin título no hay enlace en los resultados |
| Título largo | AVISO | más de 60 caracteres | Google lo acorta si no cabe; no hay un límite oficial |
| Descripción presente | ERROR | `description` no vacía | Sin ella el buscador improvisa el fragmento |
| Descripción corta o larga | AVISO | menos de 70 o más de 160 caracteres | Convención editorial para que el fragmento se lea completo |
| Slug válido | ERROR | solo minúsculas, números y guiones | URLs limpias y estables |
| Encabezado H1 en el cuerpo | AVISO | no debería haber `# ` | La plantilla ya pinta el título como H1 |
| Saltos de nivel | AVISO | un H2 no puede saltar a H4 | Estructura legible para lectores y buscadores |
| Imágenes sin alt | ERROR | `![](...)` con texto alternativo vacío | Accesibilidad y contexto de la imagen |
| Enlaces internos | AVISO | al menos uno que empiece por `/` | Ayuda a descubrir otras páginas del sitio |

Para cambiar un umbral, edita las constantes al inicio de `scripts/check_post.py`.
