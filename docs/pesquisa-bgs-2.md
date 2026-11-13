# Pesquisa 2: Boxing Gym Story a fundo → sugestões para o Corner Men (13 nov 2026)

Segunda análise do *Boxing Gym Story* (BGS, Kairosoft, 2021 no telemóvel, 2023 no Steam), mais funda do que a `docs/pesquisa-bgs.md`. Primeiro explica-se como o BGS funciona, tema a tema, com os números da wiki. Depois vêm as sugestões para o Corner Men, cada uma com número, para o Tiago responder "sim/não" por número (tabela no fim).

**Regras que as sugestões respeitam:** ideias originais (nunca copiar a arte, o aspeto, os nomes ou a interface do BGS); "no ringue tudo pode acontecer" (vantagens individuais pequenas); ecrã fixo e sem scroll; o que já está decidido em `docs/design.md` (quando uma sugestão mexe numa decisão, aparece ⚠ **CONFLITO**). Os números do Corner Men que aparecem aqui são **exemplos**: os valores a sério só na fase 7, com simulações.

**Versão 2 deste relatório:** foram lidas **todas as 16 páginas** do BGS na wiki da Kairosoft (kairosoft.wiki.gg). Vários pontos que estavam "incertos" ficaram confirmados com números, alguns estavam errados e foram corrigidos (marcados **[corrigido]**), apareceram sistemas novos (**[novo]**). Sugestões alteradas por causa dos dados novos estão marcadas **(revista)**; as novas vão de **S46** em diante.

---

## 0. De onde vem a informação

- **Wiki da Kairosoft (kairosoft.wiki.gg), lida por inteiro:** *Boxers, Boxing Council Chief, Bugs and cheats, Endgame, Facilities, Fights, Items, Marketing, Members, Photos, Skills, Tips, Tournaments, Trainers, Training* (e a página principal, vazia). É uma wiki de fãs: os números podem variar um pouco com a versão do jogo. A wiki do Fandom não foi lida (tem uma barreira anti-robôs).
- **Opiniões dos jogadores:** Steam (≈ 66–69% positivas em 66–81 críticas, "Misto"), críticas do Google Play e da App Store (por agregadores: AppGrooves, Game Solver), fórum do TouchArcade (fev. 2021), listas de conquistas (PSNProfiles, TrueAchievements).
- **Legenda:** ✅ = confirmado nas fontes · ❓ = a wiki não diz (incerto ou deduzido).
- **O que a wiki não tem:** não há página sobre o "nível" do ginásio, fama/ranking do ginásio, eventos, rivais ou "combos" de colocação. O que se diz sobre isso fica marcado ❓.

---

## 1. O BGS numa página

- ✅ És o gerente de um ginásio de boxe falido; "põe a cidade entusiasmada com o boxe e mais gente se inscreve". Ganhar lutas abre melhorias (termas, restaurante…).
- ✅ O jogo dura **cerca de 10 anos**: a pontuação é calculada todos os anos no **mês 4** e o jogo "acaba" no **Ano 11, Mês 4**; depois há Novo Jogo+.
- ✅ Duas moedas: **dinheiro (G)** e **Smile Points** ("pontos sorriso"), que pagam **todos os treinos** e as **habilidades**.
- ✅ O motor do jogo é o **Chefe do Conselho de Boxe**: cada **1.ª vitória contra um adversário novo** (há uma "caixa de presente verde" ao escolher o adversário) dá uma recompensa à escolha.
- ✅ Atributos: **Vida, Fôlego, Skill, Defesa, Força (Punch), Pés** + **Charm** (encanto) + **Spirit** (ânimo) + peso. **[corrigido]** o "Spirit" existe mesmo: sobe com o treino interior, termas e restaurante, e recupera com certas comidas.
- ✅ Lutas automáticas: o jogador **motiva/dá instruções**, não controla.
- ✅ **No máximo 3 pugilistas** (um por andar do ginásio) — uma das críticas mais fortes.
- ✅ **[novo]** Há "**preocupações do pugilista**" que aparecem ao acaso (a wiki só as menciona de passagem).

---

## 2. Ritmo e progressão (o tema mais importante)

### Como o BGS faz

**Início ✅:** o ginásio principal (100 000 G), 1 andar = **1 pugilista + 3 aparelhos**, 1 treinador (o mascarado: Skill 65, Charm 100, 8% de treino, 62 000 G/mês). Há **3 pugilistas disponíveis desde o início** (dois Mosca/Pena e um Mosca/Pena/Leve) — com 1 andar só cabe 1 (❓ a wiki não diz como se escolhe); treinos Interior e Exterior; algumas habilidades.

**Como se abrem pugilistas ✅ (15 ao todo):**

| Como abre | Quantos | Exemplos (categorias) |
|---|---|---|
| Desde o início | 3 | Mosca–Pena, Mosca–Pena–Leve |
| Torneios sazonais (nível 1–4) | 8 | Primavera nv2 e nv4, Verão nv2 e nv4, Outono nv1 e nv3, Inverno nv1 e nv2 |
| Pontuação anual (300 / 1000 / 2000 / 10 000) | 4 | o de 10 000 é um Pesado com 8 lugares de habilidade |

**Expansão ✅:** um 2.º andar "no nível 3" e um 3.º "no nível 6"; cada andar novo traz um treinador (2.º andar: Smith, 12%, 68 000 G; 3.º: Martin, 9%, 64 000 G). ❓ A wiki não explica o que é este "nível" (provavelmente o nível do próprio edifício, que nos jogos da Kairosoft sobe com o uso). **Anexos:** 1.º = ringues de treino (**é preciso para aprender habilidades**), 2.º = mais 3 lugares de aparelho, 3.º = 1 lugar para aparelho XL por andar. **Laboratório** (5 M G, +1 andar por 40 M): 3 lugares por andar para **melhorar** aparelhos e instalações.

**A escada de lutas de cada categoria ✅ (exemplo: Pena):**

| Degrau | Preparação | Rounds | Bolsa (G) | Vida do adversário |
|---|---|---|---|---|
| 3 lutas amadoras | 3 sem. | 3 | 0 | 71–121 |
| "4 combates" | 4 sem. | 3 | 150 000–250 000 | 110–159 |
| "6 combates" | 5 sem. | 4 | 300 000 | 142–205 |
| "8 combates" | 5 sem. | 4 | 500 000 | 182–263 |
| "10 combates" | 5 sem. | 5 | 575 000–595 000 | 232–336 |
| Título nacional | 6 sem. | 5 | 660 000 | 283 |
| "12 combates mundial" | 6 sem. | 5 | 720 000–750 000 | 288–417 |
| Título mundial | 8 sem. | 10 | 785 000 | 350 |
| Pré-eliminatória, meia, final do campeonato | 8 sem. | 10 | 865 000–960 000 | 355–443 |
| "Showdown" | 10 sem. | 12 | 995 000 | 448 |

- ✅ Em cada degrau há **3 adversários com nome**, de força bem diferente (no Pena "4 combates": 110 / 159 / 137 de Vida). Os adversários são **sempre os mesmos** em todos os jogos.
- ✅ Do 1.º amador ao Showdown a força do adversário multiplica por ~5–6 (Mosca: Vida 65 → 366; Pesado: 228 → 999).
- ✅ Bolsas do Showdown: Mosca 840 000, Pena 995 000, Meio-médio 1,09 M, Médio 1,37 M, Leve 1,82 M; Pesado: título mundial 2,6 M.
- ✅ Pode-se **mudar de categoria livremente** (sem ordem), desde que o peso deixe; quem ganhou o título mundial ou o Showdown numa categoria **não repete as amadoras** na seguinte.
- ✅ Depois de ganhar o Showdown em todas as categorias possíveis: **exibições contra robôs de nível 1 a 99** (cada 5 níveis dão um "+1 ano de carreira").

