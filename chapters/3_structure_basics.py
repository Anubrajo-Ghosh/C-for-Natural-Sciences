import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🏗️ Module 3: Architecture & Structure of C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">From Character Sets to the Standard Library</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to list the salient features of C, identify all six sections of a C program's structure, enumerate the character set and token types, distinguish variables from constants, and identify the major Standard Library headers and their uses.")

    st.write("")

    # --- 1. Features of C ---
    st.markdown("### 1️⃣ Salient Features of C")
    st.write("""
    C is often described as a **"Middle-Level"** language — it provides the low-level hardware control 
    of Assembly with the readable, high-level syntax of modern languages. This makes it uniquely 
    suited for both system programming and scientific computing.
    """)

    feat_col1, feat_col2 = st.columns(2)
    with feat_col1:
        st.markdown("**Performance & Control:**")
        st.markdown("- **Efficiency:** C programs compile directly to machine code — extremely fast with minimal memory overhead.")
        st.markdown("- **Middle-Level:** Can interact directly with hardware registers and memory addresses via pointers.")
        st.markdown("- **Pointer Support:** Direct memory manipulation using pointers — essential for data structures and system programming.")
        st.markdown("- **Robustness:** A rich set of built-in operators (arithmetic, logical, bitwise, relational) covering most computational needs.")
    with feat_col2:
        st.markdown("**Design & Architecture:**")
        st.markdown("- **Structured:** Enforces top-down design using functions and blocks — no implicit jumps (unlike early BASIC).")
        st.markdown("- **Modular:** Large programs are broken into small, reusable functions — each solving one well-defined task.")
        st.markdown("- **Portability:** ANSI-standard C code can be recompiled on different hardware with minimal or no changes.")
        st.markdown("- **Extensibility:** New capabilities are added by linking standard or third-party library functions — no need to modify the language itself.")
        st.markdown("- **Security:** Supports `const`, type checking, and (in modern standards) bounds-aware features to reduce vulnerabilities.")

    st.divider()

    # --- 2. Structure of a C Program ---
    st.markdown("### 2️⃣ Structure of a C Program")
    st.write("A standard C program follows a specific six-section sequence. Deviation from this often causes compilation errors or undefined behaviour.")

    # FIX: Filled in the blank block that was between the intro text and the code block
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 15px;">
            <b>The Six Sections — explained:</b>
            <ol style="margin-top: 8px; color: #FFFFFF; font-size: 0.95rem;">
                <li><b>Documentation Section:</b> Multi-line comments (<code>/* ... */</code>) describing the program's purpose, author, and date. Not processed by the compiler — purely for human readers.</li>
                <li><b>Link Section:</b> <code>#include</code> preprocessor directives that attach Standard Library header files before compilation begins.</li>
                <li><b>Definition Section:</b> <code>#define</code> macros that create symbolic constants. The preprocessor does a text substitution of the constant name with its value everywhere in the code.</li>
                <li><b>Global Declaration Section:</b> Variables declared here are accessible by <i>all</i> functions in the file (global scope). Use sparingly — global state is harder to debug.</li>
                <li><b>Main Function Section:</b> Every C program must have exactly one <code>main()</code>. Execution always begins here. Returns an <code>int</code> to the OS (0 = success).</li>
                <li><b>Subprogram Section:</b> User-defined functions called from <code>main()</code> or each other. Placing them after <code>main()</code> requires a forward declaration (prototype) in the link section.</li>
            </ol>
        </div>
    ''', unsafe_allow_html=True)

    st.code("""
/* 1. DOCUMENTATION SECTION */
// Program: Molar Mass Calculator
// Author:  SXC MDS Semester 2
// Date:    2026

/* 2. LINK SECTION */
#include <stdio.h>
#include <math.h>

/* 3. DEFINITION SECTION */
#define AVOGADRO 6.022e23
#define PI       3.14159265

/* 4. GLOBAL DECLARATION SECTION */
int experiment_run_count = 0;   // Accessible by all functions

/* 5. MAIN FUNCTION SECTION */
int main() {
    float molar_mass = 18.015;          // Local variable (water)
    printf("Molar Mass of H2O: %.3f g/mol\\n", molar_mass);
    printf("Molecules in 1 mol: %.3e\\n", AVOGADRO);
    experiment_run_count++;
    return 0;                           // 0 signals success to the OS
}

/* 6. SUBPROGRAM SECTION */
void calculate_molarity(float moles, float volume_L) {
    printf("Molarity = %.4f M\\n", moles / volume_L);
}
    """, language="c")

    st.divider()

    # --- 3. Character Set & Tokens ---
    st.markdown("### 3️⃣ Character Set, Tokens, Keywords & Identifiers")

    st.write("**A. Character Set:**")
    st.write("The complete set of characters that C recognises and can process:")
    st.markdown("- **Letters:** Uppercase A–Z and Lowercase a–z (C is case-sensitive: `int` ≠ `Int`).")
    st.markdown("- **Digits:** 0 to 9.")
    st.markdown("- **Special Characters:** `+ - * / % = & | ! < > ( ) [ ] { } , ; : . ' \" # \\ _ ^ ~ @` etc.")
    st.markdown("- **White Spaces:** Space, horizontal tab (`\\t`), carriage return (`\\r`), newline (`\\n`) — ignored by the compiler except inside string literals.")

    st.write("**B. Tokens — The Smallest Units of a C Program:**")
    st.markdown('''
        <div style="background-color: #00599C; padding: 12px 16px; border-radius: 6px; margin-bottom: 10px;">
        A <b>Token</b> is the smallest meaningful unit that the compiler recognises. There are six types:
        <br><br>
        <b>Keywords</b> · <b>Identifiers</b> · <b>Constants</b> · <b>Strings</b> · <b>Operators</b> · <b>Special Symbols</b>
        </div>
    ''', unsafe_allow_html=True)

    st.write("**C. Keywords:**")
    st.write("Reserved words with fixed, pre-defined meanings. They **cannot** be used as variable or function names.")

    kw_col1, kw_col2 = st.columns(2)
    with kw_col1:
        # FIX: Corrected keyword count — C89=32, C99 added 5, C11 added 7 more
        st.markdown("""
| Standard | Count | New Keywords Added |
|----------|-------|--------------------|
| C89/C90  | **32** | (original set) |
| C99      | **37** | `inline`, `restrict`, `_Bool`, `_Complex`, `_Imaginary` |
| C11      | **44** | `_Alignas`, `_Alignof`, `_Atomic`, `_Generic`, `_Noreturn`, `_Static_assert`, `_Thread_local` |
| C23      | **~54**| `bool`, `true`, `false`, `nullptr`, `typeof` (as first-class keywords) |
        """)
    with kw_col2:
        st.markdown("**The 32 C89 Keywords (exam baseline):**")
        st.code("""auto      break     case      char
const     continue  default   do
double    else      enum      extern
float     for       goto      if
int       long      register  return
short     signed    sizeof    static
struct    switch    typedef   union
unsigned  void      volatile  while""", language="text")

    st.write("**D. Identifiers — Naming Rules:**")
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px;">
    ''', unsafe_allow_html=True)
    st.markdown("""
Identifiers are programmer-defined names for variables, functions, arrays, and structures. Rules:

- ✅ Must begin with a **letter (A–Z, a–z) or underscore** (`_`)
- ✅ Can contain letters, digits (0–9), and underscores after the first character
- ❌ Cannot start with a digit (`2cell` is invalid; `cell2` is valid)
- ❌ Cannot be a keyword (`int`, `float`, etc.)
- ❌ Cannot contain spaces or special characters (`cell-count` is invalid; `cell_count` is valid)
- ⚠️ Case-sensitive: `CellCount`, `cellcount`, and `CELLCOUNT` are three different identifiers
- ⚠️ ANSI C guarantees only the first **31 characters** are significant (longer names may be truncated by older compilers)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 4. Variables & Constants ---
    st.markdown("### 4️⃣ Variables and Constants")

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Variables — Data Containers**")
        st.write("A variable is a named memory location whose value can change during execution. Declaration syntax: `data_type variable_name = initial_value;`")
        st.markdown("**Scope rules:**")
        st.markdown("- **Local:** Declared inside a function — only visible within that function.")
        st.markdown("- **Global:** Declared outside all functions — visible to the entire file.")
        st.code("""int cell_count = 500;   // local
cell_count = 650;       // ✅ Allowed — value changes
float ph;               // declared, not yet initialised
ph = 6.8;               // initialised later""", language="c")

    with col_b:
        st.markdown("**Constants — Fixed Values**")
        st.write("Constants are values that cannot be changed during execution. C supports four types of constants:")
        st.markdown("- **Integer Constants:** `42`, `-7`, `0xFF` (hex), `077` (octal)")
        st.markdown("- **Float Constants:** `3.14`, `6.022e23`, `-0.005f`")
        st.markdown("- **Character Constants:** `'A'`, `'\\n'`, `'0'` — single quotes, stored as ASCII int")
        st.markdown("- **String Constants:** `\"DNA\"`, `\"E. coli\"` — double quotes, null-terminated array")
        st.code("""/* Method 1: const qualifier (type-safe) */
const float PH_NEUTRAL = 7.0;

/* Method 2: #define macro (preprocessor) */
#define AVOGADRO 6.022e23
#define MAX_TEMP 121   /* autoclave temp °C */""", language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; margin-top: 8px; border-left: 3px solid #00599C;">
        <b>📌 const vs #define:</b> Prefer <code>const</code> over <code>#define</code> for typed constants — 
        the compiler can type-check <code>const</code> variables and they appear in the debugger. 
        <code>#define</code> is a dumb text substitution with no type information.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 5. The C Standard Library ---
    st.markdown("### 5️⃣ The C Standard Library")
    st.write("""
    The Standard Library is a collection of pre-written functions packaged into header files.
    You attach them to your program using the `#include` preprocessor directive. 
    The library covers I/O, mathematics, strings, memory, and more.
    """)

    lib_data = {
        "Header File": [
            "<stdio.h>", "<math.h>", "<string.h>",
            "<stdlib.h>", "<time.h>", "<ctype.h>", "<limits.h>"
        ],
        "Key Functions": [
            "printf, scanf, fopen, fclose, fprintf",
            "sin, cos, sqrt, pow, log, fabs, ceil, floor",
            "strlen, strcpy, strcat, strcmp, strstr",
            "malloc, calloc, free, exit, atoi, rand",
            "time, clock, difftime, strftime",
            "isalpha, isdigit, isupper, tolower, toupper",
            "INT_MAX, INT_MIN, CHAR_MAX, LONG_MAX (constants)"
        ],
        "Scientific Use Case": [
            "Reading sensor / lab instrument data files",
            "Calculating OD600 growth curves, enzyme kinetics",
            "Parsing and comparing DNA/RNA sequence strings",
            "Dynamic memory for variable-size data matrices",
            "Timestamping experiment logs and runs",
            "Validating and cleaning character-level sequence input",
            "Checking data type ranges before numerical overflow"
        ]
    }
    st.table(lib_data)

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 20px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Structure in Biology</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Just as a <b>Cell</b> has a rigid structure (Membrane → Cytoplasm → Nucleus) that must be 
                maintained for it to function, a <b>C Program</b> requires its six sections in the correct 
                order to compile and execute correctly.
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li>The <b>Link Section</b> (<code>#include</code>) is where bioinformatics pipelines import specialised 
                libraries — e.g., <code>htslib</code> for reading BAM/SAM genome alignment files.</li>
                <li>The <b>Definition Section</b> (<code>#define</code>) ensures scientific constants like 
                Avogadro's Number (<code>6.022e23</code>) or the Universal Gas Constant (<code>8.314</code>) 
                are defined once and reused consistently — a single wrong value in a simulation propagates into every calculation.</li>
                <li>The <b>Subprogram Section</b> maps directly to the concept of modular experimental design — 
                each function performs one well-defined assay (e.g., <code>calculate_od600()</code>, 
                <code>parse_fasta()</code>), making the code reproducible and peer-reviewable.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What are the six sections of a C program in order?"):
        st.success("**Answer:** (1) Documentation Section, (2) Link Section, (3) Definition Section, (4) Global Declaration Section, (5) Main Function Section, (6) Subprogram Section. The compiler requires sections 2–5 to appear in roughly this order; the documentation section is optional but professionally expected.")

    with st.expander("Q2: How many keywords does C89 have, and how many did C99 add?"):
        st.success("**Answer:** C89/C90 has **32** keywords. C99 added **5** more (`inline`, `restrict`, `_Bool`, `_Complex`, `_Imaginary`), bringing the total to **37**. C11 added 7 more (total ~44). The exam baseline is the 32 C89 keywords.")

    with st.expander("Q3: Which of these identifiers are INVALID and why? `2strain`, `_count`, `void`, `cell-wall`, `CellWall`"):
        st.success("""**Answer:**
- `2strain` ❌ — starts with a digit
- `_count` ✅ — valid (starts with underscore)
- `void` ❌ — is a reserved keyword
- `cell-wall` ❌ — contains a hyphen (special character not allowed)
- `CellWall` ✅ — valid (starts with letter, contains only letters)""")

    with st.expander("Q4: What is the practical difference between `const float X = 7.0;` and `#define X 7.0`?"):
        st.success("**Answer:** `const float X` is a **typed, scoped variable** — the compiler knows it is a `float`, can type-check it, and it appears in the debugger. `#define X 7.0` is a **preprocessor text substitution** — before compilation, every occurrence of `X` is replaced with the text `7.0` with no type information. This means `#define` can cause subtle bugs (e.g., `7.0` substituted in an integer context). Prefer `const` for clarity and safety.")

    with st.expander("Q5: Which Standard Library header would you use to dynamically allocate memory for a 10,000-row genomic data matrix?"):
        st.success("**Answer:** `<stdlib.h>` — it provides `malloc()` (allocate uninitialized memory) and `calloc()` (allocate zero-initialized memory). For a 2D matrix of floats: `float **matrix = malloc(10000 * sizeof(float *));` followed by allocating each row. Always pair with `free()` to prevent memory leaks.")

if __name__ == "__main__":
    render()