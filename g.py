import streamlit as st
from PIL import Image
from pathlib import Path
#import segno  
import io

# ------------------------------
# Page config & initial state
# ------------------------------
st.set_page_config(
    page_title="Découvrir son talent – Présentation interactive",
    page_icon="✨",
    layout="wide",
)

if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.section = "Introduction"
    st.session_state.presentation_on = False
    st.session_state.profile = {
        "name": "Jérémie KPOGHOMOU",
        "profil": "Ingénieur Data chez Safran Aircraft Engines",
        # ⚠️ Mets tes images dans ton dépôt GitHub (ex: assets/) et appelle-les par URL
        "image_path": "https://raw.githubusercontent.com/<ton_repo>/assets/photo.jpg",
        "linkedin": "https://www.linkedin.com/in/jérémiekpoghomou/",
        "email": "jeremie.kpoghomou77@gmail.com",
        "github": "https://github.com/Jere623",
        "linkedin_logo": "https://raw.githubusercontent.com/<ton_repo>/assets/linkedin.png",
        "github_logo": "https://raw.githubusercontent.com/<ton_repo>/assets/github.png",
    }

# ------------------------------
# Custom CSS (animations & style)
# ------------------------------
st.markdown(
    """
    <style>
    :root { --radius: 16px; }

    .big-title {
        font-weight: 900;
        font-size: clamp(32px, 5vw, 60px);
        line-height: 1.2;
        margin: 0 0 12px 0;
        background: linear-gradient(90deg, red, yellow, green);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        animation: glow 6s ease-in-out infinite;
    }

    @keyframes glow {
        0%,100% { filter: drop-shadow(0 0 0px rgba(0,0,0,0)); }
        50% { filter: drop-shadow(0 0 6px rgba(0,0,0,.35)); }
    }

    .profile-name {
        font-weight: 800; font-size: 1.5rem;
        margin-top: 2px; margin-bottom: 2px;
    }

    .profile-info {
        font-size: 0.85rem;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
    }

    .profile-profil {
        font-weight: 800;
        font-size: 1.2rem;
        color: purple;
        margin-top: 2px; margin-bottom: 6px;
    }

    .profile-info img {
        width: 20px; height: 20px;
        margin-right: 6px;
        object-fit: contain;
    }

    .footnote {
        font-size: 1rem;
        opacity: .8;
        margin-top: 80px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# LAYOUT: Left panel
# ------------------------------
left, right = st.columns([1, 1.5])

with left:
    if st.button("🔘 On|Off  la Présentation"):
        st.session_state.presentation_on = not st.session_state.presentation_on

    # ✅ QRCode
    qr = segno.make("https://jeremiekpo77.streamlit.app/")  
    buf = io.BytesIO()
    qr.save(buf, kind='png')
    buf.seek(0)
    st.image(buf, caption="🔗 QR Code", use_column_width=True)

    if st.session_state.presentation_on:
        selected_section = st.radio(
            label="",
            options=[
                "Introduction",
                "1. L’importance de découvrir son talent",
                "2. Bien s’orienter dans un monde en mutation",
                "3. L’importance des filières scientifiques et techniques",
                "4. Mon parcours comme illustration",
                "5. Messages ciblés",
                "6. Conseils pratiques pour s’orienter",
                "7. Conclusion",
            ],
            index=0,
            key="radio_plan"
        )
        st.session_state.section = selected_section

        # Profil
        prof = st.session_state.profile
        img_path = prof.get("image_path", "")
        if img_path.startswith("http"):
            st.image(img_path, width=200)
        else:
            st.warning("⚠️ Mets ton image dans GitHub et appelle-la par une URL.")

        st.markdown(f"<div class='profile-name'>{prof.get('name','')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-profil'>{prof.get('profil','')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='{prof.get('linkedin_logo','')}' /> <a href='{prof.get('linkedin','')}' target='_blank'>{prof.get('linkedin','')}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='{prof.get('github_logo','')}' /> <a href='{prof.get('github','')}' target='_blank'>{prof.get('github','')}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'>Email: <a href='mailto:{prof.get('email','')}'>{prof.get('email','')}</a></div>", unsafe_allow_html=True)

# ------------------------------
# RIGHT content
# ------------------------------
with right:
    if st.session_state.presentation_on:
        st.markdown("<div class='big-title'>Découvrir son talent et s’orienter vers les métiers d’avenir</div>", unsafe_allow_html=True)
        st.caption("Présentation interactive – radio cliquable, édition et animations")

        CONTENT = {
            "Introduction": "## Introduction\n\n**Trois questions essentielles:**\n\n1. Quel est votre talent unique ?\n\n2. Votre métier existera-t-il encore dans 10 ans ?\n\n3. Si l’IA remplaçait votre emploi, comment rebondir ?.",
            "1. L’importance de découvrir son talent": "## 1. L’importance de découvrir son talent.\n\n**Pourquoi découvrir son talent ?**\n\n Découvrir son talent est essentiel pour s’épanouir et réussir dans sa vie personnelle et professionnelle.\n\n C’est une boussole intérieure qui nous guide dans nos choix.",
            "2. Bien s’orienter dans un monde en mutation": "## 2. Un talent = aptitude naturelle + passion + persévérance.\n\n C’est une boussole qui guide notre vie professionnelle.",
            "3. L’importance des filières scientifiques et techniques": "## 3. L’importance des filières scientifiques et techniques\n\n Les maths = langue de l’IA\n\n L’informatique = outil central.\n\n Options utiles : Mathématiques, Physique-Chimie, Sciences de l’Ingénieur, NSI\n\n Ces choix ouvrent la porte aux métiers d’avenir.",
            "4. Mon parcours comme illustration": "## 4. Mon parcours comme illustration\n\n Licence en Économie-Gestion\n\n Triple Master : Data Science, Statistiques appliquées, Finances publiques\n\n Forces : analyse, rigueur, curiosité face aux chiffres\n\n Orientation stratégique vers un domaine porteur.",
            "5. Messages ciblés": None,
            "6. Conseils pratiques pour s’orienter": "## 6. Conseils pratiques pour s’orienter\n\n 👉 Identifiez vos points forts\n\n 👉 Explorez les métiers d’avenir\n\n 👉 Formez-vous continuellement.",
            "7. Conclusion": "## 7. Conclusion\n\n En découvrant vos talents et en vous orientant intelligemment, vous vous offrez une meilleure chance de réussite et d’épanouissement.",
        }

        if st.session_state.section == "5. Messages ciblés":
            st.subheader("📌 Messages ciblés")
            if st.checkbox("Étudiants", value=False):
                st.info("👉 Choisissez des options porteuses.")
            if st.checkbox("Diplômés sans emploi", value=False):
                st.info("👉 Formez-vous aux métiers d’avenir.")
            if st.checkbox("Travailleurs", value=False):
                st.info("👉 Anticipez, ne dormez pas sur vos acquis.")
        else:
            st.markdown(CONTENT.get(st.session_state.section, ""))

        st.markdown("<div class='footnote'>© Présenter - By Jérémie KPOGHOMOU - Data Scientist.</div>", unsafe_allow_html=True)
