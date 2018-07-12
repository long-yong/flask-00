# /usr/bin/python3
# coding=utf-8

from flask import Flask, render_template

def page3():
    return render_template('page3.html')

def page4(par):
    if par == '2':
        return render_template('page42.html', name=par)
    else:
        return render_template('page41.html', name=par)