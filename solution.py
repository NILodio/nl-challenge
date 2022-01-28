# -*- coding: utf-8 -*-
# @Author: Danilo Diaz Valencia
# @Date:   2022-01-27 20:16:25
# @Last Modified by:   Danilo Diaz Valencia
# @Last Modified time: 2022-01-27 23:03:59
import re
import inquirer
import sys
import os
from jsgf import parse_grammar_string
from pathlib import Path

questions_base = [
  inquirer.List('file',
                message="NL Challenge Files(JSGF))",
                choices=['base_us_JSGF.txt', 'base_us_ext_JSGF.txt','base_es_ext_JSGF.txt'],
            ),
]

questions_iter = [
  inquirer.List('iter',
                message="How many iterations?",
                choices=[10, 100 , 1000 , 10000],
            ),
]

def open_file(file: str):
    try:
        with open(file , 'r') as a:
            s = a.read()
        return s
    except FileNotFoundError:
        print(f"File : {file_base['file']} no found")
        sys.exit(1)


def main(base : str , iter : int , file : str):
    # try:
    g = parse_grammar_string(base)
    # except:
    #     print("Error")
    #     sys.exit(1)
    print("####################Rules###########################")
    for i , j in enumerate(g.rules):
        print(f"Rule : {j.name}")
    utt = []
    for _ in range(iter):
        utt.append(g.rules[0].generate())
    print(*set(utt) , sep='\n')
    with open("utt_files"+ "/"+ file + "_utt.txt" , 'w') as f:
        for i in set(utt):
            f.write("%s\n" % i)


if __name__ == "__main__":
    file_base = inquirer.prompt(questions_base)
    iter = inquirer.prompt(questions_iter)
    data_base = open_file(file=file_base['file'])
    main(base = data_base , iter=int(iter['iter']) , file =os.path.splitext(file_base['file'])[0])

    
    
       

