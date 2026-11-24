# Pesquisa: o direto perfeito (para a animação)

Guarda ortodoxa (pé esquerdo à frente), direto de direita à cabeça (em inglês *cross*, *straight right*, *rear-hand straight*). Objetivo: animar um boneco de ~40×60 px com um esqueleto 3D (pelvis, rotação de ancas e peito, inclinação do tronco, cabeça, pulsos, pés, cotovelos). Mesmo formato e mesmas unidades do relatório do jab (`docs/pesquisa-jab.md`), para se poderem comparar.

> **Fontes e marcas.** Li por inteiro: os guias do **Expert Boxing** (Johnny N) que falam do direto — *The Beginner's Guide to Boxing*, *How to Throw a One-Two*, *How to Throw a Straight Punch*, *How To Punch Harder*, *Basic Boxing Punches*, *Power Punching Secrets 1 e 2*, *How do you punch straight with the back hand?*, *10 Counters for the Right Hand* (o Expert Boxing não tem um guia só do direto); o artigo de **Stanley et al. 2018** (PDF completo, Tabelas 2a e 2b); a **tese da METU** (2011; não mede o direto, só o jab, o gancho e o uppercut, mas tem a revisão de Filimonov 1985 e de Donivan 1984). O resto (Cheraghi 2014, Dinu 2020, o estudo de 2026 com 17 pugilistas de elite, Cabral 2010, Turner 2011, Tong-Iam 2017, Lenetsky 2020, Piorkowski 2011, Precision Striking, Boxing News, Dynamic Striking, Wikipedia…) foi lido **através de excertos da pesquisa web**, porque os sites estavam bloqueados ou não foram abertos (lista no fim). **[fonte]** = dito por uma fonte (com link); **[estimativa]** = valor meu, coerente com as fontes, para a animação.
>
> **Em resumo, o direto é o contrário do jab:** no jab "nada mais se mexe" além do braço; no direto **é o corpo que bate** — o pé de trás roda, a anca roda, o peito roda (muito mais do que os 20° que o motor deixa), o peso vai um pouco para a frente e trava na perna da frente, e o braço só se estica no fim.

---

## 1. Fases e tempos

### Fases

