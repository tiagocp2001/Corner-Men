# CLAUDE.md — Corner Men

Contexto para o Claude trabalhar neste repositório. Lê isto antes de mexer em qualquer coisa.

## O que é

**Corner Men** é um jogo de gestão de um ginásio de boxe, em pixel art, para telemóvel (vertical), inspirado no anime *Hajime no Ippo*. O jogador é o dono de um ginásio de bairro pobre: treina atletas, marca lutas, ganha dinheiro e popularidade, melhora o ginásio e sobe do Amador ao título Mundial.

- Autor/dono: Tiago Pereira (projeto pessoal, sem experiência prévia em desenvolvimento de jogos).
- Língua do jogo e da conversa: **português de Portugal (PT-PT)**. Todos os textos do jogo, comentários do comentador e mensagens ao Tiago são em PT-PT.
- Jogo online: https://tiagocp2001.github.io/Corner-Men/ (GitHub Pages, branch `main`, raiz).

## Estrutura do repositório

| Ficheiro | O que é |
|---|---|
| `index.html` | O jogo inteiro: HTML + CSS + JS num só ficheiro (~200 KB). **É a fonte do jogo**: edita-se diretamente. |
| `publicar.py` | Prepara uma versão para publicar: sobe a `VERSION` do `sw.js`, atualiza a etiqueta (`vN · dia mês ano`) e confirma que a `KEY` não mudou. |
| `docs/` | `design.md` (decisões de design, a referência), o Guia de Boxe do Tiago (PDF e texto). |
| `sw.js` | Service worker: página network-first (atualiza sozinho com internet, funciona offline), resto cache-first. |
| `manifest.json` | PWA (adicionar ao ecrã principal), `lang: pt-PT`, orientação vertical. |
| `icons/` | Ícones 180/192/512. |

### Fluxo de atualização

A fonte do jogo é o **`index.html` do repositório** (até à v9 era um artefacto do Claude transformado pelo antigo `build.py`; isso acabou — não voltar a usar o artefacto antigo, perdia todas as mudanças feitas depois). Para publicar:

1. Trabalhar e testar no branch de trabalho.
2. `python3 publicar.py` — sobe a versão do `sw.js`, atualiza a etiqueta e verifica a `KEY`.
3. Levar para o `main` e fazer push. O GitHub Pages republica em 1–2 minutos.

**Antes de enviar:** confirmar que a chave do save (`const KEY='corner-men-v6'` no código) **não mudou** sem o Tiago saber. Mudar a chave apaga o progresso de todos os jogadores. Só se muda de propósito (ex.: mudanças de regras incompatíveis, quando o Tiago diz "começa de novo").

## Arquitetura do jogo (`index.html`)

Tudo dentro de uma IIFE num único `<script>`. Sem dependências externas além da fonte "Press Start 2P" (Google Fonts). Gráficos em `<canvas>` desenhados à mão (pixel art com `fillRect`), som gerado com Web Audio. Estado guardado em `localStorage`.

Secções (procurar pelos comentários `/* ===== X ===== */`):

| Secção | Conteúdo principal |
|---|---|
| `DATA` | `CATS` (Pena, Superpena, Ligeiro, Pesado), `CATMOD`, `GIFTS` (talentos escondidos), `TIERS` (Amador → Regional → Nacional → Mundial), `ECON`, `EQ` (equipamento), `UPG` (melhorias e treinadores), `TR` (treinos), `SKILLS` (golpes), `DEFS` (defesas), `COMBOS`, `STRAT` (estratégias de luta), `TUNE` |
| body / style levels | Altura e alcance (`H_BASE`, `rollBody`, `bodyType`: Compacto/Médio/Longo), níveis de estilo 0–5 (`sty`, `styleCap`, `styleFit`, `addStyleXP`), efeitos físicos na luta (`phys`, `skillF`, `sf`, `topF`) |
| `STATE` | `newGame`, `makeAthlete`, `save`/`load`, `KEY` |
| `OFFERS` | Propostas de luta, `makeOpp` (adversários de academias rivais), scouting |
| `SOUND` | `SFX` — sons 8-bit gerados (sem ficheiros) |
| `RENDER` | UI em menus num ecrã fixo: separadores Ginásio / Atletas (Ficha → Atributos/Golpes, Plano) / Lutas / Loja |
| `MODALS`, `INPUT` | `modal`, `info`, handler global de cliques (`data-*`) |
| `WEEK` | `advanceWeek`: treinos, fadiga, decadência física, economia, eventos, resumo semanal de planos |
| `GYM WORLD` | Ginásio animado em canvas 240×136: membros e atletas a treinar, treinadores a circular, sons ambiente |
| `FIGHT` | Simulação da luta (`runFight`, `exchange`, `punch`, `knockdown`, `corner`, `preTalk`), entrada no ringue, cerimónia final |
| arena drawing | Arena em vista frontal elevada (`buildArena`, `proj`/`unproj`), 4 locais por escalão, público, `ringLoop` |
| corner men | Treinadores nos cantos (`makeCrew`, `crewUpdate`, `drawCrew`) |
| `BOOT` | Menu inicial / pausa (`menu`, `pauseMenu`), `start()` |

