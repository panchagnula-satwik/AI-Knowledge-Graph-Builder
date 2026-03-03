# AI Knowledge Graph Builder for Enterprise Intelligence

## 📖 Project Overview
This project builds an enterprise-level Knowledge Graph from structured and unstructured customer support data.

It uses:
- Python (Pandas)
- LLM-based NER (Ollama + Mistral)
- Neo4j Graph Database

---

## ✅ Milestone 1 – Data Ingestion & Preprocessing

### Tasks Completed:
- Data cleaning using Pandas
- Removal of null values and duplicates
- Data normalization
- Feature enrichment
- Saved processed dataset

### Output:
- `cleaned_tickets.xlsx`

---

## ✅ Milestone 2 – Entity Extraction & Graph Construction

### Step 1: Structured Triple Extraction
Extracted entity–relationship–entity triples from structured columns:
- Customer → RAISED → Ticket
- Ticket → HAS_SEVERITY → Severity
- Ticket → SUBMITTED_VIA → Channel

Output:
- `structured_triples.csv`

---

### Step 2: LLM-Based NER (Ollama + Mistral)

Used Mistral LLM to extract semantic triples from ticket descriptions:

Example:
(Dell XPS, EXPERIENCING, Not turning on)
(Dell XPS, REQUIRED_ACTION, Troubleshoot power issues)


Output:
- `llm_triples.csv`

---

### Step 3: Graph Construction (Neo4j)

- Merged structured + LLM triples
- Inserted into Neo4j using Python driver
- Constructed graph with:
  - 162 Nodes
  - 211 Relationships
- Validated graph visually in Neo4j Browser

Final Output:
- `final_triples.csv`
- Neo4j Knowledge Graph

---

## 🏗 Architecture

Raw Dataset  
→ Data Cleaning (Pandas)  
→ Structured Triples  
→ LLM Extraction (Ollama)  
→ Merge Triples  
→ Neo4j Graph Construction  

---

## 🚀 Technologies Used

- Python
- Pandas
- Ollama (Mistral LLM)
- Neo4j
- GitHub

---

## 📊 Current Status

Milestone 1 ✅ Completed  
Milestone 2 ✅ Completed  
Milestone 3 🔜 Upcoming