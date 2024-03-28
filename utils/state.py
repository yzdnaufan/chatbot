from classes.state import ConversationState

class ConversationStateManager:
    """
    Manages the state of conversations for the chatbot.
    """

    def __init__(self):
        self.sessions = {}  # Stores session_id -> state

    def get_state(self, session_id):
        """
        Retrieves the state of a conversation session.

        Args:
            session_id (str): The ID of the conversation session.

        Returns:
            ConversationState: The state of the conversation session.
        """
        return self.sessions.get(session_id, ConversationState.INITIAL)

    def set_state(self, session_id, state: ConversationState):
        """
        Sets the state of a conversation session.

        Args:
            session_id (str): The ID of the conversation session.
            state (ConversationState): The state to set for the conversation session.
        """
        self.sessions[session_id] = state

    def reset_state(self, session_id):
        """
        Resets the state of a conversation session to the initial state.

        Args:
            session_id (str): The ID of the conversation session.
        """
        self.set_state(session_id, ConversationState.INITIAL)