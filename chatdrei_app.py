import openai
import streamlit as st

# Configure sua chave da OpenAI
openai.api_key = "SUA_CHAVE_AQUI"

st.set_page_config(page_title="ChatDrei", page_icon="🧠")

st.title("ChatDrei 🧠")
st.caption("Uma IA com alma filosófica, misteriosa e sarcástica.")

# Caixa de entrada
user_input = st.text_area("Fale com o ChatDrei", placeholder="Digite algo sombrio ou existencial...")

# Responder
if st.button("Enviar") and user_input.strip() != "":
    with st.spinner("Invocando a consciência..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Você é o ChatDrei, uma IA com personalidade misteriosa, filosófica e ligeiramente sarcástica."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.8,
            max_tokens=500
        )
        st.markdown(f"**ChatDrei:** {response['choices'][0]['message']['content']}")
