"""
Создай свою собственную игру на основе пройденного материала.
"""
import time
from multiprocessing import Process, Value
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

False
def timer(mc, coins):
    t = 60
    mc.postToChat("Найдите и уничтожте 10 ветящихся блоков за 1 минуту!")
    time.sleep(2)
    mc.postToChat("Рядом с вами появилось 12 новых предметов в случайных местах!")
    time.sleep(2)
    mc.postToChat("Время пошло!")
    while t != 0:
        time.sleep(1)
        mc.postToChat("Осталось - " + str(t) + " секунд!")
        print("Осталось - " + str(t) + " секунд!")
        t -= 1
        print(coins.value)
        if coins.value == 10:
            mc.postToChat("ПОЗДРАВЛЯЮ ВЫ ВЫЙГРАЛИ!!!")
            break
    else:
        time.sleep(1)
        print("Время вышло! Вы проиграли!!!")
        mc.postToChat("Время вышло! Вы проиграли!!!")


def def_coins(mc, coins):
    while True:
        blockEvents = mc.events.pollBlockHits()
        for blockEvent in blockEvents:
            blockType = mc.getBlock(blockEvent.pos)

            if blockType == 89:
                mc.setBlock(blockEvent.pos, 0)
                coins.value += 1
                mc.postToChat("+1!   Всего: " + str(coins.value))


def create_block(mc):
    time.sleep(3)
    pos = mc.player.getTilePos()  # x y z
    for i in range(12):
        # mc.setBlock(pos.x + random.randint(-20, 20), pos.y, pos.z + random.randint(-20, 20), block.CACTUS.id)
        mc.setBlock(pos.x + random.randint(-20, 20), pos.y + 1, pos.z + random.randint(-20, 20),
                    block.GLOWSTONE_BLOCK.id)


if __name__ == '__main__':
    coins = Value('i', 0)
    mc = minecraft.Minecraft.create()
    time.sleep(30)
    process_timer = Process(target=timer, args=(mc, coins,))
    process_coins = Process(target=def_coins, args=(mc, coins,))
    process_block = Process(target=create_block, args=(mc,))

    process_block.start()
    process_timer.start()
    process_coins.start()

    process_block.join()
    process_timer.join()
    process_coins.terminate()
