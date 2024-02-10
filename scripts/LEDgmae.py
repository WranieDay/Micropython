#example of an and (&&) bolean

from include.rcc_library import Raft

myraft = Raft()
age = 17

favcolor = "blue"

if favcolor == "blue" and age > 13:
    myraft.led_on()