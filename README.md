## WhatsApp Product Reviews App

### A full-stack application that allows users to submit product reviews via WhatsApp. The backend processes WhatsApp messages, stores reviews in PostgreSQL, and exposes a REST API consumed by a React frontend.


## 🛠 Tech Stack

### Backend

**FastAPI** - Python web framework

**PostgreSQL** - Database

**SQLAlchemy** - ORM

**Twilio** - WhatsApp integration

**Uvicorn** - ASGI server

### Frontend

**React** - Frontend framework

**Vite** - Build tool

**CSS3** - Styling



## Installation & Setup


### Clone the Repository

 git clone <your-repo-url>
 cd whatsapp-reviews-app

### Backend Setup

 Navigate to backend directory:

 cd backend
 Create and activate virtual environment:

**Create virtual environment**
 python3 -m venv venv

**Activate virtual environment**

 source venv/bin/activate


## Install Python dependencies:

 pip install fastapi uvicorn sqlalchemy psycopg2-binary python-multipart twilio
 Set up PostgreSQL Database:
 Start PostgreSQL service:

### Start the Backend Server:

 uvicorn main:app --reload --host 0.0.0.0 --port 8001
 The backend will be available at: http://localhost:8001


### Frontend Setup

Open a new terminal and navigate to frontend directory:

cd frontend

### Install dependencies:

 npm install

 npm run dev


