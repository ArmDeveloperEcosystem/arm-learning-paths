#/usr/bin/env python3

import logging
import os
import subprocess
import csv
import json
import re
from datetime import datetime, timedelta

# List of directories to parse for learning paths
dname = ["content/install-guides",
         "content/learning-paths/cross-platform",
         "content/learning-paths/laptops-and-desktops",
         "content/learning-paths/embedded-and-microcontrollers",
         "content/learning-paths/iot",
         "content/learning-paths/mobile-graphics-and-gaming",
         "content/learning-paths/servers-and-cloud-computing",
         "content/learning-paths/automotive"]




'''
Returns the date (yyyy-mm-dd) which a file in the given directory was last updated.
If Learning Path, changes in any file in the directory will count.
'''
def get_latest_updated(directory, is_lp, item):
    article_path = directory if is_lp else f"{directory}/{item}"
    date = subprocess.run(["git", "log", "-1" ,"--format=%cs", str(article_path)], stdout=subprocess.PIPE)
    return date

'''
Recursive content search in a given directory.
Returns:
- list of articles older than a given period found
- count of articles found
- list of primary authors found
'''
def content_parser(directory, period):
    count = 0
    art_list = {}
    auth_list = []
    directory_list = os.listdir(directory)
    for i in directory_list:
        item = i
        is_lp = False
        if item.endswith(".md") and not item.startswith("_"):
            count = count + 1
            if "learning-paths" in directory:
                item = "_index.md"
                is_lp = True

            logging.debug(f"Checking {directory}/{item}")

            date = get_latest_updated(directory, is_lp, item)
            # strip out '\n' and decode byte to string
            date = date.stdout.rstrip().decode("utf-8")
            logging.debug(f"Last updated: {date}")
            author = "None"
            for directory_list in open(directory +"/" + item):
                if re.search("author_primary", directory_list):
                    # split and strip out '\n'
                    author = directory_list.split(": ")[1].rstrip()
            logging.debug(f"Primary author {author}")
            if not author in auth_list:
                auth_list.append(author)

            # if date is None, this is a temporary file which is not part of the repo
            if date:
                date = datetime.strptime(date, "%Y-%m-%d")
                # check if article is older than the period
                if date < datetime.now() - timedelta(days = period):
                    if is_lp:
                        art_list[directory + "/"] = "{} days ago".format((datetime.now() - date).days)
                    else:
                        art_list[directory + "/" + item] = "{} days ago".format((datetime.now() - date).days)

            if "learning-paths" in directory:
                # no need to iterate further
                break

        # if this is a folder, let's get down one level deeper
        elif os.path.isdir(directory + "/" + item):
            res, c, a_l = content_parser(directory + "/" + item, period)
            art_list.update(res)
            count = count + c
            for a in a_l:
                if not a in auth_list:
                    auth_list.append(a)

    return [art_list, count, auth_list]


'''
Initialize Plotly data structure for stats
1 graph on the left with data for install tool guides
1 graph on the right with data for learning paths
Input: title for the graph
'''
def init_graph(title):
    data = {
            "data": [
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "install-guides",
                    "xaxis": "x1"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/cross-platform",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/laptops-and-desktops",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/embedded-and-microcontrollers",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/iot",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/mobile-graphics-and-gaming",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/servers-and-cloud-computing",
                    "xaxis": "x2"
                },
                                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/automotive",
                    "xaxis": "x2"
                }
            ],
            "layout":
            {
                "title": title,
                "xaxis":
                {
                    "tickangle": -45,
                    "domain": [0, 0.45],
                    "anchor": "x1"
                },
                "xaxis2":
                {
                    "tickangle": -45,
                    "domain": [0.55, 1],
                    "anchor": "x2"
                },
                "barmode": "stack",
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font":
                {
                    "color": "rgba(130,130,130,1)"
                },
                "legend":
                {
                    "bgcolor": "rgba(0,0,0,0)"
                }
            }
        }

    return data


'''
Generate JSON data for stats page
'''
def stats():
    global dname

    # get working directory
    orig = os.path.abspath(os.getcwd())

    # If file exists, load data. Create structure otherwise
    if os.path.exists('content/stats/lp_data.json'):
        # Opening JSON file
        f = open('content/stats/lp_data.json', 'r')
        # returns JSON object as a dictionary
        lp_data = json.load(f)
        # Closing JSON file
        f.close()
    else:
        # Create dict
        lp_data = init_graph("Number of installation guides and learning paths")

    # If file exists, load data. Create structure otherwise
    if os.path.exists('content/stats/contrib_data.json'):
        # Opening JSON file
        f = open('content/stats/contrib_data.json', 'r')
        # returns JSON object as a dictionary
        contrib_data = json.load(f)
        # Closing JSON file
        f.close()
    else:
        # Create dict
        contrib_data = init_graph("Number of contributors")

    total=0
    for d_idx, d in enumerate(dname):
        res, count, authors = content_parser(d, 0)
        # Sliding windows for data - remove data older than a year - 53 weeks
        if len(lp_data["data"][d_idx]["x"]) > 52:
            lp_data["data"][d_idx]["x"].pop(0)
            lp_data["data"][d_idx]["y"].pop(0)
        if len(contrib_data["data"][d_idx]["x"]) > 52:
            contrib_data["data"][d_idx]["x"].pop(0)
            contrib_data["data"][d_idx]["y"].pop(0)
        # Date
        lp_data["data"][d_idx]["x"].append(datetime.now().strftime("%Y-%b-%d"))
        contrib_data["data"][d_idx]["x"].append(datetime.now().strftime("%Y-%b-%d"))
        # Articles counted in category
        lp_data["data"][d_idx]["y"].append(count)
        # Authors counted in category
        contrib_data["data"][d_idx]["y"].append(len(authors))

        if "learning-paths" in d:
            logging.info(f"{count} Learning Paths found in {d} and {len(authors)} contributor(s)")
            total += count
        else:
            logging.info(f"{count} articles found in {d} and {len(authors)} contributor(s)")

    logging.info(f"Total number of Learning Paths is {total}")

    lp_data_file='content/stats/lp_data.json'
    contrib_data_file='content/stats/contrib_data.json'
    os.chdir(orig)
    logging.info(f"Learning Path data written to {orig}/{lp_data_file}")
    logging.info(f"Contributors data written to {orig}/{contrib_data_file}")

    # Save data in json file
    f_lp = open(lp_data_file, 'w')
    f_contrib = open(contrib_data_file, 'w')
    # Write results to file
    json.dump(lp_data, f_lp)
    json.dump(contrib_data, f_contrib)
    # Closing JSON file
    f_lp.close()
    f_contrib.close()


'''
List pages older than a period in days and save result as CSV
Generate JSON file with data
'''
def report(period):
    global dname


    # get working directory
    function_start_directory = os.path.abspath(os.getcwd())
    # change directory to the repository root
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

    result = {}
    total=0

    for d_idx, directory in enumerate(dname):
        res, count, _ = content_parser(directory, period)
        result.update(res)
        if "learning-paths" in directory:
            total += count

        logging.info(f"Found {count} Learning Paths in {directory}. {len(res)} of them are outdated")


    logging.info(f"Total number of Learning Paths is {total}")

    outdated_files_csv="outdated_files.csv"
    fields=["File", "Last updated"]
    # Moving back to the directory which we started in
    os.chdir(function_start_directory)

    with open(outdated_files_csv, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        for key in result.keys():
            csvfile.write("%s, %s\n" % (key, result[key]))
    logging.info(f"Results written to {function_start_directory}/{outdated_files_csv}")

