# C for Natural Sciences Website
<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge=flat-square&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge=plastic&logo=python&logoColor=ffdd54)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://c-for-natural-sciences-sbqjhssvaqhxtyxxwgzudd.streamlit.app/)

</div>

**C for Natural Sciences**

Anubrajo Ghosh | MCBA Semester 2 | St. Xavier's College (Autonomous), Kolkata

MDS Paper: AI for Natural Sciences | Academic Year 2025-2026

# **1\. Project Overview**

C for Natural Sciences is a multi-module interactive study application built with Streamlit and Python, designed as a submission for the MDS (Multidisciplinary Studies) paper - AI for Natural Sciences - at St. Xavier's College (Autonomous), Kolkata. The application serves as a structured, self-contained learning platform covering the C programming language from foundational syntax through to advanced bioinformatics-relevant programming techniques.

The core premise is that C - despite being a 1972 language - remains the computational backbone of modern bioinformatics. Tools like BWA (Burrows-Wheeler Aligner), SAMtools, BLAST, and htslib are all written in C. Understanding C is therefore not an academic exercise for a Microbiology student - it is practical preparation for the genomic data pipelines used in real research.

**Key proposition:**

Every module pairs its C programming concept with a concrete Microbiology or Bioinformatics application - so the student always knows why each concept matters to their degree, not just how it works.

# **2\. Student & Course Context**

| **Field**                       | **Details**                                   |
| ------------------------------- | --------------------------------------------- |
| Student                         | Anubrajo Ghosh                                |
| Department                      | MCBA (Microbiology)                           |
| Year / Semester                 | 1st Year, Semester 2                          |
| College                         | St. Xavier's College (Autonomous), Kolkata    |
| MDS Paper                       | AI for Natural Sciences                       |
| Academic Year                   | 2025-2026                                     |
| Project Type                    | Interactive Study Web Application (Streamlit) |

# **3\. Technology Stack**

| **Component**      | **Technology**                           | **Purpose**                                                  |
| ------------------ | ---------------------------------------- | ------------------------------------------------------------ |
| Frontend / UI      | Streamlit (Python)                       | Interactive web UI, sidebar navigation, tabs, expanders      |
| Language           | Python 3.10+                             | Application logic, module routing, session state             |
| C Code Display     | st.code() with syntax highlighting       | Renders all C programs with colour highlighting              |
| Module Import      | Python importlib                         | Dynamic import of chapter modules (avoids numeric filenames) |
| Session Management | Streamlit st.session_state               | Splash screen, loading animation, login/logout state         |
| Image Embedding    | Python base64 + CSS                      | Background image on splash page encoded as base64            |
| Math Rendering     | Streamlit LaTeX (st.write with \$...\$ ) | Renders formulas like Nt = N0 · e^(rt)                       |
| Deployment Target  | Streamlit Cloud (community.streamlit.io) | Free hosting with GitHub repository connection               |

# **4\. File & Folder Structure**

The project follows a flat chapter-module architecture where each topic is a separate Python file inside a chapters/ subdirectory. The main entry point is app.py at the root.

