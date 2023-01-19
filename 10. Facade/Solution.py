from unittest.mock import Mock


class MessagingFacade:
    def __init__(self, user_database, message_queue, notification_service):
        self._user_database = user_database
        self._message_queue = message_queue
        self._notification_service = notification_service

    def send_message(self, sender_id, recipient_id, message_text):
        if not self._user_database.user_exists(sender_id):
            raise ValueError("Sender does not exist")
        if not self._user_database.user_exists(recipient_id):
            raise ValueError("Recipient does not exist")
        message_id = self._message_queue.enqueue_message(sender_id, recipient_id, message_text)
        self._notification_service.send_notification(recipient_id, "You have a new message")
        return message_id

    def read_message(self, user_id, message_id):
        """
        Returns the text of a message for a given user and message id
        """
        return self._message_queue.get_message_text(user_id, message_id)

    def delete_message(self, user_id, message_id):
        """
        Deletes a message for a given user and message id
        """
        self._message_queue.delete_message(user_id, message_id)

    def list_messages(self, user_id):
        """
        Returns a list of messages for a given user
        """
        return self._message_queue.list_messages(user_id)

    def add_user(self, user_id, user_name):
        """
        Add user to the user_database
        """
        self._user_database.add_user(user_id, user_name)


if __name__ == "__main__":
    user_database = Mock()
    user_database.user_exists.return_value = True
    message_queue = Mock()
    message_queue.enqueue_message.return_value = 123
    notification_service = Mock()
    facade = MessagingFacade(user_database, message_queue, notification_service)
    message_id = facade.send_message(1, 2, "Hello")
    print(message_id)
