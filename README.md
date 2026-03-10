# 🕷️ Simple Python Web Crawler

Um **web crawler simples em Python** que percorre páginas da web coletando links e navegando automaticamente por eles.

O script começa a partir de uma URL inicial e continua explorando novos links encontrados nas páginas visitadas.

---

## 🚀 Funcionalidades

* Faz requisições HTTP para páginas web
* Extrai links (`<a href="">`) do HTML
* Filtra apenas links absolutos (`http/https`)
* Evita visitar o mesmo link duas vezes
* Continua navegando automaticamente até não encontrar novos links

---

## 🧰 Tecnologias utilizadas

* **Python 3**
* **requests**
* **BeautifulSoup4**

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

Instale as dependências:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Como usar

Execute o script passando uma URL inicial:

```bash
python crawler.py https://example.com
```

O crawler irá:

1. Acessar a página inicial
2. Extrair todos os links encontrados
3. Adicionar novos links à fila de exploração
4. Continuar até que não existam mais links para visitar

Exemplo de saída:

```
Crawling https://example.com
Crawling https://example.com/about
Crawling https://example.com/contact
Done
```

---

## 🧠 Como funciona

O crawler usa duas estruturas principais:

* **TO_CRAWL (lista)** → URLs que ainda serão visitadas
* **CRAWLED (set)** → URLs que já foram visitadas

Fluxo do programa:

1. Adiciona a URL inicial à lista `TO_CRAWL`
2. Remove uma URL da lista
3. Faz a requisição da página
4. Extrai os links encontrados
5. Adiciona novos links à lista
6. Marca a página como visitada

---

## 📂 Estrutura do código

```
project/
│
├─ crawler.py
└─ README.md
```

---

## ⚠️ Observações

Este projeto é um **crawler educacional** e não possui:

* controle de profundidade
* limite de páginas
* tratamento avançado de erros
* respeito ao `robots.txt`

Use com responsabilidade para não sobrecarregar sites.

---

## 📜 Licença

Este projeto pode ser usado livremente para **estudos e aprendizado**.
