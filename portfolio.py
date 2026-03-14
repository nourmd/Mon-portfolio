import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Nourhen Maddouri | AI Engineer Portfolio",
    layout="wide",
)

# ================= Sidebar =================
with st.sidebar:
    st.title("Nourhen Maddouri")

    st.markdown("""
    **Ingénieure en Intelligence Artificielle**  
    Spécialisation : **LLM · RAG · Agents IA**
    """)

    st.write("📍 Ariana, Tunis, Tunisie")

    st.markdown("---")

    st.success("Disponible immédiatement")

    st.write("nourhenemd@gmail.com")
    st.write("+216 92 384 193")

    st.markdown("[LinkedIn](https://www.linkedin.com/in/nourhen-maddouri)")

# ================= Tabs =================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Accueil", 
    "🚀 Projets", 
    "💼 Expériences", 
    "🛠 Compétences", 
    "🎓 Formation"
])

# ================= Accueil =================
with tab1:
    col1, col2 = st.columns([2,1])
    with col1:
        st.title("Bonjour, je suis Nourhen Maddouri ")

        st.write("""
Diplômée d'un **Master en Data Science**, je suis spécialisée dans le développement
de solutions d'intelligence artificielle basées sur les **Large Language Models (LLM)**,
les architectures **Retrieval-Augmented Generation (RAG)** et les **agents IA autonomes**.

Je développe des systèmes intelligents permettant l'analyse automatique de documents,
l'extraction d'informations à partir de CV et le **matching sémantique entre profils
et offres d’emploi**, ainsi que des agents IA capables de recommander des actions
ou des formations adaptées.
""")

        st.success(
        "Actuellement à la recherche d’un poste en **Intelligence Artificielle / LLM / NLP**."
        )

    with col2:
        st.metric("Projets IA réalisés", "6+")
        st.metric("Technologies maîtrisées", "10+")
        st.metric("Stage IA", "2")

# ================= Projets =================
with tab2:
    st.header("Projets en Intelligence Artificielle")

    with st.expander("Module de matching CV – Offres d’emploi & Agent IA de recommandation de formations (Projet principal)", expanded=True):
        st.subheader("Architecture du système")

        st.write("""
1️⃣ Extraction de texte depuis les CV (PDF / Word / images)  
2️⃣ Extraction des informations avec LLM  
3️⃣ Génération d'embeddings pour CV et offres  
4️⃣ Matching sémantique avec FAISS  
5️⃣ Agent IA proposant des recommandations de formations  
6️⃣ Intégration dans une application web via API REST
""")
        st.write("""
    **Conception et développement d'un système intelligent de recrutement basé sur les LLM,
    l'architecture RAG et des agents IA autonomes.**

    Le système analyse automatiquement les CV et les compare aux offres d’emploi
    afin d'identifier les candidats les plus pertinents. Il propose également
    des recommandations de formations adaptées pour améliorer les compétences
    des candidats ou des employés.
    """)

        st.subheader("Fonctionnalités principales")

        st.write("""
    • Extraction automatique d'informations à partir de CV (PDF, Word, CV scannés)  
    • Identification des compétences, expériences, formations et langues  
    • Génération d'embeddings pour CV et offres d’emploi  
    • Recherche sémantique et calcul de similarité entre candidats et postes  
    • Recommandation intelligente de formations via un agent IA  
    """)

        st.subheader("Architecture IA")

        st.write("""
    • Pipeline RAG pour la récupération d'informations pertinentes  
    • Utilisation de modèles LLM pour l'extraction et la structuration des données  
    • Base vectorielle FAISS pour la recherche sémantique  
    • Agent IA capable d'analyser un profil et proposer des recommandations de formations
    """)

        st.subheader("Intégration dans une application complète")

        st.write("""
    Le système a été intégré dans une application web permettant
    l'utilisation des fonctionnalités par les recruteurs.

    • Backend : Django  
    • Frontend : Angular  
    • API : REST API  
    • Gestion des tâches asynchrones : RabbitMQ  
    """)

        st.subheader("Technologies utilisées")

        st.write("""
    Python • LangChain • Mistral • Ollama • FAISS • Transformers  
    Django • Angular • REST API • RabbitMQ • PostgreSQL
    """)

        st.subheader("Résultats obtenus")

        st.write("""
• Automatisation de l'analyse de CV et offres d’emploi  
• Amélioration de la précision du matching sémantique  
• Réduction du temps d'analyse des candidatures  
• Recommandation intelligente de formations pour améliorer les compétences
""")

        st.subheader("Impact du projet")

        st.write("""
    Ce système permet d'automatiser l'analyse de centaines de CV
    et d'améliorer le processus de recrutement grâce à l'analyse
    sémantique et aux recommandations intelligentes de formations.
    """)

    with st.expander("Module de classification des images échographiques"):
        st.write("""
        Développement d'un pipeline permettant de classifier les images échographiques
        """)

        st.subheader("Fonctionnalités")

        st.write("""
        • Préparation des données
        • Prétraitement des données 
        • Augmentation et équilibrage des deux classes
        • Implémentation d'un FCNN avec un CNN pour la classification
        • Évaluation      
        """)

        st.subheader("Technologies")

        st.write("""
        Python • Keras • CNN/FCNN 
        """)

    with st.expander("Système de résumé automatique d'articles"):
        st.write("""
        Implémentation d'un système de résumé automatique d'articles scientifiques
        en utilisant des modèles de type Transformers.
        """)

        st.subheader("Fonctionnalités")

        st.write("""
        • Prétraitement des documents  
        • Génération automatique de résumés  
        • Évaluation des performances des modèles
        """)

        st.subheader("Technologies")

        st.write("""
        Python • NLP • Transformers • BART
        """)

