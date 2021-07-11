# Korean font-manager for python

### why use make?
- When using korean font in your project
- We should designate font paths
- But when different os need different path 
- So it is so uncomfortable process
- It can save our time when you make universial korean font path manager 

> Before and After

<img width="431" alt="스크린샷 2021-07-11 오후 10 22 23" src="https://user-images.githubusercontent.com/72845895/125196936-a8ce5b80-e296-11eb-846b-bb6bda1b79d4.png"><img width="427" alt="스크린샷 2021-07-11 오후 10 34 13" src="https://user-images.githubusercontent.com/72845895/125197345-33638a80-e298-11eb-8f92-70f17aad1204.png">



# How to make?
```python
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
# when using korean fonts, minus font sometimes break so set rcParmas
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Linux':
    rc('font', family='NanumBarunGothic')
else:
    print('Unknown system... sorry~~'
```
> this version support windows and mac and ubuntu

---
