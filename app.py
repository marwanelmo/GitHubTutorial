import streamlit as st
import openai
import key

openai.api_key = key.key
print(key.key)



# Add a dropdown menu to the sidebar
menu = st.sidebar.selectbox("Select functionality:", ["Write report", "Simplify text", "Find ICD Code"])

if menu == "Write report":
    # Display a text area for the user to enter short sentences about the patient
    text_input = st.text_area("Enter short sentences about the patient:")
    button = st.button("Create report")

    if button:
        # Call the GPT-3 API to create a structured report from the input text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Please create a bulletpoint list report from the following text: {text_input}",
            max_tokens=250,
            n=1,
            temperature=0.5,
        )
        report = response["choices"][0]["text"]
        st.write(report)
        
        # Save the report to a file
        with open("report.txt", "w") as f:
            f.write(report)
            
        # Display a success message
        st.success("Report successfully created and saved to a file!")
        
elif menu == "Simplify text":
    st.write("""
    The simplification feature is a tool that allows users to take complex or technical text and convert it into simpler, easier-to-understand language. This feature could be especially useful for healthcare organizations, as it could help them to communicate with patients or clients who may not have a medical background or who may have difficulty understanding medical terminology.

    To use the simplification feature, users would enter the text that they want to simplify into a text box. The feature could then use natural language processing (NLP) algorithms and machine learning techniques to analyze the text and identify complex or technical words or phrases. It could then replace those words or phrases with simpler alternatives, or provide definitions or explanations of the terms to help users understand the content more easily.

    The simplification feature could also include options to customize the level of simplification, such as by specifying a target reading level or age group. This could allow users to tailor the level of simplification to the needs of their audience.
    """)
    # Display a text area and a button to simplify the text
    text_input = st.text_area("Enter complex medical language:")
    button = st.button("Simplify text")

    if button:
        # Call the GPT-3 API to simplify the text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Please simplify the following text to a level that a 12 year old can understand: {text_input}",
            max_tokens=50,
            n=1,
            temperature=0.5,
        )
        simplified_text = response["choices"][0]["text"]
        st.write("Simplified text:", simplified_text)
        
        # Save the simplified text to a file
        with open("simplified_text.txt", "w") as f:
            f.write(simplified_text)
            
        # Display a success message
        st.success("Text successfully simplified and saved to a file!")
elif menu == "Find ICD Code":
    st.write("""
    ICD codes (International Classification of Diseases codes) are codes that are used to classify and describe medical diagnoses and procedures. They are used by healthcare providers, insurance companies, and other organizations to record and track medical information.
    
    A "find ICD code" feature could be a tool that allows users to search for the appropriate ICD code for a specific diagnosis or procedure. The feature could allow users to enter the name of the diagnosis or procedure, and it could use a database of ICD codes to provide the corresponding code. This could be especially useful for healthcare providers, who may need to accurately record and report ICD codes for billing and documentation purposes.
    
    The feature could also include additional functionality, such as the ability to browse through the full list of ICD codes, view the definitions and descriptions of each code, or search for codes based on keywords or other criteria.
    """)
    text_input = st.text_area("Enter Patient Scenario:")
    button = st.button("Find ICD")

    if button:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Give me a list of ICD codes with an explanation corresponding to the following medical scenario: {text_input}",
            max_tokens=50,
            n=1,
            temperature=0.5
        )
        icdtext = response["choices"][0]["text"]
        st.write("ICD codes:", icdtext)

