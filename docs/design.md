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
| 0.5 | **Animações:** cada ação do Guia fica marcada como *usa animação existente*, *precisa de animação nova* ou *só texto*. Lista "Animações necessárias" no fim deste documento. Cada fase implementa-se em dois passos: mecânica com animações existentes + comentador; depois uma passagem de animação com capturas para o Tiago aprovar. Poucas animações, só as que mudam a leitura da luta. | Decidido |

## Fase A — Núcleo da luta · *Decidido*

Ordem: 8 → 5 → 1 → 3 → 4.

### Tema 8 — Atributos físicos, técnicos e mentais · *Implementado* (A1)
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
- **Decisões:**
  - 8.1 **Decidido:** 8 barras — Força, Velocidade, Resistência, Queixo (físicos) / Técnica, Defesa, Pés, Ring IQ (técnicos).
  - 8.2 **Decidido — mentais:** todos os atletas têm os 7 mentais do Guia, cada um com o seu valor (Coração, Calma, Disciplina, Confiança, Concentração, Instinto finalizador, Ouvir o canto). A **personalidade** é um nome que sai do que se destaca (ex.: muito coração + pouca calma → "Guerreiro impulsivo"); os traços atuais (Teimoso, Cabeça fria…) passam a nascer daqui.
    - **Ecrã:** só o nome da personalidade e 2–3 palavras sobre o que se destaca; sem barras nem números (o jogador descobre o atleta a vê-lo lutar).
    - **Mudam devagar** com a carreira (confiança com vitórias, calma com experiência, coração após vitórias sofridas…).
    - **Não se treinam no ginásio:** só com experiência e com o treino mental (tema 10).
  - 8.3 **Decidido:** Queixo difícil de treinar (pescoço, core); desce com a idade e com cada KO sofrido.
  - 8.4 **Decidido:** Ring IQ cresce sobretudo com experiência (lutas e sparring), pouco com treinos de ginásio.
- **Implementado (A1, save novo `corner-men-v7`):**
  - 8.1 Ficha com 2 colunas FÍSICO / TÉCNICO. Treinos: Corda e Shadow boxing → Pés; Sparring → Ring IQ (pouco); Bola medicinal → Queixo (muito pouco). Só Força, Velocidade e Resistência perdem condição sem treino.
  - 8.2 Mentais escondidos (5–95). Personalidade = nome do par que mais se destaca (ex.: Guerreiro impulsivo, Calculista, Arrogante, Aluno exemplar) ou de um só (Coração de leão, Teimoso, Trabalhador…); "Equilibrado" se nada se destaca. Efeitos: Disciplina → ganho nos treinos e fadiga; Ouvir o canto (+ Ring IQ) → rapidez a ouvir e teimosia; Calma → confiança perdida nas derrotas e fôlego; Coração → levantar-se; Concentração → últimos rounds; Instinto finalizador → agressividade com o adversário magoado; Confiança → valor para onde a confiança do dia volta. Mudam com as lutas (confiança, calma, coração em vitórias sofridas, finalizador em KOs).
  - 8.3 Queixo de nascença (escala própria, ~50 = normal em qualquer escalão): quedas, quedas relâmpago, dano à cabeça e levantar-se. Desce em cada derrota por KO e a partir dos 28 anos (os atletas fazem anos).
  - 8.4 Ring IQ sobe em cada luta (mais com mais rounds) e um pouco com Sparring; acelera o ouvir o canto e ajuda o contra-golpe. Pés: por agora só o recuar como defesa (a distância vem no tema 5). Algumas táticas do canto pedem agora Pés ou Ring IQ.

