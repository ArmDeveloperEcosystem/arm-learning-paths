#/usr/bin/env python3

import logging
import json
import yaml
import os
import string
import re
from inclusivewriting.suggestions import detect_and_get_suggestions
from spellchecker import SpellChecker


'''
Parse commands in markdown article and return list of commands
'''
def parse(article):
    with open(article) as file:
        content = file.read()
        file.close()

    cmd = []
    for i in content:
        start = content.find("```") + 3
        end = content.find("```", start)

        if start == -1 or end == -1:
            # No code section left
            return cmd
        else:
            cmd.append(content[start:end])
            content = content[end+3:]

'''
Parse file for spelling mistakes in text
'''
def spelling(article):
    language = "en"

    with open(article) as file:
        content = file.read()
        file.close()

    spell = SpellChecker(case_sensitive=True)
    #spell.word_frequency.load_words(['bare-metal', 'x86', 'cross-compile', 'cross-compiler', 'low-level', 'toolchain', 'toolchains', 'on-screen', 'microcontrollers', 'gcc', 'cross-building', 'pre-built', '32-bit', '64-bit'])
    spell.word_frequency.load_words( open(os.path.dirname(os.path.realpath(__file__)) + '/add_words.txt').read().split() )

    # Skip header
    start = content.find("---") + 3
    end = content.find("---", start)
    if not end == start-3:
        output = content[start-3:end+3]
        content = content[end+3:]

    output += "\n\n{{< highlight red \"This article has been checked for spelling mistakes (yellow) and inclusive language (green). Hover your mouse on highlighted words to see suggested correction.\" >}}\n"

    cmd = []
    icount = 0
    rcount = 0
    while (not start == -1 or not end == -1):
        start = content.find("```")
        end = content.find("```", start+3)

        if content.find("{{< tabpane") > 0 and content.find("{{< tabpane") < start:
            start = content.find("{{< tabpane")
            end = content.find("{{< /tabpane >}}", start+11)

        # split command and text
        txt = content[:start]
        cmd = content[start:end+3]

        # check word spelling in text
        word_list=[]
        txt_list = re.split(' |\n|#|\(', txt)

        for word in txt_list:
            # get rid of punctuation and make lower case
            word_clean = word.translate(str.maketrans('', '', string.punctuation.replace("-","")))
            if not word_clean == '': 
                word_list.append(word_clean)

        new_text = txt

        unknown_list = spell.unknown(word_list)
        used_suggestions, suggestions, updated_text =  detect_and_get_suggestions(txt)

        if (len(used_suggestions) > 0):
            for word in used_suggestions:
                replacement_list = "\""
                for replacement in suggestions[word.lower()].get_replacement_lexemes():
                    replacement_list = replacement_list + replacement.get_value() + ", "
                replacement_list = replacement_list + "\""
                new_text, nsub = re.subn(" {} ".format(word), " {{{{< highlight green {} {} >}}}} ".format(word,replacement_list), new_text)
                icount += nsub
        
        for u in unknown_list:
            new_text, nsub = re.subn(" {} ".format(u), " {{{{< highlight yellow {} {} >}}}} ".format(u,spell.correction(u)), new_text)
            rcount += nsub
        output += new_text

        # concatenate cmd
        output += cmd
        content = content[end+3:]

    # No code section left
    logging.info("{} inclusive language issue(s) found.".format(icount))
    logging.info("{} spelling mistake(s) found.".format(rcount))
    return output


'''
Parse header to check file or not
Returns dict with the following elements:
    test_maintenance: bool value to check the article
    test_images: list of targets supported
    weight: int value with weight of article when in a learning path
'''
def header(article):
    dict = {"maintain": False, "img": None, "weight": -1}
    with open(article) as file:
        content = file.read()
        file.close()

    header = []
    start = content.find("---") + 3
    end = content.find("---", start)
    if end == start-3:
        # No header
        logging.debug("No header found in {}".format(article))
        return dict
    else:
        header = content[start:end]
        data = yaml.safe_load(header, )
        if "test_maintenance" in data.keys():
            dict.update(maintain=data["test_maintenance"])
        if "test_images" in data.keys():
            dict.update(img= data["test_images"])
        if "weight" in data.keys():
            dict.update(wght=data["weight"])
                    
    return dict


'''
Save list of command in json file
'''
def save(article, cmd, learningpath=False, img=None):
    
    # Parse file header
    hdr = header(article)

    if not hdr["maintain"] and not learningpath:
        logging.info("File {} settings don't enable parsing.".format(article))
        return

    if not img:
        img = hdr["img"]

    content = { "image": img, "weight": hdr["weight"]}

    logging.debug(content)

    for i_idx,i  in enumerate(cmd):
        l = list(filter(None, i.split("\n")))
        # if fvp type, check for arguments
        if not l:
            continue
        elif "fvp" in l[0]:
            content[i_idx] = {"type": "fvp"}
            # check if current directory is specified
            if "cwd" in l[0]:
                cwd = l[0].split("cwd=\"")[1].split("\"")[0]
                content[i_idx].update({"cwd": cwd })
            if "fvp_name" in l[0]:
                model = l[0].split("fvp_name=\"")[1].split("\"")[0]
                content[i_idx].update({"fvp_name": model })
            else:
                content[i_idx].update({"fvp_name": "FVP_Corstone_SSE-300_Ethos-U55" })
        # if bash type, check for arguments
        elif "bash" in l[0]:
            content[i_idx] = {"type": "bash"}
            # check if return code is specified
            if "ret_code" in l[0]:
                ret = l[0].split("ret_code=\"")[1].split("\"")[0]
                content[i_idx].update({"ret_code": ret })
            else:
                content[i_idx].update({"ret_code": "0" })
            # check if a file needs to be sourced
            if "env_source" in l[0]:
                env = l[0].split("env_source=\"")[1].split("\"")[0]
                content[i_idx].update({"env_source": env })
            # check if env var are specified
            if "env=" in l[0]:
                env = l[0].split("env=\"")[1].split("\"")[0]
                env = env.split(";")
                content[i_idx].update({"env": env })
            # check if commands need to be run beforehand
            if "pre_cmd" in l[0]:
                env = l[0].split("pre_cmd=\"")[1].split("\"")[0]
                content[i_idx].update({"pre_cmd": env })
            # check if current directory is specified
            if "cwd" in l[0]:
                cwd = l[0].split("cwd=\"")[1].split("\"")[0]
                content[i_idx].update({"cwd": cwd })
            # check target
            if "target" in l[0]:
                tgt = l[0].split("target=\"")[1].split("\"")[0]
                content[i_idx].update({"target": tgt })
            # check if any expected result
            if "|" in l[0]:
                expected_result = l[0].split("| ")[1].split("\"")[0]
                content[i_idx].update({"expected": expected_result })
        # for other types, we're assuming source code
        # check if a file name is specified
        else:
            content[i_idx] = {"type": l[0]}
            # check file name
            if "file_name" in l[0]:
                fn = l[0].split("file_name=\"")[1].split("\"")[0]
                content[i_idx].update({"file_name": fn })

        for j_idx,j in enumerate(l[1:]):
            content[i_idx].update({j_idx: j})
            content[i_idx].update({ "ncmd": j_idx+1 })
        content.update({ "ntests": i_idx+1 })

        logging.debug(content[i_idx])

    fn = article + "_cmd.json"
    logging.debug("Saving commands to " + fn)

    with open(fn, 'w') as f:
        json.dump(content, f)

