# Business Contract Validation Tool

This project is a Streamlit application for highlighting contracts and performing Named Entity Recognition (NER). The application classifies content within contract clauses, determines deviations from a template, and highlights them.

## Features
- Automated extraction and classification of contract clauses.
- Highlighting key entities such as dates, parties, and legal terms.
- Identifying deviations from standard contract templates.
- Providing a summarized view of the contract content.
- Download options for highlighted contracts as HTML.

## Technologies Used
- Streamlit: For the interactive web application.
- PyMuPDF: For PDF text extraction.
- Transformers (Huggingface): For Named Entity Recognition (NER).
- difflib: For comparing contract texts.

## Installation

### Prerequisites
- Python 3.7 or higher
- Git

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/Rohan-bit-coder/Business-Contract-Validation.git
    cd Business-Contract-Validation
    ```

2. Create a virtual environment and activate it:
    - **Windows**:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - **macOS/Linux**:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run contractapp.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.
## Project Structure
## Project Structure

```plaintext
Business-Contract-Validation/
├── contractapp.py
├── generate.py
├── requirements.txt
├── README.md
├── contracts/
│   ├── contract_1.txt
│   ├── contract_2.txt
│   ├── contract_3.txt
│   ├── contract_4.txt
└── Demonstration



