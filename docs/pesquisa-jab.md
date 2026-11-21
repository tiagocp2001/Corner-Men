# Pesquisa: o jab perfeito (para a animação)

Guarda ortodoxa (pé esquerdo à frente), jab de esquerda à cabeça. Objetivo: animar um boneco de ~40×60 px com um esqueleto 3D (pelvis, rotação de ancas e peito ≤ 20°, inclinação do tronco, cabeça, pulsos, pés, cotovelos).

> **Fontes e marcas.** Li por inteiro: o guia do jab do **Expert Boxing** (Johnny N, *How to Throw a Jab* e *The Ultimate Boxing Jab Guide*) e os guias de guarda dele; o artigo de **Stanley et al. 2018** (PDF completo, com as tabelas); a **tese da METU** (Middle East Technical University, 2011: 30 pugilistas, captura de movimento a 240 Hz). O resto (Boxing News, Precision Striking, Human Kinetics, Tony Jeffries, outros estudos) foi lido através de excertos da pesquisa web. **[fonte]** = dito por uma fonte (com link); **[estimativa]** = valor meu, coerente com as fontes, para a animação.
>
> **O que mudou em relação à primeira versão:** o peso **não** vai para a frente (fica ao centro; a perna de trás empurra); o corpo **quase não roda** (é o braço e o ombro que trabalham); o braço estica em **~100 ms**; a guarda fica com os pés mais juntos de trás para a frente; no impacto o braço pode ainda não estar todo esticado.

---

## 1. Fases e tempos

### Fases

