# github-po

Skill para interactuar con GitHub desde OpenClaw.

## Objetivo

Proveer acciones básicas para gestionar repositorios, crear issues y pull requests vía comandos simples en OpenClaw.

## Instalación

Este skill ya está instalado en skills/github-po/. No requiere pasos adicionales.

## Uso básico

- `github-po repo owner/name --list`: listar repos de un usuario
- `github-po issue owner/name repo "titulo" "descripcion"`: crear issue
- `github-po pr owner/name repo "titulo" "descripcion" "branch"`: crear pull request

## Autenticación

**Requerido para crear issues y PRs.**  

1. Obtén un token en https://github.com/settings/tokens
2. Configura tu token en `.env`:
   ```
   GITHUB_TOKEN=ghp_xxxxxxxxxxxx
   ```
3. **Importante:** Agrega `.env` a `.gitignore`

Nota: El listado de repos funciona sin autenticación.

## Desarrollo

- index.js: Lógica principal del skill
- package.json: Dependencias y scripts
- SKILL.md: Documentación del skill (este archivo)

## Estado

Versión inicial del esqueleto. Se puede extender según necesidades.
