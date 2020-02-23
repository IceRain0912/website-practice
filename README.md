# 網頁練習~

##介紹

![艾蕾]
(https://a-static.besthdwallpaper.com/ming-yun-da-ding-dan-lin-tohsaka-ai-lie-shi-ji-jia-le-qiangzhi-tw-2560x1600-17570_7.jpg)

[凜](https://lh3.googleusercontent.com/proxy/kakFIcNxc7M0dCkbMFxHPhGjQGyTwJfPOaphF9sDuYhvN5x7LBkGVr6LJ0RlXx-BIDRGfkIQL8EHtkvXsAxWuQO2yvnJPlu238rRb5pb1bY)

this is my first webpage practice!!


```python
def buyticket():
    lottery = set()
    while len(lottery) < 6:
        n = random.randint(1, 49)
        lottery.add(n)
    return lottery

prize = buyticket()
print("五星號碼:", prize)
times = 0
my = buyticket()
while len(prize & my) <= 4:
  my = buyticket()
  print("你的五星券:", my)
  times = times + 1

win = prize & my
print("中獎號碼:", win)

print("聖晶石數:", times)
print("總價:", times*30)
```