**C-for-Natural-Sciences** <-- Main Folder
| **Path / File**           | **Description**                                                |
| ------------------------- | -------------------------------------------------------------- |
| app.py                    | Main entry point; handles routing, splash screen, and sidebar. |
| loading_bio.jpg           | Background image for the splash screen.                        |
| requirements.txt          | Python dependencies required for deployment.                   |
| **chapters/**             | **Subdirectory containing all study modules**.                 |
| home.py                   | Home / landing page.                                           |
| 1_generations.py          | Module 1: Language Generations.                                |
| 2_history.py              | Module 2: History of C.                                        |
| 3_structure_basics.py     | Module 3: Program Structure.                                   |
| 4_data_management.py      | Module 4: Data Types.                                          |
| 5_operators.py            | Module 5: Operators & Expressions.                             |
| 6_input_output.py         | Module 6: Input & Output.                                      |
| 7_selection.py            | Module 7: Selection / Decision Making.                         |
| 8_iterations.py           | Module 8: Iterative Statements.                                |
| 9_functions.py            | Module 9: Functions.                                           |
| 10_arrays_pointers.py     | Module 10: Arrays & Pointers.                                  |
| 11_storage_classes.py     | Module 11: Storage Classes.                                    |
| 12_struct_union.py        | Module 12: Structures & Unions.                                |
| 13_file_handling.py       | Module 13: File Handling.                                      |
| 14_strings.py             | Module 14: Strings & Sequences.                                |
| 15_libraries.py           | Module 15: Standard Libraries & Math.                          |
| 16_lab_repository.py      | Module 16: Solved Lab Repository.                              |

Note: Python cannot import modules whose names start with a digit (e.g. import 1_generations). The importlib.import_module() approach in app.py circumvents this restriction cleanly.

# **5\. Module Content Overview**

Each of the 15 study modules follows a standardised structure to ensure consistent learning experience:

**Standard structure of every module:**

① Learning Objective banner - what the student will be able to do after completing the module

② Concept sections - each with a blue-bordered explanation block followed by annotated C code

③ MDS Integration box - how the concept applies in Microbiology / Bioinformatics / AI for Natural Sciences

④ Quick Review - 5 collapsible exam-style questions with full model answers

| **Module** | **Topic**                         | **Key Bioscience Connection**                                                                          |
| ---------- | --------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1          | Language Generations              | Python (4GL) for ML models; C (3GL) for the engines underneath; LLMs as 5GL                            |
| 2          | History of C                      | BWA, SAMtools - gold-standard alignment tools written in C                                             |
| 3          | Program Structure & Character Set | htslib's modular pipeline design; Avogadro's number as a #define constant                              |
| 4          | Data Types & Type Modifiers       | long long for genome coordinates (3.2 billion bp > INT_MAX); float vs double for OD600                 |
| 5          | Operators & Expressions           | Bitwise encoding of nucleotides (2-bit: A=00, T=01, G=10, C=11); modulus for codon frames              |
| 6          | Input & Output (printf/scanf)     | TSV output for R/Python ingestion; fgets() for FASTA header parsing; %e for Avogadro                   |
| 7          | Selection & Decision Making       | if-else for GC% classification; switch on nucleotide char; goto in samtools error handling             |
| 8          | Iterative Statements (Loops)      | for loop over OD600 arrays; while for gradient descent convergence; nested for 96-well plates          |
| 9          | Functions                         | Needleman-Wunsch recursion; call-by-reference for large genome arrays; modular FASTQ pipeline          |
| 10         | Arrays & Pointers                 | Sliding window genome scan; malloc for FASTQ files; Smith-Waterman 2D scoring matrix                   |
| 11         | Storage Classes                   | static for biomass accumulation across calls; extern for multi-file pipeline config                    |
| 12         | Structures & Unions               | bam1_t struct in htslib; biosensor union for count/concentration; protein database array               |
| 13         | File Handling                     | FASTA/FASTQ parsing; CSV output for pandas; fseek() in BLAST indexed databases                         |
| 14         | Strings & Sequence Processing     | GC content; DNA transcription; start codon detection with strstr(); codon reading frames               |
| 15         | Standard Libraries & Math         | pH via log10(); doubling time via log(2)/r; Monte Carlo mutation simulation; uint64_t for genomics     |
| 16         | Solved Lab Repository             | 10 Bio-C programs: growth models, Michaelis-Menten, pH converter, amino acid composition, MW estimator |

# **6\. Solved Lab Repository (Module 16)**

Module 16 is a curated archive of verified, runnable C programs organised into four tabs with nested sub-tabs for the Bio-C section:

### **Tab 1 - Foundations, Logic & Loops (6 programs)**

- Basic Arithmetic (all five operators with division-by-zero guard)
- Leap Year Check using the full Gregorian algorithm with ternary operator
- Prime Number Check using trial division up to √n with &lt;math.h&gt;
- Palindrome Check by integer reversal
- Armstrong Number Check using pow() for digit cubing
- Fibonacci Series generation with iterative loop

### **Tab 2 - Functions & Recursion (4 programs)**

- Prime Check encapsulated as a reusable function
- Fibonacci nth term via iterative function
- GCD using Euclidean recursive algorithm (gcd(a,b) = gcd(b, a%b))
- Multiplication by repeated addition recursively

### **Tab 3 - Arrays & Structures (4 programs)**

- Max and Min in an array (with VLA portability note)
- Linear Search with all-occurrence reporting
- Student Record struct (basic struct demonstration)
- Microbiology Sample Record struct (strain, GC content, colony count)

### **Tab 4 - Bio-C Specialisation (10 programs across 4 sub-tabs)**

**DNA/RNA & Molecular Biology:**

- DNA Thermal Stability - GC content with percentage
- DNA to RNA Transcription - template strand conversion (A→U, T→A, G→C, C→G)
- Complementary DNA Strand Generator - antiparallel strand with struct storage

**Microbial Growth & Ecology:**

- Bacterial Growth Engine - exponential model Nt = N0·e^(rt) with tabular output
- Generation Time Calculator - g = (log10 Nt - log10 N0) / log10 2
- Logistic Growth Model - dN/dt = rN(1 - N/K) with Euler step simulation

**Enzymes & Biochemistry:**

- Michaelis-Menten Kinetics - V = (Vmax × \[S\]) / (Km + \[S\]) table
- pH and \[H⁺\] Converter - bidirectional with solution category classification

**Protein & Amino Acid Analysis:**

- Amino Acid Composition Counter - frequency table from single-letter sequence
- Protein Molecular Weight Estimator - using average residue masses minus peptide bonds

# **7\. Application Architecture**

### **7.1 Entry Flow**

- User lands on splash page (app.py) - sidebar hidden via CSS injection
- Background image (loading_bio.jpg) is base64-encoded into a CSS &lt;style&gt; block
- User clicks 'Click Here' → st.session_state.entered = True → st.rerun()
- Loading animation (st.status) runs once; st.session_state.initialized = True
- Sidebar appears; user selects chapter from radio menu → module.render() called
- Auto-scroll JS fires on every render to return the user to the top of the page

### **7.2 Session State Variables**

| **Variable**                 | **Purpose**                                        |
| ---------------------------- | -------------------------------------------------- |
| st.session_state.entered     | False = show splash; True = show main app          |
| st.session_state.initialized | False = run loading animation once; True = skip it |

### **7.3 Module Import Strategy**

Python prohibits importing modules whose filenames start with a digit. The solution uses importlib.import_module() with the full dotted path:

gen = importlib.import_module('chapters.1_generations')

This loads the file chapters/1_generations.py and assigns the module object to gen. Calling gen.render() then executes that module's render() function. Every chapter file exposes exactly one public function - render() - keeping the interface consistent.

### **7.4 Visual Design System**

| **Element**          | **Specification**                                                   |
| -------------------- | ------------------------------------------------------------------- |
| Primary brand colour | #00599C (C Programming blue)                                        |
| Dark accent          | #002D5A                                                             |
| Light background     | #F0F4F8 / #E8F0FE                                                   |
| Header blocks        | Background #00599C, border-left 10px #002D5A, white text            |
| Section dividers     | Blue 3px left border on info/callout blocks                         |
| Code blocks          | st.code() with language='c' for C syntax highlighting               |
| Info callouts        | background-color: #E8F0FE, border-left: 3px solid #00599C           |
| MDS box              | background-color: #F0F4F8, border: 1px solid #00599C                |
| Font                 | Sans-serif (Streamlit default); Courier New for code in HTML blocks |

# **8\. Installation & Local Setup**

### **8.1 Prerequisites**

- Python 3.10 or higher
- pip (Python package manager)
- A terminal / command prompt
- Git (optional - for cloning from GitHub)

### **8.2 Step-by-Step Setup**

- Clone or download the repository:

`git clone <https://github.com/<your-username>/c-for-natural-sciences.git>`

`cd c-for-natural-sciences`

- Create a virtual environment (recommended):

`python -m venv venv`

`source venv/bin/activate` # Linux / macOS

`venv\\Scripts\\activate` # Windows

- Install dependencies:

`pip install -r requirements.txt`

- Place the background image in the project root:

Ensure loading_bio.jpg is in the same directory as app.py. If the file is absent, the splash page loads without a background - no crash occurs.

- Run the application:

`streamlit run app.py`

- Open in browser:

Streamlit will print a local URL (typically <http://localhost:8501>). Open it in any modern browser.

### **8.3 requirements.txt**

streamlit>=1.32.0

No additional Python packages are required. All mathematical rendering uses Streamlit's built-in LaTeX support. The C code displayed in the app is static text - it does not compile or execute within the application.

# **9\. Deployment on Streamlit Cloud**

- Push the project to a public GitHub repository.
- Go to community.streamlit.io and sign in with GitHub.
- Click 'New app' → select your repository → set Main file path to app.py.
- Click 'Deploy'. Streamlit Cloud reads requirements.txt and installs dependencies automatically.
- The app will be live at https://&lt;your-app-name&gt;.streamlit.app within 1-2 minutes.

**Important notes for deployment:**

• loading_bio.jpg must be committed to the repository (it cannot be uploaded separately to Streamlit Cloud).

• The free Streamlit Cloud tier has a 1 GB memory limit - this app uses well under 100 MB.

• The app sleeps after 7 days of inactivity on the free tier. Visiting the URL wakes it within ~30 seconds.

• All 16 chapter files must be inside a chapters/ directory at the repository root.

# **10\. Key Design Decisions**

### **10.1 Why Streamlit?**

Streamlit was chosen because it allows a Python/science-oriented developer to build a functional interactive web application without any HTML, CSS, or JavaScript expertise beyond occasional inline HTML for custom styling. A semester 2 student with Python familiarity can maintain and extend it easily.

### **10.2 Why one render() function per module?**

Each chapter file exposes exactly one public function - render(). This creates a clean contract: app.py calls module.render() and the module handles everything else internally. Adding a new chapter requires only creating a new file and adding two lines to app.py (the import and the menu entry).

### **10.3 Why importlib instead of a standard import?**

Python's import system does not allow identifiers that begin with digits. Since chapter filenames follow the pattern 1_generations.py, 2_history.py etc. (matching the natural module numbering), importlib.import_module('chapters.1_generations') is the clean solution - no renaming or sys.path hacks needed.

### **10.4 Why not execute the C code in the browser?**

Executing arbitrary C code in a web application introduces security risks (sandbox escapes, denial-of-service) and significant infrastructure complexity (requires a C compiler backend, process isolation, timeout management). The application is a study platform - the C code is the content to be read and understood, not executed. Students compile and run the programs locally using GCC or any C99+ compiler.

### **10.5 Colour choice - #00599C**

The primary brand colour (#00599C) is the exact blue used in the official C programming language logo. Using it consistently throughout headers, borders, callout boxes, and buttons ties the visual identity directly to the subject matter - making the design choice conceptually motivated, not arbitrary.

# **11\. How to Compile & Run the C Programs**

The C programs displayed in the application are intended to be copied and compiled locally. All programs are standard C99 or C11 and compile with GCC, Clang, or MSVC.

### **11.1 Basic compilation (GCC)**

`gcc -std=c99 -o program program.c`

./program # Linux / macOS

program.exe # Windows

### **11.2 Programs using &lt;math.h&gt; (requires -lm on Linux/macOS)**

`gcc -std=c99 -o growth growth.c -lm`

### **11.3 Recommended compiler flags for study**

`gcc -std=c11 -Wall -Wextra -pedantic -o program program.c -lm`

\-Wall -Wextra enables all warnings. -pedantic enforces strict standard compliance. These flags help catch bugs that would otherwise compile silently.

### **11.4 Online compilers (no local installation needed)**

- Programiz Online C Compiler - programiz.com/c-programming/online-compiler
- OnlineGDB - onlinegdb.com/online_c_compiler
- GDB Online - gdbonline.org

# **12\. Known Limitations**

- C programs are display-only - they cannot be compiled or executed within the application itself.
- However all the C Programs included have been verified and tested. If required they can be tested on any onlinegdb.com/online_c_compiler.
- The background image on the splash screen must be manually placed at the project root; it is not embedded in the Python source.
- Tab 3 of the Lab Repository uses Variable-Length Arrays (int arr\[n\]) which are C99/C11 only, optional in C11, and not available in C17+. A portability note is displayed in the module.
- The auto-scroll JavaScript uses window.parent DOM manipulation which may behave differently across Streamlit versions. A try/catch fallback is included.
- Streamlit's free cloud tier puts the app to sleep after 7 days of inactivity - the first visit after a sleep period takes ~30 seconds to load.

# **13\. Academic Context & Declaration**

This application was developed as a project submission for the MDS (Multidisciplinary Studies) elective paper 'AI for Natural Sciences' during Semester 2 of the B.Sc. programme at St. Xavier's College (Autonomous), Kolkata.

The content covers the prescribed C programming syllabus and extends it with biological context appropriate to a Microbiology major. All C programs in the Lab Repository have been verified for correctness. The biological formulas (Michaelis-Menten, exponential growth, generation time, pH, Beer-Lambert) are standard undergraduate biochemistry and microbiology equations.

**Declaration:**

This project is an original submission. The application code, module content, quiz questions, and biological commentary were developed by Anubrajo Ghosh for the 2025-2026 academic session. External references include the C standard documentation (ISO/IEC 9899), ANSI C specification (C89/C90), and standard microbiology textbooks.

# **14\. Contact & College Details**

| **Field**             | **Details**                                  |
| --------------------- | -------------------------------------------- |
| Student Name          | Anubrajo Ghosh                               |
| Department            | MCBA - Microbiology (Hons.)                  |
| Semester              | Semester 2, 1st Year                         |
| College               | St. Xavier's College (Autonomous), Kolkata   |
| Affiliated University | University of Calcutta                       |
| MDS Paper             | AI for Natural Sciences                      |
| Paper Code            | (as per your college syllabus)               |
| Academic Year         | 2025-2026                                    |
| Application           | C for Natural Sciences - Streamlit Study App |

_C for Natural Sciences | MDS Study Application | Anubrajo Ghosh | MCBA Semester 2 | SXC Kolkata | 2026_
