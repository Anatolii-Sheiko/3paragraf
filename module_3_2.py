
def send_email (message, recipient, *, sender="university.help@gmail.com"):
    boole = recipient.find ("@") >= 0 and recipient.endswiht((".com", ".ru", ".net")) and sender.find ("@") >= 0 and sender.endswiht((".com", ".ru", ".net"))

    if boole == False:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    if sender == recipient:
        print("Нельзя отправить письмо ссамому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправленно с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТЫЙ ОТПРАВИТЕЛЬ! Письмо отправленно с адреса {sender} на адрес {recipient}')
        return

    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
