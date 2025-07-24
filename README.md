# 🔐 ReBAC Policy Rule Extractor – Frontend

This repository contains the **frontend web app** built using **Streamlit** for uploading ReBAC-formatted datasets, triggering model training, and viewing extracted access control rules.

🌐 **Live App Hosted on Render**  
You can deploy this frontend on [Render](https://render.com/) or run it locally. The app reads the backend API URL from `st.secrets`, making it deployment-friendly.

## 🚀 Features

- 📤 Upload CSV file with ReBAC-style features
- 🤖 Trigger backend API to train a Decision Tree model
- 📜 Display human-readable policy rules
- 🚨 Show false positives (when access is wrongly allowed)

## 🏗️ Project Structure

```
rebac-frontend/
├── app.py               # Streamlit app interface
├── requirements.txt     # Python dependencies
```

## 🔧 Setup Instructions

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Streamlit secrets

Create a file at `.streamlit/secrets.toml`:

```toml
[general]
API_URL = "https://your-backend-api.onrender.com"  # Replace with actual Render backend URL
```

## ▶️ Run the App

```bash
streamlit run app.py
```

## 🧪 Sample Dataset Format

```csv
User_A, User_B, Relation, Resource, Access
1, 0, 1, 0, Yes
0, 1, 0, 1, No
```

- `Access` must be either `Yes` or `No`
- All other columns should be binary (0/1)

## 🛰️ Deployment on Render (Optional)

To deploy this app on Render:
1. Connect your GitHub repo to [Render.com](https://render.com)
2. Choose **Web Service** > **Python**
3. Set the start command to:

```bash
streamlit run app.py --server.port=10000 --server.enableCORS=false
```

4. Add your `API_URL` in Render’s **Environment → Secret Files** under `.streamlit/secrets.toml`

## 📬 Backend Required

Make sure to deploy or run [`rebac-backend`](https://github.com/your-user/rebac-backend) before using this frontend.

## 👤 Author

Developed by **Ruthik Chitti** under academic guidance.
