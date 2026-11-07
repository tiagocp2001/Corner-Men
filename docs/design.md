# Corner Men — Documento de design

Aqui ficam as decisões de design do jogo, tema a tema. É a referência para qualquer sessão futura: **o que está aqui decidido é para seguir; o que está "em aberto" ainda não se implementa.**

Estados usados: **Em aberto** (a discutir) · **Decidido** (pronto a implementar) · **Implementado** (já está no jogo).

## Como trabalhamos

1. Os temas vêm do "Guia Completo de Boxe" do Tiago (`docs/Guia_Completo_de_Boxe.pdf`; texto pesquisável em `docs/guia-boxe.txt`), agrupados em fases por ordem de dependência.
2. Para cada tema, uma ficha curta: **hoje no jogo · o que o Guia diz · proposta · o que o jogador vê e decide · o que muda no ecrã · fica de fora**. Depois, 2–3 perguntas ao Tiago; as respostas ficam escritas aqui.
3. Decide-se a fase inteira antes de implementar. Implementa-se por fase, publica-se no `main` para jogar e sentir.
4. O equilíbrio (simulações, números) fica para depois de tudo estar implementado.
5. O tema 12 (tudo cabe num ecrã fixo de telemóvel vertical, sem scroll) é uma **condição de todos os temas**, não um tema à parte.

---

## Fase 0 — Visão · *Decidido*

Regras gerais que orientam todos os temas.

| # | Proposta | Estado |
|---|---|---|
| 0.1 | **O jogador é o treinador, não o lutador.** Decide três coisas: o **treino**, o **plano de luta** e as **ordens do canto** (durante o round e no intervalo). Os golpes, um a um, são automáticos. | Decidido |
| 0.2 | **Nível de realismo.** Cada elemento do Guia entra de uma de três formas: **mecânica** (muda o resultado), **texto** (só o comentador e a análise o mencionam) ou **fora**. Decide-se tema a tema. | Decidido |
| 0.3 | **Regra de ouro:** tudo o que é mecânica tem de se **ver na luta** (animação, comentador) **e na análise pós-luta**. Se o jogador não o vê, não entra. | Decidido |
| 0.4 | **Ecrã fixo:** cada tema diz onde aparece no ecrã e o que sai ou se junta para caber. | Decidido |

## Fase A — Núcleo da luta · *Em aberto*

Ordem: 8 → 5 → 1 → 3 → 4.

### Tema 8 — Atributos físicos, técnicos e mentais · *Em aberto (proposta feita)*
- **Hoje:** 5 atributos em barra (Força, Velocidade, Resistência, Defesa, Técnica) + potencial; corpo (altura, alcance) fixo; traços de personalidade (Trabalhador, Teimoso, Cabeça fria, Preguiçoso, Coração de leão); talentos escondidos (Mão pesada, Mãos rápidas, Motor inesgotável, Queixo de ferro); confiança e forma variáveis.
- **Guia:** 11 físicos (potência, velocidade de mãos, explosividade, resistência, recuperação, agilidade, equilíbrio, coordenação, queixo, durabilidade, alcance/altura), 10 técnicos/táticos (timing, precisão, gestão da distância, defesa, footwork, Ring IQ, volume, versatilidade, antecipação/reflexos, controlo do ringue) e 7 mentais (coração, calma, disciplina, confiança, concentração, instinto finalizador, adaptabilidade/ouvir o canto).
- **Proposta:** 8 barras em 2 colunas de 4, cada uma a juntar vários atributos do Guia:

  | Físicos | Junta (Guia) | Técnicos | Junta (Guia) |
  |---|---|---|---|
  | Força | potência, explosividade | Técnica | precisão, timing, coordenação |
  | Velocidade | velocidade de mãos, reflexos | Defesa | defesa |
  | Resistência | resistência, recuperação | **Pés** (novo) | footwork, agilidade, equilíbrio, gestão da distância, controlo do ringue |
  | **Queixo** (novo) | queixo, durabilidade | **Ring IQ** (novo) | Ring IQ, antecipação, versatilidade, ouvir o canto |

  - Alcance e altura continuam no corpo (fixos, não se treinam).
  - Os **mentais** não viram barras: são **traços de personalidade** (1–2 por atleta), alargando a lista atual — ex.: Coração de leão (coração), Cabeça fria (calma), Trabalhador (disciplina), Teimoso (não ouve bem o canto), + novos como Finalizador (instinto finalizador) e Concentrado (não se desliga nos últimos rounds). Confiança continua a ser um valor que sobe e desce.
  - O volume de golpes (work rate) fica ligado à estratégia (Pressão/Equilibrado/Cautela), não a uma barra.
  - Ligações: Ring IQ acelera o "ouvir o canto" já implementado; Pés decide a distância (tema 5); Queixo decide quedas e KOs.
