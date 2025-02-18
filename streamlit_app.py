import streamlit as st
import yfinance as yf
import pandas as pd
from streamlit_echarts import st_echarts

indices = {
    "DOLAR": "BRL=X",
    "EURO": "EURBRL=X",
    "BITCOIN": "BTC-USD",
    "IBOVESPA": "^BVSP",
    "S&P 500": "^GSPC",
    "NASDAQ": "^IXIC",
}

historico_indices = []
cotacao_atual = {}

for nome, ticker in indices.items():
    dados = yf.Ticker(ticker).history(period="40d")[["Close"]]
    dados = dados.reset_index()
    dados["Date"] = dados["Date"].dt.strftime("%Y-%m-%d")
    dados.rename(columns={"Close": nome}, inplace=True)

    historico_indices.append(dados)

    cotacao_atual[nome] = {
        "atual": round(dados.iloc[-1][nome], 2),
        "ontem": round(dados.iloc[-2][nome], 2),
        "comparacao": round(
            ((dados.iloc[-1][nome] / dados.iloc[-2][nome]) - 1) * 100, 2
        ),
    }

df_historico = pd.concat(historico_indices, axis=0, ignore_index=True)
df_historico = df_historico.pivot_table(index="Date", aggfunc="first").reset_index()

df_historico.ffill(inplace=True)
df_historico.dropna(inplace=True)
df_historico = df_historico.round(2)
df_historico.sort_values(by="Date", ascending=False, inplace=True)

date = df_historico["Date"].head(10).values.tolist()[::-1]

st.set_page_config(layout="wide")

st.title("📈 Dashboard Mercado Financeiro")
st.write("Acompanhe os principais indicadores do mercado em um só lugar")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Dolar",
        value=f"R$ {round(cotacao_atual['DOLAR']['atual'],2)}",
        delta=cotacao_atual["DOLAR"]["comparacao"],
    )

    dolar = df_historico["DOLAR"].head(10).values.tolist()[::-1]
    min_value_dolar = round(min(dolar) * 0.95, 2)
    max_value_dolar = round(max(dolar) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_dolar,
                    "max": max_value_dolar,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": dolar,
                }
            ],
        },
        height="300px",
    )

    st.metric(
        label="Ibovespa",
        value=f"{round(cotacao_atual['IBOVESPA']['atual'],2)} pts",
        delta=cotacao_atual["IBOVESPA"]["comparacao"],
    )

    Ibovespa = df_historico["IBOVESPA"].head(10).values.tolist()[::-1]
    min_value_Ibovespa = round(min(Ibovespa) * 0.95, 2)
    max_value_Ibovespa = round(max(Ibovespa) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_Ibovespa,
                    "max": max_value_Ibovespa,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": Ibovespa,
                }
            ],
        },
        height="300px",
    )


with col2:
    st.metric(
        label="Euro",
        value=f"R$ {round(cotacao_atual['EURO']['atual'],2)}",
        delta=cotacao_atual["EURO"]["comparacao"],
    )

    Euro = df_historico["EURO"].head(10).values.tolist()[::-1]
    min_value_Euro = round(min(Euro) * 0.95, 2)
    max_value_Euro = round(max(Euro) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_Euro,
                    "max": max_value_Euro,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": Euro,
                }
            ],
        },
        height="300px",
    )

    st.metric(
        label="S&P 500",
        value=f"{round(cotacao_atual['S&P 500']['atual'],2)} pts",
        delta=cotacao_atual["S&P 500"]["comparacao"],
    )

    sep = df_historico["S&P 500"].head(10).values.tolist()[::-1]
    min_value_sep = round(min(sep) * 0.95, 2)
    max_value_sep = round(max(sep) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_sep,
                    "max": max_value_sep,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": sep,
                }
            ],
        },
        height="300px",
    )


with col3:
    st.metric(
        label="Bitcoin",
        value=f"R$ {round(cotacao_atual['BITCOIN']['atual'],2)}",
        delta=cotacao_atual["BITCOIN"]["comparacao"],
    )

    Bitcoin = df_historico["BITCOIN"].head(10).values.tolist()[::-1]
    min_value_Bitcoin = round(min(Bitcoin) * 0.95, 2)
    max_value_Bitcoin = round(max(Bitcoin) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_Bitcoin,
                    "max": max_value_Bitcoin,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": Bitcoin,
                }
            ],
        },
        height="300px",
    )

    st.metric(
        label="NASDAQ",
        value=f"{round(cotacao_atual['NASDAQ']['atual'],2)} pts",
        delta=cotacao_atual["NASDAQ"]["comparacao"],
    )

    nasdaq = df_historico["NASDAQ"].head(10).values.tolist()[::-1]
    min_value_nasdaq = round(min(nasdaq) * 0.95, 2)
    max_value_nasdaq = round(max(nasdaq) * 1.05, 2)

    st_echarts(
        options={
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "cross",
                    "label": {"backgroundColor": "#6a7985"},
                },
            },
            "toolbox": {"feature": {"saveAsImage": {}}},
            "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
            "xAxis": [
                {
                    "type": "category",
                    "boundaryGap": False,
                    "data": date,
                }
            ],
            "yAxis": [
                {
                    "type": "value",
                    "min": min_value_nasdaq,
                    "max": max_value_nasdaq,
                    "scale": True,
                    "splitNumber": 5,
                }
            ],
            "series": [
                {
                    "name": "DOLAR",
                    "type": "line",
                    "areaStyle": {},
                    "emphasis": {"focus": "series"},
                    "data": nasdaq,
                }
            ],
        },
        height="300px",
    )
