# Pesquisa: Boxing Gym Story → ideias para o Corner Men (nov 2026)

Três análises feitas por agentes (wiki da Kairosoft, Steam, vaporlens, App Store, capturas do Tiago). **Ideias originais adaptadas — nunca copiar a arte, o aspeto, os nomes ou a interface do Boxing Gym Story.** Ainda nada disto está decidido.

## 1. Gestão (o que não está a ser divertido)

**Diagnóstico do Corner Men:**
- A semana é um ciclo de janelas puxado por um botão: aviso de "plano por rever" todas as semanas, mesmo sem nada mudar; relatório grande em texto; depois negociações/talentos. Com 1 atleta e nada novo: 3–6 toques por semana, 6–8 vezes iguais entre lutas.
- Poucos eventos com escolha (só talento e aumento); patrocinadores são só uma fórmula; não há imprensa, visitas, rivais com cara.
- As recompensas são números em texto (+0,4 Força) que não se sentem.
- O ginásio animado não é interativo e não mostra o treino a acontecer.
- Não há objetivos curtos; a loja esgota-se cedo; o dinheiro acumula.

**Lições do Boxing Gym Story:** o tempo corre sozinho (sem botão "avançar"); há sempre uma contagem visível (próxima luta, estação, prémio); cada luta dá várias recompensas; decisões poucas mas frequentes e curtas (1 toque); o ginásio cresce à vista. Críticas dos jogadores: repetitivo, avanço rápido bloqueado, demasiados toques, reformas forçadas.

**Propostas (prioridade):**
1. Tempo a correr sozinho com ▶/❚❚ e ×2 (uma semana ≈ 20–30 s); pausa automática quando chega um cartão ou uma luta. (L)
2. O plano é uma ordem permanente; só se revê quando há motivo (fadiga alta, golpe aprendido, decadência a chegar, luta perto). (S)
3. Relatório da semana como aviso curto de 1–3 linhas em vez de janela. (S)
4. Treino visível no ginásio: o atleta vai ao equipamento, aparecem "+FOR", "aprendeu o 2!", o treinador comenta. (M)
5. Cartões de evento com 2–3 escolhas (~1–2 por semana): patrocinador, jornalista, atleta quer folga, rival provoca, miúdo quer experimentar, senhorio sobe a renda, susto de lesão — o resultado depende dos mentais. (M)
6. Preparação da luta com fases e marcos (vídeo do adversário, conferência de imprensa, pesagem). (M)
7. Álbum de momentos (primeiro KO, counter que derruba, fígado, reviravolta, título). (M)
8. Prémio da primeira vitória contra cada academia/adversário (escolher 1 de 3). (S)
9. Quadro com 3 objetivos curtos com prémio. (S)
10. Ginásio que cresce à vista + mais coisas para comprar + noite de luta organizada pelo ginásio. (M–L)
11. Sócios como personagens; mini-competições sazonais; reformados como treinadores. (M)

## 2. O ginásio como mapa

**Hoje:** o canvas do ginásio (240×136, escala 1,5×) ocupa ~27% do ecrã e não reage a toques; o resto são tabelas e listas (Ginásio, Atletas, Lutas, Loja).

**Proposta "O Armazém" (estilo próprio):** um só piso de armazém em vista elevada (a mesma ideia de projeção da arena), canvas vertical ~192×300 a 2× exato, rua em baixo. Zonas tocáveis:

| Zona | Toque | Substitui |
|---|---|---|
| Balneário (cacifos com nomes) | lista de atletas → Ficha | ATLETAS |
| Quadro de treino | planos da semana | Plano |
| Escritório (telefone + secretária) | telefone com "!" = propostas; secretária = finanças | LUTAS, contas |
| Placard de cortiça | diário e histórico | Diário |
| Ringue | sparring, melhoria do ringue | parte da Loja |
| Lugares vazios de equipamento (contorno a giz com preço) | comprar | Loja → Equipamento |
| Banco dos treinadores ("procura-se") | contratar | Loja → Staff |
| Porta da rua | visitas e eventos entram por aqui | eventos da semana |
| Calendário / cartaz | contagem para a próxima luta | — |
| Qualquer pessoa | mini-ficha com [FICHA] [PLANO] | — |

Ícones sobre as pessoas em vez de badges ("?" plano, "zZ" lesionado, gotas = cansado, "+€" na porta). HUD mínimo em cima (dinheiro · semana · popularidade · próxima luta) e barra em baixo ([≡ LISTA] [▶] [❚❚]). **LISTA** sempre disponível com os painéis atuais (acessibilidade). Zonas trancadas visíveis com tábuas ("Abre no nível 2"); se o mapa crescer, deslizar só o mapa (nunca menus) ou botões de piso.

## 3. As lutas

**Hoje, o que já é bom:** vista elevada, 4 pavilhões, público, árbitro com poses, equipa no canto, entrada com roupão, zoom em golpes limpos, contagem, letreiros grandes, toalha, confetis e cinturão, cordas/canto, pernas bambas, barra de distância, indicador "A OUVIR".

**O que falta:** mesa dos juízes, locutor de ringue, equipa de TV/fotógrafos, ecrã gigante, treinador a abrir as cordas, árbitro a chamar ao centro e dar início, animação de levantar depois da queda, plano largo → aproximação no 1.º gongo, pop-ups no ringue, números nas barras, proteção de cabeça no amador, segunda voz.

**O que está pior:** o Zé do Micro fala demais (~57 sítios no código chamam `say`; uma troca pode gerar 4–5 linhas; o registo passa mais depressa do que se lê); o retrato grande ocupa ~30% da largura; as defesas e os counters só existem em texto.

**Propostas (prioridade):**
1. Duas vozes: o **locutor** (Zé do Micro) com frases curtas; um **comentador** novo (ex-pugilista) com 1–2 observações por round ("está a perder pernas"). Fila com prioridades: o importante passa sempre, o rotineiro raramente. O registo completo fica só para a análise. (M)
2. Cabine pequena: 1 linha + cara pequena de quem fala; o espaço ganho vai para o ringue. (M)
3. Pop-ups no ringue, na cor do canto: "1-2-3", "PÊNDULO", "COUNTER!", "FÍGADO!" (no máx. 2 de cada vez). (M)
4. As ordens do canto em balão sobre o treinador; "OUVIU!" sobre o atleta. (S)
5. HUD legível: números nas barras, estratégia por extenso, placar sem tapar os lutadores. (S)
6. Animação de levantar (chão → joelho → cordas → guarda; árbitro verifica). (M)
7. Locutor de ringue de smoking e árbitro a dar início ("BOXE!"). (M)
8. Plano largo na entrada → aproximação suave no 1.º gongo; câmara que acompanha. (M)
9. Proteção de cabeça no amador → cartão "LICENÇA PRO" na primeira luta profissional. (S visual; regra de jogo só com decisão do Tiago)
10. Pessoal à volta do ringue (juízes, cronometrista, câmara de TV, fotógrafos). (M)
11. Ecrã gigante a partir do Regional, com repetição curta e estatísticas entre rounds. (L)
12. Chips de momento ("RITMO ▲", "PERNAS ▼") por palavras. (M)

**Originalidade:** manter a vista frontal elevada própria do Corner Men (passar a um losango isométrico seria reescrever tudo e pareceria cópia); cores, letras e ícones próprios.
