import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">📡 Module 6: Input & Output Operations</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Standard I/O Functions, Format Specifiers, and Escape Sequences</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to use `printf()` and `scanf()` with correct format specifiers, apply width/precision formatting, list all major escape sequences, distinguish formatted from unformatted I/O, and explain and resolve the dangling newline buffer problem.")

    st.write("")

    # --- 1. Standard I/O Functions ---
    st.markdown("### 1️⃣ The Standard I/O Library (`<stdio.h>`)")
    st.write("""
    In C, Input/Output is not part of the core language — it is provided entirely by the Standard Library.
    All I/O functions require `#include <stdio.h>`. The two workhorses are `printf()` for formatted output 
    and `scanf()` for formatted input.
    """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Output: `printf()`**")
        st.write("Prints formatted data to **stdout** (the screen). Returns the number of characters written.")
        st.markdown("Syntax: `printf(\"format_string\", arg1, arg2, ...);`")
        st.code("""#include <stdio.h>

int   colony_count = 3500;
float ph           = 6.82;
char  strain[]     = "E. coli K-12";

printf("Strain: %s\\n",          strain);
printf("Colonies: %d\\n",        colony_count);
printf("pH: %.2f\\n",            ph);
printf("Count: %8d\\n",          colony_count);  // width 8, right-aligned
printf("Strain: %-15s|\\n",      strain);        // width 15, left-aligned
        """, language="c")

    with col2:
        st.markdown("**Input: `scanf()`**")
        st.write("Reads formatted data from **stdin** (the keyboard). Returns the number of items successfully read.")
        st.markdown("Syntax: `scanf(\"format_string\", &var1, &var2, ...);`")
        st.code("""#include <stdio.h>

int   sample_id;
float od_reading;
char  strain_code;

/* & is the ADDRESS-OF operator — scanf needs the
   memory address to store the value, not the value itself */
scanf("%d",   &sample_id);
scanf("%f",   &od_reading);
scanf(" %c",  &strain_code);   // leading space clears buffer

/* Reading multiple values at once */
scanf("%d %f", &sample_id, &od_reading);
        """, language="c")
        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem; margin-top: 5px;">
            <b>Why &amp; in scanf but not printf?</b><br>
            <code>printf</code> only needs to <i>read</i> the value to print it.<br>
            <code>scanf</code> needs to <i>write</i> a new value into the variable — so it needs the memory address, not the current value.
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. Format Specifiers ---
    st.markdown("### 2️⃣ Format Specifiers")
    st.write("""
    Format specifiers are placeholders embedded in the format string of `printf()` and `scanf()`. 
    They tell the function what data type to expect and how to format it.
    """)

    # FIX: Filled blank block — format specifier anatomy before the table
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Anatomy of a format specifier:</b><br><br>
        <code style="font-size: 1rem;">%[flags][width][.precision]type</code><br><br>
        <ul style="margin-top: 6px; font-size: 0.93rem; color: #FFFFFF;">
            <li><b>flags:</b> <code>-</code> (left-align), <code>+</code> (show sign), <code>0</code> (zero-pad)</li>
            <li><b>width:</b> minimum field width (e.g., <code>%8d</code> → at least 8 chars wide)</li>
            <li><b>.precision:</b> decimal places for floats, max chars for strings (e.g., <code>%.3f</code>, <code>%.10s</code>)</li>
            <li><b>type:</b> the data type specifier (see table below)</li>
        </ul>
        Example: <code>%+8.3f</code> → show sign, min 8 wide, 3 decimal places, float
        </div>
    ''', unsafe_allow_html=True)

    # FIX: Expanded specifier table — added %o, %x, %e, %ld, %lld, %p, %li
    spec_data = {
        "Specifier": [
            "%d / %i", "%u", "%ld", "%lld",
            "%f", "%lf", "%e / %E", "%g",
            "%c", "%s",
            "%o", "%x / %X", "%p",
            "%%"
        ],
        "Data Type": [
            "signed int", "unsigned int", "long int", "long long int",
            "float (printf)", "double (scanf / printf)", "float or double (scientific)", "float or double (shorter of %f or %e)",
            "char (single character)", "char array (string)",
            "unsigned int (octal)", "unsigned int (hexadecimal)", "pointer (memory address)",
            "Literal % sign"
        ],
        "printf Example": [
            "42 / -7", "4294967295", "2147483647", "9200000000",
            "3.141593", "3.141593", "3.141593e+00", "3.14159",
            "A", "E. coli",
            "52 (= 42 in octal)", "2a / 2A (= 42 in hex)", "0x7fff5f3a2b10",
            "%"
        ]
    }
    st.table(spec_data)

    # Width and precision demo
    st.markdown("**Width & Precision Formatting — practical examples:**")
    st.code("""float od = 0.7320456;
int   count = 42;

printf("%f\\n",      od);       // 0.732046  (default 6 decimal places)
printf("%.2f\\n",    od);       // 0.73      (2 decimal places)
printf("%8.3f\\n",   od);       // ___0.732  (8 wide, 3 decimal, right-align)
printf("%-8.3f|\\n", od);       // 0.732___|  (left-align within 8 chars)
printf("%08.3f\\n",  od);       // 0000.732  (zero-padded to 8 chars)
printf("%e\\n",      od);       // 7.320456e-01  (scientific notation)

printf("%5d\\n",     count);    // ___42  (right-aligned, width 5)
printf("%-5d|\\n",   count);    // 42___|  (left-aligned)
printf("%05d\\n",    count);    // 00042  (zero-padded)
    """, language="c")

    st.info("**Precision Control Summary:** `%d` → integers (no precision). `%.nf` → n decimal places for float/double. `%.ns` → at most n characters of a string. `%e` → scientific notation (critical for printing Avogadro's number, very small enzyme concentrations etc.).")
    st.warning("⚠️ **Strings with spaces:** `scanf(\"%s\")` stops at the first whitespace — it will only read one word. For DNA sequence headers or multi-word strain names, use `fgets()`. See the Strings module for details.")

    st.divider()

    # --- 3. Escape Sequences ---
    st.markdown("### 3️⃣ Escape Sequences")
    st.write("""
    Escape sequences begin with a backslash `\\` and represent characters that cannot be typed 
    directly in a string literal — either because they are non-printable (newline, tab) or because 
    they are special characters in C syntax (backslash, double quote).
    """)

    # FIX: Expanded escape table — added \0, \a, \', hex/octal forms
    escape_data = {
        "Sequence": [
            "\\n", "\\t", "\\v", "\\b",
            "\\r", "\\a", "\\0",
            "\\\\", "\\\"", "\\'",
            "\\xHH", "\\OOO"
        ],
        "Name": [
            "Newline", "Horizontal Tab", "Vertical Tab", "Backspace",
            "Carriage Return", "Alert / Bell", "Null Character (String Terminator)",
            "Backslash", "Double Quote", "Single Quote",
            "Hex escape", "Octal escape"
        ],
        "Description / Use": [
            "Moves cursor to next line — most common escape sequence",
            "Inserts a tab stop — used to create TSV-formatted output",
            "Moves cursor down one line without carriage return",
            "Moves cursor one position back",
            "Moves cursor to start of current line (used in progress bars)",
            "Produces an audible beep (if terminal supports it)",
            "Marks the END of every C string — must never be overwritten",
            "Prints a literal backslash character",
            "Prints a literal double-quote inside a string",
            "Prints a literal single-quote (rarely needed)",
            "Prints the character with that hex code: e.g., \\x41 = 'A'",
            "Prints the character with that octal code: e.g., \\101 = 'A'"
        ]
    }
    st.table(escape_data)

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 14px; border-radius: 6px; border-left: 3px solid #00599C; margin-bottom: 10px;">
        <b>📌 Critical — The Null Terminator <code>\\0</code>:</b> Every C string ends with <code>\\0</code> (ASCII value 0).
        It is automatically added by the compiler when you write <code>"ATGCG"</code>, making it 6 bytes in memory, not 5.
        String functions like <code>strlen()</code> count characters <i>up to but not including</i> <code>\\0</code>.
        Accidentally overwriting it causes the program to read garbage memory beyond the string.
        </div>
    ''', unsafe_allow_html=True)

    st.markdown("**Escape sequences in action — structured lab output:**")
    st.code(r"""printf("Sample\tStrain\t\tOD600\tpH\n");
printf("S001\tE. coli K-12\t0.732\t6.82\n");
printf("S002\tB. subtilis\t1.041\t7.10\n");
/* Output (tab-separated, TSV-compatible):
   Sample  Strain          OD600   pH
   S001    E. coli K-12    0.732   6.82
   S002    B. subtilis     1.041   7.10  */

printf("Sequence: \"ATGCGATCG\"\n");   /* prints literal quotes */
printf("Path: C:\\\\data\\\\genome.fa\n"); /* prints backslashes */
    """, language="c")

    st.divider()

    # --- 4. Unformatted I/O ---
    st.markdown("### 4️⃣ Unformatted I/O Functions")
    st.write("For simpler tasks not requiring format specifiers, C provides character- and string-level I/O functions:")

    unf_col1, unf_col2 = st.columns(2)
    with unf_col1:
        st.markdown("**Character-Level**")
        st.code("""#include <stdio.h>

/* getchar() — reads one char from stdin */
char base;
printf("Enter nucleotide base: ");
base = getchar();   // reads 'A', 'T', 'G', or 'C'

/* putchar() — writes one char to stdout */
putchar(base);      // prints the character
putchar('\\n');      // prints newline
        """, language="c")

    with unf_col2:
        st.markdown("**String-Level**")
        st.code("""/* puts() — writes string + automatic newline */
char strain[] = "E. coli";
puts(strain);   // prints "E. coli\\n"

/* fgets() — SAFE string input (preferred over gets) */
char sequence[100];
fgets(sequence, sizeof(sequence), stdin);
/* Reads up to 99 chars (leaves room for \\0),
   stops at newline or EOF, NEVER overflows buffer */
        """, language="c")

    # FIX: Proper danger warning for gets() — was just a parenthetical note before
    st.error("""🚫 **NEVER use `gets()`** — it was **removed from the C standard in C11** because it performs no bounds checking, making it trivially exploitable for buffer overflow attacks. It will overflow any buffer if the user types more characters than allocated. Always use `fgets(buffer, size, stdin)` instead.""")

    st.divider()

    # --- 5. The Dangling Newline / Input Buffer Problem ---
    st.markdown("### 5️⃣ Handling the Input Buffer")
    st.write("""
    One of the most common bugs for new C programmers — and a frequent exam scenario — is the 
    **Dangling Newline** problem. When you press Enter after a `scanf()`, the `\\n` character 
    stays in the input buffer. The next `scanf(\"%c\")` reads that leftover `\\n` instead of 
    waiting for your actual input.
    """)

    buf_col1, buf_col2 = st.columns(2)
    with buf_col1:
        st.markdown("**❌ The Problem:**")
        st.code("""int id;
char grade;

scanf("%d", &id);     // User types 101 + Enter
                      // Buffer now contains: '\\n'
scanf("%c", &grade);  // Reads '\\n' immediately!
                      // grade = '\\n' — WRONG

printf("ID: %d, Grade: %c\\n", id, grade);
// Output: ID: 101, Grade:
// (grade is a newline, appears empty)
        """, language="c")

    with buf_col2:
        st.markdown("**✅ Solutions:**")
        st.code("""/* Solution 1: Leading space in format string
   (space in format = skip all whitespace inc. \\n) */
scanf(" %c", &grade);    // Note the space before %c

/* Solution 2: getchar() to consume the newline */
scanf("%d", &id);
getchar();               // manually consume the '\\n'
scanf("%c", &grade);

/* Solution 3: Use fgets() for all string/char input
   — avoids buffer issues entirely */
char input[10];
fgets(input, sizeof(input), stdin);
grade = input[0];        // take first character
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 About fflush(stdin):</b> You may see some textbooks use <code>fflush(stdin)</code> to clear the buffer.
        This works on Windows (MSVC compiler) but is <b>undefined behaviour</b> in the C standard — 
        <code>fflush()</code> is only guaranteed to work on <i>output</i> streams. 
        The portable solutions are the leading space or <code>getchar()</code> loop shown above.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: I/O in Bioinformatics & Lab Automation</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Proper I/O formatting is the difference between useful data and noise in scientific computing:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>TSV / CSV output:</b> Using <code>\\t</code> between fields and <code>\\n</code> at the end of each record produces Tab-Separated Value files that bioinformatics tools (R, Python pandas, Excel) can directly ingest — no post-processing needed.</li>
                <li><b>Scientific notation:</b> Use <code>%e</code> or <code>%g</code> for very small or large values — enzyme concentrations in nanomolar (e.g., <code>2.5e-9</code>), Avogadro's number (<code>6.022e+23</code>), or genome base pair counts.</li>
                <li><b>FASTA format reading:</b> Genome sequence files begin with a <code>&gt;</code> header line, then sequence lines. Parsing these correctly requires <code>fgets()</code> in a loop — <code>scanf("%s")</code> would break on the space in <code>&gt;chr1 Homo sapiens</code>.</li>
                <li><b>Precision in measurements:</b> An OD600 reading reported as <code>0.73</code> vs <code>0.7320</code> can change interpretations of growth phase. Always use <code>%.4f</code> or higher for spectrophotometric data in published output.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.info("💡 **Moving Beyond the Console:** You've learned `printf()` to show data on screen. In **Module 13 (File I/O)**, we will use `fprintf()` to write that same formatted output permanently to `.txt`, `.tsv`, or `.csv` files — the standard output format for lab data pipelines.")

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What format specifier would you use to print Avogadro's number (6.022 × 10²³) in scientific notation?"):
        st.success("""**Answer:** `%e` or `%E`. 

```c
double avogadro = 6.022e23;
printf("%e\\n",   avogadro);   // 6.022000e+23
printf("%.3e\\n", avogadro);   // 6.022e+23  (3 decimal places)
printf("%g\\n",   avogadro);   // 6.022e+23  (%g auto-picks scientific for large values)
```
Use `%.3e` for clean scientific output in published data.""")

    with st.expander("Q2: What is the output of: `printf(\"%08.3f\", 3.14);`"):
        st.success("**Answer:** `0003.140` — the number 3.14 formatted to 3 decimal places (`3.140`), right-aligned in a field of total width 8, with the remaining space zero-padded on the left. Total characters: `0003.140` = 8 characters.")

    with st.expander("Q3: Why was `gets()` removed from C11, and what should you use instead?"):
        st.success("**Answer:** `gets()` was removed because it performs **no bounds checking** — it reads characters until a newline regardless of how large the destination buffer is. An attacker (or simply a user) can type more characters than the buffer holds, overwriting adjacent memory — this is a **buffer overflow vulnerability**. Use `fgets(buffer, sizeof(buffer), stdin)` instead — it takes a size argument and never reads more than `size - 1` characters, always leaving room for the `\\0` terminator.")

    with st.expander("Q4: A student runs this code and finds `grade` is always a newline. What is wrong and how do you fix it?\n`scanf(\"%d\", &id); scanf(\"%c\", &grade);`"):
        st.success("""**Answer:** This is the **dangling newline problem**. When the user types the integer and presses Enter, the `\\n` (newline) is left in the input buffer. The second `scanf(\"%c\")` immediately reads that `\\n` instead of waiting for new input.

**Fix:** Add a leading space: `scanf(\" %c\", &grade);` — the space in the format string tells `scanf` to skip any whitespace (including the leftover `\\n`) before reading the character.""")

    with st.expander("Q5: What is the null terminator `\\0`, and why does `char seq[5] = \"ATGC\"` use 5 bytes for only 4 characters?"):
        st.success("""**Answer:** `\\0` is the **null terminator** — a byte with ASCII value 0 that marks the end of every C string. The compiler automatically appends it. 

`\"ATGC\"` is stored in memory as: `A  T  G  C  \\0` — 5 bytes total. The array declaration `char seq[5]` reserves exactly 5 bytes to accommodate all 4 characters plus the terminator. 

If you declared `char seq[4] = \"ATGC\"` you would have **no room for `\\0`** — string functions like `strlen()` and `printf(\"%s\")` would read past the end of the array into garbage memory (undefined behaviour).""")

if __name__ == "__main__":
    render()