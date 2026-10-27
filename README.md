# Agent Skills de Camilordz

Skills para agentes de IA (Claude Code, Codex y otras herramientas compatibles con el estándar abierto [Agent Skills](https://agentskills.io)).

Cada carpeta es una skill: un `SKILL.md` con nombre, descripción e instrucciones, y archivos de apoyo si hacen falta.

## Skills

| Skill | Qué hace |
| --- | --- |
| [`reviewing-post-seo`](reviewing-post-seo/) | Revisa los básicos de SEO de un post en Markdown antes de publicarlo: título, descripción, slug, encabezados, imágenes sin texto alternativo y enlaces internos. |

La explicación completa, con cómo se armó y cómo se probó, está en el artículo [Cómo crear skills para agentes de IA: recomendaciones y un ejemplo](https://camilordz.com/blog/crear-skills-agentes-ia/).

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/camilordz1/agent-skills.git
```

Después copia la carpeta de la skill donde tu herramienta la busca:

| Herramienta | Para todos tus proyectos | Solo para un proyecto |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` |
| Codex | `~/.agents/skills/` | `.agents/skills/` |

Por ejemplo, en Claude Code:

```bash
cp -r agent-skills/reviewing-post-seo ~/.claude/skills/
```

Abre una sesión nueva y pide algo como "revisa este post antes de publicarlo: `ruta/al/post.md`".

## Requisitos

`reviewing-post-seo` usa un script de Python 3 que solo necesita la biblioteca estándar. No hay nada que instalar.

## Antes de instalar cualquier skill

Una skill trae instrucciones y código que el agente ejecuta en tu equipo. Lee los archivos antes de instalarla, incluidas las de este repositorio.

## Licencia

[MIT](LICENSE).
