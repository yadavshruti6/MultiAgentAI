# Multi-Agent AI System
A Modular Multi-Agent AI System to Intelligently Classify and Extract Information from Diverse Input Formats like Email, JSON, and PDF.

- About This Project

This project is a simple yet powerful Multi-Agent AI system that can handle inputs in different formats like *PDF, **JSON, or **Email*. It intelligently classifies the input type and the user's intent—whether it's an Invoice, Request for Quote (RFQ), Complaint, or something else—and then routes the information to the right agent for processing.

The system also keeps a shared memory, so agents can remember important details like who sent the message, what it was about, and when it was received. This helps in maintaining context and allows the agents to work together smoothly.

## What You’ll Find Here

- *Classifier Agent:* The brain that decides what the input is and where it should go.
- *JSON Agent:* Handles structured data from JSON files, cleans it up, and checks for missing information.
- *Email Agent:* Reads emails, picks out sender info, urgency, and intent, and formats it nicely.
- *Shared Memory:* Keeps track of all the important info so nothing gets lost between agents.

## Technologies Used

- Python 3.x (main programming language)
- OpenAI or open-source Large Language Models for natural language processing
- Redis or SQLite for fast and easy shared memory storage
- Libraries for reading PDFs, parsing JSON, and processing emails

## How This Project Is Organized

multi_agent_ai_system/ │ ├── agents/                # All the agents live here │   ├── classifier_agent.py │   ├── email_agent.py │   └── json_agent.py │ ├── memory/                # Shared memory module │   └── memory_store.py │ ├── sample_inputs/         # Example files for testing │   ├── sample_email.txt │   ├── sample_invoice.json │   └── sample_invoice.pdf │ ├── outputs/               # Logs and processed output stored here │ ├── utils/                 # Helper functions used throughout │   └── helper_functions.py │ ├── main.py                # Entry point to run the system └── README.md

## How to Run This Project

1. First, clone this repo:

```bash
git clone https://github.com/yadavshruti6/multi_agent_ai_system.git
cd multi_agent_ai_system

2. Set up a virtual environment and install the dependencies:



python -m venv .venv
source .venv/bin/activate      # On Linux or macOS
.venv\Scripts\activate         # On Windows
pip install -r requirements.txt

3. Run the system with your input file:



python main.py --input sample_inputs/sample_email.txt

You can replace the input file with any sample JSON or PDF to see how it works.

Sample Output

Here is an example of what the output looks like after processing an email:

{
  "format": "Email",
  "intent": "RFQ",
  "extracted_data": {
    "sender": "shruti@company.com",
    "urgency": "High",
    "formatted_for_crm": true,
    "original_content": "Request for Quote email content here..."
  }
}


About Me

I am Shruti Yadav, an Electronics and Communication Engineering student at IIIT Kota. I am passionate about AI and full-stack development, and this project is a reflection of my enthusiasm for building smart systems that can automate and simplify real-world tasks.

Feel free to reach out to me at shrutiyadav7533@gmail.com or visit my GitHub profile yadavshruti6.