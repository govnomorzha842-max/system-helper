#       привет это информацыя о проекте если ты это читаешь
#    значит ты либо получил исходник либо открил ехе файл как ру
#  в любо случаи тебе интересно что тут так что смотри если хочешь
# текушая версия: 1.1.4
# статус обновления: завершонное
# баги/недочет: нету
# последнее обновление: фикс 4, и оформление через "from rich.panel import Panel"

from rich import print
import os
import psutil
import time
from rich.panel import Panel

os.system("chcp 65001")

text = f"""[green]
╔══════════════════════════════════════════════════════════════╗
║  ██████╗  ██╗   ██╗  ███████╗ ████████╗ ███████╗ ███╗   ███╗ ║
║ ██╔════╝  ╚██╗ ██╔╝  ██╔════╝ ╚══██╔══╝ ██╔════╝ ████╗ ████║ ║
║ ╚█████╗    ╚████╔╝   ███████╗    ██║    █████╗   ██╔████╔██║ ║
║   ╚═══██╗   ╚██╔╝    ╚════██║    ██║    ██╔══╝   ██║╚██╔╝██║ ║
║  ██████╔╝    ██║     ███████║    ██║    ███████╗ ██║ ╚═╝ ██║ ║
║  ╚═════╝     ╚═╝     ╚══════╝    ╚═╝    ╚══════╝ ╚═╝     ╚═╝ ║
║                                                              ║
║     ██╗  ██╗ ███████╗ ██╗      ██████╗  ███████╗ ██████╗     ║ 
║     ██║  ██║ ██╔════╝ ██║      ██╔══██╗ ██╔════╝ ██╔══██╗    ║
║     ███████║ █████╗   ██║      ██████╔╝ █████╗   ██████╔╝    ║
║     ██╔══██║ ██╔══╝   ██║      ██╔═══╝  ██╔══╝   ██╔══██╗    ║
║     ██║  ██║ ███████╗ ███████╗ ██║      ███████╗ ██║  ██║    ║
║     ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ╚═╝      ╚══════╝ ╚═╝  ╚═╝    ║
╚══════════════════════════════════════════════════════════════╝[/green]
[yellow]примечание большинство функцый не работает для linux, mac os
примечание скрипт нужно запускать от имени админа[/yellow]
[green]1 - показать это сообшение
2 - показать нагрузку на пк
3 - показать комплектующие
4 - выключение пк через время
5 - показть информацыю о системе
6 - проверка соиденения
7 - открыть файл
8 - показать запушеные процессы
9 - закрыть процесс
10 - очистить ненужные файлы
11 - зайти в биос(пока не работает)
[/green]
"""
def ending_command():
    print("\n\n\n[yellow]нажмите ENTER что бы открыть стартовое меню[/yellow]")
    input("")