**Críticas ao ritmo ✅:** "lento e repetitivo", "só 3 pugilistas e demora uma eternidade a lá chegar", "aumentos de preço ao acaso", "saltos enormes na força dos adversários", "o fim do jogo é uma obrigação, com melhorias caríssimas", "o modo rápido só abre depois de acabar o jogo", "entre lutas só se repetem os mesmos treinos".

**[corrigido] Os "aumentos de preço":** a wiki mostra que **os aparelhos não encarecem por unidade**. O que sobe é: (1) o custo em pontos de cada treino **com a idade do pugilista**; (2) o salário dos treinadores, **sozinho**, até 200 000 G/mês; (3) os aparelhos melhores custam mais (catálogo: 100 000 → 900 000 G); (4) **melhorar** um aparelho no laboratório custa **4× o preço** para o nível 2 e até **33×** para o máximo (ex.: corda de saltar 100 000 G; melhorias 0,4 M → 1,1 M → 1,8 M → 2,6 M → 3,3 M). Daí a sensação de "preços ao acaso" e o "fim do jogo caro".

**Lição:** o BGS começa pequeno (bom: há para onde crescer), mas **tranca o crescimento atrás de condições lentas e pouco claras** (níveis de edifício, torneios, pontuação anual) e a meio do jogo **as escolhas acabam**. Os jogadores gostam de ver o ginásio a crescer e de ter prémios frequentes; detestam esperar sem nada para decidir e custos que sobem sozinhos.

### Como o Corner Men está hoje

1 atleta (sempre Pena), 500 €, popularidade 5, 4 sócios, Saco e Zona de sparring, 3 treinadores de Bairro (só recebem quando treinam). Os talentos chegam **ao acaso** (a partir da semana 4, ~14% por semana + popularidade) até 4 lugares. Equipamento com preço fixo por unidade (ex.: 2.º saco 400 €, 3.º 600 €), 3 obras (pintar 1500 €, balneários 2500 €, ringue 6000 €). Uma semana = 45 s (×1/×2/×4). O dinheiro acumula a partir do 3.º ano (adiado).

### Avaliação das ideias do Tiago

| Ideia do Tiago | O que o BGS ensina | Avaliação |
|---|---|---|
| Começar com **1 só atleta** | O BGS faz igual (1 andar = 1 pugilista) e funciona no início | **Bom**, desde que o 2.º chegue cedo. |
| **Ginásio pequeno**, pouco equipamento, poucos sócios | Igual ao BGS (3 lugares de aparelho no início); ver o ginásio crescer é o que mais satisfaz | **Bom.** Liga-se à fase 4 (mapa): o espaço vazio a giz mostra o que falta. |
| **Condições** para ter mais atletas | No BGS a condição é um andar novo que abre "no nível 3/6", sem se perceber como → **crítica forte** | **Bom se as condições forem claras, visíveis e atingíveis em ~1 época.** Mau se forem escondidas ou se o 4.º lugar só abrir no fim. |
| **Cada equipamento encarece o seguinte** | O BGS **não faz isto**; encarece o treino com a idade, os salários sozinhos e as melhorias (até 33×) — e é criticado | **Bom se for previsível** (o botão mostra já o preço do próximo e porquê) e **moderado**. O espaço (lugares por sala, como os 3 por andar do BGS) é um travão mais claro do que o preço. |

⚠ **CONFLITO:** o início do jogo **já está decidido** com 3 treinadores de Bairro (um de cada estilo). Com 1 só atleta não custa dinheiro (só recebem quando treinam), por isso não é preciso mudar (ver S4).
⚠ **Atenção:** o treino diário depende do equipamento (`EQ_G`). Se o equipamento ficar mais caro, os atletas crescem mais devagar no início; isto vê-se com simulações na fase 7 (não afinar já).

### Proposta: o caminho completo (início → meio → fim)

A ideia: **5 etapas do ginásio**, cada uma com um nome, uma obra que a abre e **condições à vista** num quadro ("Para a próxima etapa: ✔ licença do Lobo · ✖ 12/15 sócios · ✖ obra: balneários"). Cada etapa abre **1 lugar de atleta** e mais espaço. Tempos a ×1 (1 ano ≈ 39 min reais; a ×4 ≈ 10 min).

| Etapa | Quando (alvo) | O ginásio | Atletas | O que abre |
|---|---|---|---|---|
| **1. A cave** | Ano 1, Primavera | sala pequena: 4 lugares de aparelho (2 ocupados), lotação ~8 sócios | 1 | lutas amadoras, cartas do foco TÉCNICAS, Loja básica |
| **2. Ginásio de bairro** | ~fim do Verão/Outono do ano 1 | obra "balneários" + 6 lugares, lotação ~16 | 2 | 1.º parceiro (café), sócios com nome, revista (notícias pequenas) |
| **3. Clube** | ~ano 2 | obra "2.ª sala" (ou "ringue a sério"), 9 lugares, lotação ~28 | 3 | treinadores de Clube/Regional, Torneio Rookie com 2 atletas, patrocinador com contrato, noite de luta no ginásio |
| **4. Casa de campeões nacionais** | ~ano 3–4 | obra "andar de cima", 12 lugares + 1 lugar "grande" | 4 | Europeu, parceiros avançados (clínica, nutricionista), visitas de ex-campeões, cartas raras de visita |
| **5. Ginásio de renome** | ~ano 5+ | fachada nova, letreiro, rua animada | 4 (máximo) | Mundial, treinadores Lenda, legado anual, lutas de lenda (fim de jogo) |

**Condições (exemplo, sempre 3 à vista):** uma de **carreira** (licença de um atleta; um atleta no top 10 Nacional; um campeão Nacional…), uma de **negócio** (sócios ou nível de fama) e **pagar a obra**. Nunca condições escondidas.

**O que fica igual:** 4 lugares no máximo, nunca 2 na mesma categoria, talentos numa categoria livre. Muda só **quando** os lugares abrem.

- **S1 — Etapas do ginásio com condições à vista.** Prós: objetivo claro de médio prazo, o ginásio cresce à vista, dá destino ao dinheiro. Contras: interface do quadro e equilíbrio. Fase **3B** + **4** + **7**.
- **S2 — Lugares de atleta abertos pelas etapas (2.º atleta ~6 meses de jogo).** Prós: começar com 1 sem ficar preso; evita a crítica n.º 2 do BGS. Contras: menos lutas no início → precisa de eventos e objetivos (S44/S45/S48). Fase **3B**. Muda o código atual (os 4 lugares abrem logo), não uma decisão do `design.md`.
- **S3 — Quando abre um lugar, escolher 1 de 2–3 talentos** (no BGS há 3 iniciais disponíveis). Prós: momento de decisão bom. Contras: menos surpresa (o talento ao acaso pode ficar como extra raro). Fase **3B**.
- **S4 — (Opcional) começar com 1 treinador.** ⚠ **CONFLITO** com o início decidido; recomendo **não**. Fase 3B.

---

## 3. Espaço do ginásio, obras e expansão

