import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">➕ Module 5: Operators & Expressions</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Logic, Arithmetic, and the Hierarchy of Operations</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to classify all C operator types, apply pre/post increment correctly, trace operator precedence in a complex expression, use bitwise operators on binary data, and write ternary and `sizeof` expressions correctly.")

    st.write("")

    # --- 1. Classification of Operators ---
    st.markdown("### 1️⃣ Classification of Operators")
    st.write("C provides a rich set of operators categorised by the number of operands they act on: **Unary** (1 operand), **Binary** (2 operands), **Ternary** (3 operands).")

    st.markdown('''<div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">''', unsafe_allow_html=True)

    op_col1, op_col2 = st.columns(2)

    with op_col1:
        st.markdown("**A. Arithmetic Operators (Binary)**")
        # FIX: Replaced &lt;= HTML entity with the actual character in st.write()
        st.markdown("Perform mathematical calculations on numeric operands.")
        st.code("""int a = 17, b = 5;
a + b   // 22  — Addition
a - b   // 12  — Subtraction
a * b   // 85  — Multiplication
a / b   // 3   — Integer division (truncates)
a % b   // 2   — Modulus (remainder)
        """, language="c")
        st.markdown("⚠️ `%` (modulus) only works on **integers**. For float remainder use `fmod()` from `<math.h>`.")

        st.markdown("**B. Relational Operators (Binary)**")
        st.markdown("Compare two values — always return 1 (true) or 0 (false).")
        st.code("""float ph = 6.8;
ph > 7.0    // 0 — false (acidic, not alkaline)
ph < 7.0    // 1 — true
ph >= 6.8   // 1 — true
ph <= 6.0   // 0 — false
ph == 7.0   // 0 — false
ph != 7.0   // 1 — true
        """, language="c")

        st.markdown("**C. Assignment Operators**")
        st.markdown("Store a value into a variable. Compound forms combine arithmetic with assignment.")
        st.code("""int count = 0;      // simple assignment
count += 10;        // count = count + 10 → 10
count -= 3;         // count = count - 3  → 7
count *= 2;         // count = count * 2  → 14
count /= 4;         // count = count / 4  → 3
count %= 2;         // count = count % 2  → 1
        """, language="c")

    with op_col2:
        st.markdown("**D. Logical Operators (Binary / Unary)**")
        st.markdown("Combine boolean conditions — return 1 (true) or 0 (false).")
        st.code("""int temp_ok  = (temp < 37.5);   // 1 if temp is safe
int ph_ok    = (ph > 6.5);      // 1 if pH is acceptable

/* && (AND) — true only if BOTH are true */
if (temp_ok && ph_ok)
    printf("Culture conditions optimal.\\n");

/* || (OR) — true if AT LEAST ONE is true */
if (!temp_ok || !ph_ok)
    printf("Alarm: check conditions.\\n");

/* ! (NOT) — inverts the boolean value */
int is_sterile = 1;
if (!is_sterile) printf("Contamination risk!\\n");
        """, language="c")

        st.markdown("**E. Bitwise Operators**")
        st.markdown("Operate directly on the **binary bits** of integer values. Essential for reading raw instrument data.")
        st.code("""unsigned char flags = 0b00001010; // binary: 00001010

/* & (AND) — mask specific bits */
flags & 0x0F    // 00001010 & 00001111 = 00001010

/* | (OR) — set specific bits */
flags | 0x01    // 00001010 | 00000001 = 00001011

/* ^ (XOR) — toggle specific bits */
flags ^ 0xFF    // 00001010 ^ 11111111 = 11110101

/* ~ (NOT) — invert all bits */
~flags          // ~00001010 = 11110101

/* << (left shift) — multiply by power of 2 */
flags << 1      // 00001010 → 00010100 (×2)

/* >> (right shift) — divide by power of 2 */
flags >> 1      // 00001010 → 00000101 (÷2)
        """, language="c")

    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # --- 2. Unary Operators: Increment & Decrement ---
    st.markdown("### 2️⃣ Increment & Decrement Operators (Unary)")
    st.write("`++` and `--` are unary operators that add or subtract 1. The critical distinction is **where** you place them.")

    inc_col1, inc_col2 = st.columns(2)
    with inc_col1:
        st.markdown("**Pre-increment / Pre-decrement**")
        st.write("Operator is applied **before** the value is used in the expression.")
        st.code("""int i = 5;
int x = ++i;  // i becomes 6 FIRST, then x = 6
// i = 6, x = 6

int j = 5;
int y = --j;  // j becomes 4 FIRST, then y = 4
// j = 4, y = 4
        """, language="c")

    with inc_col2:
        st.markdown("**Post-increment / Post-decrement**")
        st.write("The current value is used **first**, then the operator is applied.")
        st.code("""int i = 5;
int x = i++;  // x = 5 FIRST, then i becomes 6
// i = 6, x = 5

int j = 5;
int y = j--;  // y = 5 FIRST, then j becomes 4
// j = 4, y = 5
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 Mnemonic:</b> <b>Pre</b>-increment = <b>Pre</b>pare first (change, then use).
        <b>Post</b>-increment = <b>Post</b>pone the change (use, then change).
        In a standalone statement like <code>i++;</code> vs <code>++i;</code>, the result is identical — the difference only matters inside a larger expression.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 3. Special Operators ---
    st.markdown("### 3️⃣ Special Operators")

    sp_col1, sp_col2 = st.columns(2)
    with sp_col1:
        st.markdown("**A. Ternary Operator (`?:`)**")
        st.write("The only C operator with **three operands**. A compact shorthand for a simple if-else.")
        st.markdown("Syntax: `condition ? value_if_true : value_if_false`")
        st.code("""float ph = 6.2;

/* Ternary: classify as acidic or neutral/alkaline */
char *label = (ph < 7.0) ? "Acidic" : "Neutral/Alkaline";
printf("Sample is: %s\\n", label);

/* Equivalent if-else — ternary is more concise */
int result = (marks > 40) ? 1 : 0;  // 1=Pass, 0=Fail
        """, language="c")

    with sp_col2:
        st.markdown("**B. `sizeof` Operator**")
        st.write("Returns the size of a type or variable in **bytes** at compile time. Unary, not a function call.")
        # FIX: Changed single quotes to double quotes in printf — was syntactically invalid C
        st.code("""#include <stdio.h>

printf("Size of char:        %zu bytes\\n", sizeof(char));
printf("Size of int:         %zu bytes\\n", sizeof(int));
printf("Size of float:       %zu bytes\\n", sizeof(float));
printf("Size of double:      %zu bytes\\n", sizeof(double));
printf("Size of long long:   %zu bytes\\n", sizeof(long long));

/* Also works on variables and structs */
struct Microbe sample;
printf("Size of Microbe struct: %zu bytes\\n", sizeof(sample));
        """, language="c")
        st.markdown("⚠️ Use format specifier `%zu` (not `%d`) for `sizeof` — its return type is `size_t` (unsigned).")

    st.markdown("**C. Comma Operator (`,`)**")
    st.write("Evaluates multiple expressions left-to-right; the value of the whole expression is the **rightmost** value. Most commonly seen in `for` loop headers.")
    st.code("""/* Comma operator in for loop — two variables updated per iteration */
for (int i = 0, j = 10; i < j; i++, j--) {
    printf("i=%d  j=%d\\n", i, j);
}

/* As an expression: */
int x = (5, 10, 20);  // x = 20 (rightmost value)
    """, language="c")

    st.divider()

    # --- 4. Precedence & Associativity ---
    st.markdown("### 4️⃣ Precedence & Associativity")
    st.write("""
    When an expression contains multiple operators, **Precedence** determines which is evaluated first (higher priority = evaluated sooner).
    When two operators share the same precedence level, **Associativity** breaks the tie (Left-to-Right or Right-to-Left).
    """)

    # FIX: Filled blank block — mnemonic before the table
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Memory Aid — PURMA:</b><br>
        <b>P</b>arentheses/Postfix → <b>U</b>nary → <b>R</b>elational/Multiplicative → <b>M</b>ultiplication before Addition → <b>A</b>ssignment last<br><br>
        A fuller mnemonic for the key levels: <i>"Please Unpack My Aunt's Remarkably Equal Logical Assignment"</i><br>
        <b>P</b>ostfix · <b>U</b>nary · <b>M</b>ultiplicative · <b>A</b>dditive · <b>R</b>elational · <b>E</b>quality · <b>L</b>ogical (AND→OR) · <b>A</b>ssignment
        </div>
    ''', unsafe_allow_html=True)

    # FIX: Expanded from 5 rows to the full standard C precedence table (15 levels)
    prec_data = {
        "Level": [
            "1 (Highest)", "2", "3", "4", "5",
            "6", "7", "8", "9", "10",
            "11", "12", "13", "14", "15 (Lowest)"
        ],
        "Category": [
            "Postfix / Primary",
            "Prefix Unary",
            "Multiplicative",
            "Additive",
            "Bitwise Shift",
            "Relational",
            "Equality",
            "Bitwise AND",
            "Bitwise XOR",
            "Bitwise OR",
            "Logical AND",
            "Logical OR",
            "Conditional (Ternary)",
            "Assignment",
            "Comma"
        ],
        "Operators": [
            "()  []  ->  .  (postfix ++ --)",
            "(prefix ++ --)  +  -  !  ~  (type)  *  &  sizeof",
            "*  /  %",
            "+  -",
            "<<  >>",
            "<  <=  >  >=",
            "==  !=",
            "&",
            "^",
            "|",
            "&&",
            "||",
            "?  :",
            "=  +=  -=  *=  /=  %=  &=  |=  ^=  <<=  >>=",
            ","
        ],
        "Associativity": [
            "Left → Right",
            "Right → Left",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Left → Right",
            "Right → Left",
            "Right → Left",
            "Left → Right"
        ]
    }
    st.table(prec_data)

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>📌 Key fact:</b> Relational operators (<code>&lt; &lt;= &gt; &gt;=</code>) have <b>higher</b> precedence than equality operators (<code>== !=</code>),
        which in turn are <b>higher</b> than all bitwise operators, which are <b>higher</b> than logical operators.
        Assignment is always evaluated <b>last</b> (except comma).
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 5. Expressions & Evaluation ---
    st.markdown("### 5️⃣ Expressions & Evaluation")
    st.write("An **expression** is any valid combination of operators, constants, and variables that produces a value. C evaluates expressions by applying precedence and associativity rules.")

    ex_col1, ex_col2 = st.columns(2)
    with ex_col1:
        st.markdown("**Physics Formula (precedence demo)**")
        st.write("Final velocity: *v = u + at*")
        st.code("""float u = 0.0, a = 9.8, t = 10.0;
float v = u + a * t;
/*  Step 1: a * t = 9.8 * 10.0 = 98.0  (higher precedence)
    Step 2: u + 98.0 = 0.0 + 98.0 = 98.0
    Result: v = 98.0 m/s  */
        """, language="c")

    with ex_col2:
        st.markdown("**Biology Formula (precedence + cast)**")
        st.write("Dilution factor calculation for serial dilution:")
        st.code("""int stock_vol = 1, total_vol = 10;
int steps = 3;
double dilution_factor;

/* Without cast — integer division gives 0 */
dilution_factor = stock_vol / total_vol;  // 0 (WRONG)

/* With cast and precedence */
dilution_factor = (double) stock_vol / total_vol;
// = 0.1 per step
double final_df = dilution_factor / steps;
// = 0.0333... (1:30 dilution)
        """, language="c")

    st.info("**💡 Golden Rule:** When in doubt, use parentheses `()` to make evaluation order explicit. `(a + b) * c` is unambiguous; `a + b * c` relies on the reader knowing that `*` has higher precedence than `+`.")

    st.divider()

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Application: Operators in Lab Automation & Bioinformatics</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Operators are the fundamental decision-making and calculation tools in any scientific program:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Logical operators</b> (<code>&amp;&amp;</code>, <code>||</code>) drive automated lab alerts:
                <code>(temperature &gt; 37.5 &amp;&amp; ph_level &lt; 6.5) || oxygen_low == 1</code>
                — triggers an alarm if temperature AND pH are simultaneously out of range, OR if oxygen is low.</li>
                <li><b>Bitwise operators</b> are essential in bioinformatics for compact DNA encoding.
                A common trick stores two nucleotides per byte using 2-bit encoding:
                A=00, T=01, G=10, C=11. Extracting the second base uses <code>(byte &gt;&gt; 2) &amp; 0x03</code>.</li>
                <li><b>Modulus operator</b> (<code>%</code>) is used in reading frame analysis — 
                <code>position % 3 == 0</code> checks if a nucleotide position is the start of a new codon.</li>
                <li><b>sizeof</b> is critical when calling <code>malloc()</code> for dynamic data structures — 
                always write <code>malloc(n * sizeof(double))</code>, never hardcode byte counts.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is the output of this code?\n`int i = 5; int x = i++; int y = ++i;`"):
        st.success("""**Answer:**
- `i = 5` initially
- `x = i++` → x gets the current value of i (**x = 5**), then i increments → **i = 6**
- `y = ++i` → i increments first → **i = 7**, then y gets that value → **y = 7**

**Final values: i = 7, x = 5, y = 7**""")

    with st.expander("Q2: Evaluate `4 + 8 / 2 - 1 * 3`. Show all steps with precedence."):
        st.success("""**Answer — applying precedence (/ and * before + and -):**
1. `8 / 2 = 4` (division first, left-to-right)
2. `1 * 3 = 3` (multiplication next)
3. `4 + 4 - 3` → `8 - 3` → **= 5**

The expression evaluates to **5**, not 7 (which would be the incorrect left-to-right result).""")

    with st.expander("Q3: What is wrong with this C statement? `printf('pH value: %f', ph);`"):
        st.success("**Answer:** The string argument uses **single quotes** (`'...'`), which in C denotes a *character constant*, not a string. A string literal must use **double quotes**: `printf(\"pH value: %f\", ph);`. This is a syntax error — the compiler will reject it.")

    with st.expander("Q4: In C, what does `flags & 0x0F` do, and when would a biologist use it?"):
        st.success("""**Answer:** `&` is the **bitwise AND**. `flags & 0x0F` masks the upper 4 bits to zero and keeps only the lower 4 bits (nibble). 

In bioinformatics, this technique extracts encoded fields from compact binary data. For example, in the BAM/SAM format used for genome alignment files, each read's FLAG field is a 16-bit integer where each bit encodes metadata (paired-end, reverse strand, unmapped, etc.). To check if bit 4 is set (read is reverse complement): `if (flag & 0x10) { ... }`""")

    with st.expander("Q5: What is the precedence order of these operators from highest to lowest? `==`, `&&`, `>`, `||`, `+`"):
        st.success("""**Answer (highest to lowest):**
1. `+` (Additive — Level 4)
2. `>` (Relational — Level 6)
3. `==` (Equality — Level 7)
4. `&&` (Logical AND — Level 11)
5. `||` (Logical OR — Level 12)

So `a + b > c == d && e || f` is parsed as `(((a + b) > c) == d) && e) || f`.""")

if __name__ == "__main__":
    render()