- **Expert Boxing** divide o jab básico em 3 passos (guarda → esticar a luva → rodar o braço), mas avisa que **"na realidade, tudo acontece ao mesmo tempo"**: o braço sai depressa e roda enquanto sai, e a luva chega fechada e rodada no mesmo instante em que se expira com força. Depois **"puxa-se a mão a direito para trás"**. **[fonte]** ([Expert Boxing](https://expertboxing.com/how-to-throw-a-jab))
- **Lenetsky et al. (2020)**: a descrição antiga em duas fases (arranque e execução) **não mostra a rotação da mão (palma para baixo) nem a subida do ombro da frente para tapar o queixo**, que os treinadores consideram essenciais. Nos golpes retos, o empurrão no chão vai **para a frente, para o alvo**. **[fonte]** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/))
- **Stanley 2018** mede do **arranque** (o início de um pequeno contra-movimento: a mão desce um pouco antes de sair) até ao **contacto** (um fotograma antes de tocar no alvo). **[fonte]** ([PDF Chester](https://chesterrep.openrepository.com/bitstream/handle/10034/621889/IJPAS%20(2018).pdf?sequence=1&isAllowed=y))

Para a animação usamos 5 fases: **guarda → arranque → extensão → impacto → regresso**.

### Tempos medidos

| Medida | Valor | Fonte |
|---|---|---|
| Jab, do arranque ao contacto (15 amadores, força máxima contra um alvo) | **405 ± 150 ms**, o mais curto dos 6 golpes (direto 495, ganchos 586–657, uppercuts 606–627 ms) | Stanley 2018, Tabela 2a |
| Velocidade de pico do punho no jab | **5,85 ± 0,85 m/s** (a mais baixa dos 6 golpes; gancho da frente 11,95) | Stanley 2018 |
| Quando o **ombro** atinge a velocidade máxima | aos **87 ± 7 %** do movimento | Stanley 2018 |
| Quando o **cotovelo** atinge a velocidade máxima | aos **98 ± 2 %** — mesmo no contacto | Stanley 2018 |
| Ordem | ombro → cotovelo (o ombro atinge o pico ~12 % antes do cotovelo) | Stanley 2018 |
| Golpe reto, **só a execução** do braço | **~100 ms** em média; a ação toda: elite 446 ms, sem competição 663 ms | Filimonov et al. 1985, citado na tese METU ([PDF](https://open.metu.edu.tr/bitstream/handle/11511/21166/index.pdf?sequence=1&isAllowed=y), p. 21–22) |
| Golpes retos em geral | 357 ± 178 ms | vários estudos citados em Stanley 2018 |
| Jab isolado com força máxima | 587 ± 166 ms (em combinação são mais rápidos) | Piorkowski et al. 2011, citado ([ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics)) |
| Ida vs regresso (gesto de treino) | ida 46 %, regresso 54 % — o regresso é um pouco mais longo | estudo de 2025 ([sportpedagogy](https://sportpedagogy.org.ua/index.php/ppcs/article/view/3486)) |

**Como ler isto.** Os ~400 ms contam desde o primeiro movimento de preparação, num golpe de força máxima; a parte em que **o braço realmente estica é curta, ~100 ms** **[fonte: Filimonov via METU]**. O ombro acelera primeiro e o cotovelo só atinge a velocidade máxima mesmo no contacto, ou seja, **a mão acelera até ao fim** **[fonte: Stanley]**.

**Na animação [estimativa]:** golpe inteiro **~400 ms** (bate com os 405 ms do Stanley): extensão em ~100 ms (3 fotogramas curtos), impacto parado ~80 ms para se ler, regresso ~170 ms (um pouco mais longo do que a ida). Não pôr a mão a andar a velocidade igual: pouca distância no 1.º fotograma da ida, muita no último.

---

## 2. A posição do corpo, fase a fase

### Guarda (ponto de partida e de chegada)

- **Expert Boxing:** "mãos em cima, cotovelos para dentro, **ancas entre os pés**, joelhos ligeiramente dobrados e **calcanhar de trás levantado**. Pé da frente ligeiramente em ângulo, apontado para o adversário; pé de trás a **~45°** na diagonal." Corpo e mãos descontraídos. Pés **"mais ou menos à largura dos ombros"**. **[fonte]** ([guia do jab](https://expertboxing.com/how-to-throw-a-jab), [largura da guarda](https://expertboxing.com/perfect-boxing-stance-width))
- **Tese METU (definição usada no estudo):** pés à largura dos ombros; o pé esquerdo **15–20 cm à frente** e o de trás **~10 cm atrás** do plano do tronco; **mão esquerda à altura da cabeça**, **luva direita à altura do queixo**, as duas **ao lado da linha central** do corpo. **[fonte]** Para uma pessoa de 1,78 m: afastamento de trás para a frente ~25–30 cm ≈ **0,15 H**; de lado ≈ largura dos ombros ≈ **0,22 H**.
- **Peso:** ancas ao meio = **50/50** **[fonte: Expert Boxing]**.
- **Mão da frente:** Expert Boxing diz que o jab "começa com a **palma virada para ti**" **[fonte]**.
- **Não "carregar" o jab:** "não puxes a mão da frente para ti nem baixes as ancas para preparar" **[fonte: Expert Boxing]**. (No laboratório viu-se um pequeno contra-movimento da mão, mas o Expert Boxing e a Boxing News dizem que denuncia o golpe: **não o animar**.)

### Arranque

- **Expert Boxing:** "**NADA MAIS SE MEXE.** Mexe só o braço da frente. **Não passes o peso para a frente nem para trás, mantém o peso ao centro.**" **[fonte]**
- **Stanley 2018:** no jab a **perna de trás faz ~71 % da força no chão**, mais do que em qualquer outro golpe (pico: perna de trás 1,56 N/kg, perna da frente 0,63 N/kg); a travagem na perna da frente é **muito pequena** (oito vezes menor do que no gancho de trás). A perna de trás "empurra o punho ao longo do eixo frente-trás"; o jab "depende menos da rotação do tronco". **[fonte]**
- Ou seja: **a perna de trás empurra, mas o peso não passa para a frente** e o corpo não avança de forma visível. A primeira versão deste relatório (peso 60/40 à frente) estava errada.
- A mão sai **diretamente**, sem recuar nem baixar antes **[fonte: Expert Boxing, Boxing News]**.

### Extensão

- **Braço:** sai descontraído e rápido, "como um chicote", com os nós dos dedos à frente. Fechar o punho cedo torna o golpe mais lento **[fonte: Expert Boxing]**. Vai **em linha reta, do ombro** **[fonte: Boxing News]** ([Fight School](https://boxingnewsonline.net/features/fight-school-the-jab/)). Tese METU: o jab é "um golpe curto e reto, feito a **esticar o cotovelo com a rotação do ombro**"; ganchos e uppercuts usam o tronco todo, o jab não **[fonte]**.
- **Cotovelo:** "traz o cotovelo **a direito, para a frente**, por trás do jab, e não para o lado"; o cotovelo para o lado ("chicken wing") é mais fraco, denuncia o golpe e é menos direto **[fonte: Expert Boxing]**.
- **Rotação do braço:** "**enquanto a luva estica**, roda o braço da frente todo — ombro, cotovelo, punho — de maneira a que o golpe chegue **com a palma para baixo e o ombro rodado para cima a tapar o queixo**" **[fonte: Expert Boxing]**. Outras fontes: rotação no último terço do caminho (Precision Striking) ou a meio (Human Kinetics) **[fonte]**. Para a animação: a rotação acontece **ao longo da extensão**, a acabar no impacto.
- **Ancas e tronco:** "Não rodes o pé nem o corpo: **isso já não é um jab**, é um 'direto de esquerda'"; "num jab bem feito **o corpo não roda**" **[fonte: Expert Boxing]**. Outros guias falam de "uma pequena rotação de anca" e de um "quarto de volta" do ombro da frente (Boxing News, Papazoglou) **[fonte]**. **Nenhuma fonte dá graus.** Na tese METU, num jab de **força máxima** contra saco, o ombro da frente deslocou-se **~20 cm (principiantes) a ~33 cm (elite)** e o pulso **~70–80 cm** **[fonte: Fig. 14 e 16]**: num golpe de força máxima, o tronco e o ombro também viajam bastante (é mais um "power jab"). O jab rápido, que é o da animação principal, usa muito menos.

### Impacto

- **Ombro da frente levantado** a tapar o queixo; dá mais alcance e protege dos counters por cima. Não levantar o ombro é "erro de amador" **[fonte: Expert Boxing]**.
- **Cabeça atrás do ombro**: "uma regra sábia é manter a cabeça ATRÁS DO OMBRO"; ir com a cabeça à frente tira equilíbrio e força e tira peso do pé de trás **[fonte: Expert Boxing]**.
- **Punho fecha só no instante do impacto** e o corpo contrai "só por uma fração de segundo" **[fonte: Expert Boxing]**; expira-se com força no golpe **[fonte: Expert Boxing, Tony Jeffries]**.
- **Ângulo do cotovelo:** num golpe reto, o cotovelo começa em **50–70°** e chega ao impacto em **110–130°** (Filimonov, via METU) **[fonte]** — o golpe toca **antes de o braço estar todo esticado**. Human Kinetics: "cotovelo macio no contacto" **[fonte]**. Com esses ângulos, o pulso fica a **~0,85–0,9 L** do ombro no contacto **[estimativa por geometria]**; no fim (se não tocar em nada) pode ir até ~0,95 L.
- **Pernas:** não esticar ("popping up"): ficar em baixo ou até "baixar um pouco (uma polegada)" dá mais força e equilíbrio **[fonte: Expert Boxing]**. Os grandes pugilistas "baixam ligeiramente as ancas só quando batem" **[fonte: Expert Boxing, guia da guarda]**.
- **Mão de trás junto à cara**; baixá-la deixa-te aberto ao gancho de esquerda e denuncia o direto **[fonte: Expert Boxing]**.
- **Altura:** no estudo da METU o alvo estava **à altura do ombro** do pugilista **[fonte]** — para um adversário da mesma altura, a mão bate um pouco acima da altura do próprio ombro (queixo).

### Regresso

- "Depois de acabar o jab, **puxa-o a direito para trás**" **[fonte: Expert Boxing]**; pelo mesmo caminho até à guarda, sem baixar a mão **[fonte: Boxing News]**. O punho desfaz a rotação e o ombro desce.

---

## 3. Variantes

- **Jab parado (básico):** o descrito acima: só o braço e o ombro se mexem **[fonte: Expert Boxing]**.
- **Step jab:** "dá um passo com o pé da frente (**só umas polegadas**) enquanto bates"; "recupera o **pé de trás** enquanto recuperas o braço". Erro mais comum: passo grande demais (o golpe chega antes de o pé assentar). **[fonte: Expert Boxing]** Algumas polegadas ≈ 5–10 cm ≈ **0,03–0,06 H** **[estimativa]**. Na versão de 2008, Johnny N chamava ao step jab o "jab normal".
- **Back-step jab:** bate a recuar o pé de trás e recupera o da frente com o braço **[fonte: Expert Boxing]**.
- **Power jab:** jab a **baixar ligeiramente as ancas** ("parece uma queda"); a mão chega quando as ancas "travam" a descida; "sente-se, não se vê" **[fonte: Expert Boxing]**. Na versão de 2008: passo + um pouco de rotação do corpo + ângulo **[fonte]**.
- **Body jab:** step jab dobrando **os joelhos e a cintura**, sem se agachar demais nem olhar para o corpo; mais a empurrar do que a estalar **[fonte: Expert Boxing]**.
- **Pivot jab:** jab a rodar o corpo enquanto o pé de trás roda por trás (sentido dos ponteiros do relógio na guarda ortodoxa); erro: rodar demais **[fonte: Expert Boxing]**.
- **Tapper / space-maker / double jab / counter jab:** variações táticas **[fonte: Expert Boxing 2008]**.

**Animação principal:** o **jab parado**. Começa e acaba no mesmo sítio e é exatamente o "jab básico" das fontes. O step jab fica como segunda animação (passo pequeno).

---

## 4. Erros que fazem o jab parecer errado (evitar na animação)

Os 6 erros do Expert Boxing **[fonte]**:
1. **Cotovelo a sair para o lado** (chicken wing).
2. **Baixar a mão de trás.**
3. **Ir com a cabeça à frente** — a cabeça fica atrás do ombro.
4. **Não levantar o ombro da frente.**
5. **Esticar as pernas / subir com o jab** — as pernas ficam dobradas, as ancas não sobem.
6. **Rodar o pé ou o corpo** — isso já é um direto de esquerda, não um jab.

Outros:
7. **Carregar o golpe** (puxar a mão para trás ou baixá-la antes) **[fonte: Expert Boxing, Boxing News]**.
8. **Regresso lento ou com a mão baixa** **[fonte: Boxing News]**.
9. **Passar o peso para a frente** **[fonte: Expert Boxing; Stanley mostra que o jab assenta na perna de trás]**.
10. **[estimativa]** Mão a andar a velocidade constante (perde o "estalo"); braço a esticar para além do comprimento real.

---

## 5. Diferença para o direto (para mais tarde)

- O direto é a mão de trás e é conduzido pelo pé de trás: **calcanhar de trás roda para fora (pivô)**, ancas e ombros rodam **muito** **[fonte]** ([Wikipedia](https://en.wikipedia.org/wiki/Cross_(boxing)), [Dynamic Striking](https://dynamicstriking.com/blogs/news/cross-boxing)).
- **Stanley 2018:** o direto demora 495 ms (jab 405), com o punho mais rápido (6,97 vs 5,85 m/s); a perna da frente trava muito mais (−62,5 vs −10,1 N·s/kg) e as duas pernas fazem forças parecidas (1,06 / 1,21 N/kg), ou seja, **o peso passa para a frente e trava na perna da frente**, ao contrário do jab **[fonte]**.
- Treinadores irlandeses: o direto é como o jab mas **com mais rotação do tronco, do pé e do joelho de trás** **[fonte]** ([T&F 2025](https://www.tandfonline.com/doi/pdf/10.1080/24748668.2025.2481693)).
- Expert Boxing: depois de um jab bem feito (sem rotação), o direto sai mais depressa, porque o corpo não rodou para o lado contrário **[fonte]**.
- **[estimativa]** Ancas ~40–50°, peito ~50–60°: **passa o limite de 20° do esqueleto**. Será preciso subir o limite para o direto.

---

## 6. Tabela fotograma a fotograma — jab básico (parado), 8 fotogramas

### Convenções

- **H** = altura do corpo. **L** = comprimento do braço (ombro → pulso).
- **Pelvis** (dx, dz, dy) em fração de H, relativa à guarda: dx + = para a **direita** do pugilista, dz + = para a **frente**, dy + = para **cima**.
- **Ancas / peito:** graus à volta do eixo vertical, **relativos à guarda**; **+ = o lado esquerdo vai para a frente** (o sentido do jab). O direto seria negativo.
- **Tronco:** inclinação em graus **além** da guarda. Frente + = para o adversário; lado + = para a direita (o ombro esquerdo sobe).
- **Cabeça:** rotação relativa ao peito (− = contraria o peito, para os olhos ficarem no alvo); inclinação + = queixo para baixo.
- **Pulsos:** (frente, dentro, cima) em fração de L, **relativos ao ombro do mesmo lado**; "dentro" = para a linha central.
- **Punho:** rotação do antebraço; **0° = palma virada para a cara** (guarda, Expert Boxing), **90° = palma para baixo**.
- **Pés** (fixos no jab parado), relativos à pelvis, em fração de H: **frente (−0,11; +0,09)**, **trás (+0,11; −0,06)** (dx; dz) — pés à largura dos ombros de lado, ~0,15 H de trás para a frente **[fonte: definição da METU, convertida para H = 1,78 m]**. Pé da frente apontado para o adversário, pé de trás a ~45°, calcanhar de trás levantado **[fonte: Expert Boxing]**.

### Tabela

| F | Fase | ms | Pelvis dx / dz / dy (×H) | Ancas | Peito | Tronco frente / lado | Cabeça rot. / incl. | Pulso frente (f / d / c ×L) | Punho | Cotovelo frente | Pulso trás (f / d / c ×L) | Peso frente | Pernas |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 0,40 / 0,05 / 0,25 | 0° | para baixo | 0,30 / 0,25 / 0,15 | 50 % | joelhos dobrados ~15–20°, calc. trás levantado |
| 1 | Arranque | 30 | 0 / 0 / 0 | +1° | +2° | 0° / +1° | −2° / 0° | 0,50 / 0,06 / 0,22 | 15° | baixo, para a frente | igual | 50 % | perna de trás começa a empurrar |
| 2 | Extensão 1 | 30 | 0 / +0,002 / −0,002 | +2° | +5° | +1° / +2° | −4° / +1° | 0,66 / 0,08 / 0,16 | 40° | para a frente, por baixo do punho | igual | 50 % | |
| 3 | Extensão 2 | 40 | 0 / +0,004 / −0,004 | +3° | +8° | +1° / +3° | −6° / +2° | 0,82 / 0,10 / 0,10 | 70° | para a frente / a rodar para fora | igual | 50 % | |
| 4 | **Impacto** | 80 | 0 / +0,005 / −0,006 | +3° | +10° | +2° / +4° | −8° / +3° | **0,90 / 0,12 / 0,07** | **90°** | para fora (braço quase reto, ~120–150°) | 0,30 / 0,27 / 0,15 | **50 %** | ancas "afundam" ~0,006 H (≈1 cm); sem esticar |
| 5 | Regresso 1 | 50 | 0 / +0,004 / −0,004 | +2° | +7° | +1° / +3° | −5° / +2° | 0,74 / 0,09 / 0,12 | 60° | para a frente | igual | 50 % | |
| 6 | Regresso 2 | 60 | 0 / +0,002 / −0,002 | +1° | +3° | 0° / +1° | −2° / +1° | 0,54 / 0,06 / 0,20 | 25° | para baixo | igual | 50 % | |
| 7 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 0,40 / 0,05 / 0,25 | 0° | para baixo | 0,30 / 0,25 / 0,15 | 50 % | = F0 |

Total ~410 ms; extensão F1–F3 = 100 ms; regresso F5–F7 = 170 ms. Em loop, o F7 é igual ao F0.

### O que é fonte e o que é estimativa na tabela

- **Das fontes:**
  - **Tempos:** total ~405 ms e extensão ~100 ms. A mão acelera até ao fim (ombro no pico aos 87 %, cotovelo aos 98 %) e o regresso é um pouco mais longo do que a ida.
  - **Peso e pés:** o peso fica ao centro (**50 % constante**; Expert Boxing, e Stanley com a perna de trás a fazer 71 % da força e quase nenhuma travagem à frente). Os pés não mexem e o calcanhar de trás fica levantado. A guarda tem os pés à largura dos ombros e ~25–30 cm de trás para a frente (METU).
  - **Corpo:** quase não roda (Expert Boxing "o corpo não roda"; METU "extensão do cotovelo com rotação do ombro"; Stanley "menos dependente do tronco"). As ancas não sobem e podem baixar um pouco. A cabeça fica atrás do ombro.
  - **Braço do jab:** mão da frente à altura da cabeça e mão de trás à altura do queixo, as duas ao lado da linha central (METU). O punho vai da palma para a cara até à palma para baixo, a rodar durante a extensão. O cotovelo vem para a frente, não para o lado. O ombro da frente sobe a tapar o queixo. O braço não está todo esticado no contacto (110–130° no cotovelo; Filimonov) e o alvo fica à altura do ombro.
- **Estimativas minhas (números):**
  - Rotação e inclinação: os graus de rotação (ancas 3°, peito 10° — o peito representa o "ombro a rodar e a subir"; nenhuma fonte dá graus), a inclinação lateral de 4° (para o ombro subir num esqueleto sem omoplata) e a rotação da cabeça.
  - Posições: as frações de L dos pulsos, o afundar de 0,006 H e os 0,005 H de avanço da pelvis (praticamente nada, 1 cm).
  - Tempos: a divisão dos milissegundos por fotograma.

### Dicas para o boneco de 40×60 px

- A esta escala, **o corpo fica praticamente parado** (a pelvis mexe < 1 píxel): o que se lê é **a mão a sair reta e depressa, o ombro da frente a subir, a cabeça a ficar atrás dele e a mão de trás quieta na cara**.
- Se a animação parecer "morta" por o corpo não mexer, a opção mais fiel às fontes é **1 píxel de afundar no impacto** (o "sentar no golpe"), e **não** inclinar ou rodar mais.
- A rotação do punho mal se vê: pode desenhar-se como a luva a ficar mais "achatada" no impacto.

### Variante com passo (para depois)

Igual, mais **[fonte: Expert Boxing; valores: estimativa]**: o pé da frente avança **~0,03–0,06 H** entre F1 e F4 (assenta **antes ou com** o impacto, nunca depois); o pé de trás segue a mesma distância em F5–F7, junto com o braço a voltar; a pelvis avança de vez a mesma distância.

### Power jab (para depois)

Como o básico, mas com as ancas a descer ~0,01–0,015 H durante a extensão, a parar no impacto **[fonte: Expert Boxing; valor: estimativa]**. No golpe de força máxima, o ombro viaja até ~0,19 H (METU, elite) — aí a rotação do peito pode ir aos ~20° **[estimativa]**.

---

## Fontes

**Lidas por inteiro:**
- Expert Boxing (Johnny N): [How to Throw a Jab](https://expertboxing.com/how-to-throw-a-jab) (2012), [The Ultimate Boxing Jab Guide](https://expertboxing.com/the-ultimate-boxing-jab-guide) (2008), [Perfect Boxing Stance Width](https://expertboxing.com/perfect-boxing-stance-width)
- Stanley, Thomson, Smith & Lamb (2018), *An analysis of the three-dimensional kinetics and kinematics of maximal effort punches among amateur boxers*, IJPAS 18(5): [PDF Chester](https://chesterrep.openrepository.com/bitstream/handle/10034/621889/IJPAS%20(2018).pdf?sequence=1&isAllowed=y) — Tabelas 2a e 2b.
- Tese METU (2011), *3D Kinematic Analysis of Three Different Punches in Amateur Boxing*: [PDF](https://open.metu.edu.tr/bitstream/handle/11511/21166/index.pdf?sequence=1&isAllowed=y) — definições (p. 11), revisão de Filimonov 1985 (p. 21–22), Fig. 14–16 (p. 54–56). Nota: a tese diz que os pugilistas bateram "com a mão dominante" (todos destros), o que é ambíguo para o jab; usei só as definições e as ordens de grandeza.

**Lidas através de excertos da pesquisa:**
- Precision Striking: [How to Punch](https://precisionstriking.com/how-to-punch/)
- Boxing News: [Fight School: The Jab](https://boxingnewsonline.net/features/fight-school-the-jab/)
- Human Kinetics (*Total Knockout Fitness*): [How to throw successful jabs](https://canada.humankinetics.com/blogs/excerpt/how-to-throw-successful-jabs)
- Tony Jeffries: [How to throw a jab](https://www.thereadyroom.net/videos/tony-jeffries-how-to-throw-a-jab), [resumo Sanabul](https://sanabulsports.com/blogs/techniques/boxing-basics-how-to-throw-a-jab-sanabul)
- Teddy Atlas (Dynamic Striking): [Fix your jab](https://dynamicstriking.com/blogs/news/fix-your-jab-with-tips-from-teddy-atlas) — pouco detalhe técnico.
- fightTIPS (Shane Fazen): vídeo "5 Common Jab Mistakes" — só o título; o conteúdo não foi lido.
- Dimitris Papazoglou: [The Left Jab (PDF)](http://www.papazoglouboxing.gr/files/pdf/the_left_jab.pdf)
- West Point: [Intramural Boxing Guide](https://www.scribd.com/document/175877216/US-Army-Boxing-West-Point-Trainers-Manual-51p)
- Wikipedia: [Jab](https://en.wikipedia.org/wiki/Jab), [Cross](https://en.wikipedia.org/wiki/Cross_(boxing))
- Lenetsky et al. (2020), JSCR: [PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/)
- Piorkowski, Lees & Barton (2011): [ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics)
- Liu et al. (2022), *Frontiers in Physiology*: [artigo](https://frontiersin.org/articles/10.3389/fphys.2022.1015154/full)
- Jab angular velocity (2025): [sportpedagogy](https://sportpedagogy.org.ua/index.php/ppcs/article/view/3486)
- Treinadores irlandeses (2025), IJPAS: [PDF](https://www.tandfonline.com/doi/pdf/10.1080/24748668.2025.2481693)
- Erros comuns: [Healthy Principles](https://www.healthyprinciples.co.uk/common-jab-mistakes/), [FightCamp](https://blog.joinfightcamp.com/training/6-tips-to-throw-the-perfect-jab/)

**Lacunas:** nenhuma fonte dá **graus de rotação** de ancas/peito no jab. O Stanley 2018 só mede velocidades angulares e a tese METU só mede deslocações. O artigo de Cabral et al. (2010) sobre a rotação do tronco e da pelvis no soco pode ter esses graus, mas não o encontrei disponível.

**Sites bloqueados pela rede da sessão (não contornados):** o WebFetch não conseguiu abrir expertboxing.com nem clok.uclan.ac.uk (cópia do Piorkowski 2011). O Expert Boxing acabou por ser lido com `curl`, já com o acesso autorizado; o clok.uclan.ac.uk não voltei a tentar.
