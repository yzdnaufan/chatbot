class ContextManager:
    """
    A class that manages the context for a chatbot. The context is a dictionary that stores information 
    that the chatbot can use to maintain a conversation over multiple turns.
    """

    def __init__(self):
        """
        Initializes a new instance of the ContextManager class. The context is initially empty.
        """
        self.context = {}

    def get_context(self, key):
        """
        Retrieves a value from the context using the specified key.

        Args:
            key (str): The key to use to retrieve the value.

        Returns:
            The value associated with the specified key, or None if the key is not in the context.
        """
        return self.context.get(key)

    def set_context(self, key, value):
        """
        Sets a value in the context using the specified key.

        Args:
            key (str): The key to use to store the value.
            value: The value to store.
        """
        self.context[key] = value

    def clear_context(self):
        """
        Clears all values from the context, resetting it to an empty dictionary.
        """
        self.context = {}