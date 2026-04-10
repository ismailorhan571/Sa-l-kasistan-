import streamlit as st

# 1. Sayfa Ayarları (Mobil uyum için geniş mod)
st.set_page_config(page_title="İsmail Orhan Sağlık Paneli", page_icon="🧬", layout="centered")

# --- TÜM GİRİŞLERİ YAN MENÜYE ALDIK (EKRAN KARIŞMASIN DİYE) ---
with st.sidebar:
    st.header("👤 Kişisel Bilgiler")
    cinsiyet = st.selectbox("Cinsiyet", ["Erkek", "Kadın"])
    yas = st.number_input("Yaş", 15, 90, 31)
    boy = st.number_input("Boy (cm)", 120, 230, 178)
    kilo = st.number_input("Kilo (kg)", 40.0, 200.0, 80.0)
    
    st.divider()
    st.header("🎯 Hedef ve Hareket")
    hedef = st.selectbox("Hedefiniz", ["Yağ Yakımı", "Form Koruma", "Kas Kütlesi Artışı"])
    aktivite = st.selectbox("Günlük Aktivite", 
                            ["Masa Başı / Hareketsiz", "Az Hareketli (Haftada 1-3 gün spor)", 
                             "Orta Hareketli (Haftada 3-5 gün spor)", "Çok Hareketli (Haftada 6-7 gün ağır spor)"])
    st.divider()
    st.success("**Geliştirici: İsmail Orhan**")

# --- ANA EKRAN TASARIMI ---
st.markdown(f"<h1 style='text-align: center; color: #E63946;'>🏥 Profesyonel Sağlık Paneli</h1>", unsafe_allow_html=True)
st.write(f"Hoş geldin! Bilgilerini sol taraftaki menüden güncelleyebilirsin.")
st.divider()

# --- HESAPLAMA MOTORU (HATASIZ FORMÜLLER) ---

# 1. Bazal Metabolizma (BMR)
if cinsiyet == "Erkek":
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) + 5
    ideal_kilo = 50 + 2.3 * ((boy / 2.54) - 60)
else:
    bmr = (10 * kilo) + (6.25 * boy) - (5 * yas) - 161
    ideal_kilo = 45.5 + 2.3 * ((boy / 2.54) - 60)

# 2. TDEE (Günlük Toplam Harcama)
akt_harita = {"Masa Başı / Hareketsiz": 1.2, "Az Hareketli (Haftada 1-3 gün spor)": 1.375, 
              "Orta Hareketli (Haftada 3-5 gün spor)": 1.55, "Çok Hareketli (Haftada 6-7 gün ağır spor)": 1.725}
tdee = bmr * akt_harita[aktivite]

# 3. Hedef Kalori ve Makrolar
if hedef == "Yağ Yakımı":
    alman_gereken_kalori = tdee - 500
    protein_gr = kilo * 2.0  # Yağ yakarken kas korumak için yüksek protein
elif hedef == "Kas Kütlesi Artışı":
    alman_gereken_kalori = tdee + 400
    protein_gr = kilo * 1.8
else:
    alman_gereken_kalori = tdee
    protein_gr = kilo * 1.6

# 4. Diğer Veriler
vki = kilo / ((boy / 100) ** 2)
su_ihtiyacı = kilo * 0.04
max_nabiz = 220 - yas

# --- SONUÇLARI GÖSTERME (SEKMELİ YAPI - MOBİL DOSTU) ---
tab1, tab2, tab3 = st.tabs(["📊 Vücut & Kalori", "🥩 Beslenme / Protein", "🫀 Kalp & Sağlık"])

with tab1:
    st.subheader("Metabolik Analiz")
    c1, c2 = st.columns(2)
    c1.metric("Bazal Metabolizma", f"{bmr:.0f} kcal")
    c2.metric("Günlük Harcama", f"{tdee:.0f} kcal")
    
    st.info(f"🎯 **Hedefin İçin Alman Gereken:** {alman_gereken_kalori:.0f} Kalori")
    
    st.divider()
    st.write(f"**Vücut Kitle İndeksiniz (VKİ):** {vki:.1f}")
    if vki < 18.5: st.warning("Durum: Zayıf")
    elif vki < 25: st.success("Durum: İdeal")
    elif vki < 30: st.info("Durum: Fazla Kilolu")
    else: st.error("Durum: Obezite")
    st.progress(min(vki / 40, 1.0))

with tab2:
    st.subheader(f"Sporcu Beslenme Rehberi")
    m1, m2 = st.columns(2)
    m1.metric("Günlük Protein", f"{protein_gr:.0f} g", "Kas İnşası")
    m2.metric("Günlük Su", f"{su_ihtiyacı:.1f} L", "Hidrasyon")
    
    st.divider()
    st.write("💡 **Beslenme Notu:**")
    st.write(f"- Hedefin **{hedef}** olduğu için protein alımın kilonun **{protein_gr/kilo:.1f} katı** olarak ayarlandı.")
    st.write(f"- İdeal kilon olan **{ideal_kilo:.1f} kg** hedefine ulaşmak için kalori takibi yapmalısın.")

with tab3:
    st.subheader("Kardiyo ve Kalp Sağlığı")
    st.write(f"Maksimum Kalp Atış Hızınız: **{max_nabiz} BPM**")
    
    st.write("🎯 **Antrenman Nabız Bölgeleri:**")
    st.warning(f"🔥 Yağ Yakımı (%60-70): {max_nabiz*0.6:.0f} - {max_nabiz*0.7:.0f} BPM")
    st.info(f"🏃 Kondisyon (%70-80): {max_nabiz*0.7:.0f} - {max_nabiz*0.8:.0f} BPM")
    st.error(f"⚡ Maksimum Performans (%85+): {max_nabiz*0.85:.0f}+ BPM")
    
    if st.button("Tebrikler! Analizi Tamamla"):
        st.balloons()
