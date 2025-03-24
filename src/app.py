import streamlit as st
import pandas as pd
from validator import validate_dataframe, AdData

st.set_page_config(page_title="Validador de Dados", layout="wide")
st.title("📊 Validação de Planilha com Pydantic")

uploaded_file = st.file_uploader("📤 Faça upload do arquivo CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("Prévia dos dados:", df.head())

        with st.spinner("Validando os dados..."):
            valid, invalid = validate_dataframe(df)

        st.subheader("✅ Registros válidos")
        st.write(f"{len(valid)} linhas válidas")

        if valid:
            df_valid = pd.DataFrame([v.model_dump() for v in valid])

            csv_valid = df_valid.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Baixar registros válidos em CSV",
                data=csv_valid,
                file_name="registros_validos.csv",
                mime="text/csv",
            )

        st.subheader("❌ Registros inválidos")
        st.write(f"{len(invalid)} linhas com erro")

        if invalid:
            erros_formatados = [
                {
                    "Index": i,
                    "Error": e,
                    **r  # expande os campos da linha original
                } for i, r, e in invalid
            ]
            df_invalid = pd.DataFrame(erros_formatados)

            csv_invalid = df_invalid.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="⬇️ Baixar registros inválidos em CSV",
                data=csv_invalid,
                file_name="registros_invalidos.csv",
                mime="text/csv",
            )

            st.dataframe(df_invalid)

    except Exception as e:
        st.error(f"Erro ao processar o arquivo: {e}")