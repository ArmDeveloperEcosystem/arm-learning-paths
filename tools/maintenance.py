#!/usr/bin/env python3

import argparse
import logging
import os
import sys
# Local import
import report
import parse
import patch
import check
import filter_checker


# Set default verbosity level
verbosity = logging.INFO
# [debugging] Verbosity settings
level = { 10: "DEBUG",  20: "INFO",  30: "WARNING",  40: "ERROR" }


"""
Test Learning Path
"""
def check_lp(lp_path, link, debug):
    test_image_results = None # initialize the variable
    if not os.path.isdir(lp_path):
        lp_path = os.path.dirname(lp_path)

    logging.info("Parsing Learning Path " + lp_path)

    if os.path.exists(lp_path+"/_index.md"):
        # check _index.md for maintenance options
        idx_header = parse.header(lp_path+"/_index.md")
        if idx_header["test_maintenance"]:
            # Parse all articles in folder to check them
            for k in os.listdir(lp_path):
                # Don't parse _index, _next-steps or _review
                if k.endswith(".md") and (not "_index" in k) and (not "_next-steps" in k) and (not "_review" in k):
                    _k = lp_path + "/" + k
                    logging.info("Parsing " + _k)
                    cmd = parse.parse(_k)
                    # Generate _cmd.json file with instructions
                    parse.save_commands_to_json(_k, cmd, idx_header["test_maintenance"], idx_header["test_images"])

            logging.info("Checking Learning Path " + lp_path)
            # Look for _cmd.json
            l = [i for i in os.listdir(lp_path) if i.endswith("_cmd.json")]
            # Build dict with weight value for each article
            article_per_weight = { i: parse.header(lp_path + "/" + i.replace("_cmd.json",""))["weight"] for i in l }
            # Sort dict by value
            test_image_results_list = []
            # sort LP by weight value to have it run sequentially
            for idx, i in enumerate(sorted(article_per_weight.items(), key=lambda item: item[1])):
                logging.info("Checking " + i[0].replace("_cmd.json",""))
                # We want all the articles from the learning path to run in the same container
                # Launch the instance at the beginning, and terminate it at the end
                launch = True
                terminate = True
                if i[1] != -1 and idx != 0:
                    launch = False
                if i[1] != -1 and idx != len(article_per_weight.keys())-1:
                    terminate = False
                test_image_results = check.check(lp_path + "/" + i[0], start=launch, stop=terminate, md_article=lp_path)
                test_image_results_list.append(test_image_results)

            if not debug:
                for i in os.listdir(lp_path):
                    if i.endswith("_cmd.json"):
                        os.remove(lp_path+"/"+i)
        else:
           logging.warning(f"Learning Path {lp_path} maintenance is turned off. Add or set \"test_maintenance: true\" otherwise.")
           exit(0)
    else:
        logging.warning("No _index.md found in Learning Path")
    return test_image_results


