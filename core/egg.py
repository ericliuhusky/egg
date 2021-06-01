from . import gyb
from typing import Any, Tuple
import json

# 文件夹路径
import os
FILE_PATH = os.path.abspath(__file__)
DIRECTORY_PATH = os.path.dirname(FILE_PATH)


def parse_config(jsondict: Any) -> gyb.Block:
    filename = '%s/templates/%s.swift.gyb' % (DIRECTORY_PATH, jsondict['template'])
    file = open(filename, 'r')
    templatetext = file.read()
    ast = gyb.parse_template(filename, templatetext)
    return ast

def execute_config(ast: gyb.Block, jsondict: Any) -> str:
    bindings = jsondict
    boilerplate = gyb.execute_template(ast, line_directive='', **bindings)
    return boilerplate



def read_and_parse(filename: str) -> Tuple[gyb.Block, Any]:
    with open(os.path.normpath(filename), 'r', encoding='utf-8') as f:
        jsondict = json.loads(f.read())
        ast = parse_config(jsondict)
        return (ast, jsondict)

def parse_and_write(filename: str, ast: gyb.Block, jsondict: Any):
    if ast is not None and jsondict is not None:
        with open(filename, 'w', encoding='utf-8', newline='\n') as f:
            boilerplate = execute_config(ast, jsondict)
            f.write(boilerplate)
