import streamlit as st

st.set_page_config(page_title="Aula: Estruturas de Controle", layout="centered")

st.title("🧠 Aula Interativa: Estruturas de Controle em Python")

aba = st.sidebar.radio(
    "Tópicos",
    [
        "Introdução",
        "Condicional: if / elif / else",
        "Repetição: for",
        "Repetição: while",
        "Operadores Lógicos",
        "Desafio Final",
    ],
)

if aba == "Introdução":
    st.header("📌 O que são estruturas de controle?")
    st.markdown(
        """
    São instruções que **controlam o fluxo** da execução de um programa.
    
    Existem dois grandes grupos:
    - **Condicionais**: fazem decisões (`if`, `elif`, `else`)
    - **Repetições**: repetem blocos de código (`for`, `while`)
    """
    )

elif aba == "Condicional: if / elif / else":
    st.header("✅ Condicional: if / elif / else")

    st.markdown(
        """
    Vamos ver um exemplo simples: verificação de idade.
    """
    )

    idade = st.number_input("Digite sua idade:", 0, 150, 18)

    st.code(
        """
if idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")
    """
    )

    if idade < 12:
        st.success("Você é uma criança.")
    elif idade < 18:
        st.warning("Você é um adolescente.")
    else:
        st.info("Você é um adulto.")

elif aba == "Repetição: for":
    st.header("🔁 Estrutura de repetição: for")

    n = st.slider("Escolha um número inteiro:", 1, 20, 5)
    st.code(
        f"""
for i in range({n}):
    print(i)
    """
    )

    st.markdown("Resultado:")
    with st.expander("Executar"):
        for i in range(n):
            st.write(i)

elif aba == "Repetição: while":
    st.header("🔄 Estrutura de repetição: while")

    limite = st.slider("Valor máximo (while < limite)", 1, 20, 5)

    st.code(
        f"""
i = 0
while i < {limite}:
    print(i)
    i += 1
    """
    )

    st.markdown("Resultado:")
    with st.expander("Executar"):
        i = 0
        while i < limite:
            st.write(i)
            i += 1

elif aba == "Operadores Lógicos":
    st.header("🔗 Operadores lógicos")

    st.markdown(
        """
    Usamos operadores lógicos para combinar condições:
    
    - `and`: e
    - `or`: ou
    - `not`: não

    Exemplo:
    ```python
    if idade > 18 and tem_carteira:
        print("Pode dirigir.")
    ```
    """
    )

    idade = st.number_input("Idade", 0, 100, 20, key="idade_logica")
    tem_carteira = st.checkbox("Tem carteira de motorista?")

    if idade >= 18 and tem_carteira:
        st.success("Pode dirigir.")
    else:
        st.error("Não pode dirigir.")

elif aba == "Desafio Final":
    st.header("🚀 Desafio Final")

    st.markdown(
        """
    Faça um programa que receba um número e diga se ele é **par ou ímpar**, e também **positivo, negativo ou zero**.
    """
    )

    num = st.number_input("Digite um número", value=0)

    st.code(
        """
if num % 2 == 0:
    print("Par")
else:
    print("Ímpar")

if num > 0:
    print("Positivo")
elif num < 0:
    print("Negativo")
else:
    print("Zero")
    """
    )

    if num % 2 == 0:
        st.write("🔵 Par")
    else:
        st.write("🟠 Ímpar")

    if num > 0:
        st.write("🟢 Positivo")
    elif num < 0:
        st.write("🔴 Negativo")
    else:
        st.write("⚪ Zero")
