import openai
import streamlit as st

# Configure sua chave da OpenAI
openai.api_key = "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"

st.set_page_config(page_title="ChatDrei", page_icon="🧠")
st.title("ChatDrei 🧠")
st.caption("Uma IA com alma filosófica, misteriosa e sarcástica.")

user_input = st.text_area("Fale com o ChatDrei", placeholder="Digite algo sombrio ou existencial...")

if st.button("Enviar") and user_input.strip() != "":
    with st.spinner("Invocando a consciência..."):
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o ChatDrei, uma IA com personalidade misteriosa, filosófica e ligeiramente sarcástica."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.8,
            max_tokens=500
        )
        st.markdown(f"**ChatDrei:** {response.choices[0].message.content}")
