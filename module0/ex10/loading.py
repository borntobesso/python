import time

sleep_time = 0.005

def ft_progress(lst):
    total = len(lst)
    for i, item in enumerate(lst, 1):
        yield item
        progress = i * 100 // total
        print(f"ETA: {sleep_time * total:.2f}s [{progress:>3}%][{'=' * (progress // 5)}>{' ' * (20 - (progress // 5))}] {i}/{total} | elapsed time {sleep_time * i:.2f}s", end='\r')
        
        
listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(sleep_time)
print()
print(ret)