import socket
import time # Не забываем импортировать time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

HOST = '192.168.1.6'
PORT = 65432

class SteppedSliderApp(App):
    # Добавляем атрибут для хранения объекта сокета
    client_socket = None 

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text='Текущее значение: 50', size_hint_y=0.2)
        
        self.slider = Slider(
            min=0, max=100, value=50, step=1
        )

        # Привязываем функцию обновления метки И отправки данных
        self.slider.bind(value=self.on_value_change)

        layout.add_widget(self.label)
        layout.add_widget(self.slider)

        # Инициализируем соединение с сервером при запуске GUI
        self.connect_to_server()

        return layout

    def connect_to_server(self):
        """Устанавливает соединение с сервером."""
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
            print(f"[*] Подключено к серверу {HOST}:{PORT}")
        except socket.error as e:
            print(f"[-] Ошибка подключения к серверу: {e}")
            self.label.text = "Ошибка подключения к серверу!"

    def on_value_change(self, instance, value):
        """Обновляет метку и отправляет новое значение на сервер."""
        # 1. Обновляем интерфейс Kivy
        self.label.text = f'Текущее значение: {int(value)}'
        
        # 2. Отправляем данные на сервер, если подключены
        if self.client_socket:
            try:
                # Преобразуем числовое значение в строку, затем в байты
                message = str(int(value))
                self.client_socket.sendall(message.encode('utf-8'))
                print(f"[*] Отправлено значение: {message}")
                
                # (Необязательно) Получаем ответ от сервера
                # data = self.client_socket.recv(1024)
                # print(f"[+] Ответ сервера: {data.decode('utf-8')}")

            except socket.error as e:
                print(f"[-] Ошибка отправки данных: {e}")
                self.label.text = "Ошибка отправки данных!"

    def on_stop(self):
        """Закрывает сокет при закрытии приложения."""
        if self.client_socket:
            self.client_socket.close()
            print("[*] Соединение закрыто.")


if __name__ == '__main__':
    SteppedSliderApp().run()
