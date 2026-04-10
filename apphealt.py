import streamlit as st

# 1. Sayfa Ayarları ve Tema
st.set_page_config(page_title="İsmail Orhan Sağlık Paneli", page_icon="💪", layout="wide")

# 2. Yan Menü (Sidebar) ile Geliştirici Bilgisi
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3004/3004458.png", width=100) # Sağlık ikonu
    st.title("Geliştirici Paneli")
    st.info("🚀 Bu profesyonel sağlık asistanı **İSMAİL ORHAN** tarafından tasarlanmıştır.")
    st.write("---")
    st.caption("Versiyon: 2.0.0")

# 3. Ana Başlık ve Giriş
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🏥 Akıllı Sağlık ve Form Paneli</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Verilerinize dayalı kişisel sağlık rehberiniz.</p>", unsafe_allow_html=True)
st.write("---")

# 4. Veri Giriş Alanı (Görsel Kartlar İçinde)
col1, col2, col3 = st.columns(3)

with col1:
    boy = st.number_input("Boyunuz (cm)", min_value=100, max_value=250, value=178)
with col2:
    kilo = st.number_input("Kilonuz (kg)", min_value=30.0, max_value=250.0, value=80.0)
with col3:
    yas = st.number_input("Yaşınız", min_value=1, max_value=120, value=30)

st.write("")

# 5. Hesaplamalar ve Sekmeler (Tabs)
tab1, tab2, tab3 = st.tabs(["📊 Vücut Analizi", "💧 Su & Beslenme", "🏋️ Antrenman Notu"])

with tab1:
    st.subheader("Vücut Kitle İndeksi (VKİ) Sonucu")
    vki = kilo / ((boy/100)**2)
    
    # Renkli Metrik Gösterimi
    c1, c2 = st.columns(2)
    c1.metric(label="Hesaplanan VKİ", value=f"{vki:.1f}")
    
    if vki < 18.5:
        durum = "Zayıf"
        renk = "blue"
    elif 18.5 <= vki < 25:
        durum = "İdeal"
        renk = "green"
    elif 25 <= vki < 30:
        durum = "Kilolu"
        renk = "orange"
    else:
        durum = "Obez"
        renk = "red"
    
    st.markdown(f"#### Durumunuz: :{renk}[{durum}]")
    st.progress(min(vki/40, 1.0)) # İlerleme çubuğu

with tab2:
    st.subheader("Günlük İhtiyaçlarınız")
    # Su Hesabı: Kilo * 0.035
    su = kilo * 0.035
    # Protein Hesabı (Spor yapan biri için yaklaşık 1.6g/kg)
    protein = kilo * 1.6
    
    sc1, sc2 = st.columns(2)
    sc1.metric(label="Günlük Su İhtiyacı", value=f"{su:.2f} L", delta="Min. Tüketim")
    sc2.metric(label="Günlük Protein İhtiyacı", value=f"{protein:.0f} g", delta="Sporcu İçin")
    
    st.info("💡 Not: Su tüketimi antrenman yoğunluğuna göre artırılmalıdır.")

with tab3:
    st.subheader("Geliştiriciden Tavsiye")
    st.success(f"""
    Sayın kullanıcımız, **İsmail Orhan** tarafından hazırlanan analiz sonuçlarına göre:
    - Boyunuz olan **{boy} cm** için ideal kilo aralığınız yaklaşık **{22 * ((boy/100)**2):.1f} kg** seviyeleridir.
    - Yaşınız (**{yas}**) ve kilonuz dikkate alındığında, günlük protein alımınıza dikkat ederek formunuzu koruyabilirsiniz.
    """)
    st.balloons() # Her hesaplamada değil, bu sayfada bir sürpriz olsun

# 6. Alt Bilgi (Footer)
st.write("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2026 İsmail Orhan Sağlık Teknolojileri. Tüm Hakları Saklıdır.</p>", unsafe_allow_html=True)
