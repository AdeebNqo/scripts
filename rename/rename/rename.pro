TEMPLATE = app
CONFIG += console
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    ../../../randomM/inotify-cxx.cpp

HEADERS += \
    ../../../randomM/inotify-cxx.h

