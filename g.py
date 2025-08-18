import streamlit as st
from PIL import Image
from pathlib import Path
import qrcode   # ✅ on utilise qrcode à la place de segno
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
        width: 10px; height: 10px;
        margin-right: 3px;
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

    # ✅ QR Code
    show_qr_checkbox = st.checkbox("QRcode", value=False)
    if show_qr_checkbox:
        show_real_qr = st.checkbox("Afficher QRcode", value=False)
        if show_real_qr:
            qr = qrcode.QRCode(box_size=10, border=4)
            qr.add_data("https://jeremiekpo77.streamlit.app/")  # <-- lien du QR code
            qr.make(fit=True)
            img_qr = qr.make_image(fill="black", back_color="white")
            buf = io.BytesIO()
            img_qr.save(buf, format="PNG")
            buf.seek(0)
            st.image(buf, caption="🔗 QR Code", use_column_width=True)
