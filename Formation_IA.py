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
        font-size: clamp(18px, 5vw, 35px);
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
                st.warning("Le fichier QRCode_Quiz.png est introuvable.")

    if st.session_state.presentation_on:
        selected_section = st.radio(
            label="SOMMAIRE",
            options=[
                "Introduction",
                "1. Présentation",
                "2. Comprendre l’IA et l’IA Générative",
                "3. Les Domaines de l’IA et Applications Utiles",
                "4. L'art du prompting",
                #"4. Messages ciblés",
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
            "Introduction": "## Introduction et Objectifs de la Formation\n\n**🎯 Objectifs pédagogiques :**\n1. Comprendre ce qu’est l’Intelligence Artificielle (IA) et l’IA générative\n2. Découvrir les domaines et applications majeures de l’IA\n\n3. Savoir rédiger des prompts efficaces pour générer du contenu pertinent \n\n4. Apprendre à utiliser l’IA pour améliorer son CV.\n\n5. Éviter les pièges courants liés à l’ATS et à la rédaction de CV\n\n6. Explorer les meilleurs sites et outils pour créer un CV optimisé.",
            "1. Présentation": "## 1. Présentation.\n\n**💼 Décrire vos parcours pour comprendre les attentes et les adapter**\n\n**📖 Me présenter**\n\n- Parcours scolaire\n\n- Professionnel",
            "2. Comprendre l’IA et l’IA Générative": "## 2. Comprendre l’IA et l’IA Générative.\n\n**🎯 Bon à savoir**\n\nLes spécifisités de l'IA classique et l'IA générative.",
            "3. Les Domaines de l’IA et Applications Utiles": "## 3. Les Domaines de l’IA et Applications Utiles.",
            "4. L'art du prompting": "## 4. L'art du prompting\n\nLe prompting est **l’art de formuler correctement des requêtes** à une IA générative pour obtenir un contenu pertinent et précis.",
            #"4. Messages ciblés": "## 4. Messages ciblés\n\nCeci est une section simple pour afficher des messages aux différents profils.",
            "5. Utiliser l’IA pour Améliorer son CV": "## 5. Utiliser l’IA pour Améliorer son CV..",
            "6. Quiz de Fin de Formation (20 questions)": "## 6. Quiz de Fin de Formation (20 questions)\n\n✅ Oser rêver dès le collège...",
            "7. Conclusion": "## 7. Conclusion\n\n📌 L’avenir n’est pas une chance, c’est une responsabilité...",
        }

        current_section = st.session_state.section
        if current_section in CONTENT:
            st.markdown(CONTENT[current_section])

        # Ajout des checkbox demandées (uniquement ces 3 blocs, rien d'autre modifié)
        if current_section == "2. Comprendre l’IA et l’IA Générative":
            if st.checkbox("🧠 Définition de l'IA"):
                st.info("**L’intelligence artificielle (IA)** est l’ensemble des méthodes, technologies et systèmes informatiques qui permettent à des machines d’accomplir des tâches nécessitant normalement l’intelligence humaine, comme **l’apprentissage, le raisonnement, la résolution de problèmes, la perception ou la prise de décision**.")
            if st.checkbox("🛠️ But"):
                st.info("1- Automatisation des tâches répétitives. \n\n2- Créativité et innovation. Ex: L'IA générative crée du contenu nouveau (ChatGPT pour du texte, DALL-E pour les images, son, vidéo).\n\n3- Amélioration de la productivité, Aide à la décision et Amélioration de la productivité.")
            if st.checkbox("🔑 Le tableau comparatif IA Classique vs IA Générative"):
                st.info("Répond à “Que se passera-t-il ?” | Répond à “Invente quelque chose de nouveau”.")
                st.markdown("""
                | Aspect            | IA Classique                          | IA Générative                     |
|-------------------|---------------------------------------|-----------------------------------|
| *Objectif*      | Analyser, prédire, classer           | Créer du contenu nouveau          |
| *Techniques*    | Machine Learning, Deep Learning      | GANs 🖼️, Transformers 📝                |
| *Usages*        | Aide à la décision, automatisation   | Créativité, contenu personnalisé  |
| *Exemples*      | Reconnaissance d'images, diagnostics médical ,Système de recommandation (facebook ou Netflix) | ChatGPT, DALL-E, génération audio |

                """)
            if st.checkbox("⭐ Programme classique vs Programme IA"):
                st.markdown("""
                | **Programme / Script classique**        | **Programme utilisant l’IA**        |
                |----------------------------------------|-----------------------------------|
                | Suit des instructions fixes            | Apprend à partir de données        |
                | Ne s’adapte pas automatiquement        | Peut s’améliorer avec l’expérience |
                | Donne toujours le même résultat pour les mêmes données | Peut prédire ou générer des résultats nouveaux |
                | Exemple : script de présentation(https://github.com/Jere623/Jeremie-Kpoghomou/edit/main/Formation_IA.py) et Quiz(https://script.google.com/u/0/home/projects/1KaG6heGhOmc-O56AmUgzIQwNWqHk9HV_hJokGk5wkTN4jW8O-EgcVKI-/edit?pli=1) | Exemple : modèle de prédiction de prix |
                """)

                
            
        # Tableau comparatif et programme IA
        if current_section == "4. L'art du prompting":
            if st.checkbox("⭐ Caractéristiques et Avantage d’un Prompt"):
                st.info("Le prompting bien fait maximise la pertinence et l'efficacité des réponses de l'IA")
                st.markdown("""
| **Caractéristique**         | **Avantages**                                                           |
| --------------------------- | -------------------------------------------------------------------------------------- |
| **Clarté**                  | Évite les réponses hors sujet ou vagues                                                |
| **Précision**               | Plus le prompt est précis, plus la réponse est pertinente                              |
| **Contexte**                | Permet à l’IA d’adapter le ton, le style et la difficulté                              |
| **Format demandé**          | Facilite l’exploitation directe de la réponse (liste, tableau, plan…)                  |
| **Contraintes**             | Guide l’IA vers un résultat utilisable (longueur, style, exemples inclus)              |
| **Rôle défini** (optionnel) | Améliore la qualité en donnant une perspective (ex. “agis comme un coach en carrière”) |
 """)
                
                
            if st.checkbox("💡 Structure d'un bon prompt"):
                st.info("Des prompts efficaces permettent de gagner du temps et d'obtenir un contenu exploitable directement.")
                st.markdown(""" 
                - Sois clair (ce que tu veux).
                - Donne le contexte (pour qui, dans quel but).
                - Spécifie le format (liste, plan, tableau, texte court…).
                - Ajoute des contraintes (longueur, style, ton, exemples).
                - Ajuste si la première réponse n’est pas parfaite (prompting = dialogue).
                """)
            if st.checkbox("✅ Bonnes pratiques et ⚠️ Erreurs à éviter"):
                st.info("👉 Checklist : clair, précis, contexte, format, attentes, contraintes.")
                st.markdown(""" 

|✅ **Bonne Pratique**        | ❌ **Erreur fréquente**  | 💡 **Exemple**                   |    
| -------------------------- |-------------------| --------------------------------------------- |
| Donner un rôle         |  Prompt trop vague : “Parle-moi d’IA”           | Agis comme un coach carrière…               |
| Définir le public     |  Pas de contexte : “Écris un mail”    | “Explique pour un débutant…”                  |
| Spécifier le format    |   Demande trop longue et floue    |“Présente sous forme de tableau…”             |
| Ajouter un contexte  | Demande contradictoire : “Fais court mais très détaillé”  | “Je prépare un pitch pour des investisseurs…” |
| Mettre des contraintes |           | “En 100 mots, avec 3 exemples…”               |
| Découper les demandes  |             |“D’abord fais un plan, puis développe…”       |
 """)

        
                
        if current_section == "5. Utiliser l’IA pour Améliorer son CV":
            if st.checkbox("🛠️ Étapes concrètes"):
                st.info("")
                st.markdown("""
                        1. Analyse du CV actuel : demander à l’IA un audit et suggestions. 
                        2. Extraction de mots-clés : coller l’offre d’emploi et demander les compétences prioritaires. 
                        3. Réécriture ciblée : générer des phrases percutantes, adaptées ATS. 
                        4. Optimisation de la mise en page : conseils de lisibilité et de formatage.
                        
                        """)
            if st.checkbox("🌐 Outils recommandés"):
                st.markdown("""
                        * ChatGPT / Claude AI : rédaction et amélioration du contenu 
                        * Resumeworded / Jobscan : scoring ATS
                        - 📌 Design et mise en page
                        * Canva (https://www.canva.com/design/DAGswU6QT2w/NHYgZxhHCb5jC1lSy7Fo1w/edit)
                        * Freepik (https://www.freepik.com/pikaso/ai-image-generator?sign-up=email) 
                        * Zety (https://builder.zety.com/resume) 
                        """)

        # Tableau comparatif et programme IA
        if current_section == "3. Les Domaines de l’IA et Applications Utiles":
            if st.checkbox("Les nouveaux métiers à l'ere de l'IA"):
                st.markdown(""" | **Métier**                            | **Rôle principal**                                                                             |
| ------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Ingénieur Prompt** (Prompt Engineer)    | Crée des prompts précis et optimisés pour obtenir les meilleures réponses des IA génératives.  |
| **Data Scientist**                        | Analyse les données, entraîne des modèles d’IA et en tire des insights exploitables.           |
| Éthicien de l’IA                      | Définit les règles d’éthique pour l’utilisation responsable des IA.                            |
| Spécialiste en Gouvernance de l’IA    | Supervise les politiques de sécurité, conformité et transparence des IA.                       |
| Entraîneur de modèles (AI Trainer)    | Fournit des données d’exemple pour améliorer les modèles d’IA.                                 |
| Spécialiste en Sécurité de l’IA       | Protège les modèles d’attaques, empêche les biais malveillants et garantit la confidentialité. |
| Ingénieur MLOps                       | Met en production les modèles d’IA et assure leur suivi et mise à jour.                        |
| Développeur d’Agents Conversationnels | Conçoit et optimise des chatbots intelligents et personnalisés.                                |
| Architecte d’IA Générative            | Met en place l’infrastructure technique pour déployer des modèles génératifs à grande échelle. |
| Machine Learning Engineer              | Met en production des modèles de ML/IA, optimise leur performance et leur scalabilité.                              |
| MLOps Engineer                         | Automatise le déploiement, le suivi et la mise à jour des modèles en production.                                    |
| Spécialiste en Data éthique            | Définit des règles pour éviter les biais et garantir la conformité RGPD.                                            |
| **Data Governance Analyst**                | Supervise la qualité, la sécurité et l’accès aux données au sein de l’entreprise.                                   |
| Data Product Manager                   | Conçoit des produits data (API, dashboards, pipelines) en alignement avec les besoins métier.                       |
| Spécialiste en Données Synthétiques    | Génère des datasets artificiels pour entraîner des modèles tout en préservant la vie privée.                        |
| AI Data Trainer                        | Alimente les modèles avec des jeux de données représentatifs et valide les sorties générées.                        |
| Data Storyteller                       | Transforme les résultats de l’IA en insights clairs et percutants pour les décideurs.                               |
| Responsable de l’Explicabilité de l’IA | Analyse les modèles et explique leurs décisions de manière compréhensible pour les utilisateurs et les régulateurs. |
| Analyste en Détection de Biais         | Identifie et corrige les biais dans les datasets et les modèles IA.                                                 |

                
                """)

            if st.checkbox("Métiers sous menace avec l’arrivée de l’IA"):
                st.markdown(""" | **Métier**                                        | **Raison de la menace**                                                      |
| ------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Agent de saisie / Opérateur de données**            | L’IA peut lire, extraire et remplir des formulaires automatiquement.         |
| **Secrétaire administratif**                          | L’IA gère les agendas, écrit des mails, répond aux questions fréquentes.     |
| **Comptables**                              | L’IA peut automatiser la saisie comptable, la détection d’erreurs et la génération de rapports financiers.           |
| **Statisticiens simples**                   | Les outils d’IA et de visualisation automatisée remplacent les analyses descriptives basiques.                       |
| Secrétaires                             | L’IA (chatbots, assistants virtuels) automatise la planification, la rédaction d’e-mails et la gestion de documents. |
| Téléopérateur / Centre d’appel                    | Chatbots et assistants vocaux automatisent les réponses simples.             |
| Rédacteur de contenu basique (SEO, blogs simples) | IA générative peut écrire articles, descriptions produits, newsletters.      |
| **Traducteur de documents simples**                   | IA traduit rapidement et avec bonne qualité (DeepL, GPT).                    |
| Analyste junior / Comptable de premier niveau     | IA peut analyser des états financiers et détecter des anomalies.             |
| **Assistant juridique**                               | IA peut rédiger des contrats simples et effectuer des recherches juridiques. |
| Ouvrier sur chaîne de production simple           | Robots + vision par ordinateur = automatisation complète.                    |
| Cariste / Manutentionnaire                        | Véhicules autonomes et robots logistiques remplacent le travail humain.      |
| Caissier(e)                                       | Développement des caisses automatiques + paiement sans contact.              |
| Commerciaux pour produits simples                 | L’IA peut personnaliser les offres et faire des recommandations.             |
| Graphiste d’entrée de gamme                       | IA (DALL-E, Midjourney) peut générer logos, affiches simples.                |
| Monteur vidéo basique                             | Outils comme Runway, Pictory automatisent le montage.                        |
| **Traducteurs de base**                     | Les IA de traduction (DeepL, GPT) offrent des traductions rapides et précises.                                       |
| **Journalistes de synthèse**                | L’IA peut rédiger des articles courts (résumés, résultats sportifs, météo) automatiquement.                          |
| Télévendeurs                            | Les callbots gèrent les appels de prospection et les réponses standardisées.                                         |

                
                """)
            if st.checkbox("🛠️ Conclusion"):
                st.info("**🧠 A retenir**")
                st.markdown(""" L’**IA** n’est pas le futur, *elle est déjà là*. Chaque jour, elle transforme nos métiers, nos entreprises et notre façon de vivre.

Ceux qui *attendent* verront leurs emplois disparaître.
Ceux qui *agissent* deviendront les acteurs de demain.

🔥 **Se former** n’est plus une option, c’est une obligation pour rester compétitif.

🚀 **Les métiers porteurs** (IA, data, cybersécurité, green tech…) sont les nouvelles opportunités.

💡 **Votre valeur professionnelle** dépendra de votre capacité à comprendre, utiliser et maîtriser l’IA.

📢 Message clé : On ne peut pas arrêter le vent, mais on peut apprendre à construire des éoliennes.
L’avenir appartient à ceux qui **embrassent le changement et se réinventent avant qu’il ne soit trop tard**.""")


        # Messages ciblés
#        if current_section == "4. Messages ciblés":
#            if st.checkbox("Aux élèves et aux étudiants"):
#                st.info("👉 Vous devez explorer, tester, être curieux, car le diplôme seul ne comptera pas.")
#            if st.checkbox("Diplômés en recherche d'emploi"):
#                st.info("👉 Votre valeur n’est pas définie par votre situation actuelle. Montrez vos talents, même à petite échelle.")
#            if st.checkbox("Aux travailleurs"):
#                st.info("👉 Le monde change, et vous devez vous réinventer.")

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
                    
        if current_section == "7. Conclusion":
            st.markdown("""
                    - L'IA est un outil puissant pour améliorer vos compétences et votre visibilité.
                    - Maîtriser le prompting et l'utilisation des outils IA est essentiel.
                    - Intégrer l'IA dans votre parcours professionnel avec prudence et stratégie.
                    """)

        st.markdown("<div class='footnote'>© Présentation - By Jérémie KPOGHOMOU - Data Scientist.</div>", unsafe_allow_html=True)
