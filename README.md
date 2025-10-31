# Harness CI Demo — Python (FastAPI)

This is a simple Python **FastAPI** web application designed to demonstrate a **Harness CI Cloud pipeline**.

The pipeline performs the following:
1. **Builds** the Python application from source.
2. **Runs unit tests** using `pytest`.
3. **Builds and pushes** a Docker image to DockerHub.

---

## 🧩 Project Structure
harness-ci-demo/
├── app/
│   └── main.py            # FastAPI application
├── tests/
│   └── test_app.py        # Unit tests for endpoints
├── requirements.txt        # Dependencies
├── Dockerfile              # Image build instructions
├── .harness/pipeline.yaml  # Harness CI pipeline configuration
└── README.md               # Documentation (this file)
---

## 🧪 Run Locally

To run this project locally:

```bash
# 1. Create a virtual environment
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run tests
pytest -q

# 4. Start the server
uvicorn app.main:app --reload
