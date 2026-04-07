import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h3 style="color: white; margin: 0; font-family: sans-serif;">🧮 Module 15: Standard Libraries & Scientific Computing</h3>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Powering Natural Sciences with C's Built-In Toolkit</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to use key functions from `<math.h>`, `<stdlib.h>`, `<time.h>`, and `<ctype.h>`, build a complete microbial growth model in C, and explain how the preprocessor resolves `#include` directives.")

    st.write("")

    st.markdown("""
    In C, **libraries** are collections of pre-compiled, optimised functions that give you capabilities
    beyond the core language. Rather than writing your own square root or random number generator,
    you `#include` the relevant header and call the function directly.
    This module explores the mathematical and system-level libraries that make C a
    **Computational Biology** platform.
    """)

    st.divider()

    # --- 1. How Libraries Work ---
    st.markdown("### 1️⃣ How Libraries Work: Preprocessor & Linker")
    st.write("""
    Before the compiler sees your code, the **C Preprocessor** processes `#include` directives.
    It copies the named header file's function *declarations* (prototypes) into your source.
    The actual compiled function *definitions* live in a separate `.a` or `.so` library file
    that the **Linker** attaches to your executable at build time.
    """)

    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Build pipeline:</b>
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
Your .c file
    → Preprocessor (#include copies headers in)
    → Compiler (translates to object .o file)
    → Linker (attaches library .a/.so functions)
    → Executable binary</pre>
        <b>Note:</b> <code>&lt;math.h&gt;</code> functions require <code>-lm</code> flag when compiling on Linux/macOS:
        <code>gcc program.c -lm -o program</code>
        </div>
    ''', unsafe_allow_html=True)

    lib_col1, lib_col2 = st.columns(2)
    with lib_col1:
        st.markdown("**Standard & Utility headers:**")
        st.code("""#include <stdio.h>    /* printf, scanf, fopen, fprintf  */
#include <stdlib.h>   /* malloc, free, rand, srand, exit */
#include <string.h>   /* strlen, strcpy, strcmp, strstr  */
#include <time.h>     /* time(), clock(), difftime()     */
#include <ctype.h>    /* toupper, isalpha, isdigit       */
#include <limits.h>   /* INT_MAX, LONG_MAX, CHAR_MAX     */
        """, language="c")

    with lib_col2:
        st.markdown("**Scientific & Logic headers:**")
        st.code("""#include <math.h>     /* exp, log, sqrt, pow, sin, cos  */
#include <stdbool.h>  /* bool, true, false (C99+)        */
#include <stdint.h>   /* int32_t, uint64_t (fixed-size)  */
#include <assert.h>   /* assert() for debug validation   */
#include <errno.h>    /* error codes (ENOMEM, ENOENT...) */
        """, language="c")

    st.divider()

    # --- 2. <math.h> ---
    st.markdown("### 2️⃣ Mathematical Functions — `<math.h>`")
    st.write("All `<math.h>` functions take `double` arguments and return `double`. They provide the precision needed for biochemical and biophysical modelling.")

    # FIX: Expanded math.h table — added log, ceil, floor, sin, cos, tan, fmod
    st.table({
        "Function": [
            "exp(x)", "log(x)", "log10(x)", "log2(x)",
            "pow(b, e)", "sqrt(x)", "fabs(x)",
            "ceil(x)", "floor(x)", "fmod(x, y)",
            "sin(x)", "cos(x)", "tan(x)"
        ],
        "Mathematical Meaning": [
            "eˣ (natural exponential)", "Natural log (base e)", "Log base 10", "Log base 2",
            "b raised to power e", "Square root", "Absolute value (float)",
            "Round UP to nearest integer", "Round DOWN to nearest integer", "Floating-point remainder of x÷y",
            "Sine (x in radians)", "Cosine (x in radians)", "Tangent (x in radians)"
        ],
        "Bioscience Application": [
            "Exponential bacterial growth: N₀·eʳᵗ",
            "Doubling time: ln(2)/r; entropy calculations",
            "pH: -log₁₀([H⁺]); absorbance: log₁₀(I₀/I)",
            "Sequence information content (bits per position)",
            "Dilution series, dosage scaling, Hill equation",
            "Standard deviation from variance",
            "Error magnitude, residuals in regression",
            "Round up sample count to whole wells",
            "Round down read count to complete codons",
            "Floating-point codon position check",
            "Wave optics in microscopy; oscillatory models",
            "Phase calculations in circular statistics",
            "Slope/angle calculations in fluorescence"
        ]
    })

    st.code("""#include <math.h>

/* pH from H+ concentration */
double h_plus = 3.16e-7;      /* mol/L */
double pH = -log10(h_plus);
printf("pH = %.2f\\n", pH);    /* pH = 6.50 */

/* Absorbance from transmittance */
double T = 0.15;               /* 15% transmittance */
double A = -log10(T);
printf("Absorbance = %.4f\\n", A);   /* 0.8239 */

/* Doubling time from growth rate */
double r = 0.35;               /* h⁻¹ */
double td = log(2.0) / r;
printf("Doubling time: %.2f h\\n", td);  /* 1.98 h */
    """, language="c")

    st.divider()

    # --- 3. <ctype.h> ---
    st.markdown("### 3️⃣ Character Validation & Cleaning — `<ctype.h>`")
    st.write("Essential for cleaning and validating raw sequence input before analysis.")

    st.table({
        "Function": ["toupper(c)", "tolower(c)", "isalpha(c)", "isdigit(c)", "isspace(c)", "isupper(c)", "islower(c)"],
        "Returns / Action": [
            "Uppercase version of c", "Lowercase version of c",
            "Non-zero if c is a letter (A-Z, a-z)",
            "Non-zero if c is a digit (0-9)",
            "Non-zero if c is whitespace (space, tab, newline)",
            "Non-zero if c is uppercase", "Non-zero if c is lowercase"
        ],
        "Sequence Analysis Use": [
            "Normalise soft-masked bases (a→A, t→T)", "Convert sequence to lowercase for masking",
            "Validate that a base character is a letter",
            "Check that a quality score digit is numeric",
            "Strip whitespace/newline from fgets() output",
            "Check if base is already normalised", "Detect soft-masked (repeat) regions"
        ]
    })

    st.code("""#include <ctype.h>
#include <string.h>

char raw_seq[] = "atgCCGata\\n";   /* mixed case, trailing newline */
int  len = strlen(raw_seq);

/* Normalise: uppercase and remove non-ATGC characters */
int clean_len = 0;
char clean[100];

for (int i = 0; i < len; i++) {
    char base = toupper(raw_seq[i]);
    if (base == 'A' || base == 'T' || base == 'G' || base == 'C')
        clean[clean_len++] = base;
}
clean[clean_len] = '\\0';

printf("Raw:   %s\\n",   raw_seq);   /* atgCCGata\\n */
printf("Clean: %s\\n",   clean);     /* ATGCCGATA   */
    """, language="c")

    st.divider()

    # --- 4. Practical: Growth Engine ---
    st.markdown("### 4️⃣ Practical: Microbial Growth Engine")
    st.write(r"Using the exponential growth formula $N_t = N_0 \cdot e^{rt}$, we model population dynamics in C with full lab report output.")

    st.code("""#include <stdio.h>
#include <math.h>

int main() {
    double n0    = 100.0;    /* initial CFU/mL */
    double r     = 0.35;     /* growth rate h⁻¹ */
    int    hours = 12;

    printf("=== MICROBIOLOGY GROWTH REPORT ===\\n");
    printf("%-8s %-15s %-12s\\n", "Hour", "CFU/mL", "OD600 (est.)");
    printf("%-8s %-15s %-12s\\n", "----", "------", "------------");

    for (int t = 0; t <= hours; t += 2) {
        double nt  = n0 * exp(r * t);
        double od  = nt / 5e8;         /* rough OD600 estimate */
        printf("%-8d %-15.2e %-12.4f\\n", t, nt, od);
    }

    double td = log(2.0) / r;
    printf("\\nDoubling time: %.2f hours\\n", td);
    printf("Final count:   %.2e CFU/mL\\n", n0 * exp(r * hours));
    return 0;
}
/* Output (sample):
   Hour     CFU/mL          OD600 (est.)
   0        1.00e+02        0.0000
   2        2.01e+02        0.0000
   ...
   12       6.69e+03        0.0000
   Doubling time: 1.98 hours */
    """, language="c")

    st.divider()

    # --- 5. Stochastic Modeling ---
    st.markdown("### 5️⃣ Stochastic Modelling — `<stdlib.h>` & `<time.h>`")
    st.write("Simulating random events like point mutations or genetic drift requires a pseudo-random number generator seeded with the current time.")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #FFFFFF; margin-bottom: 10px;">
        <b>⚠️ Common mistake fixed:</b> <code>srand(time(0))</code> must be called <b>once</b> in <code>main()</code>,
        not inside the simulation function. Calling it inside a function that runs in a loop seeds with the same
        second-resolution timestamp on every call, producing the same "random" number repeatedly.
        </div>
    ''', unsafe_allow_html=True)

    # FIX: Moved srand() to main() where it belongs
    st.code("""#include <stdio.h>
#include <stdlib.h>
#include <time.h>

/* Simulate one generation — returns 1 if mutation occurred */
int simulate_generation(double mutation_rate) {
    /* rand() returns 0 to RAND_MAX */
    double prob = (double) rand() / RAND_MAX;
    return prob < mutation_rate;
}

char mutate_base(char base) {
    char bases[] = "ATGC";
    char new_base;
    do {
        new_base = bases[rand() % 4];
    } while (new_base == base);    /* ensure it actually changes */
    return new_base;
}

int main() {
    srand((unsigned int) time(0));  /* seed ONCE in main */

    char sequence[] = "ATGCGATCGAATTCGG";
    int  len = strlen(sequence);       /* requires <string.h> */
    double mut_rate = 0.05;            /* 5% per base per generation */

    printf("Original:  %s\\n", sequence);

    for (int i = 0; i < len; i++) {
        if (simulate_generation(mut_rate)) {
            char orig = sequence[i];
            sequence[i] = mutate_base(sequence[i]);
            printf("Mutation at pos %d: %c→%c\\n",
                   i, orig, sequence[i]);
        }
    }

    printf("Mutated:   %s\\n", sequence);
    return 0;
}
    """, language="c")

    st.divider()

    # --- 6. <limits.h> & <stdint.h> ---
    st.markdown("### 6️⃣ Data Type Ranges — `<limits.h>` & `<stdint.h>`")
    st.write("When processing large genomic datasets, knowing and checking data type limits prevents silent integer overflow.")

    lim_col1, lim_col2 = st.columns(2)
    with lim_col1:
        st.markdown("**`<limits.h>` — portable range constants:**")
        st.code("""#include <limits.h>
#include <stdio.h>

printf("INT_MAX:  %d\\n",  INT_MAX);     /* 2,147,483,647 */
printf("INT_MIN:  %d\\n",  INT_MIN);     /* -2,147,483,648 */
printf("LONG_MAX: %ld\\n", LONG_MAX);    /* system-dependent */
printf("CHAR_MAX: %d\\n",  CHAR_MAX);    /* 127 */

/* Safety check before accumulating genome positions */
long pos = 3199999999L;   /* 3.2 billion */
if (pos > INT_MAX) {
    printf("Warning: use long, not int!\\n");
}
        """, language="c")

    with lim_col2:
        st.markdown("**`<stdint.h>` — guaranteed-size types (C99+):**")
        st.code("""#include <stdint.h>

/* Exact-width types — size guaranteed on all platforms */
int32_t   read_count;      /* always exactly 32 bits */
uint64_t  genome_pos;      /* always 64 bits, unsigned */
int8_t    quality_score;   /* 8-bit quality (PHRED) */

/* These are critical for binary file formats (BAM/VCF)
   where field widths are fixed by the specification */

genome_pos = 3200000000ULL;   /* 3.2 billion — safe in uint64_t */
printf("Position: %llu\\n", genome_pos);
        """, language="c")

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 15px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Justification: C as a Computational Biology Platform</h4>
            <p style="color: #333; font-size: 0.95rem;">
                The standard library transforms C from a systems language into a complete computational biology toolkit:-
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Growth modelling:</b> <code>exp()</code> and <code>log()</code> from <code>&lt;math.h&gt;</code> implement the Monod equation,
                Michaelis-Menten kinetics, and exponential growth/decay — the mathematical backbone of systems biology.</li>
                <li><b>pH and absorbance:</b> <code>log10()</code> is used directly in pH calculation (<code>-log10([H⁺])</code>) and
                Beer-Lambert law (<code>A = -log10(T)</code>) — both daily tools in a microbiology lab.</li>
                <li><b>Monte Carlo simulation:</b> <code>rand()</code> seeded with <code>time(0)</code> enables stochastic modelling of
                mutation accumulation, genetic drift, and molecular diffusion — as used in population genetics simulators like SLIM.</li>
                <li><b>Overflow safety for genomics:</b> <code>uint64_t</code> from <code>&lt;stdint.h&gt;</code> stores genome coordinates
                safely — the human genome's 3.2 billion base pair positions exceed <code>INT_MAX</code> (2.1 billion).</li>
                <li><b>Sequence cleaning:</b> <code>toupper()</code> and <code>isalpha()</code> from <code>&lt;ctype.h&gt;</code> normalise
                raw FASTQ data before alignment — every production bioinformatics pipeline includes this step.</li>
            </ul>
            <p style="color: #555; font-size: 0.9rem; margin-top: 10px;">
                This completes our journey from binary machine code (Module 1) through structured programming, data types,
                functions, and file I/O — to building modular, accurate, scientifically-grounded C programs.
                The speed of silicon, harnessed in service of understanding life itself.
            </p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review — Final Module")

    with st.expander("Q1: Calculate the pH of a solution with [H⁺] = 5.0 × 10⁻⁸ mol/L using `<math.h>`. Show the C expression."):
        st.success("""**Answer:**
```c
#include <math.h>
double h_plus = 5.0e-8;
double pH = -log10(h_plus);
printf("pH = %.2f\\n", pH);   /* pH = 7.30 */
```
The Henderson-Hasselbalch formula uses `log10()` — this is one of the most direct applications of `<math.h>` in microbiology.""")

    with st.expander("Q2: Why must `srand(time(0))` be called only once, at the start of `main()`, not inside a loop or function?"):
        st.success("""**Answer:** `srand()` seeds the pseudo-random number generator. `time(0)` returns the current Unix timestamp in **whole seconds**. If `srand(time(0))` is inside a function called in a tight loop, multiple calls within the same second get the **identical seed**, producing the **identical sequence** of random numbers — so every "random" choice is the same. Seeding once in `main()` initialises the sequence once, and subsequent `rand()` calls produce a different number each time.""")

    with st.expander("Q3: What does `log()` compute vs `log10()` in `<math.h>`? Which do you use for pH and which for doubling time?"):
        st.success("""**Answer:**
- `log(x)` → **natural logarithm** (base *e* ≈ 2.718). Used for: doubling time (`td = log(2.0)/r`), entropy, growth rate calculations.
- `log10(x)` → **base-10 logarithm**. Used for: pH (`-log10([H⁺])`), absorbance (`-log10(T)`), any formula explicitly in base-10.

A common error is using `log()` where `log10()` is needed — pH computed with `log()` gives the wrong answer (off by a factor of ln(10) ≈ 2.303).""")

    with st.expander("Q4: Why does a bioinformatics program need `<stdint.h>` when working with genome coordinates?"):
        st.success("""**Answer:** The human genome has ~3.2 billion base pairs. A signed `int` on most systems can only hold up to **2,147,483,647** (~2.1 billion) — storing position 3,000,000,000 in an `int` causes **integer overflow**, silently wrapping to a negative number and producing completely wrong coordinates.

`uint64_t` from `<stdint.h>` guarantees an **unsigned 64-bit integer** on all platforms, capable of storing values up to ~18.4 × 10¹⁸ — more than sufficient for any genomic coordinate. This is why BAM/CRAM file formats (which store genome positions) use 32- and 64-bit fixed-width types specified in their binary format documentation.""")

    with st.expander("Q5: Name the library function for each task: (a) e^x, (b) -log₁₀([H⁺]), (c) normalise lowercase 'a' to 'A', (d) check if a character is a digit, (e) generate a random integer."):
        st.success("""**Answer:**
- (a) `exp(x)` from `<math.h>`
- (b) `-log10(h_plus)` from `<math.h>`
- (c) `toupper('a')` from `<ctype.h>` → returns `'A'`
- (d) `isdigit(c)` from `<ctype.h>` → returns non-zero if `c` is '0'–'9'
- (e) `rand()` from `<stdlib.h>` (seed first with `srand(time(0))` from `<time.h>`)""")

if __name__ == "__main__":
    render()