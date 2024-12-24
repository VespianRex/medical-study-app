## Project Overview
This project aims to create a medical study app that generates flashcards and other study materials from uploaded documents. The app will use a combination of frontend and backend technologies to provide a user-friendly and efficient learning experience.

## Key Components and Their Interactions
- **Frontend**: Built with Vue.js, ShadCN, and Vite, the frontend provides the user interface for uploading documents, viewing flashcards, and interacting with the knowledge graph.
- **Backend**: Built with Python, FastAPI, and Celery, the backend handles document processing, NLP tasks, flashcard generation, and data storage.
- **Data Storage**: PostgreSQL, MongoDB (if needed), and Neo4j are used for storing relational data, unstructured data, and knowledge graph data, respectively.
- **API**: RESTful APIs and GraphQL endpoints are used for communication between the frontend and backend.

## Data Flow
1. Users upload documents via the frontend.
2. The backend processes the documents using OCR and NLP tools.
3. Key terms and concepts are extracted and stored in the database.
4. Flashcards and knowledge graphs are generated based on the extracted data.
5. Users interact with the generated content via the frontend.

## External Dependencies
- **OCR Tools**: MinerU, Surya, Microsoft Kosmos
- **NLP Libraries**: spaCy, ScispaCy, Romanian language models
- **Language Models**: GPT-4, local Romanian LLMs
- **Vector Databases**: FAISS or Pinecone
- **Graph Databases**: Neo4j
- **Frontend Libraries**: Vue.js, ShadCN, Vite, D3.js or Cytoscape.js
- **Backend Libraries**: FastAPI, Celery, Drizzle ORM
- **Monitoring and Logging**: Prometheus, Grafana, ELK Stack or Loki

## Recent Significant Changes
- Initial project setup and documentation.
- Created `frontend` and `backend` directories.
- Created `frontend/index.html` and `backend/main.py` files.
- Created `backend/requirements.txt` file.
- Installed backend dependencies using `pip install -r requirements.txt`.
- Created `backend/.env` file.
- Added a basic Celery task to `backend/main.py`.
- Added a `/upload` endpoint to `backend/main.py` to handle file uploads.
- Created `docker-compose.yml` file.
- Created `backend/Dockerfile`.

## User Feedback Integration and Its Impact on Development
- User feedback will be collected and used to refine the app's features and improve its accuracy.

## Additional Documents
- `styleAesthetic.md` (future document for style guidelines)
- `wireframes.md` (future document for UI wireframes)
- `testCases.md` (future document for test cases)