- **Expert Boxing:** "roda as ancas e o tronco no sentido contrário aos ponteiros do relógio enquanto **rodas o pé direito (cerca de 90°)**. Expira com força enquanto estendes o punho direito **a direito, a partir do queixo**. Roda o punho para bater **com a palma para baixo**. **Não deixes a cabeça passar o joelho da frente.**" **[fonte]** ([Beginner's Guide](https://expertboxing.com/boxing-basics/how-to-box/the-beginners-guide-to-boxing)). E: "o pé roda, as ancas rodam, os ombros rodam, os braços estendem e o punho fecha — **tudo ao mesmo tempo**" **[fonte]** ([7 Basic Punching Tips](https://expertboxing.com/7-basic-punching-tips)).
- **Ordem (cadeia cinética):** a cadeia começa em baixo — tornozelo → joelho → anca → ombro → cotovelo → punho; a extensão do tornozelo, do joelho e do cotovelo começa a ~**45 %, ~60 % e ~80 %** do golpe (Cheraghi et al. 2014, via excertos) **[fonte]** ([ResearchGate](https://www.researchgate.net/publication/281098708_Kinematics_of_Straight_Right_Punch_in_Boxing)). Cabral et al. 2010: **a pelvis começa a rodar para o alvo enquanto o tronco ainda está a rodar para trás** (pequena "carga") **[fonte]** (citado em [Lincoln SAS blog](https://sas.blogs.lincoln.ac.uk/2023/03/07/a-biomechanical-perspective-on-increasing-rear-hand-straight-punch-performance/)). Tong-Iam et al. 2017 (3 profissionais): a rotação do tronco **atinge o máximo no impacto** (~80 % do tempo do golpe) **[fonte]** ([efsupit](https://efsupit.ro/images/stories/30dec2017/Art%20287.pdf)).
- **Stanley 2018:** no direto, o ombro atinge a velocidade máxima aos **91 ± 8 %** do movimento e o cotovelo aos **99 ± 1 %** (o ombro ~8,5 % antes do cotovelo): **o braço é o último a disparar e acelera até ao contacto** **[fonte]** ([PDF Chester](https://chesterrep.openrepository.com/server/api/core/bitstreams/3e769a4f-d46b-4921-a2e9-093e0a80e436/content)).
- **Lenetsky 2020:** define três fases para os golpes retos (incluindo o de trás): **arranque, execução, impacto** — sem preparação nem regresso **[fonte]** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/)).

Para a animação usamos 6 fases: **guarda → arranque (pé e anca) → rotação → extensão → impacto → regresso**. Ordem a respeitar: **pé → anca → peito/ombro → braço**, com cada parte a começar antes de a anterior acabar.

### Tempos medidos (comparados com o jab)

| Medida | Direto | Jab | Fonte |
|---|---|---|---|
| Do arranque ao contacto (15 amadores, força máxima) | **495 ± 150 ms** | 405 ± 150 ms | Stanley 2018, Tabela 2a |
| Velocidade de pico do punho | **6,97 ± 0,86 m/s** | 5,85 ± 0,85 m/s | Stanley 2018 |
| Pico de velocidade do ombro / do cotovelo | **91 % / 99 %** do movimento | 87 % / 98 % | Stanley 2018 |
| Velocidade angular de pico do ombro / cotovelo | 535 / 400 °/s (as mais baixas dos 6 golpes) | 691 / 561 °/s | Stanley 2018 |
| Duração do golpe (17 pugilistas de elite, 2026) | **667 ± 70 ms** — mais longo do que o golpe da mão da frente | mais curto (valor não visto) | estudo de 2026 ([PubMed](https://pubmed.ncbi.nlm.nih.gov/42106794/), via excertos) |
| Velocidade máxima no ar (16 amadores, acelerómetro) | 7,7 ± 1,5 m/s (homens) | 8,1 ± 1,4 m/s | Kimm & Thiel 2015 ([PDF](https://pub.h-brs.de/frontdoor/deliver/index/docId/1685/file/Kimm_Thiel_2015_Hand_Speed_Measurements.pdf), via excertos) |
| Golpe reto, **só a execução do braço** | ~100 ms (cotovelo de 50–70° a 110–130°) | idem | Filimonov 1985, via tese METU, p. 22 |
| Golpes retos em geral | 357 ± 178 ms | | vários, citados em Stanley 2018 |
| Golpe isolado vs combinação | o golpe isolado de força máxima é mais lento a chegar do que numa combinação "em sincronia" | idem | Piorkowski et al. 2011 ([ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics), via excertos) |

**Como ler isto.** O direto demora **~90 ms mais do que o jab** (495 vs 405 ms no mesmo estudo), porque antes de o braço sair o pé, a anca e o peito têm de rodar. O braço em si continua a esticar em ~100 ms, e o cotovelo só chega ao pico mesmo no contacto (99 %). Na Stanley o punho do direto é mais rápido do que o do jab; no ar (Kimm & Thiel) é ao contrário — o direto ganha **força**, não necessariamente velocidade.

**Na animação [estimativa]:** golpe inteiro **~500 ms** (bate com os 495 ms da Stanley): arranque e rotação ~110 ms (o corpo mexe-se antes do braço), extensão ~50 ms + impacto parado ~90 ms, regresso ~190 ms (mais longo do que a ida: o direto "é o golpe mais difícil de recuperar", Expert Boxing, [10 Counters](https://expertboxing.com/10-counters-for-the-right-hand)). Como no jab: pouca distância da mão nos primeiros fotogramas, muita no último antes do impacto.

---

## 2. A posição do corpo, fase a fase

### Guarda (ponto de partida e de chegada)

Igual à do jab (ver `pesquisa-jab.md`): pés um pouco mais afastados do que os ombros, na diagonal, **calcanhar de trás levantado**, joelhos ligeiramente dobrados, **peso igual nas duas pernas**, cotovelos em baixo, mãos em cima, queixo um pouco para baixo **[fonte: Expert Boxing, Beginner's Guide]**. **Luva direita à altura do queixo**, ao lado da linha central (tese METU) **[fonte]**. "A luva começa na cara e acaba na cara" **[fonte: Expert Boxing, [How To Punch Harder](https://expertboxing.com/how-to-punch-harder)]**.

### Arranque (pé e anca)

- **Pé de trás:** roda na **ponta (bola do pé)**, com o calcanhar a subir e a rodar **para fora** — "como se esmagasses amendoins" **[fonte: Expert Boxing, [One-Two](https://expertboxing.com/how-to-throw-a-one-two-punch-combination)]**; "roda o pé de trás, a rodar na bola do pé" **[fonte: Precision Striking, via excertos]** ([How to Throw the Cross](https://precisionstriking.com/how-to-throw-the-cross/)). **Quantos graus:** Expert Boxing diz "**cerca de 90°**"; outros guias dizem **~45°** ou "45 a 90°" **[fonte]**. Como na guarda o pé de trás já está a ~45° (Expert Boxing), o mais coerente é: **o pé roda ~45° até apontar para o adversário** (e até ~90° num direto de força máxima) **[estimativa]**. O calcanhar faz um arco de ~0,07 H para fora e para trás **[estimativa por geometria: pé ~0,10 H do calcanhar à bola, rodado 45°]**.
- **Porquê:** "rodar o calcanhar dá força porque roda as ancas e deixa a barriga da perna empurrar; **é a rotação da anca que mais acrescenta**" **[fonte: Expert Boxing, One-Two]**. "O pé roda **para dentro do chão**, não para fora dele" **[fonte: Expert Boxing, [2-Legged Punching](https://expertboxing.com/power-punching-secrets-part-1-2-legged-punching)]**.
- **Joelho de trás:** roda para dentro e **baixa**, a apontar para o chão ("sentar no golpe"; o nível baixa um pouco) **[fonte: Dynamic Striking, via excertos]** ([Mastering the Right Cross](https://dynamicstriking.com/blogs/news/cross-boxing)); "roda o joelho de trás, a anca e o tronco com o golpe" **[fonte: Sweet Science of Fighting, via excertos]**. Expert Boxing: "dobra os joelhos quando atiras a direita — 'deixa cair a direita nele'" **[fonte: One-Two]**.
- **Mão:** **não puxar a mão atrás** antes de sair ("telegrafar") **[fonte: Expert Boxing, [Basic Boxing Punches](https://expertboxing.com/basic-boxing-punches), How To Punch Harder; Precision Striking]**. A pequena "carga" que existe é **da anca, não da mão**: a pelvis já roda para a frente enquanto o peito ainda não acompanhou (Cabral 2010) **[fonte]**.

### Rotação

- **Perna de trás empurra, perna da frente trava.** Stanley 2018: no direto as duas pernas fazem picos de força parecidos (**trás 1,21 N/kg, frente 1,06 N/kg** — no jab eram 1,56 e 0,63); a perna de trás empurra **2,3× mais** do que no jab (impulso 66,6 vs 29,2) e a da frente **trava 6× mais** (−62,5 vs −10,1) **[fonte]**. Os autores (citando Cheraghi 2014 e Turner 2011): "manter a **perna da frente rígida**" ajuda a passar a força das pernas para o braço **[fonte]**. Boxing News: "o lado da frente do corpo funciona como **dobradiça**" **[fonte, via excertos]** ([Fight School: The Cross](https://boxingnewsonline.net/fight-school-the-cross/)).
- **Contribuições (Filimonov 1985, citado):** extensão da perna de trás **38 %**, rotação do tronco **37 %**, extensão do braço **24 %** da força do golpe **[fonte, via Lincoln SAS blog]**.
- **Quanto roda o tronco:** num estudo de 2026 com 17 pugilistas de elite, a **amplitude de rotação do tronco** foi **73 ± 8°** no direto e 43 ± 8° no golpe reto da mão da frente (medida no referencial do laboratório) **[fonte, via excertos]** ([Springer](https://link.springer.com/article/10.1186/s13102-026-01738-1)). **Nenhuma fonte acessível dá a rotação da pelvis em graus.** Expert Boxing: "o tronco deve rodar **o mais possível**"; "uma rotação completa com o braço pouco esticado bate mais do que uma rotação pequena com o braço todo esticado" **[fonte: How To Punch Harder]**.
- **Para o esqueleto [estimativa]:** **ancas ~−45°** e **peito ~−60°** em relação à guarda (o peito roda mais do que a anca e acaba depois dela). **O motor limita a ±20°: o direto real passa disso cerca de 3 vezes no peito (~40° a mais) e ~2 vezes na anca (~25° a mais).** Com ±20° o direto fica com aspeto de "só braço" (erro n.º 6 da secção 4). Proposta: subir o limite para **±65° no peito e ±50° nas ancas**, ou pelo menos ±60°/±45°.
- **Peso:** há duas escolas. Os principiantes aprendem a "passar o peso todo para a frente"; o Expert Boxing chama-lhe "**socar numa perna só**" e diz que é errado: o corpo deve ficar **entre as duas pernas, a rodar** ("uma perna empurra, a outra puxa") **[fonte: 2-Legged Punching]**. Mas os estudos mostram que **algum peso vai para a frente**: no direto a força na perna da frente sobe enquanto a de trás desce (Tong-Iam 2017) e a travagem da frente é grande (Stanley) **[fonte]**; o Dynamic Striking diz "passa o peso para o pé da frente" **[fonte]**. Limite claro de todos: **a cabeça não passa o joelho da frente** **[fonte: Expert Boxing]**. **Para a animação [estimativa]: de 50 % na guarda a ~60 % à frente no impacto**, nunca mais.
- **Pelvis:** avança um pouco e **baixa um pouco** — "o peso desce enquanto o punho vai para a frente"; "dobra os joelhos ou baixa a cada golpe? Sim, ligeiramente" **[fonte: Expert Boxing, comentários de [How to Throw a Straight Punch](https://expertboxing.com/how-to-throw-a-straight-punch)]**; "ir para baixo e para dentro, não para cima e para fora" **[fonte: Expert Boxing, [Implosive Punching](https://expertboxing.com/power-punching-secrets-part-2-implosive-punching)]**. Valores: avança ~0,03 H (≈5 cm), baixa ~0,013 H (≈2 cm), desvia-se ~0,01 H para a esquerda (roda à volta da perna da frente) **[estimativa]**.

### Extensão

- **Braço:** sai **a direito do queixo** para o alvo; "nunca um golpe largo" **[fonte: Expert Boxing]**. "Estica o **lado de dentro** do braço (peito/bíceps) e chega com os **nós dos dedos grandes**", senão o direto curva para dentro **[fonte: How to Throw a Straight Punch]**.
- **Cotovelo:** fica **em baixo e atrás do punho** enquanto o braço estica; só no fim, com a rotação do punho, sai um pouco para fora. "Mau: abrir o cotovelo **antes** de esticar. Bom: abrir **depois** de esticar" **[fonte: Expert Boxing, [Mailbag](https://expertboxing.com/how-do-you-punch-straight-with-the-back-hand)]**.
- **Punho:** roda durante a extensão até **palma para baixo** no impacto **[fonte: Expert Boxing; Boxing News: "palma para baixo e polegar para dentro"]**. "Não rodes demais o punho até a palma ficar virada para fora" **[fonte: Expert Boxing, comentários do One-Two]**.
- **Altura:** "aponta um pouco **acima da linha dos olhos** e dobra um pouco os joelhos para compensar" **[fonte: Expert Boxing, comentários do One-Two]**. Para um adversário da mesma altura: a mão bate à altura do queixo/olhos dele, um pouco acima do próprio ombro **[estimativa]**.
- **Ombro direito:** "deixa o ombro direito vir para a frente e roda a parte de cima do tronco para dentro do golpe" **[fonte: Expert Boxing, comentários do One-Two]**; "tenta subir os ombros durante o golpe" **[fonte: How To Punch Harder]**.

### Impacto

- **Ombro de trás e queixo:** "o ombro de trás vem para a frente e **acaba a tocar no lado de fora do queixo**" **[fonte: [Wikipedia](https://en.wikipedia.org/wiki/Cross_(boxing))]**; "o queixo um pouco para baixo, **tapado em parte pelo ombro do braço que bate**" **[fonte: Expert Boxing, How To Punch Harder]**. Ou seja: **sim, o ombro direito chega à linha do queixo** e o queixo fica **atrás/por dentro do ombro direito**.
- **Cabeça:** sai **um pouco da linha central** — "baixa a cabeça UM POUCO para a frente e **para a esquerda**, para a tirar do caminho" **[fonte: Expert Boxing, Basic Boxing Punches]** — mas **sem passar o joelho da frente** **[fonte: Beginner's Guide]**. Olhos sempre no alvo **[fonte: One-Two]**. Não rodar a cabeça com o golpe **[fonte: How to Throw a Straight Punch]**.
- **Tronco:** "**não te inclines** para a frente; não tentes chegar lá, **roda**" **[fonte: How To Punch Harder]**; inclinar demais faz abrir o cotovelo (golpe "por cima") **[fonte: Mailbag]**. Inclinação pequena: ~6° para a frente e ~6° para a esquerda **[estimativa]**.
- **Cotovelo:** como no jab, o golpe toca **antes de o braço estar todo esticado** (110–130°; Filimonov) **[fonte]**; os pugilistas mais altos da Stanley tocaram no alvo antes da extensão completa **[fonte]**. "O golpe mais forte não chega com o braço todo esticado. Não estiques demais" **[fonte: How To Punch Harder]**.
- **Punho fecha** no impacto e o corpo contrai só nesse instante; expira-se com força **[fonte: Expert Boxing, Beginner's Guide]**.
- **Pernas:** perna da frente firme (trava), joelho de trás para dentro e para baixo, calcanhar de trás no ar, pé de trás a apontar para o adversário **[fonte: Stanley, Dynamic Striking, Expert Boxing]**. Os pés **não saem do chão** **[fonte: How To Punch Harder]**.
- **Mão da frente:** "o braço esquerdo **aproxima-se da cara** para defender da direita do adversário" **[fonte: Expert Boxing, Basic Boxing Punches]**; "a mão que não bate defende o outro lado" **[fonte: Beginner's Guide]**. **Cotovelo da frente** em baixo, junto às costelas **[estimativa coerente com "cotovelos em baixo" da guarda]**.

### Regresso

- "Recupera a mão direita **depressa** para não seres apanhado no counter" **[fonte: Expert Boxing, Basic Boxing Punches]**; pelo mesmo caminho, a direito, até ao queixo **[fonte: Boxing News, Precision Striking]**. Ancas, peito e pé de trás voltam à guarda; o calcanhar de trás fica levantado.
- O direto é "o golpe mais difícil de recuperar": vai com muito peso e a direito **[fonte: Expert Boxing, 10 Counters]** → regresso um pouco mais lento do que a ida **[estimativa]**.

---

## 3. Variantes

- **Direto parado à cabeça (básico):** o descrito acima. **É a animação principal**: começa e acaba no mesmo sítio, é o "2" das fontes e é o que mais se distingue do jab (rotação do corpo e pivô).
- **Direto ao corpo:** "dobra os joelhos e a cintura" **[fonte: Expert Boxing]**; Boxing News: o joelho da frente dobra até ~90°, os ombros alinham com o alvo, **o tronco fica direito** e o punho bate com a palma para baixo **[fonte, via excertos]**. Para a animação: pelvis a baixar ~0,06–0,08 H e pulso com "cima" negativo **[estimativa]**.
- **1-2 (jab-direto):** "jab com um pequeno passo do pé da frente → o pé de trás desliza → direita a rodar ombros, ancas e pé de trás"; **a direita sai enquanto o jab ainda está a voltar** ("ir ao encontro do jab") **[fonte: Expert Boxing, One-Two]**. Um jab sem rotação deixa o direto sair mais depressa **[fonte: How to Throw a Straight Punch]**.
- **Cross-counter (troca de direitas):** responder à direita dele com a tua, **baixando um pouco a cabeça** ao entrar; contar com timing e velocidade, não com força **[fonte: Expert Boxing, 10 Counters, counter #4]**. Por cima do jab dele, a cabeça sai para a esquerda **[estimativa coerente com Basic Boxing Punches]**.
- **Overhand:** o cotovelo dobra para fazer um pequeno arco por cima da guarda **[fonte: Expert Boxing, Beginner's Guide]** (já existe no jogo como golpe próprio).

---

## 4. Erros que fazem o direto parecer errado (evitar na animação)

1. **Pé de trás parado / calcanhar no chão** — sem pivô não há rotação da anca **[fonte: Expert Boxing; guias via excertos]**.
2. **Cair para a frente / socar numa perna só** — o peso todo à frente, a cabeça a passar o joelho da frente **[fonte: Expert Boxing, Beginner's Guide e 2-Legged Punching; Precision Striking]**.
3. **Baixar a mão da frente** — fica aberto à direita do adversário **[fonte: Expert Boxing, Basic Boxing Punches; Precision Striking]**.
4. **Abrir o cotovelo** antes de esticar (golpe em arco, "chicken wing") — muitas vezes por se inclinar demais ou por estar de lado demais **[fonte: Expert Boxing, Mailbag]**.
5. **Telegrafar** — puxar a mão atrás ou baixá-la antes de sair. Os bons counter-punchers batem com o gancho de esquerda "quando a mão dele sai do queixo" **[fonte: Expert Boxing, 10 Counters e Basic Boxing Punches; Precision Striking]**.
6. **Rodar só o braço** — "o braço acaba o golpe antes de o corpo ter começado a rodar" **[fonte: Expert Boxing, How To Punch Harder]**. Na animação: o peito parado (ou limitado a 20°) e só o braço a sair.

Outros:
7. **Esticar demais** (o braço para lá do comprimento real; risco de hiperextensão) **[fonte: Expert Boxing]**.
8. **Rodar demais o punho** (palma para fora) **[fonte: Expert Boxing]**.
9. **Não voltar à guarda** ou voltar devagar e com a mão baixa **[fonte: Precision Striking, Expert Boxing]**.
10. **Subir com o golpe** (esticar as pernas) — o certo é baixar um pouco **[fonte: Expert Boxing]**.
11. **[estimativa]** Tudo a rodar ao mesmo tempo e à mesma velocidade: perde-se a ordem pé → anca → peito → braço que faz o direto "ler-se" como um golpe de corpo.

---

## 5. Comparação rápida com o jab

| | Jab | Direto |
|---|---|---|
| Tempo total (Stanley) | 405 ms | 495 ms |
| Quem trabalha | braço e ombro | pé, anca, tronco, depois braço |
| Ancas / peito (relativos à guarda) | +3° / +10° | **−45° / −60°** [estimativa] |
| Pé de trás | parado, calcanhar levantado | **roda ~45° na ponta**, calcanhar para fora |
| Peso à frente | 50 % constante | 50 → ~60 % |
| Pelvis | quase parada (1 cm) | avança ~5 cm, baixa ~2 cm |
| Perna da frente | quase não trava | trava muito (rígida) |
| Ombro que tapa o queixo | o da frente (sobe) | o de trás (vem para a frente) |
| Cabeça | atrás do ombro da frente | um pouco para a frente e para a esquerda, atrás do ombro direito |
| Regresso | a direito, rápido | a direito, um pouco mais lento |

---

## 6. Tabela fotograma a fotograma — direto básico (parado, à cabeça), 8 fotogramas

### Convenções (iguais às do jab)

- **H** = altura do corpo. **L** = comprimento do braço (ombro → pulso).
- **Pelvis** (dx, dz, dy) em fração de H, relativa à guarda: dx + = para a **direita** do pugilista, dz + = para a **frente**, dy + = para **cima**.
- **Ancas / peito:** graus à volta do eixo vertical, **relativos à guarda**; **+ = o lado esquerdo vai para a frente** (jab). **O direto é negativo** (o lado direito vai para a frente).
- **Tronco:** inclinação além da guarda. Frente + = para o adversário; lado + = para a direita (o ombro esquerdo sobe). **No direto o lado é negativo** (inclina para a esquerda, o ombro direito sobe para o queixo).
- **Cabeça:** rotação relativa ao peito (+ aqui contraria o peito, para os olhos ficarem no alvo); inclinação + = queixo para baixo.
- **Pulsos:** (frente, dentro, cima) em fração de L, **relativos ao ombro do mesmo lado**, com os eixos da guarda (frente = para o adversário). Atenção: no direto **o próprio ombro direito avança ~0,11 H** com a rotação do peito **[estimativa por geometria: meia largura de ombros 0,11 H, peito em guarda ~35° de lado]**, por isso a mão chega muito mais longe do que os números do pulso sozinhos sugerem.
- **Punho:** rotação do antebraço; **0° = palma virada para a cara** (guarda), **90° = palma para baixo**.
- **Pés**, relativos à pelvis da guarda, em fração de H: **frente (−0,11; +0,09)**, **trás (+0,11; −0,06)** (dx; dz), como no jab. **Rotação do pé de trás**: graus à volta da ponta do pé, relativos à guarda (− = a ponta roda para o adversário, o calcanhar para fora). **Calcanhar**: deslocação (dx; dz) do calcanhar em relação à guarda, a ponta fica no sítio.

### Tabela A — corpo

| F | Fase | ms | Pelvis dx / dz / dy (×H) | Ancas | Peito | Tronco frente / lado | Cabeça rot. / incl. | Peso frente | Pernas |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 50 % | joelhos dobrados ~15–20°, calc. trás levantado |
| 1 | Arranque | 60 | −0,002 / +0,005 / −0,004 | −10° | −4° | +1° / −1° | +4° / +2° | 52 % | calc. trás sobe e começa a rodar para fora; joelho de trás começa a rodar para dentro |
| 2 | Rotação | 50 | −0,005 / +0,015 / −0,008 | −28° | −22° | +3° / −3° | +18° / +4° | 55 % | perna de trás empurra; perna da frente começa a travar |
| 3 | Extensão | 50 | −0,008 / +0,025 / −0,011 | −40° | −45° | +5° / −5° | +38° / +6° | 58 % | joelho de trás para dentro e para baixo |
| 4 | **Impacto** | 90 | **−0,010 / +0,030 / −0,013** | **−45°** | **−60°** | **+6° / −6°** | **+50° / +8°** | **60 %** | perna da frente firme; joelho de trás a apontar para o chão; ancas ~2 cm mais baixas; cabeça atrás do joelho da frente |
| 5 | Regresso 1 | 60 | −0,007 / +0,020 / −0,009 | −32° | −40° | +4° / −4° | +34° / +5° | 56 % | |
| 6 | Regresso 2 | 70 | −0,003 / +0,008 / −0,004 | −14° | −16° | +2° / −2° | +13° / +2° | 52 % | |
| 7 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 50 % | = F0 |

### Tabela B — braços e pés

| F | Pulso trás (f / d / c ×L) | Punho trás | Cotovelo trás | Pulso frente (f / d / c ×L) | Cotovelo frente | Pé de trás: rotação | Calcanhar de trás dx / dz (×H) |
|---|---|---|---|---|---|---|---|
| 0 | 0,30 / 0,25 / 0,15 | 0° | para baixo, junto às costelas | 0,40 / 0,05 / 0,25 | para baixo | 0° | 0 / 0 (levantado ~0,02 H) |
| 1 | 0,34 / 0,25 / 0,14 | 5° | para baixo, a ir para a frente (a mão não recua) | 0,40 / 0,08 / 0,25 | para baixo, junto às costelas | −10° | +0,015 / −0,005 |
| 2 | 0,48 / 0,27 / 0,12 | 25° | para baixo, atrás do punho | 0,42 / 0,12 / 0,25 | para baixo | −28° | +0,045 / −0,015 |
| 3 | 0,68 / 0,29 / 0,10 | 55° | atrás do punho, a começar a rodar para fora | 0,43 / 0,14 / 0,26 | para baixo | −40° | +0,065 / −0,025 |
| 4 | **0,80 / 0,30 / 0,10** (≈0,86 L do ombro; cotovelo ~120°) | **90°** | para fora (horizontal), braço quase reto | **0,44 / 0,15 / 0,26** (luva junto à cara, à esquerda do queixo) | para baixo, a tapar as costelas | **−45°** (ponta para o adversário) | **+0,070 / −0,030** (~0,04 H no ar) |
| 5 | 0,58 / 0,28 / 0,12 | 55° | a voltar para baixo | 0,43 / 0,12 / 0,26 | para baixo | −32° | +0,050 / −0,020 |
| 6 | 0,40 / 0,26 / 0,14 | 20° | para baixo | 0,41 / 0,08 / 0,25 | para baixo | −14° | +0,020 / −0,008 |
| 7 | 0,30 / 0,25 / 0,15 | 0° | para baixo, junto às costelas | 0,40 / 0,05 / 0,25 | para baixo | 0° | 0 / 0 |

Total ~500 ms; ida F1–F3 = 160 ms (o braço estica sobretudo em F2–F4, ~100 ms); regresso F5–F7 = 190 ms. Em loop, o F7 é igual ao F0. O pé da frente não mexe (direto parado).

### O que é fonte e o que é estimativa na tabela

- **Das fontes:**
  - **Tempos:** total ~495 ms (Stanley); o braço estica em ~100 ms (Filimonov); ombro antes do cotovelo e cotovelo no pico mesmo no contacto (91 % / 99 %); a rotação do tronco atinge o máximo no impacto (Tong-Iam).
  - **Ordem:** pé → joelho → anca → ombro → cotovelo (Cheraghi); a pelvis começa a rodar antes do tronco (Cabral) — por isso em F1–F2 as **ancas vão à frente do peito** e em F3–F4 o peito passa as ancas.
  - **Pés e pernas:** pivô na ponta do pé de trás, calcanhar para fora, pé "cerca de 90°" (Expert Boxing) ou ~45° (outros); joelho de trás para dentro e para baixo (Dynamic Striking); perna da frente rígida a travar (Stanley, Turner, Cheraghi); dobrar os joelhos / baixar ligeiramente (Expert Boxing).
  - **Peso:** vai um pouco para a frente (Stanley, Tong-Iam, Dynamic Striking) sem a cabeça passar o joelho da frente (Expert Boxing).
  - **Tronco:** roda muito (73° de amplitude no estudo de 2026) e não se inclina para a frente (Expert Boxing).
  - **Braço:** sai do queixo a direito, sem recuar; cotovelo em baixo e só abre depois de esticar; punho de palma para a cara a palma para baixo; toca antes da extensão completa (110–130°).
  - **Cabeça e ombro:** ombro direito a tocar o lado de fora do queixo (Wikipedia, Expert Boxing); cabeça um pouco para a frente e para a esquerda (Expert Boxing).
  - **Mão da frente:** fica na cara e aproxima-se dela (Expert Boxing).
- **Estimativas minhas (números):**
  - Os graus exatos de ancas (−45°) e peito (−60°) — escolhidos a partir dos 73° de amplitude do tronco e do pivô de ~45–90° do pé; nenhuma fonte acessível dá a pelvis em graus.
  - As deslocações da pelvis (0,03 H para a frente, 0,013 H para baixo, 0,01 H para a esquerda), as inclinações do tronco (6°/6°), a rotação da cabeça e os 60 % de peso à frente.
  - As frações de L dos pulsos (calculadas por geometria para o cotovelo a ~120° e a mão a acabar na linha central) e o arco do calcanhar.
  - A divisão dos milissegundos por fotograma.

### Dicas para o boneco de 40×60 px

- Ao contrário do jab, aqui **o corpo tem de se ver a rodar**: com H = 60 px, o ombro direito avança ~6–7 px, o calcanhar de trás sai ~4 px para fora, a pelvis avança ~2 px e baixa ~1 px. É isto que distingue o "2" do "1".
- Ordem que se tem de ler: **F1 calcanhar e anca → F2 peito → F3–F4 braço**. Se tudo começar no mesmo fotograma parece um empurrão de braço.
- No impacto: **ombro direito a tapar o queixo**, cabeça ligeiramente à esquerda e para a frente, **luva esquerda colada à cara**, calcanhar de trás no ar. Estes quatro sinais valem mais do que o braço esticado.
- Se o motor ficar limitado a ±20°, a opção menos má é pôr os 20° todos no peito e compensar com o ombro a avançar e o tronco a inclinar −8° para a esquerda — mas vai parecer "rodar só o braço". **Recomendo subir o limite** (peito ±65°, ancas ±50°).

### Direto ao corpo (para depois)

Igual, mais **[fonte: Expert Boxing, Boxing News; valores: estimativa]**: pelvis a baixar até ~−0,07 H em F2–F4 (joelho da frente a ~90°), tronco direito (inclinação para a frente ≤ 10°), pulso de trás com "cima" ~−0,35 L no impacto, cabeça a olhar para o alvo sem baixar o queixo para o chão.

### 1-2 (para depois)

O jab do `pesquisa-jab.md` com passo pequeno, e **o direto a começar (F1 deste) quando o jab está em "Regresso 1"** — a mão direita sai enquanto a esquerda volta **[fonte: Expert Boxing, One-Two]**. O pé de trás desliza para a frente (~0,03–0,06 H) entre os dois golpes **[fonte: Expert Boxing; valor: estimativa]**.

---

## Fontes

**Lidas por inteiro:**
- Expert Boxing (Johnny N): [The Beginner's Guide to Boxing](https://expertboxing.com/boxing-basics/how-to-box/the-beginners-guide-to-boxing) (2012), [How to Throw a One-Two](https://expertboxing.com/how-to-throw-a-one-two-punch-combination) (com os comentários do autor), [How to Throw a Straight Punch](https://expertboxing.com/how-to-throw-a-straight-punch) (2012), [How To Punch Harder](https://expertboxing.com/how-to-punch-harder) (2008), [Basic Boxing Punches](https://expertboxing.com/basic-boxing-punches), [7 Basic Punching Tips](https://expertboxing.com/7-basic-punching-tips), [Power Punching Secrets 1: 2-Legged Punching](https://expertboxing.com/power-punching-secrets-part-1-2-legged-punching), [Power Punching Secrets 2: Implosive Punching](https://expertboxing.com/power-punching-secrets-part-2-implosive-punching), [How do you punch straight with the back hand?](https://expertboxing.com/how-do-you-punch-straight-with-the-back-hand), [10 Counters for the Right Hand](https://expertboxing.com/10-counters-for-the-right-hand). Nota: o Expert Boxing não tem um guia só do direto (os endereços `how-to-throw-a-right-cross` e parecidos dão "página não encontrada").
- Stanley, Thomson, Smith & Lamb (2018), IJPAS 18(5): [PDF Chester](https://chesterrep.openrepository.com/server/api/core/bitstreams/3e769a4f-d46b-4921-a2e9-093e0a80e436/content) — Tabelas 2a e 2b e discussão. (O link antigo `…/bitstream/handle/10034/621889/…` agora devolve só a página do repositório; este é o PDF direto.)
- Tese METU (2011): [PDF](https://open.metu.edu.tr/bitstream/handle/11511/21166/index.pdf?sequence=1&isAllowed=y) — definições (p. 11) e revisão de Filimonov 1985 e Donivan 1984 (p. 22–23). Não mede o direto.

**Lidas através de excertos da pesquisa:**
- Cheraghi, Agha Alinejad, Arshi & Shirzad (2014), *Kinematics of Straight Right Punch in Boxing*, Ann Appl Sport Sci 2(2): [ResearchGate](https://www.researchgate.net/publication/281098708_Kinematics_of_Straight_Right_Punch_in_Boxing), [aassjournal](https://aassjournal.com/article-1-136-en.pdf) — 8 pugilistas de elite, captura 3D; os valores de ângulos não apareceram nos excertos.
- Estudo de 2026, *Kinematic and kinetic differences between lead and rear straight punches in elite boxers*, BMC Sports Sci Med Rehabil: [Springer](https://link.springer.com/article/10.1186/s13102-026-01738-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/42106794/) — rotação do tronco 73 ± 8° vs 43 ± 8°, duração 667 ± 70 ms.
- Dinu & Louis (2020), *Biomechanical Analysis of the Cross, Hook, and Uppercut in Junior vs. Elite Boxers*, Frontiers: [Frontiers](https://www.frontiersin.org/articles/10.3389/fspor.2020.598861/full); Dinu, Millot, Slawinski & Louis (2020), Proceedings 49(1): 61 ([DOI](https://doi.org/10.3390/proceedings2020049061)) — só conclusões gerais (a elite bate mais forte e mais depressa; os juniores usam mais o ombro); os números não apareceram.
- Cabral, João, Amado & Veloso (2010), ASB — citado no [Lincoln SAS blog](https://sas.blogs.lincoln.ac.uk/2023/03/07/a-biomechanical-perspective-on-increasing-rear-hand-straight-punch-performance/) (pelvis antes do tronco; contribuições de Filimonov 38/37/24 %).
- Turner, Baker & Miller (2011), *Increasing the impact force of the rear hand punch*, SCJ 33(6): [repositório Middlesex](https://repository.mdx.ac.uk/item/83zw1).
- Tong-Iam, Rachanavy & Lawsirirat (2017), JPES: [PDF](https://efsupit.ro/images/stories/30dec2017/Art%20287.pdf).
- Lenetsky et al. (2020), JSCR: [PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/).
- Piorkowski, Lees & Barton (2011): [ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics).
- Kimm & Thiel (2015), Procedia Engineering: [PDF](https://pub.h-brs.de/frontdoor/deliver/index/docId/1685/file/Kimm_Thiel_2015_Hand_Speed_Measurements.pdf).
- Treinadores irlandeses (Britton et al. 2025), IJPAS: [T&F](https://www.tandfonline.com/doi/full/10.1080/24748668.2025.2481693) — no direto: rodar o pé de trás, rodar as ancas, pronar a mão e subir o ombro para proteger o queixo; o pé da frente assenta quando o punho chega.
- Precision Striking: [How to Throw the Cross](https://precisionstriking.com/how-to-throw-the-cross/), [How to Punch](https://precisionstriking.com/how-to-punch/).
- Boxing News: [Fight School: The Cross](https://boxingnewsonline.net/fight-school-the-cross/).
- Dynamic Striking: [Mastering the Right Cross](https://dynamicstriking.com/blogs/news/cross-boxing).
- Wikipedia: [Cross (boxing)](https://en.wikipedia.org/wiki/Cross_(boxing)).
- Tony Jeffries: vídeo [How to Throw the Perfect Cross](https://www.youtube.com/watch?v=sK-6Ujp3KYY) e resumo na [Men's Health](https://menshealth.com.au/watch-olympic-boxer-tony-jeffries-explain-how-to-throw-the-hardest-punch-in-the-world/) — só ideias gerais ("a força começa nos pés"); os detalhes do vídeo não foram lidos.
- fightTIPS (Shane Fazen): não encontrei material escrito dele sobre o direto.

**Lacunas:** nenhuma fonte acessível dá a **rotação da pelvis em graus** nem a **percentagem de peso** em cada perna durante o direto; os 73° de amplitude do tronco são do estudo de 2026 (lidos em excertos). Os PDFs de Cheraghi 2014 e Dinu 2020 devem ter ângulos do joelho, da anca e do tronco — valia a pena lê-los se a rede deixar.

**Sites bloqueados pela rede da sessão (não contornados):** `frontiersin.org` e `aassjournal.com` (WebFetch e curl), `pmc.ncbi.nlm.nih.gov` e `researchonline.ljmu.ac.uk` (curl, recusados pelo proxy). Depois disto não tentei abrir outros sites; o resto foi lido só por excertos da pesquisa web.
