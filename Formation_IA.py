import streamlit as st
from pathlib import Path
from PIL import Image
import io

# ------------------------------
# Page config & initial state
# ------------------------------
st.set_page_config(
    page_title="L'IA, le monde de demain  – Présentation interactive",
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
        "linkedin_logo": "Linkedin-Logo-PNG.png",
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

    .profile-profil {
        font-weight: 800;
        font-size: 1.2rem;
        color: purple;
        margin-top: 2px; margin-bottom: 6px;
    }

    .profile-info {
        font-size: 0.85rem;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
    }

    .profile-info img {
        width: 20px; height: 20px;
        margin-right: 6px;
        object-fit: contain;
    }

    .intro-box {
        background-color: #f5f5f5;
        border-radius: 16px;
        padding: 0px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
    }

    .intro-box img {
        margin: 0;
    }

    .footnote {
        font-size: 1rem;
        opacity: .8;
        margin-top: 10px;
        text-align: center;
    }

    .quiz-button {
        background-color: #FF5733;
        color: white;
        font-weight: bold;
        padding: 12px;
        border-radius: 12px;
        text-align: center;
        cursor: pointer;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.3);
    }

    .nice-button {
        display: inline-block;
        background: linear-gradient(90deg, #ff7e5f, #feb47b);
        color: white;
        font-weight: bold;
        padding: 12px 24px;
        border-radius: 12px;
        text-align: center;
        text-decoration: none;
        font-size: 1.1rem;
        transition: 0.3s;
    }
    .nice-button:hover {
        background: linear-gradient(90deg, #feb47b, #ff7e5f);
        transform: scale(1.05);
        cursor: pointer;
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
    if st.button("🔘 On|Off la Présentation"):
        st.session_state.presentation_on = not st.session_state.presentation_on

    show_qr_checkbox = st.checkbox("QRcode", value=False)
    if show_qr_checkbox:
        show_real_qr = st.checkbox("Afficher QRcode", value=True)
        if show_real_qr:
            qr_path = Path("QRCode_Formation_IA.png")
            if qr_path.exists():
                img_qr = Image.open(qr_path)
                st.image(img_qr, caption="🔗 QR Code", use_column_width=True)
            else:
                st.warning("Le fichier QRCode_Formation_IA.png est introuvable.")

    if st.session_state.presentation_on:
        selected_section = st.radio(
            label="SOMMAIRE",
            options=[
                "Introduction",
                "1. Présentation",
                "2. Comprendre l’IA et l’IA Générative",
                "3. Les Domaines de l’IA et Applications Utiles",
                "4. L'art du prompting",
                "4. Messages ciblés",
                "5. Utiliser l’IA pour Améliorer son CV",
                "6. Quiz de Fin de Formation (20 questions)",
                "7. Conclusion",
            ],
            index=0,
            key="radio_plan"
        )
        st.session_state.section = selected_section

        # Profil affiché dans le panneau gauche
        prof = st.session_state.profile
        img_path = Path(prof.get("image_path", ""))
        if img_path.exists():
            img = Image.open(img_path)
            img = img.resize((180, 200))
            st.image(img)
        else:
            st.warning("Aucune image valide trouvée.")

        st.markdown(f"<div class='profile-name'>{prof['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-profil'>{prof['profil']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='file://{prof['linkedin_logo']}' /> <a href='{prof['linkedin']}' target='_blank'>{prof['linkedin']}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'><img src='file://{prof['github_logo']}' /> <a href='{prof['github']}' target='_blank'>{prof['github']}</a></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='profile-info'>Email: <a href='mailto:{prof['email']}'>{prof['email']}</a></div>", unsafe_allow_html=True)

# ------------------------------
# RIGHT: Display section content dynamically
# ------------------------------
with right:
    if st.session_state.presentation_on:
        st.markdown("<div class='big-title' style='text-align: center;'>Comprendre le fonctionnement de l'IA et l'IA générative, améliorer son CV</div>", unsafe_allow_html=True)
        st.caption("L'IA, le monde de demain  – Présentation interactive")

        # Nouveau contenu injecté dans chaque section
        CONTENT = {
            "Introduction": "## Introduction & Objectifs de la Formation\n\n**🎯 Objectifs pédagogiques :**\n1. Comprendre ce qu’est l’Intelligence Artificielle (IA) et l’IA générative\n2. Découvrir les domaines et applications majeures de l’IA\n3. Apprendre à utiliser l’IA pour améliorer son CV\n4. Savoir rédiger des prompts efficaces pour générer du contenu pertinent\n5. Éviter les pièges courants liés à l’ATS et à la rédaction de CV\n6. Explorer les meilleurs sites et outils pour créer un CV optimisé.",
            "1. Présentation": "## 1. Présentation.\n\n**📌 Parcours Scolaire**\n\nExpériences professionnelles...",
            "2. Comprendre l’IA et l’IA Générative": "## 2. Comprendre l’IA et l’IA Génative.\n\n**🎯 Objectifs pédagogiques**\n\nComprendre ce qu’est l’Intelligence Artificielle (IA) et l’IA générative.\nDécouvrir les domaines et applications majeures de l’IA.\nApprendre à utiliser l’IA pour améliorer son CV.\nSavoir rédiger des prompts efficaces pour générer du contenu pertinent.\nÉviter les pièges courants liés à l’ATS et à la rédaction de CV.\nExplorer les meilleurs sites et outils pour créer un CV optimisé....",
            "3. Les Domaines de l’IA et Applications Utiles": "## 3. Les Domaines de l’IA et Applications Utiles\n\n**🧠 Définition de l’IA**\n\nComprendre ce qu’est l’Intelligence Artificielle (IA) et l’IA générative.\nIA (Intelligence Artificielle) : ensemble de technologies permettant à une machine d’imiter l’intelligence humaine (raisonner, apprendre, décider).\n\n**🖼️ Définition de l’IA générative**\n\nIA générative : branche de l’IA capable de créer du contenu nouveau (texte, image, vidéo, son).\nExemples : ChatGPT (texte), DALL-E (images), Midjourney, Claude AI.",
            "4. L'art du prompting": "## 4. L'art du prompting\n\nLe prompting est l’art de formuler correctement des requêtes à une IA générative pour obtenir un contenu pertinent et précis.",
            "4. Messages ciblés": "## 4. Messages ciblés\n\nCeci est une section simple pour afficher des messages aux différents profils.",
            "5. Utiliser l’IA pour Améliorer son CV": "## 5. Utiliser l’IA pour Améliorer son CV\n\n📌 Résumons tout en trois mots simples...",
            "6. Quiz de Fin de Formation (20 questions)": "## 6. Quiz de Fin de Formation (20 questions)\n\n✅ Oser rêver dès le collège...",
            "7. Conclusion": "## 7. Conclusion\n\n📌 L’avenir n’est pas une chance, c’est une responsabilité...",
        }

        current_section = st.session_state.section
        if current_section in CONTENT:
            st.markdown(CONTENT[current_section])

        # Ajout des checkbox demandées (uniquement ces 3 blocs, rien d'autre modifié)
        if current_section == "2. Comprendre l’IA et l’IA Générative":
            if st.checkbox("🎯 Objectif"):
                st.info("aaaaaa")
            if st.checkbox("📖 Présentation"):
                st.info("yyyyyy")
            

        if current_section == "4. L'art du prompting":
            if st.checkbox("⭐ Importance"):
                st.info("vsbsbsbssbsb")
            if st.checkbox("💡 Avantage"):
                st.info("oooooooooo")
            if st.checkbox("📋 Liste"):
                st.info("fffffffff")

        if current_section == "5. Utiliser l’IA pour Améliorer son CV":
            if st.checkbox("✅ Bonnes pratiques"):
                st.info("eeeeee")
            if st.checkbox("⚠️ Erreurs à éviter"):
                st.info("tttttttt")

        # Tableau comparatif et programme IA
        if current_section == "3. Les Domaines de l’IA et Applications Utiles":
            if st.checkbox("Afficher le tableau comparatif IA classique vs IA générative"):
                st.markdown("""
                | **IA classique**                        | **IA générative**                    |
                |----------------------------------------|-------------------------------------|
                | Analyse, prédit, classifie, optimise   | Crée du contenu original             |
                | Utilise des modèles prédictifs         | Utilise des modèles de langage (LLM) |
                | Répond à “Que se passera-t-il ?”       | Répond à “Invente quelque chose de nouveau” |
                | Ex. : Système de recommandation Netflix | Ex. : Rédaction automatique d’un CV personnalisé |
                """)

            if st.checkbox("Afficher le tableau comparatif Programme classique vs Programme IA"):
                st.markdown("""
                | **Programme / Script classique**        | **Programme utilisant l’IA**        |
                |----------------------------------------|-----------------------------------|
                | Suit des instructions fixes            | Apprend à partir de données        |
                | Ne s’adapte pas automatiquement        | Peut s’améliorer avec l’expérience |
                | Donne toujours le même résultat pour les mêmes données | Peut prédire ou générer des résultats nouveaux |
                | Exemple : script de calcul             | Exemple : modèle de prédiction de prix |
                """)

        # Messages ciblés
        if current_section == "4. Messages ciblés":
            if st.checkbox("Aux élèves et aux étudiants"):
                st.info("👉 Vous devez explorer, tester, être curieux, car le diplôme seul ne comptera pas.")
            if st.checkbox("Diplômés en recherche d'emploi"):
                st.info("👉 Votre valeur n’est pas définie par votre situation actuelle. Montrez vos talents, même à petite échelle.")
            if st.checkbox("Aux travailleurs"):
                st.info("👉 Le monde change, et vous devez vous réinventer.")

        # Section Quiz
        if current_section == "6. Quiz de Fin de Formation (20 questions)":
            if st.button("📲 Cliquez ici pour voir le QR Code du Quiz"):
                qr_path = Path("Quiz_sépa_en_2_IA.png")
                if qr_path.exists():
                    img_qr = Image.open(qr_path)
                    img_qr = img_qr.resize((200, 180))
                    st.image(img_qr, caption="Scannez pour accéder au Quiz")
                else:
                    st.warning("⚠️ QR Code introuvable, vérifiez le fichier.")

        st.markdown("<div class='footnote'>© Présentation - By Jérémie KPOGHOMOU - Data Scientist.</div>", unsafe_allow_html=True)
