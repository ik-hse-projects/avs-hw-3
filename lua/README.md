# Архитектура

Аналогична таковой на Python, однако в коде на Lua гораздо лучше видна эта структура.

# Производительность
```
> luajit ./main.lua -f tests/in/1.txt -o tests/out/1.txt
Executed in  4.20 millis

> luajit ./main.lua -f tests/in/1000.txt -o tests/out/1000.txt
Executed in  49.96 millis

> luajit ./main.lua -f tests/in/5000.txt -o tests/out/5000.txt
Executed in  962.37 millis

> luajit ./main.lua -f tests/in/10000.txt -o tests/out/10000.txt
Executed in  5.54 secs
```

На небольших тестах (1000) решение сравнимо по производительности с решениями на C и на C++, и значительно быстрее решения на CPython или PyPy. Однако на больших тестах это решение имеет ту же производительность, что и решение на PyPy. В среднем, в два раза медленнее решений на компилируемых языках.
