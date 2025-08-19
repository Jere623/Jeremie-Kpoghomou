import streamlit as st
from PIL import Image
from pathlib import Path
import io

# ------------------------------
# Page config & initial state
# ------------------------------
st.set_page_config(
    page_title="Oser c'est deverouiller  – Présentation interactive",
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
        "image_path": "KPOGHOMOU-Style libre-102x152 mm.jpg",
        "linkedin": "https://www.linkedin.com/in/jérémiekpoghomou/",
        "email": "jeremie.kpoghomou77@gmail.com",
        "github": "https://github.com/Jere623",
        "linkedin_logo": "LinkedIn_icon.svg.png",
        "github_logo": "GitHub-cat-logo.jpg",
    }

# ------------------------------
# Custom CSS (animations & style)
# ------------------------------
st.markdown(
    """
    <style>
    :root { --radius: 16px; }

    .big-title {
        font-weight: 800;
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
        color: purple; /* VIOLET */
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
left, right = st.columns([1, 3])

with left:
    if st.button("🔘 On|Off  la Présentation"):
        st.session_state.presentation_on = not st.session_state.presentation_on

    # ✅ Affichage QRCode depuis fichier
    show_qr_checkbox = st.checkbox("QRcode", value=False)
    if show_qr_checkbox:
        show_real_qr = st.checkbox("Afficher QRcode", value=False)
        if show_real_qr:
            qr_path = Path("QRCode_oserrever.png")
            if qr_path.exists():
                img_qr = Image.open(qr_path)
                st.image(img_qr, caption="🔗 QR Code", use_column_width=True)
            else:
                st.warning("Le fichier QRCode_oserrever.png est introuvable.")

    if st.session_state.presentation_on:
        selected_section = st.radio(
            label="",
            options=[
                "Introduction",
                "1. Oser rêver",
                "2. Choisir avec courage",
                "3. Construire pas à pas",
                "4. Mon parcours comme illustration",
                "5. Messages ciblés",
                "6. Trois trois (3) mots clés universelles",
                "7. Conclusion",  # ✅ corrigé
            ],
            index=0,
            key="radio_plan"
        )
        st.session_state.section = selected_section

        # Profil
        prof = st.session_state.profile
        img_path = Path(prof.get("image_path", ""))
        if img_path.exists():
            img = Image.open(img_path)
            img = img.resize((180, 200))
            st.image(img)
        else:
            st.warning("Aucune image valide trouvée.")

        st.markdown(f"<div class='profile-name'>{prof.get('name','')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-profil'>{prof.get('profil','')}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='file://{prof.get('linkedin_logo','')}' /> <a href='{prof.get('linkedin','')}' target='_blank'>{prof.get('linkedin','')}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='file://{prof.get('github_logo','')}' /> <a href='{prof.get('github','')}' target='_blank'>{prof.get('github','')}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'>Email: <a href='mailto:{prof.get('email','')}'>{prof.get('email','')}</a></div>", unsafe_allow_html=True)

# ------------------------------
# RIGHT content
# ------------------------------
with right:
    if st.session_state.presentation_on:

        # ----------- CONTENU PRINCIPAL ----------
        st.markdown("<div class='big-title' style='text-align: center;'>Oser rêver, choisir et construire son avenir</div>", unsafe_allow_html=True)

        st.caption("Présentation interactive – radio cliquable, édition et animations")

        CONTENT = {
            "Introduction": "## Introduction\n\n**Trois questions essentielles:**\n\n1. Quel est mon talent ?\n\n2. Quelle voie choisir ?\n\n3. Comment bâtir ma carrière pas à pas ?.",
            
            "1. Oser rêver": "## 1. Oser rêver.\n\n**Pourquoi rêver est indispensable ?**\n\nSans rêve, on avance sans boussole. On subit les choix des autres, on vit dans la routine, c'est l'horizon qui guide nos pas.\n\n Exemple concret: l'innovation = c'est le fruit du rêve ",
            
            "2. Choisir avec courage": "## 2. Passer de l’intention à l’action.\n\n**Pourquoi le choix fait peur ?**\n\nLa clé du choix : il faut oser franchir le pas.\n\n Exemple : ose planter, même avec des doutes, verra pousser des fruits.",
            
            "3. Construire pas à pas": "## 3. Faire de son avenir une réalité\n\nConstruire, c’est accepter le temps et l’effort.\n\n**Les ingrédients de la construction :**\n\n La discipline\n\n L’apprentissage\n\n La persévérance",
           
            "4. Mon parcours comme illustration": "## 4. Mon parcours comme illustration\n\n Licence en Économie-Gestion\n\n Triple Master : Data Science, Statistiques appliquées, Finances publiques\n\n Forces : analyse, rigueur, curiosité face aux chiffres.\n\n Orientation stratégique vers un domaine porteur.",
            
            "5. Messages ciblés": None,
            
            "6. Trois trois (3) mots clés universelles": "## 6. Trois trois (3) mots clés universelles\n\n Résumons tout en trois mots simples:\n\n 👉 Rêver : pour savoir où aller.\n\n 👉 Choisir : pour oser avancer.\n\n 👉 Construire : pour donner une réalité à vos projets.",
            
            "7. Conclusion": "## 7. Conclusion\n\n**l’avenir n’est pas une chance, c’est une responsabilité.**\n\n Il ne dépend pas seulement de vos conditions, mais de votre capacité à rêver, à choisir et à construire.\n\n Votre avenir commence aujourd’hui. Pas demain, pas dans un an : aujourd’hui.",
        }

        if st.session_state.section == "5. Messages ciblés":
            st.subheader("📌 Messages ciblés")
            etudiants = st.checkbox("Aux élèves et aux Aux étudiants", value=False)
            if etudiants:
                st.info("👉 vous devez explorer, tester, être curieux, car le diplôme seul ne comptera pas.")

            diplomes = st.checkbox("Diplômés sans emploi", value=False)
            if diplomes:
                st.info("👉 Votre valeur n’est pas définie par votre situation actuelle. Montrez vos talents, même à petite échelle.")

            travailleurs = st.checkbox("Aux travailleurs", value=False)
            if travailleurs:
                st.info("👉 Le monde change, et vous devez vous réinventer.")

        else:
            st.markdown(CONTENT.get(st.session_state.section, ""))

        st.markdown("<div class='footnote'>© Présenter - By Jérémie KPOGHOMOU - Data Scientist.</div>", unsafe_allow_html=True)
