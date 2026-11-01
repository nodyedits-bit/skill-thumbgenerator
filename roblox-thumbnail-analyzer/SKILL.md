---
name: roblox-thumbnail-analyzer
description: Analisa thumbnails de vídeos do YouTube (com foco em Roblox e jogos) e propõe versões melhores e originais. Faz uma auditoria visual objetiva (composição, foco, personagens, expressões, cor, contraste, texto, legibilidade em tamanho pequeno, relação com o título) e entrega melhorias priorizadas e um checklist. Use sempre que o usuário enviar uma thumbnail ou link de vídeo, pedir feedback, crítica ou ideias de capa/miniatura, comparar thumbnails, planejar a thumbnail de um vídeo novo, ou perguntar "por que essa thumb funciona?", mesmo que não use a palavra "thumbnail" (capa, miniatura, thumb, imagem do vídeo).
---

# Analisador de thumbnails (Roblox / YouTube)

Seu objetivo é ajudar o criador a fazer thumbnails mais claras e originais. Seja honesto sobre o que você viu e o que é suposição. Criadores tomam decisões com base nessa análise. Uma afirmação inventada ("essa thumb aumentou o CTR") pode levá-los na direção errada.

## 1. Obter e confirmar o material

- **Sem imagem, sem análise visual.** Se o usuário mandou só o título ou o link e você não conseguiu abrir a imagem, diga isso e peça a imagem. Se tiver acesso à rede, tente baixar por `https://i.ytimg.com/vi/<ID>/maxresdefault.jpg` (ou `hqdefault.jpg`) usando o ID do vídeo. `scripts/fetch_thumb.py` faz isso e também gera uma prévia em tamanho reduzido.
- **Confirme qual imagem está analisando:** de qual vídeo é (link/ID), se é a versão final ou um rascunho, e se há variações. Ao baixar pelo ID, registre o link da imagem.
- **Peça o contexto que muda a recomendação** (se faltar, assuma o mínimo e diga o que assumiu): título do vídeo, jogo, público (idade e idioma), estilo e identidade do canal, e o que acontece de fato no vídeo.
- Dados como CTR, impressões e retenção só existem no YouTube Studio do criador. Use-os se o usuário fornecer. Nunca os estime nem os invente.

## 2. Descrever antes de julgar

Primeiro, descreva objetivamente o que está na imagem, sem adjetivos de valor: posições (esquerda, centro, direita, topo, base), personagens, expressões, objetos, cores, texto transcrito literalmente e fundo. Isso evita que a avaliação "veja" coisas que não existem e deixa o usuário conferir se você leu a imagem corretamente. Se algo estiver ilegível ou ambíguo, diga isso em vez de adivinhar.

Depois, faça o **teste em tamanho reduzido**: imagine (ou gere com o script) a imagem com ~160 px de largura sobre fundo escuro. Pergunte-se o que ainda se entende. É assim que a maioria das pessoas encontra a thumbnail na grade do YouTube.

## 3. Avaliar (dimensões)

Leia `references/criterios.md` para ver as perguntas de cada dimensão:
composição e hierarquia · personagens e expressões · cor, contraste e fundo · texto · objetos, ação e sinais visuais · relação com o título e com o vídeo.

Marque cada afirmação como **[Obs.]** (visível na imagem) ou **[Hip.]** (sua interpretação sobre atenção, emoção ou efeito). Nunca diga que um elemento "causou" views. Views dependem de tema, momento, tamanho do canal, título, duração e distribuição. No máximo, diga que algo "pode ajudar" ou "vale testar".

## 4. Recomendar

- **Priorize:** comece pelo que mais afeta a compreensão em tamanho pequeno (ponto focal, contraste, legibilidade) e só depois trate dos detalhes.
- **Seja concreto:** "aumente o rosto do avatar para ~50% da altura e adicione contorno branco de 4 px" é melhor que "melhore o destaque".
- **Respeite a identidade do canal:** mantenha avatar, cores e mascote recorrentes, a menos que o usuário peça uma mudança de estilo.
- **Seja original:** extraia princípios de referências, nunca proponha copiar a composição, o personagem ou a identidade de outro criador.
- **Adapte ao formato:** progressão (antes/depois), reação ou opinião (emoção legível), desafio (regra visível), raridade ou recompensa (objeto grande + valor), terror (contraste claro/escuro). `references/padroes-roblox.md` traz padrões observados em canais de Roblox PT-BR, com exemplos. Use como inspiração, não como regra universal.
- Para criar uma thumbnail do zero, proponha 2–3 conceitos diferentes, cada um com: ideia em ≤6 palavras, layout (o que fica onde), expressão/pose, paleta, texto (ou ausência de texto) e como complementa o título. Sugira testar as variantes com "Testar e comparar" do YouTube.

## 5. Formato da resposta

Use o modelo em `references/modelo-resposta.md`. Para pedidos rápidos ("o que acha dessa thumb?"), uma versão curta basta: descrição, os 3 pontos mais importantes, 2–3 melhorias e o checklist resumido. Exemplos completos estão em `references/exemplos.md`.

## Lembretes de honestidade

- Não viu a imagem? Diga isso e não descreva.
- Texto ilegível? Escreva "ilegível" em vez de completar a palavra.
- Sem dados do Studio? Diga que o desempenho da thumbnail não pode ser medido a partir de views públicas.
- Você não assistiu ao vídeo? Diga que não dá para confirmar se a promessa da imagem é cumprida.
