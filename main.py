import asyncio 
import logging

from colorama import Fore, Style,init

from tgbot.loader import bot
from tgbot.handlers import dp

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    
    logging.debug('Launching the bot...')
    await dp.start_polling(bot)

if __name__ == '__main__':
    init()

    print(f""" {Fore.RED + Style.BRIGHT}
        ██╗░░██╗██╗░░░██╗███╗░░██╗██╗░░░██╗██╗░░██╗
        ╚██╗██╔╝██║░░░██║████╗░██║██║░░░██║╚██╗██╔╝
        ░╚███╔╝░╚██╗░██╔╝██╔██╗██║╚██╗░██╔╝░╚███╔╝░
        ░██╔██╗░░╚████╔╝░██║╚████║░╚████╔╝░░██╔██╗░
        ██╔╝╚██╗░░╚██╔╝░░██║░╚███║░░╚██╔╝░░██╔╝╚██╗
        ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝ {Fore.YELLOW}
        
        ░█████╗░░█████╗░██████╗░███████╗██████╗░
        ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
        ██║░░╚═╝██║░░██║██║░░██║█████╗░░██████╔╝
        ██║░░██╗██║░░██║██║░░██║██╔══╝░░██╔══██╗
        ╚█████╔╝╚█████╔╝██████╔╝███████╗██║░░██║ {Fore.RESET}

        Telegram: @VHVH00
        Topic: https://zelenka.guru/threads/5872770/ {Style.RESET_ALL}
        """)

    asyncio.run(main())
    logging.info('Bot has stopped')
