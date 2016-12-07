#!/usr/bin/python
#coding:utf8
from subprocess import PIPE, Popen

import os

import sys



def installipython():
    ip = os.system('pip install ipython')
	if not ip:
	    print 'ipython安装成功'
    else:
	    print '请手动安装ipython(pip install ipython)'
def updateyum():
    yu = os.system('\cp -fr ./yum  /usr/bin/')
    if yu == 0:
        print 'update successfully'

def installpip():
    print os.getcwd()
    os.system('tar -zxvf pip-8.1.2.tar.gz')
    os.chdir('pip-8.1.2')
    a = os.system('python setup.py install')
    if a == 0:
        print 'pip 安装成功'
    if os.system('pip install --upgrade pip') == 0:
        print 'pip更新成功'
		
	
    os.chdir('..')

def changedir():
    os.system('mv /usr/bin/python /usr/bin/python2.6')
    os.system('ln -s /usr/local/bin/python2.7 /usr/bin/python')

def installPython():
    os.getcwd()
    py = os.system('tar -zxvf Python-2.7.9.tgz')
    print py,'*' * 50
    os.chdir('Python-2.7.9')
    install_python = os.system('./configure  && make && make install')
    if install_python == 0:
        print 'python安装成功'
    
    os.chdir('..')





def main():
    print '开始安装python包 需要安装依赖包 openssl openssl-devel readline-devl readline setuptools wget https://bootstrap.pypa.io/ez_setup.py -O - | python'
    a = os.system('yum install -y openssl openssl-devel readline-devl readline')
    if a == 0:
        print '安装成功'
    #setuptools = os.system('wget https://bootstrap.pypa.io/ez_setup.py -O - | python')
    #if setuptools == 0:
    #    print 'setuptools 安装成功'
   
    installPython()
    changedir()
	os.system('unzip setuptools-30.2.0.zip')
    os.chdir('setuptools-30.2.0')
    os.system('python setup.py install')
    os.chdir('..')
    installpip()
    updateyum()



if __name__ == '__main__':
    main()
