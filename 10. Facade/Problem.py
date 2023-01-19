from unittest.mock import Mock


def send_message(sender_id, recipient_id, message_text, user_database, message_queue, notification_service):
    if not user_database.user_exists(sender_id):
        raise Exception("Sender does not exist")
    if not user_database.user_exists(recipient_id):
        raise Exception("Recipient does not exist")
    message_id = message_queue.enqueue_message(sender_id, recipient_id, message_text)
    notification_service.send_notification(recipient_id, "You have a new message")
    return message_id


if __name__ == "__main__":
    user_database = Mock()
    user_database.user_exists.return_value = True
    message_queue = Mock()
    message_queue.enqueue_message.return_value = 123
    notification_service = Mock()
    message_id = send_message(1, 2, "Hello", user_database, message_queue, notification_service)
    print(message_id)