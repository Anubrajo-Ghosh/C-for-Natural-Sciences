import streamlit as st
import math


def render():
    # --- Professional Lab Header ---
    st.markdown('''
        <div style="background-color: #00599C; padding: 25px; border-radius: 10px; border-left: 10px solid #002d5a;">
            <h1 style="color: white; margin: 0; font-family: sans-serif;">🧪 Comprehensive Lab Repository</h1>
            <p style="color: #FFFFFF; font-size: 1.1rem; margin-top: 5px;">Verified C Programs: From Foundations to Bio-Computing</p>
        </div>
    ''', unsafe_allow_html=True)

    st.write("")
    st.info("""
        This repository serves as a functional archive of C programs. Each section represents a step up in 
        computational logic, moving from basic syntax to specialized biological analysis.
    """)

    # --- Main Navigation Tabs ---
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌱 Foundations, Logic & Loops",
        "⚙️ Functions & Recursion",
        "📦 Arrays & Structures",
        "🔬 Bio-C Specialization"
    ])


    # =========================================================
    # TAB 1: FOUNDATIONS, LOGIC & LOOPS
    # =========================================================
    with tab1:
        st.subheader("Foundations, Logic & Loops")
        st.info("Basic arithmetic, decision-making, and iterative pattern problems.")

        with st.expander("1. Basic Arithmetic (Add, Subtract, Multiply, Divide, Modulo)"):
            st.write("A single program demonstrating all five fundamental arithmetic operations.")
            st.code("""
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    printf("Addition       : %d + %d = %d\\n", a, b, a + b);
    printf("Subtraction    : %d - %d = %d\\n", a, b, a - b);
    printf("Multiplication : %d * %d = %d\\n", a, b, a * b);

    if (b != 0) {
        printf("Division       : %d / %d = %d\\n", a, b, a / b);
        printf("Modulo         : %d %% %d = %d\\n", a, b, a % b);
    } else {
        printf("Division and Modulo undefined (divisor is zero).\\n");
    }

    return 0;
}
            """, language='c')

        with st.expander("2. Leap Year Check (Ternary Operator)"):
            st.write("Uses the ternary operator to determine if a year is a leap year.")
            st.code("""
#include <stdio.h>

int main() {
    int year;
    printf("Enter a year: ");
    scanf("%d", &year);

    // Ternary operator: condition ? true_val : false_val
    char *result = ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0))
                   ? "a Leap Year"
                   : "NOT a Leap Year";

    printf("%d is %s.\\n", year, result);
    return 0;
}
            """, language='c')

        with st.expander("3. Prime Number Check"):
            st.write("Checks whether a given number is prime using loop-based trial division.")
            st.code("""
#include <stdio.h>
#include <math.h>

int main() {
    int n, isPrime = 1;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if (n < 2) {
        isPrime = 0;
    } else {
        for (int i = 2; i <= (int)sqrt(n); i++) {
            if (n % i == 0) {
                isPrime = 0;
                break;
            }
        }
    }

    if (isPrime)
        printf("%d is a Prime number.\\n", n);
    else
        printf("%d is NOT a Prime number.\\n", n);

    return 0;
}
            """, language='c')

        with st.expander("4. Palindrome Check"):
            st.write("Reverses an integer and checks if it equals the original.")
            st.code("""
#include <stdio.h>

int main() {
    int n, original, reversed = 0, rem;
    printf("Enter an integer: ");
    scanf("%d", &n);

    original = n;
    while (n != 0) {
        rem = n % 10;
        reversed = reversed * 10 + rem;
        n /= 10;
    }

    if (original == reversed)
        printf("%d is a Palindrome.\\n", original);
    else
        printf("%d is NOT a Palindrome.\\n", original);

    return 0;
}
            """, language='c')

        with st.expander("5. Armstrong Number Check (3-Digit)"):
            st.write("Checks if the sum of cubes of digits equals the number itself.")
            st.code("""
#include <stdio.h>
#include <math.h>

int main() {
    int n, original, dig, sum = 0;
    printf("Enter a 3-digit number: ");
    scanf("%d", &n);

    original = n;
    while (n > 0) {
        dig = n % 10;
        sum += (int)pow(dig, 3);
        n /= 10;
    }

    if (sum == original)
        printf("%d is an Armstrong number.\\n", original);
    else
        printf("%d is NOT an Armstrong number.\\n", original);

    return 0;
}
            """, language='c')

        with st.expander("6. Fibonacci Series"):
            st.write("Generates the Fibonacci sequence up to n terms using a loop.")
            st.code("""
#include <stdio.h>

int main() {
    int n, a = 0, b = 1, next;
    printf("Enter number of terms: ");
    scanf("%d", &n);

    printf("Fibonacci Series: ");
    for (int i = 1; i <= n; i++) {
        printf("%d ", a);
        next = a + b;
        a = b;
        b = next;
    }
    printf("\\n");
    return 0;
}
            """, language='c')


    # =========================================================
    # TAB 2: FUNCTIONS & RECURSION
    # =========================================================
    with tab2:
        st.subheader("Functions & Recursion")
        st.info("User-defined functions, then recursive implementations of classic problems.")

        with st.expander("1. Prime Check Using a Function"):
            st.write("Encapsulates prime-checking logic inside a reusable function.")
            st.code("""
#include <stdio.h>
#include <math.h>

// Function declaration
int isPrime(int n);

int main() {
    int num;
    printf("Enter a number: ");
    scanf("%d", &num);

    if (isPrime(num))
        printf("%d is Prime.\\n", num);
    else
        printf("%d is NOT Prime.\\n", num);

    return 0;
}

// Function definition
int isPrime(int n) {
    if (n < 2) return 0;
    for (int i = 2; i <= (int)sqrt(n); i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
            """, language='c')

        with st.expander("2. Fibonacci Using a Function"):
            st.write("Computes the nth Fibonacci term using a dedicated iterative function.")
            st.code("""
#include <stdio.h>

// Function: returns nth Fibonacci number (0-indexed)
int fibonacci(int n) {
    int a = 0, b = 1, next;
    if (n == 0) return 0;
    if (n == 1) return 1;
    for (int i = 2; i <= n; i++) {
        next = a + b;
        a = b;
        b = next;
    }
    return b;
}

int main() {
    int n;
    printf("Enter the term position (n): ");
    scanf("%d", &n);
    printf("Fibonacci(%d) = %d\\n", n, fibonacci(n));
    return 0;
}
            """, language='c')

        with st.expander("3. GCD Using Recursion (Euclidean Algorithm)"):
            st.write("Classic recursive implementation: gcd(a, b) = gcd(b, a % b).")
            st.code("""
#include <stdio.h>
#include <stdlib.h>

// Recursive GCD
int gcd(int a, int b) {
    if (b == 0) return abs(a);
    return gcd(b, a % b);
}

int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("GCD(%d, %d) = %d\\n", a, b, gcd(a, b));
    return 0;
}
            """, language='c')

        with st.expander("4. Multiplication Using Recursion"):
            st.write("Computes a × b by repeated addition recursively.")
            st.code("""
#include <stdio.h>

// Recursive multiplication: a * b = a + a*(b-1)
int multiply(int a, int b) {
    if (b == 0) return 0;
    if (b < 0) return -multiply(a, -b);
    return a + multiply(a, b - 1);
}

int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    printf("%d x %d = %d\\n", a, b, multiply(a, b));
    return 0;
}
            """, language='c')


    # =========================================================
    # TAB 3: ARRAYS & STRUCTURES
    # =========================================================
    with tab3:
        st.subheader("Arrays & Structures")
        st.info("Array operations and struct-based data modeling.")
        st.markdown('''
            <div style="background-color: #00599C; padding: 8px 14px; border-radius: 6px; border-left: 3px solid #FFFFFFF; font-size: 0.88rem;">
            <b>📌 Note on Variable-Length Arrays (VLAs):</b> Programs 1 and 2 use <code>int arr[n]</code> where n is set at runtime.
            VLAs are supported in C99 and C11, were made optional in C11, and are not available in C17+.
            For maximum portability, use <code>malloc(n * sizeof(int))</code> instead.
            </div>
        ''', unsafe_allow_html=True)

        with st.expander("1. Maximum and Minimum in an Array"):
            st.write("Finds the largest and smallest element in a user-defined array.")
            st.code("""
#include <stdio.h>

int main() {
    int n;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\\n", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    int max = arr[0], min = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];
    }

    printf("Maximum: %d\\n", max);
    printf("Minimum: %d\\n", min);
    return 0;
}
            """, language='c')

        with st.expander("2. Linear Search in an Array"):
            st.write("Searches for a target element sequentially and reports its index.")
            st.code("""
#include <stdio.h>

void linearSearch(int arr[], int size, int target) {
    int found = 0;
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            printf("Element %d found at index %d.\\n", target, i);
            found = 1;
        }
    }
    if (!found)
        printf("Element %d not found in the array.\\n", target);
}

int main() {
    int n, target;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter %d elements:\\n", n);
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("Enter element to search: ");
    scanf("%d", &target);

    linearSearch(arr, n, target);
    return 0;
}
            """, language='c')

        with st.expander("3. Structure: Student Record"):
            st.write("Demonstrates a struct to store and display student data.")
            st.code("""
#include <stdio.h>
#include <string.h>

struct Student {
    char name[50];
    int rollNo;
    float marks;
};

int main() {
    struct Student s;

    printf("Enter student name: ");
    scanf("%s", s.name);
    printf("Enter roll number: ");
    scanf("%d", &s.rollNo);
    printf("Enter marks: ");
    scanf("%f", &s.marks);

    printf("\\n--- Student Record ---\\n");
    printf("Name    : %s\\n", s.name);
    printf("Roll No : %d\\n", s.rollNo);
    printf("Marks   : %.2f\\n", s.marks);

    return 0;
}
            """, language='c')

        with st.expander("4. Structure: Microbiology Sample Record"):
            st.write("Uses a struct to model a lab sample — a domain-relevant application of structs.")
            st.code("""
#include <stdio.h>
#include <string.h>

struct Sample {
    char sampleID[20];
    char organism[50];
    float gcContent;      // in percentage
    int colonyCount;
};

int main() {
    struct Sample s;

    printf("Enter Sample ID: ");
    scanf("%s", s.sampleID);
    printf("Enter Organism Name: ");
    scanf("%s", s.organism);
    printf("Enter GC Content (%%): ");
    scanf("%f", &s.gcContent);
    printf("Enter Colony Count: ");
    scanf("%d", &s.colonyCount);

    printf("\\n--- Lab Sample Report ---\\n");
    printf("Sample ID    : %s\\n", s.sampleID);
    printf("Organism     : %s\\n", s.organism);
    printf("GC Content   : %.2f%%\\n", s.gcContent);
    printf("Colony Count : %d CFU/mL\\n", s.colonyCount);

    return 0;
}
            """, language='c')


    # =========================================================
    # TAB 4: BIO-C SPECIALIZATION
    # =========================================================
    with tab4:
        st.subheader("Computational Microbiology (Bio-C)")
        st.info("Targeted programs for Semester 2 Microbiology & Biochemistry modeling.")

        bioc_tab1, bioc_tab2, bioc_tab3, bioc_tab4 = st.tabs([
            "🧬 DNA/RNA & Molecular Biology",
            "🦠 Microbial Growth & Ecology",
            "⚗️ Enzymes & Biochemistry",
            "🔗 Protein & Amino Acid Analysis"
        ])

        # ---- DNA/RNA & MOLECULAR BIOLOGY ----
        with bioc_tab1:

            with st.expander("1. DNA Thermal Stability (GC Content)"):
                st.write("Determines the thermal stability of a DNA sequence by computing GC content. Higher GC% → higher melting temperature due to triple hydrogen bonds.")
                st.code("""
#include <stdio.h>
#include <string.h>

int main() {
    char seq[] = "ATGCGTAC";
    int gc = 0;
    int len = strlen(seq);

    for (int i = 0; i < len; i++) {
        if (seq[i] == 'G' || seq[i] == 'C') gc++;
    }

    printf("Sequence    : %s\\n", seq);
    printf("Length      : %d bp\\n", len);
    printf("GC Count    : %d\\n", gc);
    printf("GC Content  : %.2f%%\\n", (float)gc / len * 100);

    return 0;
}
                """, language='c')

            with st.expander("2. DNA to RNA Transcription"):
                st.write("Converts a DNA template strand to its mRNA transcript by replacing T with U. Uses pointers to traverse the sequence.")
                st.code("""
#include <stdio.h>
#include <string.h>

void transcribe(char *dna, char *rna) {
    int i;
    for (i = 0; dna[i] != '\\0'; i++) {
        if      (dna[i] == 'A') rna[i] = 'U';
        else if (dna[i] == 'T') rna[i] = 'A';
        else if (dna[i] == 'G') rna[i] = 'C';
        else if (dna[i] == 'C') rna[i] = 'G';
        else                    rna[i] = '?';  // unknown base
    }
    rna[i] = '\\0';
}

int main() {
    char dna[100], rna[100];
    printf("Enter DNA template strand (e.g. ATGCGT): ");
    scanf("%s", dna);

    transcribe(dna, rna);

    printf("\\n--- Transcription Result ---\\n");
    printf("DNA Template : %s\\n", dna);
    printf("mRNA Strand  : %s\\n", rna);

    return 0;
}
                """, language='c')

            with st.expander("3. Complementary DNA Strand Generator"):
                st.write("Generates the complementary antiparallel DNA strand (A↔T, G↔C) from a given sequence. Uses a struct to store both strands together.")
                st.code("""
#include <stdio.h>
#include <string.h>

struct DNAStrand {
    char original[100];
    char complement[100];
};

char getComplement(char base) {
    if (base == 'A') return 'T';
    if (base == 'T') return 'A';
    if (base == 'G') return 'C';
    if (base == 'C') return 'G';
    return '?';
}

int main() {
    struct DNAStrand ds;
    printf("Enter DNA sequence (5'→3'): ");
    scanf("%s", ds.original);

    int len = strlen(ds.original);
    for (int i = 0; i < len; i++) {
        ds.complement[i] = getComplement(ds.original[len - 1 - i]); // antiparallel
    }
    ds.complement[len] = '\\0';

    printf("\\n--- Complementary Strand ---\\n");
    printf("5'→3' (Original)    : %s\\n", ds.original);
    printf("3'→5' (Complement)  : %s\\n", ds.complement);

    return 0;
}
                """, language='c')

        # ---- MICROBIAL GROWTH & ECOLOGY ----
        with bioc_tab2:

            with st.expander("4. Bacterial Growth Engine (Exponential Model)"):
                st.write("Models exponential population dynamics using Nt = N0 × e^(rt). Applicable to the log phase of bacterial growth.")
                st.code("""
#include <stdio.h>
#include <math.h>

int main() {
    double n0, r;
    int t;

    printf("Enter initial population (N0): ");
    scanf("%lf", &n0);
    printf("Enter growth rate constant (r): ");
    scanf("%lf", &r);
    printf("Enter time in hours (t): ");
    scanf("%d", &t);

    double nt = n0 * exp(r * t);

    printf("\\n--- Exponential Growth Model ---\\n");
    printf("Formula     : Nt = N0 * e^(r*t)\\n");
    printf("N0 = %.2f | r = %.3f | t = %d hrs\\n", n0, r, t);
    printf("Population after %d hours: %.2f cells\\n", t, nt);

    return 0;
}
                """, language='c')

            with st.expander("5. Generation Time & Doubling Calculator"):
                st.write("Calculates the number of generations and generation time (g) from initial and final population counts and elapsed time. Uses the formula: g = (log10 Nt - log10 N0) / log10 2.")
                st.code("""
#include <stdio.h>
#include <math.h>

int main() {
    double n0, nt, time_hrs;

    printf("Enter initial population (N0)   : ");
    scanf("%lf", &n0);
    printf("Enter final population (Nt)     : ");
    scanf("%lf", &nt);
    printf("Enter elapsed time (hours)      : ");
    scanf("%lf", &time_hrs);

    // Number of generations
    double generations = (log10(nt) - log10(n0)) / log10(2);

    // Generation time
    double gen_time = time_hrs / generations;

    printf("\\n--- Generation Time Calculator ---\\n");
    printf("Number of Generations : %.2f\\n", generations);
    printf("Generation Time (g)   : %.4f hours\\n", gen_time);
    printf("Generation Time (g)   : %.2f minutes\\n", gen_time * 60);

    return 0;
}
                """, language='c')

            with st.expander("6. Logistic Growth Model (Carrying Capacity)"):
                st.write("More realistic than exponential growth — models population growth with a carrying capacity K using the logistic equation: dN/dt = rN(1 - N/K). Simulates population at each time step.")
                st.code("""
#include <stdio.h>

int main() {
    double n0, r, K, n, dt = 0.1;
    int steps;

    printf("Enter initial population (N0)     : ");
    scanf("%lf", &n0);
    printf("Enter growth rate (r)             : ");
    scanf("%lf", &r);
    printf("Enter carrying capacity (K)       : ");
    scanf("%lf", &K);
    printf("Enter number of time steps        : ");
    scanf("%d", &steps);

    n = n0;
    printf("\\n--- Logistic Growth Simulation ---\\n");
    printf("%-10s %-15s\\n", "Time", "Population");
    printf("%-10s %-15s\\n", "----", "----------");

    for (int i = 0; i <= steps; i++) {
        double t = i * dt;
        printf("%-10.2f %-15.4f\\n", t, n);
        double dn = r * n * (1.0 - n / K) * dt;
        n += dn;
    }

    return 0;
}
                """, language='c')

        # ---- ENZYMES & BIOCHEMISTRY ----
        with bioc_tab3:

            with st.expander("7. Michaelis-Menten Enzyme Kinetics"):
                st.write("Calculates reaction velocity (V) for a range of substrate concentrations [S] using V = (Vmax × [S]) / (Km + [S]). Prints a table suitable for plotting a Michaelis-Menten curve.")
                st.code("""
#include <stdio.h>

int main() {
    double vmax, km, s;
    int n;

    printf("Enter Vmax (µmol/min)   : ");
    scanf("%lf", &vmax);
    printf("Enter Km (mM)           : ");
    scanf("%lf", &km);
    printf("Enter number of [S] points to compute: ");
    scanf("%d", &n);

    printf("\\n--- Michaelis-Menten Kinetics ---\\n");
    printf("Formula: V = (Vmax * [S]) / (Km + [S])\\n\\n");
    printf("%-15s %-15s\\n", "[S] (mM)", "V (µmol/min)");
    printf("%-15s %-15s\\n", "--------", "------------");

    double s_step = km / 2.0;   // generate evenly spaced [S] values
    for (int i = 1; i <= n; i++) {
        s = i * s_step;
        double v = (vmax * s) / (km + s);
        printf("%-15.4f %-15.4f\\n", s, v);
    }

    return 0;
}
                """, language='c')

            with st.expander("8. pH and [H⁺] Converter"):
                st.write("Converts between pH and hydrogen ion concentration using pH = -log10[H⁺]. Also determines the solution category (strongly acidic, weakly acidic, neutral, alkaline).")
                st.code("""
#include <stdio.h>
#include <math.h>

int main() {
    int choice;
    printf("pH ↔ [H+] Converter\\n");
    printf("1. Enter pH → get [H+]\\n");
    printf("2. Enter [H+] → get pH\\n");
    printf("Choice: ");
    scanf("%d", &choice);

    if (choice == 1) {
        double ph;
        printf("Enter pH value: ");
        scanf("%lf", &ph);
        double h_conc = pow(10, -ph);
        printf("\\n[H+] concentration : %.2e mol/L\\n", h_conc);

        if      (ph < 3)  printf("Category : Strongly Acidic\\n");
        else if (ph < 7)  printf("Category : Weakly Acidic\\n");
        else if (ph == 7) printf("Category : Neutral\\n");
        else if (ph < 11) printf("Category : Weakly Alkaline\\n");
        else              printf("Category : Strongly Alkaline\\n");

    } else if (choice == 2) {
        double h_conc;
        printf("Enter [H+] in mol/L (e.g. 0.001): ");
        scanf("%lf", &h_conc);
        double ph = -log10(h_conc);
        printf("\\npH = %.4f\\n", ph);
    } else {
        printf("Invalid choice.\\n");
    }

    return 0;
}
                """, language='c')

        # ---- PROTEIN & AMINO ACID ANALYSIS ----
        with bioc_tab4:

            with st.expander("9. Amino Acid Composition Counter"):
                st.write("Counts occurrences of each unique amino acid in a single-letter code protein sequence. Uses an array to track frequency, then prints a composition table.")
                st.code("""
#include <stdio.h>
#include <string.h>

int main() {
    // Single-letter amino acid codes (20 standard)
    char aa_codes[] = "ACDEFGHIKLMNPQRSTVWY";
    char seq[200];
    int count[20] = {0};

    printf("Enter protein sequence (single-letter codes, e.g. MKVLWA): ");
    scanf("%s", seq);

    int len = strlen(seq);

    // Count each amino acid
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < 20; j++) {
            if (seq[i] == aa_codes[j]) {
                count[j]++;
                break;
            }
        }
    }

    printf("\\n--- Amino Acid Composition ---\\n");
    printf("Sequence Length: %d residues\\n\\n", len);
    printf("%-6s %-10s %-10s\\n", "Code", "Count", "Percentage");
    printf("%-6s %-10s %-10s\\n", "----", "-----", "----------");

    for (int j = 0; j < 20; j++) {
        if (count[j] > 0) {
            printf("%-6c %-10d %.2f%%\\n",
                   aa_codes[j], count[j],
                   (float)count[j] / len * 100);
        }
    }

    return 0;
}
                """, language='c')

            with st.expander("10. Protein Molecular Weight Estimator"):
                st.write("Estimates the molecular weight of a protein from its amino acid sequence using average residue masses. Uses a struct to pair each amino acid code with its mass.")
                st.code("""
#include <stdio.h>
#include <string.h>

// Struct to store amino acid code and its average residue mass (Da)
struct AminoAcid {
    char code;
    float mass;
};

int main() {
    struct AminoAcid aa[] = {
        {'A', 89.09},  {'R', 174.20}, {'N', 132.12}, {'D', 133.10},
        {'C', 121.16}, {'E', 147.13}, {'Q', 146.15}, {'G', 75.03},
        {'H', 155.16}, {'I', 131.17}, {'L', 131.17}, {'K', 146.19},
        {'M', 149.21}, {'F', 165.19}, {'P', 115.13}, {'S', 105.09},
        {'T', 119.12}, {'W', 204.23}, {'Y', 181.19}, {'V', 117.15}
    };
    int aa_count = 20;

    char seq[200];
    printf("Enter protein sequence (single-letter codes): ");
    scanf("%s", seq);

    int len = strlen(seq);
    float total_mass = 0.0;
    int unrecognised = 0;

    for (int i = 0; i < len; i++) {
        int found = 0;
        for (int j = 0; j < aa_count; j++) {
            if (seq[i] == aa[j].code) {
                total_mass += aa[j].mass;
                found = 1;
                break;
            }
        }
        if (!found) unrecognised++;
    }

    // Subtract water for each peptide bond formed (n-1 bonds)
    float mw = total_mass - (len - 1) * 18.02;

    printf("\\n--- Molecular Weight Estimate ---\\n");
    printf("Sequence Length   : %d residues\\n", len);
    printf("Unrecognised AAs  : %d\\n", unrecognised);
    printf("Estimated MW      : %.2f Da\\n", mw);
    printf("Estimated MW      : %.4f kDa\\n", mw / 1000);

    return 0;
}
                """, language='c')

    # --- Footer ---
    st.markdown("---")
    st.info("💡 **Academic Note:** This repository demonstrates the transition from basic logic to bioinformatics-ready code.")
    st.caption("© 2026 Lab Journal Portfolio | MCBA Semester 2 | St. Xavier's College (Autonomous), Kolkata")