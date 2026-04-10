import streamlit as st
import math

# 1. Sayfa Temelleri
st.set_page_config(page_title="İsmail Orhan Sağlık Paneli", page_icon="🧬", layout="wide")

# 2. Sidebar: Tüm Girişleri Buraya Topladık (Ekran Karışmasın Diye)
with st.sidebar:
    st.header("👤 Kullanıcı Bilgileri")
    cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
    yas = st.number_input("Yaş", min_value=15, max_value=90, value=31)
    boy = st.number_input("Boy (cm)", min_value=120, max_value=230, value=178)
    kilo = st.number_input("Kilo (kg)", min_value=40.0, max_value=200.0, value=80.0)
    
    st.divider()
    st.header("📏 Ölçümler (Opsiyonel)")
    bel = st.number_input("Bel Çevresi (cm)", value=85)
    boyun = st.number_input("Boyun Çevresi (cm)", value=40)
    
    st.divider()
    st.header("🎯 Hedef & Aktivite")
    hedef = st.selectbox("Hedefiniz", ["Yağ Yakımı", "Form Koruma", "Kas Kütlesi (Bulk)"])
    aktivite = st.selectbox("Aktivite Seviyesi", ["Hareketsiz", "Az Hareketli", "Orta Hareketli", "Çok Hareketli", "Profesyonel"])
    
    st.divider()
    st.success("**Geliştirici: İsmail Orhan**")

# 3. Ana Panel Başlığı
st.markdown(f"<h1 style='text-align: center; color: #E63946;'>🧬 Profesyonel Performans Analizi</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>Hoş geldiniz! İşte <b>{hedef}</b> hedefiniz için analizleriniz:</p>", unsafe_allow_html=True)

# 4. Hesaplama Motoru (Hatasız Formüller)
# BMR
if cinsiyet == "Erkek":
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) + 5
    # Yağ Oranı Tahmini (Navy Formülü Basitleştirilmiş)
    yag_orani = 495 / (1.0324 - 0.19077 * math.log10(bel - boyun) + 0.15456 * math.log10(boy)) - 450
else:
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) - 161
    yag_orani = 495 / (1.29579 - 0.35004 * math.log10(bel - boyun) + 0.22100 * math.log10(boy)) - 450

# TDEE
akt_kat = {"Hareketsiz": 1.2, "Az Hareketli": 1.375, "Orta Hareketli": 1.55, "Çok Hareketli": 1.725, "Profesyonel": 1.9}
tdee = bmr * akt_kat[aktivite]

# Makrolar
if hedef == "Yağ Yakımı":
    g_kalori = tdee - 500
    p_g, k_g, y_g = (kilo * 2.0), ((g_kalori * 0.3) / 4), ((g_kalori * 0.25) / 9)
elif hedef == "Kas Kütlesi (Bulk)":
    g_kalori = tdee + 400
    p_g, k_g, y_g = (kilo * 1.8), ((g_kalori * 0.5) / 4), ((g_kalori * 0.2) / 9)
else:
    g_kalori = tdee
    p_g, k_g, y_g = (kilo * 1.6), ((g_kalori * 0.4) / 4), ((g_kalori * 0.25) / 9)

# 5. Sonuç Ekranı (Temiz Düzen)
t1, t2, t3 = st.tabs(["📊 Metabolizma & Yağ", "🥩 Beslenme Programı", "🫀 Kalp & Sağlık"])

with t1:
    col1, col2 = st.columns(2)
    col1.metric("Bazal Metabolizma (BMR)", f"{bmr:.0f} kcal")
    col2.metric("Günlük Harcama (TDEE)", f"{tdee:.0f} kcal")
    
    st.write("---")
    vki = kilo / ((boy/100)**2)
    st.subheader(f"Vücut Kitle İndeksi: {vki:.1f}")
    if vki < 25: st.success("Normal Kilodasınız")
    elif vki < 30: st.warning("Fazla Kilolu")
    else: st.error("Obezite Sınırı")
    
    st.info(f"Tahmini Vücut Yağ Oranı: %{max(yag_orani, 0):.1f}")

with t2:
    st.subheader(f"Günlük Makro İhtiyacı ({g_kalori:.0f} kcal)")
    m1, m2, m3 = st.columns(3)
    m1.error(f"🥩 Protein\n{p_g:.0f}g")
    m2.success(f"🍞 Karb\n{k_g:.0f}g")
    m3.warning(f"🥑 Yağ\n{yag_g:.0f}g")
    
    st.divider()
    st.write(f"💧 **Günlük Su İhtiyacınız:** {kilo * 0.04:.1f} Litre")

with t3:
    max_n = 220 - yas
    st.subheader("Kardiyo Hedefleri")
    st.write(f"Maksimum Kalp Atış Hızınız: **{max_n} BPM**")
    
    st.write("🎯 **Yağ Yakım Bölgesi:**", f"{max_n*0.6:.0f} - {max_n*0.7:.0f} BPM")
    st.write("⚡ **Kondisyon Bölgesi:**", f"{max_n*0.75:.0f} - {max_n*0.85:.0f} BPM")
    
    if st.button("Kutlamayı Başlat!"):
        st.balloons()
