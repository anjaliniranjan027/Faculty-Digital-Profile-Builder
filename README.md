# Faculty-Digital-Profile-Builder

# 👩‍🏫 Faculty Digital Profile Builder (RAG-Based)

A smart system to automatically generate structured faculty profiles from uploaded documents using IBM Granite LLM and Streamlit.

---

## 📌 Problem Statement

Faculty members across higher education institutions are often required to maintain detailed academic profiles for accreditation (NAAC, NBA), research collaborations, promotions, and institutional visibility. 

However, manually creating and updating these profiles from various documents—CVs, research papers, certificates, and spreadsheets—is time-consuming and prone to errors. There is no simple or intelligent system to handle this automatically.

---

## ✅ Proposed Solution

This project aims to build a simple AI-powered tool that allows faculty to upload their resume or document (PDF). The system processes the file using IBM Granite foundation model and extracts important academic details such as:

- Name & contact
- Education history
- Experience
- Skills
- Research interests
- Publications (if any)

The information is presented in a clean, structured profile format that can be viewed or copied for reporting and documentation.

---

## 🧰 Tech Stack

| Technology      | Purpose                          |
|-----------------|----------------------------------|
| **Python 3.10** | Core backend logic               |
| **Streamlit**   | Web UI for user interaction      |
| **IBM Granite** | LLM to extract & structure data  |
| **dotenv**      | Manage environment variables     |
| **Virtualenv**  | Manage isolated dependencies     |

---

## 🗂️ Folder Structure

faculty_profile_builder/
│
├── app.py # Main Streamlit app
├── granite_api.py # API integration with IBM Granite
├── sample_resume.pdf # Test input document
├── .env # Environment credentials (API key etc.)
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## ⚙️ System Requirements

- Python 3.10
- IBM Cloud Lite Account
- Virtual Environment (venv)
- Web browser (Chrome, Firefox)
- IBM `ibm-watson-machine-learning` Python SDK

---

## ▶️ How to Run

1. Clone the repository:

2. Create and activate a virtual environment:

3. Install dependencies:

5. Run the app:

---

## 🏁 Conclusion

This project demonstrates a basic use-case of integrating LLMs with simple interfaces to solve real-world academic problems. It helps save time and improve accuracy in generating faculty records.

---

## 🔮 Future Scope

This system is a prototype and has limitations. It can be improved in the following ways:

- Support for DOCX, scanned PDFs
- Better JSON parsing with error handling
- Profile editing or download options
- Adding vector search to retrieve past records (RAG fully)
- Multi-language document support

---

## 📚 References

- [IBM Granite Foundation Models](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-lifecycle.html)
- [Streamlit Docs](https://docs.streamlit.io)
- [IBM Watson Machine Learning SDK](https://pypi.org/project/ibm-watson-machine-learning/)


 