**BGS ✅:** andares de 1 pugilista + 3 aparelhos; anexos (ringues de treino para aprender habilidades; +3 lugares; lugares XL); laboratório para melhorar aparelhos; edifícios da cidade (loja, termas, restaurante) com andares. O limite é o **espaço**.
**Corner Men hoje:** sem espaço: cada aparelho tem um máximo por tipo; 3 obras que dão lotação e popularidade e sobem a renda.

- **S5 — Lugares de aparelho por sala (o espaço é o limite).** A cave tem 4 lugares; cada etapa acrescenta. Com a sala cheia: vender um (devolve metade) ou fazer a obra. Prós: escolha a sério ("pera ou pesos?"), liga-se ao mapa. Contras: rever o `EQ`. Fase **3B** + **4**.
- **S6 — Obras com efeitos de jogo:** balneários (+lotação), duche quente (recuperação um pouco mais rápida), escritório (revista, contratos), 2.ª sala (lugares), ringue a sério (sparring rende mais, noite de luta), letreiro (fama). Cada uma sobe a renda. Fase **3B**.
- **S7 — Um lugar "grande" para um aparelho especial na etapa 4** (a ideia do XL do BGS, com peças próprias: ex. ringue de competição, sala de vídeo). Efeito pequeno mas visível. Fase **3B/7**.
- **S49 [novo] — Obra "ringue de treino" que ajuda as técnicas.** No BGS sem o ringue de treino **não se aprendem habilidades**. No Corner Men isso seria demasiado (⚠ as técnicas já se aprendem sem condições do ginásio), mas a obra pode **acelerar um pouco** a chance semanal de aprender a técnica em curso. Prós: liga as obras às técnicas. Contras: mais um fator na chance. Fase **3B/7**.

---

## 4. Equipamento: custo, preços, níveis

**BGS ✅ — aparelhos do ginásio** (efeito em letras de F a S; nível 1 → nível 6):

| Aparelho | Treina | Preço (G) | Taxa nv1 → nv6 (G) | Popularidade |
|---|---|---|---|---|
| Corda de saltar | Fôlego, Pés | 100 000 | 1 000 → 10 000 | E |
| Saco pequeno / médio / grande | Vida, Força | 200 000 / 500 000 / 600 000 | 3 000–5 000 → 30 000–50 000 | E / D / C |
| Passadeira | Fôlego, Pés | 300 000 | 2 000 → 20 000 | E |
| Pera simples / dupla | Skill, Defesa | 400 000 / 700 000 | 3 000–5 000 → 30 000–50 000 | D / C |
| Bicicleta | Fôlego, Pés | 800 000 | 4 000 → 40 000 | C |
| Saco de água | Defesa, Força | 900 000 | 5 000 → 50 000 | C |
| 3 aparelhos XL | Defesa, Força | 1,0–1,2 M | 5 000 → 100 000 | C |

- ✅ "Sem aparelho" num lugar tem taxa de 2000 G e tira um pouco de Defesa e Pés.
- ✅ Os aparelhos sobem de nível 1 a 6; melhorá-los no **laboratório** custa caro (nível 2 = 4× o preço; máximo = 33×).
- ✅ Muitos aparelhos vêm de **torneios** (corda, sacos, passadeira, pera dupla, bicicleta, saco de água); os outros do Chefe do Conselho; os XL só depois do 3.º anexo.
- ❓ A wiki não explica a "taxa": provavelmente é o que os sócios pagam para usar o aparelho (rendimento), porque sobe com o nível e com a qualidade.
- ✅ **[novo] Equipamento pessoal do pugilista** (luvas, calções, sapatilhas), vendido na loja de desporto: **taxa de contrato + aluguer mensal** (ex.: luvas novas 50 000 + 5000/mês, +15 Skill, +9 Defesa, +5 Charm; as "power" 1,75 M + 215 000/mês, +70 Skill). 4 gamas.
- ✅ **[novo] Equipamento de patrocinador:** **tira** atributos (ex.: −5 a −30) mas **paga por cada vitória** (80 000 a 480 000 G). É uma troca: mais dinheiro, pugilista um pouco pior.
- ✅ No torneio sazonal contam só os atributos "de base" (sem o equipamento).
**Corner Men hoje:** 9 aparelhos com preço por unidade, máximo por tipo, manutenção 3 €/semana, cada um treina certas coisas, o 1.º de cada tipo vale mais, cada aparelho +2 de lotação.

- **S8 (revista) — Preços que sobem, mas à vista e moderados.** O BGS não encarece por unidade; o que irrita é o que sobe sozinho e as melhorias a 4–33×. Proposta: (a) **catálogo em gamas** (cada aparelho tem uma versão básica e uma melhor, mais cara); (b) pequena subida por cada aparelho que o ginásio já tem (ex. +10%), mostrada no botão ("Pera: 495 € · +10% por cada aparelho que já tens"). **Escolher com o S5**: espaço como travão principal, subida pequena. Fase **3B** + **7**.
- **S9 (revista) — Melhorar um aparelho (níveis 1–3)** em vez de comprar outro, com custos **comedidos** (ex.: nível 2 = 1× o preço, nível 3 = 2×; nunca as 4–33× do BGS). Treina um pouco mais e atrai mais sócios; ocupa só 1 lugar. Fase **3B/7**.
- **S10 — Aparelhos que se ganham** (prémio da 1.ª vitória, desafios da estação, parceiros, patrocínios). No BGS é uma das principais fontes. Fase **3B**.
- **S46 [novo] — Equipamento pessoal do atleta (luvas, calções, sapatilhas) com aluguer.** Para não dar vantagens grandes: efeito **muito pequeno** ou só **fãs/carisma** (as "luvas do ginásio" com o logótipo), e aspeto no ringue (fase 8). Prós: personaliza o atleta, gasto semanal com sentido. Contras: ⚠ vantagens individuais têm de ser pequenas; desenho. Fase **3B** (regra) + **8**.

---

## 5. Sócios (membros do ginásio)

**BGS ✅:** os "Members" são **12 personagens com nome**: 9 entram quando um tipo de marketing chega a um nível (página da internet nv2, redes sociais nv4, canal de vídeo nv6, clube de fãs nv7, limpeza do bairro nv3, oficina de boxe nv5, calendário de eventos nv7, auditório nv8), os outros vêm do Chefe ou do início. ❓ A wiki **não diz o que fazem** (nem se pagam). O que traz gente "comum" ao ginásio são o equipamento (grau de popularidade), o letreiro e os candeeiros da rua ("mais moradores").
**Corner Men hoje:** sócios são um **número** que paga 15 €/semana; o alvo sobe com a popularidade e o equipamento, até à lotação.

- **S11 — Sócios continuam um número; a lotação trava cada etapa.** Fase **3B**.
- **S12 (revista) — 4–8 "sócios com nome" que entram com marcos** (como os do BGS entram com o marketing; aqui com a fama, as obras e a divulgação — S30). Cada um com uma coisa pequena: traz uma carta comum de vez em quando, é parceiro de sparring, o miúdo pode tornar-se um talento anos depois. Prós: o ginásio ganha vida e cada nível de divulgação tem uma surpresa. Contras: textos e desenhos. Fase **3B** + **4/8**.
- **S13 — Treinadores livres dão aulas aos sócios** (já anotado no `design.md`). Fase **3B**.

---

## 6. Quantos atletas e como se recrutam

