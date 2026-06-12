
def base_response(intent):
    responses = {
        "Academic": "This is an academic explanation of the topic.",
        "Technical": "Here is a technical breakdown of the problem.",
        "Entertainment": "This is meant to entertain you.",
        "Personal": "I understand how you feel.",
        "General": "Here is the information you requested."
    }
    return responses.get(intent, "I'm not sure how to respond to that.")