"""
Main function
"""
def main():
    global verbosity, level

    logging.info("This is Dougs Test maintenance.py FILE")

    arg_parser = argparse.ArgumentParser(description='Maintenance tool.', prefix_chars='-')
    arg_parser.add_argument('-v', '--version', action='version', version='Maintenance toolkit version 0.1', help='Display software version')
    arg_parser.add_argument('-d', '--debug', action='store_true', help='Enable debugging messages')
    arg_parser.add_argument('-l', '--link', metavar='URL', action='store', type=str, help='Specify URL to github actions report. Added when patching sources files with --instructions')
    arg_parser.add_argument('-p', '--patch', action='store_true', help='Patch categories _index.md with results when using --filter-checker')
    arg_parser.add_argument('-t', '--type', metavar='REPORT', action='store', default='all', type=str, help='Specify report type detailing the closed filter status when using --filter-checker. Can be either \'all\', \'subjects\', \'softwares\', \'oses\', \'tools\'')
    arg_parser.add_argument('-sr', '--stats-report', action='store_true', help='Added when patching statistics file with --instructions')

    arg_group = arg_parser.add_mutually_exclusive_group()
    arg_group.add_argument('-f', '--filter-checker', action='store_true', help='Validates the correct closed schema filters are being used, reports any errors, and optionally updates _index.md files for each learning path category to reflect the currently supported filters.')
    arg_group.add_argument('-s', '--spelling', metavar='INPUT', action='store', type=str, help='Parse spelling of md file as INPUT. On completion the INPUT is patched with highlighted text and correction.')
    arg_group.add_argument('-i', '--instructions', metavar='INPUT', action='store', type=str, help='Parse instructions from Learning Path(s) and test them. INPUT can be a CSV file with the list of Learning Paths, a single .md file or the Learning Path folder. Test results are stored in Junit XML file. A summary is also added to the Learning Path _index.md page.')
    arg_group.add_argument('-q', '--query', action='store_true', help='Query data and update website stats.')
    arg_group.add_argument('-r', '--report', metavar='DAYS', action='store', type=int, default=1, help='List articles older than a period in days (default is 1). Output a CSV file. This option is used by default.')

    args = arg_parser.parse_args()

    if args.debug:
        verbosity = logging.DEBUG

    logging.basicConfig(format='[%(levelname)s]\t%(message)s', level = verbosity)
    logging.debug("Verbosity level is set to " + level[verbosity])

    if args.instructions:
        if not os.path.exists(args.instructions):
            raise SystemExit(f"No such file or directory: {args.instructions}")
        results_dict = {}
        # check if article is a csv file corresponding to a file list
        if args.instructions.endswith(".csv"):
            # TODO idea: separate parsing of CSV into list, run in same way as a single one passed
            logging.info("Parsing CSV " + args.instructions)
            with open(args.instructions) as f:
                next(f) # skip header
                for line in f:
                    fn = line.split(",")[0]
                    # Check if this article is a learning path
                    if "/learning-paths/" in os.path.abspath(fn):
                        results_dict = check_lp(fn, args.link, args.debug)
                    elif fn.endswith(".md"):
                        logging.info("Parsing " + fn)
                        # check if maintenance if enabled
                        if parse.header(fn)["test_maintenance"]:
                            cmd = parse.parse(fn)
                            parse.save_commands_to_json(fn, cmd)
                            logging.info("Checking " + fn)
                            results_dict = check.check(fn+"_cmd.json", start=True, stop=True, md_article=fn)
                            if not args.debug:
                                os.remove(fn+"_cmd.json")
                        else:
                            logging.warning(f"{fn} maintenance is turned off. Add or set \"test_maintenance: true\" otherwise.")
                            sys.exit(0)
                    else:
                        logging.error("Unknown type " + fn)
        elif args.instructions.endswith(".md"):
            # Check if this article is a learning path
            if "/learning-paths/" in os.path.abspath(args.instructions):
                results_dict = check_lp(args.instructions, args.link, args.debug)
            else:
                logging.info("Parsing " + args.instructions)
                # check if maintenance if enabled
                if parse.header(args.instructions)["test_maintenance"]:
                    cmd = parse.parse(args.instructions)
                    parse.save_commands_to_json(args.instructions, cmd)
                    results_dict = check.check(args.instructions+"_cmd.json", start=True, stop=True, md_article=args.instructions)
                    if not args.debug:
                        os.remove(args.instructions+"_cmd.json")
                else:
                    logging.warning(f"{args.instructions} maintenance is turned off. Add or set \"test_maintenance: true\" otherwise.")
                    sys.exit(0)
        elif os.path.isdir(args.instructions) and "/learning-paths/" in os.path.abspath(args.instructions):
            results_dict = check_lp(args.instructions, args.link, args.debug)
        else:
            logging.error("-i/--instructions expects a .md file, a CSV with a list of files or a Learning Path directory")
        if args.stats_report:
            # If all test results are zero, all tests have passed
            patch.patch(args.instructions, results_dict, args.link)
        if results_dict is not None:
            if all(results_dict.get(k) for k in results_dict):
                # Errors exist
                logging.info("Tests failed in test suite")
                sys.exit(1)
        else:
            logging.info(f"results_dict is None for LP. Link: {args.link}")
    elif args.spelling:
        logging.info(f"Checking spelling of {args.spelling}")
        output = parse.spelling(args.spelling)
        logging.info(f"Highlighing mispelling in {args.spelling}")
        f = open(args.spelling, "w")
        f.write(output)
        f.close()
    elif args.filter_checker:
        logging.info("Filter-check")
        filter_checker.checker(args.type, args.patch)
    elif args.query:
        logging.info("Querying data and generating stats")
        report.stats()
        logging.info("Stats updated in content/stats/data.json")
    elif args.report:
        logging.info(f"Creating report of articles older than {args.report} days")
        report.report(args.report)


if __name__ == "__main__":
    main()
