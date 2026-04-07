import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h2 style="color: white; margin: 0; font-family: sans-serif;">🧬 Module 14: Strings & Sequence Processing</h2>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Character Arrays, String Functions, and Biological Sequence Analysis</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to declare and initialise C strings, explain the null terminator's role, use all major `<string.h>` functions correctly, handle string input safely, perform GC content analysis, and traverse strings with pointer arithmetic.")

    st.write("")

    st.markdown("""
    In the Natural Sciences, strings represent **genetic codes (DNA/RNA)** and **protein sequences**.
    In C, a string is **not** a built-in type — it is a **one-dimensional character array** that must end
    with a `\\0` (null terminator, ASCII 0) to mark the end of the sequence. Everything else about strings
    follows from this single rule.
    """)

    st.divider()

    # --- 1. Declaration & Memory Layout ---
    st.markdown("### 1️⃣ String Declaration & Memory Layout")
    st.write("When you declare a string, C allocates a contiguous block of bytes. The null terminator is the sentinel that tells every string function where the string ends.")

    mem_col1, mem_col2 = st.columns(2)
    with mem_col1:
        st.markdown("**Three ways to declare a string:**")
        st.code("""/* 1. Array initialised from a string literal (most common) */
char dna[] = "ATGC";
/* Memory: ['A']['T']['G']['C']['\\0']  — 5 bytes */

/* 2. Array with explicit size — must be >= length + 1 */
char rna[10] = "AUGC";
/* Memory: ['A']['U']['G']['C']['\\0'][?][?][?][?][?]
   remaining bytes are zero-initialised */

/* 3. Pointer to a string literal (read-only!) */
char *motif = "TATAAA";
/* motif points to a read-only section of memory.
   Modifying motif[0] is undefined behaviour. */
        """, language="c")

    with mem_col2:
        st.markdown("**Memory layout — why 5 bytes for 4 characters:**")
        st.code("""char dna[] = "ATGC";

/* Index:    [0]  [1]  [2]  [3]  [4]  */
/* Value:    'A'  'T'  'G'  'C'  '\\0' */
/* ASCII:     65   84   71   67    0  */

printf("Length: %zu\\n", strlen(dna));  /* 4 */
printf("Size:   %zu\\n", sizeof(dna));  /* 5 */
/* strlen counts chars up to (not including) \\0
   sizeof returns total array size in bytes   */

/* Individual character access */
printf("Base 1: %c (ASCII %d)\\n",
       dna[0], dna[0]);      /* A (ASCII 65) */
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>📌 Critical — The Null Terminator <code>\\0</code>:</b>
        All standard string functions (<code>strlen</code>, <code>printf("%s")</code>, <code>strcpy</code>) stop at the first <code>\\0</code>.
        Accidentally overwriting it causes these functions to read past your array into adjacent memory — 
        producing garbage output or a crash. Always allocate <b>length + 1</b> bytes.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. string.h Library ---
    st.markdown("### 2️⃣ Standard String Operations — `<string.h>`")
    st.write("The `<string.h>` library provides all standard string manipulation functions. All operate on null-terminated character arrays.")

    # FIX: Expanded table — added strncpy, strncat, strchr, strrchr, strtok
    st.table({
        "Function": [
            "strlen(s)", "strcpy(dst, src)", "strncpy(dst, src, n)",
            "strcat(dst, src)", "strncat(dst, src, n)",
            "strcmp(s1, s2)", "strncmp(s1, s2, n)",
            "strstr(s1, s2)", "strchr(s, c)", "strtok(s, delim)"
        ],
        "Returns / Action": [
            "Length (chars before \\0)", "Copies src into dst (dst must be big enough)",
            "Copies at most n chars (safer — always null-terminate manually after)",
            "Appends src onto end of dst", "Appends at most n chars of src (safer)",
            "0 if equal; <0 if s1<s2; >0 if s1>s2 (lexicographic)",
            "Compares first n characters only",
            "Pointer to first occurrence of s2 in s1; NULL if not found",
            "Pointer to first occurrence of char c in s; NULL if not found",
            "Splits s by delimiter; call repeatedly for successive tokens"
        ],
        "Bio-Scientific Use": [
            "Validate read length before processing", "Duplicate a gene string for modification",
            "Safe copy of fixed-width sequence fields",
            "Concatenate exon fragments into transcript", "Safe ligation with length control",
            "Check exact sequence match / detect mutation (0=no mutation)",
            "Compare first N bases (compare primers, short motifs)",
            "Find TATA box, Shine-Dalgarno sequence, restriction site",
            "Find start codon 'A' position or restriction character",
            "Parse comma-separated FASTA headers into fields"
        ]
    })

    st.markdown("**Key `strcmp` return values — most commonly misunderstood:**")
    st.code("""char ref[]  = "ATGCGA";
char read[] = "ATGCGA";
char mut[]  = "ATGCGG";   /* last base changed G→G (same here for demo) */

int result = strcmp(ref, read);
if (result == 0)
    printf("Exact match — no mutation\\n");
else if (result < 0)
    printf("ref comes before read lexicographically\\n");
else
    printf("ref comes after read lexicographically\\n");

/* strstr — find restriction site EcoRI (GAATTC) */
char *site = strstr("AAGAATTCGG", "GAATTC");
if (site != NULL)
    printf("EcoRI site found at position %ld\\n",
           site - "AAGAATTCGG");    /* pointer arithmetic: position 2 */
    """, language="c")

    st.divider()

    # --- 3. Safe Input Handling ---
    st.markdown("### 3️⃣ String Input — Safe vs Unsafe")
    st.write("Reading strings from the user or a file requires careful handling. The wrong approach causes buffer overflows.")

    input_col1, input_col2 = st.columns(2)
    with input_col1:
        st.markdown("**❌ Unsafe — `scanf(\"%s\")`:**")
        st.code("""char seq[20];

/* DANGEROUS — two problems:
   1. Stops at whitespace — misses sequence headers
   2. No length limit — typing >19 chars overflows buffer */
scanf("%s", seq);

/* Even with width limit, stops at spaces: */
scanf("%19s", seq);   /* safer but still stops at space */
        """, language="c")

    with input_col2:
        st.markdown("**✅ Safe — `fgets()`:**")
        st.code("""char seq[200];

/* fgets reads up to (size-1) chars including spaces,
   stops at newline or EOF, always adds \\0 */
fgets(seq, sizeof(seq), stdin);

/* Note: fgets keeps the trailing \\n character.
   Remove it if needed: */
seq[strcspn(seq, "\\n")] = '\\0';

/* Now seq contains the line without trailing newline */
printf("Sequence: %s  (len=%zu)\\n",
       seq, strlen(seq));
        """, language="c")

    st.warning("⚠️ **Never use `=` to copy strings.** `str1 = str2` only copies the pointer address — both names now point to the same memory. Use `strcpy(str1, str2)` for a true copy. And always ensure `str1` is large enough: `strcpy` into a too-small buffer causes a buffer overflow.")

    st.divider()

    # --- 4. Practical: GC Content ---
    st.markdown("### 4️⃣ Practical: GC Content & Sequence Analysis")
    st.write("GC content determines DNA thermal stability — higher GC% means higher melting temperature (Tm). This is fundamental in primer design and identifying genomic regions.")

    st.code("""#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char sequence[] = "ATGCCGATAgcTAGCCG";  /* mixed case input */
    int  len = strlen(sequence);
    int  gc = 0, at = 0, invalid = 0;

    for (int i = 0; i < len; i++) {
        char base = toupper(sequence[i]);    /* normalise to uppercase */
        if      (base == 'G' || base == 'C') gc++;
        else if (base == 'A' || base == 'T') at++;
        else                                  invalid++;
    }

    int valid = gc + at;
    printf("Sequence:   %s\\n",  sequence);
    printf("Length:     %d bp\\n", len);
    printf("GC count:   %d\\n",  gc);
    printf("AT count:   %d\\n",  at);
    printf("Invalid:    %d\\n",  invalid);
    printf("GC Content: %.2f%%\\n", (float)gc / valid * 100);
    printf("AT Content: %.2f%%\\n", (float)at / valid * 100);

    /* Find start codon ATG */
    char *start_codon = strstr(sequence, "ATG");
    if (start_codon)
        printf("Start codon at position: %ld\\n",
               start_codon - sequence);

    return 0;
}
/* Output:
   Sequence:   ATGCCGATAgcTAGCCG
   GC Content: 58.82%
   Start codon at position: 0  */
    """, language="c")

    st.divider()

    # --- 5. Pointer Arithmetic with Strings ---
    st.markdown("### 5️⃣ Pointer Arithmetic with Strings")
    st.write("A string's name is a pointer to its first character. Pointer arithmetic lets you traverse and slice sequences without copying — critical for high-speed processing.")

    ptr_col1, ptr_col2 = st.columns(2)
    with ptr_col1:
        st.markdown("**Character-by-character traversal:**")
        st.code("""char dna[] = "ATGCGATCG";
