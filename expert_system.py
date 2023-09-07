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
    
    # Create a dropdown list of predefined symptoms
    predefined_symptoms = [
        "Pimpled skin", "Blackheads", "Whiteheads", "Inflammation",
        "Red itchy skin", "Red, scaly patches", "Silvery scales",
        "Unusual moles", "Changes in existing moles", "Skin lesions",
        "Bleeding or itching", "Others"
    ]
    
    selected_symptom = st.selectbox("Select a symptom:", predefined_symptoms)
    
    # Allow users to enter custom symptoms
    if selected_symptom == "Others":
        custom_symptom = st.text_input("Enter custom symptom:", "")
        if custom_symptom:
            symptoms.append(custom_symptom)
    else:
        symptoms.append(selected_symptom)
    
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