**BGS ✅:** máximo 3; elenco fixo de 15 pugilistas com nome (ver tabela da secção 2), cada um com atributos máximos iniciais, **intervalo de peso** (ex.: 47–56 kg), mês de aniversário, 2–5 categorias e **2 a 8 lugares de habilidade**. **Reformados não contratados como treinadores voltam 2 anos depois como "2.ª geração"** (com os atributos que tinham), e assim sucessivamente (3.ª, 4.ª…).
**Corner Men hoje:** 4 lugares, gerados ao acaso (talento escondido 1/15), chegada ao acaso.

- **S14 (revista) — Fontes de talentos variadas e com escolha:** etapa nova → escolher 1 de 2–3 (S3); prémio de um **desafio da estação** (S24, como os torneios do BGS abrem pugilistas); o olheiro (treinador de Clube+) encontra um no Torneio Rookie; um sócio com nome que cresceu (S12); um miúdo à porta (evento); a **pontuação de legado** (S41) traz um talento especial. Fase **3B**.
- **S15 — Herdeiro de uma lenda** (ideia própria, não a "2.ª geração" do BGS): anos depois, o filho/sobrinho/aluno de um campeão reformado aparece com um pouco do estilo dele; o Abílio conta a história. Fase **3B** ou **9**.

---

## 7. Atributos dos atletas

**BGS ✅:** Vida e Fôlego (pontos), **Skill** (acerto: com pouca Skill falha e leva counters; também ajuda a aprender habilidades), Defesa (menos dano), Força (dano), **Pés** (velocidade de movimento, frequência de ataque e esquiva; desce com o fôlego na luta). Mais **Charm** (sobe com o peso certo, comida, equipamento) e **Spirit** (ânimo). Valores de centenas (os pugilistas começam com 100–950). Itens "+50 de teto" para cada atributo. Treinadores: Skill até 500, Charm até 1500.
**Corner Men hoje:** 8 atributos + 7 mentais escondidos + potencial + confiança do dia. Mais rico.

- **S16 — Não mudar os atributos.** Sem regras novas.
- **S17 — Carisma escondido mostrado por palavras** (já decidido na 3B). No BGS o Charm sobe com o peso certo, a comida e as luvas; no Corner Men o peso perfeito já dá fãs. Fase **3B**.

---

## 8. Treino e crescimento

**BGS ✅:**

| Treino | Sobe | Peso | Pontos (início) | Estação "HOT" | Abre |
|---|---|---|---|---|---|
| Interior | Vida, **Skill ▲▲**, Defesa | ▲ | 6 | Inverno | início |
| Força | Skill, Defesa, **Força ▲▲** | ▼ | 10 | Primavera | Chefe |
| Velocidade | Vida, Fôlego, **Pés ▲▲** | ▼ | 12 | Verão | Chefe |
| Exterior | **Fôlego ▲▲**, Força, Pés | ▼ | 9 | Outono | início |

- ✅ Cada treino tem **até 5 sessões** (mais sessões com treinador de "Coaching" alto); o custo em pontos **sobe com a idade**; na estação "HOT" ganha mais e mexe mais no peso; o treino interior dá mais ânimo mas engorda.
- ✅ Às vezes dá **zero** (crítica: "opaco").
**Corner Men hoje:** treino diário sozinho (rotina + equipamento + treinador + foco + idade + personalidade); foco Atributos/Técnicas/Perder peso; cartas.

- **S18 — Treino visível no ginásio** (o atleta vai ao aparelho, "+FOR"). Fase **4/8**.
- **S19 — "Carta da estação" na Loja**, não no treino. No BGS cada estação favorece um treino; no Corner Men está decidido que **as estações não mexem no treino** (⚠ evitar). A Loja de cartas (que já muda por estação) tem uma carta da estação mais barata. Fase **3B**.

---

## 9. A segunda moeda (Smile Points)

**BGS ✅ — ganha-se:** 1.ª vitória contra cada adversário (30 → 100 à escolha), 5 por cada foto, 5 por participar num torneio, 3–15 por mês com os tipos de marketing "de pontos", folhetos e banca de inquéritos na rua, a habilidade "Análise detalhada". **Gasta-se:** todos os treinos e as habilidades. ✅ Um jogador ficou preso no tutorial sem pontos para treinar.
**Corner Men hoje:** só dinheiro; as cartas fazem de "recurso especial".

- **S20 — Não criar uma 2.ª moeda.** Traria de volta a gestão constante que o Tiago tirou; as cartas fazem esse papel.

---

## 10. Habilidades / técnicas e lugares

**BGS ✅ — 25 habilidades** com custo em pontos, abertas no início, pelo Chefe ou por torneios: golpes (flicker jab, corkscrew, smash, "jolt haymaker", "chop cross"), defesas (shoulder roll, cross-arm block, Dempsey roll, elbow block, down parry, cross counter, "dart & dance"), **Combo +1/+2/+4** (mais combinações por luta), **"Boosts"** (+atributo e treina melhor esse atributo), **estilo** (In-fighter / Out-fighter **são habilidades**), "Análise detalhada" (mais pontos). Aprender: **é preciso o ringue de treino**; o pugilista vai lá **quando quer** (o jogador não controla); **~1 mês**; chance pela Skill do pugilista + Skill do treinador + dificuldade; só se decide ao chegar a 100% (os jogadores gravam a 90% e recarregam). Não aprende lesionado nem com "preocupações". **Lugares**: 2–8 por pugilista + item "+1".
**Corner Men hoje:** 25 técnicas com chance semanal (~4 semanas), lugares pela carreira, afinidade de estilo, regra do fígado; estilo pelo treinador. Muito parecido em espírito e mais rico. ⚠ Nota: vários nomes coincidem (flicker jab, smash, corkscrew, cross-counter, shoulder roll, bloqueio de cotovelo) — são termos do boxe e do anime, permitidos pelo `CLAUDE.md`, mas convém não copiar as **descrições** nem a **lista** do BGS.

- **S21 — Prémio raro +1 lugar de técnica** (gala, título Mundial; o BGS dá-o como item de torneio). Fase **3B/7**.
- **S22 — Técnicas avançadas abertas por conquistas do ginásio.** ⚠ "qualquer atleta aprende qualquer técnica" (decidido). Fase **3B**.

---

## 11. Peso e pesagem

**BGS ✅:** 6 categorias (Mosca 50,8 · Pena 57,2 · Leve 61,2 · Meio-médio 66,7 · Médio 72,6 · Pesado sem limite). **Pesagem 2 semanas antes**, com um treino especial:

| Opção | Custo (G) | Ânimo | Peso |
|---|---|---|---|
| Correr | 0 | ++ | − |
| Descansar | 30 000 | + | + |
| Perder peso | 100 000 | ++ | −− |
| Comer muito | 200 000 | +++ | ++ |

Acima do limite: "foge para perder peso" e luta com atributos mais baixos. Abaixo do peso: o adversário recebe um bónus de força. Peso exato: bónus de Charm (dica: Descansar quando está 0,1–0,6 kg abaixo do limite). Pesado sem limite.

**Corner Men hoje:** 8 categorias (limites do boxe real, por isso iguais), cartão de pesagem com Correr (grátis) / Descansar (30 €) / Perder peso (120 €) / Comer muito (200 €), acima → fôlego e força mais baixos, abaixo → adversário com mais Força, perfeito → fãs.

