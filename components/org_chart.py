import streamlit as st

def display():
    with st.container():
        st.markdown("<h3> </h3>", unsafe_allow_html=True)
        st.markdown("""
**Chairman of the Board** (رییس هیئت مدیره)  
└── **CEO – AIVS** (مدیر عامل شرکت AIVS)  
  └── **VP – AIVS** (معاون شرکت AIVS)  
    ├── **AIVS Internal Division** (نیروهای ستاد AIVS)  
    │  ├── **COO – Chief Operating Officer**  
    │  │  (مدیر ارشد عملیات – استراتژی و عملیات داخلی)  
    │  │  ├── Strategy & Operations Lead (سرپرست استراتژی و عملیات)  
    │  │  └── Head of Facilities & Logistics (رییس امور تدارکات و پشتیبانی)  
    │  ├── **CMO – Chief Marketing Officer**  
    │  │  (مدیر ارشد بازاریابی – بازاریابی و برند)  
    │  │  ├── Head of International Market Research (رییس تحقیقات بازار بین‌الملل)  
    │  │  ├── Head of Domestic Market Research (رییس تحقیقات بازار داخلی)  
    │  │  ├── AIVS Product Growth & Brand Team (تیم توسعه محصول، برند و رشد AIVS)  
    │  │  └── Innovation Unit Marketing Support Team (تیم پشتیبانی بازاریابی واحدهای نوآوری)  
    │  ├── **CFO – Chief Financial Officer**  
    │  │  (مدیر ارشد مالی – مالی و حقوقی)  
    │  │  ├── Head of AIVS Accounting (رییس حسابداری AIVS)  
    │  │  └── Head of IU Accounting (رییس حسابداری واحدهای نوآوری)  
    │  ├── **CHRO – Chief Human Resources Officer**  
    │  │  (مدیر ارشد منابع انسانی – منابع انسانی و فرهنگ)  
    │  └── **CTO – Chief Technology Officer**  
    │    (مدیر ارشد فناوری – توسعه محصولات و ابزارهای پشتیبان)  
    │    ├── Head of Product Design & Customer Experience (رییس طراحی محصول و تجربه کاربری)  
    │    ├── Head of Strategic & Decision Support (رییس پشتیبانی راهبردی و تصمیم‌سازی)  
    │    └── Head of Prototyping & MVP Development (رییس توسعه نمونه اولیه و MVP)  
    └── **Innovation Management Division** (مدیریت واحدهای نوآوری)  
      └── **PMO – Project Management Office** (دفتر مدیریت پروژه)  
        ├── **Innovation Unit 1** (واحد نوآوری ۱)  
        │  ├── Product Manager (مدیر محصول)  
        │  ├── CTO – AIVS Appointed (ناظر فنی منصوب‌شده از AIVS)  
        │  └── Innovation Unit Team Members (اعضا)  
        ├── **Innovation Unit 2** (واحد نوآوری ۲)  
        │  ├── Product Manager (مدیر محصول)  
        │  ├── CTO – AIVS Appointed (ناظر فنی)  
        │  └── Innovation Unit Team Members (اعضا)  
        └── **Innovation Unit 3** (واحد نوآوری ۳)  
          ├── Product Manager (مدیر محصول)  
          ├── CTO – AIVS Appointed (ناظر فنی)  
          └── Innovation Unit Team Members (اعضا)
""")
