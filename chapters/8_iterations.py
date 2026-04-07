import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🔄 Module 8: Iterative Statements</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Looping Logic: for, while, do-while, and Loop Control</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to write all three loop types with correct syntax, choose the appropriate loop for a given problem, trace `break` and `continue` execution, write nested loops for 2D data, and identify infinite loop conditions.")

    st.write("")

    # --- 1. while Loop ---
    st.markdown("### 1️⃣ The `while` Loop — Entry-Controlled")
    st.write("""
    The `while` loop checks its condition **before** each iteration. If the condition is false on the very 
    first check, the body never executes (minimum 0 executions). Use when the number of iterations is unknown.
    """)
    st.markdown("**Syntax:** `while (condition) { body; }`")

    wh_col1, wh_col2 = st.columns(2)
    with wh_col1:
        st.markdown("**Generic example:**")
        st.code("""int count = 1;
while (count <= 5) {
    printf("Iteration: %d\\n", count);
    count++;         /* CRITICAL: must update condition var */
}
/* Output: Iteration: 1  2  3  4  5 */

/* If count++ is forgotten → INFINITE LOOP */
        """, language="c")

    with wh_col2:
        st.markdown("**Scientific use — OD600 monitoring:**")
        st.code("""float od600 = 0.05;        /* inoculation OD */
float target = 0.8;        /* harvest OD */

while (od600 < target) {
    printf("OD600: %.3f — still growing\\n", od600);
    od600 += 0.05;         /* simulate hourly reading */
}
printf("Target OD reached: %.3f\\n", od600);
/* Runs unknown number of times — ideal while use case */
        """, language="c")

    st.divider()

    # --- 2. for Loop ---
    st.markdown("### 2️⃣ The `for` Loop — Entry-Controlled")
    st.write("""
    The `for` loop consolidates initialization, condition, and update into one line, making it 
    the preferred choice when the number of iterations is known in advance.
    """)
    st.markdown("**Syntax:** `for (initialisation; condition; update) { body; }`")
    # FIX: Filled blank block — for loop anatomy before the code
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
            Initialisation: Runs ONCE at the very start</pre>
            <p>Condition: Checked BEFORE each iteration; loop stops when false</p>
            <p>Update: Runs after EACH iteration (i++, i--, i+=2 etc.)</p>
        <b>Execution order:</b> initialisation → [check condition → body → update] → [check → body → update] → ... → condition false → exit
        </div>
    ''', unsafe_allow_html=True)

    for_col1, for_col2 = st.columns(2)
    with for_col1:
        st.markdown("**Standard forward loop:**")
        st.code("""/* Process 10 sequence readings */
for (int i = 0; i < 10; i++) {
    printf("Processing read %d\\n", i + 1);
}

/* Countdown — decrementing loop */
for (int i = 5; i >= 1; i--) {
    printf("T-%d seconds\\n", i);
}

/* Step of 2 */
for (int i = 0; i <= 100; i += 2) {
    printf("%d ", i);   /* even numbers: 0 2 4 ... 100 */
}
        """, language="c")

    with for_col2:
        st.markdown("**Scientific use — mean OD calculation:**")
        st.code("""float od_readings[] = {0.21, 0.45, 0.73, 0.89, 0.94};
int   n = 5;
float sum = 0.0;

for (int i = 0; i < n; i++) {
    sum += od_readings[i];
    printf("Reading %d: %.2f\\n", i + 1, od_readings[i]);
}

float mean_od = sum / n;
printf("Mean OD600: %.3f\\n", mean_od);
/* Output: Mean OD600: 0.644 */
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>📌 Flexible for loop:</b> Any or all three parts can be omitted. <code>for(;;)</code> with all three empty
        creates an infinite loop (must use <code>break</code> to exit). Multiple initialisations and updates
        can be separated by the comma operator: <code>for (i=0, j=10; i &lt; j; i++, j--)</code>.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 3. do-while Loop ---
    st.markdown("### 3️⃣ The `do-while` Loop — Exit-Controlled")
    st.write("""
    The `do-while` loop checks its condition **after** the body executes. This guarantees the 
    body runs **at least once** — regardless of whether the condition is initially true or false.
    """)
    st.markdown("**Syntax:** `do { body; } while (condition);` ← note the semicolon after `)`")

    dw_col1, dw_col2 = st.columns(2)
    with dw_col1:
        st.markdown("**Menu-driven input validation:**")
        st.code("""int choice;
do {
    printf("\\n=== Lab Menu ===\\n");
    printf("1. Run OD measurement\\n");
    printf("2. Log pH reading\\n");
    printf("3. Exit\\n");
    printf("Enter choice: ");
    scanf("%d", &choice);

    if (choice < 1 || choice > 3)
        printf("Invalid choice. Try again.\\n");

} while (choice != 3);
printf("Session ended.\\n");
/* Menu ALWAYS shows at least once */
        """, language="c")

    with dw_col2:
        st.markdown("**Input validation — never accept invalid data:**")
        st.code("""float ph;
do {
    printf("Enter pH (0.0 - 14.0): ");
    scanf("%f", &ph);

    if (ph < 0.0 || ph > 14.0)
        printf("Invalid pH — outside 0-14 range.\\n");

} while (ph < 0.0 || ph > 14.0);

printf("pH recorded: %.2f\\n", ph);
/* Loop keeps asking until valid pH is entered */
        """, language="c")

    st.divider()

    # --- 4. Nested Loops ---
    st.markdown("### 4️⃣ Nested Loops — Processing 2D Data")
    st.write("A loop inside another loop. The inner loop completes **all** its iterations for each single iteration of the outer loop. Essential for matrices, grids, and multi-well plate data.")

    nest_col1, nest_col2 = st.columns(2)
    with nest_col1:
        st.markdown("**Basic nested loop — multiplication table:**")
        st.code("""for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        printf("%d ", i * j);
    }
    printf("\\n");
}
/* Output:
   1 2 3
   2 4 6
   3 6 9  */
        """, language="c")

    with nest_col2:
        st.markdown("**Scientific use — 96-well plate processing:**")
        st.code("""/* 8 rows (A-H) × 12 columns = 96 wells */
float plate[8][12];

for (int row = 0; row < 8; row++) {
    for (int col = 0; col < 12; col++) {
        /* Process each well */
        printf("Well %c%d: %.3f\\n",
               'A' + row,
               col + 1,
               plate[row][col]);
    }
}
/* Inner loop (12 cols) runs 8 × 12 = 96 times total */
        """, language="c")

    st.divider()

    # --- 5. break, continue, goto ---
    st.markdown("### 5️⃣ Loop Control: `break`, `continue`, and `goto`")

    ctrl_col1, ctrl_col2 = st.columns(2)
    with ctrl_col1:
        st.markdown("**`break` — Exit the loop immediately:**")
        st.write("Jumps to the first statement after the loop. In nested loops, only exits the innermost loop.")
        st.code("""/* Stop scanning when contaminated sample found */
for (int i = 1; i <= 10; i++) {
    if (contamination[i] > threshold) {
        printf("Contamination at sample %d!\\n", i);
        break;     /* stop processing further samples */
    }
    printf("Sample %d: OK\\n", i);
}
printf("Scan complete.\\n");
/* 'Scan complete.' prints whether or not break fired */
        """, language="c")

        st.markdown("**`goto` — Jump to a label (use rarely):**")
        st.code("""/* Legitimate use: break out of nested loops */
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        if (plate[i][j] < 0) {
            printf("Negative value detected!\\n");
            goto error_exit;   /* exits BOTH loops */
        }
    }
}
error_exit:
    printf("Stopping plate analysis.\\n");
        """, language="c")

    with ctrl_col2:
        st.markdown("**`continue` — Skip to next iteration:**")
        st.write("Skips the rest of the current iteration's body and jumps to the update step.")
        st.code("""/* Skip invalid (negative) OD readings */
float readings[] = {0.21, -1.0, 0.73, -0.5, 0.89};
int n = 5;
float sum = 0.0;
int   valid = 0;

for (int i = 0; i < n; i++) {
    if (readings[i] < 0) {
        printf("Skipping invalid reading %d\\n", i);
        continue;    /* skip this iteration */
    }
    sum += readings[i];
    valid++;
}
printf("Mean of valid readings: %.3f\\n", sum / valid);
/* Output: Mean of valid readings: 0.610 */
        """, language="c")

        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem; margin-top: 6px;">
            <b>break vs continue:</b><br>
            <code>break</code> → exits the loop entirely<br>
            <code>continue</code> → skips the rest of this iteration, loop continues<br>
            Both only affect the <b>innermost</b> enclosing loop.
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 6. Comparative Table ---
    st.subheader("📊 Choosing the Right Loop")

    loop_data = {
        "Loop Type": ["while", "for", "do-while"],
        "Syntax": [
            "while (cond) { body; }",
            "for (init; cond; update) { body; }",
            "do { body; } while (cond);"
        ],
        "Condition Check": ["Entry (before body)", "Entry (before body)", "Exit (after body)"],
        "Minimum Executions": ["0", "0", "1 (always)"],
        "Best Use Case": [
            "Unknown iterations (e.g., read until EOF, wait for threshold)",
            "Known/fixed iterations (e.g., process n samples, iterate array)",
            "Must run at least once (e.g., menus, input validation)"
        ]
    }
    st.table(loop_data)

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Loops in Scientific Computing</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Loops are the engine of quantitative biology:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>for loop</b> iterates over arrays of hourly incubator temperature readings, absorbance values, or
                genome positions — any fixed-size dataset. The mean, max, min, and standard deviation are all computed this way.</li>
                <li><b>while loop</b> drives AI optimisation algorithms like Gradient Descent — the loop continues
                reducing the error rate until it drops below a convergence threshold, with the number of iterations unknown in advance.</li>
                <li><b>do-while</b> implements lab instrument menus and input validation — the prompt must always show
                at least once before the user's input can be validated.</li>
                <li><b>Nested for loops</b> process 2D data: 96-well plate absorbance matrices, genomic alignment
                score matrices (Smith-Waterman), or pixel intensity grids from microscopy images.</li>
                <li><b>continue</b> is used to skip corrupted sensor readings or invalid data points mid-array
                without stopping the entire analysis pipeline.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is the output of this loop?\n`for (int i = 1; i <= 5; i++) { if (i == 3) continue; printf(\"%d \", i); }`"):
        st.success("""**Answer:** `1 2 4 5`

When `i == 3`, `continue` skips the `printf` for that iteration and jumps to the update (`i++`). All other values (1, 2, 4, 5) print normally.""")

    with st.expander("Q2: What is the minimum number of times a `do-while` loop executes, and why?"):
        st.success("**Answer:** **At least 1 time.** The `do-while` loop checks its condition *after* the body executes. Even if the condition is false from the very beginning, the body runs once before the check — unlike `while` and `for`, which check before any execution.")

    with st.expander("Q3: A student writes `while (1) { ... }` with no break. What happens and how do you fix it?"):
        st.success("""**Answer:** `1` is always non-zero (true in C), so this is an **infinite loop** — it runs forever, freezing the program.

Fix options:
1. Add a `break` inside the loop body when an exit condition is met: `if (done) break;`
2. Replace with a proper condition: `while (od600 < target) { ... }`
3. For intentional indefinite loops (like embedded systems), `while(1)` with `break` is actually the standard pattern.""")

    with st.expander("Q4: How many total times does the inner loop body execute?\n`for (int i=0; i<4; i++) { for (int j=0; j<3; j++) { printf(\"*\"); } }`"):
        st.success("**Answer:** **12 times.** The outer loop runs 4 times (i = 0, 1, 2, 3). For each outer iteration, the inner loop runs 3 times (j = 0, 1, 2). Total = 4 × 3 = 12 executions. This is the general rule: nested loop body executes `outer_count × inner_count` times.")

    with st.expander("Q5: What is the difference between `break` in a loop vs `break` in a switch?"):
        st.success("""**Answer:** Functionally identical — `break` exits the **nearest enclosing** `switch`, `for`, `while`, or `do-while` block. 

The important distinction is context:
- In a **loop**, `break` terminates the loop and continues after it.
- In a **switch**, `break` exits the switch block; without it, execution falls through to the next case.
- In a **nested loop inside a switch** (or vice versa), `break` only exits the *innermost* enclosing construct — not both.""")

if __name__ == "__main__":
    render()