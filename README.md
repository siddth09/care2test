# Care2Test — AI Test Case Generator (Open‑Source PoC)

**One-liner:** Care2Test ingests healthcare requirements (PDF/Word/XML/HL7), extracts atomic requirements, maps them to regulatory clauses, generates structured test cases, and syncs them into test management tools while producing a traceability matrix and evidence pack — all using open-source components.

---

## 🚀 Quickstart

### Prerequisites

* Docker & docker-compose
* Git
* Python 3.10+ (if running without containers)

### Run with Docker Compose

```bash
git clone <repo-url>
cd auto-tc-prototype
cp .env.example .env   # edit with secrets (postgres, minio)
docker-compose up --build
```

Open FastAPI docs at: [http://localhost:8000/docs](http://localhost:8000/docs)

### API Flow

1. Upload an SRS document

   ```bash
   curl -X POST "http://localhost:8000/upload" \
        -F "file=@sample/SRS_sample.pdf"
   ```
2. Generate test cases

   ```bash
   curl -X POST "http://localhost:8000/generate?project=demo&target_alm=testlink"
   ```
3. Check job status

   ```bash
   curl http://localhost:8000/status/{job_id}
   ```
4. Download artifacts

   ```bash
   curl -O http://localhost:8000/artifacts/{job_id}
   ```

---

## 🛠️ Tech Stack (Open‑Source)

* **FastAPI** — API layer
* **Postgres** — metadata store
* **MinIO** — object storage (artifacts, docs)
* **Milvus/FAISS** — vector store for regulatory/RAG
* **Sentence-Transformers** — embeddings
* **Mistral/MPT/LLaMA (HF)** — open-source LLMs for test case generation
* **Haystack / LlamaIndex** — retrieval orchestration
* **Celery / Prefect** — background jobs
* **TestLink / KiwiTCMS** — test management integration
* **Pandoc / ReportLab** — evidence pack generation

---

## 📑 Features

* Upload multi-format docs (PDF, DOCX, XML)
* Automatic parsing + requirement extraction
* Requirement → Test Case generation via LLM + RAG
* Compliance mapping (FDA, IEC 62304, ISO standards)
* Traceability matrix & evidence pack generation
* Integration with open-source ALM/test tools

---

## 🔒 Security & Privacy (GDPR Ready)

* No PHI stored in vector DB (pseudonymize before ingestion)
* Configurable TTL for raw uploads
* Encrypted MinIO buckets
* Role-based access for API
* Local-only inference (no cloud API calls)

---

## 📊 Evaluation Metrics

* Requirement coverage %
* Compliance mapping completeness %
* SME quality score (1–5)
* Cycle time (upload → ALM push)

---

## 📜 License

MIT / Apache-2.0 (pick one)


---

## 📣 Demo 

See walkthrough used in submission.

https://youtu.be/gSKWZw28__Y<img width="460" height="66" alt="image" src="https://github.com/user-attachments/assets/b04d8409-dc82-42d3-95ef-dfafc27bdb74" />

