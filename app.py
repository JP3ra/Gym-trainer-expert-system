import streamlit as st
from expertsystem import GymExpertSystem  
from data.gym_knowledge_base import gym_knowledge_base  

def render_gym_advice(advice):
    st.markdown("## Gym Training Advice")
    for item in advice:
        st.write(item)
    st.markdown("---") 

def main():
    # Set custom theme for the Streamlit app
    st.set_page_config(
        page_title="Gym Training Expert System",
        page_icon=":weight_lifter:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Set custom theme colors
    st.markdown(
        """
        <style>
            body {
                color: #333333;  /* Set text color to dark gray */
            }
            .css-1v3fvcr {
                color: #000000 !important;  /* Set text color for sidebar to black */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Gym Training Expert System")
    st.write("Enter your information to receive personalized gym training advice.")

    user_goals = st.multiselect("Select your goals:", ['weight_loss', 'muscle_gain', 'endurance', 'flexibility'])
    user_experience_level = st.selectbox("Select your experience level:", ['beginner', 'intermediate', 'advanced'])
    user_injury_history = st.selectbox("Select your injury history:", ['none', 'back_pain', 'knee_injury', 'shoulder_injury'])

    user_input = {
        'goals': user_goals,
        'experience_level': user_experience_level,
        'injury_history': user_injury_history,
    }

    expert_system = GymExpertSystem(gym_knowledge_base)
    advice = expert_system.provide_advice(user_input)

    render_gym_advice(advice)

    st.sidebar.title("Gym Training Education")
    education_options = st.sidebar.radio("Select a topic:", ["General Fitness Tips", "Nutrition Guidance", "Recovery Strategies"])

    if education_options:
        st.markdown(f"## {education_options}")

        if education_options == "General Fitness Tips":
            st.write("Here are some general fitness tips:")
            st.write("- Stay consistent with your workouts.")
            st.write("- Get enough sleep for proper recovery.")

        elif education_options == "Nutrition Guidance":
            st.write("Here are personalized nutrition tips based on your goals:")
            for goal in user_goals:
                st.write(f"- For {goal}, consider including foods rich in {get_nutrition_recommendation(goal)}.")

        elif education_options == "Recovery Strategies":
            st.write("Here are personalized recovery strategies based on your injury history:")
            st.write(f"- If you have a history of {user_injury_history}, consider incorporating {get_recovery_strategy(user_injury_history)}.")

# Add functions to get personalized nutrition recommendations and recovery strategies
def get_nutrition_recommendation(goal):
    # Add logic to provide nutrition recommendations based on the user's goal
    if goal == 'weight_loss':
        return 'fiber and lean proteins'
    elif goal == 'muscle_gain':
        return 'protein and complex carbohydrates'
    elif goal == 'endurance':
        return 'carbohydrates and hydration'
    elif goal == 'flexibility':
        return 'nutrient-rich foods to support joint health'

def get_recovery_strategy(injury_history):
    # Add logic to provide recovery strategies based on the user's injury history
    if injury_history == 'back_pain':
        return 'core-strengthening exercises and low-impact activities'
    elif injury_history == 'knee_injury':
        return 'low-impact exercises and knee-friendly movements'
    elif injury_history == 'shoulder_injury':
        return 'focus on exercises that do not exacerbate shoulder pain'

if __name__ == "__main__":
    main()
