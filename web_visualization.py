import streamlit as st
import pandas as pd

# Function to translate numbers to political opinions
def translate_number_to_political_opinion(number, lang):
    if lang == "English":
        if number == 1: 
            return "Liberal"
        elif number == 2:
            return "Moderate Liberal"
        elif number == 3:
            return "Moderate"
        elif number == 4:
            return "Moderate Conservative"
        else:
            return "Conservative"
    elif lang == "Korean":
        if number == 1: 
            return "자유주의"
        elif number == 2:
            return "온건 자유주의"
        elif number == 3:
            return "중도"
        elif number == 4:
            return "온건 보수주의"
        else:
            return "보수주의"

# Function to get colors based on political opinions
def get_color_based_on_political_opinion(number):
    if number == 1: 
        return "#87CEEB"  # Light Blue for Liberal
    elif number == 2:
        return "#B0E0E6"  # Powder Blue for Moderate Liberal
    elif number == 3:
        return "#9370DB"  # Medium Purple for Moderate
    elif number == 4:
        return "#FFB6C1"  # Light Pink for Moderate Conservative
    else:
        return "#FF6347"  # Tomato Red for Conservative

# Language selection
lang = st.selectbox("🌐 Select Language / 언어 선택", ["English", "Korean"])

# Text in both languages
title = "🇰🇷 Korean News Political Opinion Predictor 📰" if lang == "English" else "🇰🇷 한국 뉴스 정치 의견 예측기 📰"
intro = "✨ Welcome to my first political AI project!✨" if lang == "English" else "✨ 정치 AI 프로젝트에 오신 것을 환영합니다!✨"
desc1 = "🇰🇷 This app **predicts the political opinion** of Korean news articles!" if lang == "English" else "🇰🇷 이 앱은 한국 뉴스 기사의 **정치적 의견**을 예측합니다!"
desc2 = "📚 We used the **KoPolitics-Benchmark** dataset available [here](https://github.com/Kdavid2355/KoPolitic-Benchmark-Dataset/tree/main) and fine-tuned a RoBERTa model from Hugging Face 🤗 which can be found [here](https://huggingface.co/klue/roberta-base)." if lang == "English" else "📚 우리는 **KoPolitics-Benchmark** 데이터셋을 사용하였으며, RoBERTa 모델을 Hugging Face 🤗에서 가져와 세부 튜닝했습니다. [여기](https://huggingface.co/klue/roberta-base)를 참조하세요."
instructions = "🎯 What you can do here:" if lang == "English" else "🎯 여기에서 할 수 있는 작업:"
tip = "- 🌟 **Tip:** Play around and have fun exploring AI predictions! 💡" if lang == "English" else "- 🌟 **팁:** AI 예측을 탐색하며 즐겨보세요! 💡"
test_header = "📖 Test Set: News Articles" if lang == "English" else "📖 테스트 세트: 뉴스 기사"
test_desc = "💌 Here are the news articles we’re testing. Pick one, and let’s see what AI thinks!" if lang == "English" else "💌 테스트 중인 뉴스 기사입니다. 하나를 선택하고 AI의 생각을 확인해 보세요!"
selected_article = "📜 Selected Article:" if lang == "English" else "📜 선택한 기사:"
pred_opinion = "🤖 Predicted Political Opinion:" if lang == "English" else "🤖 예측된 정치 의견:"
true_opinion = "👩🏻 True Political Opinion:" if lang == "English" else "👩🏻 실제 정치 의견:"

# Title with playful emojis
st.title(title)

# Markdown with emojis and playful tone
st.markdown(intro)
st.markdown(desc1)
st.markdown(desc2)
st.markdown(instructions)
st.markdown("- 📊 **Peek at news articles** in the test set" if lang == "English" else "- 📊 테스트 세트의 뉴스 기사 살펴보기")
st.markdown("- 📰 **Select an article** and see what political opinion the model predicts for it!" if lang == "English" else "- 📰 기사를 선택하고 모델이 예측한 정치적 의견 확인하기")
st.markdown(tip)

# Load the dataset
df = pd.read_csv('political_orientation_dataset/predictions.csv')

# Display news articles with a cute section header
st.subheader(test_header)
st.markdown(test_desc)

# Rename and simplify columns
df = df.rename(columns={'text': 'Article'})

# Use Streamlit's DataFrame and Select Box
selected_row = st.selectbox(
    "✨ Select an Article ✨" if lang == "English" else "✨ 기사를 선택하세요 ✨",
    df.index,
    format_func=lambda x: f"Article #{x + 1}: {df.iloc[x]['Article'][:50]}..."  # Preview the first 50 chars
)

# Display the article and predictions
if selected_row is not None:
    st.markdown(f"### {selected_article}")
    st.write(f"_{df.iloc[selected_row]['Article']}_")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**{pred_opinion}**")
        pred_color = get_color_based_on_political_opinion(df.iloc[selected_row]['predicted_label'])
        st.markdown(
            f'<p style="background-color:{pred_color}; color:white; padding:10px; border-radius:10px;">'
            f'{translate_number_to_political_opinion(df.iloc[selected_row]["predicted_label"], lang)}</p>',
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(f"**{true_opinion}**")
        true_color = get_color_based_on_political_opinion(df.iloc[selected_row]['true_label'])
        st.markdown(
            f'<p style="background-color:{true_color}; color:white; padding:10px; border-radius:10px;">'
            f'{translate_number_to_political_opinion(df.iloc[selected_row]["true_label"], lang)}</p>',
            unsafe_allow_html=True,
        )