- **S23 — Regras do peso: nada a mudar.** Se os atletas ficarem presos numa categoria, alternativa na fase 7 (o BGS deixa mudar livremente).
- **S47 [novo] — Dar à pesagem uma cara própria.** A pesagem do Corner Men ficou **muito parecida** com a do BGS: as mesmas 4 opções, quase os mesmos preços relativos (0 / 30 / 100 / 200) e os mesmos efeitos. Foi uma decisão do Tiago ("modelo do BGS adaptado"), mas convém afastar-se: ex. opções com o sabor do bairro e ligadas aos parceiros — "Treino leve no parque", "Sauna do clube" (com a clínica/ginásio de musculação), "Dieta da nutricionista" (só com esse parceiro), "Jantar de massa da avó"; preços e números diferentes; e um efeito próprio (ex.: a Calma decide se a sauna correu bem). Prós: originalidade, liga a pesagem aos parceiros. Contras: mexe numa coisa já implementada (só textos e números). Fase **3B**.

---

## 12. Torneios sazonais (fora das lutas)

**BGS ✅ — um por estação** (meses 3, 6, 9, 12), **não é uma luta**: é uma prova de 2 atributos; ganha quem tem a soma acima do mínimo. Cada torneio tem **níveis 1 → 4 + EX**, a abrir à medida que se ganha:

| Estação | Prova (atributos) | Mínimo nv1 / 2 / 3 / 4 / EX | Prémios (exemplos) |
|---|---|---|---|
| Primavera | Saltar à corda (Pés + Fôlego) | 200 / 400 / 800 / 1400 / 2000 | 100 000–400 000 G, corda, sacos, passadeira, "+1 lugar de habilidade", **2 pugilistas** |
| Verão | Meditação na cascata (Vida + Defesa) | 200 / 600 / 950 / 1350 / 2000 | letreiros, candeeiro, "+1 ano de carreira", habilidades, **2 pugilistas**, **2 adversários novos** |
| Outono | Saco de pancada (Força + Vida) | 200 / 408 / 800 / 950 / 2000 | pera, sacos, bicicleta, saco de água, **2 pugilistas** |
| Inverno | Bola de esquiva (Skill + Defesa) | 200 / 400 / 800 / — / 2000 | cartaz da luta, banco, mesa de bebidas, relógio, fato de sauna, **2 pugilistas** |

Todos os participantes ganham 5 pontos. Só contam os atributos de base.
**Corner Men hoje:** Torneio Rookie (lutas, Primavera), gala (Inverno); "taças sazonais" adiadas para a fase 6.

- **S24 (revista) — Desafios da estação** (provas rápidas sem luta), **com níveis a abrir**: uma por estação, com provas próprias do bairro (ex.: Primavera — "Subida ao Castelo" (Resistência + Pés); Verão — "Travessia a nado" (Resistência + Queixo); Outono — "Feira da força" (Força + Técnica); Inverno — "Noite dos reflexos" (Velocidade + Defesa)). Inscrever 1 atleta (1 toque), resultado no fim da semana. Cada vitória abre o nível seguinte do mesmo desafio no ano a seguir (mais difícil, prémio melhor). Prémios: carta, aparelho (S10), coisa para a rua (S33), às vezes um **talento** (S14). Prós: coisas para fazer entre lutas, usa atletas parados. Contras: ⚠ prémios **pequenos** (não pode valer mais do que lutar). Fase **6** (taças) ou **3B**.

---

## 13. Lutas: como funcionam

**BGS ✅:** automáticas; o jogador **motiva/dá instruções**. Os Pés decidem movimento, ataques e esquiva e caem com o fôlego; a Skill decide o acerto (falhar abre counters). Combinações limitadas por luta (habilidade Combo +n). Um fotógrafo tira fotos dos momentos.
**Críticas:** "demasiado acaso: um adversário com mais Força ganha mesmo com o resto muito melhor", "um pugilista dominante foi KO com dois golpes", "cada luta demora muito a começar", "o modo rápido está trancado".
**Elogios:** "é como um jogo de manager: não controlas, dás instruções", "dá para construir tipos de pugilista".
**Corner Men hoje:** muito mais rico.

- **S25 — Saltar a entrada com 1 toque e ×2 na luta desde o início.** Fase **3B** ou **8**.

---

## 14. Escada da carreira e fim da carreira de lutas

**BGS ✅:** a escada fixa da secção 2 (12 degraus por categoria, 3 adversários com nome em cada), sempre igual em todos os jogos; bolsas sobem ~6× do primeiro combate pago ao Showdown; fim de jogo com robôs de exibição.
**Corner Men hoje:** amador → licença → Nacional → Europeu → Mundial, com rankings vivos, eliminatórias, defesas, Torneio Rookie, arenas e público; o mundo muda de jogo para jogo. Já é mais vivo do que a escada fixa do BGS. Falta **conteúdo depois do título Mundial**.

- **S27 — Depois do Mundial: unificação e lutas de lenda** (desafios contra os melhores reformados do mundo, uma vez por ano, com prémio raro — no BGS os robôs dão "+1 ano de carreira"). Fase **9**.

---

## 15. Prémio da primeira vitória (o "Chefe do Conselho")

**BGS ✅ — é o motor do jogo.** Cada 1.ª vitória contra um adversário novo (caixa de presente verde na escolha do adversário) → escolher entre categorias:

| Categoria | Como funciona |
|---|---|
| Dinheiro | 100 000 G, sobe cada vez que se escolhe, até 20 M; depois volta a 100 000 e não sobe mais |
| Pontos | 30 → 100, depois volta a 30 |
| Aparelhos | todos os que não vêm de torneios (XL só depois do 3.º anexo) |
| Patrocinadores | os 3 só vêm daqui |
| Sócios | alguns |
| Termas / restaurante | **todas** as instalações vêm daqui (mais opções a cada nível do edifício) |
| Itens de teto, conjuntos de itens (3 de cada de 4 comidas), conjuntos para a rua (7 tamanhos) | — |

**Corner Men hoje:** está na lista da 3B ("prémio da 1.ª vitória"), não feito.

- **S26 (revista) — Prémio da 1.ª vitória contra cada pugilista do mundo: escolher 1 de 3**, com um **sinal na lista de propostas** ("🎁 nunca o venceste") para o jogador procurar adversários novos. Quem dá: uma personagem própria (ex.: "o Sr. Pimenta da Federação" ou a revista). As 3 opções vêm de: dinheiro (cresce com o nível da luta), carta comum (rara contra o top 5), **um desbloqueio** (aparelho novo na Loja, parceiro, divulgação, coisa para a rua), fama. Só conta contra adversários **do teu nível ou acima** (para não abusar). Prós: cada vitória tem presente e escolha; abre coisas sem menus. Fase **3B**.

---

## 16. Fama, popularidade, fãs e divulgação (marketing)

**BGS ✅ — 8 tipos de marketing** (abertos pelo Chefe), cada um com **10 níveis pagos**; os números crescem **em linha reta** (nível n = n × nível 1):

| Tipo | Dá | Nível 1 → nível 10 | Custo nv1 → nv10 | Sócio com nome |
|---|---|---|---|---|
| Página na internet | fãs + dinheiro/mês | 2500 fãs, 3600/mês → 25 000, 36 000 | 100 000 → 1 M | nv2 |
| Redes sociais | fãs + dinheiro/mês | 3500, 6500 → 35 000, 65 000 | 120 000 → 1,2 M | nv4 |
| Canal de vídeo | fãs + dinheiro/mês | 5000, 8500 → 50 000, 85 000 | 160 000 → 1,6 M | nv6 |
| Clube de fãs | fãs + dinheiro/mês | 3500, 4800 → 35 000, 48 000 | 160 000 → 1,6 M | nv7 |
| Limpeza do bairro | fãs + pontos/mês | 150, 4 → 1500, 13 | 45 000 → 450 000 | nv3 |
| Oficina de boxe | fãs + pontos/mês | 300, 3 → 3000, 12 | 75 000 → 750 000 | nv5 |
| Calendário de eventos | fãs + pontos/mês | 1500, 3 → 15 000, 12 | 160 000 → 1,6 M | nv7 |
| Auditório | fãs + pontos/mês | 500, 6 → 5000, 15 | 80 000 → 800 000 | nv8 |

