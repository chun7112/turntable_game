import streamlit as st
import random
import time
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

st.title("🎡 吃什麼轉盤")

# ⭐ 載入中文字體（關鍵🔥）
font_path = "NotoSansTC-Regular.ttf"
font_prop = fm.FontProperties(fname=font_path)

# ⭐ 初始化
if "foods" not in st.session_state:
    st.session_state.foods = ["火鍋", "拉麵", "便當", "壽司", "麥當勞"]

# ⭐ 拿出來用
foods = st.session_state.foods

# ===== ⭐ 標題 =====
st.markdown("<h3 style='text-align: center;'>今天吃什麼？</h3>", unsafe_allow_html=True)

# ===== ⭐ 指針（朝下 + 貼近圓盤🔥）=====
st.markdown(
    "<div style='text-align: center; font-size:40px; margin-bottom:-25px;'>▼</div>",
    unsafe_allow_html=True
)

# ===== ⭐ 圓盤 =====
if len(foods) > 0:
    fig, ax = plt.subplots()

    sizes = [1] * len(foods)

    ax.pie(
        sizes,
        labels=foods,
        startangle=90,
        counterclock=False,
        textprops={'fontproperties': font_prop}  # ⭐ 中文關鍵
    )

    st.pyplot(fig)

else:
    st.warning("⚠️ 沒有食物可以轉！")

# ===== 顯示清單 =====
st.write("今天可能想吃的有...")
for i, food in enumerate(foods, start=1):
    st.write(f"{i}. {food}")

# ===== 新增 =====
new_food = st.text_input("可能還想吃...")
if st.button("想吃它！"):
    if new_food:
        foods.append(new_food)
        st.rerun()

# ===== 刪除 =====
delete_num = st.text_input("還是不要吃...")
if st.button("下次再吃它！"):
    if delete_num.isdigit():
        num = int(delete_num)
        if 1 <= num <= len(foods):
            del foods[num - 1]
            st.rerun()
        else:
            st.error("⚠️ 沒有這個食物哦！")
    else:
        st.error("⚠️ 請輸入數字！")

# ===== 轉盤動畫 =====
if st.button("開始通靈"):
    placeholder = st.empty()

    for i in range(15):
        spin = random.choice(foods)
        placeholder.write(f"👉 {spin}")
        time.sleep(0.1)

    final = random.choice(foods)
    placeholder.write(f"今天吃...{final}!🎉")