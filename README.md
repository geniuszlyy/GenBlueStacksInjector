# EN
**GenBlueStacksInjector** is a tool designed to automate the deployment of payloads to startup directories in user profiles on systems running BlueStacks. This tool demonstrates potential security risks and aims to help in understanding how payloads can be programmatically injected.

### Note:
This project is related to CVE-2024-33352, a vulnerability in BlueStacks that allows unauthorized access to user directories, potentially leading to arbitrary code execution.

## Features
- **Automated Payload Deployment**: Automatically installs specified payloads into user startup directories.
- **User Enumeration**: Lists user profiles on the host system, excluding common system profiles.
- **Error Logging**: Provides detailed logs for monitoring and troubleshooting.

## Installation
To install and set up the project, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/geniuszlyy/GenBlueStacksInjector.git
   ```
2. Navigate into the directory:
   ```bash
   cd GenBlueStacksInjector
   ```
3. Open the project in your preferred Python environment.

## Usage
- **Configure the Payload**: Modify the payload to be deployed in the `inject_payload` method in `GenVuln_CVE2024_33352.py`.
- **Run the Script**: Execute the script using Python to deploy the payload.
- **Monitor Logs**: Check the generated `system_manager.log` file for logging information and error messages.

## Important Note
This exploit, known as **GenBlueStacksInjector**, should be used solely for educational purposes and security research. Unauthorized use on systems without explicit permission is illegal and unethical. Always seek consent and follow legal guidelines when testing or demonstrating vulnerabilities.

# RU
**GenBlueStacksInjector** -  это инструмент для автоматизации установки пейлоадов в директории автозагрузки в пользовательских профилях на системах с BlueStacks. Этот инструмент демонстрирует потенциальные риски безопасности и помогает понять, как программно внедряются пейлоады.

### Примечание
Этот проект связан с CVE-2024-33352, уязвимостью в BlueStacks, которая позволяет неавторизованный доступ к директориям пользователей, что может привести к выполнению произвольного кода.

## Функции
- **Автоматическая установка пейлоадов**: Автоматически устанавливает указанные пейлоады в директории автозагрузки пользователей.
- **Перечисление пользователей**: Выводит список профилей пользователей на хост-системе, исключая общие системные профили.
- **Логирование ошибок**: Предоставляет подробные логи для мониторинга и устранения неполадок.

## Установка
Для установки и настройки проекта выполните следующие шаги:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/geniuszlyy/GenBlueStacksInjector.git
   ```
2. Перейдите в директорию:
   ```bash
   cd GenBlueStacksInjector
   ```
3. Откройте проект в предпочитаемой среде разработки Python.
   
## Использование
- **Настройка пейлоада**: Измените пейлоад, который необходимо установить, в методе `inject_payload` в `GenVuln_CVE2024_33352.py`.
- **Запуск скрипта**: Запустите скрипт с помощью Python для развертывания пейлоада.
- **Мониторинг логов**: Проверьте файл `system_manager.log` для получения информации о логах и сообщениях об ошибках.

## ВАЖНО
Этот эксплойт, известный как **GenBlueStacksInjector**, должен использоваться только в учебных целях и для исследований безопасности. Несанкционированное использование на системах без явного разрешения незаконно и неэтично. Всегда получайте согласие и следуйте юридическим нормам при тестировании или демонстрации уязвимостей.
