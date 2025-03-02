import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

class ClickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.level = 0
        self.max_level = 4
        self.images = [
            "WhatsApp Image 2022-08-25 at 12.07.57.jpeg", 
            "IL1aEFka4po.jpg", 
            "channels4_profile.jpg", 
            "347216719729177.jpeg", 
            "bloger-boec-ashab-tamaev-nabrosilsya-na-hejtera-v-lobbi-moskva-siti_1697808918334691254.jpg"
        ]
        self.song_path = "Песня - Ахмед Ахмед Ахмедик догоняю иди сюда.mp3"  # Добавляем путь к аудиофайлу
        self.player = QMediaPlayer()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Симулятор Тамаева")
        self.setGeometry(100, 100, 400, 300)  # Увеличенный размер окна
        
        self.layout = QVBoxLayout()
        
        self.label = QLabel(self)
        self.update_label()
        self.layout.addWidget(self.label)
        
        self.image_label = QLabel(self)
        self.update_image()
        self.image_label.setScaledContents(True)
        self.image_label.setFixedSize(200, 150)  # Уменьшенный размер изображения
        self.layout.addWidget(self.image_label)
        
        self.button = QPushButton("изУэнэния", self)
        self.button.setFixedSize(150, 50)  # Увеличение кнопки
        self.button.clicked.connect(self.increase_score)
        self.layout.addWidget(self.button)
        
        self.setLayout(self.layout)
    
    def increase_score(self):
        self.score += 1
        self.update_label()
        
        if self.score >= (self.level + 1) * 10:
            self.offer_game()
    
    def offer_game(self):
        reply = QMessageBox.question(self, "Мини-игра", "Сыграть в ракетку?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.play_game()
    
    def play_game(self):
        cost = (self.level + 1) * 10
        if self.score < cost:
            QMessageBox.warning(self, "Ошибка", "Недостаточно очков для игры в ракетку!")
            return
        
        self.score -= cost  # Списываем очки
        
        if random.choice([True, False]):
            if self.level < self.max_level:
                self.level += 1
        else:
            if self.level > 0:
                self.level -= 1
        
        self.update_image()
        self.update_label()
        
        if self.level == self.max_level:
            self.end_game()
    
    def update_image(self):
        pixmap = QPixmap(self.images[self.level])
        self.image_label.setPixmap(pixmap)
    
    def update_label(self):
        self.label.setText(f"изУэнэния: {self.score}\nУровень: {self.level}")
    
    def end_game(self):
        self.label.setText("Забрал ракетку!")
        
        # Запуск музыки
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(self.song_path)))
        self.player.play()
        
        # Закрытие приложения через 10 секунд
        QTimer.singleShot(10000, self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickerApp()
    window.show()
    sys.exit(app.exec_())
