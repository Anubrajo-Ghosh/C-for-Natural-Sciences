import streamlit as st

def render():
    # --- Hero Section (Blue Theme) ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 40px; border-radius: 15px; text-align: center; margin-bottom: 30px;">
            <h1 style="color: white; margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; font-size: 3rem;">
                C for Natural Sciences
            </h1>
            <p style="color: #a0c4ff; font-size: 1.2rem; font-weight: 300;">
                <b>Bridging Biological Logic with Computational Power</b>
            </p>
        </div>
    ''', unsafe_allow_html=True)

    # --- Introduction Columns ---
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📌 Project Overview")
        st.write("""
        This platform is designed as a teachable resource for the **MDS (Multidisciplinary Studies)** paper: 
        *AI for Natural Sciences*. As science moves toward a data-driven future, the efficiency 
        of the C programming language remains the backbone of bioinformatics, molecular modeling, 
        and high-speed genomic sequencing.
        """)

        st.markdown("""
        **Why C in Microbiology?**
        * **Speed:** Processing millions of DNA base pairs requires the raw performance of C.
        * **Memory Control:** Pointers allow us to handle large datasets without crashing lab hardware.
        * **Hardware Integration:** C talks directly to sensors, incubators, and sequencers.
        """)

    with col2:
        # FIX: Corrected student profile — MCBA department, not "Minor: Computer Science"
        st.markdown('''
            <div style="background-color: #f0f4f8; padding: 20px; border-radius: 10px; border: 1px solid #00599C;">
                <h4 style="color: #00599C; margin-top: 0;">🎓 Student Profile</h4>
                <p style="font-size: 0.9rem; color: #333;">
                    <b>Name:</b> Anubrajo Ghosh <br>
                    <b>Roll No.:</b> 0618 <br>
                    <b>Department:</b> MCBA (Microbiology)<br>
                    <b>Year / Sem:</b> 1st Year, Semester 2<br>
                    <b>Paper:</b> MDS — AI for Natural Sciences<br>
                    <b>Focus:</b> Bioinformatics & Computational Biology using C Programming Language
                </p>
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- The 15-Module Roadmap ---
    # FIX: Corrected "12-Module Roadmap" → "15-Module Roadmap" (actual count is 15 chapters + home + lab repo)

    st.subheader("🚀 Learning Path — 15 Core Modules")
    st.write("Navigate through the sidebar to explore all modules of this curriculum:")

    m1, m2, m3 = st.columns(3)

    with m1:
        # FIX: Replaced st.info() (blue) — already correct colour, kept as is
        st.info("**📘 Foundations**\n\n1. Language Generations\n2. History of C\n3. Program Structure\n4. Data Types\n5. Operators")

    with m2:
        # FIX: Replaced st.success() (green) with st.info() to keep consistent blue brand colour
        st.info("**💻 Core Syntax**\n\n6. Input & Output\n7. Selection & Control\n8. Iterations & Loops\n9. Functions\n10. Arrays & Pointers")

    with m3:
        # FIX: Replaced st.warning() (orange) with st.info() for consistent blue brand colour
        st.info("**🔬 Advanced Topics**\n\n11. Storage Classes\n12. Structures & Unions\n13. File Handling\n14. Strings & Sequences\n15. Libraries & Math")

    st.divider()

    # --- Quick Navigation Guide ---
    st.subheader("🧭 How to Navigate This Website")
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        st.markdown('''
            <div style="background-color: #00599C; padding: 16px; border-radius: 8px; border-left: 4px solid #00599C;">
                <b style="color: #FFFFFF;">📚 Study Modules (1–15)</b><br><br>
                Each module covers one topic with:<br>
                • Learning objective<br>
                • Concept explanation with code examples<br>
                • MDS / Microbiology application box<br>
                • Quick Review quiz (5 questions)
            </div>
        ''', unsafe_allow_html=True)
    with nav_col2:
        st.markdown('''
            <div style="background-color: #00599C; padding: 16px; border-radius: 8px; border-left: 4px solid #00599C;">
                <b style="color: #FFFFFF;">🧪 Lab Repository (Module 16)</b><br><br>
                A curated archive of verified C programs:<br>
                • Foundations, Logic & Loops<br>
                • Functions & Recursion<br>
                • Arrays & Structures<br>
                • Bio-C Specialization (DNA, Growth, Enzymes, Proteins)
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- Footer ---
    st.markdown('''
        <div style="text-align: center; color: #7d8590; font-size: 0.90rem; padding: 20px;">
            <b>Anubrajo Ghosh | Roll No. - 0618</b><br>
            <b>Developed for the 2026 Academic Session | MDS Paper: AI for Natural Sciences | Semester 2 | St. Xavier's College (Autonomous), Kolkata</b>
        </div>
    ''', unsafe_allow_html=True)

if __name__ == "__main__":
    render()