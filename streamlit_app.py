import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/generate_roadmap"

st.set_page_config(page_title="AI Learning Roadmap Generator", page_icon="🧠")

st.title("🧠 Personalized Learning Roadmap Generator")
st.markdown("Enter a topic you're interested in, and get a structured roadmap with curated resources.")

topic = st.text_input("Enter a topic you're interested in ")

if st.button("Generate Roadmap"):
    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating Roadmap..."):
            try:
                response = requests.post(API_URL, json={"topic": topic})
                response.raise_for_status()
                data = response.json()

                st.success(f"Roadmap for: **{data['topic']}**")
                st.markdown(f"**Estimated Time**: {data['estimated_time']}")

                st.markdown("### ✅ Prerequisites")
                for pre in data['prerequisites']:
                    st.markdown(f"- {pre}")

                st.markdown("### 🎯 Roadmap Milestones")
                for i, item in enumerate(data['roadmap_milestones'], start=1):
                    st.markdown(f"**{i}. {item['milestone']}**")
                    st.markdown(f"> {item['description']}")
                    st.markdown("**Resources:**")
                    for res in item['resources']:
                        st.markdown(f"- [{res}]({res})")

            except requests.exceptions.RequestException as e:
                st.error("Something went wrong. Please try again.")
                st.error(e)