# ================= Expériences =================
with tab3:
    st.header("Expériences professionnelles")

    st.subheader("Stage de fin d'études – Data Science & Intelligence Artificielle")

    st.write("""
    **Looyas Digital Solutions – Tunis**  
    Février 2025 – Août 2025
    """)

    st.write("""
    Participation au développement d'une plateforme intelligente de recrutement
    basée sur les technologies de traitement du langage naturel et les modèles
    de langage de grande taille (LLM).
    """)

    st.subheader("Responsabilités")

    st.write("""
• Conception d'un pipeline RAG pour l'analyse de CV et d’offres d’emploi  
• Extraction automatique d'informations à partir de documents (CV)  
• Génération d'embeddings et recherche sémantique pour le matching  
• Développement d'un agent IA de recommandation de formations  
• Intégration du système dans une application web complète  
• Développement d'API REST pour connecter les modules IA à l'application  
• Mise en place d'un système de tâches asynchrones avec RabbitMQ
""")

    st.subheader("Technologies")

    st.write("""
    Python • NLP • LLM • RAG • LangChain • Transformers • PostgreSQL • Django • RabbitMQ
    """)

    st.subheader("Stage Deep Learning – Computer Vision")

    st.write("""
    **IDEA Lab – Bizerte**  
    Février 2023 – Juin 2023
    """)

    st.write("""
    Développement d'un modèle de Deep Learning pour l'analyse d'images médicales.
    """)

    st.subheader("Travaux réalisés")

    st.write("""
    • Prétraitement de données d'images médicales  
    • Conception et entraînement d'un modèle CNN  
    • Évaluation des performances du modèle  
    • Développement d'une application web pour visualiser les résultats
    """)

    st.subheader("Technologies")

    st.write("""
    Python • TensorFlow • Keras • Computer Vision • CNN/FCNN
    """)

# ================= Compétences =================
with tab4:
    st.header("Compétences techniques")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("IA & Machine Learning")
        st.write("Transformers")
        st.write("NLP")
        st.write("RAG")
        st.write("LLM")
    with col2:
        st.subheader("Outils & Frameworks")
        st.write("LangChain")
        st.write("Mistral / Ollama")
        st.write("FAISS")
        st.write("FastAPI / Django")
        st.write("Git")    
    with col3:
        st.subheader("Langages")
        st.write("Python")
        st.write("SQL")

# ================= Formation =================
with tab5:
    st.header("Formation")

    st.write("""
    **Master Professionnel en Data Science**  
             
    Faculté des Sciences de Bizerte  
    2023 – 2025
    """)

    st.write("""
    **Licence en Sciences Informatiques**
             
    Faculté des Sciences de Bizerte  
    2020 – 2023
    """)


st.markdown("---")
st.markdown("Portfolio réalisé avec Streamlit | Dernière mise à jour : Mars 2026")