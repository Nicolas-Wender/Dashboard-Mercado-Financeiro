import streamlit as st
import yfinance as yf
import pandas as pd

indices = {
    "DOLAR": "BRL=X",
    "EURO": "EURBRL=X",
    "BITCOIN": "BTC-USD",
    "IBOVESPA": "^BVSP",
    "S&P 500": "^GSPC",
    "NASDAQ": "^IXIC"
}

historico_indices = {}
cotacao_atual = {}

for nome, ticker in indices.items():
    dados = yf.Ticker(ticker).history(period="40d")[["Close"]]

    dados = dados.reset_index()
    dados["Date"] = dados["Date"].dt.strftime('%Y-%m-%d')
    dados.set_index("Date", inplace=True)

    historico_indices[nome] = dados.rename(columns={"Close": nome})

    cotacao_atual[nome] = {}
    cotacao_atual[nome]["atual"] = round(dados.iloc[-1, 0], 2)
    cotacao_atual[nome]["ontem"] = round(dados.iloc[-2, 0], 2)
    cotacao_atual[nome]["comparacao"] = round(
        ((dados.iloc[-1, 0] / dados.iloc[-2, 0]) - 1)*100, 2)

df_historico = pd.concat(historico_indices.values(), axis=1, join="outer")
df_historico.ffill(inplace=True)
df_historico.dropna(inplace=True)

st.title("📈 Dashboard Mercado Financeiro")
st.write(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt"
)

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Dolar",
              value=f"R$ {round(cotacao_atual['DOLAR']['atual'],2)}", delta=cotacao_atual['DOLAR']["comparacao"])

    st.metric(label="Ibovespa",
              value=f"{round(cotacao_atual['IBOVESPA']['atual'],2)} pts", delta=cotacao_atual['IBOVESPA']["comparacao"])


with col2:
    st.metric(label="Euro",
              value=f"R$ {round(cotacao_atual['EURO']['atual'],2)}", delta=cotacao_atual['EURO']["comparacao"])

    st.metric(label="S&P 500",
              value=f"{round(cotacao_atual['S&P 500']['atual'],2)} pts", delta=cotacao_atual['S&P 500']["comparacao"])


with col3:
    st.metric(label="Bitcoin",
              value=f"R$ {round(cotacao_atual['BITCOIN']['atual'],2)}", delta=cotacao_atual['BITCOIN']["comparacao"])

    st.metric(label="NASDAQ",
              value=f"{round(cotacao_atual['NASDAQ']['atual'],2)} pts", delta=cotacao_atual['NASDAQ']["comparacao"])