### Tema 5 — Pés, distância e controlo do ringue · *Implementado* (A3; análise e animações no A4)
- **Hoje:** zonas do ringue e alcance existem; não há distância longa/média/curta explícita.
- **Guia:** distância longa/média/curta, trabalho de pés, controlo do ringue.
- **Decisões:**
  - 5.0 **Decidido:** a distância (longe / meio / perto) e o sítio do ringue (centro / cordas / canto) passam a contar na luta (hoje são só visuais).
  - 5.1 **Decidido — quem decide a distância:** cada atleta tem uma distância preferida que vem do estilo (Outboxer longe, Puncher meio, In-fighter perto). Quando querem distâncias diferentes, disputam-na: conta sobretudo **Pés**, depois **Ring IQ**. Nunca é garantido. A influência da **estratégia** fica por decidir: a estratégia ainda vai ser redefinida (plano de combate); se fizer sentido na altura, entra.
  - 5.2 **Decidido — efeito de cada distância:** **longe** — jab e direto; alcance conta muito; menos dano, mais pontos; pouco fôlego gasto. **Meio** — direto, combinações, ganchos largos; troca equilibrada. **Perto** — ganchos curtos, uppercuts, corpo, clinch; jab quase sem força; braços longos atrapalham um pouco; mais dano e mais fôlego gasto. Os golpes treinados valem mais ou menos conforme a distância.
  - 5.3 **Decidido — centro, cordas e canto:** quem ganha a disputa para se aproximar empurra o outro para as cordas e depois para o canto ("cortar o ringue"); quem prefere longe e tem Pés circula e fica no centro. Cordas: defende e foge pior, luta tende para perto. Canto: quase sempre perto, defende ainda pior, combinações fazem mais estragos. Sai-se com Pés (pivô, passo lateral), clinch ou a bater para sair. Em rounds equilibrados, quem dominou o centro tem uma pequena vantagem nos juízes. Comentador e análise (tempo no centro/cordas/canto) mostram isto.
  - 5.4 **Decidido — estado mexe nos Pés:** os Pés que contam na luta descem com pouco fôlego e com muita dor; logo depois de uma queda, "pernas bambas" (Pés caem muito durante um bocado). O atleta cansado vai sendo empurrado para as cordas.
  - 5.5 **Decidido — ecrã:** pequena barra LONGE · MEIO · PERTO por cima do ringue, junto ao relógio, além do movimento no ringue, do comentador e da análise.
- **Animações (tema 5):** pivô/passo lateral e circular — usam o movimento existente; clinch — existe; **encostado às cordas/canto** — nova; **pernas bambas** — nova; a distância vê-se pela distância entre os lutadores no ringue.
- **Implementado (A3):**
  - 5.0/5.1 `F.dist` (longe/meio/perto) e `F.zone` (centro/cordas/canto) contam na luta. Distância preferida pelo estilo; em cada troca, se querem distâncias diferentes, disputam-na: Pés que contam agora + metade do Ring IQ, com um mínimo de 12% para quem perde (nunca garantido). **A estratégia não entra** (fica um parâmetro `TUNE.dStrat` a 0 para quando o plano de combate for decidido). Se querem a mesma distância, vão para lá com algum vaivém.
  - 5.2 Escolha do golpe e da defesa, acerto e dano pela tabela `DIST_FIT`: longe vive do jab e do direto (o primeiro golpe é mais vezes o jab, menos golpes seguidos), alcance conta o dobro, ganchos e uppercuts quase não chegam, 80% do dano e do fôlego gasto; perto — ganchos, uppercuts, clinch, jab quase sem força, braços longos atrapalham um pouco, 115% do dano e 120% do fôlego. O fígado usa a curta distância. Recuar com os Pés pode abrir a distância.
  - 5.3 Quem ganha a disputa para se aproximar pode empurrar o outro para as cordas e depois para o canto; quem a ganha para se afastar pode sair (pivô/passo lateral). Nas cordas a disputa pende para quem se aproxima e não há espaço para longe; no canto é quase sempre perto. Encostado: a defesa rende 85% (cordas) / 70% (canto) e leva mais golpes; no canto as combinações fazem +20% de dano. Sai-se com os Pés (disputa ou defesa de pés a resultar), com o clinch ou a bater (2+ golpes a entrar). Em rounds equilibrados, quem controlou o ringue (mais tempo a encostar o outro ou a ganhar a distância) tem uma pequena vantagem nos juízes.
  - 5.4 Os Pés que contam (`pesEff`) descem com fôlego abaixo de 50 e vida abaixo de 50; depois de uma queda, "pernas bambas" (~27 s de relógio, Pés a 45%; o que sobra passa em parte ao round seguinte). O mesmo vale para a defesa de Pés.
  - 5.5 Barra LONGE · MEIO · PERTO por baixo do relógio, no cabeçalho do ringue. A distância entre os lutadores no ringue e o sítio (centro/cordas/canto) seguem o estado; o comentador diz "mantém-no à ponta do jab", "encurta a distância", "encostou-o às cordas", "saiu com um pivô", "pernas bambas", etc.
  - Dados por luta para a análise do A4 (`an.dz`, um por lutador): segundos em cada distância e no centro/cordas/canto, segundos a controlar o ringue, trocas ganhas em cada distância, antecipações, cross-counters, counters de ângulo e de clinch, saídas das cordas (pés/clinch/a bater). A análise ainda não os mostra.
  - Ritmo: os lutadores andam menos no ringue do que antes; um tempo a estudar-se em cada troca (`TUNE.fwT`) mantém o número de golpes por round como no A2.

