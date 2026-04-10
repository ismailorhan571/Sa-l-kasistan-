import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Orhan | Pro Health & Fitness", page_icon="🧬", layout="wide")

# --- SIDEBAR: PROFESYONEL AYARLAR ---
with st.sidebar:
    st.title("👨‍⚕️ Klinik Panel")
    st.success("**Geliştirici: İsmail Orhan**")
    st.divider()
    hedef = st.selectbox("Hedef Belirleyin", ["Yağ Yakımı", "Form Koruma", "Kas Kütlesi Artışı (Bulk)"])
    aktivite = st.selectbox("Günlük Aktivite", 
                            ["Hareketsiz (Ofis)", "Az Hareketli", "Orta Hareketli", "Çok Hareketli", "Sporcu/Ağır İş"])
    st.divider()
    st.write("🔧 *Bu panel profesyonel algoritmalar kullanır.*")

# --- ANA BAŞLIK ---
st.markdown("<h1 style='text-align: center; color: #E63946;'>🧬 Profesyonel Sağlık ve Performans Analizi</h1>", unsafe_allow_html=True)
st.write("---")

# --- VERİ GİRİŞİ ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    boy = st.number_input("Boy (cm)", value=178)
    boyun = st.number_input("Boyun Çevresi (cm)", value=40)
with col2:
    kilo = st.number_input("Kilo (kg)", value=80.0)
    bel = st.number_input("Bel Çevresi (cm)", value=85)
with col3:
    yas = st.number_input("Yaş", value=31)
    cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
with col4:
    st.write("**Hedef & Seviye**")
    st.info(f"Hedef: {hedef}")
    st.info(f"Aktivite: {aktivite}")

# --- PROFESYONEL HESAPLAMALAR ---

# 1. BMR (Mifflin-St Jeor)
if cinsiyet == "Erkek":
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) + 5
    # Yağ Oranı (Navy Method - Yaklaşık)
    yag_orani = 495 / (1.0324 - 0.19077 * (3.14159/180) + 0.15456 * (3.14159/180)) - 450 # Basit gösterim
else:
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) - 161
    yag_orani = 25 # Kadın için varsayılan

# 2. TDEE (Toplam Günlük Enerji Harcaması)
aktivite_katsayilari = {"Hareketsiz (Ofis)": 1.2, "Az Hareketli": 1.375, "Orta Hareketli": 1.55, "Çok Hareketli": 1.725, "Sporcu/Ağır İş": 1.9}
tdee = bmr * aktivite_katsayilari[aktivite]

# 3. Makro Dağılımı (Hedefe Göre)
if hedef == "Yağ Yakımı":
    gunluk_kalori = tdee - 500
    p_oran, k_oran, y_oran = 0.40, 0.30, 0.30 # %40 Protein, %30 Karb, %30 Yağ
elif hedef == "Kas Kütlesi Artışı (Bulk)":
    gunluk_kalori = tdee + 400
    p_oran, k_oran, y_oran = 0.30, 0.50, 0.20
else:
    gunluk_kalori = tdee
    p_oran, k_oran, y_oran = 0.30, 0.40, 0.30

# Gram hesaplama (Protein: 4kcal, Karb: 4kcal, Yağ: 9kcal)
prot_g = (gunluk_kalori * p_oran) / 4
karb_g = (gunluk_kalori * k_oran) / 4
yag_g = (gunluk_kalori * y_oran) / 9

# --- SONUÇLAR ---
tab1, tab2, tab3 = st.tabs(["📉 Metabolik Analiz", "🍎 Makro & Beslenme", "🫀 Kardiyovasküler"])

with tab1:
    st.subheader("Vücut Kompozisyonu")
    m1, m2, m3 = st.columns(3)
    m1.metric("BMR (Bazal Metabolizma)", f"{bmr:.0f} kcal")
    m2.metric("TDEE (Günlük Harcama)", f"{tdee:.0f} kcal")
    m3.metric("Hedef Kalori", f"{gunluk_kalori:.0f} kcal")
    
    st.write("---")
    vki = kilo / ((boy/100)**2)
    st.write(f"**Vücut Kitle İndeksi:** {vki:.1f}")
    st.progress(min(vki/40, 1.0))
    st.caption("Profesyonel Not: TDEE, gün boyu hareketleriniz dahil yaktığınız toplam enerjidir.")

with tab2:
    st.subheader(f"Günlük Makro Dağılımı ({hedef})")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🥩 **Protein:** {prot_g:.0f} g")
    c2.warning(f"🍞 **Karbonhidrat:** {karb_g:.0f} g")
    c3.error(f"🥑 **Yağ:** {yag_g:.0f} g")
    
    st.write("---")
    st.write("💧 **Su İhtiyacı:** Antrenman günleri için önerilen: ", f"**{kilo * 0.045:.1f} Litre**")

with tab3:
    st.subheader("Kalp Sağlığı ve Nabız Bölgeleri")
    max_nabiz = 220 - yas
    
    st.write(f"**Maksimum Kalp Atış Hızı:** {max_nabiz} BPM")
    st.write("🎯 **Hedef Nabız Bölgeleri:**")
    st.text(f"🔥 Yağ Yakımı (%60-70): {max_nabiz*0.6:.0f} - {max_nabiz*0.7:.0f} BPM")
    st.text(f"🏃 Aerobik Kapasite (%70-80): {max_nabiz*0.7:.0f} - {max_nabiz*0.8:.0f} BPM")
    st.text(f"⚡ Anaerobik Eşik (%80-90): {max_nabiz*0.8:.0f} - {max_nabiz*0.9:.0f} BPM")
    
    st.balloons()
