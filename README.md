# skill-thumbgenerator

Pesquisa sobre thumbnails de vídeos de Roblox (PT-BR) e uma skill do Claude para analisar e melhorar thumbnails.

## Conteúdo
- `pesquisa/01-relatorio.md` — resumo executivo, método, cobertura, limitações, comparação entre vídeos, referências, recomendações e checklist (consulta em 01/11/2026)
- `pesquisa/02-inventario.md` — 57 vídeos com título, data, duração, views e links do vídeo e da thumbnail
- `pesquisa/03-auditorias.md` — auditoria individual de cada thumbnail
- `roblox-thumbnail-analyzer/` — a skill
  - `SKILL.md` — fluxo principal
  - `references/criterios.md`, `padroes-roblox.md`, `modelo-resposta.md`, `exemplos.md`
  - `scripts/fetch_thumb.py` — baixa a thumbnail pelo ID do vídeo e gera uma prévia de 160 px

## Instalar a skill
Claude Code: copie a pasta para `~/.claude/skills/` (uso pessoal) ou para `.claude/skills/` de um projeto.

    cp -r roblox-thumbnail-analyzer ~/.claude/skills/

Claude.ai: compacte a pasta em um .zip e envie pela seção de Skills nas configurações.

As imagens analisadas não estão no repositório porque pertencem aos criadores. Os links diretos estão no inventário.