### Tema 1 — Golpes · *Implementado* (A2)
- **Hoje:** jab, direto, gancho, uppercut, direto ao corpo, gancho ao fígado, Contra-golpe.
- **Guia:** numeração 1–6 (mão da frente/de trás), overhand, cabeça/corpo como alvo, variações (jab duplo, power jab, flicker jab, check hook, shovel hook, cross-counter…), que treino ensina cada golpe, números usados pelo comentador.
- **Nota:** havia perguntas em aberto deste tema numa conversa anterior que não ficaram registadas; refazem-se aqui.
- **Decisões:**
  - 1.1 **Decidido:** os golpes do atleta são os 7 do Guia — 1 jab, 2 direto, 3 gancho da frente, 4 gancho de trás, 5 uppercut da frente, 6 uppercut de trás, overhand — cada um com o seu nível.
  - 1.2 **Decidido:** cabeça ou corpo é o **alvo** do golpe, escolhido pelo atleta na luta (não há golpes "ao corpo" separados). À cabeça: mais quedas e KOs; ao corpo: tira fôlego e baixa a guarda. **Gancho ao fígado** = gancho da frente ao corpo, com uma pequena hipótese de efeito especial: leve (perde muito fôlego, fica curvado uns segundos) ou forte e raro (queda atrasada, difícil levantar-se mesmo lúcido). Hipótese maior com golpe forte, adversário cansado, muito trabalho ao corpo antes, e a curta distância; o Queixo ajuda pouco.
  - 1.3 **Decidido:** o Contra-golpe deixa de ser um tipo de golpe. Um counter é um dos 7 golpes lançado logo a seguir a uma defesa, com bónus por apanhar o adversário aberto; o golpe que sai depende da defesa (tabela do Guia). O comentador e a análise chamam-lhe counter. O que torna um atleta bom a contra-atacar decide-se nos temas da defesa e do contra-ataque.
  - 1.4 **Decidido — variações:** nenhuma é golpe treinado à parte. **Alvo:** jab/direto/gancho/uppercut ao corpo. **Distância:** gancho e uppercut curtos (perto) ou largos/longos (meio). **Outros temas:** jab duplo/triplo, gancho duplo, hook off the jab → combinações; feint jab, range finder → fintas; check hook, cross-counter → contra-ataque; straight left → guarda; jab de recuo → distância (usado quando é empurrado). **Só texto (comentador):** power jab, flicker jab, lead right, pivot hook, shovel hook, leaping uppercut, bolo punch, corkscrew, hookercut. Ilegais → faltas.
  - 1.5 **Decidido (provisório, o Tiago pode mudar depois):** o comentador usa os números do Guia sobretudo nas combinações ("1-2!", "1-6-3-2"), e o nome nos golpes soltos; a Ficha mostra o número ao lado de cada golpe ("3 Gancho da frente").
  - 1.6 **Decidido — como se treinam:** nas **luvas de foco** o treinador escolhe o golpe da semana (muita experiência nesse golpe; pode ser um golpe que o atleta ainda não sabe, se os atributos deixarem — aprende-o em algumas sessões). Os outros treinos dão um pouco aos golpes ligados (Guia): saco pesado → 2, 4, overhand; saco de ângulo → 3–6; saco de velocidade → 1; saco duplo elástico → 1, 2; shadowboxing → todos um pouco; sparring → os golpes mais usados. Lista final de treinos no tema dos treinos.