Cada nível também dá **popularidade** (50 → 450 nos de dinheiro; 100 → 900 nos de pontos). Também sobem a popularidade: o letreiro do ginásio, o cartaz da luta (mais público), os bancos (mais adeptos). ❓ A wiki não diz o que a popularidade abre.
**Corner Men hoje:** popularidade → nível 1/2/3, lotação, treinadores, talentos, patrocínios. **Já decidido para a 3B:** **fama do ginásio** (desce devagar, **nunca perde um nível já ganho**, abre portas) ≠ **fãs de cada atleta** (bilheteira, público, confiança); carisma escondido; rookie de ginásio famoso já tem fãs.

- **S28 — Níveis de fama do ginásio com nome e o que abrem** (para o Tiago mexer):

  | Nível | Nome (exemplo) | Abre |
  |---|---|---|
  | 0 | Desconhecido | início |
  | 1 | Falado no bairro | treinadores de Clube, 1.º parceiro, sócios com nome, cartazes |
  | 2 | Conhecido na cidade | treinadores Regionais, revista (entrevistas), patrocinador com contrato, rádio local |
  | 3 | Referência regional | parceiros avançados, recrutas melhores, visitas de ex-pugilistas |
  | 4 | Nome nacional | treinadores Nacionais, televisão, cartas raras de visita, noites de luta grandes |
  | 5 | Casa de campeões | treinadores Lenda, visitas de lendas, convites para o estrangeiro |

  A etapa (S1) é a obra; a fama é a reputação. Fase **3B**.
- **S29 — Fãs à vista na Ficha, "+120 fãs (KO no 2.º round)"** depois de cada luta. Fase **3B**.
- **S30 (revista) — Divulgação como investimentos com 3 níveis, de dois tipos** (como o BGS separa "dinheiro" e "pontos"): **de dinheiro** (dão sócios/rendimento por semana: Cartazes no café e na mercearia, Rádio local, Página do ginásio) e **de fama** (dão fama e às vezes uma carta, sem dinheiro: Escolinha de boxe ao sábado, Ação no bairro, Arraial do ginásio uma vez por ano). Cada nível traz às vezes um **sócio com nome** (S12). Crescimento em linha reta e à vista (o BGS faz assim e funciona; só 3 níveis em vez de 10 para caber no ecrã). Fase **3B**.
- **S31 — A revista mostra a fama, os rankings e entrevistas com 2 respostas.** Fase **3B**.

---

## 17. Edifícios da cidade → negócios parceiros

**BGS ✅:**
- **Loja de desporto** (100 000 G; andares nos níveis 3/6/9 por 0,6 / 1,1 / 1,6 M): vende itens e equipamento pessoal; cada andar abre mais escolhas; as termas e o restaurante fazem a loja vender coisas novas.
- **Termas** (500 000; andares nos níveis 3 e 6 por 2 M e 3,5 M; 3 lugares por andar): **12 instalações** (banheira, duche, sauna seca, cadeira de massagem, banho de espuma, banho de cascata, banho turco, esfoliação, banho quente, duche de jato, sauna de infravermelhos, osteopata; 80 000 a 3,5 M G) que dão recuperação de Vida, Vida máxima, Defesa, Pés, Charm e crescimento do ânimo; cada uma tem uma **taxa** (rendimento ❓) e níveis 1–6.
- **Restaurante** (1 M; andares nos níveis 3/6/9 por 4 / 7 / 10 M): **12 pratos** (salada, soba, arroz salteado, bolo, tigela de arroz, ramen, hambúrguer, sushi, gyoza, bife, enguia, pato; 210 000 a 3,4 M) que dão recuperação de Vida/Fôlego, ânimo e **peso**; com taxa e níveis.
- Todas as instalações das termas e do restaurante **só vêm do Chefe** (prémio da 1.ª vitória).
**Corner Men hoje:** "negócios parceiros" aceites para a 3B (fisioterapia, nutricionista, loja de desporto, café, musculação), como patrocinadores que também ajudam; gancho `cardGive(id,'parceiro')`.

- **S32 (revista) — Parceiros por acordo, com 3 níveis, que ajudam e dão algum dinheiro.** O BGS mostra que termas e restaurante funcionam como **negócios que ajudam os pugilistas e rendem taxas** — é exatamente a ideia do Tiago. No Corner Men **não se constroem**: fazem-se **acordos** (entrada paga; sobem de nível com dinheiro e fama). Ex.: **Café do bairro** (fama; carta "Festa no bairro" na Loja; rende um pouco), **Clínica de fisioterapia** (recuperação −1 semana 1× por estação; carta Fisioterapia mais barata; menos risco de lesão), **Nutricionista** (opção de pesagem própria — S47; carta Semana de dieta), **Loja de desporto** (aparelhos −10%; equipamento pessoal S46), **Ginásio de musculação** (carta de Força). Como no BGS, **cada parceiro novo acrescenta cartas à Loja**. Fase **3B**.

---

## 18. Coisas na rua (à volta do ginásio)

**BGS ✅ — 13 instalações exteriores** (do Chefe ou dos torneios), umas junto ao ginásio, outras junto ao rio: candeeiro (mais moradores), letreiro do ginásio (popularidade), folhetos e banca de inquéritos (pontos), banco (mais adeptos), mesa de bebidas e relógio (corrida rende mais), máquina de bebidas e banca de donuts (dinheiro), cartaz da luta (mais público), letreiros das termas e do restaurante (popularidade deles), fato de sauna (a corrida tira mais peso).
**Corner Men hoje:** nada; na fase 4 há "rua em baixo".

- **S33 (revista) — A rua do ginásio com 5–6 coisas pequenas** (sem rio, para não copiar; o largo ou a rua do bairro): letreiro luminoso (fama), mural com o campeão do ginásio (aparece quando há um; fama), máquina de bebidas (dinheiro pouco), cartaz da próxima luta (um pouco mais de público + contagem), banco onde se sentam os velhos do bairro (histórias para o Abílio), **fonte/bebedouro no percurso da corrida** (a rotina de corrida rende um pouquinho). Vêm do prémio da 1.ª vitória e dos desafios da estação. Fase **4** + **8**.

---

## 19. Patrocinadores

**BGS ✅:** 3 patrocinadores, **só pelo Chefe**, depois de haver loja de desporto. Dão **equipamento que tira atributos** (−2 a −30) e **paga por cada vitória** (80 000 a 480 000 G). Os mais generosos são os que mais atrapalham.
**Corner Men hoje:** patrocínios = fórmula (popularidade − 20 € + extra por títulos).

- **S34 (revista) — Contratos de patrocínio com escolha (1 de 2–3 propostas por ano):** **fixo** (X €/semana), **por vitória** (mais, mas nada nas derrotas), **com exigência** (paga bem mas pede "2 lutas por estação") e — ideia do BGS — **com material da marca que atrapalha um pouco** (ex.: luvas pesadas: −2% de Velocidade, +bónus por vitória). Contrato de 1 ano; renovação conforme a fama. Prós: decisão com risco a sério. Contras: ⚠ o efeito negativo tem de ser pequeno; equilibrar a economia. Fase **3B**.

