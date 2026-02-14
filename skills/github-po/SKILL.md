# github-po

Skill para interactuar con GitHub desde OpenClaw. Permite consultar repos, crear issues, o abrir pull requests mediante comandos simples.

Objetivo
- Proveer acciones básicas para gestionar GitHub desde OpenClaw.

Casos de uso (ejemplos)
- github-po repo owner/name --list
- github-po issue owner/name repo "titulo" "descripcion"
- github-po pr owner/name repo "titulo" "descripcion" "branch" 

Arquitectura breve
- Archivos clave en skills/github-po/
- index.js: lógica principal (comportamientos esperados)
- package.json: dependencias y entry point

Disparadores
- comandos con prefijo: github-po, o palabras clave definidas en README

Vivir en
- skills/github-po/

Notas
- Este es un esqueleto inicial. Podemos extenderlo con autenticación, manejo de tokens, y pruebas.
