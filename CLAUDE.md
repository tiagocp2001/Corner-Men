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

**Antes de enviar:** confirmar que a chave do save (`const KEY='corner-men-v8'` no código; passou de v6 para v7 na fase A e de v7 para v8 na fase 3A — a 3A recomeça os jogos, por decisão do Tiago —, com um aviso único no menu a quem tinha um save antigo) **não mudou** sem o Tiago saber. Mudar a chave apaga o progresso de todos os jogadores. Só se muda de propósito (ex.: mudanças de regras incompatíveis, quando o Tiago diz "começa de novo").

## Arquitetura do jogo (`index.html`)

Tudo dentro de uma IIFE num único `<script>`. Sem dependências externas além das letras do Google Fonts (Silkscreen para títulos, números, placard e botões; VT323 para textos compridos). Gráficos em `<canvas>` desenhados à mão (pixel art com `fillRect`), som gerado com Web Audio. Estado guardado em `localStorage`.

Secções (procurar pelos comentários `/* ===== X ===== */`):

| Secção | Conteúdo principal |
|---|---|
| `DATA` | `CATS` (8 categorias: Mosca, Galo, Pena, Leve, Meio-médio, Médio, Meio-pesado, Pesado), `CAT_LIM` (limites em kg), `SLOTS` (4 atletas), `CATMOD` (carácter de cada categoria na luta), `GIFTS` (talentos escondidos), `ATTRS`/`ATTR_G` (8 atributos), `MENT`/`PERS1`/`PERS2` (mentais e nomes de personalidade), `TIERS` (Amador → Regional → Nacional → Mundial), `ECON`, `ROUTINE`/`EQ_G`/`EQ_SK` (o que a rotina e cada aparelho treinam), `EQ` (equipamento), `UPG` (instalações), treinadores (`CT` escalões, `CMAX`, `STY_ATTR`, `C_NAMES`, `BOND` ligação, `FOCUS` foco do treino), `SKILLS` (7 golpes), `DEFS` (6 defesas), `LEARN`, confiança (`belOf`/`belUpd`), `DIST_FIT`/`curDist`/`distFit` (golpes e defesas por distância), `COMBOS`, técnicas (`TECH` catálogo de 25 técnicas de ataque, defesa e guardas; `techK`, `techLack`, `techSlots`/`careerLv`, `techSpeed`/`techHaz`/`techEta`/`techHint`, `techAff`/`tq` afinidade, gancho `techBoost` para as cartas), `STRAT` (estratégias de luta), `TUNE` |
| body / style levels | Altura e alcance (`H_BASE`, `rollBody`, `bodyType`: Compacto/Médio/Longo), níveis de estilo 0–5 (`sty`, `styleCap`, `styleFit`, `addStyleXP`), efeitos físicos na luta (`phys`, `skillF`, `sf`, `topF`) |
| `STATE` | `newGame`, `makeAthlete`, `save`/`load`, `KEY`; treinadores: `makeCoach`, `startCoaches`, `coachOf`/`athOf`, `assignCoach`, `styleFollow`, `autoCoach`, `bondLv`/`bondK`, `coachPay`, `gymFame` |
| `OFFERS` | Propostas de luta, `makeOpp` (adversários de academias rivais), scouting |
| `SOUND` | `SFX` — sons 8-bit gerados (sem ficheiros) |
| `RENDER` | UI em menus num ecrã fixo: separadores Ginásio (Ginásio / Treinadores: `panelCoaches`, `coachInfo`, `pickCoachFor`, `pickAthFor`, `confirmCoach`, `hireCard`) / Atletas (Ficha → Atributos/Golpes/Técnicas (`panelTech`, `techInfo`, `techForget`)/Estilos/Lutas, Treino: `panelTreino`, `improving`) / Lutas / Loja |
| `MODALS`, `INPUT` | `modal`, `info`, handler global de cliques (`data-*`) |
| `WEEK` | Tempo a correr sozinho (experiência): `TIME` (semana de 45 s, ×1/×2/×4, treino todos os dias; `window.__TIME` sobrepõe nos testes), `clockTick` → `dayStep` (treino diário: `trainDay`, `attrW`, `attrRate`, `skW`, `coachK`, `ageK`, `sessQ`, `learnK`, `addXP`) → `endWeek`/`weekEnd` (`weekTrain`: ligação, estilos antigos a descer, idade; `techWeek`: chance semanal de aprender a técnica em curso → cartão TÉCNICA APRENDIDA); aviso curto da semana (`toast`), caixa ESTA SEMANA (`S.evo`) e relatório completo no Ginásio. Nos testes, `window.__week()` avança uma semana inteira de imediato (`#goBtn` é ▶/❚❚, já não avança semanas) |
| `GYM WORLD` | Ginásio animado em canvas 240×136: membros e atletas a treinar, treinadores a circular, sons ambiente |
| `FIGHT` | Simulação da luta (`runFight`, `exchange`, `punch`, `knockdown`, `corner`, `preTalk`), distância e ringue (`ringStep`, `pesEff`, `placeRing`, `footwork`, antecipação `antP`, cross-counter `crossCounter`; dados em `x.dx`), técnicas na luta (`techPick`, `figP` regra do fígado, `tUse`/`tPop`, `guardHit`/`guardW`/`defE`, `tryLstep`), o atleta escolhe estilo e guarda (`styleAI`, `styleVal`, `guardVal`), marcas da luta (`mkWords`, `armK`, `hurtHand`, `elbowHit`, `eyeChk`), atributos do momento (`mom`, `E`, `stWords`), entrada no ringue, cerimónia final. Ecrã da luta (fase 2): placard (`hud`), frases com canais (`say`, `LPRI`, `F.log`), mesa dos comentadores (`deskTick`, `showLine`, `bustZe`/`bustAb`), registo (`openLog`), Abílio (`abRound`, `abTick`, `ABL`/`ABC`), pop-ups (`pop`, `drawPop`, `POPS`), balões dos treinadores (`drawBalloons`), ringue a ocupar o espaço livre (`fitStage`, `drawFrame`) |
| arena drawing | Arena em vista frontal elevada (`buildArena`, `proj`/`unproj`), 4 locais por escalão, público, `ringLoop`; lutadores desenhados por esqueleto de poses (`drawFighter`, `POSE`, `STRK` por golpe, `ANIM` com o saltitar por estilo) |
| corner men | Treinadores nos cantos (`makeCrew`, `crewUpdate`, `drawCrew`) |
| `BOOT` | Menu inicial / pausa (`menu`, `pauseMenu`), `start()` |

