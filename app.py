import streamlit as st
from transformers import pipeline

# عنوان صفحه
st.set_page_config(page_title="تحلیل‌گر طرح سرمایه‌گذاری", layout="centered")

# مدل زبانی رایگان
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt2")

generator = load_model()

# رابط کاربری
st.title("💼 تحلیل‌گر هوشمند طرح سرمایه‌گذاری")
st.markdown("✍️ خلاصه طرح سرمایه‌گذاری خود را وارد کنید:")
user_input = st.text_area("مثال: می‌خوام یه اپلیکیشن مالی بسازم برای دانش‌آموزا. سرمایه اولیه ۳۰ میلیون. انتظار سود سالیانه ۴۰٪ دارم.")

if st.button("🔍 تحلیل ایده"):
    if user_input.strip() == "":
        st.warning("لطفاً خلاصه‌ای وارد کنید.")
    else:
        with st.spinner("در حال تحلیل..."):
            prompt = f"ایده سرمایه‌گذاری:\n{user_input}\n\nتحلیل این ایده:"
            result = generator(prompt, max_length=200, num_return_sequences=1)[0]["generated_text"]
            st.subheader("🔎 نتیجه:")
      st.write(result.replace(prompt, ""))
