
class SessionManager:
    """
    A class that manages sessions and session data.

    Attributes:
        sessions (list): A list of session dictionaries.
        session_data_history (list): A list of all session data.

    Methods:
        create_session(session_id): Creates a new session with the given session ID.
        add_data_to_session(session_id, data): Adds data to the specified session.
        get_session(session_id): Retrieves the session with the specified session ID.
        get_session_data_history(): Retrieves the session data history.
    """

    def __init__(self):
        self.sessions = []
        self.session_data_history = []

    def create_session(self, session_id):
        """
        Creates a new session with the given session ID.

        Args:
            session_id (str): The ID of the session.
        """
        session = {str(session_id): {
            'data': [

            ]}
        }
        self.sessions.append(session)

    def add_data_to_session(self, session_id, data):
        """
        Adds data to the specified session.

        Args:
            session_id (str): The ID of the session.
            data (any): The data to be added to the session.
        """
        session = self.get_session(session_id)
        if session:
            session['data'].append(data)
            self.session_data_history.append(data)

    def get_session(self, session_id):
        """
        Retrieves the session with the specified session ID.

        Args:
            session_id (str): The ID of the session.

        Returns:
            dict or None: The session dictionary if found, None otherwise.
        """
        for session in self.sessions:
            if session['session_id'] == session_id:
                return session
        return None

    def get_session_data_history(self):
        """
        Retrieves the session data history.

        Returns:
            list: The list of all session data.
        """
        return self.session_data_history
    
    def set_session_ended(self):
        """
        Sets the session as ended.
        """
        self.session_ended = True