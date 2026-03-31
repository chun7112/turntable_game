import streamlit as st
import random
import time

st.title("🎡 吃什麼轉盤")

# ⭐ 初始化（很重要）
if "foods" not in st.session_state:
    st.session_state.foods =  ["火鍋", "拉麵", "便當", "壽司", "麥當勞"]

# ===== 顯示目前清單 =====
st.write("今天可能想吃的有...")
for i, food in enumerate(st.session_state.foods, start=1):
    st.write(f"{i}. {food}")

# ===== 新增餐點 =====
new_food = st.text_input("可能還想吃...")

if st.button("想吃它！"):
    if new_food:
        st.session_state.foods.append(new_food)
        st.rerun()

# ===== 刪除餐點 =====
delete_num = st.text_input("還是不要吃...")

if st.button("下次再吃它！"):
    if delete_num.isdigit():
        num = int(delete_num)
        if 1 <= num <= len(st.session_state.foods):
            del st.session_state.foods[num - 1]
            st.rerun()
        else:
            st.error("⚠️ 沒有這個食物哦！")
    else:
        st.error("⚠️ 請輸入數字！")

# ===== 轉盤 =====
if st.button("開始通靈"):
    placeholder = st.empty()  # ⭐ 用來做動畫

    for i in range(15):
        spin = random.choice(st.session_state.foods)
        placeholder.write(f"👉 {spin}")
        time.sleep(0.1)

    final = random.choice(st.session_state.foods)
    placeholder.write(f"今天吃...{final}!🎉")