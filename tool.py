#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from rich.console import Console
console = Console()
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from heeletool import HeeleCompany

brand_name = "Heele"  # Название бренда
__CHANNEL_USERNAME__ = "HeeleBot"
__GROUP_USERNAME__   = "Heeletool"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = "HEELE\n"
    brand_name =  "       ██╗░░██╗███████╗███████╗██╗░░░░░███████╗\n" 
    brand_name += "       ██║░░██║██╔════╝██╔════╝██║░░░░░██╔════╝\n" 
    brand_name += "       ███████║█████╗░░█████╗░░██║░░░░░█████╗░░\n" 
    brand_name += "       ██╔══██║██╔══╝░░██╔══╝░░██║░░░░░██╔══╝░░\n" 
    brand_name += "       ██║░░██║███████╗███████╗███████╗███████╗\n" 
    brand_name += "       ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚══════╝\n" 
    colors = [
        "rgb(75,0,130)", "rgb(102,0,153)", "rgb(123,31,162)", "rgb(147,112,219)", "rgb(186,85,211)",  
        "rgb(216,191,216)", "rgb(221,160,221)", "rgb(238,130,238)", "rgb(255,0,255)", "rgb(153,50,204)",  
        "rgb(139,0,139)"
]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.purple_to_blue, '\t    ВЫЙДЕТЕ ИЗ АККАУНТА ПЕРЕД ИСПОЛЬЗОВАНИЕМ!'))
    print(Colorate.Horizontal(Colors.purple_to_blue, f'       𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺: @{__CHANNEL_USERNAME__} 𝐎𝐫 @{__GROUP_USERNAME__}'))
    print(Colorate.Horizontal(Colors.purple_to_blue, f' '))




