#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r'''
    # Web开发-使用模板：使用Flask框架
    # 使用场景：
        由于用Python开发一个Web框架十分容易，所以Python有上百个开源的Web框架。这里我们先不讨论各种Web框架的优缺点，直接选择一个比较流行的Web框架——Flask来使用。
        用Flask编写Web App比WSGI接口简单（这不是废话么，要是比WSGI还复杂，用框架干嘛？），我们先用pip安装Flask：
            $ pip install flask
        然后写一个app.py，处理3个URL，分别是：
            1、GET /：首页，返回Home；
            2、GET /signin：登录页，显示登录表单；
            3、POST /signin：处理登录表单，显示登录结果。
        注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
        Flask通过Python的装饰器在内部自动地把URL和函数给关联起来；
        下面我们将web_dev_wsgi_application_flask_test1.py中直接输出字符串作为HTML的例子用高端大气上档次的MVC模式改写一下：

'''
# 将web_dev_wsgi_application_flask_test1.py中的例子使用MVC模板改写
# 导入依赖
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html') 

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)   
    return render_template('form.html', message='Bad username or password', username=username)  

if __name__ == '__main__':
    app.run()


r'''
    #注：Flask通过render_template()函数来实现模板的渲染。和Web框架类似，Python的模板也有很多种。Flask默认支持的模板是jinja2，所以我们先直接安装jinja2：
            $ pip install jinja2
        然后，开始编写jinja2模板，具体参见templates目录下；注意，目录一定要命名准确：templates，与此文件放于同级目录下；
        除了Jinja2，常见的模板还有：
            （1）Mako：用<% ... %>和${xxx}的一个模板；
            （2）Cheetah：也是用<% ... %>和${xxx}的一个模板；
            （3）Django：Django是一站式框架，内置一个用{% ... %}和{{ xxx }}的模板。   
        小结
            有了MVC，我们就分离了Python代码和HTML代码。HTML代码全部放到模板里，写起来更有效率。         

'''