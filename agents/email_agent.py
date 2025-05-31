# agents/email_agent.py

def process_email(content):
    """
    Process the raw email content to extract key information
    like sender, intent, and urgency. Returns a formatted dict
    suitable for further use (e.g., CRM systems).

    Args:
        content (str): The full raw text content of the email.

    Returns:
        dict: Extracted and formatted email information.
    """
    # Extract the sender's email address from the content
    sender = extract_sender(content)
    
    # Determine the intent (purpose) of the email, e.g., Invoice or RFQ
    intent = extract_intent(content)
    
    # Determine urgency based on keywords like 'urgent' or 'ASAP'
    urgency = extract_urgency(content)

    # Format the extracted data in a dictionary with extra info
    formatted = {
        "sender": sender,
        "intent": intent,
        "urgency": urgency,
        "formatted_for_crm": True,  # Mark as ready for CRM import
        "original_content": content  # Keep original email text for reference
    }
    
    # Debug print to verify processed email details
    print(f"[Email Agent] Processed email: {formatted}")
    
    # Return the formatted dictionary
    return formatted


def extract_sender(content):
    """
    Extract the sender email address by scanning for a line
    starting with 'From:'.

    Args:
        content (str): Email raw text.

    Returns:
        str: Extracted sender email or 'Unknown Sender' if not found.
    """
    # Split content into lines and look for 'From:' line
    for line in content.split('\n'):
        if line.lower().startswith("from:"):
            # Extract and return email after the colon, strip spaces
            return line.split(":", 1)[1].strip()
    
    # Return fallback if sender not found
    return "Unknown Sender"


def extract_intent(content):
    """
    Identify the intent of the email based on keywords.

    Args:
        content (str): Email raw text.

    Returns:
        str: Intent label like 'Invoice', 'RFQ', 'Complaint', or 'General'.
    """
    content = content.lower()
    
    # Check for common keywords to classify intent
    if "invoice" in content:
        return "Invoice"
    elif "rfq" in content or "request for quote" in content:
        return "RFQ"
    elif "complaint" in content:
        return "Complaint"
    else:
        # Default if no keywords matched
        return "General"


def extract_urgency(content):
    """
    Determine the urgency level of the email.

    Args:
        content (str): Email raw text.

    Returns:
        str: 'High' if urgent keywords found, else 'Normal'.
    """
    content = content.lower()
    
    # Look for urgency-related keywords
    if "urgent" in content or "asap" in content:
        return "High"
    else:
        return "Normal"