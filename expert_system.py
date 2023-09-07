import streamlit as st

# Define a knowledge base using if-else rules
knowledge_base = [
    {
        "condition": ["Pimpled skin", "Blackheads", "Whiteheads", "Inflammation"],
        "diagnosis": "Acne"
    },
    {
        "condition": ["Red itchy skin", "Inflammation"],
        "diagnosis": "Eczema"
    },
    {
        "condition": ["Red, scaly patches", "Itching", "Silvery scales", "Inflammation"],
        "diagnosis": "Psoriasis"
    },
    {
        "condition": ["Unusual moles", "Changes in existing moles", "Skin lesions", "Bleeding or itching"],
        "diagnosis": "Skin Cancer"
    },
   
    # Add more rules as needed
]

# Define a function to diagnose the disease based on if-else rules
def diagnose(symptoms, knowledge_base):
    for rule in knowledge_base:
        if set(symptoms) == set(rule["condition"]):
            return rule["diagnosis"]
    
    return "Unknown"

# Streamlit app
def main():
    st.title("Medical Diagnosis Expert System")
    
    # Create a list to store up to 5 symptoms
    symptoms = []
    
    # Create input fields for symptoms
    for i in range(5):
        symptom = st.text_input(f"Symptom {i+1}", "")
        if symptom:
            symptoms.append(symptom)
    
    # Add a "Clear" button to clear the input
    if st.button("Clear"):
        symptoms = []

    # Add an "Enter" button to show the diagnosis
    if st.button("Enter"):
        if symptoms:
            possible_diagnosis = diagnose(symptoms, knowledge_base)
            if possible_diagnosis != "Unknown":
                st.success(f"Possible Diagnosis: {possible_diagnosis}")
            else:
                st.warning("No matching diagnoses found.")
        else:
            st.warning("No symptoms entered.")

if __name__ == "__main__":
    main()
