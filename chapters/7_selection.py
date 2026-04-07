import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🧠 Module 7: Decision Making Statements</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Conditional Branching: if, if-else, switch, and Jump Statements</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to write all forms of `if-else` including nested and ladder variants, use `switch-case` with correct `break` and fall-through behaviour, apply the ternary operator, and explain when `goto` is and isn't appropriate.")

    st.write("")

    # --- 1. The if-else Family ---
    st.markdown("### 1️⃣ The `if-else` Family")
    st.write("The `if` statement evaluates a condition — if it is true (non-zero), the block executes. It scales from simple single-branch to multi-way ladders.")

    if_col1, if_col2 = st.columns(2)
    with if_col1:
        st.markdown("**Simple `if` — Single Branch**")
        st.write("Executes the block only if the condition is true. If false, skips it entirely.")
        st.code("""float od600 = 0.85;

if (od600 > 1.0) {
    printf("Culture in stationary phase.\\n");
}
/* If od600 <= 1.0, nothing is printed */
        """, language="c")

        st.markdown("**`if-else` — Two-Way Decision**")
        st.write("Covers both the true AND false case — exactly one block always executes.")
        st.code("""float ph = 6.2;

if (ph < 7.0) {
    printf("Sample is Acidic.\\n");
} else {
    printf("Sample is Neutral or Alkaline.\\n");
}
/* Output: Sample is Acidic. */
        """, language="c")

    with if_col2:
        st.markdown("**`if-else-if` Ladder — Multi-Way Decision**")
        st.write("Tests conditions sequentially — the first true branch executes, the rest are skipped.")
        st.code("""float concentration = 0.35;

if (concentration > 0.5) {
    printf("High Toxicity Level\\n");
} else if (concentration > 0.2) {
    printf("Moderate Toxicity Level\\n");
} else if (concentration > 0.05) {
    printf("Low Toxicity Level\\n");
} else {
    printf("Safe — Below Detection Limit\\n");
}
/* Output: Moderate Toxicity Level */
        """, language="c")

        st.markdown("**Nested `if` — Multi-Criterion Decision**")
        st.write("An `if` inside another `if` — used when a condition only makes sense after a prior one passes.")
        st.code("""float temp = 36.5, ph = 7.1;

if (temp >= 35.0 && temp <= 38.0) {
    /* Inner check — only reached if temp is valid */
    if (ph >= 6.8 && ph <= 7.4) {
        printf("Optimal culture conditions.\\n");
    } else {
        printf("Temp OK, but pH is off.\\n");
    }
} else {
    printf("Temperature out of range.\\n");
}
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 Dangling else problem:</b> In a nested <code>if</code> without braces, an <code>else</code> always pairs with
        the <b>nearest preceding</b> unpaired <code>if</code>. Always use curly braces <code>{ }</code> even for single-statement
        blocks to avoid ambiguous nesting bugs.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. Switch-Case ---
    st.markdown("### 2️⃣ The `switch-case` Statement")
    st.write("""
    `switch` tests a single expression against a list of constant values (cases). 
    It is cleaner and faster than an `if-else` ladder when checking one variable against many fixed values.
    """)

    # FIX: Filled blank block — switch syntax anatomy before the columns
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Syntax anatomy of switch:</b>
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
switch (expression) {
    case constant1:
        // statements
        break;       ← exits switch; without this, falls into next case
    case constant2:
        // statements
        break;
    default:         ← optional; runs if no case matches
        // statements
}</pre>
        <b>Critical restrictions:</b> The switch expression must be an <b>integer type</b> (<code>int</code>, <code>char</code>, <code>enum</code>).
        <code>float</code>, <code>double</code>, and <code>string</code> are <b>NOT allowed</b> — use <code>if-else</code> for those.
        </div>
    ''', unsafe_allow_html=True)

    sw_col1, sw_col2 = st.columns(2)
    with sw_col1:
        st.markdown("**Normal switch — with `break`:**")
        st.code("""int sample_id = 102;

switch (sample_id) {
    case 101:
        printf("Strain: E. coli\\n");
        break;
    case 102:
        printf("Strain: B. subtilis\\n");
        break;
    case 103:
        printf("Strain: S. aureus\\n");
        break;
    default:
        printf("Unknown Sample ID\\n");
}
/* Output: Strain: B. subtilis */
        """, language="c")

    with sw_col2:
        st.markdown("**Intentional fall-through — without `break`:**")
        st.write("Omitting `break` causes execution to continue into the next case. Occasionally useful for grouping.")
        st.code("""char base = 'A';

switch (base) {
    case 'A':
    case 'G':
        printf("Purine base\\n");
        break;       /* both A and G reach here */
    case 'T':
    case 'C':
        printf("Pyrimidine base\\n");
        break;
    default:
        printf("Invalid nucleotide\\n");
}
/* Output: Purine base */
        """, language="c")
        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem;">
            <b>Fall-through</b> here is intentional — A and G share the same action (both purines).
            Always add a comment <code>/* fall-through */</code> when omitting <code>break</code> on purpose,
            so future readers know it's deliberate.
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 3. Ternary Operator ---
    st.markdown("### 3️⃣ The Ternary / Conditional Operator (`?:`)")
    st.write("The ternary operator provides a compact single-expression alternative to `if-else`. It is the only C operator with three operands.")
    st.markdown("**Syntax:** `condition ? value_if_true : value_if_false`")

    tern_col1, tern_col2 = st.columns(2)
    with tern_col1:
        st.markdown("**Basic ternary:**")
        st.code("""float ph = 6.2;
char *status = (ph < 7.0) ? "Acidic" : "Neutral/Alkaline";
printf("Status: %s\\n", status);
/* Output: Status: Acidic */

/* Equivalent if-else — ternary is more concise */
int result = (od600 > 0.8) ? 1 : 0;
        """, language="c")

    with tern_col2:
        st.markdown("**Chained ternary (use sparingly):**")
        st.write("Ternary operators can be nested, but deep chains reduce readability — prefer `if-else-if` beyond 2 levels.")
        st.code("""float conc = 0.35;
char *level = (conc > 0.5) ? "High"   :
              (conc > 0.2) ? "Moderate":
                             "Safe";
printf("Toxicity: %s\\n", level);
/* Output: Toxicity: Moderate */
        """, language="c")

    st.divider()

    # --- 4. goto Statement ---
    st.markdown("### 4️⃣ The `goto` Statement")
    st.write("""
    `goto` transfers control unconditionally to a labelled statement elsewhere in the same function. 
    It is part of the C standard but considered poor practice in most situations.
    """)

    goto_col1, goto_col2 = st.columns(2)
    with goto_col1:
        st.markdown("**Syntax & Example:**")
        st.code("""int i = 1;

start:                          /* label */
    if (i > 5) goto end;        /* jump forward */
    printf("i = %d\\n", i);
    i++;
    goto start;                 /* jump back — acts like a loop */

end:
    printf("Done.\\n");
        """, language="c")

    with goto_col2:
        st.markdown("**When is `goto` acceptable?**")
        st.markdown("""
- ✅ **Error handling in C** — breaking out of deeply nested loops (where `break` only exits one level)
- ✅ **Resource cleanup** — jumping to a single cleanup block at the end of a function
- ❌ **General control flow** — `goto` skips variable initialisations and makes code hard to trace
- ❌ **Replacing loops** — always use `for`, `while`, or `do-while` instead
        """)
        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem; margin-top: 6px;">
            <b>📌 Exam note:</b> <code>goto</code> can only jump within the <b>same function</b>.
            It cannot transfer control between functions. The label and <code>goto</code> must be in the same scope.
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 5. Comparative Analysis ---
    st.markdown("### 5️⃣ Comparative Analysis")

    comp_data = {
        "Feature": ["Condition type", "Data types supported", "Speed (many cases)", "Range checks (x > 5)", "Readability (many cases)", "Fall-through behaviour"],
        "if-else": ["Any expression", "Any (float, string, pointer)", "Slower — sequential evaluation", "✅ Yes", "Lower — verbose for many branches", "Not applicable"],
        "switch-case": ["Equality only (==)", "int, char, enum ONLY", "Faster — uses jump tables", "❌ No", "Higher — structured and scannable", "Yes — without break, falls to next case"]
    }
    st.table(comp_data)

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Branching in Biological AI</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Decision-making statements are the "logic gates" of any scientific algorithm:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>if-else ladder</b> is used in genomic classifiers to branch based on GC content ranges —
                &lt;40% (AT-rich), 40–60% (balanced), &gt;60% (GC-rich) — each triggering different downstream analysis.</li>
                <li><b>switch on nucleotide char</b> (`A`, `T`, `G`, `C`) is more efficient than four <code>if</code> checks
                when parsing raw FASTA sequence data character by character in a high-throughput pipeline.</li>
                <li><b>Nested if</b> implements multi-criterion biosafety checks — a sample must pass temperature range AND
                pH range AND sterility flag before being cleared for downstream AI processing.</li>
                <li><b>goto</b> is used legitimately in C bioinformatics tools (like samtools source code)
                for error-cleanup jumps — jumping to a <code>cleanup:</code> label that frees allocated memory before returning.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is the 'dangling else' problem and how do you avoid it?"):
        st.success("""**Answer:** When `if` statements are nested without braces, an `else` is paired with the **nearest preceding unmatched `if`** — not necessarily the one the programmer intended. 

Example: `if (a) if (b) X; else Y;` — the `else` pairs with `if (b)`, not `if (a)`.

**Fix:** Always use curly braces `{ }` for every branch, even single-statement ones: `if (a) { if (b) { X; } else { Y; } }`""")

    with st.expander("Q2: Why can't you use `switch` to check if a pH value (float) falls in a range?"):
        st.success("""**Answer:** Two reasons:
1. `switch` only accepts **integer types** (`int`, `char`, `enum`) — `float` and `double` are not allowed as the switch expression (compiler error).
2. Even if you could, `switch` only checks **exact equality** (`case 6.8:`) — it cannot evaluate range conditions like `ph > 6.5 && ph < 7.5`.

Use an `if-else-if` ladder for float ranges.""")

    with st.expander("Q3: What is the output of this switch block?\n`int x = 2; switch(x) { case 1: printf(\"A\"); case 2: printf(\"B\"); case 3: printf(\"C\"); break; default: printf(\"D\"); }`"):
        st.success("""**Answer:** `BC`

Execution enters at `case 2` (matches x=2), prints `B`. There is **no `break`**, so it **falls through** to `case 3`, prints `C`. The `break` in `case 3` then exits the switch. `case 1` and `default` are never reached.

This demonstrates why every `case` needs a `break` unless fall-through is intentional.""")

    with st.expander("Q4: Rewrite this if-else as a ternary: `if (temp > 37) risk = 1; else risk = 0;`"):
        st.success("""**Answer:** `int risk = (temp > 37) ? 1 : 0;`

Or even more concisely: `int risk = (temp > 37);` — since a relational expression already evaluates to 1 (true) or 0 (false) in C.""")

    with st.expander("Q5: In what scenario is `goto` considered acceptable in professional C code?"):
        st.success("""**Answer:** The most widely accepted use of `goto` in C is for **error handling and resource cleanup** in functions that allocate multiple resources (memory, file handles, sockets). Instead of repeating cleanup code in every error branch, all error paths `goto cleanup:` at the end of the function, which frees all resources in one place. The Linux kernel and many C bioinformatics tools (e.g., htslib, samtools) use this pattern explicitly.""")

if __name__ == "__main__":
    render()