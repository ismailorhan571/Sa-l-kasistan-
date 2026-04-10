import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="İsmail Orhan | Sağlık & Performans", page_icon="🧬", layout="wide")

# --- CSS İLE GÖRSEL DÜZENLEME ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (YAN MENÜ) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2966/2966327.png", width=80)
    st.title("👨‍⚕️ Klinik Panel")
    st.success(f"**Geliştirici: İsmail Orhan**")
    st.divider()
    hedef = st.selectbox("Hedefiniz nedir?", 
                         ["Yağ Yakımı", "Form Koruma", "Kas Kütlesi (Bulk)"])
    aktivite = st.selectbox("Günlük Aktivite Seviyeniz", 
                            ["Hareketsiz", "Az Hareketli", "Orta Hareketli", "Çok Hareketli", "Profesyonel Sporcu"])
    st.divider()
    st.caption("© 2026 Tüm Sağlık Hesaplamaları Aktiftir.")

# --- ANA BAŞLIK ---
st.markdown("<h1 style='text-align: center; color: #E63946;'>🧬 Profesyonel Sağlık ve Performans Analizi</h1>", unsafe_allow_html=True)
st.write("---")

# --- VERİ GİRİŞ ALANI ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    boy = st.number_input("Boy (cm)", min_value=120, max_value=230, value=178)
    yas = st.number_input("Yaş", min_value=15, max_value=90, value=31)
with col2:
    kilo = st.number_input("Kilo (kg)", min_value=40.0, max_value=200.0, value=80.0)
    cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
with col3:
    bel = st.number_input("Bel Çevresi (cm)", min_value=50, max_value=150, value=85)
    boyun = st.number_input("Boyun Çevresi (cm)", min_value=20, max_value=60, value=40)
with col4:
    st.write("**Özet Bilgi**")
    st.info(f"Hedef: {hedef}")
    st.info(f"Yaş: {yas} | Cinsiyet: {cinsiyet}")

# --- PROFESYONEL HESAPLAMA MOTORU ---

# 1. BMR (Bazal Metabolizma - Mifflin-St Jeor)
if cinsiyet == "Erkek":
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) + 5
    # Navy Method Yağ Oranı Tahmini (Basitleştirilmiş Formül)
    yag_tahmini = 86.010 * 0.4343 + 70.041 * 0.4343 - 100 # Yaklaşık
else:
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) - 161
    yag_tahmini = 163.205 * 0.4343 - 97.684 * 0.4343 - 70

# 2. TDEE (Toplam Harcanan Enerji)
akt_kat = {"Hareketsiz": 1.2, "Az Hareketli": 1.375, "Orta Hareketli": 1.55, "Çok Hareketli": 1.725, "Profesyonel Sporcu": 1.9}
tdee = bmr * akt_kat[aktivite]

# 3. Makro Dağılımı ve Kalori Hedefi
if hedef == "Yağ Yakımı":
    g_kalori = tdee - 500
    p, k, y = 0.40, 0.30, 0.30
elif hedef == "Kas Kütlesi (Bulk)":
    g_kalori = tdee + 400
    p, k, y = 0.30, 0.50, 0.20
else:
    g_kalori = tdee
    p, k, y = 0.30, 0.40, 0.30

# Gram Hesapları
prot_g = (g_kalori * p) / 4
karb_g = (g_kalori * k) / 4
yag_g = (g_kalori * y) / 9

# --- SONUÇ PANELLERİ ---
t1, t2, t3, t4 = st.tabs(["📊 Vücut Kompozisyonu", "🥩 Beslenme & Makro", "🫀 Kardiyo", "⚖️ İdeal Değerler"])

with t1:
    st.subheader("Metabolik Durum Analizi")
    c1, c2, c3 = st.columns(3)
    c1.metric("Bazal Metabolizma (BMR)", f"{bmr:.0f} kcal")
    c2.metric("Günlük Harcama (TDEE)", f"{tdee:.0f} kcal")
    c3.metric("Alınması Gereken", f"{g_kalori:.0f} kcal", delta=f"{g_kalori-tdee:.0f}")
    
    st.write("---")
    vki = kilo / ((boy/100)**2)
    st.write(f"**Vücut Kitle İndeksiniz (VKİ):** {vki:.1f}")
    st.progress(min(vki/40, 1.0))

with t2:
    st.subheader(f"Günlük Makro Rehberi ({hedef})")
    m1, m2, m3 = st.columns(3)
    m1.success(f"🥩 **Protein:** {prot_g:.0f} g")
    m2.info(f"🍞 **Karbonhidrat:** {karb_g:.0f} g")
    m3.warning(f"🥑 **Yağ:** {yag_g:.0f} g")
    
    st.divider()
    st.write(f"💧 **Günlük Su İhtiyacı:** **{(kilo * 0.04):.1f} Litre**")

with t3:
    st.subheader("Kalp Sağlığı ve Nabız Bölgeleri")
    max_n = 220 - yas
    st.write(f"Maksimum Nabız Kapasitesi: **{max_n} BPM**")
    
    st.text(f"🔥 Yağ Yakım Bölgesi (%65): {max_n*0.6:.0f}-{max_n*0.7:.0f} BPM")
    st.text(f"⚡ Kondisyon Bölgesi (%80): {max_n*0.75:.0f}-{max_n*0.85:.0f} BPM")

with t4:
    st.subheader("Bilimsel İdeal Veriler")
    # Devine Formülü
    if cinsiyet == "Erkek": ideal = 50 + 2.3 * ((boy/2.54) - 60)
    else: ideal = 45.5 + 2.3 * ((boy/2.54) - 60)
    
    st.metric("Tıbbi İdeal Kilonuz", f"{ideal:.1f} kg")
    st.write("💡 Bu değer, boyunuza göre eklem ve organ sağlığınız için en dengeli ağırlıktır.")
    st.balloons()
