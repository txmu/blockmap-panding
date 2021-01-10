import py_compile

py_compile.compile(file = "tzpd.py",cfile = "tzpd.pyc",optimize=-1)
py_compile.compile(file = "tzpd.py",cfile = "tzpd.pyo",optimize=1)