os.system("cls")
while True:
    print(text)
    number = input("ведите номер оперыции: ")
    if number == "1":
        print("")
    elif number == "2":
        # нагрузка
        # помогал с функцией ии
        print("выводим...")
        cpu = int(psutil.cpu_percent(interval=1))
        ram = int(psutil.virtual_memory().percent)

        net_start = psutil.net_io_counters()
        time.sleep(1)
        net_end = psutil.net_io_counters()

        net_recv = round((net_end.bytes_recv - net_start.bytes_recv) / 1024, 1)  # КБ/с
        net_sent = round((net_end.bytes_sent - net_start.bytes_sent) / 1024, 1)  # КБ/с

        disk_free = round(psutil.disk_usage("C:\\").free / (1024 ** 3), 1)  # ГБ

        print(f"Загрузка ЦП: [green]{cpu}%[/green]")
        print(f"Загрузка ОЗУ: [green]{ram}%[/green]")
        print(f"Сетевой трафик: [green]↓ {net_recv} KB/s | ↑ {net_sent} KB/s[/green]")
        print(f"Свободно на диске C: [green]{disk_free} GB[/green]")
        
        ending_command()
    elif number == "3":
        # вывод комплектуюших
        # помогал с функцией ии
        print("выводим...")
        def show_hardware():
            # Получаем нормальное имя процессора через PowerShell
            cpu_cmd = 'powershell -Command "(Get-CimInstance Win32_Processor).Name"'
            cpu = os.popen(cpu_cmd).read().strip()

            # Видеокарта
            gpu_cmd = 'powershell -Command "(Get-CimInstance Win32_VideoController).Name"'
            gpu = os.popen(gpu_cmd).read().strip()

            # Оперативная память
            ram = round(psutil.virtual_memory().total / (1024 ** 3), 1)

            # Диски
            disk_cmd = 'powershell -Command "(Get-CimInstance Win32_DiskDrive).Model"'
            disks_raw = os.popen(disk_cmd).read().strip()
            disks_list = disks_raw.split('\n')
            disks_fmt = "\n  • ".join([d.strip() for d in disks_list if d.strip()])

            # Вывод
            text = (
                f"[bold cyan]Процессор:[/bold cyan] {cpu}\n"
                f"[bold cyan]Видеокарта:[/bold cyan] {gpu}\n"
                f"[bold cyan]Оперативная память:[/bold cyan] {ram} ГБ\n"
                f"[bold cyan]Диски:[/bold cyan]\n  • {disks_fmt}"
            )

            print(Panel(text, title="[bold green]Характеристики ПК[/bold green]", expand=False))

            ending_command()

        show_hardware()
    elif number == "4":
        # отключение пк
        try:
            time_shutdown = int(input("укажите время в минутах: "))
            time_shutdown = time_shutdown * 60

            Y_N2 = input("подтверди выключение введите Y для продолжения N для отмены: ")
            if Y_N2 != "Y":
                print("отмена")
                os.system("shutdown /a")
                ending_command()
            else:
                os.system("shutdown /a")
                os.system(f"shutdown /s /t {int(time_shutdown)}")
                time_shutdown = time_shutdown / 60
                for i in range(int(time_shutdown), 0, -1):
                    print(f"компютер выключится через: [green]{i} минут[/green], не закрываейте програму")
                    time.sleep(60)
        except ValueError:
            print("[red]EROR это не число[/red]")
            ending_command()

    elif number == "5":
        # информация о системе
        print("выводим...")
        system_info = os.popen("systeminfo").read().strip()
        print(Panel(
            system_info,
            title="[bold green]Информация о системе[/bold green]",
            expand=False,
            border_style="cyan"
        ))
        ending_command()

    elif number == "6":
        # команда пинг
        ping = input("введите айпи: ")
        os.system(f"ping -n 4 -w 1500 {ping}")
        ending_command()

    elif number == "7":
        # открытие файла
        file = input("ведите путь к файлу или папке(без \" или \'): ")
        if '"' in file or "'" in file:
            print("[red]ERROR: путь содержит \" или \' файл не был открыт[/red]")
            ending_command()
        else:
            print(f"открываем файл по пути {file}")
            os.system(f"start {file}")
            ending_command()

    elif number == "8":
        # вывод процесов
        tasklist = os.popen('tasklist /FI "STATUS eq RUNNING"').read().strip()
        print(Panel(
            tasklist,
            title="[bold green]Запущенные процессы[/bold green]",
            expand=False,
            border_style="cyan"
        ))

        ending_command()

    elif number == "9":
        # закрытие
        process = input("вседите название процеса который нужно закрыть(без \" и \'): ")
        if '"' in process or "'" in process:
            print("[red]EROR в названии содержится \" или \' файл не был закрыт[/red]")
            ending_command()
        else:
            Y_N = input("введите Y для продолжения N для отмены: ")
            if Y_N == "Y":
                print("закрываем через 3")
                time.sleep(1)
                print("закрываем через 2")
                time.sleep(1)
                print("закрываем через 1")
                time.sleep(1)
                print(f"процесс под названием {process} был успешно закрыт")
                os.system(f"taskkill /F /IM {process}")
                ending_command()
            elif Y_N == "N":
                print("отменяем")
                ending_command()
            else:
                ending_command()
    elif number == "10":
        # очистка
        folders_del = [
            os.path.expandvars(r"C:\Windows\Temp"),
            os.path.expandvars(r"%TEMP%"),
            os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache"),
            os.path.expandvars(r"%LOCALAPPDATA%\Opera Software\Opera Stable\Cache"),
            os.path.expandvars(r"%LOCALAPPDATA%\Opera Software\Opera GX Stable\Cache"),
            os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache")
        ]

        print("удаляем мусор...")
        for path in folders_del:
            fullpath = os.path.join(path, "*.*")
            os.system(f'del /q /f /s "{fullpath}"')

        print("[green]готово[/green]")
        ending_command()
    else:
        print("[red]ERROR: вы указали не число или число больше чем нужно[/red]")
        ending_command()