- **Implementado (A2):**
  - 1.1 Os 7 golpes com nível 1–5 e experiência (`jab, direto, ganchoF, ganchoT, upperF, upperT, overhand`). Saíram o Direto ao corpo, o Gancho ao fígado e o Contra-golpe. Para aprender: Direto Técnica 20; ganchos Força 28/30 e treinador assistente; uppercuts Força 22–25 e Técnica 25; overhand Força 30 e Direto nv 2. O overhand gasta mais fôlego e usa a animação do gancho de trás.
  - 1.2 Alvo escolhido em cada golpe (estilo: In-fighter vai mais ao corpo, Outboxer menos; corpo mais cedo na luta e com o adversário cansado; cabeça quando ele está magoado; ordem do canto "ao corpo"). Corpo: tira fôlego e acumula trabalho ao corpo, que baixa a guarda (mais acerto à cabeça). Só golpes à cabeça dão quedas relâmpago. Fígado = gancho da frente ao corpo que entra: hipótese pequena (força, nível, adversário cansado, trabalho ao corpo acumulado, curta distância — neutra até ao A3 —, Queixo pouco). Leve: perde muito fôlego e fica curvado uns segundos (animação `hurtBody`; não ataca e defende pior). Forte (~15% dos casos): "aguenta um segundo… e cai", contagem difícil mesmo lúcido.
  - 1.3 Counters: ver 3.3/4.1.
  - 1.4 Variações só no comentador: flicker jab, power jab, lead right, corkscrew, shovel hook, pivot hook, hookercut, leaping uppercut, bolo punch (quando encaixam no golpe/estilo/alvo).
  - 1.5 Comentador: números nas combinações ("1-2-3 de X: 3 golpes a entrar!"), nomes nos golpes soltos. Ficha → GOLPES: número ao lado de cada golpe, em 2 colunas (golpes | defesas) com o nível; tocar abre o detalhe (para que serve, como se treina, progresso). Os estilos passaram para um separador próprio (ESTILOS) para caber sem scroll. As combinações antigas passaram a 1-2, 1-1-2, 1-2-3, 3-3 corpo-cabeça, 1-6-3-2, 1-2-3-2 (o tema 2 mexe nelas a sério).
  - 1.6 Pads: no plano aparece "PADS · GOLPE DA SEMANA" (Livre ou um dos 7); o golpe escolhido leva quase toda a experiência; um golpe que ainda não sabe aprende-se em ~3 sessões se os atributos deixarem. Saco → 2, 4, overhand; Pera → 1; Shadow → todos; Sparring → os mais usados nas lutas. **Saco de ângulo e saco duplo elástico ficam para o tema 9** (são equipamento novo: loja, ginásio animado e treino).

