import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🧩 Module 9: Functions in C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Declaration, Definition, Scope, and the Logic of Recursion</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to write a function prototype, definition, and call correctly; distinguish call-by-value from call-by-reference; explain local vs global scope; trace a recursive call stack; and state the conditions for correct recursion.")

    st.write("")

    # --- 1. Anatomy of a Function ---
    st.markdown("### 1️⃣ The Anatomy of a Function")
    st.write("""
    A function is a self-contained, named block of statements that performs one specific task. 
    Functions are the foundation of structured programming — they eliminate code duplication and make programs testable.
    To use a function correctly, you must understand three distinct steps:
    """)

    st.markdown("""
    1. **Function Declaration (Prototype):** Tells the compiler the function's name, return type, and parameter types — *before* it is called.
    2. **Function Definition:** The actual implementation — the body with the executable statements.
    3. **Function Call:** Transfers execution control to the function and optionally captures its return value.
    """)

    # FIX: Filled blank block — added syntax anatomy before the code block
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Function definition syntax:</b>
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
return_type  function_name  (parameter_type param1, parameter_type param2, ...) {
    /* local variable declarations */
    /* executable statements      */
    return value;    ← must match return_type; omit if return_type is void
}</pre>
        </div>
    ''', unsafe_allow_html=True)

    st.code("""#include <stdio.h>

/* 1. DECLARATION (Prototype) — placed before main()
   Ends with semicolon; parameter names are optional here */
float calculate_bmi(float weight, float height);
float dilution_factor(int stock_vol, int total_vol, int steps);

int main() {
    /* 3. FUNCTION CALLS */
    float bmi = calculate_bmi(70.5, 1.75);
    printf("BMI: %.2f\\n", bmi);                    /* Output: BMI: 23.02 */

    float df = dilution_factor(1, 10, 3);
    printf("Dilution factor: %.4f\\n", df);          /* Output: 0.0010 */

    return 0;
}

/* 2. DEFINITIONS — placed after main() because prototypes declared above */
float calculate_bmi(float w, float h) {
    return w / (h * h);                             /* 70.5 / (1.75 * 1.75) */
}

float dilution_factor(int stock, int total, int steps) {
    float per_step = (float) stock / total;         /* cast to avoid integer division */
    float result = 1.0;
    for (int i = 0; i < steps; i++)
        result *= per_step;
    return result;
}
    """, language="c")

    st.divider()

    # --- 2. Parameters, Return Values, and void ---
    st.markdown("### 2️⃣ Function Parameters & Return Values")
    st.write("Functions communicate through **parameters** (input) and **return values** (output). The `return` statement both sends a value back and immediately exits the function.")

    param_col1, param_col2 = st.columns(2)
    with param_col1:
        st.markdown("**Call by Value (default in C)**")
        st.write("A **copy** of the argument is passed. Changes inside the function do NOT affect the original variable.")
        st.code("""void double_it(int x) {
    x = x * 2;            /* modifies LOCAL copy only */
    printf("Inside: %d\\n", x);
}

int main() {
    int val = 5;
    double_it(val);
    printf("Outside: %d\\n", val);
    return 0;
}
/* Output:
   Inside:  10
   Outside: 5   ← original unchanged */
        """, language="c")

        st.markdown("**The `void` Keyword**")
        st.write("`void` as return type = function returns nothing. `void` as parameter list = function takes no arguments.")
        st.code("""/* No return value, no parameters */
void print_header(void) {
    printf("=== Lab Results ===\\n");
    printf("Date: 2026-04-06\\n");
    /* no return statement needed */
}

/* No return value, but has parameters */
void log_reading(int id, float od) {
    printf("Sample %d: OD600 = %.3f\\n", id, od);
}
        """, language="c")

    with param_col2:
        st.markdown("**Call by Reference (using Pointers)**")
        st.write("A pointer (memory address) is passed. Changes inside the function **directly modify** the original variable. This is how C achieves pass-by-reference.")
        st.code("""/* & operator gets the address; * dereferences it */
void swap_samples(float *a, float *b) {
    float temp = *a;      /* dereference: read value at address */
    *a = *b;              /* write to address a */
    *b = temp;
}

int main() {
    float od1 = 0.45, od2 = 0.82;
    printf("Before: od1=%.2f  od2=%.2f\\n", od1, od2);

    swap_samples(&od1, &od2);   /* pass addresses, not values */

    printf("After:  od1=%.2f  od2=%.2f\\n", od1, od2);
    return 0;
}
/* Output:
   Before: od1=0.45  od2=0.82
   After:  od1=0.82  od2=0.45  ← originals swapped */
        """, language="c")

        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem; margin-top: 6px;">
            <b>Value vs Reference summary:</b><br>
            <b>By Value</b> → copy passed → original safe → use for read-only inputs<br>
            <b>By Reference</b> → address passed → original modified → use when function must change caller's variable or return multiple values
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 3. Scope of Variables ---
    st.markdown("### 3️⃣ Scope of Variables")
    st.write("**Scope** defines where in the program a variable is visible and accessible. C has two primary scopes related to functions:")

    scope_col1, scope_col2 = st.columns(2)
    with scope_col1:
        st.markdown("**Local Variables**")
        st.write("Declared inside a function or block `{ }`. Visible only within that block. Created when the block is entered, destroyed when it exits.")
        st.code("""void analyse(void) {
    float od = 0.72;     /* local to analyse() */
    int   count = 10;    /* local to analyse() */
    printf("%.2f\\n", od);
}

int main() {
    analyse();
    /* printf("%f", od);  ERROR — od not visible here */
    return 0;
}
        """, language="c")

    with scope_col2:
        st.markdown("**Global Variables**")
        st.write("Declared outside all functions. Visible to all functions in the file. Persist for the entire program lifetime. Use sparingly — global state makes debugging harder.")
        st.code("""int experiment_count = 0;     /* GLOBAL — all functions can see this */

void run_experiment(void) {
    experiment_count++;           /* modifies global */
    printf("Run #%d\\n", experiment_count);
}

int main() {
    run_experiment();             /* Run #1 */
    run_experiment();             /* Run #2 */
    printf("Total: %d\\n", experiment_count);  /* 2 */
    return 0;
}
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>📌 Shadowing:</b> If a local variable has the same name as a global, the local one takes precedence
        inside its block — it "shadows" the global. The global is unchanged. Avoid giving local and global variables
        the same name — it causes confusion and subtle bugs.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 4. Recursive Functions ---
    st.markdown("### 4️⃣ Recursive Functions")
    st.write("""
    **Recursion** occurs when a function calls itself — either directly or indirectly. 
    It breaks a complex problem into a smaller version of the same problem, solving it step by step 
    until a **base case** is reached that terminates the chain.
    """)

    # FIX: Filled second blank block — added the two-condition rule before the warning
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Every correct recursive function must have exactly two parts:</b>
        <ol style="margin-top: 6px; color: #FFFFFF; font-size: 0.95rem;">
            <li><b>Base Case:</b> A condition where the function returns a direct answer without calling itself.
            This is what stops the recursion.</li>
            <li><b>Recursive Case:</b> The function calls itself with a <i>simpler or smaller</i> version of the problem,
            moving towards the base case.</li>
        </ol>
        </div>
    ''', unsafe_allow_html=True)

    st.warning("**Crucial:** Without a base case, recursion never terminates — the function keeps calling itself, filling the call stack until a **Stack Overflow** error crashes the program.")

    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        st.markdown("**Recursive factorial:**")
        st.code("""int factorial(int n) {
    /* Base Case: 0! = 1  (stop here) */
    if (n == 0) return 1;

    /* Recursive Case: n! = n × (n-1)! */
    return n * factorial(n - 1);
}

int main() {
    printf("5! = %d\\n", factorial(5));
    /* Output: 5! = 120 */
    return 0;
}
        """, language="c")

    with rec_col2:
        st.markdown("**Call stack trace for `factorial(4)`:**")
        st.code("""factorial(4)
  → 4 * factorial(3)
       → 3 * factorial(2)
            → 2 * factorial(1)
                 → 1 * factorial(0)
                      → returns 1      ← BASE CASE
                 → 1 * 1 = 1
            → 2 * 1 = 2
       → 3 * 2 = 6
  → 4 * 6 = 24

Final result: 24
        """, language="text")

    st.markdown("**Scientific recursive example — GC content via recursion:**")
    st.code("""/* Count G and C bases recursively in a DNA string */
#include <string.h>

int count_gc(char *seq, int index) {
    /* Base Case: reached end of string */
    if (seq[index] == '\\0') return 0;

    /* Recursive Case: check current base, then recurse on rest */
    int is_gc = (seq[index] == 'G' || seq[index] == 'C') ? 1 : 0;
    return is_gc + count_gc(seq, index + 1);
}

int main() {
    char dna[] = "ATGCGATCGG";
    int  gc    = count_gc(dna, 0);
    printf("GC count: %d / %zu (%.1f%%)\\n",
           gc, strlen(dna), (float)gc / strlen(dna) * 100);
    /* Output: GC count: 6 / 10 (60.0%) */
    return 0;
}
    """, language="c")

    st.divider()

    # --- 5. Why Use Functions ---
    st.markdown("### 5️⃣ Why Use Functions? — Advantages")
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 18px 20px; border-radius: 8px; border: 1px solid #00599C;">
            <ul style="color: #333; font-size: 0.95rem; margin: 0;">
                <li><b>Reusability:</b> Write the logic once (e.g., <code>calculate_od600()</code>) and call it from anywhere in the program — no copy-pasting code.</li>
                <li><b>Modularity:</b> Each function does one job. Large programs are decomposed into small, independently testable units.</li>
                <li><b>Readability:</b> <code>main()</code> reads like a high-level outline: <code>load_data(); process_samples(); write_report();</code> — intention is clear.</li>
                <li><b>Easy Debugging:</b> A bug in <code>parse_fasta()</code> is confined to that function. You can test it in isolation with known inputs.</li>
                <li><b>Reduced Redundancy:</b> Avoids the maintenance nightmare of fixing the same bug in 10 places — fix the function once, fixed everywhere.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)
    st.divider()
    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 15px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Functions in Computational Biology</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Functions are the direct equivalent of standardised protocols in wet-lab science — reusable, validated procedures:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Recursion in bioinformatics:</b> The Needleman-Wunsch global sequence alignment algorithm and
                phylogenetic tree construction (divide sequences into sub-problems recursively) both rely on recursive logic.</li>
                <li><b>Call by reference for large data:</b> Passing a 3GB genome array by value would copy the entire dataset
                into the function's stack — catastrophic. Passing a pointer (address) costs just 8 bytes regardless of data size.</li>
                <li><b>Modular pipeline design:</b> A bioinformatics pipeline is a chain of functions:
                <code>read_fastq()</code> → <code>quality_filter()</code> → <code>align_to_reference()</code> → <code>call_variants()</code> → <code>write_vcf()</code>.
                Each can be developed, tested, and updated independently.</li>
                <li><b>Global variables for shared state:</b> Experiment metadata (run ID, date, instrument serial number)
                is often stored as global constants shared across all analysis functions in a pipeline.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is a function prototype (declaration), and why is it needed when the definition comes after `main()`?"):
        st.success("""**Answer:** A **function prototype** is a declaration that tells the compiler the function's name, return type, and parameter types — ending with a semicolon. Example: `float calculate_bmi(float, float);`

It is needed because C compiles top-to-bottom. If `main()` calls `calculate_bmi()` before its definition appears in the file, the compiler would not know the return type or parameter types — causing a compilation error or incorrect code generation. The prototype acts as a forward declaration, allowing definitions to appear anywhere in the file.""")

    with st.expander("Q2: What is the output of this program?\n`void add(int x) { x += 10; } int main() { int a = 5; add(a); printf(\"%d\", a); }`"):
        st.success("""**Answer:** `5`

This is **call by value**. The function `add()` receives a copy of `a` (value 5). It modifies the local copy (`x` becomes 15), but the original variable `a` in `main()` is completely unaffected. The output is `5`, not `15`.

To actually modify `a`, you would need call by reference: `void add(int *x) { *x += 10; }` called as `add(&a);`""")

    with st.expander("Q3: Trace the recursive call stack for `factorial(3)` and show every return value."):
        st.success("""**Answer:**
```
factorial(3)
  → n=3, not 0, so: return 3 * factorial(2)
       → n=2, not 0, so: return 2 * factorial(1)
            → n=1, not 0, so: return 1 * factorial(0)
                 → n=0, BASE CASE: return 1
            → 1 * 1 = 1  (factorial(1) returns 1)
       → 2 * 1 = 2  (factorial(2) returns 2)
  → 3 * 2 = 6  (factorial(3) returns 6)

Final result: 6
```""")

    with st.expander("Q4: What is variable shadowing, and why is it dangerous?"):
        st.success("""**Answer:** Shadowing occurs when a **local variable has the same name as a global variable**. Inside the local scope, the local variable "shadows" (hides) the global — any use of that name refers to the local copy, not the global.

```c
int count = 100;           /* global */
void show() {
    int count = 5;         /* local — shadows global */
    printf("%d\\n", count); /* prints 5, not 100 */
}
```
It is dangerous because it silently changes which variable is being accessed, leading to bugs that are hard to track — the global is not modified when you expect it to be, or vice versa. Always use distinct names for local and global variables.""")

    with st.expander("Q5: What happens if a recursive function has no base case? How does C handle it?"):
        st.success("""**Answer:** Without a base case, the function calls itself indefinitely. Each call pushes a new **stack frame** (local variables, return address) onto the call stack. The call stack has a fixed maximum size — once it is exhausted, the OS raises a **Stack Overflow** (Segmentation Fault on Linux/macOS, Stack Overflow exception on Windows), and the program crashes.

The key lesson: the recursive case must always move *closer* to the base case (e.g., `n - 1`, shorter string, smaller subarray) — never remain the same or grow larger.""")

if __name__ == "__main__":
    render()