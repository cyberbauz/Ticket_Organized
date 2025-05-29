import streamlit as st
import datetime
import re

st.set_page_config(page_title="IT Ticket Note Organizer", layout="centered")

st.title("🛠️ IT Ticket Note Organizer")
st.markdown("Paste your raw notes below and get a clean, structured ticket summary.")

raw_notes = st.text_area("Enter raw ticket notes:", height=250)

def organize_notes(raw):
    steps = re.split(r"\.|\n", raw)
    steps = [step.strip() for step in steps if step.strip()]

    organized = f"""
**🗓️ Date:** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}

**📝 Issue Summary:** [To be filled or extracted]

**🔧 Steps Taken:**
"""
    for step in steps:
        organized += f"- {step}\n"

    organized += """
**📌 Root Cause:** [Add if known]  
**✅ Resolution:** [Summarize the fix]  
**📞 Follow-Up:** [Mention if user was advised or issue to monitor]  
"""
    return organized

if st.button("Organize Notes"):
    if raw_notes.strip() == "":
        st.warning("Please enter some notes first.")
    else:
        st.subheader("🧾 Organized Ticket Summary")
        st.text_area("Formatted Notes:", organize_notes(raw_notes), height=300)