### Tema 3 — Defesa · *Implementado* (A2; counters de Pés e Clinch no A3)
- **Hoje:** defesas com níveis (bloqueio, esquiva, baixar, recuar…).
- **Guia:** 6 famílias — bloqueio, parry, movimento de cabeça, ombro, pés, clinch — cada uma abre um contra-golpe específico.
- **Decisões:**
  - 3.1 **Decidido — 6 famílias**, cada uma com nível 1–5: **Bloqueio** (tudo um pouco, ganchos e corpo; seguro, absorve algum dano, quase não abre counters), **Aparar/parry** (retos; sem dano; não serve contra ganchos), **Movimento de cabeça** (slip contra retos, pendular contra ganchos/overhand; sem dano, melhores counters; gasta fôlego e piora com o cansaço), **Ombro** (direto e retos; ótimo para contra-atacar; precisa de timing/Ring IQ, arriscado), **Pés** (recuar, pivô, passo lateral; evita combinações inteiras; liga à distância; gasta fôlego), **Clinch** (magoado/cansado, perto; trava e recupera um pouco; árbitro separa, juízes não gostam). O atleta escolhe sozinho conforme o golpe que vem, os níveis, a distância e o estado; o estilo pesa (Outboxer: pés e aparar; In-fighter: cabeça e bloqueio; Puncher: bloqueio).
  - 3.2 **Decidido — confiança em cada habilidade (vale para golpes e defesas):** cada habilidade tem um **nível real** (decide se resulta) e um **nível em que o atleta acredita** (decide se a usa). Habilidade nova começa com pouca confiança; cada sucesso em sparring/luta sobe a crença, cada falhanço desce; a Confiança e a personalidade puxam para cima/baixo; Ring IQ alto corrige mais depressa. Também se ajusta durante a luta. O jogador vê notas vagas na Ficha ("ainda não confia", "confia demais") e números na análise ("tentou o overhand 15 vezes, entrou 2"). O sparring serve também para ganhar confiança. O treinador poder corrigir no canto decide-se no plano de combate.
  - 3.3 **Decidido — counters por defesa** (tabela do Guia + Pés e Clinch): slip para dentro do jab → 2 ou cross-counter; slip para fora do jab → 4 ou 6 ao corpo; slip do direto → 3; pendular do gancho → gancho/uppercut do lado contrário; aparar o jab → 1 ou 2; pull back → 2; shoulder roll → 2 por cima; bloqueio de gancho → gancho da mesma mão; *pivô/passo lateral → ataque de ângulo (gancho ou direto)*; *clinch → ao separar, gancho/uppercut curto*. Hipótese de counter: família (cabeça e ombro mais; aparar e pés médio; bloqueio e clinch menos), nível da defesa, Ring IQ, Técnica, confiança. Se não souber o golpe, usa a alternativa; senão não há counter. Counter tem bónus de precisão e dano (mais quedas relâmpago ao queixo). Comentador diz o nome; análise conta counters por defesa.
