import streamlit as st

def main():
    st.title("My Computer Quiz")

    # Initialize session state
    if "playing" not in st.session_state:
        st.session_state.playing = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # Questions and answers (revised feedback for appropriateness)
    questions = [
        {"q": "How many beers you think you can drink?", "options": ["1", "2", "3", "4"], "correct": "1", "incorrect": "Nice try, but not quite!"},
        {"q": "Are you a virgin?", "options": ["Yes", "No"], "correct": "No", "incorrect": "Oops, try again!"},
        {"q": "How many accounts you opened till now?", "options": ["0", "1", "2", "3"], "correct": "1", "incorrect": "Not quite, think again!"},
        {"q": "Yadhavas ekkuva leda Gouds ekkuva?", "options": ["Yadhavas", "Gouds"], "correct": "Yadhavas", "incorrect": "Almost, give it another shot!"},
        {"q": "Telangana Jathi Pitha evaru?", "options": ["KCR", "Other"], "correct": "KCR", "incorrect": "Incorrect, think harder!"},
        {"q": "Nee brathukulo eppudu aina beer konukoni tagava okkadive?", "options": ["Yes", "No"], "correct": "Yes", "incorrect": "Close, but not right!"},
        {"q": "Nuvvu pedda fan-a? Chinna fan-a?", "options": ["Big fan", "Small fan"], "correct": "Small fan", "incorrect": "Haha, nice try!"},
        {"q": "Neku inka takita takita workout avutunda?", "options": ["Yes", "No"], "correct": "Yes", "incorrect": "Keep practicing!"}
    ]

    # Ask if the user wants to play
    if not st.session_state.playing:
        st.write("Do you want to play?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                st.session_state.playing = True
                st.session_state.submitted = False
                st.rerun()
        with col2:
            if st.button("No"):
                st.write("Goodbye!")
                return

    # Display questions
    if st.session_state.playing and st.session_state.question_index < len(questions):
        q = questions[st.session_state.question_index]
        st.write(f"Question {st.session_state.question_index + 1}: {q['q']}")
        answer = st.radio("Choose an answer:", q["options"], key=f"q{st.session_state.question_index}")
        
        if st.button("Submit Answer") and not st.session_state.submitted:
            st.session_state.submitted = True
            if answer.lower() == q["correct"].lower():
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(q["incorrect"])
        
        if st.session_state.submitted:
            if st.button("Next Question"):
                st.session_state.question_index += 1
                st.session_state.submitted = False
                st.rerun()
        
        st.write(f"Score: {st.session_state.score}/{len(questions)}")
    elif st.session_state.playing:
        st.write(f"You got {st.session_state.score} questions correct")
        st.write(f"You got {(st.session_state.score / len(questions)) * 100:.2f}%")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.session_state.playing = False
            st.session_state.submitted = False
            st.rerun()

if __name__ == "__main__":
    main()