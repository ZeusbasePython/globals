# Globals
This library allows global access to different python api classes and functions

# Simplest way to use it

- put all your git projects you wanna exchange classes between them in a single folder
```
C:\Users\my_user\path\path\path\all_my_git_projects
```
Globas project, don't actually needs to be included in this directory. It doesn't even need to be cloned at all.

Unless you wanna use this library the proper way. Bu it can be done later if it's actually needed

![Directory with all mai guit projects](https://i.pinimg.com/originals/67/ec/2c/67ec2c13bc7ee72a06eb737eac3dc8bb.png)


- on the directory you wanna launch the "main api" (the one that will consume other projects classes and funtions), 
you put the PathMannanger.py file following this path tree:
```
C:\Users\my_user\path\path\path\all_my_git_projects\my_launcher_api\api\src\domain\control\PathMannanger.py
```
Don't forget to put your main class in src directory

![PathMannanger.py file](https://i.pinimg.com/originals/d1/a3/3e/d1a33efcc8880eefadec49f503352429.png)

- put the following code right on top of the __main__ class of your api.
```
from domain.control import PathMannanger
PathMannanger.PathMannanger(mode = 'WRONG_WAY_TO_MAKE_IT_WORKS')
```
![Chess api main file](https://i.pinimg.com/originals/85/69/13/856913a6ab812d67a54e1b9e0feeb6dd.png)

- Be happy. 

You don'd even need to specify the path of the classes you are importing.

Yes, its really that simple. 🌈✨🎇

![be hapy](https://i.pinimg.com/originals/9a/73/d0/9a73d02d6552502c748e436edacf1994.png)


# About the proper way to use this library
I'll be implementing more funcionalities in order to make it extendable and more compatible to python framewors in general.
If you want more information or just want to contribute a litle bit, please hit me up.
