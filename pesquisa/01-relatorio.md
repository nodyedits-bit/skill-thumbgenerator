# Thumbnails de vídeos de Roblox — relatório de pesquisa

**Data da consulta:** 01/11/2026 · **Idioma do nicho:** PT-BR · **Canal de referência:** Blox (@BL_OX)

Arquivos deste relatório:
- [01-relatorio.md](01-relatorio.md): este arquivo (método, cobertura, comparação, referências, recomendações, checklist, resumo)
- [02-inventario.md](02-inventario.md): tabela com os 57 vídeos (título, data, duração, views, link do vídeo e da imagem)
- [03-auditorias.md](03-auditorias.md): auditoria individual de cada thumbnail

---

## Resumo executivo

**Padrões que aparecem em vários canais (observação, não causa):**
1. **Um assunto dominante grande** (personagem, ovo/pet ou monstro) ocupa de 40% a 70% da imagem em quase todas as thumbnails. Os casos em que o protagonista fica pequeno (REW-9, LAJ-6, ZAP-10) são os menos legíveis no teste em tamanho reduzido.
2. **Pouco texto:** quando há texto, costuma ter de 1 a 3 palavras, letras grossas sem serifa, amarelo ou branco com contorno escuro. Ele quase sempre **recorta ou complementa** o título e raramente o repete inteiro.
3. **Antes/depois em tela dividida** aparece 10 vezes em 4 canais (REW-2, REW-5, LAJ-2, LAJ-3, LAJ-5, LAJ-9, PLAGG-4, PLAGG-6, PLAGG-10, ZAP-1). Sete desses casos estão entre os mais vistos dos canais.
4. **Uma fonte de emoção legível**: um rosto real (GurasBlox), um mascote ilustrado (PlaggXz), um emoji 3D (zapblack) ou um avatar com expressão. Isso compensa o rosto padrão do Roblox, que tem pouca expressão.
5. **Setas vermelhas e símbolos de valor** ("T/s", "0,001%", "TOP 1", Robux) aparecem com frequência nos canais de simuladores (Roube um Ovo).

**Achado específico do canal principal:** os 5 vídeos mais vistos do @BL_OX (jul–set/2025) seguem o mesmo molde: palavra-chave grossa no topo, três personagens em linha e raios no fundo. Os 4 mais recentes (out/2026) mudaram para logo pichado, letras serifadas finas e paletas escuras. **No teste em tamanho reduzido, as letras finas ficaram menos legíveis.** Isso é uma observação. Não é possível concluir que a mudança derrubou as views: os vídeos recentes têm de 1 a 25 dias, os mais vistos têm mais de um ano, e o interesse pelo Forsaken pode ter mudado.

**Hipóteses que vale testar (com "Testar e comparar" do YouTube):**
- H1: no @BL_OX, voltar para letras grossas de 1 a 2 palavras, em vez de serifa fina, mantendo o resto da imagem.
- H2: ampliar o rosto ou a expressão do protagonista (ou adicionar uma camada de emoção, como mascote ou emoji) e comparar com a versão sem esse elemento.
- H3: antes/depois em tela dividida contra uma imagem única, em vídeos de progressão.
- H4: thumbnail sem texto contra texto que complementa o título (e não o repete).

**O que não dá para concluir:** nada sobre CTR, impressões ou causalidade. Esses dados não são públicos, e as views dependem de tema, momento, tamanho do canal, distribuição e título.

---

## 1. Método

