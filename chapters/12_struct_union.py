import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🗂️ Module 12: Structures & Unions</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">User-Defined Data Grouping and Memory Optimization</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to declare and use `struct` and `union` types, access members with `.` and `->` operators, use `typedef struct` correctly, create arrays of structures, and explain the memory difference between struct and union.")

    st.write("")

    # --- 1. Structures ---
    st.markdown("### 1️⃣ Structures (`struct`) — Grouping Heterogeneous Data")
    st.write("""
    A **structure** is a user-defined type that groups variables of **different types** under one name.
    Each group member (field) gets its own separate memory allocation.
    Think of it as a digital lab record — one `struct` holds all attributes of one sample.
    """)

    # FIX: Filled first blank block — struct syntax anatomy
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Declaration syntax:</b>
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
struct TagName {
    data_type member1;
    data_type member2;
    ...
};                      ← semicolon after the closing brace is mandatory</pre>
        <b>Size of struct</b> = sum of all member sizes (+ possible padding bytes for alignment).<br>
        <b>Member access</b>: use the <b>dot operator</b> (<code>.</code>) for struct variables, <b>arrow operator</b> (<code>-&gt;</code>) for struct pointers.
        </div>
    ''', unsafe_allow_html=True)

    st_col1, st_col2 = st.columns(2)
    with st_col1:
        st.markdown("**Basic struct — declaration and dot operator:**")
        st.code("""struct Bacteria {
    char  strain[30];
    float ph_level;
    int   incubation_hrs;
    char  gram_stain;    /* 'P' or 'N' */
};

/* Declaring a variable of struct type */
struct Bacteria sample1;

/* Assigning members via dot operator */
sample1.ph_level       = 7.2;
sample1.incubation_hrs = 24;
sample1.gram_stain     = 'N';

/* Initialising at declaration */
struct Bacteria sample2 = {"E. coli K-12", 7.0, 18, 'N'};

printf("Strain: %s\\nGram: %c\\npH: %.1f\\n",
       sample2.strain,
       sample2.gram_stain,
       sample2.ph_level);
        """, language="c")

    with st_col2:
        st.markdown("**`typedef struct` — the standard real-world pattern:**")
        st.write("Combines struct definition with a type alias so you don't need to type `struct` every time.")
        st.code("""typedef struct {
    char  strain[30];
    float ph_level;
    int   incubation_hrs;
    char  gram_stain;
} Bacteria;              /* 'Bacteria' is now a type */

/* Use directly without 'struct' keyword */
Bacteria sample1 = {"B. subtilis", 7.1, 20, 'P'};
Bacteria sample2 = {"E. coli",     7.0, 18, 'N'};

printf("%-15s  pH %.1f  %c-stain\\n",
       sample1.strain, sample1.ph_level, sample1.gram_stain);
        """, language="c")

    st.markdown("**Arrow operator (`->`) — accessing struct members via pointer:**")
    st.code("""Bacteria *ptr = &sample1;

/* These two are equivalent: */
printf("%s\\n", sample1.strain);   /* dot — direct access */
printf("%s\\n", ptr->strain);      /* arrow — pointer access */
/* ptr->strain is shorthand for (*ptr).strain */

/* Modifying through pointer */
ptr->ph_level = 7.35;
printf("Updated pH: %.2f\\n", sample1.ph_level);  /* 7.35 */
    """, language="c")

    st.markdown("**Array of structs — a sample database:**")
    st.code("""#define MAX_SAMPLES 5

Bacteria lab_db[MAX_SAMPLES] = {
    {"E. coli K-12",    7.0, 18, 'N'},
    {"B. subtilis 168", 7.1, 20, 'P'},
    {"S. aureus MRSA",  7.2, 24, 'P'},
    {"P. aeruginosa",   6.9, 16, 'N'},
    {"L. acidophilus",  5.5, 36, 'P'}
};

/* Iterate over array of structs */
for (int i = 0; i < MAX_SAMPLES; i++) {
    printf("[%d] %-20s  pH %.1f  BSL: %d hrs\\n",
           i+1,
           lab_db[i].strain,
           lab_db[i].ph_level,
           lab_db[i].incubation_hrs);
}
    """, language="c")

    st.divider()

    # --- 2. Unions ---
    st.markdown("### 2️⃣ Unions (`union`) — Memory-Efficient Shared Storage")
    st.write("""
    A **union** looks like a struct, but all members **share the same memory location**.
    The union's size equals the size of its **largest member**. Only one member can hold a valid value at a time.
    """)

    # FIX: Filled second blank block — union memory diagram
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Memory layout of a union vs struct:</b>
        <pre style="background:#f0f4f8; padding:8px; border-radius:4px; font-size:0.9rem;">
struct Example { int i; float f; char c; }
Memory: [  i  ][  i  ][  i  ][  i  ][  f  ][  f  ][  f  ][  f  ][ c ]  = 9+ bytes

union Example  { int i; float f; char c; }
Memory: [  all three share the same 4 bytes  ]                            = 4 bytes</pre>
        Writing to one member and reading from another gives <b>undefined behaviour</b> — only the last-written member is valid.
        </div>
    ''', unsafe_allow_html=True)

    un_col1, un_col2 = st.columns(2)
    with un_col1:
        st.markdown("**Union — declaration and usage:**")
        st.code("""union SensorReading {
    int   colony_count;   /* 4 bytes */
    float absorbance;     /* 4 bytes */
    char  category;       /* 1 byte  */
};
/* Total size: 4 bytes (largest member) */

union SensorReading r;

r.absorbance = 0.732;          /* write float */
printf("OD: %.3f\\n", r.absorbance);   /* valid */

r.colony_count = 3500;         /* now write int */
/* r.absorbance is now INVALID — overwritten */
printf("CFU: %d\\n", r.colony_count);  /* valid */
        """, language="c")

    with un_col2:
        st.markdown("**Practical union — type-tagged sensor packet:**")
        st.write("A common pattern pairs a union with an enum to track which member is currently valid:")
        st.code("""typedef enum { INT_TYPE, FLOAT_TYPE, CHAR_TYPE } DataKind;

typedef struct {
    DataKind kind;          /* tag: what's stored */
    union {
        int   count;
        float concentration;
        char  flag;
    } value;
} SensorPacket;

SensorPacket pkt;
pkt.kind         = FLOAT_TYPE;
pkt.value.concentration = 2.5e-6;

if (pkt.kind == FLOAT_TYPE)
    printf("Conc: %e mol/L\\n", pkt.value.concentration);
        """, language="c")

    st.divider()

    # --- 3. Comparison Table ---
    st.subheader("📊 Structure vs Union — Comparison")

    comp_data = {
        "Feature": ["Keyword", "Memory size", "Member access", "Members valid simultaneously", "Primary use case", "Scientific example"],
        "struct": [
            "struct", "Sum of all member sizes (+ padding)", "Dot (.) or Arrow (->)", "✅ All members valid at once",
            "Storing all attributes of one entity",
            "struct Protein { char seq[500]; float mol_weight; float pI; }"
        ],
        "union": [
            "union", "Size of the LARGEST member only", "Dot (.) or Arrow (->)", "❌ Only the last-written member is valid",
            "Memory saving when data is mutually exclusive",
            "union SensorData { int count; float od; } — device sends one OR the other"
        ]
    }
    st.table(comp_data)

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Biological Databases & Embedded Lab Instruments</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Structs and unions are the natural language for biological data modelling in C:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>Array of structs as a database:</b> A <code>Protein</code> struct storing sequence, molecular weight, isoelectric point,
                and 3D coordinates can be used as an in-memory protein database — one <code>struct Protein records[10000]</code> holds
                10,000 entries, traversable with a simple for loop.</li>
                <li><b>Linked-list nodes using structs:</b> Advanced bioinformatics tools (sequence assemblers) build linked lists
                where each node is a struct containing data and a <code>struct Node *next</code> pointer — forming dynamic chains.</li>
                <li><b>Unions in bio-sensor firmware:</b> A portable glucometer or spectrophotometer may pack readings into a union —
                sending either a raw integer count or a calibrated float concentration depending on the measurement mode,
                saving RAM on microcontrollers with 8–64 KB of memory.</li>
                <li><b>typedef struct in bioinformatics C libraries:</b> htslib (the library behind samtools/bcftools) uses
                <code>typedef struct { ... } bam1_t;</code> to represent a single sequencing read — every aligned read in a BAM file
                is one <code>bam1_t</code> struct.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")

    with st.expander("Q1: What is the size of `struct S { char c; int i; float f; }` and why might it be larger than 9 bytes?"):
        st.success("""**Answer:** Theoretically `1 + 4 + 4 = 9 bytes`, but in practice it is likely **12 bytes** due to **struct padding** (alignment). The compiler inserts 3 padding bytes after `char c` so that `int i` starts at a 4-byte-aligned address (required by most CPUs for efficient access). Use `sizeof(struct S)` to check the actual size on your system. `#pragma pack(1)` or `__attribute__((packed))` can disable padding when needed (e.g., parsing binary file formats).""")

    with st.expander("Q2: What is the difference between the `.` and `->` operators for structs?"):
        st.success("""**Answer:**
- **Dot (`.`)**: used when you have a **struct variable** directly. E.g., `sample1.ph_level`
- **Arrow (`->`)**: used when you have a **pointer to a struct**. E.g., `ptr->ph_level`

`ptr->ph_level` is exactly equivalent to `(*ptr).ph_level` — the arrow dereferences the pointer and accesses the member in one step. If you use `.` on a pointer by mistake, the compiler will give a type error.""")

    with st.expander("Q3: A union has members `int i` (4 bytes), `float f` (4 bytes), `char str[20]` (20 bytes). What is its total size and why?"):
        st.success("**Answer: 20 bytes.** A union's size equals the size of its **largest member** — which is `char str[20]` at 20 bytes. All three members share the same 20-byte block. Writing to `i` modifies the first 4 bytes of that block; `f` also occupies the first 4 bytes; `str` uses all 20. Reading `f` after writing to `str` gives undefined behaviour.")

    with st.expander("Q4: Why is `typedef struct { ... } Bacteria;` preferred over `struct Bacteria { ... };` in practice?"):
        st.success("""**Answer:** With a plain `struct Bacteria { ... }`, every variable declaration requires the `struct` keyword: `struct Bacteria sample1;`. With `typedef struct { ... } Bacteria;`, you create a type alias and can write simply `Bacteria sample1;` — cleaner, shorter, and matches how you use built-in types like `int`. This is the near-universal convention in professional C code and in C libraries like htslib.""")

    with st.expander("Q5: In an array of structs `Bacteria lab[5]`, how do you print the strain of the third element?"):
        st.success("""**Answer:** `printf(\"%s\\n\", lab[2].strain);`

Array indexing starts at 0, so the third element is at index 2. The dot operator `.` accesses the `strain` member. Full example:
```c
Bacteria lab[5] = {
    {"E. coli", 7.0, 18, 'N'},
    {"B. subtilis", 7.1, 20, 'P'},
    {"S. aureus", 7.2, 24, 'P'},  /* index 2 — third */
    ...
};
printf("%s\\n", lab[2].strain);  /* S. aureus */
```""")

if __name__ == "__main__":
    render()