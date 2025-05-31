# memory/memory_store.py

import datetime

# We're using a simple list to simulate a memory system for the app.
# It will store logs of every processed input with some useful metadata.
memory_store = []

def log_to_memory(source, format, intent, extracted_data):
    """
    Save a record of the input that was processed.
    
    Arguments:
    - source: where the input came from (e.g., filename or label)
    - format: type of input (e.g., Email, JSON)
    - intent: what we understood the message to be about
    - extracted_data: details pulled from the input (output of processing)
    
    Adds a new dictionary entry to the shared memory list.
    """
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),  # Add current timestamp
        "source": source,
        "format": format,
        "intent": intent,
        "extracted_data": extracted_data
    }

    # Store this log in memory
    memory_store.append(log_entry)
    
    # Print confirmation to the console for visibility
    print(f"[Memory] Logged: {log_entry}")

def get_memory():
    """
    Retrieve everything we've logged so far.
    Used to review all the data we’ve processed.
    """
    return memory_store