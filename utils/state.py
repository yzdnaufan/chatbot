from classes.state import ConversationState

class ConversationStateManager:
    """
    Manages the state of conversations for the chatbot.
    """

    def __init__(self):
        self.states = {}  # Stores session_id -> state

    def get_state(self, session_id):
        """
        Retrieves the state of a conversation session.

        Args:
            session_id (str): The ID of the conversation session.

        Returns:
            ConversationState: The state of the conversation session.
        """
        # Check if session was available
        if session_id not in self.states:
            self.states[session_id] = ConversationState.INITIAL
            return ConversationState.INITIAL

        return self.states.get(session_id)

    def set_state(self, session_id, state: ConversationState):
        """
        Sets the state of a conversation session.

        Args:
            session_id (str): The ID of the conversation session.
            state (ConversationState): The state to set for the conversation session.
        """
        self.states[session_id] = state

    def reset_state(self, session_id):
        """
        Resets the state of a conversation session to the initial state.

        Args:
            session_id (str): The ID of the conversation session.
        """
        self.set_state(session_id, ConversationState.INITIAL)