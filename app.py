import streamlit as st
import pandas as pd

st.write("Hello World")

st.write("Hello :blue[World]")

st.title("Hello World")

st.title("Hello World :sunglasses:")

st.write(
    pd.DataFrame(
        {
            "first column" : [1, 2, 3, 4],
            "second column" : [10, 20, 30, 40]
        }
    )
)

st.link_button("Click here", "https://docs.streamlit.io/develop/api-reference")

st.header("Hello World", divider="rainbow")

code = """print("hello")"""
st.code(code, language="python")

agree = st.checkbox("I agree")
if agree:
    st.write("Okay!")


options = st.multiselect(
    "好きな色は何ですか",
    ["赤","青","緑","黄"]
)

st.write("あなたが選んだ色は：", options)

options = st.radio(
    "好きな色は何ですか",
    ["赤","青","緑","黄"]
)

st.write("あなたが選んだ色は：", options)

# 修正できるデータフレーム
df = pd.DataFrame(
    [
        {"colors": "赤", "rating": 4, "mark":True},
        {"colors": "緑", "rating": 5, "mark":True},
        {"colors": "青", "rating": 3, "mark":True}
    ]
)
edited_df = st.data_editor(df)
edited_df = edited_df[edited_df["mark"] == True]
st.write(edited_df.loc[edited_df["rating"].idxmax()]["colors"])

# ダウンロードボタン
csv = edited_df.to_csv().encode("utf-8")
st.download_button(
    label="CSVをダウンロード",
    data=csv,
    file_name="sample_df.csv",
    mime="text/csv"
)

# プログレスバー表示
df = pd.DataFrame(
    {
        "sales": [20, 33, 100, 80],
        "progress_sales": [20, 33, 100, 80]
    }
)

st.data_editor(
    df,
    column_config={
        "progress_sales": st.column_config.ProgressColumn(
            min_value = 0,
            max_value = 100, 
        ),
    }
)

# 時系列バー表示
df = pd.DataFrame(
    {
        "sales" : [
            [0, 4, 26, 30, 60, 80, 100],
            [3, 50, 0, 80, 40, 30, 100]
        ]
    }
)

st.data_editor(df)
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.BarChartColumn(
            y_min = 0,
            y_max = 100, 
        ),
    }
)
# 時系列折れ線グラフ
st.data_editor(
    df,
    column_config={
        "sales": st.column_config.LineChartColumn(
            y_min = 0,
            y_max = 100, 
        ),
    }
)

# スライダー
age = st.slider("あなたは何歳ですか？", 0, 130, 40)
st.write("私は", age, "歳です")

# 日付選択
import datetime
date = st.date_input("あなたが生まれたのはいつですか？", datetime.date(2000, 1, 1))
st.write("私は", date, "に生まれました")

# ユーザーの自由記述
text = st.text_input("入力して下さい", "XXXXXXX")
st.write(text)

# カラムを分ける
col1, col2 = st.columns(2)
with col1:
    st.title("Column1")
    st.write("これはカラムの1です")
with col2:
    st.title("Column2")
    st.write("これはカラムの2です")

# タブを分ける
tab1, tab2 = st.tabs(["tab1", "tab2"])
with tab1:
    st.title("Tab1")
    st.write("これはタブの1です")
with tab2:
    st.title("Tab2")
    st.write("これはタブの2です")

# アコーディオン表示
with st.expander("もっと詳しく見る"):
    st.write("XXXXXXXX")

# ポップアップ表示
with st.popover("もっと詳しく見る"):
    st.write("XXXXXXXX")

# ポップアップ表示
with st.sidebar:
    st.title("XXXXXXXX")
    st.write("XXXXXXXX")

# notification
agree = st.checkbox("同意しますか？")
if agree :
    st.toast("Thank you", icon="👍")
    st.toast("Thank you2", icon="👍")
    st.toast("Thank you3", icon="👍")


birthday = st.checkbox("今日はあなたの誕生日ですか？")
if birthday:
    st.toast("誕生日おめでとう", icon="👍")
    st.balloons()

# 複数ページ実装
st.page_link("app.py", label="Home", icon="🏠")
st.page_link("pages/page1.py", label="Page1")
st.page_link("pages/page2.py", label="Page2")
st.page_link("https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/", label="stramlitのemoji")



A = st.checkbox("A？") 
B = st.checkbox("B？") 

# 各チェックボックスの初期状態をセッションステートで保持
if "A_checked" not in st.session_state:
    st.session_state.A_checked = False
if "B_checked" not in st.session_state:
    st.session_state.B_checked = False

# Aのトースト表示
if A and not st.session_state.A_checked:
    st.toast("A", icon="👍")
    st.session_state.A_checked = True
elif not A:
    st.session_state.A_checked = False

# Bのトースト表示
if B and not st.session_state.B_checked:
    st.toast("B", icon="👍")
    st.session_state.B_checked = True
elif not B:
    st.session_state.B_checked = False
