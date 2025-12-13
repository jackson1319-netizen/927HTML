import streamlit as st
import streamlit.components.v1 as components

# 1. 設定 Streamlit 頁面配置 (讓畫面寬一點，看起來比較氣派)
st.set_page_config(
    page_title="富邦人壽 - 配息小金庫",
    page_icon="💰",
    layout="wide", # 使用寬版面
    initial_sidebar_state="collapsed" # 隱藏側邊欄
)

# 2. 定義您的 GitHub Pages 網址
# ⚠️ 請將下方的網址換成您第一階段取得的真實網址
github_url = "https://jackson1319-netizen.github.io/927HTML/big.html"

# 3. 使用 iframe 嵌入
# height 建議設定 800-1000，確保手機版滑動順暢
# scrolling=True 允許在框框內捲動
components.iframe(github_url, height=1000, scrolling=True)

# (選用) 可以在下方加上 Python 的功能
# st.write("這是由 Python Streamlit 生成的容器")
