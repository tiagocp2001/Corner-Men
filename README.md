# Corner Men

Jogo de gestão de um ginásio de boxe, em pixel art. Joga-se no browser, funciona offline e pode ser adicionado ao ecrã principal do telemóvel.

## Publicar (GitHub Pages)
Settings → Pages → Source: *Deploy from a branch* → Branch: `main` / `(root)` → Save.
O link fica `https://<utilizador>.github.io/<repositório>/`.

## Atualizar
Substitui `index.html` e faz commit. Quem tiver o jogo recebe a versão nova da próxima vez que o abrir com internet.
O progresso de cada jogador fica guardado no próprio telemóvel e não se perde com atualizações.

## Como atualizar a partir do artefacto do Claude
1. Descarregar o `index.html` mais recente do artefacto "Ginásio Esperança".
2. `python3 build.py <caminho para esse index.html>` — aplica nome, ícone, modo offline, correção do fundo, e mostra a versão (ex.: `v5 · 05 nov 2026`) no fundo do ecrã.
3. Commit e push para `main`. O GitHub Pages republica em 1–2 minutos.
