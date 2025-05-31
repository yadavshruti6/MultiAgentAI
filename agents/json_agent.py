# agents/json_agent.py

def process_json(json_data):
    """
    Process incoming JSON data to check for required fields,
    report any missing fields, and then reformat it into a
    standard schema for further processing.

    Args:
        json_data (dict): Raw JSON data input.

    Returns:
        dict: Reformatted JSON with status information.
    """
    # List of fields that must be present in the input JSON
    required_fields = ["id", "sender", "intent", "content"]
    missing = []  # To keep track of any missing required fields

    # Check if each required field exists in the input JSON
    for field in required_fields:
        if field not in json_data:
            missing.append(field)  # Record missing field names

    # If some fields are missing, print a warning with details
    if missing:
        print(f"[JSON Agent] Missing fields: {missing}")

    # Create a new dictionary with standardized keys,
    # using .get() to safely access values with defaults
    formatted = {
        "identifier": json_data.get("id", "unknown"),
        "source": json_data.get("sender", "unknown"),
        "purpose": json_data.get("intent", "unknown"),
        "body": json_data.get("content", ""),
        # Add a status message depending on missing fields
        "status": "Processed with warnings" if missing else "Processed"
    }

    # Debug output showing the processed and formatted JSON data
    print(f"[JSON Agent] Processed JSON: {formatted}")
    
    # Return the cleaned, standardized dictionary for next steps
    return formatted