### Sistemas principais (resumo)

- **Atletas:** 8 atributos em 2 grupos — FÍSICO: Força, Velocidade, Resistência, Queixo (de nascença, escala própria ~50, desce com a idade e com KOs); TÉCNICO: Técnica, Defesa, Pés, Ring IQ (sobe sobretudo com lutas e sparring) — com potencial, idade (faz anos), 7 mentais escondidos (`a.ment`: Coração, Calma, Disciplina, Confiança, Concentração, Instinto finalizador, Ouvir o canto) de onde sai o nome da personalidade (`persona`), estilo e níveis de estilo, golpes e defesas com níveis 1–5, fadiga (só depois das lutas), confiança e forma, altura e alcance, treinador (`a.coach`, semanas juntos `a.cw`) e foco do treino (`a.focus`). Talento escondido com probabilidade 1/15. O primeiro atleta é **sempre peso Pena**; os outros entram numa categoria livre. Peso em kg (`a.kg`), peso natural (`a.nw`), categoria ideal (`a.icat`), derrotas seguidas (`a.lst`).
- **Treino sem plano (3A-1):** não há plano semanal nem cansaço de treino nem lesões por excesso de treino. O atleta treina sozinho **todos os dias**: cada atributo sobe conforme a **rotina** de todos (corrida e shadow: Resistência), o **equipamento** do ginásio (cada aparelho treina certas coisas; sem ele sobem mais devagar), o **treinador** (escalão, ligação e estilo), o **foco do treino** (Atributos / Técnicas / Perder peso), a **idade** (jovem cresce mais; a partir dos 31 perde físico devagar), a **personalidade** (Disciplina, Concentração, confiança do dia) e a falta até ao potencial. Golpes e defesas também sobem sozinhos (mais os do estilo do treinador, os do equipamento e os usados nas lutas); os novos aprendem-se sozinhos quando o atleta cumpre o `LEARN`. Acabou a perda de condição sem treino. Constantes no `TUNE` (bloco 3A-1).
- **Peso e categorias (3A-2):** 8 categorias com os limites reais (Pesado sem limite); no máximo 4 atletas (`SLOTS`), **nunca dois na mesma categoria**; os talentos chegam numa categoria livre (com o ginásio cheio, só para trocar com o da mesma categoria). Cada atleta tem uma categoria ideal (a de entrada) e pode lutar na de cima ou na de baixo (`natCats`). O peso muda todos os dias (`weightDay`): sobe devagar com ATRIBUTOS/TÉCNICAS e a recuperar, desce com PERDER PESO; não mexe na semana da pesagem. **Pesagem:** na semana anterior à luta, cartão de um toque (`prepCard`, `PREP`: Correr / Descansar / Perder peso / Comer muito, com custo, kg e ânimo = `conf`); no dia, `weighIn` (`wiVerdict`): peso perfeito → popularidade (`fanBonus`, fãs na 3B), acima do limite → menos fôlego inicial, Força e Resistência, abaixo do peso → o adversário com mais Força; guardado em `a.fight.wi` e na análise (`an.wi`). **Mudar de categoria** (`catMoves`, Atletas → Treino → MUDAR): só para uma vizinha dentro das suas, livre e sem luta marcada, depois de completar a categoria (`catDone`: por agora o título Mundial nela; o 3A-4 redefine) ou de `TUNE.catLoss` (4) derrotas seguidas; recomeça no n.º 10. Constantes no `TUNE` (bloco 3A-2).
- **Treinadores (3A-1):** cada atleta tem **um treinador principal** (`S.coaches`: nome, estilo Outboxer/In-fighter/Puncher, escalão Bairro → Clube → Regional → Nacional → Lenda; até 5). O ginásio começa com 3 de Bairro, um de cada estilo; só recebem salário quando treinam um atleta. Mais escalão = ensina mais depressa, custa mais e precisa de mais fama (por agora a popularidade). A **ligação** cresce com as semanas juntos e perde-se ao trocar. **Trocar de treinador = mudar de estilo principal:** o atleta continua a lutar no estilo antigo até ter nível no novo; o antigo desce muito devagar (nunca abaixo de 1). Gerem-se no Ginásio → Treinadores; em Atletas → Treino vê-se o treinador, o foco e o que está a melhorar (por palavras). Substituem o treinador assistente e os especialistas de estilo da loja.
- **Velocidade de aprender** (golpes, defesas, atributos e estilos): lado do treinador (escalão e ligação `coachK`; o estilo dele ensina mais depressa os seus golpes e defesas, `STY_TEACH`) e lado do atleta (Disciplina, Concentração, confiança do dia, Técnica num golpe novo) — `sessQ`, `learnK`, constantes no `TUNE`.
- **Estilos:** triângulo clássico — **In-fighter > Outboxer > Puncher > In-fighter**. A força da vantagem cresce com o nível do estilo (quase nada no amador, completa no topo). O corpo define o nível máximo de cada estilo. O estilo principal é o do treinador do atleta. **Na luta o atleta escolhe sozinho** (3A-3) o estilo (entre os que tem nível ≥ 1) e a guarda (entre as que sabe), também a meio do round, conforme o estilo do adversário, a distância, o estado e o Ring IQ (muito IQ escolhe bem; pouco teima). O jogador já não escolhe o estilo antes da luta nem no intervalo; fica com as estratégias e as ordens. Vale para os adversários.
- **Estratégias de luta:** Pressão / Equilibrado / Cautela.
- **Técnicas e guardas (3A-3):** catálogo `TECH` (12 de ataque, 9 de defesa, 4 guardas) com golpe/defesa de origem, estilo natural (ou contra-ataque), requisitos (níveis, atributos, técnica antes) e "regra do fígado" (`fig`: sem a técnica acontece raramente e pior — cross-counter, check hook, jab de recuo, fígado, cotovelo, rolling, L-step, framing). O jogador escolhe **uma técnica de cada vez** (Ficha → TÉCNICAS); no fim de cada semana de treino há uma chance de a aprender (sem barra; ~4 semanas), mais depressa com Técnica, Disciplina/Concentração, treinador do estilo natural, foco TÉCNICAS; avançadas mais devagar. **Lugares** partilhados (por escalão 2→5, +1 campeão do mundo, até 6, +1 com Ring IQ ≥ 70); cheio → escolhe-se a que esquece quando aprender. **Afinidade:** no seu estilo a técnica rende até +20% (depende do nível nesse estilo). Na luta: pop-ups especiais e frases próprias; os adversários (`oppTech`) também têm técnicas. **Marcas da luta** (primeiro nas palavras de estado): MÃO MAGOADA, BRAÇO DORIDO, OLHO FECHADO, SEM AR. Análise: técnicas usadas/resultou em GOLPES (`an.tq`, `an.mk`). Constantes no `TUNE` (bloco 3A-3).
- **Golpes e defesas:** 7 golpes do Guia (1 jab, 2 direto, 3/4 gancho da frente/de trás, 5/6 uppercut da frente/de trás, overhand) com nível 1–5; o alvo cabeça/corpo escolhe-se na luta (corpo tira fôlego e baixa a guarda; o gancho da frente ao corpo pode dar o efeito do fígado). Aprendem-se e melhoram sozinhos no treino diário. 6 defesas (bloqueio, aparar, cabeça, ombro, pés, clinch) escolhidas golpe a golpe; quando resultam podem abrir um counter (tabela do Guia). Cada golpe e defesa tem um nível real e um nível em que o atleta acredita (`a.bel`). Combinações pelos números (1-2, 1-2-3…) desbloqueiam com os golpes.
- **Contra-ataque:** depois (counter a seguir a uma defesa que resultou, golpe conforme a defesa; pivô/passo lateral → ataque de ângulo; clinch → sair a bater), antes (antecipação: apanhá-lo a entrar com o jab, jab de recuo ou check hook) e ao mesmo tempo (cross-counter: direto por cima; sem timing os dois acertam). Desde o 3A-3, jab de recuo, check hook e cross-counter são técnicas com a regra do fígado. Ring IQ é o mais importante.
- **Distância e ringue:** distância longe / meio / perto (`F.dist`; cada estilo prefere uma: Outboxer longe, Puncher meio, In-fighter perto) disputada com os Pés que contam agora (`pesEff`: descem com cansaço, dor e "pernas bambas" depois de uma queda) e o Ring IQ; mexe nos golpes, defesas, dano e fôlego. Centro / cordas / canto (`F.zone`, `F.zp`): quem ganha a disputa para se aproximar encosta o outro; encostado defende pior; sai-se com pés, clinch ou a bater. Barra LONGE · MEIO · PERTO junto ao relógio; animações de encostado às cordas/canto e pernas bambas.
- **Luta:** rounds de 3 minutos, fôlego, vida, quedas, quedas relâmpago, KO/TKO/médico/toalha/decisão, perguntas no canto (tática certa, meia certa ou errada), ordens do canto durante o round, cantos com corner men, entrada no ringue e cerimónia com cinturão e confetis.
- **Ecrã da luta (fase 2, luta legível):** o ringue ocupa o espaço livre (tecto por cima, público por baixo). Placard com nome, barras de vida e fôlego sem números (piscam a vermelho quando caem de repente), estratégia por extenso e **palavras de estado** ("SEM PERNAS", "MÃOS LENTAS", "ABANADO", "SEM GUARDA"; também numa caixa no canto). **Mesa dos comentadores** por baixo do ringue: o **Zé do Micro** (esquerda, relato curto) e o **Abílio "Bigorna" Santos** (direita, ex-pugilista: 1–2 vezes por round explica o porquê com o estado real da luta, ou conta uma história — percurso, desforra, público, título). **Uma frase de cada vez** (normal ~2 s, importante ~4 s a dourado); tocar na mesa abre o **registo** e a luta pára. Canais em `say()`: importante (quedas, counters, técnicas, fígado, fim do round, ordens ouvidas/perdidas, encostar ao canto) passa sempre; rotina (cada jab, bloqueio, esquiva) só fica no registo `F.log` e vê-se no ringue — com os pop-ups desligados o Zé diz algumas. **Pop-ups** no ringue, por ordem e do lado de fora de cada pugilista: normais (defesas, combinações "1-2-3", LIMPO!) e especiais com moldura dourada (COUNTER!, CROSS!, FÍGADO!, QUEDA!, CHECK HOOK!); opção nas Definições: todos / só especiais / desligados (`localStorage` `cm-popups`). A ordem gritada aparece num **balão por cima do nosso treinador** (reaparece enquanto o atleta não ouve) e a caixa A OUVIR / NÃO TE OUVE! / OUVIU!; o treinador adversário grita coisas de ambiente (sem efeito).
- **Atributos do momento (2.9):** `mom(x)` dá o multiplicador de cada atributo conforme o estado e junta os efeitos de estado que já existiam (acerto/dano com pouco fôlego, defesa de cabeça cansada, counters, ouvir o canto). Fôlego baixo tira Pés (muito), Velocidade, Força, Defesa e Técnica; vida baixa tira Queixo (e cada queda), Ring IQ (a Calma ajuda), Defesa, Pés e um pouco do resto; pernas bambas → Pés; Concentração baixa → Técnica nos últimos rounds; a Resistência não desce. `E(x,k)` é o atributo que conta agora. Constantes `m*`/`w*` no `TUNE`, por afinar.
- **Análise pós-luta:** 6 separadores em duas linhas (RESUMO com motivos e dicas de treino, por palavras e sem números de atributos; GOLPES por golpe e defesa, counters, fígado e confiança vs realidade; RINGUE com distância, cordas/canto, controlo e contra-ataque; ROUNDS; CANTO; COMPARAR com os 8 atributos no início da luta, tu a vermelho e ele a azul, com números — `TUNE.cmpNums=false` troca por só barras; guardado em `an.at`). Histórico de lutas na Ficha (análise completa nas 3 últimas).
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
- **Fazer sempre perguntas antes de cada parte, mesmo sobre coisas já faladas.**
- **Avisar o Tiago** quando uma decisão que ele está a tomar ficaria melhor mais tarde, entra em conflito com outra coisa (já decidida ou planeada) ou não vai funcionar.
- **Decisões ainda abertas:** muitas decisões da fase 3 são direção, não definitivas. Quando uma decisão nova mexer numa anterior, **relembrar o Tiago** e ver com ele se é preciso alterar.
- **Imagens de teste só quando o trabalho é muito visual.** Nas fases de funcionamento, programa-se logo; os agentes tomam a opção mais simples coerente com `docs/design.md` quando algo não está decidido e listam essas decisões para o Tiago confirmar.
- **Legível primeiro, bonito depois:** resolver já o que impede de perceber o jogo; deixar o que é só beleza para a fase visual (fase 8 do plano).
- Fazer perguntas quando há decisões de design em aberto, em vez de assumir. Ele gosta de conversar sobre o design, tema a tema.
- **Ecrã fixo, sem scroll:** tudo tem de caber num ecrã de telemóvel vertical, com navegação por menus e separadores. Verificar com capturas a 390×720/760.
- Pixel art coerente (letras Silkscreen e VT323, paleta quente; o vermelho é o teu canto e o azul o adversário). Atletas originais, **não** personagens do Hajime no Ippo. Nomes de técnicas podem coincidir com termos do boxe ou do anime quando o Tiago decide (ex.: "jolty counter"); avisar, mas a decisão é dele.
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

O Tiago quer o jogo baseado num guia de boxe que escreveu. **As decisões, o plano por fases e o estado de cada tema estão em `docs/design.md` — é a referência; mantê-lo atualizado.** Os temas estão a ser decididos um a um. **Fase A implementada** (A1 = tema 8, A2 = temas 1 e 3/4.1, A3 = tema 5 e 4.2/4.3, A4 = análise, comentador, animações e velocidade de aprender 9.1); o resto (fases B e C) ainda não está implementado:

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

Último ponto aberto: ver o **Plano geral** no topo de `docs/design.md` (neste momento: fase 3 — gestão divertida).
