from rich import print
import os
import psutil
import time

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
[green]1 - показать ето сообшение
2 - показать нагрузку на пк
3 - показть информацыю о системе
4 - открыть файл
5 - закрыть процесс
6 - показать запушеные процессы
7 - очистить ненужные файлы(очишяет временные файлs temp)
8 - проверка соиденения
9 - выключение пк через время
10 - зайти в биос(пока отключено и недоделано)
[/green]
"""
while True:
    os.system("cls")

    print(text)
    number = input("ведите номер оперыции: ")
    if number == "1":
        print("")
    elif number == "2":
        print("выводим...")
        print("ето может занять некоторое время")
        cpu = int(psutil.cpu_percent(interval=1))

        memory = int(psutil.virtual_memory().percent)

        net_start = psutil.net_io_counters()
        time.sleep(1)
        net_end = psutil.net_io_counters()

        network = (net_end.bytes_recv - net_start.bytes_recv) + (net_end.bytes_sent - net_start.bytes_sent)
        memory2 = int(psutil.virtual_memory().available / (1024 * 1024))

        print(f"твоя нагрузка цп: [green]{cpu}%[/green]")
        print(f"твоя нагрузка оперативной памяти: [green]{memory}%[/green]")
        print(f"твоя нагрузка интернет: [green]{network} B/s[/green]")
        print(f"свободное место на диске: [green]{memory2} мегабайт[/green]")
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "3":
        print("выводим...")
        system_info = os.system("systeminfo")
        print(f"{system_info}")
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "4":
        file = input("ведите путь к файлу или папке(без \" или \'): ")
        if '"' in file or "'" in file:
            print("[red]EROR путь содержит \" или \' файл не был открыт[/red]")
            input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
        else:
            print(f"открываем файл по пути {file}")
            os.system(f"start {file}")
            input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "5":
        process = input("вседите название процеса который нужно закрыть(без \" и \'): ")
        if '"' in process or "'" in process:
            print("[red]EROR в названии содержится \" или \' файл не был закрыт[/red]")
            input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
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
                input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
            elif Y_N == "N":
                print("отменяем")
                input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
            else:
                input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "6":
        os.system("tasklist")
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "7":
        print("очищаем мусор и освобождаем место на диске...")
        os.system(r'del /q /f /s "C:\Windows\Temp\*.*" 2>nul')
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "8":
        ping = input("введите айпи: ")
        os.system(f"ping -n 4 -w 1500 {ping}")
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    elif number == "9":
        time_shutdown = int(input("укажите время в минутах: "))
        time_shutdown = time_shutdown * 60

        Y_N2 = input("подтверди выключение введите Y для продолжения N для отмены: ")
        if Y_N2 != "Y":
            print("отмена")
            os.system(f"shutdown /a")
        else:
            os.system(f"shutdown /s /t {time_shutdown}")

        time_shutdown = time_shutdown / 60
        for i in range(int(time_shutdown)):
            time_shutdown = time_shutdown - 1
            time.sleep(60)
            print(f"компютер выключится через: [green]{time_shutdown} минут[/green], не закрываейте програму")
    elif number == "10":
        print('пока не работает')
         # print("компютер перезагрузится и зайдет в биос чрез 5 секунд")
         # os.system("shutdown /r /o /t 0 5")
         # input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
    else:
        print("[red]EROR вы указали не число или число больше чем нужно[/red]")
        input("\n\n\nнажмите ENTER что бы перезапустить хелпер")