---

## 20. Itens e consumíveis

**BGS ✅:** **12 comidas** (recuperam Vida/Fôlego/ânimo, engordam 0,1–0,3 kg e **sobem o Charm do treinador**), **12 itens de treino** (halteres, batidos, toalhas, champô: +1/+2/+3 num atributo, emagrecem e **sobem a Skill do treinador**), **6 itens de teto** (+50 ao máximo de um atributo), **+1 lugar de habilidade**, **+1 ano de carreira** (até 5). Vêm das lutas, do Chefe e da loja. ✅ Crítica: "os itens são muito limitados".
**Corner Men hoje:** não há itens; as **cartas** fazem esse papel.

- **S35 — Não criar itens à parte; tudo o que seria item vira carta** (ex.: "Jantar de equipa": confiança e +0,5 kg; e, como no BGS, algumas cartas podem melhorar também a **ligação ao treinador**). Fase **3B**.

---

## 21. Treinadores

**BGS ✅:** 3 treinadores fixos (1 por andar), **todos com Skill 65** (Charm 100 / 175 / 125; Coaching 8 / 12 / 9%); salários **sobem sozinhos** até 200 000 G/mês; atributos sobem com itens (comida → Charm, treino → Skill; teto 500 e 1500); a chance de ensinar habilidades depende da Skill do treinador; reformados podem ser treinadores (com a Skill e o Charm que tinham). ✅ Críticas: "queria escolher treinadores"; no Novo Jogo+ um treinador caro arruína o início.
**Corner Men hoje:** já melhor (5 escalões, estilos, ligação, contratar 3 à escolha, reformados como treinadores).

- **S36 (revista) — O treinador cresce com os êxitos e pede aumento** — mas **só quando há razão** (atleta campeão, 10 vitórias…), nunca sozinho com o tempo como no BGS (criticado). Pode subir um escalão; cartão: aceitar o aumento / recusar (pode sair). ⚠ mexe nos escalões (fixos por contratação). Fase **3B** + **7**.

---

## 22. Idade, reforma e legado

**BGS ✅:** reformam-se **aos 24 anos** (os pugilistas entram novos; carreira de ~10 anos); "+1 ano de carreira" até 5 (prémio frequente nos torneios e nos robôs); depois treinadores ou **"2.ª geração"** 2 anos depois. ✅ Crítica: "o teu favorito acaba e tens de recomeçar".
**Corner Men hoje:** idade real; melhora até ~27–30, desce a partir dos 31; cartão de reforma a partir dos 33; hall da fama; treinador do seu estilo.

- **S37 — Prolongar a carreira, uma vez por atleta, efeito pequeno** (carta rara ou clínica nv3 atrasa a quebra física 1 ano). No BGS é um prémio comum (até 5); aqui só 1. Fase **3B/7**.
- **S38 — Despedida com "número retirado" na parede** e fama do ginásio para sempre. Fase **3B** + **8**.

---

## 23. Fotos, álbum de momentos e conquistas

**BGS ✅ — fotos** (5 pontos cada; **contam à parte em cada categoria de peso**, e na pontuação anual ×3): 2–7 combinações seguidas; um golpe com mais de 15 / 25 / 50 … 500 de dano; 10 / 20 / 30 golpes numa luta; 1 a 50 KOs; 1 título; 1 / 2 / 3 quedas numa luta; counter que derruba; uppercut que derruba; 3 / 7 / 12 esquivas de cintura; 3 / 7 esquivas de pés ou clinch; quedas em menos de 60 s; ganhar 1 / 5 / 10 / 20 / 30 lutas no 1.º round. **Conquistas** da loja: 6 (Steam/PS) ou 10 (Xbox, com marcos de 20/40/60/80 vitórias).
**Corner Men hoje:** "álbum de momentos" na lista da 3B.

- **S39 (revista) — Álbum de momentos com cromos**, ~30–40 momentos próprios: primeiro KO, primeira queda sofrida e ganha, counter que derruba, FÍGADO!, CROSS!, reviravolta, título, defesa, ganhar fora, ganhar ao rival, despedida… e, como as fotos do BGS, **marcos com degraus** (1 / 5 / 10 KOs; 3 / 7 esquivas numa luta) para durar o jogo todo. Cada cromo novo dá um pouco de **fama**. Ecrã em páginas de 9, sem scroll. Fase **3B** + **8**.
- **S40 — Marcos do ginásio (10 / 25 / 50 / 100 vitórias)** com prémio pequeno e um quadro na parede. Fase **3B**.

---

## 24. Pontuação anual, fim de jogo e Novo Jogo+

**BGS ✅ — pontuação no mês 4 de cada ano:** dinheiro ÷ 10 000 + fotos × 3 + pontos do ano ÷ 10 + popularidade ÷ 100 + **títulos × 100** + dano total ÷ 10. Abre pugilistas (300 / 1000 / 2000 / 10 000). O jogo acaba no Ano 11 Mês 4. **Novo Jogo+ guarda:** pugilistas abertos pela pontuação, atributos máximos dos pugilistas, atributos dos treinadores iniciais, itens, níveis dos edifícios. **Não guarda:** dinheiro, pugilistas dos torneios, atributos atuais, treinos abertos, lugares de habilidade, anos de carreira extra, marketing. ✅ Bug: gravar depois do Ano 11 Mês 4 perde tudo. ✅ Crítica: o modo rápido só abre no fim.
**Corner Men hoje:** sem fim; gala anual; "pontuação anual de legado" e "Novo Jogo+" estão "por encaixar".

- **S41 (revista) — Pontuação de legado anual na gala** (sem acabar o jogo): títulos (o que pesa mais, como no BGS), prémios, vitórias, fama, cromos, atletas formados no ginásio. Mostra o melhor ano e uma tabela das academias. Como no BGS, **marcos de legado abrem coisas** (ex.: um talento especial, um treinador lenda). Fase **3B** ou **9**.
- **S42 — Capítulo de 10 anos opcional e Novo Jogo+ leve** (guarda só álbum, hall da fama e um treinador). ⚠ Saves sagrados. Fase **9**.

---

## 25. "Combos" de colocação (típico da Kairosoft)

**BGS:** ✅ a wiki **não tem** combos de colocação no BGS (os "combos" são as combinações de golpes na luta). O que existe é o **laboratório** para melhorar aparelhos.
- **S43 — (Opcional) pares de aparelhos que combinam**, só com o mapa da fase 4, bónus muito pequeno. Recomendação: **adiar**. Fase **4**.

---

## 26. Tempo, eventos e o que fazer entre lutas

**BGS ✅:** o tempo corre sozinho (ano/mês/semana); modo rápido trancado até ao fim; "entre lutas não há nada para fazer"; **preocupações do pugilista** ao acaso (impedem de aprender habilidades enquanto duram).
**Corner Men hoje:** semana de 45 s, ×1/×2/×4 desde o início; eventos e objetivos por fazer (3B).

