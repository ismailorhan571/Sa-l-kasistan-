import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Orhan Sağlık Paneli", page_icon="🏥", layout="wide")

# Sidebar - Geliştirici Bilgisi
with st.sidebar:
    st.header("👨‍⚕️ Geliştirici")
    st.success("**İsmail Orhan**")
    st.write("Bu panel, profesyonel sağlık verilerini analiz etmek için tasarlanmıştır.")
    st.divider()
    st.info("Not: Bu veriler genel bilgilendirme amaçlıdır.")

# Ana Başlık
st.markdown("<h1 style='text-align: center;'>🏥 Akıllı Sağlık ve Form Analizi</h1>", unsafe_allow_html=True)
st.divider()

# Giriş Alanları
col1, col2, col3, col4 = st.columns(4)

with col1:
    boy = st.number_input("Boy (cm)", min_value=100, max_value=250, value=178)
with col2:
    kilo = st.number_input("Kilo (kg)", min_value=30.0, max_value=250.0, value=80.0)
with col3:
    yas = st.number_input("Yaş", min_value=1, max_value=120, value=31)
with col4:
    cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])

# --- HESAPLAMALAR ---

# 1. VKİ (Vücut Kitle İndeksi)
vki = kilo / ((boy/100)**2)

# 2. İdeal Kilo (Devine Formülü)
if cinsiyet == "Erkek":
    ideal_kilo = 50 + 2.3 * (((boy/2.54) - 60))
    # Bazal Metabolizma Hızı (Mifflin-St Jeor)
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) + 5
else:
    ideal_kilo = 45.5 + 2.3 * (((boy/2.54) - 60))
    # Bazal Metabolizma Hızı (Mifflin-St Jeor)
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) - 161

# 3. Günlük Su İhtiyacı
su_ihtiyacı = kilo * 0.035

# --- SONUÇ EKRANI ---
st.write("")
tab1, tab2, tab3 = st.tabs(["📊 Analiz Sonuçları", "💧 Beslenme Rehberi", "🏃 Aktivite"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("VKİ Sonucunuz", f"{vki:.1f}")
    c2.metric("İdeal Kilonuz", f"{ideal_kilo:.1f} kg")
    c3.metric("Bazal Metabolizma (BMR)", f"{bmr:.0f} kcal")
    
    # VKI Durum Çubuğu
    if vki < 18.5:
        st.warning("Durum: Zayıf")
    elif 18.5 <= vki < 25:
        st.success("Durum: İdeal (Normal)")
    elif 25 <= vki < 30:
        st.info("Durum: Fazla Kilolu")
    else:
        st.error("Durum: Obezite")
    st.progress(min(vki/40, 1.0))

with tab2:
    st.subheader("Günlük Tüketim Önerileri")
    sc1, sc2 = st.columns(2)
    sc1.metric("Su Tüketimi", f"{su_ihtiyacı:.2f} Litre")
    sc2.metric("Günlük Protein (Min)", f"{kilo * 0.8:.1f} g")
    
    st.write("---")
    st.write(f"💡 **Uzman Notu:** {yas} yaşındaki bir {cinsiyet} birey olarak, günlük metabolizma hızınız olan **{bmr:.0f}** kalori, vücudunuzun hiçbir şey yapmadan yaktığı enerjidir. Kilo vermek için bu rakamın biraz altında, kas kazanmak için biraz üzerinde beslenmelisiniz.")

with tab3:
    st.subheader("Kalori Yakım Tablosu")
    st.write("30 Dakikalık Aktivite Tahminleri:")
    st.write(f"🚶 **Yürüyüş:** ~{bmr * 0.1:.0f} kcal")
    st.write(f"🏃 **Koşu:** ~{bmr * 0.25:.0f} kcal")
    st.write(f"🏋️ **Ağırlık Antrenmanı:** ~{bmr * 0.15:.0f} kcal")
    st.balloons()
