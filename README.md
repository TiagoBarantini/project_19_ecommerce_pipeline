# 🚀 E-commerce Data Pipeline

Projeto de Engenharia de Dados simulando um pipeline completo de e-commerce, desde a ingestão de dados até a visualização em BI.

---

## 📊 Arquitetura

O projeto segue o modelo de camadas:

- **Bronze**: ingestão de dados brutos via API  
- **Silver**: tratamento e padronização dos dados  
- **Gold**: modelagem dimensional para análise  

Modelo final:
- `fato_vendas`
- `dim_produto`

---

## 🛠️ Tecnologias Utilizadas

- Apache Airflow (orquestração)
- PostgreSQL (armazenamento)
- Docker (ambiente)
- Power BI (visualização - DirectQuery)
- Python (ETL)

---

## 🔄 Pipeline de Dados

1. Coleta de dados via API (Fake Store API)
2. Armazenamento na camada Bronze
3. Transformações na camada Silver
4. Modelagem na camada Gold
5. Consumo via Power BI

---

## 📈 Modelagem de Dados

### Tabela fato
- `fato_vendas`
  - produto_id
  - quantidade
  - data_venda

### Tabela dimensão
- `dim_produto`
  - id
  - nome
  - categoria
  - preco

---

## 📊 Dashboard (Power BI)

Conectado via **DirectQuery**, permitindo análise em tempo real.

Principais métricas:
- Total de vendas
- Ticket médio
- Receita
- Ranking de produtos
- Evolução de vendas ao longo do tempo

---

## 🚀 Como Executar o Projeto

### 1. Clonar repositório
```bash
git clone git@github.com:TiagoBarantini/project_19_ecommerce_pipeline.git
cd project_19_ecommerce_pipeline
```

### 2. Configurar variáveis de ambiente

Criar arquivo `.env`:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=******
POSTGRES_DB=ecommerce
POSTGRES_HOST=postgres
POSTGRES_PORT=5432
```

### 3. Subir containers
```bash
docker-compose up -d
```

### 4. Acessar Airflow
http://localhost:8080

### 5. Executar DAGs
- Bronze
- Silver
- Gold

### 6. Conectar no Power BI

Servidor:
IP_DA_VM:5433

Banco:
ecommerce

Modo:
DirectQuery

---

## 🔍 Exemplos de Queries

### Top produtos mais vendidos
```sql
SELECT 
    d.nome,
    SUM(f.quantidade) AS total_vendido
FROM fato_vendas f
JOIN dim_produto d ON f.produto_id = d.id
GROUP BY d.nome
ORDER BY total_vendido DESC
LIMIT 5;
```

---

## 💡 Diferenciais do Projeto

- Pipeline completo (end-to-end)
- Modelagem dimensional (Star Schema)
- Orquestração com Airflow
- Integração com BI em tempo real (DirectQuery)
- Uso de boas práticas (variáveis de ambiente, Docker)

---

## 📌 Próximos Passos

- Criar dimensão de tempo (`dim_tempo`)
- Adicionar mais fontes de dados (APIs externas)
- Implementar testes de qualidade de dados
- Deploy em ambiente cloud

---

## 👨‍💻 Autor

Tiago Barantini