1. **Coleta:** usei `yt-dlp` para listar todos os vídeos longos (aba "Vídeos") de cada canal: título, views e duração. Datas e títulos originais em PT-BR vieram do metadado público de cada vídeo. O feed do canal devolvia títulos traduzidos automaticamente para o inglês, então usei sempre o título original.
2. **Amostra por canal:** os 5 mais vistos, os 4 mais recentes e, em 3 canais, o vídeo de menor view entre os 40 mais recentes, para ter um contraste.
3. **Imagens:** baixei `https://i.ytimg.com/vi/<ID>/maxresdefault.jpg` (1280×720) pelo **ID do vídeo**. Isso garante que cada imagem pertence ao vídeo citado. Vi cada imagem em 640×360 e de novo em **164×94 sobre fundo escuro**, para simular a grade do YouTube em modo escuro.
4. **Referências externas:** busquei no YouTube "forsaken roblox", "roube um ovo roblox" e "blue lock rivals roblox". Escolhi 8 vídeos de outros criadores sobre os mesmos jogos.
5. **Separação:** cada auditoria indica o que é observação (Obs.) e o que é hipótese (Hip.).

### Limitações
- **Vídeos não assistidos:** o YouTube exigiu login ("confirm you're not a bot") para reproduzir. Por isso não verifiquei se cada vídeo entrega o que a thumbnail promete.
- **Thumbnail atual ≠ thumbnail histórica:** o criador pode ter trocado a imagem ou usado "Testar e comparar". Só vi a imagem servida em 01/11/2026.
- **Sem dados de CTR, impressões, retenção ou testes A/B.** Esses dados são privados do criador.
- **Idade dos vídeos:** "recentes" têm de horas a semanas de vida, e "top" têm meses ou anos. Comparar views brutas entre eles é enviesado.
- A amostra **não é** uma análise completa: 57 de 1.511 vídeos listados.

## 2. Cobertura

