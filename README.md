# Finance Data Processing & Access Control Backend

### 👤 Candidate Information
- **Name:** Anchal Patel
- **Email:** anchal6392patel@gmail.com
- **Role:** Backend Developer Intern (Assignment)

---

## 🚀 Project Overview
This project is a specialized finance dashboard backend built with **FastAPI**. It handles financial transaction processing, user role simulation, and real-time data aggregation for a dashboard interface.

### Key Features
- **Financial CRUD:** Create, Read, Update, and Delete financial entries (Amount, Type, Category, Date).
- **Dashboard Analytics:** Automated calculation of Total Income, Total Expenses, and Net Balance.
- **Access Control:** Logic structured to support Role-Based Access Control (RBAC) with specific permissions for Admins, Analysts, and Viewers.
- **Interactive UI:** Built-in frontend to test API endpoints directly from the dashboard.

---

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, Uvicorn
- **Data Modeling:** Pydantic (Validation)
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API)
- **Environment:** Google Colab / GitHub

---

## 📖 How to Run

### Using Google Colab (Recommended)
1. Open the `.ipynb` file in Google Colab.
2. Run the installation cell for dependencies (`fastapi`, `uvicorn`, `nest_asyncio`).
3. Run the main code cell to start the background server and display the UI.
4. Use the "Add Record" form to test live data updates.

---

## 📝 Assumptions & Logic
- **Data Persistence:** Uses an in-memory dictionary for rapid prototyping.
- **Authentication:** Mocked using custom headers (`x-user-id`) to demonstrate role-based behavior.
- **Validation:** Pydantic models ensure all inputs (amounts, types) meet strict format requirements before processing.

---
*© 2026 Anchal Patel | Prepared for Zorvyn FinTech Pvt. Ltd.*
[main.py](https://github.com/user-attachments/files/26431563/main.py)
