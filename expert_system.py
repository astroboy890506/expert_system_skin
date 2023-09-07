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
    
    # Create a list to store selected symptoms
    selected_symptoms = []
    
    # Create a multiselect widget with predefined symptoms
    predefined_symptoms = [
        "Pimpled skin", "Blackheads", "Whiteheads", "Inflammation",
        "Red itchy skin", "Red, scaly patches", "Silvery scales",
        "Unusual moles", "Changes in existing moles", "Skin lesions",
        "Bleeding or itching"
    ]
    
    selected_symptoms = st.multiselect("Select symptoms:", predefined_symptoms)
    
    # Create a space for layout adjustment
    st.write("")  # Add an empty space for separation
    
    # Create a container for the "Enter" and "Clear" buttons with custom CSS
    button_container = st.empty()
    button_container.markdown(
        """
        <style>
        .st-cc {
            display: flex;
            justify-content: space-between;
        }
        </style>
        """
    )

    # Add an "Enter" button and a "Clear" button to the container
    if button_container.button("Enter"):
        if selected_symptoms:
            possible_diagnosis = diagnose(selected_symptoms, knowledge_base)
            if possible_diagnosis != "Unknown":
                # Increase the font size of the diagnosis using CSS styling
                st.markdown(f"<h2 style='text-align: center;'>Possible Diagnosis: {possible_diagnosis}</h2>", unsafe_allow_html=True)
            else:
                st.warning("No matching diagnoses found.")
        else:
            st.warning("No symptoms selected.")

    # Clear the selected symptoms when the "Clear" button is clicked
    if button_container.button("Clear"):
        selected_symptoms = []

if __name__ == "__main__":
    main()
