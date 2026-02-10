from abc import ABC, abstractmethod


class UserAccount:
    def __init__(self, username, balance, password):
        self.username = username
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password

    def reset_password(self, old_password, new_password):
        if self.__password == old_password:
            self.__password = new_password
            return True
        return False

    def get_balance(self):
        return self._balance


class NotificationService(ABC):
    @abstractmethod
    def send_to_phone(self, phone, message):
        pass

    @abstractmethod
    def send_to_email(self, email, message):
        pass


class JsonNotification(NotificationService):
    def send_to_phone(self, phone, message):
        return {
            "channel": "SMS",
            "phone": phone,
            "message": message
        }

    def send_to_email(self, email, message):
        return {
            "channel": "EMAIL",
            "email": email,
            "message": message
        }


class XmlNotification(NotificationService):
    def send_to_phone(self, phone, message):
        return f"<sms><phone>{phone}</phone><text>{message}</text></sms>"

    def send_to_email(self, email, message):
        return f"<email><to>{email}</to><text>{message}</text></email>"


user = UserAccount("admin", 1000, "1234")

print(user.username)
print(user.get_balance())
print(user.login("1234"))
print(user.reset_password("1234", "5678"))
print(user.login("5678"))

json_service = JsonNotification()
xml_service = XmlNotification()

print(json_service.send_to_phone("+996777123456", "Код: 1234"))
print(json_service.send_to_email("test@mail.com", "Добро пожаловать"))

print(xml_service.send_to_phone("+79991234567", "Код: 5678"))
print(xml_service.send_to_email("admin@mail.com", "Уведомление"))
