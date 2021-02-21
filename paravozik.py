# made by @Ilya_Kozyrev14 
 
 
from time import sleep 
from userbot.events import register 
 
 
@register(outgoing=True, pattern='^.paravozik(?: |$)(.*)') 
async def typewriter(typew): 
    await typew.edit("Хахахахаха") 
    sleep(1) 
    await typew.edit("...") 
    number = 1 
    await typew.edit(str(number) + "🚂 я как") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂  паравозик") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂   томас") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂   иди нахуй хуйсос") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂   не ебу причём тут паравоз") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂  может потомучто") 
    number = number + 1 
    sleep(1) 
    await typew.edit(str(number) + "🚂   я дебил ебучий")
