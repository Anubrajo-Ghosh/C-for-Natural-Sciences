import streamlit as st
import time
import importlib

# Instead of 'from chapters import 1_generations', use this:
gen        = importlib.import_module("chapters.1_generations")
hist       = importlib.import_module("chapters.2_history")
struct     = importlib.import_module("chapters.3_structure_basics")
data_mg    = importlib.import_module("chapters.4_data_management")
ops        = importlib.import_module("chapters.5_operators")
io         = importlib.import_module("chapters.6_input_output")
select     = importlib.import_module("chapters.7_selection")
iters      = importlib.import_module("chapters.8_iterations")
funcs      = importlib.import_module("chapters.9_functions")
arr_ptr    = importlib.import_module("chapters.10_arrays_pointers")
storage    = importlib.import_module("chapters.11_storage_classes")
str_uni    = importlib.import_module("chapters.12_struct_union")
file_mod   = importlib.import_module("chapters.13_file_handling")
string_mod = importlib.import_module("chapters.14_strings")
lib_mod    = importlib.import_module("chapters.15_libraries")
lab_repo   = importlib.import_module("chapters.16_lab_repository")
home_mod   = importlib.import_module("chapters.home")

# --- Page Configuration ---
st.set_page_config(page_title="C for Natural Sciences", page_icon="🦠", layout="wide")

# --- SESSION STATE ---
if 'entered' not in st.session_state:
    st.session_state.entered = False
if 'initialized' not in st.session_state:
    st.session_state.initialized = False

# --- Helper: convert local image to base64 for CSS background ---
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


# --- OPENING SPLASH PAGE ---
def show_opening_page():
    try:
        bin_str = get_base64_of_bin_file('loading_bio.jpg')
        bg_img_style = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .main .block-container {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 3rem;
        }}
        [data-testid="stAppViewBlockContainer"] {{ overflow: hidden; }}
        </style>
        '''
        st.markdown(bg_img_style, unsafe_allow_html=True)
    except FileNotFoundError:
        # Background image missing — continue without it (no st.error inside column)
        pass

    _, col, _ = st.columns([1, 2, 1])
    with col:
        st.markdown('''
            <div style="text-align: center; margin-top: 10px; margin-bottom: 15px;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg"
                     style="width:100px; height: 100px;">
            </div>
            <div style="text-align: center; padding: 25px; border: 2px solid #00599C;
                        border-radius: 15px; background-color: rgba(240, 244, 248, 0.9);">
                <h1 style="color: #002d5a; font-size: 2.2rem; margin-bottom: 5px;
                           text-align: center; width: 109%;">
                    C for Natural Sciences
                </h1>
                <!-- FIX: removed extra quote and fixed width from 110% → 100% -->
                <h4 style="color: #00599C; font-weight: 300; margin-bottom: 10px;
                           text-align: center; width: 109%;">
                    <b>Bridging Biological Logic with Computational Power</b>
                </h4>
                <hr style="border-color: #00599C;">
                <p style="font-size: 1.8rem; color: #333; margin-bottom: 0;"><b>Anubrajo Ghosh</b></p>
                <p style="font-size: 1.7rem; color: #333; margin-bottom: 0;"><b>Roll No. - 0618</b></p>
                <p style="font-size: 1.6rem; color: #333; margin-bottom: 0;"><b>Semester 2 | MCBA</b></p>
            </div>
        ''', unsafe_allow_html=True)

        st.write("")
        if st.button("Click Here", use_container_width=True, type="primary"):
            st.session_state.entered = True
            st.rerun()


# =====================================================================
# MAIN APP
# =====================================================================
if not st.session_state.entered:
    st.markdown("<style>[data-testid='stSidebar'] {display: none;}</style>",
                unsafe_allow_html=True)
    show_opening_page()

else:
    # --- CODING ANIMATION (vanishes after completion) ---
    if not st.session_state.initialized:
        placeholder = st.empty()
        with placeholder.container():
            with st.status("🚀 Initializing Bio-Computational Environment...",
                           expanded=True) as status:
                st.write("Linker: Connecting <stdio.h> to Microbiology Modules...")
                time.sleep(0.6)
                st.write("Compiler: Optimizing Pointers for Genomic Arrays...")
                time.sleep(0.8)
                st.write("System: Mounting MDS Research Paper Assets...")
                time.sleep(0.5)
                status.update(label="✅ System Ready!", state="complete", expanded=False)
            time.sleep(0.8)
        placeholder.empty()
        st.session_state.initialized = True

    # --- SIDEBAR ---
    st.sidebar.markdown('''
        <div style="text-align: center; padding-bottom: 10px;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/1/18/C_Programming_Language.svg"
                 style="width: 60px;">
            <h3 style="color: #FFFFFF; margin-top: 10px;">Chapters</h3>
        </div>
    ''', unsafe_allow_html=True)
    st.sidebar.markdown("---")


    menu = {
        "🏠 Home":                    home_mod,
        "📜 Language Generations":    gen,
        "🌐 History of C":            hist,
        "🏗️ Program Structure":       struct,
        "📊 Data Types":              data_mg,
        "➕ Operators":               ops,
        "📡 Input & Output":          io,
        "🧠 Selection Control":       select,
        "🔄 Iterations & Loops":      iters,
        "🧩 Functions":               funcs,
        "🎯 Arrays & Pointers":       arr_ptr,
        "💾 Storage Classes":         storage,
        "🗂️ Structures & Unions":     str_uni,   
        "📁 File Handling":           file_mod,
        "🧬 Strings & Sequences":     string_mod,
        "🧮 Libraries & Math":        lib_mod,
        "🧪 Solved Lab Repository":   lab_repo,
    }

    choice = st.sidebar.radio("Navigate:", list(menu.keys()))

    # --- AUTO-SCROLL TO TOP ON MENU CHANGE ---
    # FIX: Updated JS target — previous selector missed in some Streamlit versions
    st.components.v1.html(
        """
        <script>
            try {
                // Scroll the main content area to top on every page render
                window.parent.document.querySelector('section.main').scrollTo(0, 0);
            } catch(e) {
                // Fallback: scroll the whole parent window
                window.parent.scrollTo(0, 0);
            }
        </script>
        """,
        height=0,
    )

    # --- RENDER SELECTED MODULE ---
    menu[choice].render()

    # --- SIDEBAR FOOTER ---
    st.sidebar.markdown("---")
    st.sidebar.caption("© AG | MCBA Sem 2 | SXC Kolkata | 2026")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.entered = False
        st.session_state.initialized = False
        st.rerun()