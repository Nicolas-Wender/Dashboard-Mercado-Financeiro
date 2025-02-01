import yfinance as yf
import pandas as pd

indices = {
    "DOLAR": "BRL=X",
    "BITCOIN": "BTC-USD",
    "EURO": "EURBRL=X",
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