### Sistemas principais (resumo)

- **Atletas:** 5 atributos (Força, Velocidade, Resistência, Defesa, Técnica) com potencial, idade, traço de personalidade, estilo e níveis de estilo, golpes e defesas com níveis 1–5, fadiga, confiança e forma, altura e alcance. Talento escondido com probabilidade 1/15. O primeiro atleta é **sempre peso Pena**; o resto é aleatório.
- **Plano semanal:** 3 treinos por semana; o plano tem de ser revisto todas as semanas (resumo antes de avançar e badges). Os atributos físicos sem treino durante mais de 3 semanas perdem condição, com mínimo.
- **Estilos:** triângulo clássico — **In-fighter > Outboxer > Puncher > In-fighter**. A força da vantagem cresce com o nível do estilo (quase nada no amador, completa no topo). O corpo define o nível máximo de cada estilo. Novos estilos aprendem-se com treinadores especialistas da loja. Na luta escolhe-se o estilo antes do combate e pode trocar-se no intervalo (nível ≥ 2). Os adversários de Nacional/Mundial também trocam.
- **Estratégias de luta:** Pressão / Equilibrado / Cautela.
- **Golpes:** jab, direto, gancho, uppercut, direto ao corpo, gancho ao fígado, Contra-golpe (dispara depois de uma defesa). Combinações desbloqueiam com os golpes.
- **Luta:** rounds de 3 minutos, fôlego, vida, quedas, quedas relâmpago, KO/TKO/médico/toalha/decisão, perguntas no canto (tática certa, meia certa ou errada), comentador "Zé do Micro", cantos com corner men, entrada no ringue e cerimónia com cinturão e confetis.
- **Economia:** quota fixa dos sócios, renda, manutenção, salários, patrocínios, prémios por escalão, negociação de salários.

## Equilíbrio (muito importante)

> **Fase atual:** primeiro define-se como cada sistema funciona; o equilíbrio (simulações e afinação de números) fica para depois, quando o Tiago disser. Até lá, não afinar números nem fazer estudos de equilíbrio — basta confirmar que nada parte.

Todo o equilíbrio passa pelo objeto `TUNE` (pode ser sobreposto com `window.__TUNE` para testes). **Nunca afinar números "a olho"**: o Tiago espera que cada mudança de regras seja **testada com simulações** e que os resultados lhe sejam mostrados.

Princípio do Tiago: **"no ringue tudo pode acontecer"** — as vantagens individuais (estilo, talento, corpo, alcance) devem ser **pequenas**.

Alvos atuais (lutas contra adversário igual, exceto no fator testado):

| Medida | Alvo |
|---|---|
| Espelho | ~50% |
| Estilo certo | ~55% amador → ~60–63% topo |
| +10 cm de alcance | ~50% amador → ~55–57% topo |
| Corpo a combinar com o estilo | quase nada no amador → ~55% topo |
| Contra-golpe nível 5 vs 0 | ~55% |
| Tudo a favor no topo | ≤ ~65–68% |
| +5 / +15 em todos os atributos | ~66% / ~85–92% |
| KOs | amador ~5%; nível médio leves 30–40%, Pesados ~55%; topo leves ~40%, Pesados ~60% |
| Fôlego (Equilibrado) | fim do R1 ~65, desce aos poucos; Pressão chega a ~20 no R3; Cautela mantém-se alto |
| Carreira (potencial ~70) | título Amador ~1,5 anos, Regional ~2,5, Nacional ~3,5–4 |

