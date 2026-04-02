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

# ⭐ 圓盤位置（只保留一個）
placeholder = st.empty()

# ⭐ 產生換行文字
foods_wrapped = []

for food in foods:
    if len(food) > 6:
        new_food = food[:6] + "\n" + food[6:]
    else:
        new_food = food
    foods_wrapped.append(new_food)

# ===== ⭐ 預設顯示圓盤（關鍵🔥）=====
if len(foods) > 0:
    fig, ax = plt.subplots(figsize=(5, 5), facecolor='white')

    sizes = [1] * len(foods)

    ax.pie(
    sizes,
        labels=foods_wrapped,   # ⭐ 換這裡
        startangle=90,
        counterclock=True,
        labeldistance=0.5,
        rotatelabels=True,
        textprops={
            'fontproperties': font_prop,
            'fontsize': 8
        }
    )
    
    ax.set_aspect('equal')
    plt.tight_layout()
    
    placeholder.pyplot(fig)

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
    result = random.choice(foods)
    index = foods.index(result)

    angle_per = 360 / len(foods)
    target_angle = 360 - (index * angle_per) - (angle_per / 2)

    # ⭐ 模擬幾個角度（關鍵🔥）
    angles = [0, 180, 360, 540, 720 + target_angle]

    for angle in angles:
        fig, ax = plt.subplots(figsize=(5, 5))
        sizes = [1] * len(foods)

        ax.pie(
            sizes,
            labels=foods_wrapped,
            startangle=90 + angle,
            counterclock=True,
            labeldistance=0.5,
            textprops={'fontproperties': font_prop}
        )

        ax.set_aspect('equal')
        plt.tight_layout()

        placeholder.pyplot(fig, clear_figure=True)
        time.sleep(0.1)  # ⭐ 這裡才有用

    st.success(f"🎉 今天吃：{result}")

# if st.button("開始通靈"):
#     result = random.choice(foods)
#     index = foods.index(result)

#     angle_per = 360 / len(foods)

#     # ⭐ 停在正中央
#     target_angle = 360 - (index * angle_per) - (angle_per / 2)

#     final_angle = 720 + target_angle

#     # ⭐ 新增：目前角度（起點）
#     current_angle = 0
#     count = 0
    
#     # ⭐ 改成 while（減速關鍵🔥）
#     while current_angle < final_angle and count < 200:

#         # ⭐ 剩餘距離
#         remaining = final_angle - current_angle

#         # ⭐ 決定速度（核心🔥）
#         if remaining > 360:
#             step =30
#         elif remaining > 180:
#             step = 15
#         elif remaining > 60:
#             step = 5
#         else:
#             step = 1

#         # ⭐ 這行超重要（很多人會漏❗）
#         current_angle += step
#         count += 1

#         fig, ax = plt.subplots()
#         sizes = [1] * len(foods)

#         ax.pie(
#             sizes,
#             labels=foods,
#             startangle=90 + current_angle,  # ⭐ 用 current_angle
#             counterclock=True,
#             labeldistance=0.5,
#             textprops={'fontproperties': font_prop}
#         )

#         placeholder.pyplot(fig)
#         time.sleep(0.01)

#     st.success(f"🎉 今天吃：{result}")