char *ptr  = dna;            /* points to 'A' */

while (*ptr != '\\0') {
    printf("%c ", *ptr);     /* print current base */
    ptr++;                   /* advance one byte */
}
/* Output: A T G C G A T C G */

/* Jump to position 3 directly */
ptr = dna + 3;
printf("\\nFrom pos 3: %s\\n", ptr);  /* CGATCG */
        """, language="c")

    with ptr_col2:
        st.markdown("**Sliding window — codon reading frame:**")
        st.code("""char cds[] = "ATGAAAGCCTGA";
int  len   = strlen(cds);

printf("Codons in reading frame 0:\\n");
for (int i = 0; i + 2 < len; i += 3) {
    /* Print 3-character codon without copying */
    printf("  %c%c%c\\n", cds[i], cds[i+1], cds[i+2]);
}
/* Output:
   ATG  (Met — start codon)
   AAA  (Lys)
   GCC  (Ala)
   TGA  (STOP) */

/* strncmp to check for start codon */
if (strncmp(cds, "ATG", 3) == 0)
    printf("Valid ORF: starts with Met\\n");
        """, language="c")

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 15px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Strings as the Language of Life</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Every major bioinformatics operation is fundamentally a string operation:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Sequence alignment (BLAST, BWA):</b> Uses <code>strcmp</code>-like comparisons across millions of read–reference pairs. Pointer arithmetic slides the comparison window across the reference without copying.</li>
                <li><b>Motif finding:</b> <code>strstr(sequence, "TATAAA")</code> locates the TATA box promoter; <code>strstr(sequence, "GAATTC")</code> finds an EcoRI restriction site.</li>
                <li><b>FASTA parsing:</b> <code>fgets()</code> reads lines; lines starting with <code>'&gt;'</code> are headers parsed with <code>strtok()</code> to split fields; other lines are sequence appended with <code>strncat()</code>.</li>
                <li><b>Codon analysis:</b> Pointer arithmetic with step size 3 reads successive codons for translation — the same logic used in ORF finders and gene prediction tools.</li>
                <li><b>Case normalisation:</b> Raw sequencing output may contain lowercase soft-masked bases. <code>toupper()</code> from <code>&lt;ctype.h&gt;</code> normalises them before analysis.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")

    with st.expander("Q1: Why does `char seq[4] = \"ATGC\"` cause a bug, but `char seq[5] = \"ATGC\"` is correct?"):
        st.success("""**Answer:** `"ATGC"` is 5 bytes in memory: `'A'`, `'T'`, `'G'`, `'C'`, `'\\0'`. With `char seq[4]`, there is no room for the null terminator — it gets placed in adjacent memory, corrupting the next variable. Functions like `strlen()` and `printf(\"%s\")` then read past `seq` until they find a `\\0` somewhere in memory — producing garbage output or a crash. Always allocate **length + 1** bytes.""")

    with st.expander("Q2: What does `strcmp(s1, s2)` return, and how do you use it to check for an exact sequence match?"):
        st.success("""**Answer:** `strcmp` returns:
