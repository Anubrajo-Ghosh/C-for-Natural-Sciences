import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">💾 Module 11: Storage Classes in C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Scope, Visibility, Lifetime, and Memory Location of Variables</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to describe all four storage classes by their four properties, explain the behaviour of `static` across function calls, demonstrate `extern` across files, and identify when each class is appropriate in a scientific program.")

    st.write("")

    # --- 1. The Four Pillars ---
    st.markdown("### 1️⃣ The Four Properties of a Variable")
    st.write("""
    In C, every variable has four properties determined by its **storage class**. 
    Understanding these is essential for writing correct, efficient scientific programs — especially
    in multi-function simulations where state persistence and memory layout matter.
    """)

    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <ol style="color:#FFFFFF; font-size:0.95rem; margin-top:6px;">
            <li><b>Storage Location:</b> Where the variable lives — Stack (RAM), CPU Register, or Data Segment (RAM).</li>
            <li><b>Default Value:</b> What it contains if you don't initialise it — <b>Garbage</b> (undefined) or <b>Zero</b>.</li>
            <li><b>Scope:</b> Which parts of the code can see and use the variable — block-local, file-wide, or program-wide.</li>
            <li><b>Lifetime:</b> How long the variable persists in memory — until block exits, or until program ends.</li>
        </ol>
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. Comparison Table ---
    st.markdown("### 2️⃣ The Four Storage Classes — Overview")

    storage_data = {
        "Storage Class": ["auto", "register", "static (local)", "static (global)", "extern"],
        "Storage Location": ["Stack (RAM)", "CPU Register (hint only)", "Data Segment (RAM)", "Data Segment (RAM)", "Data Segment (RAM)"],
        "Default Value": ["Garbage", "Garbage", "Zero", "Zero", "Zero"],
        "Scope": ["Local to block", "Local to block", "Local to block", "Entire file", "All files (program-wide)"],
        "Lifetime": ["Until block exits", "Until block exits", "Entire program run", "Entire program run", "Entire program run"]
    }
    st.table(storage_data)

    st.divider()

    # --- 3. Detailed Breakdown ---
    st.markdown("### 3️⃣ Each Storage Class in Detail")

    sc_col1, sc_col2 = st.columns(2)

    with sc_col1:
        st.markdown("**A. `auto` — Automatic (Default)**")
        st.write("Every local variable is `auto` by default. The keyword is never written in practice — it is implicit. Created on the stack when the block is entered, destroyed when it exits.")
        st.code("""void analyse(float od) {
    auto int count = 0;   /* same as: int count = 0; */
    count++;
    printf("Count: %d, OD: %.2f\\n", count, od);
}
/* count is destroyed every time analyse() returns
   Next call starts fresh at 0 */
        """, language="c")

        st.markdown("**B. `register` — Register Hint (Legacy)**")
        st.write("Asks the compiler to store the variable in a CPU register for fastest possible access. The compiler may **ignore** this hint.")
        st.code("""register int i;
for (i = 0; i < 1000000; i++) {
    /* tight loop — register hint may speed this up */
    process(data[i]);
}
        """, language="c")
        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #FFFFFFF; font-size: 0.88rem; margin-top: 5px;">
            <b>⚠️ Modern status:</b> <code>register</code> was <b>deprecated in C11</b> and its meaning removed in C17.
            Modern compilers (GCC, Clang) perform register allocation automatically and far more effectively than manual hints.
            You cannot take the address (<code>&amp;</code>) of a register variable.
            </div>
        ''', unsafe_allow_html=True)

    with sc_col2:
        st.markdown("**C. `static` — Persistent Local Variable**")
        st.write("A `static` local variable is **initialised only once** and retains its value between function calls — it does not reset. Stored in the data segment, not the stack.")
        st.code("""void count_calls(void) {
    static int call_count = 0;   /* initialised once */
    call_count++;
    printf("Function called %d time(s)\\n", call_count);
}

int main() {
    count_calls();   /* Function called 1 time(s) */
    count_calls();   /* Function called 2 time(s) */
    count_calls();   /* Function called 3 time(s) */
    return 0;
}
/* call_count persists — NOT reset between calls */
        """, language="c")

        st.markdown("**`static` at File Scope — Internal Linkage**")
        st.write("When applied to a global variable or function, `static` restricts visibility to the current file only — useful for hiding implementation details.")
        st.code("""/* In analysis.c — hidden from other files */
static float calibration_factor = 1.042;

/* Only functions in analysis.c can see this */
static void internal_helper(void) { ... }
        """, language="c")

        st.markdown("**D. `extern` — External Linkage Across Files**")
        st.write("Declares that a variable is **defined in another source file**. It does not create the variable — it just tells the compiler it exists elsewhere.")
        st.code("""/* === main.c === */
#include <stdio.h>
extern int experiment_id;    /* defined in config.c */
extern float sensitivity;    /* defined in config.c */

int main() {
    printf("Experiment #%d\\n", experiment_id);
    printf("Sensitivity: %.4f\\n", sensitivity);
    return 0;
}

/* === config.c === */
int   experiment_id = 42;    /* actual definition */
float sensitivity   = 0.001; /* actual definition */
        """, language="c")

    st.divider()

    # --- 4. Practical Comparison ---
    st.markdown("### 4️⃣ auto vs static — Side-by-Side Trace")
    st.write("The most commonly tested distinction: what happens when you call the same function multiple times.")

    trace_col1, trace_col2 = st.columns(2)
    with trace_col1:
        st.markdown("**auto (resets each call):**")
        st.code("""void auto_demo(void) {
    int x = 0;   /* auto — reset every call */
    x++;
    printf("x = %d\\n", x);
}
auto_demo();   /* x = 1 */
auto_demo();   /* x = 1 */
auto_demo();   /* x = 1 */
        """, language="c")

    with trace_col2:
        st.markdown("**static (persists across calls):**")
        st.code("""void static_demo(void) {
    static int x = 0;   /* init once, persists */
    x++;
    printf("x = %d\\n", x);
}
static_demo();   /* x = 1 */
static_demo();   /* x = 2 */
static_demo();   /* x = 3 */
        """, language="c")

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 15px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Memory Management in Scientific Simulation</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Storage classes directly control simulation state and performance:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>static local</b> variables track simulation state across iterations without global variables —
                e.g., a <code>static double total_biomass = 0;</code> inside a growth-step function accumulates biomass
                across every time-step call without needing a global.</li>
                <li><b>static global</b> variables hide calibration constants (e.g., instrument sensitivity factors)
                inside a single .c file, preventing other modules from accidentally modifying them — a form of encapsulation in C.</li>
                <li><b>extern</b> allows a multi-file bioinformatics pipeline to share configuration (genome build version,
                threshold values, run IDs) across analysis.c, io.c, and report.c without passing everything as function arguments.</li>
                <li><b>register</b> — though deprecated — appears in legacy bioinformatics code (BLAST, older SAMtools versions)
                and must be recognised when reading existing codebases.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.warning("⚠️ **Note on Persistence:** Storage classes keep data alive only while the *program runs*. Once the program exits, all memory is released. To persist data permanently between program runs, you must use **File Handling (Module 13)**.")

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")

    with st.expander("Q1: What are the four properties defined by a storage class?"):
        st.success("**Answer:** (1) **Storage Location** — where in memory (Stack, Register, Data Segment). (2) **Default Value** — garbage (auto, register) or zero (static, extern). (3) **Scope** — which code can access it (block-local or file/program-wide). (4) **Lifetime** — how long it persists (until block exits, or until program ends).")

    with st.expander("Q2: What is the output of calling `static_counter()` three times, where it contains `static int n = 0; n++; printf(\"%d\", n);`?"):
        st.success("**Answer:** `1`, then `2`, then `3`. The `static int n = 0` initialises `n` to 0 only once — the very first time the function runs. On every subsequent call, `n` retains its previous value instead of resetting. This is the key behaviour that distinguishes `static` from `auto`.")

    with st.expander("Q3: Why was `register` deprecated in C11 and effectively removed in C17?"):
        st.success("**Answer:** Modern compilers (GCC, Clang) perform **register allocation automatically** using sophisticated algorithms that analyse the entire function's data flow. Manual `register` hints are almost always inferior to the compiler's decisions and can actually prevent optimisations. The keyword was deprecated because it served no useful purpose and the restriction it imposed (no `&` operator allowed) was a pointless constraint.")

    with st.expander("Q4: What is the difference between `static` applied to a *local* variable vs. a *global* variable/function?"):
        st.success("""**Answer:**
- `static` on a **local variable**: Changes its *lifetime* — from "until block exits" to "entire program run". The variable persists between function calls. Scope remains local to the block.
- `static` on a **global variable or function**: Changes its *linkage* — from "visible to all files" (external linkage) to "visible only within this file" (internal linkage). Lifetime is already program-wide for globals. This is used to hide implementation details from other source files.""")

    with st.expander("Q5: A `config.c` file defines `int run_id = 7;`. How do you access `run_id` from `main.c` without passing it as a function argument?"):
        st.success("""**Answer:** Add `extern int run_id;` at the top of `main.c` (or in a shared header file included by both). This tells the compiler that `run_id` is an `int` defined in another translation unit. The linker resolves the reference at link time, connecting `main.c`'s reference to `config.c`'s definition.

Important: `extern` is a *declaration*, not a *definition*. The actual memory is allocated only in `config.c` where it is defined without `extern`.""")

if __name__ == "__main__":
    render()