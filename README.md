# AI Knowledge Graph Builder for Enterprise Intelligence

## 📖 Project Overview
This project builds an enterprise-level Knowledge Graph from structured and unstructured customer support data.

The system extracts entities and relationships from support tickets and constructs a scalable knowledge graph for enterprise intelligence and analysis.

### Technologies Used
- Python
- Pandas
- Ollama (Mistral LLM)
- Neo4j Graph Database
- Flask
- GitHub

---

# 🎯 Objective

To transform enterprise support ticket data into a scalable knowledge graph that enables relationship-based analysis, issue tracking, and intelligent insights.

---

# 🏗 Project Architecture

Raw Dataset  
→ Data Cleaning (Pandas)  
→ Structured Triple Extraction  
→ LLM-based Entity Extraction (Ollama + Mistral)  
→ Merge Structured + LLM Triples  
→ Neo4j Graph Construction  
→ Graph Validation

---

# ✅ Milestone 1 – Data Ingestion & Preprocessing

### Tasks Completed
- Data cleaning using Pandas
- Removal of null values and duplicates
- Data normalization
- Feature enrichment
- Processed dataset generation

### Output

```
cleaned_tickets.xlsx
```

---

# ✅ Milestone 2 – Entity Extraction & Graph Construction

## Step 1: Structured Triple Extraction

Extracted entity–relationship–entity triples from structured columns.

Example triples:

```
Customer → RAISED → Ticket
Ticket → HAS_SEVERITY → Severity
Ticket → SUBMITTED_VIA → Channel
```

Output:

```
structured_triples.csv
```

---

## Step 2: LLM-Based NER (Ollama + Mistral)

Used Mistral LLM to extract semantic relationships from ticket descriptions.

Example triples:

```
(Dell XPS, EXPERIENCING, Not turning on)
(Dell XPS, REQUIRED_ACTION, Troubleshoot power issues)
```

Output:

```
llm_triples.csv
```

---

## Step 3: Graph Construction (Neo4j)

- Combined structured and LLM-generated triples
- Inserted triples into Neo4j using the Python Neo4j driver
- Constructed graph nodes and relationships

Graph Statistics:

```
Nodes: 162
Relationships: 244
```

---

## Step 4: Graph Validation

Validated graph integrity using Cypher queries.

### Count Nodes

```cypher
MATCH (n)
RETURN count(n);
```

### Count Relationships

```cypher
MATCH ()-[r]->()
RETURN count(r);
```

### Visualize Graph

```cypher
MATCH (n)-[r]->(m)
RETURN n,r,m
LIMIT 25;
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/AI-Knowledge-Graph-Builder.git
cd AI-Knowledge-Graph-Builder
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install pandas ollama neo4j flask openpyxl
```

---

# 🤖 LLM Setup (Ollama)

Install Ollama and pull the Mistral model.

```bash
ollama pull mistral
```

This model is used for entity extraction from ticket descriptions.

---

# 🧠 Neo4j Setup

1. Install **Neo4j Desktop**
2. Create a local database
3. Start the database

Connection details:

```
bolt://localhost:7687
username: neo4j
password: <your-password>
```

Insert triples into Neo4j:

```bash
python scripts/push_to_neo4j.py
```

---

# 📁 Project Structure

```
AI-Knowledge-Graph-Builder
│
├── app
│   └── app.py
│
├── data
│   ├── raw
│   │   └── tickets.xlsx
│   │
│   └── processed
│       ├── cleaned_tickets.xlsx
│       ├── structured_triples.csv
│       ├── llm_triples.csv
│       └── final_triples.csv
│
├── notebooks
│   └── milestone2_llm_extraction.ipynb
│
├── scripts
│   └── push_to_neo4j.py
│
└── README.md
```

---

# 📊 Current Status

```
Milestone 1 ✅ Completed
Milestone 2 ✅ Completed
Milestone 3 🔜 Upcoming
```

---

# 📌 Future Work

- Advanced graph analytics
- Knowledge graph querying
- Graph visualization dashboards
- Integration with enterprise AI applications