def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.red_to_white, '==========[ PLAYER DETAILS ]=========='))
            
            print(Colorate.Horizontal(Colors.red_to_white, f'Имя   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.'))
                
            print(Colorate.Horizontal(Colors.red_to_white, f'ID: {data.get("localID")}.'))
            
            print(Colorate.Horizontal(Colors.red_to_white, f'Валюта  : {data.get("money")}.'))
            
            print(Colorate.Horizontal(Colors.red_to_white, f'Коины  : {data.get("coin")}.'))
            
        else:
            print(Colorate.Horizontal(Colors.rainbow, '! ОШИБКА: новые учетные записи должны быть авторизованы в игре хотя бы один раз!.'))
            exit(1)
    else:
        print(Colorate.Horizontal(Colors.rainbow, '! ОШИБКА: похоже, ваш логин установлен неправильно !.'))
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.red_to_white, '========[ ACCESS KEY DETAILS ]========'))
    
    print(Colorate.Horizontal(Colors.red_to_white, f'Ключ Активации : {data.get("access_key")}.'))
    
    print(Colorate.Horizontal(Colors.red_to_white, f'Telegram ID: {data.get("telegram_id")}.'))
    
    print(Colorate.Horizontal(Colors.red_to_white, f'Баланс $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.'))
    print(Colorate.Horizontal(Colors.red_to_white, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            print(Colorate.Horizontal(Colors.rainbow, f'{tag} cannot be empty or just spaces. Please try again.'))
        else:
            return value
            
#def load_client_details():
#    response = requests.get("http://ip-api.com/json")
#    data = response.json()
#    print(Colorate.Horizontal(Colors.red_to_white, '=============[ 𝐋𝐎𝐂𝐀𝐓𝐈𝐎𝐍 ]============='))
#    print(Colorate.Horizontal(Colors.red_to_white, f'Ip Адресс : {data.get("query")}.'))
#    print(Colorate.Horizontal(Colors.red_to_white, f'Локация   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.'))
 #   print(Colorate.Horizontal(Colors.red_to_white, f'Страна    : {data.get("country")} {data.get("zip")}.'))
#    print(Colorate.Horizontal(Colors.red_to_white, '===============[ 𝐌𝐄𝐍𝐔 ]==============='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Почта аккаунта[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Пароль аккаунта[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Ключ активации[/bold]", "Access Key", password=False)
        console.print("[bold cyan][%] Попытка войти[/bold cyan]: ", end=None)
        cpm = HeeleCompany(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                print(Colorate.Horizontal(Colors.rainbow, 'АККАУНТ НЕ НАЙДЕН.'))
                sleep(2)
                continue
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'НЕВЕРНЫЙ ПАРОЛЬ.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'НЕВЕРНЫЙ КЛЮЧ.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'ПОПРОБУЙТЕ ЕЩЕ РАЗ.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Примечание: убедитесь, что вы заполнили поля !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
#            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
            print(Colorate.Horizontal(Colors.red_to_white, '{01}: Накрутка валюты          1.5K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{02}: Накрутка коинов          4.5K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{03}: Кинг Ранг                8K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{04}: Сменить ID               4.5K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{05}: Сменить имя              100'))
            print(Colorate.Horizontal(Colors.red_to_white, '{06}: Сменить имя (rainbow)    100'))
            print(Colorate.Horizontal(Colors.red_to_white, '{07}: Номерные знаки           2K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{08}: Удалить Аккаунт          FREE'))
            print(Colorate.Horizontal(Colors.red_to_white, '{09}: Регистрация Аккаунта     FREE'))
            print(Colorate.Horizontal(Colors.red_to_white, '{10}: Удалить друзей           500'))
            print(Colorate.Horizontal(Colors.red_to_white, '{11}: Разбллок. донат авто     5k'))
            print(Colorate.Horizontal(Colors.red_to_white, '{12}: Разблок. все авто        6K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{13}: Разблок. миги            3.5K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{14}: Разблок. w16 мотор       4K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{15}: Разблок. все гудки       3K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{16}: Отключие урона авто      3K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{17}: Разблок. Бесконеч. бенз  3K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{18}: Разблок. 3 дома          4K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{19}: Разблок. цветной дым     4K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{20}: Разблок. диски           4K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{21}: Получить все анимации    2K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{22}: Разблок. Equipaments M   3K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{23}: Разблок. Equipaments F   3K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{24}: Изменить Race Win        1K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{25}: Изменить Race Loses      1K'))
            print(Colorate.Horizontal(Colors.red_to_white, '{26}: Клон Аккаунта            7K'))
         #   print(Colorate.Horizontal(Colors.red_to_white, '{27}: Глитч авто               2.5k'))
         #   print(Colorate.Horizontal(Colors.red_to_white, '{28}: Изм. выворота колеса     1.5k'))
            print(Colorate.Horizontal(Colors.red_to_white, '{0} : Exit'))
            
            print(Colorate.Horizontal(Colors.red_to_white, '===============[ 𝐂𝐏𝐌 ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Выберите услугу [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.red_to_white, '===============[ 𝐂𝐏𝐌 ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Укажите, сколько денег вы хотите.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Сохраняю процесс: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Введите необходимое количество коинов.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Сохраняю процесс: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Примичание:[/bold red]: если в игре не отображается звание короля, закройте ее и откройте несколько раз", end=None)
                console.print("[bold red][!] Примичание:[/bold red]: пожалуйста, не получайте King Rank на одном аккаунте дважды.", end=None)
                sleep(2)
                console.print("[%] Даю вам звание короля: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Введите свой новый ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Сохраняем процесс: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, попробуйте еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Вы ввели неправильный ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Введите ваше новое имя.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Сохраняем процесс: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, повторите еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, используйте действительные значения.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Введите свое новое Радужное Имя.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Сохраняем процесс: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти? ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, повторите еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, используйте действительные значения.'))
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Даем вам номерные знаки: ", end=None)
                if cpm.set_player_plates():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хоитите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Пожалуйста, повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                print(Colorate.Horizontal(Colors.rainbow, '[!] После удаления аккаунта пути назад не будет. !!.'))
                answ = Prompt.ask("[?] Вы хотите удалить аккаунт? ?!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                else: continue
            elif service == 9: # Account Register
                print(Colorate.Horizontal(Colors.rainbow, '[!] Регистрация нового аккаунта.'))
                acc2_email = prompt_valid_value("[?] Почта аккаунта", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Пароль аккаунта", "Password", password=False)
                console.print("[%] Создаю новый аккаунт: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    print(Colorate.Horizontal(Colors.rainbow, f'ИНФО: Настройте этот аккаунт с помощью HeeleTool'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Вы чаще всего входите в игру, используя эту учетную запись.'))
                    sleep(2)
                    continue
                elif status == 105:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Этот адрес электронной почты уже существует !.'))
                    sleep(2)
                    continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Удаляю ваших друзей: ", end=None)
                if cpm.delete_player_friends():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хоитите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Примечание: выполнение этой функции займет некоторое время, пожалуйста, не отменяйте ее..", end=None)
                console.print("[%] Разблокировка авто: ", end=None)
                if cpm.unlock_paid_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'Ошибка.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Выдаю вам авто: ", end=None)
                if cpm.unlock_all_cars():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Открываю сирены для всех авто: ", end=None)
                if cpm.unlock_all_cars_siren():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Открываю w16 мотор: ", end=None)
                if cpm.unlock_w16():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Открываю для вас гудки: ", end=None)
                if cpm.unlock_horns():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] ВЫ хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Убираю урон для ваших авто: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Делаю бесконечный бензин: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти? ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Открываю дома: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Открываю для вас цветной дым: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Открываю диски: ", end=None)
                if cpm.unlock_wheels():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Открываю все анимации: ", end=None)
                if cpm.unlock_animations():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Открываю Equipaments Male: ", end=None)
                if cpm.unlock_equipments_male():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Открываю Equipaments Female: ", end=None)
                if cpm.unlock_equipments_female():
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Укажите, сколько выигранных гонок пополнить.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Повторите еще раз.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Укажите правильное число.'))
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Укажите, сколько сделать проигрышев в гонках.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] Пожалуйста, повторите попытку.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Пожалуйста, дайте верное число.'))
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Пожалуйста, укажите данные аккаунта.'))
                to_email = prompt_valid_value("[?] Почта аккаунта", "Email", password=False)
                to_password = prompt_valid_value("[?] Пароль аккауанта", "Password", password=False)
                console.print("[%] Клонирование вашего аккаунта: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                        
                    print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Пожалуйста, вводите верные данные.'))
                    sleep(2)
                    continue
        #    elif service == 27:
        #        console.print("[bold yellow][!] Примечание[/bold yellow]: исходная скорость не может быть восстановлена!.")
        #        console.print("[bold cyan][!] Введите данные автомобиля.[/bold cyan]")
        #        car_id = IntPrompt.ask("[bold][?] Авто Id[/bold]")
        #        console.print("[bold cyan][%] Взлом скорости автомобиля[/bold cyan]:",end=None)
        #        if cpm.hack_car_speed(car_id):
        #            console.print("[bold green]УСПЕШНО (✔)[/bold green]")
        #            console.print("================================")
        #            answ = Prompt.ask("[?] Вы хотите выйти ?", choices=["y", "n"], default="n")
         #           if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Спасибо за использование нашего инструмента, присоединяйтесь к нашему каналу в Telegram: @{__CHANNEL_USERNAME__}.'))
        #            else: continue
        #        else:
        #            print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА.'))
       #             print(Colorate.Horizontal(Colors.rainbow, '[!] Пожалуйста, вводите правильные данные.'))
        #            sleep(2)
     #               continue
     #       elif service == 28: # ANGLE
     #           print(Colorate.Horizontal(Colors.rainbow, '[!] ВВЕДИТЕ ДАННЫЕ АВТО'))
     #           car_id = IntPrompt.ask("[red][?] АВТО ID[/red]")
     #           print(Colorate.Horizontal(Colors.rainbow, '[!] ВВЕДИТЕ УГОЛ ПОВОРОТА РУЛЕВОГО КОЛЕСА'))
     #           custom = IntPrompt.ask("[red][?]﻿ПРОЦЕСС[/red]")                
     #           console.print("[red][%] ВЗЛОМ УГЛА АВТО[/red]: ", end=None)
     #           if cpm.max_max1(car_id, custom):
     #               print(Colorate.Horizontal(Colors.rainbow, 'УСПЕШНО'))
     #               answ = Prompt.ask("[red][?] ВЫ ХОТИТЕ ВЫЙТИ?[/red] ?", choices=["y", "n"], default="n")
     #               if answ == "y": console.print("СПАСИБО ЗА ИСПОЛЬЗОВАНИЕ")
     #               else: continue
     #           else:
     #               print(Colorate.Horizontal(Colors.rainbow, 'ОШИБКА'))
     #               print(Colorate.Horizontal(Colors.rainbow, 'ПОВТОРИТЕ ЕЩЕ РАЗ'))
     #               sleep(2)
     #               continue                                        
     #       else: continue
            break
        break
            
        
            
              
