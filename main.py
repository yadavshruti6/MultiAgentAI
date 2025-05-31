# Developed by Shruti Yadav
# GitHub: https://github.com/yadavshruti6
# Email: shrutiyadav7533@gmail.com

from utils.file_reader import read_file
from memory.memory_store import log_to_memory, get_memory
from agents.email_agent import process_email
from agents.json_agent import process_json

def classify_input(input_data):
    """
    Try to guess the type of input (Email, JSON, or Text)
    and figure out what the input is about (intent).
    """
    if isinstance(input_data, dict):
        # Input is a dictionary, likely JSON
        return "JSON", input_data.get("intent", "Unknown")
    elif isinstance(input_data, str):
        # If it looks like an email based on text patterns
        if "@gmail.com" in input_data or "From:" in input_data:
            # Just a rough way to detect if it's a Request for Quote
            return "Email", "RFQ" if "RFQ" in input_data.upper() else "Unknown"
        else:
            return "Text", "Unknown"
    else:
        # Couldn't recognize the input type
        return "Unknown", "Unknown"

def main():
    """
    This is the core function that:
    1. Reads an email text file and processes it.
    2. Uses a hardcoded JSON sample and processes it.
    3. Logs the results to memory.
    4. Prints the full memory log.
    """

    # --- Process Email Sample ---

    # Read sample email content from file
    email_text = read_file("sample_inputs/sample_email.txt")

    # Determine format and intent for the email
    fmt, intent = classify_input(email_text)
    print(f"\nDetected Format: {fmt}, Intent: {intent}")

    # If it's an email, run it through the email processing logic
    if fmt == "Email":
        output = process_email(email_text)
        log_to_memory("sample_email.txt", fmt, intent, output)

    # --- Process JSON Sample ---

    # Define a fake JSON message (simulates an incoming data packet)
    sample_json = {
        "id": "INV-0023",
        "sender": "client@company.com",
        "intent": "Invoice",
        "content": "Please process attached invoice."
    }

    # Detect format and intent for the JSON sample
    fmt, intent = classify_input(sample_json)
    print(f"\nDetected Format: {fmt}, Intent: {intent}")

    # If it's JSON, run the JSON processor
    if fmt == "JSON":
        output = process_json(sample_json)
        log_to_memory("sample_json", fmt, intent, output)

    # --- Review Memory Log ---

    # Finally, print everything logged so far
    print("\nFinal Memory Log:")
    for entry in get_memory():
        print(entry)

# Standard entry point to run the program
if __name__ == "__main__":
    main()