- **Ecrã:** a Ficha mostra 2 colunas de 4 barras (FÍSICO / TÉCNICO). A Ficha já está apertada a 390×720; tem de ser reorganizada.
- **Perguntas ao Tiago:** ver conversa de 7 nov 2026 (8 barras? mentais como traços? Queixo treinável? Ring IQ por experiência?).
- **Decisões:** —

### Tema 5 — Pés, distância e controlo do ringue
- **Hoje:** zonas do ringue e alcance existem; não há distância longa/média/curta explícita.
- **Guia:** distância longa/média/curta, trabalho de pés, controlo do ringue.
- **Decisões:** —

### Tema 1 — Golpes
- **Hoje:** jab, direto, gancho, uppercut, direto ao corpo, gancho ao fígado, Contra-golpe.
- **Guia:** numeração 1–6 (mão da frente/de trás), overhand, cabeça/corpo como alvo, variações (jab duplo, power jab, flicker jab, check hook, shovel hook, cross-counter…), que treino ensina cada golpe, números usados pelo comentador.
- **Nota:** havia perguntas em aberto deste tema numa conversa anterior que não ficaram registadas; refazem-se aqui.
- **Decisões:** —

### Tema 3 — Defesa
- **Hoje:** defesas com níveis (bloqueio, esquiva, baixar, recuar…).
- **Guia:** 6 famílias — bloqueio, parry, movimento de cabeça, ombro, pés, clinch — cada uma abre um contra-golpe específico.
- **Decisões:** —

### Tema 4 — Contra-ataque
- **Hoje:** Contra-golpe dispara depois de uma defesa.
- **Guia:** contra-ataque antes, ao mesmo tempo e depois.
- **Decisões:** —

## Fase B — Camada tática · *Em aberto*

### Tema 2 — Combinações e fintas
- **Guia:** 1-2, 1-1-2, 1-2-3, 1-2-3-2, 2-3-2, 1-6-3-2, gancho duplo, mudança de nível; fintas.
- **Decisões:** —

### Tema 7 — Guarda ortodoxa / canhota
- **Guia:** ortodoxo, canhoto (southpaw), trocar de guarda.
- **Decisões:** —

### Tema 6 — Estilos
- **Hoje:** triângulo In-fighter > Outboxer > Puncher > In-fighter, com níveis de estilo.
- **Guia:** possíveis híbridos Counter-puncher e Boxer-puncher.
- **Decisões:** —

## Fase C — Preparação · *Em aberto*

### Tema 9 — Treinos novos
- **Guia:** saco duplo, maize bag, escada, sparring leve/condicionado/duro, clinch work, HIIT, core/pescoço.
- **Decisões:** —

### Tema 10 — Treino mental e tático
- **Guia:** vídeos do adversário, plano de combate, peso/pesagem.
- **Liga com:** pesagem (adiada), "chave do plano" da pesquisa a outros jogos.
- **Decisões:** —

### Tema 11 — Faltas e golpes ilegais
- **Decisões:** —

---

## Já implementado (fora do Guia)

- **Ordens do canto durante o round:** Pressão / Equilibrado / Cautela. O treinador grita até o atleta ouvir; o ritmo a que ouve depende do estado atual (cansado/dorido ouve mais devagar; muito cansado e muito dorido não ouve). Se o gongo tocar antes, ouve no intervalo.
- **Toalha a meio do round**, com confirmação (a luta pára enquanto se confirma).
- **Análise pós-luta:** Resumo, Golpes, Rounds, Canto; motivos com dica de treino; diferenças de atributos ditas por palavras, sem números.
- **Histórico de lutas** na Ficha (separador LUTAS, páginas de 4): registo curto de todas as lutas; análise completa só das últimas 3.
- **Estratégia no canto** entre rounds: a ordem que ficou por ouvir aparece já escolhida; o treinador pode mudá-la.

## Adiado (não começar sem o Tiago pedir)

- Dinheiro no fim de jogo (ainda sem direção).
- Taças sazonais e pesagem (a definir como funcionam).
- Acelerar o título Amador, animações dos golpes ao corpo, golpe especial.
- Equilíbrio geral (incluindo: Cautela não protege o atleta dorido, porque a Pressão domina no nível médio).

## Ideias da pesquisa (Boxing Gym Story e MMA Manager 2) por encaixar

Noites de luta organizadas pelo ginásio · hall da fama / reformados como treinadores · parceiro de sparring contratado · treinadores com nível máximo · prémio da primeira vitória contra cada adversário · equipamento de patrocinador · pontuação anual de legado · rivalidades e desforras · galeria de momentos · prolongar a carreira · Novo Jogo+ com o que passa bem explicado. Regras: lutas curtas com 1–2 decisões que contam; ganhar tem de pagar claramente mais do que perder.
