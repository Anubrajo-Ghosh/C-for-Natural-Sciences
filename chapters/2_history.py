import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a; margin-bottom: 30px;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🌐 Module 2: The Chronicles of C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Tracing the Evolution from Silicon to Software</p>
        </div>
    ''', unsafe_allow_html=True)

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to trace the full lineage of C from ALGOL to C23, identify the key figures who shaped it, and explain why C remains relevant in modern scientific computing.")

    st.write("")

    # --- SECTION 1: THE FOUNDERS ---
    # FIX: Removed duplicate st.columns() call (was defined twice on consecutive lines)
    st.header("👥 The Architects of Modern Computing")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('''
            <div style="text-align: justify; padding-right: 10px;">
                <h3 style="color: #00599C;">Dennis Ritchie</h3>
                <p>Known as the <b>'Father of C'</b>, he created the language at AT&T Bell Labs between 1969–1973.
                His goal was to build a language powerful enough to rewrite the <b>UNIX Operating System</b>,
                moving it away from machine-specific Assembly code. He passed away in 2011.</p>
            </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown('''
            <div style="text-align: justify; padding: 0 10px; border-left: 1px solid #00599C; border-right: 1px solid #00599C;">
                <h3 style="color: #00599C;">Ken Thompson</h3>
                <p>The creator of the <b>B Language</b> (C's direct predecessor). He worked closely with
                Ritchie at Bell Labs and is the co-author of UNIX. His work on B — itself derived from BCPL —
                provided the syntactic foundation for what became C.</p>
            </div>
        ''', unsafe_allow_html=True)

    with col3:
        st.markdown('''
            <div style="text-align: justify; padding-left: 10px;">
                <h3 style="color: #00599C;">Brian Kernighan</h3>
                <p>Co-author of the landmark book <b><i>'The C Programming Language'</i> (1978)</b> — nicknamed
                <b>K&R C</b>. Kernighan also coined the name "UNIX" and wrote some of the earliest C tutorials,
                making the language accessible to the wider world.</p>
            </div>
        ''', unsafe_allow_html=True)

    st.markdown("---")
    st.info("📜 **Historical Note:** In 1983, Dennis Ritchie and Ken Thompson received the **ACM Turing Award** — computing's highest honour — for their development of generic operating systems theory and specifically for the implementation of the UNIX Operating System.")
    st.markdown("---")

    # --- SECTION 2: THE EVOLUTIONARY TIMELINE ---
    st.header("⏳ From Research to Global Standard")

    with st.expander("🏗️ The Pre-Standard Era (1960–1978) — Click to expand"):
        st.markdown('''
            <div style="border-left: 3px solid #00599C; padding-left: 15px;">
        ''', unsafe_allow_html=True)
        st.markdown("""
**The full lineage of C** follows a clear chain of descent — each language inherited and improved upon its predecessor:

| Year | Language | Creator | Key Contribution |
|------|----------|---------|-----------------|
| 1960 | **ALGOL 60** | International committee | Introduced *structured programming* — the concept of blocks, loops, and conditionals. The grandfather of most modern languages. |
| 1963 | **CPL** | Cambridge & London Universities | Combined ALGOL's structure with low-level hardware access. Too complex to implement fully. |
| 1967 | **BCPL** | Martin Richards (Cambridge) | Stripped CPL down to essentials. Introduced the concept of a *typeless* language — every variable was just a machine word. |
| 1970 | **B Language** | Ken Thompson (Bell Labs) | A further simplification of BCPL, tailored for the PDP-7 minicomputer. Still typeless, limited for system programming. |
| 1972 | **C** | Dennis Ritchie (Bell Labs) | Added a **type system** (`int`, `char`, `float`, pointers) to B — making it safe and expressive enough to rewrite UNIX. |
| 1978 | **K&R C** | Kernighan & Ritchie | Published *'The C Programming Language'* — the de facto standard before formal standardization. |
        """)
        st.markdown('''</div>''', unsafe_allow_html=True)

    # --- SECTION 3: THE ANSI & ISO STANDARDS ---
    st.subheader("🏛️ The ANSI/ISO Standardization Era")
    st.markdown("""
    By the early 1980s, C was so popular that different compilers and vendors were producing incompatible
    dialects. To prevent fragmentation, the **American National Standards Institute (ANSI)** formed
    committee **X3J11** in 1983 to produce a definitive standard.
    """)

    st.table({
        "Standard": ["C89 / C90", "C99", "C11", "C17", "C23"],
        "Year Ratified": ["1989 / 1990", "1999", "2011", "2018", "2024"],
        "Key Additions": [
            "First official standard. Introduced function prototypes, the Standard Library (stdio.h, stdlib.h), and const/volatile qualifiers.",
            "Added long long int, variable-length arrays (VLAs), inline functions, and // single-line comments. Essential for scientific computing.",
            "Added multi-threading support (_Thread_local), anonymous structs/unions, and better Unicode handling.",
            "A technical corrigendum — no new features, only defect fixes and clarifications for stability.",
            "Removed K&R-style declarations. Added bool, true, false as keywords. Introduced nullptr. Improved type-generic math."
        ]
    })

    # --- SECTION 4: RECENT DEVELOPMENTS ---
    st.header("🚀 Recent Developments: C23 & Beyond")
    st.markdown("""
    Contrary to popular belief, C is still evolving rapidly to stay relevant in **AI and Natural Sciences**.

    * **C23 (Ratified 2024):** The biggest update in a decade.
        * Removed legacy K&R style function declarations (no more ambiguous parameter lists).
        * Added `bool`, `true`, and `false` as first-class keywords — previously required `#include <stdbool.h>`.
        * Introduced `nullptr` to replace the error-prone `NULL` macro, improving memory safety.
        * Added `[[nodiscard]]` and other attributes borrowed from C++ for better compiler warnings.
    * **2025–2026 Trend — 'Safe C':** New compilers (Clang 18+, GCC 14+) are being integrated with static analysis and AI-assisted tooling to detect **Buffer Overflows** and **Memory Leaks** at compile time — essential for processing large genomic and proteomic datasets without runtime crashes.
    """)

    st.markdown('''
        <div style="background-color: #00599C; padding: 14px 18px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
            <b>📌Note:</b>  One is expected to know C89/C90, C99, C11, C17, and C23 by name and be able to state at least one key feature introduced in each standard.
        </div>
    ''', unsafe_allow_html=True)

    st.markdown("---")

    # --- SECTION 5: THE MICROBIOLOGY CONNECTION ---
    # FIX: Replaced st.success() (green) with the consistent blue-themed div
    st.header("🧬 Why C is Relevant in Bioinformatics?")
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">C as the Engine of Biological Data Processing</h4>
            <p style="color: #333; font-size: 0.95rem;">
                In <b>Molecular Biology and Bioinformatics</b>, we routinely deal with very long character
                strings (DNA/RNA sequences) and enormous numerical matrices (expression data, distance matrices).
                While Python is the scientist's interface, <b>C is the engine underneath</b>.
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Memory Efficiency:</b> When analysing a 3 GB whole-genome FASTQ file, C lets you control
                exactly how much RAM is allocated — avoiding the overhead that Python's garbage collector introduces.</li>
                <li><b>Speed:</b> Tools like <b>BWA</b> (Burrows-Wheeler Aligner) and <b>SAMtools</b> — the gold
                standard for DNA sequence alignment — are written in C. They can process millions of reads per
                second that would take hours in pure Python.</li>
                <li><b>Foundation for Libraries:</b> NumPy, SciPy, and even parts of TensorFlow are written in C/C++
                at their core. Understanding C helps you understand <i>why</i> these libraries are fast.</li>
                <li><b>Embedded & Lab Instrumentation:</b> Microcontrollers in PCR machines, spectrophotometers,
                and fermenters are typically programmed in C — directly relevant to wet-lab automation.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- SECTION 6: QUICK REVIEW QUIZ ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is the correct lineage of C? Arrange: B, BCPL, ALGOL, C, CPL"):
        st.success("**Answer:** ALGOL 60 → CPL → BCPL → B → C. Each step simplified or extended the previous language, with C adding the crucial type system that made it suitable for OS-level programming.")

    with st.expander("Q2: Why was ANSI standardization of C necessary in 1983?"):
        st.success("**Answer:** By the early 1980s, different vendors (IBM, Microsoft, etc.) had created incompatible dialects of C. Code written for one compiler would fail on another. ANSI committee X3J11 was formed to define a single, portable standard — resulting in C89/C90.")

    with st.expander("Q3: What is the significance of C99 for scientific computing specifically?"):
        st.success("**Answer:** C99 introduced **long long int** (64-bit integers, essential for large genomic indices), **variable-length arrays** (VLAs, allowing array sizes set at runtime from experimental data), and **inline functions** (for performance-critical numerical loops). It also added `//` comments, making code more readable.")

    with st.expander("Q4: Name two bioinformatics tools written in C and explain why C was chosen over Python for them."):
        st.success("**Answer:** **BWA** (Burrows-Wheeler Aligner) and **SAMtools** are written in C. C was chosen because they process millions of short DNA reads — speed and low memory overhead are critical. A Python implementation of the same algorithm would be 10–50× slower and use significantly more RAM, making whole-genome analysis impractical.")

if __name__ == "__main__":
    render()