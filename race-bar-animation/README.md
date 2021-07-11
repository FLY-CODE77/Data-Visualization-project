# RACE-BAR-CHART
Very usefull tool when you showing rank chart

> Result


- data : mobile application rank data

## Requirement?
> bar-chart moduel 
- pip install bar-chart-race 
- conda install -c conda-forge bar_chart_race
> ffmpeg (for saving mp4 file)
- conda install -c conda-forge ffmpeg (ubuntu)
- brew install ffmpeg (mac)

# How to use?
1. make data frame like this 

<img width="712" alt="스크린샷 2021-07-11 오후 11 02 20" src="https://user-images.githubusercontent.com/72845895/125198750-2b0e4e00-e29e-11eb-938c-387121a8a608.png">

---
2. use race_bar_chart moduel
```python 
import bar_chart_race as bcr
bcr.bar_chart_race(df = data, 
                   n_bars = 6, 
                   sort='desc',
                   title='mobile',
                   filename = 'mobile.mp4')
print("bar-race is ready")
```
