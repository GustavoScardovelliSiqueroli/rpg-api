# 🖥️ Jogo: Sobreviva ao Escritório

Um RPG estilo dungeon em que você é um funcionário tentando apenas... **sobreviver ao escritório**. O jogo é infinito, baseado em decisões, aleatoriedade e eventos cotidianos transformados em desafios.

---

## 🎯 Objetivo

Viver mais um dia de trabalho sem ser demitido.  
Melhorar seu personagem, acumular itens e sobreviver aos absurdos da vida corporativa.

---

## ⏰ Estrutura do Dia

- Cada ação consome **1 hora**
- Um dia tem **8 horas**
- Após o 8º turno, o dia **acaba** e começa um novo dia (0h)
- Só é possível **comprar** no fim do dia
- No fim do dia recupera energia
- No fim da semana ganha salario

---

## 🧍‍♂️ Jogador

### Atributos
- **Produtividade**: capacidade de resolver desafios (ataque)
- **Energia**: quanto você aguenta antes de precisar descansar

### Recursos
- **Dinheiro**: ganho por trabalhar, usado para compras pessoais
- **Network**: moeda mais rara, trocada por vantagens corporativas (ex: plano de saúde, cargos, aumentos)

### Inventário
- **Mochila** com itens acumulados

---

## 🛍️ Sistema de Compras

### Com Dinheiro
> Usado no fim do dia
- Roupas novas
- Canetas
- Café especial
- Lanches

### Com Network
> Compras mais “corporativas”
- Cargo melhorado
- Impressora infinita
- Cartão VIP do café
- Plano de saúde
- Sala privada
- Benefícios passivos

---

## 🎒 Exemplos de Itens

| Item       | Efeito                                      | Restrição               |
|------------|---------------------------------------------|-------------------------|
| Cigarro    | Recupera energia ou aumenta produtividade   | Usável apenas no fumódromo |
| Copo       | Usado para beber café                       | Precisa ir até a Sala do Café |
| Papel      | Necessário para imprimir documentos         | Usável na Sala da Impressora |
|Papel preenchido| Chance de aliviar evento | Precisa de papel + impressora |

---

## 🗺️ Tipos de Sala

| Sala            | Descrição                                                  |
|------------------|------------------------------------------------------------|
| RH               | Quase sempre algo ruim acontece                           |
| Café             | Recupera energia                                           |
| Sala do Chefe    | Eventos difíceis, alto risco e alto retorno               |
| Fumódromo        | Recupera energia ou dá buffs (chance de evento negativo)  |
| Impressora       | Gera papel, pode quebrar                                  |
| Sala de Trabalho | Gera dinheiro, produtividade, eventos médios              |

---

## 📅 Eventos

Exemplos aleatórios que podem acontecer ao entrar em salas:

- Alguém roubou seu cigarro no fumódromo
- Foi dispensado mais cedo (ganha tempo)
- Te passaram uma tarefa enorme e inútil
- Impressora engasgou com papel
- Chefe pediu ideia nova na hora

---

## ⚔️ Sistema de Combate / Desafio

Ao entrar numa sala:

1. Um evento é disparado
2. O evento tem uma **complexidade** (ex: 10)
3. Você enfrenta com:
   - Sua **produtividade**
   - + bônus de itens/buffs
4. Resultado:
   - Se vencer: ganha energia, network, dinheiro, itens, etc.
   - Se falhar: perde energia, pode perder itens ou receber punições

### Exemplo

> Evento: "Apresente uma ideia nova ao chefe"  
> Complexidade: 10  
> Produtividade: 7  
> Bônus: +3 (item + café)  
> Resultado: Sucesso → +5 network, +10 dinheiro

---

## 💤 Descanso

- Se ficar com **energia 0**, você não pode agir
- É necessário **esperar 1 hora real** para regenerar um pouco de energia
- Após isso, o jogador pode voltar ao jogo normalmente

---

## ♾️ Progresso

- O jogo **não tem fim**
- O personagem acumula itens, network, buffs e histórico
- Pode regredir se ignorar descanso, gastar tudo, ser punido

---

## 🔄 Possíveis Extensões Futuras

- Buffs e debuffs temporários
- Itens raros com efeitos passivos
- Eventos semanais (como auditoria, visita do CEO)
- Sistema de reputação

