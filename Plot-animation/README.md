# Matplotlib - Animation plot version

>Data 
- toyota car sale prediction history
- loss  and val loss values graph 

> RESULT
![ezgif com-gif-maker](https://user-images.githubusercontent.com/72845895/125196204-ed0c2c80-e293-11eb-8b6c-96e11f377dea.gif)

# How to make?
``` python
for i in range(1800): 
    x.append(history.index[i])
    y.append(history["loss"][i])
    k.append(history["val_loss"][i])
    
    if i % 5 ==0: # graph speed control params1
        plt.ylim(0,10)
        plt.xlim(0,1800)
        plt.xlabel("반복 시행 횟수")
        plt.ylabel("오차율 ")
        plt.plot(x, y , color="red", label="loss")
        plt.plot(x, k , color="blue", label="val_loss")
        plt.pause(0.001) # graph speed control params 2
plt.show()
```

