# agents/classifier_agent.py

class ClassifierAgent:
    def _init_(self, memory):
        """
        Initialize the ClassifierAgent with a memory object.

        Args:
            memory: An object responsible for logging and storing data.
        """
        self.memory = memory

    def classify(self, input_data):
        """
        Analyze the input data to identify its format and the user's intent.

        This function checks whether the input is a JSON dictionary,
        an email text (detected by presence of 'From:' at start),
        or a filename ending with '.pdf' to mark as PDF.

        It then tries to classify the intent by searching for key terms
        like 'invoice' or 'rfq' within the input text.

        Args:
            input_data: The raw input which can be a dict (JSON), string (email content or file name).

        Returns:
            A tuple of two strings:
            - format_type: 'JSON', 'Email', 'PDF', or 'Unknown'
            - intent: 'Invoice', 'RFQ', or 'Unknown'
        """
        try:
            # Detect input format
            if isinstance(input_data, dict):
                format_type = "JSON"  # Input is JSON data
            elif isinstance(input_data, str) and input_data.strip().startswith("From:"):
                format_type = "Email"  # Input looks like an email text
            elif isinstance(input_data, str) and input_data.endswith(".pdf"):
                format_type = "PDF"  # Input is a PDF filename
            else:
                format_type = "Unknown"  # Format could not be identified

            # Initialize intent as Unknown
            intent = "Unknown"

            # Simple keyword matching for intent detection
            # Convert input to lowercase for case-insensitive matching
            lowered_input = input_data.lower() if isinstance(input_data, str) else ""

            if "invoice" in lowered_input:
                intent = "Invoice"
            elif "rfq" in lowered_input:
                intent = "RFQ"

            # Log the detected format and intent into memory for tracking
            self.memory.log({"format": format_type, "intent": intent})

            # Return the results
            return format_type, intent

        except Exception as e:
            # Catch any unexpected errors during classification
            print(f"[Classifier] Error in classification: {e}")
            # Return Unknown if classification fails
            return "Unknown", "Unknown"