### Como simular

As simulações correm o próprio jogo num Chromium headless (Playwright) com um build de teste que:
- define `window.__SIM` (tempos de espera instantâneos, salta a entrada no ringue e a cerimónia);
- expõe `window.__sim(n, A, B, rounds)`, que corre `n` lutas entre dois atletas descritos por `{cat, lvl, sk, style, slv, strat, ctr, dh, dr, ...}` e devolve os resultados.

O build de teste gera-se a partir do `index.html` por substituição de texto (os scripts antigos, `mksim.py` e `runsim*.py`, viviam fora do repositório). Notas práticas:
- Correr em blocos de ~50 lutas por página e reabrir a página, porque uma página com centenas de lutas esgota a memória.
- O botão inicial do menu é `#mNew`, depois `#gOk` (criar ginásio) e `#mOk` (ajuda).
- Com 150–200 lutas por teste o ruído é de ±4%. Não tirar conclusões de diferenças menores do que isso.

## Regras de trabalho com o Tiago

- **Quando ele diz "responde antes de fazeres" (ou "explica antes"), não implementar nada:** explicar o plano e fazer perguntas, e só avançar depois de ele confirmar.
- Não avisar o Tiago de pequenas alterações de arrumação (documentação, notas, commits de rotina); só falar delas se houver uma razão importante.
- Fazer perguntas quando há decisões de design em aberto, em vez de assumir. Ele gosta de conversar sobre o design, tema a tema.
- **Ecrã fixo, sem scroll:** tudo tem de caber num ecrã de telemóvel vertical, com navegação por menus e separadores. Verificar com capturas a 390×720/760.
- Pixel art coerente (fonte Press Start 2P, paleta quente; o vermelho é o teu canto e o azul o adversário). Atletas originais, **não** personagens do Hajime no Ippo.
- O teu canto fica **à frente à esquerda**; o adversário ao fundo à direita.
- Depois de cada mudança: `node --check` ao script extraído, um teste headless sem erros de página e capturas de ecrã para confirmar o aspeto.
- Explicar os resultados de forma clara em PT-PT, com números das simulações quando houver mudanças de regras.
- Os jogos guardados dos jogadores são sagrados: migrar dados antigos em `start()` sempre que possível, em vez de mudar a `KEY`.

## Adiado (não começar sem perguntar)

- Melhorias de fim de jogo (o dinheiro acumula a partir do 3.º ano).
- Acelerar o título Amador.
- Animações próprias dos golpes ao corpo.
- Golpe especial.

## Em discussão: alinhar o jogo com o "Guia Completo de Boxe"

O Tiago quer o jogo baseado num guia de boxe que escreveu. **As decisões, o plano por fases e o estado de cada tema estão em `docs/design.md` — é a referência; mantê-lo atualizado.** Os temas estão a ser decididos um a um, e **nada disto está implementado**:

1. **Golpes:** numeração 1–6 (frente/trás), overhand, cabeça/corpo como alvo, variações (jab duplo, power jab, flicker jab, check hook, shovel hook, cross-counter…), que treino ensina cada golpe, uso dos números pelo comentador.
2. Combinações clássicas (1-2, 1-1-2, 1-2-3, 1-2-3-2, 2-3-2, 1-6-3-2, gancho duplo, mudança de nível) e fintas.
3. Defesa em 6 famílias (bloqueio, parry, movimento de cabeça, ombro, pés, clinch), cada uma a abrir um contra-golpe específico.
4. Contra-ataque: antes, ao mesmo tempo e depois.
5. Pés, distância (longa/média/curta) e controlo do ringue.
6. Estilos: possíveis híbridos Counter-puncher e Boxer-puncher.
7. Guarda ortodoxa/canhota (southpaw) e trocar de guarda.
8. Atributos físicos, técnicos e mentais (proposta: juntar Pés, Queixo e Ring IQ aos 5 atuais).
9. Treinos novos: saco duplo, maize bag, escada, sparring leve/condicionado/duro, clinch work, HIIT, core/pescoço.
10. Treino mental/tático: vídeos do adversário, plano de combate, peso/pesagem.
11. Faltas e golpes ilegais.
12. Como tudo isto cabe num ecrã fixo.

Último ponto aberto: ver `docs/design.md` (neste momento, **pés, distância e controlo do ringue**).
