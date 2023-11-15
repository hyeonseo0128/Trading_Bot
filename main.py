import pyautogui as pg
import pyscreeze
import time
import yaml
import subprocess
import telegram
import asyncio
import gspread
import mss
# import datetime

PASSWORD = ""
ORDER_STOCK = ""
TELEGRAM_TOKEN = ""
TELEGRAM_CHAT_ID = ""
QUANTITY_UNIT = ""

bot = ""
chat_id = ""


def init():
    global PASSWORD
    global ORDER_STOCK
    global TELEGRAM_TOKEN
    global TELEGRAM_CHAT_ID
    global QUANTITY_UNIT
    global bot
    global chat_id

    try:
        with open("./info.yaml", "r") as f:
            config = yaml.full_load(f)
            PASSWORD = config["PASSWORD"]
            ORDER_STOCK = config["ORDER_STOCK"]
            TELEGRAM_TOKEN = config["TELEGRAM_TOKEN"]
            TELEGRAM_CHAT_ID = config["TELEGRAM_CHAT_ID"]
            QUANTITY_UNIT = config["QUANTITY_UNIT"]

        bot = telegram.Bot(token=TELEGRAM_TOKEN)
        chat_id = TELEGRAM_CHAT_ID
    except Exception:
        print("Does not exist config.yaml")


# async def messageBot(message):
#     await bot.sendMessage(chat_id=chat_id, text=message)


def toLogin():
    subprocess.Popen(["C:\\KiwoomGlobal\\bin\\NFStarter.exe"])  # run program
    time.sleep(3)

    # with mss.mss() as sct:  # Screen Capture
    #     sct.shot(mon=1, output='run_program.png')
    #     print('Captured!')

    try:  # find certificate button
        certificateBtn = pyscreeze.locateOnScreen('./image/certificateLogin.png')
    except:
        certificateBtn = pyscreeze.locateOnScreen('./image/certificateLogin2.png')

    pg.moveTo(certificateBtn.left + certificateBtn.width / 2,
              certificateBtn.top + certificateBtn.height / 2)
    pg.click()

    try:  # find login button
        certificateLoginBtn = pyscreeze.locateOnScreen('./image/loginBtn.png')
    except:
        certificateLoginBtn = pyscreeze.locateOnScreen('./image/loginBtn2.png')

    pg.moveTo(certificateLoginBtn.left + certificateLoginBtn.width / 2,
              certificateLoginBtn.top + certificateLoginBtn.height / 2)
    pg.click()
    pg.write(PASSWORD)  # input password

    time.sleep(2)

    doneBtn = pyscreeze.locateOnScreen('./image/done.png')
    pg.moveTo(doneBtn.left + doneBtn.width / 2,
              doneBtn.top + doneBtn.height / 2)
    pg.click()
    time.sleep(10)
    # bot.sendMessage(chat_id=chat_id, text="장 시작")
    asyncio.run(bot.sendMessage(chat_id=chat_id, text="장 시작"))


def openOrderWindow():
    searchTap = pyscreeze.locateOnScreen('./image/serchTap.png')
    pg.moveTo(searchTap.left + searchTap.width / 3,
              searchTap.top + searchTap.height / 3)
    pg.click()
    pg.write(ORDER_STOCK)
    time.sleep(2)


def toExit():
    exitBtn = pyscreeze.locateOnScreen('./image/exitBtn.png')
    pg.moveTo(exitBtn.left + exitBtn.width / 2,
              exitBtn.top + exitBtn.height / 2)
    pg.click()
    time.sleep(0.5)

    exitDoneBtn = pyscreeze.locateOnScreen('./image/exitDone.png')
    pg.moveTo(exitDoneBtn.left + exitDoneBtn.width / 2,
              exitDoneBtn.top + exitDoneBtn.height / 2)
    pg.click()


def buyStock():
    buyStockTap = pyscreeze.locateOnScreen('./image/buyStockTap.png')
    pg.moveTo(buyStockTap.left + buyStockTap.width / 2,
              buyStockTap.top + buyStockTap.height / 2)
    pg.click()

    inputBuyQuantity = pyscreeze.locateOnScreen('./image/buyQuantity.png')
    pg.moveTo(inputBuyQuantity.left + inputBuyQuantity.width / 2,
              inputBuyQuantity.top + inputBuyQuantity.height / 2)
    pg.click()
    pg.write(QUANTITY_UNIT)

    inputBuyPrice = pyscreeze.locateOnScreen('./image/buyPrice.png')
    pg.moveTo(inputBuyPrice.left + inputBuyPrice.width,
              inputBuyPrice.top + inputBuyPrice.height / 2)
    pg.click()
    pg.write("20.00")

    clickBuyBtn = pyscreeze.locateOnScreen('./image/buyStockBtn.png')
    pg.moveTo(clickBuyBtn.left + clickBuyBtn.width / 2,
              clickBuyBtn.top + clickBuyBtn.height / 2)
    pg.click()

    buyDoneBtn = pyscreeze.locateOnScreen('./image/buyDone.png')
    pg.moveTo(buyDoneBtn.left + buyDoneBtn.width / 2,
              buyDoneBtn.top + buyDoneBtn.height / 2)
    pg.click()

    time.sleep(0.5)


def sellStock():
    sellStockTap = pyscreeze.locateOnScreen('./image/sellStockTap.png')
    pg.moveTo(sellStockTap.left + sellStockTap.width / 2,
              sellStockTap.top + sellStockTap.height / 2)
    pg.click()

    inputSellQuantity = pyscreeze.locateOnScreen('./image/sellQuantity.png')
    pg.moveTo(inputSellQuantity.left + inputSellQuantity.width / 2,
              inputSellQuantity.top + inputSellQuantity.height / 2)
    pg.click()
    pg.write(QUANTITY_UNIT)

    inputSellPrice = pyscreeze.locateOnScreen('./image/sellPrice.png')
    pg.moveTo(inputSellPrice.left + inputSellPrice.width,
              inputSellPrice.top + inputSellPrice.height / 2)
    pg.click()
    pg.write("25.00")

    clickSellBtn = pyscreeze.locateOnScreen('./image/sellStockBtn.png')
    pg.moveTo(clickSellBtn.left + clickSellBtn.width / 2,
              clickSellBtn.top + clickSellBtn.height / 2)
    pg.click()

    sellDoneBtn = pyscreeze.locateOnScreen('./image/sellDone.png')
    pg.moveTo(sellDoneBtn.left + sellDoneBtn.width / 2,
              sellDoneBtn.top + sellDoneBtn.height / 2)
    pg.click()


def main():
    toLogin()
    openOrderWindow()

    # buyStock()
    # sellStock()
    toExit()


if __name__ == "__main__":
    init()
    main()
