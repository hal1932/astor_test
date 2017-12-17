# encoding: utf-8
import astor
import ast
import importlib
import datetime as dt

begin = dt.datetime.now()
with open('aaa.py', 'r') as f:
    tree = ast.parse(f.read())
print(dt.datetime.now() - begin)

begin = dt.datetime.now()
for node in tree.body:
    if not isinstance(node, ast.FunctionDef):
        continue

    print node.name
    for deco in node.decorator_list:
        if isinstance(deco, ast.Name):
            print '-- ' + deco.id
        elif isinstance(deco, ast.Call) and isinstance(deco.func, ast.Name):
            print '== {} {} {}'.format(deco.func.id, deco.args, deco.keywords)
print(dt.datetime.now() - begin)

begin = dt.datetime.now()
code = compile(tree, '<filename>', 'exec')
print(dt.datetime.now() - begin)
