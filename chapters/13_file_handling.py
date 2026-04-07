import streamlit as st

def render():
    # --- Blue Theme Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">📁 Module 13: File Handling in C</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Persistent Data Storage: Reading, Writing, and Navigating Files</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    st.info("💡 **Learning Objective:** By the end of this module, you should be able to open and close files safely with NULL checks, write formatted data using `fprintf`, read data using `fgets` and `fscanf`, use all major file modes, and navigate files with `fseek`, `ftell`, and `rewind`.")

    st.write("")

    st.markdown("""
    In Microbiology, experiments generate datasets far larger than can be stored in RAM — and RAM itself is 
    volatile (lost when power is cut). **File Handling** allows C programs to permanently save results 
    as `.txt`, `.csv`, `.dat`, or `.fasta` files on disk, and to reload them in future program runs.
    """)

    st.divider()

    # --- 1. The FILE Pointer ---
    st.markdown("### 1️⃣ The `FILE` Pointer and `fopen()` / `fclose()`")
    st.write("C does not access files directly. Every file operation goes through a `FILE *` pointer — a handle to the file stream managed by the OS.")

    st.markdown('''
        <div style="border-left: 3px solid #00599C; padding-left: 15px; margin-bottom: 12px;">
        <b>The file operation sequence — always follow this order:</b>
        <ol style="margin-top:6px; font-size:0.93rem; color:#FFFFFF;">
            <li><b>Declare</b> a <code>FILE *</code> pointer</li>
            <li><b>Open</b> the file with <code>fopen(filename, mode)</code> — returns <code>NULL</code> on failure</li>
            <li><b>Check</b> for <code>NULL</code> before any read/write — skipping this causes a crash on missing files</li>
            <li><b>Read or Write</b> using <code>fprintf</code>, <code>fscanf</code>, <code>fgets</code>, etc.</li>
            <li><b>Close</b> with <code>fclose()</code> — flushes the buffer and saves changes to disk</li>
        </ol>
        </div>
    ''', unsafe_allow_html=True)

    st.code("""FILE *fptr;                         /* Step 1: declare */
fptr = fopen("data.csv", "w");     /* Step 2: open     */

if (fptr == NULL) {                /* Step 3: ALWAYS CHECK */
    printf("Error: File could not be opened!\\n");
    return 1;                      /* exit — do not proceed */
}

fprintf(fptr, "Hello, file!\\n");  /* Step 4: write    */
fclose(fptr);                      /* Step 5: close    */
    """, language="c")

    st.divider()

    # --- 2. File Access Modes ---
    st.markdown("### 2️⃣ File Access Modes")
    st.write("The second argument to `fopen()` controls how the file is opened. Choosing the wrong mode can silently destroy data.")

    # FIX: Expanded modes table — added r+, w+, a+, rb, wb, ab
    modes_data = {
        "Mode": ["\"r\"", "\"w\"", "\"a\"", "\"r+\"", "\"w+\"", "\"a+\"", "\"rb\" / \"wb\"", "\"ab\""],
        "Action": [
            "Read only",
            "Write (creates new; OVERWRITES existing)",
            "Append (adds to end; creates if missing)",
            "Read + Write (file must exist)",
            "Read + Write (creates new; OVERWRITES existing)",
            "Read + Append (creates if missing)",
            "Binary Read / Write",
            "Binary Append"
        ],
        "fptr == NULL if...": [
            "File not found", "Cannot create file", "Cannot create/open file",
            "File not found", "Cannot create file", "Cannot create/open file",
            "File not found / cannot create", "Cannot create/open file"
        ],
        "Scientific Use Case": [
            "Loading a FASTA sequence file",
            "Creating a fresh experiment log (overwrites old)",
            "Adding today's OD600 readings to a running log",
            "Correcting a record in an existing results file",
            "Creating a temporary analysis scratch file",
            "Appending new reads while also being able to re-read header",
            "Serialising struct data / reading binary sensor output",
            "Appending binary sensor packets"
        ]
    }
    st.table(modes_data)

    st.markdown('''
        <div style="background-color: #00599C; padding: 10px 16px; border-radius: 6px; border-left: 3px solid #00599C;">
        <b>⚠️ Critical:</b> Opening an existing file with <code>"w"</code> immediately truncates (empties) it — even before you write anything.
        If you want to add data to an existing log, always use <code>"a"</code> (append), not <code>"w"</code>.
        </div>
    ''', unsafe_allow_html=True)

    st.divider()

    # --- 3. Writing Data ---
    st.markdown("### 3️⃣ Writing Lab Results — `fprintf()`")
    st.write("`fprintf()` works exactly like `printf()`, but takes a `FILE *` as its first argument — directing output to the file instead of the screen.")

    st.code("""#include <stdio.h>

int main() {
    FILE *fptr = fopen("lab_results.csv", "w");

    if (fptr == NULL) {
        printf("Error: Could not create file!\\n");
        return 1;
    }

    /* Write CSV header */
    fprintf(fptr, "Hour,OD600,CFU_per_ml,pH\\n");

    /* Simulated hourly readings */
    float od[]  = {0.05, 0.12, 0.31, 0.72, 1.10};
    float cfu[] = {1e5,  2.4e5, 6.1e5, 1.8e6, 3.2e6};
    float ph[]  = {7.10, 7.05,  6.95,  6.80,  6.60};

    for (int h = 0; h < 5; h++) {
        fprintf(fptr, "%d,%.2f,%.2e,%.2f\\n",
                h + 1, od[h], cfu[h], ph[h]);
    }

    fclose(fptr);    /* CRITICAL — flushes buffer; file saved here */
    printf("Data saved to lab_results.csv\\n");
    return 0;
}
/* File contents:
   Hour,OD600,CFU_per_ml,pH
   1,0.05,1.00e+05,7.10
   2,0.12,2.40e+05,7.05
   ...  */
    """, language="c")

    st.divider()

    # --- 4. Reading Data ---
    st.markdown("### 4️⃣ Reading from a File — `fgets()` and `fscanf()`")
    st.write("Two functions cover most file-reading needs: `fgets()` for line-by-line text, `fscanf()` for formatted values.")

    read_col1, read_col2 = st.columns(2)
    with read_col1:
        st.markdown("**`fgets()` — safe line-by-line reading:**")
        st.code("""#include <stdio.h>
#include <string.h>

int main() {
    char buffer[200];
    FILE *fptr = fopen("sequence.fasta", "r");

    if (fptr == NULL) {          /* NULL check — mandatory */
        printf("File not found!\\n");
        return 1;
    }

    while (fgets(buffer, sizeof(buffer), fptr)) {
        /* fgets returns NULL at EOF — loop stops */
        if (buffer[0] == '>') {
            printf("Header: %s", buffer);
        } else {
            printf("Sequence (%zu bp): %s",
                   strlen(buffer) - 1, buffer);
        }
    }

    fclose(fptr);
    return 0;
}
        """, language="c")

    with read_col2:
        st.markdown("**`fscanf()` — formatted value reading:**")
        st.code("""#include <stdio.h>

int main() {
    int   hour;
    float od, ph;
    FILE *fptr = fopen("lab_results.csv", "r");

    if (fptr == NULL) {
        printf("Cannot open file!\\n");
        return 1;
    }

    /* Skip header line */
    char header[100];
    fgets(header, sizeof(header), fptr);

    /* Read each data row */
    while (fscanf(fptr, "%d,%f,%*f,%f",
                  &hour, &od, &ph) == 3) {
        printf("Hour %d: OD=%.2f  pH=%.2f\\n",
               hour, od, ph);
    }

    fclose(fptr);
    return 0;
}
/* %*f skips the CFU column without storing it */
        """, language="c")

    st.divider()

    # --- 5. File Navigation ---
    st.markdown("### 5️⃣ Navigating Files — `fseek()`, `ftell()`, `rewind()`")
    st.write("C provides functions to move the file position indicator (the 'cursor') to any point in the file — enabling random access rather than only sequential reading.")

    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        st.markdown("**`fseek()` and `ftell()`:**")
        st.code("""FILE *f = fopen("genome.bin", "rb");
if (f == NULL) { return 1; }

/* Move to byte 1000 from start of file */
fseek(f, 1000, SEEK_SET);

/* Move 50 bytes forward from current position */
fseek(f, 50, SEEK_CUR);

/* Move 20 bytes before end of file */
fseek(f, -20, SEEK_END);

/* Get current byte position */
long pos = ftell(f);
printf("Current position: %ld bytes\\n", pos);

fclose(f);
        """, language="c")

    with nav_col2:
        st.markdown("**`rewind()` and file size trick:**")
        st.code("""FILE *f = fopen("sequence.txt", "r");
if (f == NULL) { return 1; }

/* Read entire file once */
char ch;
int  line_count = 0;
while ((ch = fgetc(f)) != EOF)
    if (ch == '\\n') line_count++;
printf("Lines: %d\\n", line_count);

/* Get file size */
fseek(f, 0, SEEK_END);
long file_size = ftell(f);
printf("Size: %ld bytes\\n", file_size);

/* Go back to beginning for a second pass */
rewind(f);                   /* equivalent to fseek(f,0,SEEK_SET) */

fclose(f);
        """, language="c")

        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 12px; border-radius: 5px; border-left: 3px solid #FFFFFF; font-size: 0.88rem; margin-top:6px;">
            <b>fseek() origin constants:</b><br>
            <code>SEEK_SET</code> = from beginning of file<br>
            <code>SEEK_CUR</code> = from current position<br>
            <code>SEEK_END</code> = from end of file
            </div>
        ''', unsafe_allow_html=True)

    # --- MDS / Science Integration ---
    st.markdown('''
        <div style="background-color: #f0f4f8; padding: 20px; border-radius: 8px; border: 1px solid #00599C; margin-top: 15px;">
            <h4 style="color: #00599C; margin-top: 0;">🔬 Multidisciplinary Focus: Data Persistence in Bioinformatics</h4>
            <p style="color: #333; font-size: 0.95rem;">
                File handling is the bridge between C programs and the scientific data ecosystem:
            </p>
            <ul style="color: #333; font-size: 0.95rem;">
                <li><b>FASTA / FASTQ parsing:</b> Genome sequencing files are read with <code>fgets()</code> in a loop — lines starting with <code>&gt;</code> are headers,
                subsequent lines are sequence. This is exactly how tools like BLAST and BWA ingest input.</li>
                <li><b>CSV output for R/Python:</b> Using <code>fprintf()</code> with comma separation and a header row produces files
                directly importable into R (<code>read.csv()</code>) or Python pandas (<code>pd.read_csv()</code>) for statistical analysis.</li>
                <li><b>Binary files for large datasets:</b> Storing 10 million float readings in binary with <code>"wb"</code> takes
                40 MB; the equivalent CSV would be ~120 MB. BAM files (binary alignment format) are the binary counterpart of SAM — read with <code>"rb"</code>.</li>
                <li><b>fseek for indexed access:</b> BLAST database files use fixed-size binary records so that <code>fseek()</code>
                can jump directly to any sequence by record number without reading all preceding records.</li>
            </ul>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")

    # --- Quick Review Quiz ---
    st.subheader("🧠 Quick Review")

    with st.expander("Q1: A file `data.csv` exists and has important data. What happens if you open it with mode `\"w\"`, and how do you avoid losing the data?"):
        st.success("""**Answer:** Opening with `"w"` **immediately truncates** (empties) the file to zero bytes — even before you write a single character. All existing data is permanently lost.

To preserve existing data and add new records, use **`"a"` (append) mode** — it opens the file, positions the cursor at the end, and all writes add to the existing content without erasing it.""")

    with st.expander("Q2: Why must you always check `if (fptr == NULL)` after `fopen()`?"):
        st.success("""**Answer:** `fopen()` returns `NULL` when it fails — e.g., the file doesn't exist (for `"r"` mode), or the disk is full / permissions denied. 

If you proceed without checking and call `fprintf(NULL, ...)` or `fgets(buf, n, NULL)`, the program dereferences a null pointer, causing an immediate **Segmentation Fault (crash)**. The NULL check lets you print a meaningful error message and exit gracefully instead of crashing silently.""")

    with st.expander("Q3: What is the difference between `fprintf()` and `printf()`?"):
        st.success("""**Answer:** Both format and print data using the same format specifiers. The only difference is the destination:
- `printf(format, ...)` → always writes to **stdout** (the screen)
- `fprintf(file_ptr, format, ...)` → writes to the **FILE stream** pointed to by `file_ptr`

`fprintf(stdout, ...)` is actually equivalent to `printf(...)`. Similarly, `fprintf(stderr, ...)` writes error messages to the standard error stream.""")

    with st.expander("Q4: What do `SEEK_SET`, `SEEK_CUR`, and `SEEK_END` mean in `fseek()`?"):
        st.success("""**Answer:** They are the three reference points for the seek offset:
- `SEEK_SET` — offset measured from the **beginning** of the file. `fseek(f, 0, SEEK_SET)` goes to byte 0 (same as `rewind()`).
- `SEEK_CUR` — offset measured from the **current position**. `fseek(f, 10, SEEK_CUR)` skips forward 10 bytes from where you are.
- `SEEK_END` — offset measured from the **end** of the file. `fseek(f, 0, SEEK_END)` goes to the last byte; `fseek(f, -4, SEEK_END)` goes 4 bytes before the end.""")

    with st.expander("Q5: Why use binary mode (`\"rb\"`/`\"wb\"`) instead of text mode (`\"r\"`/`\"w\"`)?"):
        st.success("""**Answer:** In text mode, C performs newline translation: on Windows, `\\n` in memory is written as `\\r\\n` (two bytes) on disk, and `\\r\\n` on disk is read back as `\\n`. This is transparent for text files but **corrupts binary data** — a float value's bytes could be altered mid-stream.

Binary mode disables all translation: bytes are written and read exactly as they are in memory. Use binary mode for structs, image data, sensor packets, BAM files, and any format where every byte's exact value matters.""")

if __name__ == "__main__":
    render()