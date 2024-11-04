#/usr/bin/env python3

import logging
import json
import yaml
import os
import string
import re
from inclusivewriting.suggestions import detect_and_get_suggestions
from spellchecker import SpellChecker

"""
Parse commands in markdown article and return list of commands
"""
def parse(article):
    with open(article) as file:
        content = file.read()
        file.close()

    cmds_list = []
    for i in content:
        start = content.find("```") + 3
        end = content.find("```", start)

        if start == -1 or end == -1:
            # No code section left
            return cmds_list
        else:
            cmds_list.append(content[start:end])
            content = content[end+3:]

"""
Parse file for spelling mistakes in text
"""
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
    logging.info(f"{icount} inclusive language issue(s) found.")
    logging.info(f"{rcount} spelling mistake(s) found.")
    return output


"""
Parse header to check file or not
Returns dict with the following elements:
    test_maintenance: bool value to check the article
    test_images: list of targets supported
    weight: int value with weight of article when in a learning path
"""
def header(article):
    dict = {"test_maintenance": False, "test_images": None, "weight": -1}
    with open(article) as file:
        content = file.read()
        file.close()

    header = []
    start = content.find("---") + 3
    end = content.find("---", start)
    if end == start-3:
        # No header
        logging.debug(f"No header found in {article}")
        return dict
    else:
        header = content[start:end]
        data = yaml.safe_load(header, )
        if "test_maintenance" in data.keys():
            dict.update(test_maintenance=data["test_maintenance"])
        if "test_images" in data.keys():
            dict.update(test_images=data["test_images"])
        if "weight" in data.keys():
            dict.update(weight=data["weight"])

    return dict

"""
Extract the argument value and return in a dict with the argument key.
"""
def get_arg_to_key_dict(cmd, key):
    value = cmd[0].split(f"{key}\"")[1].split("\"")[0]
    return { key : value }

"""
Parse all code blocks in a Markdown article and write to a JSON file.
"""
def save_commands_to_json(md_article, cmds_list, learningpath=False, img=None):

    # Parse file header
    article_header = header(md_article)

    if not article_header["test_maintenance"] and not learningpath:
        logging.info(f"File {md_article} settings doesn't enable parsing")
        return

    if not img:
        img = article_header["test_images"]

    content = {"test_images": img, "weight": article_header["weight"]}

    logging.debug(content)

    for cmd_idx, cmd_str in enumerate(cmds_list):
        cmd_lines = list(filter(None, cmd_str.split("\n")))
        if not cmd_lines:
            continue

        cmd_lines_header = cmd_lines[0]
        logging.debug(cmd_lines_header)
        # if fvp type, check for arguments
        if "fvp" in cmd_lines_header:
            content[cmd_idx] = {"type": "fvp"}
            # check if current directory is specified
            if "cwd" in cmd_lines_header:
                cwd = cmd_lines_header.split("cwd=\"")[1].split("\"")[0]
                content[cmd_idx].update({"cwd": cwd})
            if "fvp_name" in cmd_lines_header:
                model = cmd_lines_header.split("fvp_name=\"")[1].split("\"")[0]
                content[cmd_idx].update({"fvp_name": model })
            else:
                content[cmd_idx].update({"fvp_name": "FVP_Corstone_SSE-300_Ethos-U55" })
        # if bash type, check for arguments
        elif "bash" in cmd_lines_header:
            # Equal sign on env so that it's not picked up by env_source
            arg_list = ["ret_code", "env_source", "env=", "pre_cmd", "cwd", "target"]
            content[cmd_idx] = {"type": "bash"}
            for arg in arg_list:
                if arg in cmd_lines_header:
                    arg_str = cmd_str.split(arg)[1].split("\"")[1]
                    content[cmd_idx].update({arg:arg_str})
            if "|" in cmd_lines_header:
                expected_result = cmd_str.split("| ")[1].split("}")[0].split("-")
                if len(expected_result) > 1:
                    expected_lines = list(range(*[int(x)-1 for x in expected_result]))
                elif len(expected_result) == 1 and expected_result[0]:
                    expected_lines = [int(expected_result[0])-1]
                else:
                    raise SystemExit(
                    """The expected output line(s) should be specified as one of two options:
                    A single number:  | 2
                    A range:          | 2-10
                    The code block is indexing starts at 1""")
                content[cmd_idx].update({"expected": expected_lines })
        # for other types, we're assuming source code
        # check if a file name is specified
        else:
            content[cmd_idx] = {"type": cmd_lines_header}
            # check file name
            if "file_name" in cmd_lines_header:
                fn = cmd_lines_header.split("file_name=\"")[1].split("\"")[0]
                content[cmd_idx].update({"file_name": fn })

        # Parse all the lines in the code block
        for cmd_line_idx, cmd_line in enumerate(cmd_lines[1:]):
            content[cmd_idx].update({cmd_line_idx: cmd_line})
            content[cmd_idx].update({ "ncmd": cmd_line_idx+1 })
        content.update({ "ntests": cmd_idx+1 })

        logging.debug(content[cmd_idx])

    fn = md_article + "_cmd.json"
    logging.debug("Saving commands to " + fn)

    with open(fn, 'w') as f:
        json.dump(content, f)

