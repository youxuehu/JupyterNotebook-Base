# -*- coding:utf-8 -*-
import pyttsx3

engine = pyttsx3.init() #初始化语音引擎
engine.setProperty('rate', 100)   #设置语速
engine.setProperty('volume',0.6)  #设置音量
rate = engine.getProperty('rate')
print(f'语速：{rate}')
volume = engine.getProperty('volume')
print(f'音量：{volume}')
#语音播放
pyttsx3.speak("How are you?")
pyttsx3.speak("I am fine, thank you")