- **0** — strings are identical (exact match)
- **negative** — `s1` comes before `s2` lexicographically (first differing char in `s1` has smaller ASCII value)
- **positive** — `s1` comes after `s2` lexicographically

To check for an exact match: `if (strcmp(read, reference) == 0) { /* match */ }`. A common beginner mistake is writing `if (strcmp(s1, s2)) { ... }` which is TRUE when they are **different** (non-zero), not when they are the same.""")

    with st.expander("Q3: What is the difference between `strcpy` and `strncpy`, and which should you use in scientific code?"):
        st.success("""**Answer:** `strcpy(dst, src)` copies all of `src` (including `\\0`) into `dst` with no length limit — if `src` is longer than `dst`'s buffer, it overflows. `strncpy(dst, src, n)` copies at most `n` characters, preventing overflow — but it does NOT automatically add `\\0` if `src` is `n` or more characters long, so you must manually set `dst[n-1] = '\\0'`.

In scientific code, always use `strncpy` (or the even safer `snprintf`) to prevent buffer overflows when handling user-supplied or file-sourced sequences of unknown length.""")

    with st.expander("Q4: A sequence `\"AAATGCCCGATG\"` has two ATG codons. How does `strstr()` help you find the first one, and how do you find the second?"):
        st.success("""**Answer:**
```c
char seq[] = "AAATGCCCGATG";

/* First ATG */
char *first = strstr(seq, "ATG");
printf("First ATG at: %ld\\n", first - seq);   /* 2 */

/* Second ATG — start searching AFTER the first match */
char *second = strstr(first + 1, "ATG");
printf("Second ATG at: %ld\\n", second - seq); /* 9 */
```
`first + 1` moves the search start one position past the first match, so `strstr` finds the next occurrence. Repeat in a loop to find all ORF start positions.""")

    with st.expander("Q5: What does `ptr++` do when `ptr` is a `char *` pointing into a string?"):
        st.success("""**Answer:** It advances `ptr` by **1 byte** (since `sizeof(char) == 1`), moving it to point to the next character in the string. This is pointer arithmetic — adding 1 to a `char *` moves 1 byte; adding 1 to an `int *` moves 4 bytes (on a 32-bit int system).

This is how `while (*ptr != '\\0') { process(*ptr); ptr++; }` traverses a string character by character without needing an index variable — identical to `for (int i = 0; seq[i] != '\\0'; i++)`, but using pointer notation.""")

if __name__ == "__main__":
    render()