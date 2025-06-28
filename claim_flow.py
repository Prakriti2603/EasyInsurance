import streamlit as st

# Simple session-based claim handler
def handle_claim_flow(user_input):
    if "claim_data" not in st.session_state:
        st.session_state.claim_data = {
            "description": "",
            "date": "",
            "location": "",
            "injury": ""
        }

    claim = st.session_state.claim_data

    # Fill data step-by-step
    if not claim["description"]:
        claim["description"] = user_input
        return "Got it. When did the incident happen? (e.g., 26 June 2025)"
    
    elif not claim["date"]:
        claim["date"] = user_input
        return "Thanks. Where did it occur?"

    elif not claim["location"]:
        claim["location"] = user_input
        return "Understood. Was anyone injured? (Yes/No)"

    elif not claim["injury"]:
        claim["injury"] = user_input
        return generate_claim_summary(claim)
    
    else:
        return "Your claim summary is already complete!"

# Generates the claim summary nicely formatted
def generate_claim_summary(claim):
    summary = f"""
### 📝 Claim Summary
- **Description**: {claim['description']}
- **Date of Incident**: {claim['date']}
- **Location**: {claim['location']}
- **Injury**: {claim['injury']}

✅ This draft is ready to review or submit.
"""
    return summary
