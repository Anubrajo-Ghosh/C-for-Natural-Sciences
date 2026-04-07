import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">📊 Module 4: Data Types in C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Primitive, Derived, User-Defined, and Type Conversion Logic</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to classify all C data types, apply type modifiers correctly, use `struct`, `union`, `typedef`, and `enum` for scientific data modelling, and explain both implicit and explicit type conversion with the promotion hierarchy.")

    st.write("")

    # --- 1. Primitive Data Types ---
    st.markdown("### 1️⃣ Primitive (Primary) Data Types")
    st.write("""
    These are the fundamental data types built directly into the C compiler. All other types 
    are built from these. They fall into four families:
    """)

    # FIX: Filled blank block — type family classification before the table
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 15px;">
            <b>The four primary type families in C:</b>
            <ul style="margin-top: 8px; color: #FFFFFF; font-size: 0.95rem;">
                <li><b>Integer types</b> — store whole numbers: <code>char</code>, <code>short</code>, <code>int</code>, <code>long</code>, <code>long long</code></li>
                <li><b>Floating-point types</b> — store decimals: <code>float</code>, <code>double</code>, <code>long double</code></li>
                <li><b>Character type</b> — <code>char</code> is technically an integer (1 byte) storing an ASCII code</li>
                <li><b>Void type</b> — <code>void</code> means "no type" — used for functions that return nothing, or generic pointers</li>
            </ul>
            Each integer type can be prefixed with <b>type modifiers</b>: <code>signed</code>, <code>unsigned</code>, <code>short</code>, <code>long</code> — see Section 2.
        </div>
    ''', unsafe_allow_html=True)

    # FIX: Expanded table — added short, long, long double, unsigned int; changed bits→bytes for consistency
    st.markdown("#### Primary Type Specifications (on a 32-bit / typical modern system)")
    primary_data = {
        "Type": [
            "char", "unsigned char",
            "short int", "unsigned short int",
            "int", "unsigned int",
            "long int", "unsigned long int",
            "long long int",
            "float", "double", "long double",
            "void"
        ],
        "Size (Bytes)": [
            "1", "1",
            "2", "2",
            "2 or 4", "2 or 4",
            "4", "4",
            "8",
            "4", "8", "12 or 16",
            "0"
        ],
        "Range (Typical)": [
            "-128 to 127", "0 to 255",
            "-32,768 to 32,767", "0 to 65,535",
            "-2,147,483,648 to 2,147,483,647", "0 to 4,294,967,295",
            "-2,147,483,648 to 2,147,483,647", "0 to 4,294,967,295",
            "-9.2E+18 to 9.2E+18",
            "3.4E-38 to 3.4E+38 (~6–7 sig. digits)", "1.7E-308 to 1.7E+308 (~15 sig. digits)", "3.4E-4932 to 3.4E+4932 (~18 sig. digits)",
            "No value"
        ],
        "Scientific Use": [
            "Nucleotide base characters (A, T, G, C)", "Pixel/byte-level image data",
            "Small counters, indices", "Port numbers, small unsigned data",
            "Colony counts, sample IDs", "Large unsigned counts",
            "File sizes, loop indices (large datasets)", "Memory addresses, large counts",
            "Genomic position indices (billions of bases)",
            "pH, temperature (moderate precision)", "OD600, enzyme kinetics (high precision)", "Ultra-precise physical constants",
            "Functions with no return value"
        ]
    }
    st.table(primary_data)

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 Important:</b> The C standard guarantees <i>minimum</i> sizes, not exact sizes. 
        Use <code>sizeof(type)</code> to check the actual size on your system. 
        Example: <code>printf("%zu bytes\\n", sizeof(int));</code>
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. Type Modifiers ---
    st.markdown("### 2️⃣ Type Modifiers")
    st.write("""
    Type modifiers change the size or sign interpretation of a base type. 
    They apply to integer types (`char`, `int`, `long`).
    """)

    mod_col1, mod_col2 = st.columns(2)
    with mod_col1:
        st.markdown("**Sign Modifiers:**")
        st.markdown("- `signed` — can hold negative and positive values (default for `int` and `char`)")
        st.markdown("- `unsigned` — can only hold 0 and positive values, but doubles the positive range")
        st.code("""signed int temp = -5;    // -2147483648 to 2147483647
unsigned int count = 0;  // 0 to 4294967295
// Use unsigned for values that cannot be negative:
unsigned int colony_count = 3500000;""", language="c")

    with mod_col2:
        st.markdown("**Size Modifiers:**")
        st.markdown("- `short` — reduces size (typically 2 bytes) to save memory")
        st.markdown("- `long` — increases size (typically 4–8 bytes) for large values")
        st.markdown("- `long long` — guarantees at least 8 bytes (C99+)")
        st.code("""short int day_number = 180;
long int genome_size = 3200000000L; // 3.2 billion (human genome bp)
long long int reads_processed = 9000000000LL;""", language="c")

    st.divider()

    # --- 3. User-Defined Data Types ---
    st.markdown("### 3️⃣ User-Defined Data Types")
    st.write("""
    C allows programmers to define their own composite types. This is critical in Natural Sciences 
    for grouping related experimental data — e.g., a single `Microbe` record containing its name, 
    pH optimum, and risk level.
    """)

    udt_col1, udt_col2 = st.columns(2)
    with udt_col1:
        st.markdown("**`struct` — Structure**")
        st.write("Groups variables of *different* types under one name. Each member gets its **own** memory block.")
        st.code("""struct Microbe {
    char  name[30];
    float ph_optimum;
    int   biosafety_level;
    char  gram_stain;  // 'P' or 'N'
};

// Declaring and using a struct variable
struct Microbe sample;
sample.ph_optimum = 7.2;
sample.biosafety_level = 1;""", language="c")

        # FIX: Added typedef+struct combined pattern (the most common real-world usage)
        st.markdown("**`typedef struct` — Combined Pattern (most common)**")
        st.code("""typedef struct {
    char  name[30];
    float ph_optimum;
    int   biosafety_level;
} Microbe;

// Now use 'Microbe' directly — no 'struct' keyword needed
Microbe sample1;
sample1.ph_optimum = 6.8;""", language="c")

    with udt_col2:
        st.markdown("**`union` — Union**")
        st.write("Like a `struct`, but all members **share the same memory location**. Size = size of the largest member. Only one member can hold a value at a time.")
        st.code("""union SampleReading {
    int    colony_count;   // 4 bytes
    float  absorbance;     // 4 bytes
    char   category;       // 1 byte
};
// ALL share the same 4 bytes of memory

union SampleReading r;
r.absorbance = 0.732;  // Only this is valid now
// r.colony_count would give garbage""", language="c")

        st.markdown('''
            <div style="background-color: #00599C; padding: 10px 14px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 8px; font-size: 0.9rem;">
            <b>struct vs union:</b><br>
            <code>struct</code> → each member has its own memory → use when you need ALL fields simultaneously<br>
            <code>union</code> → all members share one memory block → use when you need only ONE field at a time (saves RAM)
            </div>
        ''', unsafe_allow_html=True)

        st.markdown("**`typedef` — Type Alias**")
        st.write("Creates a shorter, readable alias for any existing type.")
        st.code("""typedef unsigned long int ulong;
typedef float           pH_t;  // custom type for pH values

ulong bacterial_count = 1000000UL;
pH_t  sample_ph       = 7.35;""", language="c")

    st.divider()

    # --- 4. Enumerated Data Type ---
    st.markdown("### 4️⃣ Enumerated Data Type (`enum`)")
    st.write("""
    An `enum` is a user-defined type consisting of named integer constants. 
    It replaces "magic numbers" with meaningful words, making scientific classification logic 
    self-documenting and less error-prone.
    """)

    st.code("""enum BiosafeyLevel { BSL1, BSL2, BSL3, BSL4 };
// Internally: BSL1=0, BSL2=1, BSL3=2, BSL4=3

// You can also assign custom starting values:
enum GramStain { GRAM_POSITIVE = 1, GRAM_NEGATIVE = 2, GRAM_VARIABLE = 3 };

enum BiosafeyLevel lab_clearance = BSL2;

if (lab_clearance >= BSL3) {
    printf("Full PPE required.\\n");
} else {
    printf("Standard precautions.\\n");
}
    """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>📌 Why enum over #define for constants?</b> <code>enum</code> groups related constants logically under one type name,
        making intent clear. The compiler can also warn if you miss an enum value in a <code>switch</code> statement — 
        <code>#define</code> constants have no such grouping or type checking.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 5. Type Casting (Conversion) ---
    st.markdown("### 5️⃣ Type Casting: Conversion Logic")
    st.write("""
    Type casting is the process of converting a value from one data type to another. 
    This is critical when mixing types in calculations — incorrect casting causes data loss or wrong results.
    """)

    # FIX: Added the promotion hierarchy — key exam concept that was missing
    st.markdown("**The Implicit Promotion Hierarchy (lower → higher, automatic):**")
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding: 10px 16px; margin-bottom: 12px; font-family: monospace; font-size: 0.95rem; background-color: #00599C; border-radius: 6px;">
        char → short → int → unsigned int → long → unsigned long → long long → float → double → long double
        </div>
    ''', unsafe_allow_html=True)
    st.write("When two different types meet in an expression, the smaller type is automatically promoted to the larger. This is called **widening**.")

    cast_col1, cast_col2 = st.columns(2)
    with cast_col1:
        st.markdown("**A. Implicit Conversion (Automatic Promotion)**")
        st.write("Performed automatically by the compiler — smaller type is widened to the larger type. No data loss when widening.")
        st.code("""char base_code = 65;   // 'A' in ASCII
int  gene_pos  = base_code;  // char → int, now 65

int   reads = 1500;
float ratio = reads;  // int → float, now 1500.0

// Mixed expression — int promoted to double:
double result = reads * 2.718;
// 'reads' (int) is promoted to double before multiply""", language="c")

    with cast_col2:
        st.markdown("**B. Explicit Conversion (Manual Cast)**")
        st.write("Performed by the programmer using the cast operator `(type)`. Required to avoid integer truncation in division.")
        st.code("""int total_colonies = 155;
int petri_dishes   = 4;
float average;

/* Without cast — integer division, truncates decimal */
average = total_colonies / petri_dishes;
// Result: 38 (WRONG — lost .75)

/* With explicit cast — correct float division */
average = (float) total_colonies / petri_dishes;
// Result: 38.75 (CORRECT)

/* Narrowing — double to int, decimal part LOST */
double od_reading = 0.732;
int    rounded    = (int) od_reading;  // becomes 0""", language="c")

    st.divider()

    # --- 6. Declaration & Initialization ---
    st.markdown("### 6️⃣ Declaration vs. Initialization")
    st.write("In C, memory must be explicitly reserved (declared) before a value can be stored in it.")

    st.code("""/* Declaration only — memory is reserved but contains garbage */
int temperature;

/* Assignment — stores a value into already-declared memory */
temperature = 37;

/* Initialization — declaration + assignment in one line (preferred) */
float ph        = 7.4;
double od_blank = 0.000;

/* Multiple declarations in one line (same type) */
int row, col, depth;

/* IMPORTANT: Uninitialized local variables contain garbage values in C.
   Always initialize before use to avoid undefined behaviour. */
    """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 Bytes vs Bits reminder:</b> Use <code>sizeof()</code> which returns size in <b>bytes</b>. 
        1 byte = 8 bits. So <code>sizeof(int)</code> returns 4 on most modern systems, meaning <code>int</code> occupies 32 bits.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Research Context: Data Integrity in Scientific Computing</h4>
            <p style="color: #333; font-size: 0.95rem;">
                In <b>AI-driven Natural Sciences</b>, choosing the wrong data type is not a minor inconvenience — it directly corrupts results:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li>Using <code>int</code> to store a pH value (e.g., 6.8) truncates it to 6 — a full unit off, which in enzyme kinetics 
                means the difference between a functional and denatured protein.</li>
                <li><code>float</code> gives only ~6–7 significant digits. For spectrophotometry (OD600 readings like 0.00372), 
                use <code>double</code> to preserve precision.</li>
                <li><code>long long int</code> is essential for genomics — the human genome has ~3.2 billion base pairs. 
                A plain <code>int</code> overflows at ~2.1 billion, silently wrapping to a negative number.</li>
                <li><code>struct</code> is the natural way to represent a biological sample — group <code>strain_name</code>, 
                <code>od600</code>, <code>incubation_temp</code>, and <code>biosafety_level</code> into one cohesive record.</li>
                <li><code>enum</code> for Gram stain result (<code>GRAM_POS</code>, <code>GRAM_NEG</code>, <code>GRAM_VAR</code>) 
                prevents a logic bug where <code>0</code> and <code>1</code> are easy to confuse — named constants are self-documenting.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: Why would you use `unsigned int` instead of `int` for a bacterial colony count variable?"):
        st.success("**Answer:** Colony counts can never be negative. `unsigned int` discards the sign bit and uses it to extend the positive range — from ~2.1 billion (signed) to ~4.29 billion (unsigned). This both prevents logically impossible negative values and doubles the usable range for counting applications.")

    with st.expander("Q2: What is the key difference between `struct` and `union`? When would you choose `union`?"):
        st.success("**Answer:** In a `struct`, every member has its own separate memory — total size = sum of all members. In a `union`, all members share the same memory block — total size = size of the largest member. Choose `union` when a variable can hold one of several types but never more than one at a time (e.g., a sensor reading that is either an integer count OR a float absorbance), saving memory in resource-constrained environments like embedded lab instruments.")

    with st.expander("Q3: What is the output of this code? `int a = 7; int b = 2; float result = a / b;`"):
        st.success("""**Answer:** `result = 3.0` — NOT `3.5`. 

Even though `result` is `float`, the division `a / b` is evaluated first as **integer division** (both operands are `int`), producing `3`. That integer `3` is then promoted to `float` giving `3.0`. 

To get `3.5`, you must cast: `result = (float) a / b;`""")

    with st.expander("Q4: State the implicit type promotion hierarchy from lowest to highest."):
        st.success("**Answer:** `char → short → int → unsigned int → long → unsigned long → long long → float → double → long double`. When two different types meet in an expression, the lower type is automatically promoted to the higher before the operation is performed.")

    with st.expander("Q5: Why is `long long int` necessary for storing human genome base-pair positions?"):
        st.success("**Answer:** The human genome contains approximately **3.2 billion** base pairs. The maximum value of a signed `int` on a 32-bit system is ~2.147 billion — storing a position beyond this causes **integer overflow**, silently wrapping to a negative number and producing a completely wrong index. `long long int` guarantees at least 8 bytes, supporting values up to ~9.2 × 10¹⁸ — more than enough for any genomic coordinate.")

if __name__ == "__main__":
    render()