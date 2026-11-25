# Pesquisa: levar um golpe na cara (para a animação)

Reação de um pugilista em guarda ortodoxa (pé esquerdo à frente) que leva **um jab ou um direto de frente na cara**, dados pelo adversário que está à frente dele (também ortodoxo). Objetivo: animar o mesmo boneco de ~40×60 px com o mesmo esqueleto 3D (pelvis, rotação de ancas e peito, inclinação do tronco, cabeça, pulsos, pés, cotovelos). Mesmo formato e mesmas unidades de `docs/pesquisa-jab.md` e `docs/pesquisa-direto.md`, para se poder juntar a reação ao golpe de quem bate.

> **Fontes e marcas.** Li por inteiro: os artigos do **Expert Boxing** (Johnny N) *How To Take Punches Better*, *How to AVOID getting knocked out* e a resposta do *Boxing Mailbag 3-7-11* sobre o que acontece a quem leva um direto; o estudo de **Pashaei et al. 2023** (kickboxers a levar um golpe na testa, preparados e de surpresa, com sensores no pescoço); o estudo de **Eckner et al. 2014** (força do pescoço e "preparar-se" para o impacto). Na segunda ronda li também a **revisão da UBC** sobre biomecânica do boxe (com a tabela do Atha 1985 e do Walilko 2005) e a página **Hitlag do SSBWiki** (fórmulas do hit-stop do Smash Bros.). Do **Walilko, Viano & Bir 2005** continuo a ter só o resumo e a tabela da UBC: o texto completo é um PDF digitalizado e o PMC, o Europe PMC e o BMJ pedem verificação anti-robô. A coluna da **Capcom** está fora do ar. O resto (velocidades, tempos de reflexo, alguns números de jogos) vem de **excertos da pesquisa web** — ver a lista no fim. **[fonte]** = dito por uma fonte (com link); **[estimativa]** = valor meu, coerente com as fontes, para a animação.

---

## 1. O que acontece ao corpo

### O impacto em números (o que os estudos medem)

