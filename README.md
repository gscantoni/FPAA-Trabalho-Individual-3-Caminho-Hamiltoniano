# FPAA - Trabalho Individual 3 - Caminho Hamiltoniano

##  Objetivo
Implementar um algoritmo em Python para determinar se existe um **Caminho Hamiltoniano** em um grafo orientado ou não orientado, e exibir o caminho, caso exista.

---

##  Como Executar

### 1. Clonar o repositório:
```bash
git clone https://github.com/gscantoni/FPAA-Trabalho-Individual-3-Caminho-Hamiltoniano.git
cd FPAA-Trabalho-Individual-3-Caminho-Hamiltoniano
```

### 2. Executar o programa:
```bash
python main.py
```

### 3. Saída esperada:
```
✅ Caminho Hamiltoniano encontrado:
A → B → C → D
```

---

##  Lógica do Algoritmo

O algoritmo usa **backtracking** para explorar recursivamente todos os possíveis caminhos no grafo até encontrar um que:
- Passe **por todos os vértices exatamente uma vez**.
- Pare assim que encontrar um caminho válido.

---

##  Relatório Técnico

### 🔹 1. Classes de Complexidade
O **Problema do Caminho Hamiltoniano** é **NP-completo**, pois:
- Está em **NP** (uma solução pode ser verificada em tempo polinomial);
- É tão difícil quanto o **Problema do Caixeiro Viajante**, que é NP-completo.

### 🔹 2. Complexidade Assintótica
- **Tempo:** O(n!) — o algoritmo tenta todas as combinações possíveis de vértices.  
- **Espaço:** O(n) — profundidade máxima da pilha de recursão.

### 🔹 3. Teorema Mestre
Não aplicável, pois o algoritmo **não segue uma recorrência recursiva do tipo T(n) = aT(n/b) + f(n)**.  
Ele utiliza **busca exaustiva**.

### 🔹 4. Casos de Complexidade
| Caso | Descrição | Complexidade |
|------|------------|---------------|
| Melhor caso | Caminho encontrado logo na primeira tentativa | O(n) |
| Caso médio | Depende da densidade do grafo | O(k·n!) |
| Pior caso | Nenhum caminho encontrado | O(n!) |

---

## Visualização
Será implementada em `view.py` com **NetworkX** e **Matplotlib**, destacando o Caminho Hamiltoniano encontrado.

---

## Autor
**Guilherme Cantoni**  
Curso: Engenharia de Software  
Disciplina: Fundamentos de Projeto e Análise de Algoritmos  
Professor: João Paulo Carneiro Aramuni
