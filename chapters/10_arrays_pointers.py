import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🎯 Module 10: Arrays & Pointers</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Memory Addresses, Contiguous Data Structures, and Dynamic Memory</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to declare and use 1D and 2D arrays, explain pointer declaration and dereferencing, describe the array-pointer relationship, perform pointer arithmetic, and use `malloc`/`free` for dynamic memory allocation.")

    st.write("")

    # --- 1. Arrays ---
    st.markdown("### 1️⃣ Arrays: Fixed-Size Sequences")
    st.write("""
    An array is a collection of variables of the **same data type** stored in **contiguous** (consecutive)
    memory locations. All elements share one name, accessed by index. The size is fixed at compile time.
    """)

    # FIX: Filled blank block — array syntax anatomy
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Declaration syntax:</b> <code>data_type array_name[size];</code><br>
        <b>Initialisation syntax:</b> <code>data_type array_name[size] = {val0, val1, ..., valN-1};</code><br><br>
        Key rules:
        <ul style="margin-top:6px; font-size:0.93rem; color:#FFFFFF;">
            <li>Index always starts at <b>0</b>; last element is at index <b>N-1</b></li>
            <li>C does <b>not</b> check bounds — accessing index N or beyond is undefined behaviour (silent data corruption or crash)</li>
            <li>If fewer initialisers than elements are given, the rest are zero-initialised</li>
        </ul>
        </div>
    ''', unsafe_allow_html=True)

    arr_col1, arr_col2 = st.columns(2)
    with arr_col1:
        st.markdown("**1D Array — basic operations:**")
        st.code("""/* Declaration + initialisation */
float od_readings[5] = {0.21, 0.45, 0.73, 0.89, 0.94};

/* Accessing by index */
printf("First:  %.2f\\n", od_readings[0]);   // 0.21
printf("Last:   %.2f\\n", od_readings[4]);   // 0.94

/* Modifying an element */
od_readings[2] = 0.80;

/* Iterating with a for loop */
float sum = 0;
for (int i = 0; i < 5; i++)
    sum += od_readings[i];

printf("Mean OD: %.3f\\n", sum / 5);         // 0.626
        """, language="c")

    with arr_col2:
        st.markdown("**2D Array — matrix (rows × columns):**")
        st.code("""/* 3 plates × 4 time-point readings */
float plate[3][4] = {
    {0.10, 0.25, 0.52, 0.80},   /* Plate 0 */
    {0.12, 0.30, 0.61, 0.95},   /* Plate 1 */
    {0.08, 0.19, 0.44, 0.72}    /* Plate 2 */
};

/* Access: plate[row][column] */
printf("Plate 1, Time 3: %.2f\\n", plate[1][2]); // 0.61

/* Nested loop to process all readings */
for (int r = 0; r < 3; r++) {
    for (int c = 0; c < 4; c++) {
        printf("%.2f  ", plate[r][c]);
    }
    printf("\\n");
}
        """, language="c")

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C; margin-top: 5px;">
        <b>📌 Memory layout of a 2D array:</b> C stores 2D arrays in <b>row-major order</b> —
        all elements of row 0 are stored first, then row 1, etc., in one contiguous block.
        <code>plate[1][2]</code> is physically at offset <code>(1×4 + 2) = 6</code> from the start.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 2. Pointers ---
    st.markdown("### 2️⃣ Pointers: The Power of Addresses")
    st.write("""
    A pointer is a variable that stores the **memory address** of another variable — not the data value itself,
    but the location where the data lives in RAM. Pointers are the foundation of dynamic memory, call-by-reference, and array processing in C.
    """)

    # FIX: Filled second blank block — pointer syntax anatomy
    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>Declaration syntax:</b> <code>data_type *pointer_name;</code><br>
        The <code>*</code> in the declaration means "this is a pointer to a <code>data_type</code>".<br><br>
        <b>Two key operators:</b>
        <ul style="margin-top:6px; font-size:0.93rem; color:#FFFFFF;">
            <li><code>&amp;variable</code> — <b>Address-of</b>: returns the memory address of <code>variable</code></li>
            <li><code>*pointer</code> — <b>Dereference</b>: returns the value stored at the address held in <code>pointer</code></li>
        </ul>
        </div>
    ''', unsafe_allow_html=True)

    ptr_col1, ptr_col2 = st.columns(2)
    with ptr_col1:
        st.markdown("**Pointer declaration, assignment, dereferencing:**")
        st.code("""int od_int = 73;         /* regular variable */
int *ptr  = &od_int;    /* ptr holds address of od_int */

printf("Value:   %d\\n",  od_int);  /* 73        */
printf("Address: %p\\n",  ptr);     /* 0x7fff... (varies) */
printf("Via ptr: %d\\n", *ptr);     /* 73        */

/* Modifying original via pointer */
*ptr = 89;
printf("New value: %d\\n", od_int); /* 89 — original changed! */
        """, language="c")

    with ptr_col2:
        # FIX: Changed printf('%d', *ptr) single quotes → double quotes
        st.markdown("**Pointer to a float — scientific example:**")
        st.code("""float ph = 7.35;
float *ph_ptr = &ph;

printf("pH value:   %.2f\\n", ph);          /* 7.35 */
printf("pH address: %p\\n",   ph_ptr);       /* address */
printf("Via ptr:    %.2f\\n", *ph_ptr);      /* 7.35 */

/* Sensor update: write through pointer */
*ph_ptr = 6.80;
printf("Updated pH: %.2f\\n", ph);           /* 6.80 */
        """, language="c")

    st.divider()

    # --- 3. Array-Pointer Relationship ---
    st.markdown("### 3️⃣ The Array–Pointer Relationship")
    st.write("""
    In C, the **name of an array is a constant pointer to its first element**.
    `arr` is equivalent to `&arr[0]`. This is why passing an array to a function passes the address,
    not a copy — and why arrays are efficient even when large.
    """)

    ap_col1, ap_col2 = st.columns(2)
    with ap_col1:
        st.markdown("**Array name as pointer:**")
        st.code("""int temps[4] = {37, 38, 39, 40};
int *p = temps;          /* p points to temps[0] */

printf("%d\\n", *p);      /* 37 — same as temps[0]   */
printf("%d\\n", *(p+1));  /* 38 — same as temps[1]   */
printf("%d\\n", *(p+2));  /* 39 — same as temps[2]   */

/* Index notation and pointer notation are equivalent */
printf("%d\\n", temps[3]);   /* 40 */
printf("%d\\n", *(temps+3)); /* 40 — identical result */
        """, language="c")

    with ap_col2:
        st.markdown("**Pointer arithmetic — traversing a sequence:**")
        st.code("""char dna[] = "ATGCGA";
char *ptr = dna;         /* points to 'A' */

while (*ptr != '\\0') {
    printf("%c ", *ptr); /* print each base */
    ptr++;               /* advance to next byte */
}
/* Output: A T G C G A */

/* Pointer difference = number of elements between */
char *start = dna;
char *end   = dna + 6;   /* points past last char */
printf("Length: %ld\\n", end - start);  /* 6 */
        """, language="c")

    st.divider()

    # --- 4. Dynamic Memory ---
    st.markdown("### 4️⃣ Dynamic Memory Allocation (`malloc`, `calloc`, `free`)")
    st.write("""
    Arrays have a fixed size declared at compile time. When the size is unknown until runtime
    (e.g., reading a FASTQ file of unknown length), use **dynamic memory allocation** from `<stdlib.h>`.
    """)

    dyn_col1, dyn_col2 = st.columns(2)
    with dyn_col1:
        st.markdown("**`malloc` — allocate uninitialised memory:**")
        st.code("""#include <stdlib.h>

int n = 1000;   /* could come from file header */

/* Allocate array of n floats at runtime */
float *readings = malloc(n * sizeof(float));

if (readings == NULL) {
    printf("Memory allocation failed!\\n");
    return 1;
}

/* Use like a normal array */
for (int i = 0; i < n; i++)
    readings[i] = i * 0.01f;

printf("Reading 500: %.2f\\n", readings[500]);

/* ALWAYS free when done — prevents memory leak */
free(readings);
readings = NULL;   /* good practice: avoid dangling ptr */
        """, language="c")

    with dyn_col2:
        st.markdown("**`calloc` — allocate zero-initialised memory:**")
        st.code("""/* calloc(count, element_size) — zeros all bytes */
int rows = 96, cols = 12;

float **plate = malloc(rows * sizeof(float *));
for (int i = 0; i < rows; i++)
    plate[i] = calloc(cols, sizeof(float));
    /* each row is zeroed — safe to read before writing */

plate[0][0] = 0.732;   /* set individual well value */

/* Free 2D array — must free each row, then array */
for (int i = 0; i < rows; i++)
    free(plate[i]);
free(plate);
        """, language="c")

        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #00599C; font-size: 0.88rem; margin-top: 6px;">
            <b>malloc vs calloc:</b><br>
            <code>malloc(n * size)</code> → uninitialized (contains garbage)<br>
            <code>calloc(n, size)</code> → zero-initialized (safer for numeric data)<br>
            Both return <code>NULL</code> on failure — always check!
            </div>
        ''', unsafe_allow_html=True)

    st.divider()

    # --- 5. Performance Summary ---
    st.subheader("📊 Arrays vs Dynamic Memory — When to Use Which")
    st.table({
        "Feature": ["Size known at compile time?", "Memory location", "Initialisation", "Bounds checking", "Can be resized?", "Must be freed?"],
        "Static Array": ["✅ Yes (required)", "Stack (fast)", "Optional (garbage if not)", "❌ None — programmer's job", "❌ No", "❌ No (automatic)"],
        "Dynamic (malloc/calloc)": ["❌ No — set at runtime", "Heap (slightly slower)", "malloc=garbage / calloc=zero", "❌ None — programmer's job", "✅ Yes (realloc)", "✅ Yes — always call free()"]
    })

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 10px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Bioinformatics & Genomics</h4>
            <p style="color: #333; font-size: 0.95rem;">
                Arrays and pointers are the twin engines of bioinformatics data processing:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>DNA as a char array:</b> A genome is stored as a character array of 'A', 'T', 'G', 'C'. Pointer arithmetic enables
                high-speed "sliding window" scans — moving a pointer across 3 billion bases to find motifs (e.g., the TATA box promoter).</li>
                <li><b>Dynamic allocation for FASTQ files:</b> When reading a sequencing file, the number of reads is unknown until parsing begins.
                <code>malloc()</code> is called once the header count is read, allocating exactly the needed memory.</li>
                <li><b>2D arrays for alignment matrices:</b> The Smith-Waterman and Needleman-Wunsch local/global sequence alignment
                algorithms use a 2D scoring matrix — naturally represented as a 2D C array.</li>
                <li><b>Hardware registers:</b> Microcontroller firmware for lab instruments (PCR machines, spectrophotometers) uses pointers
                to directly read/write hardware memory-mapped I/O registers — impossible without pointer support.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")
    st.write("Test your understanding before moving to the next module.")

    with st.expander("Q1: What is the index of the last element in `int arr[8]`? What happens if you access `arr[8]`?"):
        st.success("""**Answer:** The last valid index is **7** (indices 0–7). Accessing `arr[8]` is **out-of-bounds** — C performs no bounds checking, so it reads whatever value happens to be in the adjacent memory. This is **undefined behaviour**: it may print garbage, corrupt other variables, or cause a segmentation fault. Never rely on this behaviour.""")

    with st.expander("Q2: What is the difference between `int *p` and `*p = 5`?"):
        st.success("""**Answer:**
- `int *p` — **declaration**: `*` here means "p is a pointer to int". This creates the pointer variable.
- `*p = 5` — **dereferencing assignment**: `*` here means "go to the address stored in p and write 5 there". This modifies the value at the pointed-to location.

The `*` symbol has two different meanings depending on context: pointer declaration vs. dereference operation.""")

    with st.expander("Q3: If `int arr[] = {10, 20, 30}` and `int *p = arr`, what does `*(p+2)` evaluate to?"):
        st.success("""**Answer:** `30`. 

`p` points to `arr[0]` (value 10). `p+2` moves the pointer forward by 2 integer-sized steps (2 × 4 bytes = 8 bytes on a 32-bit int system), landing on `arr[2]`. Dereferencing with `*` gives the value at that location: **30**.

This is **pointer arithmetic** — adding an integer to a pointer advances it by that many elements, not bytes.""")

    with st.expander("Q4: What is the critical rule when using `malloc()`, and what happens if you break it?"):
        st.success("""**Answer:** Every `malloc()` call must be paired with exactly one `free()` call when the memory is no longer needed.

If you forget `free()`: the memory remains allocated for the program's lifetime — a **memory leak**. In long-running bioinformatics pipelines processing thousands of files, leaks accumulate until the OS runs out of RAM and kills the process.

Always also check the return value: if `malloc()` returns `NULL`, allocation failed (out of memory). Using a NULL pointer without checking causes an immediate crash.""")

    with st.expander("Q5: What is the memory layout difference between a 1D array `int a[3]` and a 2D array `int b[2][3]`?"):
        st.success("""**Answer:** Both are stored as a **single contiguous block** in RAM — the 2D layout is an abstraction. 

`int a[3]` → 3 consecutive integers: `[a0][a1][a2]`

`int b[2][3]` → 6 consecutive integers in **row-major order**: `[b00][b01][b02][b10][b11][b12]`

`b[1][2]` is at offset `(1×3 + 2) = 5` from the start — same as `*(b[0] + 5)`. This is why 2D arrays passed to functions can be treated as 1D pointers with manual index arithmetic.""")

if __name__ == "__main__":
    render()