| Medida | Valor | Fonte |
|---|---|---|
| Direto de pugilistas olímpicos num boneco Hybrid III (7 pugilistas, 18 golpes) | força 3427 ± 811 N; mão a 9,14 ± 2,06 m/s; aceleração da cabeça **58 ± 13 g**; rotação **6343 ± 1789 rad/s²**; corte no pescoço 994 N | Walilko, Viano & Bir 2005 (resumo, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1725037/)) |
| Variação da velocidade da cabeça (ΔV) nesse estudo | **2,97 ± 0,81 m/s** (no futebol americano, nas concussões: 7,2 m/s) | Walilko 2005, via excertos ([ResearchGate](https://www.researchgate.net/publication/7580102_Biomechanics_of_the_head_for_Olympic_boxer_punches_to_the_face)) |
| Os golpes mais pesados abanam mais | a força sobe com a categoria, sobretudo por causa da massa efetiva do golpe | Walilko 2005 (resumo) |
| Jab vs gancho num boneco (amadores) | jab **21,5 ± 4,6 g** e 293 rad/s²; gancho 43,6 ± 15,6 g e 676 rad/s² — **o jab mexe a cabeça cerca de metade** | estudo canadiano citado nos excertos ([IRCOBI 1988](https://www.ircobi.org/wordpress/downloads/irc1988/pdf_files/1988_20.pdf)) |
| Duração do contacto luva-cabeça | **11,4 ms** no Walilko 2005; no Atha 1985 (um pesado profissional contra um alvo pendular) a força chega ao pico de 4096 N **aos 14 ms** e a 6320 N no fim do contacto, com 53 g no alvo | revisão UBC, Tabela 1 ([UBC wiki](https://wiki.ubc.ca/Documentation:FIB_book/Boxing_Injury_Biomechanics)) |
| Mais dados do Walilko 2005 | força **2625 N (médios) a 4345 N (pesados)**; HIC 71; Nij 0,27 (índice de lesão do pescoço, bem abaixo de 1) | revisão UBC, Tabela 1 |
| Em sparring (capacete com sensores, 30 homens e 30 mulheres) | **30 g** e **2571 rad/s²** em média — cerca de metade dos golpes máximos; os golpes **de frente** deram acelerações **menores** do que os de lado e de trás, "talvez porque os golpes de frente são mais frequentes e o pescoço já está preparado" | Stojsih/Beckwith, via revisão UBC (Tabela 2) |
| Velocidade angular do pescoço num direto (boneco) | **31 rad/s** (≈ 1800 °/s); o direto teve o maior momento no pescoço (99,8 N·m) | Bartsch et al. 2009, resumo ([OSU](https://ibrc.osu.edu/wp-content/uploads/2014/01/Bartsch_Abstract_2009.pdf), excerto) |
| Tempo de reação dos músculos do pescoço a um puxão inesperado | **~30–90 ms** (esternocleidomastoideu ~33 ms, trapézio ~45–50 ms; 53 ms a resistir, 76 ms relaxado) | Wochner 2022 e J Physiol 1996, excertos ([BMC](https://biomedical-engineering-online.biomedcentral.com/articles/10.1186/s12938-022-00994-9/tables/2), [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC1160902)) |
| Contrair o pescoço **antes** do golpe | modelo: ativar 40 ms antes baixa o pico da velocidade de rotação da cabeça em **18–31 %**; a força dos músculos não muda os primeiros **< 50 ms** | modelos citados nos excertos ([Duke](https://scholars.duke.edu/publication/1361336)) |

**Como ler isto.** O contacto dura **menos de um fotograma** de um jogo a 60 fps (16 ms). Nesse tempo a cabeça ganha **~3 m/s** para trás num direto olímpico; o pescoço só reage **30–90 ms depois**, por isso, **se o golpe não era esperado, o pescoço não chega a tempo**: a cabeça vai para trás "solta" e o corpo é que a trava. Se o pugilista viu o golpe e contraiu o pescoço antes, a cabeça mexe muito menos. **[fonte: tempos de reflexo + modelos]**

### Preparado vs apanhado de surpresa (o estudo que mais interessa)

**Pashaei et al. 2023** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10227954/)): 24 kickboxers de pé levaram 3 golpes "seguros" na testa (de luvas e capacete) de um campeão do mundo, primeiro de **olhos abertos** (a ver o golpe) e depois de **olhos fechados** e pescoço relaxado. Sensores na nuca e na C7 a 100 Hz.

| | Preparado (vê o golpe) | Surpresa (não vê) |
|---|---|---|
| **Extensão do pescoço** (cabeça para trás) | **6,4°** | **29,2°** |
| Flexão do pescoço (o ressalto para a frente) | 29,0° | 42,5° |

**[fonte]** É um golpe leve (controlado, à testa). A diferença é enorme: **~4,5 vezes mais** para trás quando não se vê o golpe. O estudo diz que o esternocleidomastoideu (o músculo da frente do pescoço) "trabalhou mais" quando o atleta via o golpe e foi isso que travou a extensão. Os valores de flexão (o regresso para a frente) são grandes nos dois casos; o estudo não explica bem como os mediu, por isso uso-os só como sinal de que **há um ressalto para a frente depois do recuo** **[fonte; leitura minha]**.

**Eckner et al. 2014** ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4344320/)): 46 atletas, puxões rápidos na cabeça em todas as direções. **Mais força no pescoço e contrair antes do impacto** ("preparar-se") **baixam as duas coisas, a velocidade e a rotação da cabeça**, em todas as direções (todos p < 0,001); os dois efeitos somam-se. Os registos mostram o movimento da cabeça nos **primeiros 150 ms** depois do puxão **[fonte]**.

**Expert Boxing** diz o mesmo por palavras de pugilista **[fonte]** ([How To Take Punches Better](https://expertboxing.com/how-to-take-punches-better), [How to AVOID getting knocked out](https://expertboxing.com/how-to-avoid-getting-knocked-out-in-a-fight)):
- "Os golpes que não vês são os que doem mais"; o profissional "via todos os golpes a chegar e **preparava-se** para eles".
- **Queixo para baixo**: "com o queixo em baixo, os golpes têm menos alavanca na cabeça. Com a cabeça direita no ar, o golpe vai direto à cabeça e no ângulo perfeito para **'estalar' o pescoço**." Com a cabeça inclinada, o impacto "espalha-se pelo pescoço até à coluna" e o golpe tende a bater na testa (a parte mais dura do crânio) em vez do queixo.
- **Cabeça virada para a frente** aguenta melhor os diretos do que de lado; os golpes **mais perigosos são os que apanham a cabeça a virar-se para eles**.
- Relaxar ("como apanhar uma bola rápida") e fortalecer o pescoço "para a cabeça não levar um esticão tão forte".

### A cabeça

- **Direção:** um golpe de frente empurra a cabeça **para trás, com o queixo a subir** (extensão do pescoço) **[fonte: Pashaei — "extension"; Walilko — direto ao queixo]**.
- **Rotação:** depende de onde vem a luva **[estimativa por geometria]**. Os dois são ortodoxos, de frente um para o outro:
  - o **jab** do adversário (mão esquerda dele) vem quase a direito, um pouco do **nosso lado direito**: empurra o queixo um nadinha para a nossa esquerda → a cabeça roda **pouco para a esquerda**;
  - o **direto** dele (mão direita) vem do **nosso lado esquerdo** e atravessa para o centro: empurra o queixo para a nossa direita → a cabeça roda **para a direita** (afasta-se da luva). É também para aí que se "rola com o golpe": Freddie Roach — "se vem uma direita, roda o queixo para a direita" **[fonte: excerto da [Bloomberg](https://www.bloomberg.com/news/articles/2012-04-12/how-to-take-a-punch-freddie-roach)]**.
- **Quantos graus:** jab preparado ~5–8°; jab de surpresa ~20–30°; direto forte preparado ~15–25°; direto de surpresa ou abanado 30–40° **[6° e 29° = fonte Pashaei para um golpe leve; o resto = estimativa: no boneco o gancho dá ~2× a aceleração do jab, e assumi o mesmo para o direto]**.
- **Quando:** a cabeça começa a mexer **no próprio fotograma do contacto** (< 15 ms) e chega ao máximo **~50–100 ms depois** (o tempo de o pescoço reagir e travar) **[estimativa a partir dos tempos de reflexo e da janela de 150 ms do Eckner]**.
- **Volta depressa:** "quando acerto em alguém em cheio na cabeça, **a cabeça volta logo à posição neutra**"; "é muito difícil empurrar alguém a bater-lhe na cabeça" **[fonte: Expert Boxing, Mailbag]**. Regresso à guarda ~150–250 ms depois do máximo **[estimativa]**, com um **pequeno ressalto para a frente** (queixo a descer um pouco abaixo da guarda) antes de assentar **[fonte: Pashaei mostra flexão depois da extensão; valor: estimativa]**.

### O pescoço, o tronco e as pernas (o "almofada")

- Expert Boxing: "Bater num adversário vivo não é como bater num objeto duro. Ele **absorve a força sem ser empurrado todo para trás**. Há articulações no **pescoço, ombros, cintura, joelhos e tornozelos** que deixam a zona batida absorver um pouco o golpe e **'ressaltar'**. Pensa no corpo como **uma almofada**, não como um saco pesado." E: "**um golpe não é um empurrão**." **[fonte: [Mailbag 3-7-11](https://expertboxing.com/boxing-mailbag-3-7-11)]**
- Para a animação, isto quer dizer: a cabeça faz a maior parte do movimento; o **tronco inclina um pouco para trás** (poucos graus), as **ancas recuam muito pouco** (1–2 cm), os **joelhos dobram um nadinha** a absorver e o **peso passa um pouco para o pé de trás**; os pés **não** escorregam para trás num jab ou num direto normal **[fonte: Expert Boxing; valores: estimativa]**.
- **Ombros e cotovelos:** os braços estão "pendurados" nos ombros; quando o tronco recua, as mãos ficam um instante para trás do movimento e depois **sobem e fecham a guarda** (reflexo de proteção, olhos a piscar) **[estimativa: princípio de "follow-through/overlap" da animação; nenhuma fonte de boxe dá números]**.

### Leve, forte e muito forte (abanado)

| | Jab (leve) | Direto forte | Muito forte / abanado |
|---|---|---|---|
| Cabeça para trás | 5–8° (preparado) / 20–30° (surpresa) | 15–25° / 30–35° | 30–40°, e fica "solta" |
| Rotação da cabeça | 2–4° (para a esquerda) | 10–15° (para a direita) | 15–25° |
| Tronco para trás | 1–2° | 5–8° | 8–12° e depois **cai para a frente/para baixo** |
| Pernas | quase nada | joelhos dobram ~10°, peso no pé de trás | **as pernas falham**: ancas descem, um passo atrás ou de lado para não cair |
| Guarda | fica; aperta | abre um pouco e fecha logo | **as mãos descem** |
| Tempo total | ~300 ms | ~450–500 ms | 0,8–1,5 s ("abanado"), regresso lento |

Fontes da linha "abanado": Expert Boxing — "um direto perfeito **não o empurra para fora do alcance**: o mais provável é ele **ir ao chão, a desmoronar-se para baixo quando as pernas falham**" **[fonte: [Mailbag](https://expertboxing.com/boxing-mailbag-3-7-11)]**; num KO há uma **perda do tónus muscular imediata, em dezenas de milissegundos** **[fonte: estudo de vídeo de KOs, excerto ([esmed.org](https://esmed.org/MRA/mra/article/view/4007))]**; nas animações, "a reação começa muito depressa e **acaba devagar** para mostrar efeitos como tonturas" **[fonte: [Game Developer](https://gamedeveloper.com/programming/the-role-of-animations-in-hit-effects), excerto]**. Os graus são **[estimativa]**.

---

## 2. Tempos

| Fase | Real (estudos) | Na animação (proposta) |
|---|---|---|
| Contacto | 11,4 ms (Walilko), pico aos 14 ms (Atha) **[fonte: revisão UBC]** | 1 fotograma **congelado** ("hit-stop") de 80 ms no jab e 90–130 ms no direto, igual ao fotograma de impacto de quem bate (80 ms no jab, 90 ms no direto, nos outros relatórios) **[estimativa, dentro do intervalo do Smash Bros.: ~4–8 fotogramas para golpes leves a médios]** |
| Recuo da cabeça até ao máximo | pescoço só reage aos ~30–90 ms; registos até 150 ms **[fonte: reflexos, Eckner]** | 40–50 ms depois do hit-stop **[estimativa]** |
| Recuo do corpo (tronco, ancas, peso) | — (sem dados) | 50–120 ms, a acabar **depois** da cabeça **[estimativa]** |
| Regresso + ressalto | "a cabeça volta logo ao neutro" **[fonte: Expert Boxing]** | 150–250 ms, a abrandar no fim **[estimativa]** |
| Reação inteira | — | jab ~330 ms, direto ~510 ms, abanado ~1 s **[estimativa]** |

---

## 3. O que os jogos de luta fazem

- **Hit-stop (congelar no impacto):** "os fotogramas congelados que dão força ao golpe, às vezes com o ecrã a tremer se o golpe for muito forte"; é sobretudo dos jogos 2D **[fonte: Sakurai, coluna da Famitsu, via [Source Gaming](https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/) e [My Nintendo News](https://mynintendonews.com/2015/11/12/sakurai-talks-about-the-term-hitstop-used-in-fighting-games/), excertos]**. **Congela os dois**, quem bate e quem leva; congelar só quem leva "parece um soluço" **[fonte: [Uhiyama Lab](https://uhiyama-lab.com/en/notes/unity/unity-game-feel-hit-feedback/), excerto]**.
- **Quantos fotogramas no Smash Bros. (a 60 fps):** quem bate e quem leva ficam congelados; quem bate no fotograma em que acertou, quem leva **no primeiro fotograma da animação de estremecer, a tremer**. Fórmula (d = dano do golpe em %): Melee ⌊d/3 + 3⌋; Brawl/Smash 4 ⌊0,385·d + 5⌋; Ultimate ⌊0,65·d + 6⌋. Um golpe de 15 % dá **8 fotogramas no Melee (133 ms), 10 no Brawl/Smash 4 e 15 no Ultimate**; golpes fracos como o jab do Mario têm "hit-stop mínimo" (com ~3 %: 4 fotogramas no Melee, 7 no Ultimate); máximo de **20 fotogramas no Melee e 30 do Brawl em diante**; ataques elétricos ×1,5 **[fonte: [SSBWiki, Hitlag](https://www.ssbwiki.com/Hitlag)]**.
- **Capcom e outros:** a Capcom dá como exemplo **8 / 12 / 16** para golpes leve / médio / forte, e menos nos golpes de vários toques para não ficarem "pesados" **[fonte: [SF Seminar, Capcom](https://game.capcom.com/cfn/sfv/column/131545?lang=en), excerto]**. Outra regra prática: leves ~9, médios ~11, fortes ~13; no Street Fighter II antigo, ~14 em todos **[fonte: excerto de pesquisa sobre frame data, por confirmar]**. 8–16 fotogramas = **130–270 ms**: para um simulador sem botões, é muito; aqui proponho **~5 fotogramas (80 ms) no jab e ~6–8 (90–130 ms) no direto**, mais no golpe que abana — perto do Smash Melee (4 fotogramas num golpe fraco, 8 num de 15 %) **[estimativa apoiada no SSBWiki]**. (A coluna da Capcom estava fora do ar nesta pesquisa, "maintenance", por isso os 8/12/16 continuam a vir só do excerto.)
- **Durante o hit-stop, quem leva já está a reagir:** no Smash, a personagem passa em **4 fotogramas** do primeiro estremeção para a pose de "magoado", e **treme de um lado para o outro** (no chão) **[fonte: Sakurai via Source Gaming, excerto; [Gameranx](https://gameranx.com/updates/id/474375/article/masahiro-sakurai-reveals-insane-details-put-into-hit-animations-for-smash-bros/)]**. Ou seja: o fotograma congelado **não** é a pose de guarda, é já a cabeça a sair para trás.
- **Clarão:** 2 fotogramas a branco no fotograma do golpe **[fonte: [Uhiyama Lab](https://uhiyama-lab.com/en/notes/unity/unity-game-feel-hit-feedback/), excerto]**.
- **Começar de repente, acabar devagar; sem mistura:** a reação "deve começar muito depressa e acabar devagar"; pôr **o tempo de mistura (crossfade) a zero** na entrada da reação, senão parece mole **[fonte: [Game Developer](https://gamedeveloper.com/programming/the-role-of-animations-in-hit-effects), excerto]**.
- **Reação conforme direção e força** do golpe e peso de quem leva; a cabeça precisa de menos força do que o peito para parecer certa **[fonte: excertos ([Game Developer](https://www.gamedeveloper.com/production/the-12-principles-of-animation-in-video-games), [Ironsami](https://ironsami-studio.gitbook.io/proceduralhitreactions))]**.
- **Atraso das partes soltas (follow-through):** depois do golpe "o corpo não pára de uma vez: o peito assenta, os braços recuam, o cabelo vai um tempo atrás" **[fonte: excerto]**.
- **Não congelar em todos os golpes pequenos**, senão o jogo fica "pegajoso" **[fonte: Sakurai; Uhiyama Lab, excertos]** → num jab de rotina, hit-stop curto (ou nenhum se forem muitos seguidos).

---

## 4. Erros a evitar

1. **Reação exagerada num jab.** O jab mexe a cabeça cerca de metade de um gancho (21,5 vs 43,6 g) e "não faz tanto dano como um gancho" **[fonte]**. Num pugilista preparado, a cabeça vai ~6° para trás, não 30°.
2. **O corpo todo a escorregar para trás**, como se fosse empurrado. "Um golpe não é um empurrão"; o corpo é "uma almofada" **[fonte: Expert Boxing]**. Os pés ficam; quem recua é a cabeça e um pouco o tronco.
3. **A cabeça a ir para o lado errado:** para a frente, para a luva, ou a rodar **para** o golpe. Vai **para trás, queixo para cima**, e roda **para longe** da luva (direto: para a direita) **[fonte + geometria]**.
4. **Voltar devagar demais.** "A cabeça volta logo à posição neutra" **[fonte]**. Só volta devagar quando está abanado.
5. **Atraso no início:** a reação começa **no fotograma do contacto**. Quem leva não tem "antecipação" (o *wind-up* é de quem bate); a única preparação de quem leva é **baixar o queixo e apertar a guarda** antes, se viu o golpe **[fonte + estimativa]**.
6. **Tudo a mexer ao mesmo tempo:** a ordem é **cabeça → tronco → ancas/peso**, e no regresso também; as mãos vão um tempo atrás **[estimativa: follow-through]**.
7. **Mistura suave a entrar na reação** (parece mole) **[fonte: Game Developer]**.
8. **A mesma reação para tudo:** variar com o golpe (jab/direto), a força, e com "viu/não viu" **[fonte: Game Developer; Pashaei]**.
9. **Ficar parado no hit-stop na pose de guarda** — o fotograma congelado deve já mostrar o estremeção **[fonte: Sakurai]**.
10. **Cair para trás num golpe que abana:** quem fica abanado **desmorona-se para baixo**, as pernas falham **[fonte: Expert Boxing]**.

---

## 5. Tabelas fotograma a fotograma

### Convenções (iguais às do jab e do direto)

- **H** = altura do corpo. **L** = comprimento do braço (ombro → pulso).
- **Pelvis** (dx, dz, dy) em fração de H, relativa à guarda: dx + = para a **direita** do pugilista, dz + = para a **frente** (para o adversário), dy + = para **cima**. **Na reação o dz é negativo** (recua).
- **Ancas / peito:** graus à volta do eixo vertical, relativos à guarda; **+ = o lado esquerdo vai para a frente** (o nariz vira para a direita).
- **Tronco:** inclinação além da guarda. Frente + = para o adversário (**para trás é negativo**); lado + = para a direita (o ombro esquerdo sobe).
- **Cabeça:** rotação relativa ao peito com o **mesmo sinal** (+ = o nariz vira para a direita); inclinação + = queixo para baixo, **− = queixo para cima / cabeça para trás** (extensão).
- **Pulsos:** (frente, dentro, cima) em fração de L, relativos ao ombro do mesmo lado. Guarda: frente 0,40 / 0,05 / 0,25; trás 0,30 / 0,25 / 0,15 (dos outros relatórios).
- **Pés:** frente (−0,11; +0,09), trás (+0,11; −0,06) (dx; dz, ×H, relativos à pelvis da guarda); calcanhar de trás levantado na guarda. **Joelhos:** 180° = esticado; guarda ~160°.
- **Peso frente:** % do peso no pé da frente (guarda 50 %).
- **ms** = quanto tempo fica cada fotograma. O **F1 (contacto)** é o mesmo instante do fotograma de impacto de quem bate (F4 do jab e do direto) e é o **hit-stop**: os dois pugilistas ficam congelados.

### (a) Reação a um jab na cara — 7 fotogramas (preparado: viu o golpe)

| F | Fase | ms | Pelvis dx / dz / dy (×H) | Ancas | Peito | Tronco frente / lado | Cabeça rot. / incl. | Peso frente | Joelho trás / frente |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Guarda (golpe a chegar) | 40 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / **+3°** (queixo baixa ao ver o golpe) | 50 % | 160° / 160° |
| 1 | **Contacto (hit-stop)** | 80 | 0 / −0,002 / 0 | 0° | 0° | −1° / 0° | −2° / −3° | 49 % | 160° / 160° |
| 2 | Recuo máximo da cabeça | 40 | 0 / −0,004 / −0,002 | 0° | +1° | −2° / 0° | −3° / **−6°** | 47 % | 158° / 159° |
| 3 | Recuo do tronco | 50 | 0 / −0,005 / −0,003 | 0° | +1° | −2° / 0° | −2° / −4° | 46 % | 157° / 158° |
| 4 | Regresso | 50 | 0 / −0,003 / −0,002 | 0° | 0° | −1° / 0° | −1° / −1° | 48 % | 158° / 159° |
| 5 | Ressalto | 50 | 0 / −0,001 / −0,001 | 0° | 0° | 0° / 0° | 0° / +2° | 49 % | 159° / 160° |
| 6 | Guarda | 60 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 50 % | 160° / 160° |

| F | Pulso frente (f / d / c ×L) | Cotovelo frente | Pulso trás (f / d / c ×L) | Cotovelo trás | Pés |
|---|---|---|---|---|---|
| 0 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | fixos, calc. trás levantado |
| 1 | 0,39 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,16 | junto às costelas | fixos |
| 2 | 0,37 / 0,06 / 0,24 (a mão fica um tempo atrás do tronco) | para baixo | 0,29 / 0,26 / 0,18 (sobe para o queixo) | para dentro | fixos |
| 3 | 0,37 / 0,07 / 0,26 (aperta a guarda) | para dentro | 0,29 / 0,27 / 0,18 | para dentro | fixos; calc. trás desce ~0,005 H |
| 4 | 0,39 / 0,06 / 0,26 | para baixo | 0,30 / 0,26 / 0,16 | junto às costelas | fixos |
| 5 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | fixos |
| 6 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | = F0 |

Total ~370 ms (~330 ms depois do contacto). **Apanhado de surpresa** (não viu o jab): sem o +3° no F0; cabeça F2 **−20° a −25°**, rotação −4°; tronco F2–F3 −3°; pelvis dz −0,008 H; peso 44 %; mãos da guarda abrem ~0,03 L para fora e descem ~0,03 L em F2 antes de voltar; F4 e F5 com +20 ms cada.

### (b) Reação a um direto forte na cara — 8 fotogramas (meio preparado)

| F | Fase | ms | Pelvis dx / dz / dy (×H) | Ancas | Peito | Tronco frente / lado | Cabeça rot. / incl. | Peso frente | Joelho trás / frente |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Guarda (golpe a chegar) | 40 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / +2° | 50 % | 160° / 160° |
| 1 | **Contacto (hit-stop)** | 110 | 0 / −0,003 / 0 | 0° | −2° | −1° / +1° | +6° / −8° | 48 % | 160° / 160° |
| 2 | Recuo máximo da cabeça | 50 | +0,002 / −0,008 / −0,004 | −1° | −4° | −4° / +2° | **+14° / −22°** | 43 % | 155° / 158° |
| 3 | Recuo do tronco | 60 | +0,003 / −0,014 / −0,008 | −2° | −5° | **−7° / +2°** | +10° / −16° | 38 % | 150° / 157° |
| 4 | Travagem no pé de trás | 60 | +0,003 / −0,016 / −0,010 | −2° | −4° | −6° / +1° | +5° / −9° | **36 %** | **148°** / 157° |
| 5 | Regresso | 70 | +0,002 / −0,010 / −0,006 | −1° | −2° | −3° / +1° | +2° / −3° | 42 % | 153° / 158° |
| 6 | Ressalto | 70 | 0 / −0,004 / −0,002 | 0° | 0° | +1° / 0° | 0° / +3° | 48 % | 158° / 159° |
| 7 | Guarda | 70 | 0 / 0 / 0 | 0° | 0° | 0° / 0° | 0° / 0° | 50 % | 160° / 160° |

| F | Pulso frente (f / d / c ×L) | Cotovelo frente | Pulso trás (f / d / c ×L) | Cotovelo trás | Pés |
|---|---|---|---|---|---|
| 0 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | fixos, calc. trás levantado |
| 1 | 0,39 / 0,04 / 0,25 | para baixo | 0,30 / 0,25 / 0,16 | junto às costelas | fixos |
| 2 | 0,36 / 0,01 / 0,21 (atrás do tronco, abre e desce) | a abrir para fora | 0,28 / 0,24 / 0,19 (sobe para a cara) | para dentro | fixos |
| 3 | 0,35 / 0,02 / 0,22 | para fora | 0,28 / 0,26 / 0,19 | para dentro | calc. trás desce (~0,01 H) |
| 4 | 0,37 / 0,05 / 0,26 (fecha a guarda) | para dentro | 0,29 / 0,27 / 0,18 | para dentro | calcanhar de trás no chão |
| 5 | 0,39 / 0,06 / 0,26 | para baixo | 0,30 / 0,26 / 0,16 | junto às costelas | calc. trás a subir |
| 6 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | fixos |
| 7 | 0,40 / 0,05 / 0,25 | para baixo | 0,30 / 0,25 / 0,15 | junto às costelas | = F0 |

Total ~530 ms (~490 ms depois do contacto). A pelvis vai **+0,003 H para a direita** porque o direto vem do lado esquerdo dele e empurra para a nossa direita **[estimativa]**.

**Direto que abana** (variante): igual até ao F3 com a cabeça a −30° a −35° e rotação +18°; depois, em vez de regressar, **F4–F6 "pernas a falhar"**: pelvis dy até **−0,04 H**, joelhos ~135°, tronco cai para +5° (para a frente), mãos descem até "cima" ≈ 0,05 L, o pé de trás dá um passo de ~0,03 H para trás ou de lado; a cabeça fica a −8° e balança ±3° a cada 150 ms; regresso à guarda **lento, 600–1000 ms**, a abrandar no fim **[fonte: Expert Boxing ("as pernas falham"), Game Developer ("acabar devagar"); valores: estimativa]**.

### O que é fonte e o que é estimativa nas tabelas

- **Das fontes:**
  - **Direção:** cabeça para trás com o queixo a subir (extensão); o corpo absorve em várias articulações e **não é empurrado** para trás; a cabeça **volta logo** ao neutro (Expert Boxing, Pashaei).
  - **Tamanho:** jab preparado ~6° de extensão, de surpresa ~29° (Pashaei, golpe leve); o gancho tem ~2× a aceleração do jab (estudo canadiano; para o direto assumi o mesmo).
  - **Tempos:** contacto 11,4 ms (Walilko) a 14 ms (Atha); pescoço só reage aos 30–90 ms; registos da cabeça até ~150 ms (Atha, Walilko, Wochner, Eckner).
  - **Preparar-se:** baixar o queixo e contrair o pescoço reduz muito o movimento (Eckner, Pashaei, Expert Boxing) — por isso o **+2°/+3° no F0** (queixo a descer quando vê o golpe).
  - **Ressalto** para a frente depois do recuo (Pashaei mede flexão depois da extensão).
  - **Hit-stop** com os dois congelados e o estremeção já a acontecer durante o congelamento (Sakurai, SSBWiki, Uhiyama); a duração do F1 (80 ms no jab, 110 ms no direto ≈ 5 e 7 fotogramas a 60 fps) fica dentro do que o Smash usa para golpes fracos e médios (4–10 fotogramas no Melee/Brawl).
  - **Abanado:** pernas a falhar, cair para baixo; perda de tónus em dezenas de ms; reação "rápida a começar, lenta a acabar".
- **Estimativas minhas (números):**
  - Os graus da cabeça no direto (−22° de extensão, +14° de rotação) e todas as rotações.
  - A pelvis (dz −0,005 H no jab, −0,016 H no direto ≈ 1 cm e 3 cm), o peso no pé de trás (46 % e 36 %) e os joelhos.
  - Os pulsos (a mão "fica para trás" do tronco e depois aperta) e a divisão dos milissegundos por fotograma.
  - A direção da rotação da cabeça (geometria de dois ortodoxos de frente).

### Dicas para o boneco de 40×60 px

- Com H = 60 px, **no jab o corpo quase não mexe**: a cabeça (~8 px de altura) inclina ~6°, o que dá **~1 px** de queixo a subir e ~1 px de recuo. O que vende o golpe é o **hit-stop de 80 ms**, o **clarão de 2 fotogramas** na cabeça e o tremer de ±1 px; o boneco quase não precisa de mexer.
- No **direto**, a cabeça vai ~2 px para trás e roda (vê-se a cara a virar para a direita), os ombros recuam ~1 px, as ancas ~1 px, e **a mão da frente abre e desce 1–2 px** antes de voltar — é isto que distingue "levou um 2" de "levou um 1".
- Abanado: o sinal mais claro é **o boneco a descer 2–3 px** (joelhos) com as mãos a cair; não o deitar para trás.

---

## Fontes

**Lidas por inteiro:**
- Expert Boxing (Johnny N): [How To Take Punches Better](https://expertboxing.com/how-to-take-punches-better) (2008), [How to AVOID getting knocked out (in a fight)](https://expertboxing.com/how-to-avoid-getting-knocked-out-in-a-fight) (2019), [Boxing Mailbag 3-7-11](https://expertboxing.com/boxing-mailbag-3-7-11) (pergunta 4), [Boxing Defense Techniques](https://expertboxing.com/boxing-defense-techniques).
- Pashaei, Babakhani & Banihashemi (2023), *Evaluation of surface electromyography of selected neck muscles during the whiplash mechanism in aware and unaware conditions due to safe punching in kickboxing*, BMC Musculoskelet Disord: [PMC10227954](https://pmc.ncbi.nlm.nih.gov/articles/PMC10227954/) — Tabela 1.
- Eckner et al. (2014), *Effect of Neck Muscle Strength and Anticipatory Cervical Muscle Activation on the Kinematic Response of the Head to Impulsive Loads*, AJSM: [PMC4344320](https://pmc.ncbi.nlm.nih.gov/articles/PMC4344320/).
- Walilko, Viano & Bir (2005), *Biomechanics of the head for Olympic boxer punches to the face*, BJSM: [PMC1725037](https://pmc.ncbi.nlm.nih.gov/articles/PMC1725037/) — **só o resumo** (o texto completo é um PDF digitalizado; o PMC, o Europe PMC e o BMJ pedem verificação anti-robô, que não contornei).
- Revisão da UBC, *FIB book / Boxing Injury Biomechanics*: [UBC wiki](https://wiki.ubc.ca/Documentation:FIB_book/Boxing_Injury_Biomechanics) — Tabelas 1 e 2 (Atha 1985, Walilko 2005, Stojsih/Beckwith), McIntosh & Patton 2015.
- SSBWiki, [Hitlag](https://www.ssbwiki.com/Hitlag) — fórmulas, exemplos e máximos do hit-stop no Smash Bros.

**Lidas através de excertos da pesquisa:**
- Walilko 2005, ΔV 2,97 m/s: [ResearchGate](https://www.researchgate.net/publication/7580102_Biomechanics_of_the_head_for_Olympic_boxer_punches_to_the_face), [Semantic Scholar](https://www.semanticscholar.org/paper/Biomechanics-of-the-head-for-Olympic-boxer-punches-Walilko-Viano/edbd929ed7812c983b4780fc106ecdf716b58a30).
- Viano & Pellman (2005), *Concussion in Professional Football: Biomechanics of the Striking Player — Part 8*: [PDF](https://nflps.org/wp-content/uploads/2012/08/Neurosurgery-2005-10-1.pdf) (o futebol americano como comparação: ΔV 7,2 m/s).
- Jab vs gancho num Hybrid III (1988): [IRCOBI](https://www.ircobi.org/wordpress/downloads/irc1988/pdf_files/1988_20.pdf).
- Bartsch et al. 2009 (velocidade angular do pescoço 31 rad/s): [OSU](https://ibrc.osu.edu/wp-content/uploads/2014/01/Bartsch_Abstract_2009.pdf).
- Tempos de reflexo do pescoço: [Wochner 2022](https://biomedical-engineering-online.biomedcentral.com/articles/10.1186/s12938-022-00994-9/tables/2), [J Physiol 1996](https://pmc.ncbi.nlm.nih.gov/articles/PMC1160902), [pré-ativação em modelo](https://scholars.duke.edu/publication/1361336).
- Perda de tónus em KOs (vídeo): [esmed.org](https://esmed.org/MRA/mra/article/view/4007).
- Freddie Roach, rolar com o golpe: [Bloomberg](https://www.bloomberg.com/news/articles/2012-04-12/how-to-take-a-punch-freddie-roach).
- Hit-stop e reações nos jogos: [Capcom SF Seminar](https://game.capcom.com/cfn/sfv/column/131545?lang=en), [Sakurai via Source Gaming](https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/), [My Nintendo News](https://mynintendonews.com/2015/11/12/sakurai-talks-about-the-term-hitstop-used-in-fighting-games/), [Game Developer — hit effects](https://gamedeveloper.com/programming/the-role-of-animations-in-hit-effects), [Game Developer — 12 princípios](https://www.gamedeveloper.com/production/the-12-principles-of-animation-in-video-games), [Uhiyama Lab](https://uhiyama-lab.com/en/notes/unity/unity-game-feel-hit-feedback/), [Ironsami](https://ironsami-studio.gitbook.io/proceduralhitreactions), [Gameranx](https://gameranx.com/updates/id/474375/article/masahiro-sakurai-reveals-insane-details-put-into-hit-animations-for-smash-bros/).

**Lacunas:** nenhum estudo dá **os graus da cabeça num direto real** a um pugilista vivo nem a curva no tempo (os estudos de boxe usam bonecos e medem acelerações). O único com graus em pessoas é o Pashaei (golpe leve na testa, 100 Hz), por isso os graus do direto são extrapolação. Não encontrei dados do tronco, das ancas nem do peso de quem leva um golpe.

**Sites bloqueados ou que falharam (não contornados):**
- **WebFetch:** continua a não resolver nenhum destes nomes (`pmc.ncbi.nlm.nih.gov`, `wiki.ubc.ca`, `game.capcom.com`, `www.ssbwiki.com`, `europepmc.org`, `bjsm.bmj.com`); com `curl` abriram o wiki da UBC e o SSBWiki. Os outros sites dos excertos (sourcegaming.info, gamedeveloper.com, researchgate.net, ircobi.org, ibrc.osu.edu, biomedcentral.com, bloomberg.com, uhiyama-lab.com, esmed.org, nflps.org) não foram abertos.
- **curl no PMC:** abriu os artigos do Pashaei e do Eckner; numa tentativa deu uma página reCAPTCHA e o PDF do Walilko pede uma "prova de trabalho" anti-robô — não contornei.
- **Segunda ronda (depois de o Tiago autorizar):** `europepmc.org` e `bjsm.bmj.com` respondem com a página de verificação da Cloudflare ("Just a moment…", 403), também depois de esperar ~30 s — não contornei; a API do Europe PMC (`www.ebi.ac.uk`) confirma que o artigo só existe em PDF e o texto XML dá erro 500. `game.capcom.com` responde 503 "MAINTENANCE" (serviço desligado por um problema de segurança no PHP), também depois de esperar. `www.bmj.com` não foi preciso.
