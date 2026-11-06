import streamlit as st
from datetime import datetime

st.set_page_config(page_title="طلاچی", page_icon="🪙")

st.title("🪙 طلاچی")
st.subheader("دستیار هوشمند طلای میلی")

st.success("ربات آزمایشی آماده است")

st.metric("سرمایه معاملاتی", "صفر تومان")
st.metric("وضعیت", "آزمایشی")

mode = st.selectbox(
    "انتخاب حالت فعالیت",
    ["مشاهده قیمت", "تحلیل و سیگنال"]
)

st.write("حالت انتخابی:", mode)
st.info("هیچ معامله واقعی انجام نمی‌شود.")

st.write("زمان سیستم:")
st.write(datetime.now().strftime("%Y-%m-%d %H:%M"))

st.caption("Talachi Test Version")
