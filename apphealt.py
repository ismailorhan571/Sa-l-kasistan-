import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Orhan Sağlık & Spor Paneli", page_icon="🏋️", layout="wide")

# Sidebar
with st.sidebar:
    st.header("👨‍⚕️ Geliştirici")
    st.success("**İsmail Orhan**")
    st.write("Profesyonel Sağlık ve Sporcu Beslenme Paneli")
    st.divider()
    antreman_seviyesi = st.select_slider(
        "Haftalık Antrenman Yoğunluğu",
        options=["Düşük", "Orta", "Yüksek", "Profesyonel"]
    )

# Ana Başlık
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏆 Profesyonel Sporcu Analiz Paneli</h1>", unsafe_allow_html=True)
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
vki = kilo / ((boy/100)**2)

# Protein Hesaplama Mantığı (Antrenman Seviyesine Göre katsayı)
protein_katsayilari = {"Düşük": 1.2, "Orta": 1.6, "Yüksek": 2.0, "Profesyonel": 2.2}
katsayi = protein_katsayilari[antreman_seviyesi]
gunluk_protein = kilo * katsayi

# --- SEKME DÜZENİ ---
tab1, tab2, tab3 = st.tabs(["📊 Vücut Analizi", "🥩 Sporcu Beslenmesi", "💡 Tavsiyeler"])

with tab1:
    c1, c2, c3 = st.columns(3)
    c1.metric("VKİ", f"{vki:.1f}")
    c2.metric("İdeal Kilo", f"{50 + 2.3 * (((boy/2.54) - 60)):.1f} kg")
    c3.metric("Seviye Katsayısı", f"{katsayi}x")
    
    if vki < 25:
        st.success(f"Formunuz yerinde! Antrenman seviyeniz: {antreman_seviyesi}")
    else:
        st.warning("Kas kütleniz yüksek değilse, yağ oranına dikkat etmelisiniz.")
    st.progress(min(vki/40, 1.0))

with tab2:
    st.subheader("Günlük Makro İhtiyaçları")
    m1, m2, m3 = st.columns(3)
    
    m1.metric("Toplam Protein", f"{gunluk_protein:.0f} g", delta="Kas İnşası İçin")
    m2.metric("Günlük Su", f"{kilo * 0.04:.1f} L", delta="Min. Hidrasyon")
    m3.metric("Tahmini Kalori", f"{(10*kilo + 6.25*boy - 5*yas + 5) * 1.5:.0f} kcal")
    
    st.info(f"💡 **Protein Notu:** Seçtiğin '{antreman_seviyesi}' seviyesi için kilo başına {katsayi}g protein hesaplanmıştır.")

with tab3:
    st.subheader("İsmail Orhan'dan Sporcu Notları")
    st.write(f"""
    - **Protein Kaynağı:** Günlük alman gereken **{gunluk_protein:.0f} gram** proteini; yumurta, tavuk, kırmızı et ve gerekirse whey protein ile dengeli dağıtmalısın.
    - **Zamanlama:** Antrenman sonrası ilk 2 saat içinde kaliteli bir protein ve karbonhidrat öğünü toparlanmanı hızlandırır.
    - **Su:** Antrenman esnasında kaybettiğin sıvıyı yerine koymak için günlük **{kilo * 0.04:.1f} litre** suyun altına düşmemelisin.
    """)
    st.balloons()
