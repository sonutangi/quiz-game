import streamlit as st

def main():
    st.title("Welcome to My Computer Quiz!")

    # Initialize session state
    if "playing" not in st.session_state:
        st.session_state.playing = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0

    # Questions and correct answers
    questions = [
        {"question": "How many beers you think you can drink?", "options": ["1", "2", "3", "4"], "correct": "1", "incorrect_msg": "Dengindi sharma"},
        {"question": "Are you a virgin?", "options": ["Yes", "No"], "correct": "No", "incorrect_msg": "Pikavule sharma"},
        {"question": "How many accounts you opened till now?", "options": ["0", "1", "2", "3"], "correct": "1", "incorrect_msg": "Incorrect! Neku antha scene ledu le"},
        {"question": "Yadhavas ekkuva leda Gouds ekkuva?", "options": ["Yadhavas", "Gouds"], "correct": "Yadhavas", "incorrect_msg": "Tappu! Nuvvu janmalo maravu inka"},
        {"question": "Telangana Jathi Pitha evaru?", "options": ["KCR", "Other"], "correct": "KCR", "incorrect_msg": "Siggu undali, me anna entha chesadu meku"},
        {"question": "Nee brathukulo eppudu aina beer konukoni tagava okkadive?", "options": ["Yes", "No"], "correct": "Yes", "incorrect_msg": "Chi! Enduku sharma a brathuku endulo aina duki chavu"},
        {"question": "Nuvvu pedda lanjava? Chinna lanjava?", "options": ["Pedda lanja", "Chinna lanja"], "correct": "Chinna lanja", "incorrect_msg": "Gudda musuko nuvvu pedda lanjavi"},
        {"question": "Neku inka takita takita workout avutunda?", "options": ["Yes", "No"], "correct": "Yes", "incorrect_msg": "Mothaniki oppukunnavu"}
    ]

    # Ask if the user wants to play
    if not st.session_state.playing:
        st.write("Do you want to play?")
        if st.button("Yes"):
            st.session_state.playing = True
        if st.button("No"):
            st.write("Goodbye!")
            return

    # Display questions
    if st.session_state.playing and st.session_state.question_index < len(questions):
        q = questions[st.session_state.question_index]
        st.write(f"Question {st.session_state.question_index + 1}: {q['question']}")
        answer = st.radio("Choose an answer:", q["options"], key=f"q{st.session_state.question_index}")
        
        if st.button("Submit Answer"):
            if answer.lower() == q["correct"].lower():
                st.session_state.score += 1
                st.success("Correct!")
            else:
                st.error(q["incorrect_msg"])
            st.session_state.question_index += 1
            st.experimental_rerun()  # Refresh to show next question
        
        st.write(f"Score: {st.session_state.score}/{len(questions)}")
    elif st.session_state.playing:
        st.write(f"You got {st.session_state.score} questions correct")
        st.write(f"You got {(st.session_state.score / len(questions)) * 100:.2f}%")
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.question_index = 0
            st.session_state.playing = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