| Canal | Papel | Inscritos (01/11/2026) | Vídeos encontrados (aba Vídeos) | Thumbnails verificadas | Limitações |
|---|---|---|---|---|---|
| [Blox @BL_OX](https://www.youtube.com/@BL_OX) (UC-zTQU9RLXwuxvypj8UMY4Q) | Principal / referência | 97,2 mil | 125 | 9 | vídeos não assistidos |
| [RewtorBlox](https://www.youtube.com/@rewtorblox/videos) | Comparação (Roube um Ovo) | 95,5 mil | 112 | 9 | idem; REW-6 publicado no dia da consulta |
| [GurasBlox](https://www.youtube.com/@GurasBloxx/videos) | Comparação (Roube um Ovo, rosto real) | 278 mil | 135 | 10 | idem; GURAS-10 não é Roblox |
| [LajotaBlox](https://www.youtube.com/@LajotaBlox/videos) | Comparação (desafios/quiz) | 84,1 mil | 240 | 9 | idem |
| [PlaggXz](https://www.youtube.com/@PlaggXz2/videos) | Comparação (mascote ilustrado) | 331 mil | 832 | 10 | idem; amostra pequena em relação ao total |
| [zapblack](https://www.youtube.com/@zapblack1/videos) | Comparação mais próxima (Forsaken, colaborador do BL_OX) | 60,2 mil | 67 | 10 | idem |
| 8 referências externas (seção 4) | Referências semelhantes | — | — | 8 | idem |
| **Total** | | | **1.511** | **65** | Nenhuma imagem inacessível |

## 3. Comparação: mais vistos × recentes × menos vistos

### 3.1 Contagem de elementos (apenas na amostra; observação direta)

| Elemento | Top 5 (30 thumbs) | Recentes (24) | Low (3) |
|---|---|---|---|
| Texto grosso sem serifa curto como elemento de destaque | 25 | 12 | 1 (PLAGG-10) |
| Nenhum texto sobreposto | 2 (PLAGG-2, ZAP-5) | 9 (REW-8, REW-9, LAJ-6, LAJ-7, LAJ-8, PLAGG-7, PLAGG-8, PLAGG-9, ZAP-7) | 1 (ZAP-10) |
| Letras serifadas finas como texto principal | 0 | 2 (BLOX-6, BLOX-8) | 0 |
| Tela dividida antes/depois | 7 (REW-2, REW-5, LAJ-2, LAJ-3, LAJ-5, PLAGG-4, ZAP-1) | 2 (LAJ-9, PLAGG-6) | 1 (PLAGG-10) |
| Rosto real, mascote ilustrado ou emoji 3D | 10 (GURAS-1–5, PLAGG-1/2/3/5, ZAP-5) | 7 (GURAS-6–9, PLAGG-9, ZAP-7, ZAP-8) | 2 (GURAS-10, ZAP-10) |
| Seta vermelha | 10 (REW-1/2/3, GURAS-1/3/4/5, LAJ-4, ZAP-2/5) | 6 (REW-8/9, GURAS-6, PLAGG-9, ZAP-8/9) | 1 (ZAP-10) |

> Contagens feitas visualmente por mim. Servem para descrever a amostra, não para fazer inferência estatística. A diferença de texto entre top e recentes é **dominada por canais específicos**: LajotaBlox e PlaggXz deixaram de usar texto nos vídeos recentes, e o BL_OX trocou o estilo das letras.

### 3.2 Por canal

- **BL_OX:** a mudança de estilo é a mais clara da amostra (seção de resumo). Os vídeos mais vistos têm o molde "palavra-chave + trio de personagens" e são todos de um período de 2 meses de 2025, provavelmente ligado a updates populares do Forsaken (Hip.). Um ponto fraco recorrente, inclusive nos top: os personagens escuros sobre fundo escuro perdem definição em tamanho pequeno.
- **zapblack (mesmo jogo):** usa fundo claro (baseplate) quase sempre, o que dá contraste com killers escuros. Os temas dos top são conceitos extremos e fáceis de visualizar ("24 horas", "invisível", "hack"). Os recentes mantêm o estilo; a diferença de views acompanha a idade e o tema (Hip.).
- **RewtorBlox:** o estilo é estável entre top e recentes (avatar fixo + objeto gigante brilhante). Os top têm conceito narrativo (bug, noob→top, tutorial); os recentes mostram "peguei X raro". Os mais vistos do canal são do mesmo mês (set–out/2026), durante a alta de Roube um Ovo (Hip.).
- **GurasBlox:** o molde é idêntico entre top e recentes (rosto real + pet). O vídeo menos visto é de **outro jogo** (Dtank). Isso sugere que o assunto pesa mais que o estilo da imagem nesse caso (Hip.).
- **LajotaBlox:** os top usam diálogo curto e quadros divididos (quiz). Os recentes não têm texto e mostram cenas cheias. Os temas também mudaram (quiz → tarefas de Halloween), então não dá para separar o efeito do estilo do efeito do tema.
- **PlaggXz:** o mascote ilustrado aparece em todos os top e some na maioria dos recentes. Os top são da era de pico do Blue Lock Rivals (2024–25). Os dois fatores estão misturados.

### 3.3 Padrões recorrentes × isolados

- **Recorrentes (≥3 canais):** assunto grande e central, texto curto e grosso, antes/depois, setas, camada de emoção, números/raridades como "prêmio".
- **Isolados:** rosto real (só GurasBlox), mascote 2D (só PlaggXz), letras serifadas finas (só BL_OX recente), banner de notificação em letra fina (REW-3), cards de item estilo loja (GURAS-2, GURAS-9, LAJ-4, PLAGG-3/5).

### 3.4 Explicações alternativas para as diferenças de views
Idade do vídeo; momento do jogo (updates e hype de Forsaken, Roube um Ovo, Blue Lock Rivals); tamanho do canal (60 mil a 331 mil inscritos); duração (de 8 min a 1h38); título; tema fora do nicho (GURAS-10); colaborações (ZAP-6 com @BL_OX); recomendação algorítmica e sazonalidade (Halloween em out/2026).

## 4. Referências semelhantes (todas vistas diretamente, consulta 01/11/2026)

| # | Criador / vídeo | Views · data | Por que é comparável | Recursos visuais observados | Semelhanças / diferenças | Princípio extraído |
|---|---|---|---|---|---|---|
| R1 | Connor — [I Reached LEVEL 100 With Helperbot! (Forsaken)](https://www.youtube.com/watch?v=Qmw2OR8HYFs) | 71.015 · 27/10/2026 | Mesmo jogo e mesmo tema do BLOX-7/BLOX-8 (Helperbot, level 100) | Ilustração 2D: personagem metade caveira com rosto assustado, Helperbot ao centro com braços verdes, bloco vermelho bravo; logo Forsaken; sem texto | Mesmo tema que o BL_OX, mas emoção desenhada e exagerada | Expressões desenhadas ficam legíveis onde o rosto padrão do Roblox não fica |
| R2 | Jaac — [Forsaken Just Got DISTURBING...](https://www.youtube.com/watch?v=ga2Wq8nQFmA) | 47.825 · 30/10/2026 | Forsaken, update de modelo | "NO WAY..!" branco+vermelho; quadro com modelo antigo; killer vermelho com placa "DIGNITY"; selo "NEW MODEL" | Fundo claro como o do zapblack | Antes/depois de modelo com selo explicativo curto |
| R3 | Lucas Clash ON — [FINALMENTE ENTREI NO TOP DO MUNDO NO ROUBE UM OVO](https://www.youtube.com/watch?v=9SooRRmRqck) | 990.020 · 18/09/2026 | Mesmo jogo do Rewtor/Guras, PT-BR | Rosto real fazendo "shh"; avatares perseguindo; ovo "Divine"; barra de ranking "1 Clashon_Lucas 9T" | Rosto real como no GurasBlox; canal muito maior (7,84 mi) | Ranking em formato de interface comunica status sem frase |
| R4 | Lucas Clash ON — [FINGI SER GAROTA NO ROUBE UM OVO E O RESULTADO...](https://www.youtube.com/watch?v=PFiuUAnT2_c) | 320.110 · 29/10/2026 | Idem | Rosto real tímido com blush desenhado; avatar feminino; balão "<You received a gift🎁>"; "$0" | Mensagem de jogo como texto | Texto diegético (do jogo) cria história |
| R5 | Pabllym GO! — [COMECEI do ZERO com ESTEIRA BROCKODILE ADMIN…](https://www.youtube.com/watch?v=cJ28lddMQZ0) | 141.931 · 31/10/2026 | Roube um Ovo | Avatar estilizado sorrindo; esteira-crocodilo; seta para card "ESTEIRA BROCKODILE x9999 Speed"; "Nível 1" | Card de item como GURAS-2/LAJ-4 | Card de "item cobiçado" + seta |
| R6 | Fer — [ABRI O MELHOR OVO DIVINO NO ADMIN ABUSE…](https://www.youtube.com/watch?v=6lyZe48yRnA) | 86.858 · 31/10/2026 | Roube um Ovo | Ovo gigante vermelho/roxo com brilho e estrelas; "$3.7T/s" com seta; avatar pequeno | Quase idêntico em princípio ao REW-9 | Escala + valor numérico |
| R7 | FoltynPlays — [Pretending To Be A NOOB With The RAREST SKILLS in Blue Lock Rivals..](https://www.youtube.com/watch?v=ME08qxkjFoc) | 1.378.569 · 17/04/2025 | Mesmo jogo do PlaggXz/ZAP-3 (canal em inglês) | Avatar de costas com "ME"; card "Kaiser Equipped"; rival com balão "TRASH NOOB" | Card de equipamento como PLAGG-3; canal de 5,9 mi | Ironia: o espectador sabe algo que o rival não sabe |
| R8 | TheProtagonistBacon — [We're becoming THE NUMBER 1 STRIKER…](https://www.youtube.com/watch?v=5GC5tGKFonA) | 853.985 · 28/09/2025 | Blue Lock Rivals | Avatares em ação em ângulo baixo; bola em primeiro plano; balão "MY BALL!"; coroa | Sem texto grande, só um balão | Ação congelada em perspectiva cria movimento |

Não recomendo reproduzir nenhuma dessas composições. Os princípios estão na última coluna.

## 5. Recomendações práticas

| # | Recomendação | Observação que motivou | Útil para | Status |
|---|---|---|---|---|
| 1 | **Uma ideia visual por thumbnail.** Antes de abrir o editor, escreva a promessa em ≤6 palavras ("noob vira top em 24h"). | Os casos mais legíveis (LAJ-2, REW-2, ZAP-4) têm uma única ideia; os carregados (LAJ-6, REW-3) têm várias | Todos | Apoiada por padrão |
| 2 | **Protagonista ocupando ≥40% da altura**, com contorno claro (2–6 px) se o fundo for escuro. | BLOX-8 e personagens laterais do BLOX-1 somem em mini; ZAP usa fundo claro | Jogos de terror, cenários escuros | Apoiada |
| 3 | **Uma camada de emoção legível**: avatar com expressão, close dramático, ilustração, emoji ou rosto real (se fizer parte da identidade). | GURAS, PLAGG, ZAP, R1 | Reações, opinião, desafios | Hipótese para testar (H2) |
| 4 | **Texto: 0 a 3 palavras, letra grossa, contorno**, que **complemente** o título. | BLOX-6/8 (serifa fina) pouco legíveis; BLOX-7 "CINEMA" completa o título | Todos | Apoiada (legibilidade); efeito em views = hipótese (H1/H4) |
| 5 | **Antes/depois** para progressão (nível, dias, raridade). | 10 ocorrências em 4 canais | "Noob→pro", "dia 1→100", evolução | Padrão recorrente; efeito = H3 |
| 6 | **Contraste por zona**: fundo claro + assunto escuro, ou o contrário; evite escuro sobre escuro. | ZAP (fundo claro com killers escuros) × BLOX recentes | Forsaken e terror | Apoiada |
| 7 | **No máximo 3 elementos principais.** Retire interfaces e textos pequenos que só funcionam em tela grande. | REW-3, REW-4 (placar), GURAS-10, BLOX-9 | Simuladores | Apoiada |
| 8 | **Mostre o jogo ou o contexto** se o título não diz o jogo. | BLOX-2 não tem nenhum sinal do Forsaken | Canais com 1 jogo | Hipótese |
| 9 | **Promessa honesta**: a imagem deve representar algo que acontece no vídeo. | ZAP-7 (ironia) e REW-1 ("BUG" × "mitos") mostram tensão entre imagem e título | Todos | Boa prática (não medido) |
| 10 | **Teste em 160 px e em modo escuro** antes de publicar. | Teste mini deste estudo | Todos | Prática de verificação |

### Checklist antes de publicar
- [ ] Consigo dizer a ideia da thumbnail em ≤6 palavras?
- [ ] Em ~160 px de largura, entendo quem é o protagonista e o que está acontecendo?
- [ ] O protagonista ocupa boa parte da altura e se separa do fundo (contraste ou contorno)?
- [ ] Há uma emoção legível (expressão, pose, símbolo)?
- [ ] Texto: no máximo 3 palavras, letra grossa, legível em tamanho pequeno? Complementa o título em vez de repeti-lo?
- [ ] Nenhum texto, número ou interface importante fica no canto inferior direito, onde fica o selo de duração?
- [ ] No máximo 3 elementos principais e nenhum detalhe decorativo disputando a atenção?
- [ ] O jogo ou o contexto é reconhecível, ou está no título?
- [ ] A imagem mostra algo que realmente acontece no vídeo?
- [ ] Funciona em modo escuro e em modo claro?
- [ ] É original: sem copiar composição, personagem ou identidade de outro criador?
- [ ] Se possível, preparei uma variante para "Testar e comparar"?

## 6. Skill criada
Veja `roblox-thumbnail-analyzer/` na raiz do repositório (detalhes no [README](../README.md)).
