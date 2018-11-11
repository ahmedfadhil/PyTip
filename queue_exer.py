from queue import LifoQueue

stacking = LifoQueue()
stacking.put("cat")
stacking.put("dog")
stacking.put("cow")
stacking.put("bird")

print(stacking.qsize())
print(stacking.queue)
stacking.get()
stacking.empty()