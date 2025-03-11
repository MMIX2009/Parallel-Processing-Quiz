import streamlit as st

# Title of the app
st.title("Parallel Processors Quiz")
st.write("Parallel Pathways: Test Your Knowledge of Multicore Computing and Threading 🚀")

# Initialize session state variables if they don’t exist
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answer_submitted" not in st.session_state:
    st.session_state.answer_submitted = False

# Questions and answers

quiz = [
    # Introduction to Parallel Processing
    {"question": "What is the primary motivation for using multiple computers or processors?",
     "options": ["Reducing energy consumption", "Increasing performance", "Minimizing memory usage", "Eliminating software dependencies"],
     "answer": "Increasing performance"},

    {"question": "Which of the following is NOT a benefit of parallel processing?",
     "options": ["Scalability", "Availability", "Reduced hardware costs", "Power efficiency"],
     "answer": "Reduced hardware costs"},

    # Parallel Hardware and Software
    {"question": "What is the key challenge in making effective use of parallel hardware?",
     "options": ["Designing high-performance GPUs", "Developing parallel software", "Minimizing cache memory", "Reducing transistor count"],
     "answer": "Developing parallel software"},

    {"question": "Which hardware example best represents a parallel processor?",
     "options": ["Intel Pentium 4", "Quad-core Xeon e5345", "Single-core ARM Cortex A7", "IBM System/360"],
     "answer": "Quad-core Xeon e5345"},

    # Parallel Programming Challenges
    {"question": "Which of the following is NOT a major challenge in parallel programming?",
     "options": ["Partitioning", "Coordination", "Communications overhead", "Instruction caching"],
     "answer": "Instruction caching"},

    {"question": "What does coordination in parallel programming refer to?",
     "options": ["Dividing tasks into equal workloads", "Managing dependencies and interactions between subtasks", "Optimizing cache memory", "Executing instructions sequentially"],
     "answer": "Managing dependencies and interactions between subtasks"},

    # Amdahl's Law
    {"question": "What fundamental law describes the limitation of speedup in parallel computing?",
     "options": ["Moore's Law", "Amdahl's Law", "Little’s Law", "Ohm’s Law"],
     "answer": "Amdahl's Law"},

    {"question": "According to Amdahl's Law, what factor limits speedup in a parallel system?",
     "options": ["Cache miss rate", "The sequential portion of a program", "Number of CPU cores", "Power consumption"],
     "answer": "The sequential portion of a program"},

    # Scaling in Parallel Systems
    {"question": "What is the difference between strong and weak scaling?",
     "options": ["Strong scaling keeps the problem size fixed, while weak scaling increases it with the number of processors", "Strong scaling requires more memory, while weak scaling requires less", "Weak scaling improves efficiency, while strong scaling decreases it", "There is no difference"],
     "answer": "Strong scaling keeps the problem size fixed, while weak scaling increases it with the number of processors"},

    {"question": "In weak scaling, what happens to the problem size as the number of processors increases?",
     "options": ["It remains constant", "It decreases", "It increases proportionally", "It is divided into smaller subproblems"],
     "answer": "It increases proportionally"},

    # Flynn's Taxonomy
    {"question": "Which classification describes a processor executing a single instruction stream on a single data stream?",
     "options": ["MISD", "SIMD", "SISD", "MIMD"],
     "answer": "SISD"},

    {"question": "What does SIMD stand for?",
     "options": ["Single Instruction, Multiple Data", "Simultaneous Instruction, Multiple Data", "Single Integrated Multi-core Device", "Serial Instruction, Multi-threaded Design"],
     "answer": "Single Instruction, Multiple Data"},

    {"question": "Which type of parallel architecture executes multiple instruction streams on multiple data streams?",
     "options": ["MIMD", "SIMD", "MISD", "SISD"],
     "answer": "MIMD"},

    # Vector Processors
    {"question": "What is a key advantage of vector processors?",
     "options": ["Increased instruction fetch bandwidth", "Reduced pipeline complexity", "More efficient execution of data-parallel operations", "Higher branch prediction accuracy"],
     "answer": "More efficient execution of data-parallel operations"},

    {"question": "What does the instruction 'lv' do in a vector processor?",
     "options": ["Loads a scalar value", "Loads a vector from memory", "Stores a vector into memory", "Performs vector multiplication"],
     "answer": "Loads a vector from memory"},

    {"question": "What is a key difference between vector instructions and multimedia extensions?",
     "options": ["Vector instructions have variable vector width, while multimedia extensions have fixed width", "Vector instructions are slower but more power-efficient", 
     "Multimedia extensions support strided memory access, while vector instructions don't", "Vector instructions only work with integers, while multimedia extensions support floating-point"],
     "answer": "Vector instructions have variable vector width, while multimedia extensions have fixed width"}

    # Multithreading
    {"question": "What is the primary goal of multithreading?",
     "options": ["Increasing memory bandwidth", "Reducing power consumption", "Hiding stalls by executing multiple threads", "Minimizing instruction cache misses"],
     "answer": "Hiding stalls by executing multiple threads"},

    {"question": "Which type of multithreading switches threads after every cycle?",
     "options": ["Coarse-grain multithreading", "Fine-grain multithreading", "Simultaneous multithreading", "Parallel pipeline threading"],
     "answer": "Fine-grain multithreading"},

    # Simultaneous Multithreading (SMT)
    {"question": "Which processor first introduced Hyper-Threading (HT) technology?",
     "options": ["Intel Pentium 4", "AMD Ryzen", "IBM POWER9", "Apple M1"],
     "answer": "Intel Pentium 4"},

    {"question": "In simultaneous multithreading (SMT), how are instructions from different threads executed?",
     "options": ["Sequentially in the same core", "Simultaneously using available function units", "Only after cache misses", "Only when the pipeline is empty"],
     "answer": "Simultaneously using available function units"}
]
# The above list contains 20 MCQ questions covering exceptions, interrupts, and pipeline handling.

# Display the current question
current_question = quiz[st.session_state.question_index]
st.write(f"**Question {st.session_state.question_index + 1}: {current_question['question']}**")

# Multiple-choice options
selected_option = st.radio("Select your answer:", current_question["options"], key=f"question_{st.session_state.question_index}")

# Submit button to evaluate the selected answer
if st.button("Submit Answer") and not st.session_state.answer_submitted:
    if selected_option == current_question["answer"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Incorrect. The correct answer is: {current_question['answer']}")
    st.session_state.answer_submitted = True

# Next button (enabled only after an answer is submitted)
if st.session_state.answer_submitted:
    if st.button("Next Question"):
        if st.session_state.question_index < len(quiz) - 1:
            st.session_state.question_index += 1
            st.session_state.answer_submitted = False
            # Force rerun to display the next question immediately
            st.rerun()
        else:
            st.write("### Quiz Completed!")
            st.write(f"Your final score is {st.session_state.score}/{len(quiz)}")
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.answer_submitted = False

st.write(f"**Current Score:** {st.session_state.score}")
