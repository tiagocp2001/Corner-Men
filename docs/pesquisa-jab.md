# Pesquisa: o jab perfeito (para a animação)

Guarda ortodoxa (pé esquerdo à frente), jab de esquerda à cabeça. Objetivo: animar um boneco de ~40×60 px com um esqueleto 3D (pelvis, rotação de ancas e peito ≤ 20°, inclinação do tronco, cabeça, pulsos, pés, cotovelos).

> **Nota sobre as fontes.** A rede desta sessão não deixou abrir as páginas diretamente (expertboxing.com e os repositórios das universidades deram erro de acesso). Toda a informação veio do motor de pesquisa, que lê as páginas e devolve excertos. Por isso marco sempre o que é **[fonte]** (dito por uma fonte, com link) e o que é **[estimativa]** (valor meu, coerente com as fontes, para a animação). Onde as fontes não dão números (graus de rotação, percentagem de peso), digo-o.

---

## 1. Fases e tempos

### Fases

Os estudos dividem o jab de maneiras diferentes:

- **Lenetsky et al. (2020)** definiram as fases com plataformas de força, EMG e vídeo rápido. Notaram que a descrição antiga em duas fases (arranque e execução) **não mostra duas coisas que os treinadores acham essenciais**: a **rotação da mão (pronação, palma para baixo)** e a **subida do ombro da frente para proteger o queixo no impacto**. Nos golpes retos (jab e direto) a força no chão empurra **para a frente, em direção ao alvo** (nos ganchos é mais para o lado). **[fonte]** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/), [JSCR](https://journals.lww.com/nsca-jscr/fulltext/2020/04000/defining_the_phases_of_boxing_punches__a.22.aspx))
- O estudo com sensores inerciais (*Dynamic inertial analysis of the technical boxing gesture of Jab*, 2022) divide o jab em **três fases seguidas**, a começar pela preparação; a fase de execução e a torção do tronco foram as que mais distinguiram um pugilista menos experiente de um de elite (o menos experiente demora mais na execução). **[fonte]** ([PDF efsupit](http://efsupit.ro/images/stories/martie2022/Art%2083.pdf), [ResearchGate](https://www.researchgate.net/publication/359684836_Dynamic_inertial_analysis_of_the_technical_boxing_gesture_of_Jab))

Para a animação usamos 5 fases: **guarda → arranque → extensão → impacto → regresso**.

### Tempos medidos

| Medida | Valor | Fonte |
|---|---|---|
| Jab, do arranque ao contacto, golpe máximo contra saco (15 amadores) | **405 ms** — o mais curto dos 6 golpes | Stanley et al. 2018 ([Chester](https://chesterrep.openrepository.com/bitstream/handle/10034/621889/IJPAS%20(2018).pdf?sequence=1&isAllowed=y), [T&F](https://www.tandfonline.com/doi/abs/10.1080/24748668.2018.1525651)) |
| Jab isolado com força máxima | **587 ± 166 ms**; direto 553 ± 211 ms; em combinação são mais rápidos | Piorkowski, Lees & Barton 2011, citado noutro artigo ([ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics)) |
| Velocidade da mão no contacto | ~9,3 m/s golpe isolado; 7,5–8,0 m/s em combinação | Piorkowski 2011 |
| Velocidade de pico do jab | elite 7,16 m/s, juniores 6,32 m/s | Liu et al. 2022 ([Frontiers](https://frontiersin.org/articles/10.3389/fphys.2022.1015154/full)) |
| Quando a velocidade do ombro é máxima | aos **87 %** do movimento (ou seja, mesmo antes do contacto) | Stanley 2018 |
| Quando a perna da frente faz mais força no chão | aos **84 %** do movimento (a mais tardia dos golpes) | Stanley 2018 |
| Ida vs regresso (jab de treino, movimento inteiro) | ida 0,84 s (46 %), regresso 0,99 s (54 %) — o regresso é ~10 % mais longo | estudo ucraniano 2025 ([sportpedagogy](https://sportpedagogy.org.ua/index.php/ppcs/article/view/3486)) |
| Direto de um pesado profissional (referência) | 100 ms | Atha et al. 1985, citado |

**Como ler isto.** Os 400–600 ms dos laboratórios contam desde o primeiro movimento do corpo (o empurrão no chão), com força máxima contra um saco; o estudo de 2025 (1,8 s) é um gesto de treino lento e não serve para o tempo. Nenhuma fonte deu o tempo de um jab rápido num combate. **[estimativa]** Um jab rápido de combate: ~120–180 ms a ir, ~150–200 ms a voltar (o regresso um pouco mais longo, como no estudo de 2025). Na animação, o golpe inteiro deve durar **~400–450 ms**, com um fotograma de impacto um pouco mais longo para se ler. Isto bate com o `jab.py` de hoje (440 ms).

**Importante para o ritmo:** a velocidade **acelera até ao fim** (pico aos 84–87 %). O arranque é curto e quase não se vê; a mão percorre mais distância nos últimos fotogramas da ida. Não pôr a mão a andar a velocidade igual.

---

## 2. A posição do corpo, fase a fase

### Guarda (ponto de partida e de chegada)

- **Pés:** à largura dos ombros, joelhos ligeiramente dobrados, queixo para baixo, mãos em cima, olhos no adversário **[fonte: Expert Boxing, via pesquisa]** ([expertboxing](https://expertboxing.com/how-to-throw-a-jab)). Calcanhar de trás **levantado**, apoio na planta do pé de trás; pé da frente apontado para o adversário (ou 10–15° para dentro), pé de trás a ~45° para fora **[fonte: guias de guarda]** ([Honour & Glory](https://www.honourandglory.co.uk/blog/boxing-stance-and-guard)).
- **Peso:** **50/50**, ou um pouco mais atrás (55/45) **[fonte: guias; não é um dado medido]**.
- **Mão da frente:** à altura da cara, à frente; **mão de trás encostada à bochecha/queixo**; cotovelos em baixo, a proteger as costelas **[fonte]**.
- **Tronco:** de lado em relação ao adversário (ombro esquerdo à frente), ligeiramente para a frente.

### Arranque

- O pé de trás **empurra o chão** e as ancas avançam um pouco **[fonte]** ([Fight Encyclopedia](https://fightencyclopedia.com/blog/blog-how-to-throw-a-perfect-jab-biomechanics); Human Kinetics: "pushing off the ball of the foot" — [excerto](https://canada.humankinetics.com/blogs/excerpt/how-to-throw-successful-jabs)). A força do jab começa com a **extensão do joelho de trás, que põe a pelvis a rodar** (estudo de biomecânica citado na pesquisa).
- A mão sai **diretamente**, sem recuar nem baixar antes (baixar a mão primeiro denuncia o golpe e torna o caminho mais longo) **[fonte]** ([guia de erros](https://kostudio.co/blogs/news/how-to-throw-a-jab-in-boxing)).
- Sequência do mais perto do centro para a ponta: pernas → anca → ombro → cotovelo → mão (Stanley 2018: o jab segue esta ordem "proximal-distal") **[fonte]**.

### Extensão

- O braço vai **em linha reta, do ombro**, "como um soco por dentro de um cano" **[fonte: Boxing News]** ([Fight School: The Jab](https://boxingnewsonline.net/features/fight-school-the-jab/)).
- **Cotovelo por baixo/por dentro**, sem abrir para o lado ("chicken wing"); o cotovelo a abrir tira força e velocidade **[fonte]** ([Healthy Principles](https://www.healthyprinciples.co.uk/common-jab-mistakes/), [FightCamp](https://blog.joinfightcamp.com/training/6-tips-to-throw-the-perfect-jab/)).
- **Rotação do punho no último terço** do caminho (o Human Kinetics diz "a meio") até ficar **palma para baixo / polegar para o chão** no fim; a rotação mesmo antes do impacto é o que dá o "estalo" **[fonte]** ([Precision Striking](https://precisionstriking.com/how-to-punch/), Human Kinetics).
- **Ancas e ombros rodam pouco:** "uma pequena rotação de anca adiciona torção sem tornar o jab mais lento"; "o resto do corpo fica quieto, sem rodar demais" **[fonte]** (Expert Boxing; [Fight Encyclopedia](https://fightencyclopedia.com/blog/blog-how-to-throw-a-perfect-jab-biomechanics); Papazoglou: "ligeiro pivô na anca e no ombro" — [PDF](http://www.papazoglouboxing.gr/files/pdf/the_left_jab.pdf)). Boxing News: o pé da frente pressiona o chão, a anca vira e o **ombro da frente completa "um quarto de volta"** (dito como imagem, não em graus) **[fonte]**. Os treinadores irlandeses descrevem o jab com **menos flexão do pé e do joelho de trás e menos rotação das ancas do que o direto** **[fonte]** ([T&F 2025](https://www.tandfonline.com/doi/pdf/10.1080/24748668.2025.2481693)). **Nenhuma fonte dá graus.**

### Impacto

- **Braço quase esticado**, cotovelo "macio" no contacto (não trancado) **[fonte: Human Kinetics]**. O manual de West Point diz que o braço estica todo, com o cotovelo como uma dobradiça, e palma para baixo **[fonte]** ([West Point](https://www.scribd.com/document/175877216/US-Army-Boxing-West-Point-Trainers-Manual-51p)). Para a animação: ~95 % do comprimento do braço.
- **Ombro da frente sobe** e tapa o queixo (defesa contra o direto do adversário) **[fonte: Expert Boxing, Precision Striking, Lenetsky]**.
- **Cabeça:** queixo em baixo, **atrás do ombro da frente**, sem inclinar para a frente (inclinar deixa a cabeça exposta) **[fonte: Expert Boxing]**.
- **Mão de trás colada à bochecha**; baixá-la é o erro clássico (fica aberto ao direto) **[fonte]**.
- **Peso:** passa para a frente — "o peso passa firmemente para o pé da frente" (um guia) ou "fica centrado" (Expert Boxing) **[fonte, em desacordo]**. No laboratório, o jab foi o **único golpe com diferença clara entre a força das duas pernas** e o que tem **menos força na perna da frente** (Stanley 2018) — ou seja, a perna de trás empurra e a da frente trava pouco. **[estimativa]** 50/50 → ~60/40 (frente) no impacto.
- Expira no golpe **[fonte: Tony Jeffries]** ([Sanabul](https://sanabulsports.com/blogs/techniques/boxing-basics-how-to-throw-a-jab-sanabul)).

### Regresso

- A mão volta **pelo mesmo caminho**, depressa, até à guarda, para proteger o queixo **[fonte]**. O Tony Jeffries põe a "posição de regresso" entre as 4 qualidades do jab (velocidade, força, precisão, regresso) **[fonte]** ([The Ready Room](https://www.thereadyroom.net/videos/tony-jeffries-how-to-throw-a-jab)).
- O punho desfaz a rotação, o ombro desce, o peso volta ao centro.

---

## 3. Variantes

- **Jab parado:** sem mexer os pés, a distância certa. O mais simples e o mais rápido.
- **Jab com passo (step jab):** o pé da frente avança um pouco e chega **pouco antes ou ao mesmo tempo** que a mão; o de trás vem atrás **[fonte: Papazoglou, Boxing News, Tony Jeffries "sync your foot with hand"]**. Mais alcance e um pouco mais de força.
- **Power jab:** passo e peso por trás do golpe, corpo "a afundar" um pouco; o peso vai quase todo para o pé da frente **[fonte: Expert Boxing / Wikipedia, via pesquisa]** ([5 types of jabs](https://expertboxing.com/5-types-of-jabs), [Wikipedia](https://en.wikipedia.org/wiki/Jab)).
- **Jab de recuo (backstep):** o pé de trás recua ao mesmo tempo que a mão sai; fraco, mas trava quem vem a entrar **[fonte: Expert Boxing]**.
- **Jab ao corpo:** dobra-se os joelhos para baixar o corpo (não se aponta a mão para baixo a partir de pé); é menos usado porque expõe ao counter **[fonte: Wikipedia]**.
- **Pivot jab:** jab e pivô no pé da frente para sair do sítio.

**Animação principal:** o **jab parado** (sem passo), com um pequeno avanço da pelvis. Começa e acaba no mesmo sítio, encaixa em todas as distâncias e o jogo já desloca os lutadores à parte. O jab com passo fica como segunda animação (precisa de mover o boneco para a frente: "root motion").

---

## 4. Erros que fazem o jab parecer errado (evitar na animação)

1. **Baixar a mão de trás** — tem de ficar colada à cara o tempo todo **[fonte]**.
2. **Cotovelo a abrir para o lado** (chicken wing) — o cotovelo vai por baixo; só no fim, com a palma para baixo, aponta para fora **[fonte]**.
3. **Puxar o braço devagar ou baixar a mão no regresso** — o regresso é rápido e à altura da cara **[fonte: Boxing News]**.
4. **Inclinar demais / cabeça à frente** — a cabeça fica atrás do ombro; leaning in é "dos erros mais comuns" **[fonte]**. **[estimativa]** regra prática: o nariz não passa à frente do joelho da frente.
5. **Rodar demais** — o jab roda pouco; rodar muito torna-o lento e parece um direto **[fonte]**.
6. **Recuar ou baixar a mão antes de bater** (denunciar o golpe) **[fonte]**.
7. **Rodar o punho cedo** — a rotação é no fim, para a mão ir reta **[fonte]**.
8. **Ombro da frente em baixo no impacto** — queixo à mostra **[fonte]**.
9. **[estimativa]** Mão a andar a velocidade constante: tira o "estalo".
10. **[estimativa]** Esticar o braço para além do comprimento real (o braço "estica" no desenho) — nunca passar de ~0,95–1,0 do comprimento do braço.

---

## 5. Diferença para o direto (para mais tarde)

- O direto é a mão de trás e é **conduzido pelo pé de trás**: o **calcanhar de trás roda para fora (pivô)** e as ancas e ombros rodam **muito** em direção ao alvo **[fonte]** ([Wikipedia](https://en.wikipedia.org/wiki/Cross_(boxing)), [Dynamic Striking](https://dynamicstriking.com/blogs/news/cross-boxing)). Guias falam de 45–90° de pivô do pé (valor sem fonte primária).
- O peso passa mais claramente do pé de trás para o da frente **[fonte]**; mais flexão do pé e do joelho de trás **[fonte: treinadores irlandeses]**.
- A mão de trás cruza a linha central; a mão do jab volta para a cara **[fonte]**.
- Golpe mais forte (num estudo 1702 N vs 1262 N do jab; na elite as forças ficam parecidas) **[fonte]** e ligeiramente mais lento a reagir **[fonte: Loturco et al. 2015]** ([USP](https://repositorio.usp.br/item/002735639)).
- **[estimativa]** Ancas ~40–50°, peito ~50–60°: **passa o limite de 20° do esqueleto**. Será preciso subir o limite para o direto (ou fazer de conta com o ombro/pulso).

---

## 6. Tabela fotograma a fotograma — jab básico (parado), 8 fotogramas

### Convenções

- **H** = altura do corpo (pés ao topo da cabeça). **L** = comprimento do braço (ombro ao pulso).
- **Pelvis** (dx, dz, dy) em fração de H, relativa à guarda: dx + = para a **direita** do pugilista, dz + = para a **frente** (para o adversário), dy + = para **cima**.
- **Ancas / peito:** graus à volta do eixo vertical, **relativos à guarda** (a guarda já está de lado). **+ = o ombro/anca esquerda vai para a frente** (o sentido do jab). O direto seria negativo.
- **Tronco:** inclinação em graus, **além** da que já tem na guarda (~5° para a frente). Frente + = para o adversário; lado + = para a direita (para trás, o lado da mão de trás).
- **Cabeça:** rotação relativa ao peito (− = contraria o peito para os olhos ficarem no alvo); inclinação + = queixo para baixo, além da guarda.
- **Pulso da frente / de trás:** (frente, dentro, cima) em fração de L, **relativo ao ombro do mesmo lado**; "dentro" = para a linha central do corpo.
- **Punho:** rotação do antebraço; 0° = polegar para cima (guarda), 90° = palma para baixo.
- **Cotovelo:** para onde aponta a ponta do cotovelo.
- **Pés:** relativos à pelvis inicial, em fração de H: **frente (−0,07; +0,16)** e **trás (+0,07; −0,16)** (dx; dz) — afastamento total ~0,32 H, à largura dos ombros de lado **[estimativa a partir de "largura dos ombros"]**. No jab parado **os pés não mudam de sítio**.

### Tabela

| F | Fase | ms | Pelvis dx / dz / dy (×H) | Ancas | Peito | Tronco frente / lado | Cabeça rot. / incl. / lado | Pulso frente (f, d, c ×L) | Punho | Cotovelo frente | Pulso trás (f, d, c ×L) | Peso frente | Pés / joelhos |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° / 0° | 0,40 / 0,10 / 0,15 | 0° | para baixo | 0,30 / 0,30 / 0,20 | 50 % | calc. trás levantado ~0,015 H; joelhos ~15–20° dobrados |
| 1 | Arranque | 40 | −0,002 / +0,005 / 0 | +2° | +2° | +1° / 0° | −2° / 0° / 0° | 0,48 / 0,10 / 0,13 | 0° | para baixo | igual | 52 % | pé de trás empurra |
| 2 | Extensão 1 | 40 | −0,003 / +0,010 / 0 | +4° | +7° | +2° / +1° | −5° / +1° / +1° | 0,62 / 0,11 / 0,10 | 10° | baixo, por dentro | igual | 55 % | joelho de trás começa a esticar |
| 3 | Extensão 2 | 40 | −0,004 / +0,015 / −0,003 | +6° | +13° | +3° / +2° | −10° / +2° / +3° | 0,82 / 0,12 / 0,07 | 45° | baixo-fora (~30°) | igual (mais junto ao queixo) | 58 % | |
| 4 | **Impacto** | 80 | −0,005 / +0,020 / −0,005 | +8° | +18° | +4° / +3° | −14° / +3° / +5° | **0,95 / 0,12 / 0,05** | **90°** | para fora (horizontal) | 0,30 / 0,32 / 0,20 | **~60 %** | calc. trás +0,005 H; joelho trás −5°, frente +3° |
| 5 | Regresso 1 | 50 | −0,004 / +0,015 / −0,003 | +6° | +12° | +3° / +2° | −10° / +2° / +3° | 0,78 / 0,12 / 0,08 | 60° | baixo-fora | igual | 57 % | |
| 6 | Regresso 2 | 60 | −0,002 / +0,007 / 0 | +3° | +5° | +1° / +1° | −4° / +1° / +1° | 0,55 / 0,11 / 0,12 | 20° | para baixo | igual | 53 % | |
| 7 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° / 0° | 0,40 / 0,10 / 0,15 | 0° | para baixo | 0,30 / 0,30 / 0,20 | 50 % | = F0 |

Total ~430 ms (F1–F7 ≈ 370 ms). Em loop, o F7 é igual ao F0: pode-se saltar um deles.

### O que é fonte e o que é estimativa na tabela

- **Das fontes (qualitativo):** ordem dos movimentos (pernas → anca → ombro → mão); ancas e peito rodam **pouco** e o peito mais do que as ancas ("quarto de volta" do ombro); velocidade máxima perto do fim; punho palma para baixo no fim, a rodar no último terço; braço quase esticado (cotovelo macio); ombro da frente a subir e queixo atrás dele; cabeça sem ir para a frente; mão de trás fixa na bochecha; cotovelos por baixo; regresso pelo mesmo caminho e um pouco mais longo do que a ida; peso de ~50/50 para a frente; calcanhar de trás levantado; pés sem passo no jab parado; duração total de ~400 ms (Stanley 2018).
- **Estimativas minhas (números):** todos os graus (ancas 8°, peito 18°, tronco 4°/3°, cabeça), as frações de H e de L, os 60 % de peso, a altura do calcanhar e os ângulos dos joelhos, e a divisão dos milissegundos por fotograma. Escolhidos para respeitar o limite de 20° e para se lerem num boneco de 40×60 px (onde 0,02 H ≈ 1 píxel).

### Dicas para o boneco de 40×60 px

- A 60 px de altura, o avanço da pelvis (0,02 H) é **~1 píxel** — chega para se notar o peso a ir para a frente.
- O que mais se lê é: **a mão a sair reta e depressa, o ombro da frente a subir, a mão de trás quieta na cara**. Se só houver píxeis para três coisas, são essas.
- A rotação do punho mal se vê a esta escala: pode desenhar-se como a luva a ficar mais "achatada" no fotograma de impacto.

### Variante com passo (para depois)

Igual, mais: pé da frente avança **~0,06–0,08 H** entre F1 e F4 (chega com o impacto ou um pouco antes); pé de trás segue a mesma distância em F5–F7; a pelvis avança de vez +0,06–0,08 H (o boneco fica mais à frente). **[estimativa; ordem do passo: fonte]**

---

## Fontes

- Expert Boxing (Johnny N): [How to throw a jab](https://expertboxing.com/how-to-throw-a-jab), [5 types of jabs](https://expertboxing.com/5-types-of-jabs), [The ultimate boxing jab guide](https://expertboxing.com/the-ultimate-boxing-jab-guide) — lidos através de excertos da pesquisa.
- Precision Striking: [How to Punch: the 8 basic punches](https://precisionstriking.com/how-to-punch/)
- Boxing News: [Fight School: The Jab](https://boxingnewsonline.net/features/fight-school-the-jab/)
- Human Kinetics (McKenzie & Kirchner, *Total Knockout Fitness*): [How to throw successful jabs](https://canada.humankinetics.com/blogs/excerpt/how-to-throw-successful-jabs)
- Tony Jeffries: [How to throw a jab](https://www.thereadyroom.net/videos/tony-jeffries-how-to-throw-a-jab), [resumo Sanabul](https://sanabulsports.com/blogs/techniques/boxing-basics-how-to-throw-a-jab-sanabul)
- Teddy Atlas (Dynamic Striking): [Fix your jab](https://dynamicstriking.com/blogs/news/fix-your-jab-with-tips-from-teddy-atlas) — pouco detalhe técnico nos excertos.
- fightTIPS (Shane Fazen): vídeo "5 Common Jab Mistakes" — não foi possível ler o conteúdo; só o título.
- Dimitris Papazoglou: [The Left Jab (PDF)](http://www.papazoglouboxing.gr/files/pdf/the_left_jab.pdf)
- West Point: [Intramural Boxing Guide](https://www.scribd.com/document/175877216/US-Army-Boxing-West-Point-Trainers-Manual-51p)
- Wikipedia: [Jab](https://en.wikipedia.org/wiki/Jab), [Cross](https://en.wikipedia.org/wiki/Cross_(boxing))
- Erros comuns: [Healthy Principles](https://www.healthyprinciples.co.uk/common-jab-mistakes/), [FightCamp](https://blog.joinfightcamp.com/training/6-tips-to-throw-the-perfect-jab/), [KO Studio](https://kostudio.co/blogs/news/how-to-throw-a-jab-in-boxing), [Fight Encyclopedia](https://fightencyclopedia.com/blog/blog-how-to-throw-a-perfect-jab-biomechanics) (blog; usado só para confirmar o que outros dizem)
- Biomecânica:
  - Stanley, Thomson, Smith & Lamb (2018), *IJPAS* 18(5): [PDF Chester](https://chesterrep.openrepository.com/bitstream/handle/10034/621889/IJPAS%20(2018).pdf?sequence=1&isAllowed=y)
  - Piorkowski, Lees & Barton (2011), *Sports Biomechanics* 10(1): [ResearchGate](https://www.researchgate.net/publication/51115734_Single_maximal_versus_combination_punch_kinematics)
  - Lenetsky et al. (2020), *JSCR* 34(4): [PubMed](https://pubmed.ncbi.nlm.nih.gov/30789570/)
  - Liu et al. (2022), *Frontiers in Physiology*: [artigo](https://frontiersin.org/articles/10.3389/fphys.2022.1015154/full)
  - Dynamic inertial analysis of the Jab (2022): [PDF](http://efsupit.ro/images/stories/martie2022/Art%2083.pdf)
  - Increasing the maximum angular velocity of the jab punch (2025): [sportpedagogy](https://sportpedagogy.org.ua/index.php/ppcs/article/view/3486)
  - Treinadores irlandeses (2025), *IJPAS*: [PDF](https://www.tandfonline.com/doi/pdf/10.1080/24748668.2025.2481693)
  - Kimm & Thiel (2015), *Hand speed measurements in boxing*: [PDF](https://pub.h-brs.de/frontdoor/deliver/index/docId/1685/file/Kimm_Thiel_2015_Hand_Speed_Measurements.pdf)
  - Loturco et al. (2015), tempo de reação jab vs direto: [USP](https://repositorio.usp.br/item/002735639)

**Lacuna:** nenhuma fonte encontrada dá **graus** de rotação de ancas/peito no jab, nem a percentagem de peso em cada perna. Se for preciso, os PDFs de Stanley 2018 (Chester) e da tese METU ([PDF](https://open.metu.edu.tr/bitstream/handle/11511/21166/index.pdf?sequence=1&isAllowed=y)) devem ter ângulos nas tabelas — dá para os ler se o acesso a esses sites for autorizado nas definições de rede da sessão.