- **Implementado (A2):**
  - 3.1 As 6 famílias com nível 1–5 (`bloqueio, aparar, cabeca, ombro, pes, clinch`). Antes de cada golpe o defensor escolhe a família: lê o golpe que vem (mais com Ring IQ), eficácia da família contra esse golpe (retos / ganchos / uppercuts / corpo), nível, crença, estilo (Outboxer pés e aparar; In-fighter cabeça e bloqueio; Puncher bloqueio) e estado (cansado: menos cabeça e pés; magoado: clinch). A defesa errada para o golpe defende pior. Bloqueio deixa passar ~15% do dano; cabeça e pés gastam fôlego e pioram com o cansaço; Pés usa o atributo Pés e corta a combinação; ombro precisa de Ring IQ e, se falha, o golpe entra mais forte; clinch trava a combinação, recupera fôlego, o árbitro separa e conta contra quem agarra nos juízes. Todos começam com Bloqueio 1 e Pés 1; o Clinch vem com Resistência 20. Treinos: Corda de esquiva → cabeça; Shadow → cabeça e pés; Corda → pés; Pads → aparar; Bola medicinal → bloqueio; Sparring → todas (mais as que usa).
  - 3.2 Confiança em cada golpe e defesa (`a.bel`): o nível real decide se resulta, a crença decide quantas vezes a usa. Cada sucesso sobe, cada falhanço desce (na luta e no Sparring); equilíbrio no nível real, puxado pela Confiança (mental) e pela confiança do dia; Ring IQ corrige mais depressa. Golpe novo começa a 0,3; subir de nível dá só um pouco. Ficha: ▼ "ainda não confia" / ▲ "confia demais" só quando a diferença é grande; depois da luta, uma linha se a confiança mudou muito ("Ganhou confiança no gancho da frente"). A análise guarda tentados/acertados por golpe e tentadas/resultadas por defesa (números finos no A4).
  - 3.3 (A3) Pés → pivô/passo lateral abre um ataque de ângulo (gancho da frente ou direto, ou jab), com bónus de acerto (ele está virado); Clinch → ao separar, quem agarrou pode sair a bater com gancho ou uppercut curto. Contam na análise como counters de pés e de clinch.
  - 3.3 Counters pela tabela do Guia (slip para dentro → 2 / overhand; slip para fora → 4 ou 6 ao corpo; slip do direto → 3 / 5; pull back → 2 / 1; pendular → gancho/uppercut do lado contrário (contra o gancho da frente → 3 ou 5; contra o de trás ou o overhand → 4 ou 6); aparar ou apanhar o jab → 1 ou 2; shoulder roll → 2 / overhand; bloquear um gancho → gancho da outra mão, a que bloqueou). Pés (ângulo) e clinch (sair a bater): ver A3, acima.

### Tema 4 — Contra-ataque · *Implementado* (4.1 no A2; 4.2 e 4.3 no A3)
- **Hoje:** Contra-golpe dispara depois de uma defesa.
- **Guia:** contra-ataque antes, ao mesmo tempo e depois.
- **Decisões:**
  - 4.1 **Implementado (A2) — depois:** defender e responder (tabela 3.3). Hipótese: família (cabeça e ombro mais; aparar médio; bloqueio pouco), nível da defesa, Ring IQ, Técnica, confiança do dia e crença no golpe de resposta; o In-fighter é mais difícil de contra-atacar (como antes). O counter tem bónus de acerto e dano, o adversário defende pior (apanhado aberto) e, se entra limpo à cabeça, mais hipótese de queda relâmpago. O comentador diz o nome ("Slip e direto por cima!"); a análise conta counters por família.
  - 4.2 **Implementado (A3) — antes (antecipação):** quando o adversário ganha a disputa para se aproximar, o atleta pode tentar apanhá-lo a entrar: jab (de longe; "jab de recuo" se está a ser empurrado) ou check hook (gancho da frente, de meia distância). Hipótese: Ring IQ, Velocidade, Pés que contam, nível e crença no golpe. Se o golpe entra, a distância não encurta; se não, ele entra.
  - 4.3 **Implementado (A3) — ao mesmo tempo (cross-counter):** contra jab ou direto à cabeça, o defensor (se sabe o direto) pode soltar o direto por cima sem defender. Tenta mais com Ring IQ e crença no direto (menos perto, nunca com pernas bambas). Timing: Ring IQ, Técnica, Velocidade (contra a do outro) e nível do direto. Se resulta, o golpe dele não entra e o direto entra com bónus de dano e muita hipótese de queda relâmpago; se falha, os dois acertam. Conta à parte dos counters por defesa.
  - 4.4 **Decidido:** ser bom contra-atacante vem de Ring IQ (o mais importante), níveis das defesas e dos golpes de resposta, e confiança. Drills de parceiro como treino → tema dos treinos.

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
- **Decisões:**
  - 9.1 **Decidido — velocidade de aprender e melhorar** (vale para golpes, defesas, atributos e estilos): depende do **treinador** (qualidade da equipa técnica: adjunto melhor/mais treinadores; especialista de um estilo ensina mais depressa os golpes desse estilo) e do **atleta** (Disciplina, Concentração, Técnica para golpes novos, fadiga da semana, confiança do dia). Nas luvas de foco, "aprende em ~N sessões" mostra a estimativa desse atleta. Números ficam para o equilíbrio. **Implementar no passo A4.**

