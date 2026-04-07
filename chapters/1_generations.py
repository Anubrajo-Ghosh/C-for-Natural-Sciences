import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h2 style="color: white; margin: 0; font-family: sans-serif;">📜 Module 1: Generations of Programming Languages</h2>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Navigating the Different Generations of Programming Languages</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to identify the five generations of programming languages, explain their characteristics, and relate each to real-world scientific computing contexts.")

    st.write("")

    # --- 1. First Generation (1GL): Machine Language ---
    st.markdown("### 1️⃣ First Generation (1GL): Machine Language")
    st.write("""
    Machine language is the lowest level of programming. It consists of binary digits (0s and 1s) 
    that the CPU can process directly without any translation.
    """)
    
    with st.container():
        st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px;">''', unsafe_allow_html=True)
        st.write("**Characteristics:**")
        st.markdown("- **Hardware Dependent:** Each CPU architecture has its own unique machine code.")
        st.markdown("- **No Translation:** Runs instantly because it is already in the final form the CPU understands.")
        st.markdown("- **Complexity:** Extremely difficult for humans to write, read, or debug — even a single misplaced bit causes failure.")
        st.markdown("- **Era:** Dominant in the 1940s–1950s on early machines like ENIAC and UNIVAC.")
        st.code("10110000 01100001  // Example: Load the value 97 (ASCII 'a') into register AL", language="text")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 2. Second Generation (2GL): Assembly Language ---
    st.markdown("### 2️⃣ Second Generation (2GL): Assembly Language")
    st.write("""
    Assembly language introduced **Mnemonics** (short abbreviations) to represent binary instructions. 
    It requires a program called an **Assembler** to convert it back into 1GL.
    """)
    
    with st.container():
        st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px;">''', unsafe_allow_html=True)
        st.write("**Characteristics:**")
        st.markdown("- **Human-Readable Symbols:** Uses words like `ADD`, `SUB`, `MOV` instead of raw binary.")
        st.markdown("- **Efficiency:** Still offers near 1:1 control over hardware registers and memory addresses.")
        st.markdown("- **Translation Tool:** An **Assembler** converts assembly code → machine code.")
        st.markdown("- **Usage Today:** Still used for writing device drivers, OS kernels, bootloaders, and embedded microcontroller firmware.")
        st.code("""
MOV AL, 61h    ; Load hex value 61 into register AL
ADD AL, 10h    ; Add hex 10 to the value in AL
        """, language="asm")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 3. Third Generation (3GL): Procedural Languages ---
    st.markdown("### 3️⃣ Third Generation (3GL): Procedural / High-Level")
    st.write("""
    3GLs are designed to be **Platform Independent**. You write the code once, and a **Compiler** or 
    **Interpreter** translates it for different types of computers. They focus on the logic and 
    procedures (functions) rather than hardware-level instructions.
    """)

    st.markdown('''
        <div style="background-color: #00599C; padding: 12px 16px; border-radius: 6px; margin-bottom: 10px;">
            <b>Key Translators in 3GL:</b><br>
            🔹 <b>Compiler</b> — Translates the <i>entire</i> source code into machine code before execution (e.g., C, C++, Fortran). Results in faster runtime.<br>
            🔹 <b>Interpreter</b> — Translates and executes the code <i>line-by-line</i> at runtime (e.g., early BASIC, Python in interpreted mode). Easier to debug.
        </div>
    ''', unsafe_allow_html=True)

    with st.container():
        st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px;">''', unsafe_allow_html=True)
        st.write("**Characteristics of C as a 3GL:**")
        st.markdown("- **Abstraction:** Developers don't need to manage specific CPU registers manually.")
        st.markdown("- **Structured Programming:** Programs are broken into smaller, reusable functions — improving readability and maintenance.")
        st.markdown("- **Portability:** Code written on Windows can be recompiled and run on Linux or macOS.")
        st.markdown("- **Examples:** C, Fortran, COBOL, Pascal, BASIC.")
        st.code("""
#include <stdio.h>

void calculate_growth(int initial) {
    int final_pop = initial * 2;
    printf("Projected Population: %d\\n", final_pop);
}

int main() {
    calculate_growth(500);
    return 0;
}
        """, language="c")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 4. Fourth Generation (4GL): Object-Oriented & Declarative ---
    st.markdown("### 4️⃣ Fourth Generation (4GL): Non-Procedural / OOP")
    st.write("""
    4GLs aim to reduce programming effort and speed up development. They often use **Objects** to 
    represent real-world entities, or focus on **Declarative** logic — telling the computer 
    *what* to do, not *how* to do it step-by-step.
    """)
    
    with st.container():
        st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px;">''', unsafe_allow_html=True)
        st.write("**Two main paradigms in 4GL:**")
        st.markdown("- **Object-Oriented (OOP):** Languages like Java and Python group data and functions into **Classes** and **Objects**, modelling real-world entities.")
        st.markdown("- **Data-Centric / Declarative:** SQL is a classic 4GL — you declare *what* records you want, and the database engine figures out *how* to fetch them.")
        st.markdown("- **Natural Language-Like Syntax:** Reads much closer to human English compared to 3GLs.")
        st.markdown("- **Examples:** Python, Java, Ruby, R, SQL, MATLAB.")

        col1, col2 = st.columns(2)
        with col1:
            st.code("""
// Java OOP Example
public class Microbe {
    String strain = "B. subtilis";
    int count = 1000;

    void display() {
        System.out.println(
          strain + ": " + count
        );
    }
}
            """, language="java")
        with col2:
            st.code("""
# SQL Declarative Example
SELECT strain, colony_count
FROM cultures
WHERE growth_rate > 0.5
ORDER BY colony_count DESC;
            """, language="sql")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="background-color: #00599C; border-left: 3px solid #f59e0b; padding: 10px 14px; border-radius: 4px; margin-top: 10px;">
        <b>💡Note on Classification</b>: Technically, languages like Python and Java are classified as 3rd Generation Languages (3GL) because they are general-purpose and procedural. However, they are included in this 4GL section because their modern syntax, extensive library support, and Object-Oriented nature allow them to function as "Very High-Level Languages" (VHLL), achieving the same goal as 4GLs: reducing programming effort and focusing on high-level logic over machine-level management.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 5. Fifth Generation (5GL): AI & Natural Language ---
    st.markdown("### 5️⃣ Fifth Generation (5GL): Artificial Intelligence & Natural Language")
    st.write("""
    5GLs represent the frontier of programming language evolution. Rather than writing explicit 
    procedures or objects, the programmer provides **constraints**, **goals**, or even 
    **natural language instructions**, and the system figures out the logic automatically.
    """)

    with st.container():
        st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px;">''', unsafe_allow_html=True)
        st.write("**Characteristics:**")
        st.markdown("- **Constraint-Based / Logic Programming:** The programmer defines the *problem* and *constraints*, not the solution steps. Classic examples: **Prolog**, **Mercury**.")
        st.markdown("- **AI-Assisted Code Generation:** Tools like GitHub Copilot and ChatGPT allow programmers to describe intent in plain English and receive working code.")
        st.markdown("- **Knowledge Representation:** 5GLs are core to expert systems and AI inference engines.")
        st.markdown("- **Usage:** Natural Language Processing (NLP), Expert Systems, AI-driven automation.")
        st.code("""
% Prolog Example — Logic Programming (5GL)
% Define facts
parent(tom, bob).
parent(bob, ann).

% Define rule: X is an ancestor of Y
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Query: Who are ann's ancestors?
% ?- ancestor(Who, ann).
% Result: Who = bob ; Who = tom
        """, language="prolog")

        st.markdown("""
        <div style="background-color: #00599C; border-left: 3px solid #f59e0b; padding: 10px 14px; border-radius: 4px; margin-top: 10px;">
        <b>🤖 Modern 5GL — Prompt Engineering:</b> When you type a natural language instruction into an LLM like Claude or GPT-4 and it generates code for you, you are effectively working at the 5GL level. The model handles all procedural and logical steps internally.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- Comparison Summary Table ---
    st.subheader("📊 Summary Table")
    st.write("This table summarises the jump in abstraction between all five generations:")
    
    summary_data = {
        "Generation": ["1GL", "2GL", "3GL", "4GL", "5GL"],
        "Language Type": [
            "Machine Code",
            "Assembly",
            "High-Level / Procedural",
            "Object-Oriented / Problem-Solving",
            "AI / Natural Language / Logic"
        ],
        "Translation Needed": [
            "None (direct CPU execution)",
            "Assembler",
            "Compiler or Interpreter",
            "Specialised Interpreters / JIT Compilers",
            "Inference Engine / LLM"
        ],
        "Human Readability": ["None", "Low", "High", "Very High", "Conversational"],
        "Hardware Control": [
            "Absolute",
            "Excellent",
            "Good (C is best here)",
            "Low / Abstracted",
            "None (fully abstracted)"
        ],
        "Key Examples": ["CPU binary", "x86 ASM", "C, Fortran, COBOL", "Python, Java, SQL, R", "Prolog, Copilot, GPT-4"]
    }
    st.table(summary_data)

    # --- Scientific Application ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 20px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Context: Choosing the Right Tool for the Job</h4>
            <p style="color: #333; font-size: 0.95rem;">
                In <b>AI for Natural Sciences</b>, different generations of languages serve distinct roles in the scientific computing pipeline:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>1GL / 2GL:</b> Rarely used directly, but foundational — GPU shaders for molecular dynamics simulations operate close to this level.</li>
                <li><b>3GL (C/C++/Fortran):</b> Used to write the mathematical <i>engines</i> — the BLAS libraries for linear algebra, the GROMACS engine for MD simulations, the TensorFlow backend. Speed is critical here.</li>
                <li><b>4GL (Python, R, MATLAB):</b> The scientist's day-to-day tool — building ML models, processing genomic data, visualising results with libraries like <code>ggplot2</code> or <code>matplotlib</code>. Python's ecosystem (NumPy, Pandas, Biopython) makes it dominant in bioinformatics.</li>
                <li><b>5GL (Prolog, AI tools):</b> Emerging in drug discovery (logic-based constraint solvers), protein folding pipelines, and AI-assisted hypothesis generation. Knowing this generation exists helps you anticipate where the field is heading.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: Which generation of programming language requires NO translation tool to run on the CPU?"):
        st.success("**Answer: 1GL (Machine Language).** It is already in binary — the CPU's native format — so no assembler, compiler, or interpreter is needed.")

    with st.expander("Q2: What is the key difference between a Compiler and an Interpreter?"):
        st.success("**Answer:** A **Compiler** translates the entire source code into machine code *before* execution (e.g., C programs). An **Interpreter** translates and executes the code *line by line* at runtime (e.g., Python in interactive mode). Compiled programs are generally faster; interpreted programs are easier to debug interactively.")

    with st.expander("Q3: Why is Python considered a 4GL and not a 3GL?"):
        st.success("**Answer:** Python supports **Object-Oriented Programming** (classes, objects, inheritance) and has a very high level of abstraction — the programmer focuses on *what* to do rather than managing memory, registers, or CPU-level details. This non-procedural, problem-solving focus is the hallmark of 4GL. (Note: Python is technically multi-paradigm — it also supports procedural and functional styles.)")

    with st.expander("Q4: Give one real-world example of 5GL in use in the natural sciences."):
        st.success("**Answer (example):** AlphaFold2's underlying protein structure prediction pipeline uses deep learning models where the 'logic' of folding is learned from data, not explicitly programmed step-by-step — this is a characteristic of 5GL AI systems. Another example: using Prolog-based constraint solvers in cheminformatics to enumerate molecular structures satisfying given chemical rules.")

if __name__ == "__main__":
    render()