- **S44 — Uma decisão com interesse a cada 1–2 minutos reais** (×1), medida num jogo de teste antes de afinar. Fase **3B** + **7**.
- **S45 — 3 objetivos curtos, um deles ligado à próxima etapa** (S1). Fase **3B**.
- **S48 [novo] — "O atleta anda preocupado": cartões de vida pessoal com escolha** (a ideia das preocupações do BGS, com histórias próprias): a namorada quer que ele deixe o boxe, o patrão do part-time não lhe dá folga, a mãe está doente, recebeu uma proposta de outro ginásio, perdeu a confiança depois de um KO… 2–3 escolhas (dar folga, pagar, conversar com o treinador, ignorar); o resultado depende dos mentais (Coração, Calma, Ouvir o canto) e mexe na confiança, na disciplina da semana ou na técnica em curso. 1 cartão a cada poucas semanas, nunca durante a preparação de uma luta grande. Prós: dá vida aos atletas e decisões entre lutas. Contras: textos. Fase **3B** (eventos).

---

## 27. O que os jogadores elogiam e criticam (resumo)

**Elogiam (✅):** jogo de manager (instruções, não controlo); construir tipos de pugilista; ver o ginásio crescer; simples, limpo, sem anúncios; bom passatempo; a loja salva o início.
**Criticam (✅):**
1. Lento e repetitivo; nada para fazer entre lutas (o maior problema).
2. Só 3 pugilistas e demora muito a lá chegar.
3. Custos que sobem sozinhos (treino com a idade, salários) e melhorias caríssimas (4–33×) no fim.
4. Saltos grandes na força dos adversários (×5–6 numa categoria); demasiado acaso.
5. Reforma obrigatória aos 24 / ~10 anos de carreira.
6. Modo rápido trancado; lutas lentas a começar.
7. Treino opaco e repetitivo; itens limitados; não se escolhem treinadores.
8. Bugs (Novo Jogo+, tutorial preso sem pontos, prémio duplicado).

**O Corner Men já resolve:** 2 (em parte), 4 (rankings vivos, muitos fatores), 6 (×4), 7 (treino sozinho, cartas, treinadores à escolha). **Falta:** 1 (S24, S44, S45, S48), 3 (S8, S9, S36), 5 (S37, S38) e o fim de jogo (S27, S41, S42).

---

## 28. Tabela das sugestões (responder sim/não por número)

(revista) = mudou nesta versão por causa dos dados da wiki · [novo] = sugestão nova

| N.º | Sugestão | Fase | Conflito? |
|---|---|---|---|
| S1 | Etapas do ginásio (cave → bairro → clube → casa de campeões → renome) com 3 condições à vista | 3B + 4 + 7 | — |
| S2 | Lugares de atleta abertos pelas etapas; 2.º atleta cedo (~6 meses) | 3B | muda o código atual |
| S3 | Ao abrir um lugar, escolher 1 de 2–3 talentos | 3B | — |
| S4 | (Opcional) começar com 1 treinador | 3B | ⚠ início decidido — recomendo não |
| S5 | Espaço como limite: lugares de aparelho por sala | 3B + 4 | — |
| S6 | Obras com efeitos de jogo | 3B | — |
| S7 | Um lugar "grande" para um aparelho especial | 3B / 7 | — |
| S8 (revista) | Preços que sobem à vista e moderados: gamas de aparelhos + pequena subida por aparelho | 3B + 7 | escolher com S5 |
| S9 (revista) | Melhorar aparelhos (níveis 1–3) com custos comedidos (nunca 4–33×) | 3B / 7 | — |
| S10 | Aparelhos que se ganham | 3B | — |
| S11 | Sócios continuam um número; lotação trava cada etapa | 3B | — |
| S12 (revista) | 4–8 sócios com nome que entram com marcos (fama, obras, divulgação) | 3B + 4/8 | — |
| S13 | Treinadores livres dão aulas aos sócios | 3B | — |
| S14 (revista) | Talentos de várias fontes (etapa, desafio da estação, olheiro, sócio, porta, legado) | 3B | — |
| S15 | Herdeiro de uma lenda | 3B / 9 | — |
| S16 | Não mudar os atributos | — | — |
| S17 | Carisma escondido mostrado por palavras | 3B | — |
| S18 | Treino visível no ginásio | 4 / 8 | — |
| S19 | Carta da estação na Loja (as estações não mexem no treino) | 3B | evita ⚠ |
| S20 | Não criar uma 2.ª moeda | — | — |
| S21 | Prémio raro +1 lugar de técnica | 3B / 7 | mexe pouco nos lugares |
| S22 | Técnicas avançadas abertas por conquistas do ginásio | 3B | ⚠ técnicas livres |
| S23 | Regras do peso: nada a mudar | 7 | — |
| S24 (revista) | Desafios da estação com níveis a abrir (provas sem luta, prémios pequenos) | 6 ou 3B | — |
| S25 | Saltar a entrada com 1 toque e ×2 na luta desde o início | 3B / 8 | — |
| S26 (revista) | Prémio da 1.ª vitória: escolher 1 de 3, com sinal 🎁 nas propostas | 3B | — |
| S27 | Depois do Mundial: unificação e lutas de lenda | 9 | — |
| S28 | Níveis de fama do ginásio com nome e o que abrem | 3B | — |
| S29 | Fãs à vista depois da luta | 3B | — |
| S30 (revista) | Divulgação com 3 níveis, de dois tipos (dinheiro / fama), com sócios com nome | 3B | — |
| S31 | Revista: fama, rankings e entrevistas | 3B | — |
| S32 (revista) | Parceiros por acordo, 3 níveis, ajudam, rendem um pouco e acrescentam cartas à Loja | 3B | — |
| S33 (revista) | A rua do ginásio (letreiro, mural, máquina, cartaz, banco, fonte da corrida) | 4 + 8 | — |
| S34 (revista) | Contratos de patrocínio, incluindo material da marca que atrapalha um pouco | 3B | ⚠ efeito pequeno |
| S35 | Sem itens à parte: tudo vira carta | 3B | — |
| S36 (revista) | O treinador cresce e pede aumento só com razão (nunca sozinho) | 3B + 7 | mexe nos escalões |
| S37 | Prolongar a carreira, uma vez, efeito pequeno | 3B / 7 | — |
| S38 | Despedida com "número retirado" | 3B + 8 | — |
| S39 (revista) | Álbum de momentos com cromos e marcos em degraus | 3B + 8 | — |
| S40 | Marcos do ginásio (10/25/50/100 vitórias) | 3B | — |
| S41 (revista) | Legado anual na gala; marcos de legado abrem coisas | 3B / 9 | — |
| S42 | Capítulo de 10 anos opcional e Novo Jogo+ leve | 9 | saves sagrados |
| S43 | (Opcional) pares de aparelhos que combinam | 4 | adiar |
| S44 | Uma decisão com interesse a cada 1–2 min reais | 3B + 7 | — |
| S45 | 3 objetivos curtos, um ligado à próxima etapa | 3B | — |
| S46 [novo] | Equipamento pessoal (luvas, calções, sapatilhas) com aluguer; efeito mínimo ou só fãs | 3B + 8 | ⚠ vantagens pequenas |
| S47 [novo] | Dar à pesagem uma cara própria (opções, preços e efeitos diferentes do BGS) | 3B | mexe no que está feito (textos/números) |
| S48 [novo] | "O atleta anda preocupado": cartões de vida pessoal com escolha | 3B | — |
| S49 [novo] | Obra "ringue de treino" que acelera um pouco as técnicas | 3B / 7 | — |

**Recomendação de prioridade para a 3B:** S1 + S2 + S3 (ritmo e lugares), S28 (fama), S26 (prémio da 1.ª vitória), S44 + S45 + S48 (decisões entre lutas), S5 ou S8 (espaço/preços), S32 + S34 (parceiros e patrocínios), S47 (originalidade da pesagem), S39 (álbum). O resto pode esperar.