### Tema 10 — Treino mental e tático
- **Guia:** vídeos do adversário, plano de combate, peso/pesagem.
- **Liga com:** pesagem (adiada), "chave do plano" da pesquisa a outros jogos.
- **A decidir aqui:** como funciona mudar de estilo/plano durante a luta (incluindo o adversário), e se o canto deve dar uma pista do que o canto dele vai mudar no intervalo.
- **Decisões:** —

### Tema 11 — Faltas e golpes ilegais
- **Decisões:** —

---

## Já implementado (fora do Guia)

- **Ordens do canto durante o round:** Pressão / Equilibrado / Cautela. O treinador grita até o atleta ouvir; o ritmo a que ouve depende do estado atual (cansado/dorido ouve mais devagar; muito cansado e muito dorido não ouve). Se o gongo tocar antes, ouve no intervalo.
- **Toalha a meio do round**, com confirmação (a luta pára enquanto se confirma).
- **Análise pós-luta:** Resumo, Golpes, Rounds, Canto; motivos com dica de treino; diferenças de atributos ditas por palavras, sem números.
- **Histórico de lutas** na Ficha (separador LUTAS, páginas de 4): registo curto de todas as lutas; análise completa só das últimas 3. Sem limite: mostra todas as lutas do atleta. Uma ordem ouvida durante o round mantém-se no canto seguinte.
- **Estratégia no canto** entre rounds: a ordem que ficou por ouvir aparece já escolhida; o treinador pode mudá-la.

## Adiado (não começar sem o Tiago pedir)

- **Update visual maior** do jogo: o Tiago quer fazê-lo depois. Por agora a prioridade é definir como as coisas funcionam; as passagens de animação de cada fase ficam no mínimo necessário para se perceber a luta.

- Dinheiro no fim de jogo (ainda sem direção).
- Taças sazonais e pesagem (a definir como funcionam).
- Acelerar o título Amador, animações dos golpes ao corpo, golpe especial.
- Equilíbrio geral (incluindo: Cautela não protege o atleta dorido, porque a Pressão domina no nível médio).

## Ideias da pesquisa (Boxing Gym Story e MMA Manager 2) por encaixar

Noites de luta organizadas pelo ginásio · hall da fama / reformados como treinadores · parceiro de sparring contratado · treinadores com nível máximo · prémio da primeira vitória contra cada adversário · equipamento de patrocinador · pontuação anual de legado · rivalidades e desforras · galeria de momentos · prolongar a carreira · Novo Jogo+ com o que passa bem explicado. Regras: lutas curtas com 1–2 decisões que contam; ganhar tem de pagar claramente mais do que perder.

## Animações necessárias

| Ação | Tema | Estado |
|---|---|---|
| Encostado às cordas / ao canto | Distância | Por fazer (A4). No A3 vê-se pela posição no ringue (`F.zone`, `F.zp`, lado `F.zs`) |
| Pernas bambas (depois de uma queda) | Distância | Por fazer (A4). No A3 usa `stagger` de vez em quando enquanto `x.wobbly > F.ft` |
| Antecipação / cross-counter / ângulo / sair do clinch | Contra-ataque | Usam as animações dos golpes (A3) |
| Overhand | Golpes | Usa a do gancho de trás (A2); própria se o Tiago quiser |
| Curvado depois do fígado | Golpes | Usa `hurtBody` (A2) |
| Slip / pendular / aparar / ombro / pivô | Defesa | Usam slip, duck, block e o movimento existente (A2) |
