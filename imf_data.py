import pandas as pd
import streamlit as st
import plotly.express as px

st.title('世界経済データ')

# CSVファイルの読み込み
df_gdp_all = pd.read_csv('csv_data/GDP（前年比）.csv', index_col=0)
df_gdp_usd = pd.read_csv('csv_data/GDP（米ドル）.csv', index_col=0)
df_gdp_per = pd.read_csv('csv_data/一人当たりGDP.csv', index_col=0)
df_cpi = pd.read_csv('csv_data/インフレ率（％）.csv', index_col=0)
df_unemp = pd.read_csv('csv_data/失業率.csv', index_col=0)
df_pop = pd.read_csv('csv_data/人口.csv', index_col=0)

# データフレームを転置（行と列を入れ替える）
df_gdp_all = df_gdp_all.transpose()
df_gdp_usd = df_gdp_usd.transpose()
df_gdp_per = df_gdp_per.transpose()
df_cpi = df_cpi.transpose()
df_unemp = df_unemp.transpose()
df_pop = df_pop.transpose()

# データの型を変更
df_gdp_all = df_gdp_all.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
df_gdp_usd = df_gdp_usd.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
df_gdp_per = df_gdp_per.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
df_cpi = df_cpi.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
df_unemp = df_unemp.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)
df_pop = df_pop.applymap(lambda x: float(x.replace(',', '')) if isinstance(x, str) else x)

# ユーザーに国名の選択肢を表示
selected_countries = st.multiselect('国名を選択してください', df_gdp_all.columns)

# 選択した国のデータを抽出
selected_data1 = df_gdp_all.loc[:, selected_countries] if all(country in df_gdp_all.columns for country in selected_countries) else pd.DataFrame()
selected_data2 = df_gdp_usd.loc[:, selected_countries] if all(country in df_gdp_usd.columns for country in selected_countries) else pd.DataFrame()
selected_data3 = df_gdp_per.loc[:, selected_countries] if all(country in df_gdp_per.columns for country in selected_countries) else pd.DataFrame()
selected_data4 = df_cpi.loc[:, selected_countries] if all(country in df_cpi.columns for country in selected_countries) else pd.DataFrame()
selected_data5 = df_unemp.loc[:, selected_countries] if all(country in df_unemp.columns for country in selected_countries) else pd.DataFrame()
selected_data7 = df_pop.loc[:, selected_countries] if all(country in df_pop.columns for country in selected_countries) else pd.DataFrame()


# グラフの作成
fig1 = px.line(selected_data1)
fig2 = px.line(selected_data2)
fig3 = px.line(selected_data3)
fig4 = px.line(selected_data4)
fig5 = px.line(selected_data5)
fig7 = px.line(selected_data7)

# グラフにタイトルを追加
fig1.update_layout(title='GDP（前年比）')
fig2.update_layout(title='GDP')
fig3.update_layout(title='国民一人当たりのGDP')
fig4.update_layout(title='インフレ率（前年比）')
fig5.update_layout(title='失業率')
fig7.update_layout(title='人口')

# x,y軸のラベル
fig1.update_xaxes(title='')
fig1.update_yaxes(title='%')
fig2.update_xaxes(title='')
fig2.update_yaxes(title='10億ドル')
fig3.update_xaxes(title='')
fig3.update_yaxes(title='ドル')
fig4.update_xaxes(title='')
fig4.update_yaxes(title='%')
fig5.update_xaxes(title='')
fig5.update_yaxes(title='%')
fig7.update_xaxes(title='')
fig7.update_yaxes(title='百万人')

fig1 = px.line(selected_data1, line_width=3)
fig2 = px.line(selected_data2, line_width=3)
fig3 = px.line(selected_data3, line_width=3)
fig4 = px.line(selected_data4, line_width=3)
fig5 = px.line(selected_data5, line_width=3)
fig7 = px.line(selected_data7, line_width=3)

st.write('source: IMF 世界経済見通し')