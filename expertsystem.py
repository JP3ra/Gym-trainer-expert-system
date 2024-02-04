class GymExpertSystem:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base

    def provide_advice(self, user_input):
        advice = []

        for rule in self.knowledge_base:
            if 'goals' in rule and all(goal in user_input['goals'] for goal in rule['goals']):
                advice.append(f"If your goal is {', '.join(user_input['goals'])}, consider a {rule.get('routine', 'unknown')} routine.")
            
            exercise_type = rule.get('exercise_type', 'unknown')
            muscle_group = rule.get('muscle_group', 'unknown')
            
            if exercise_type == user_input.get('exercise_type') and muscle_group == user_input.get('muscle_group'):
                advice.append(f"For {muscle_group} {exercise_type} training, {rule.get('advice', 'unknown')}")
            
            experience_level = rule.get('experience_level', 'unknown')
            if experience_level == user_input.get('experience_level'):
                advice.append(f"If you're at a {experience_level} level, here's some advice: {rule.get('advice', 'unknown')}")
            
            injury_history = rule.get('injury_history', 'unknown')
            if injury_history == user_input.get('injury_history'):
                advice.append(f"If you have a history of {injury_history}, consider: {rule.get('advice', 'unknown')}")

        return advice if advice else ['No specific advice found based on the provided information.']

    def get_all_advice(self):
        return [rule.get('advice', 'unknown') for rule in self.knowledge_base]
