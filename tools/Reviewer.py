import os, sys
import re
import frontmatter
from collections import defaultdict, Counter

def extract_metrics_from_content(content):
    heading_hierarchy = []
    heading_stack = []
    char_count_by_heading = defaultdict(int)
    code_blocks = 0
    code_lines  = 0
    code_output = 0

    # code dict should be populated like so: {'C': {'blocks': 2, 'code_lines': 5, 'output_lines': 0}, 'python': {...}, ...}
    code_dict = {}

    lines = content.split('\n')

    current_heading = None
    in_code_block = False

    # Iterate over all lines in this .md file
    for line in lines:
        # Check if line is a header; handle specifically
        heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)

            # Adjust heading stack to match the current level
            while len(heading_stack) >= heading_level:
                heading_stack.pop()

            heading_stack.append(heading_text)
            heading_hierarchy.append((' ' * (heading_level - 1) * 2) + '- ' + heading_text)

            current_heading = '/'.join(heading_stack)
            continue

        # Gather metrics, store under this heading
        if current_heading:
            
            # Code block processing
            if in_code_block:
                if not '```' in line:       
                    # increment code lines
                    code_lines += 1

            if '```' in line:
                # code block start
                if not in_code_block:
                    in_code_block = True

                    # in code block
                    code_blocks += 1
                    code_language = line.replace('```','').strip()


                # code block end
                else:
                    # add to code dict
                    if code_language not in code_dict:
                        code_dict[code_language] = {
                            'blocks': code_blocks,
                            'lines': code_lines,
                            'output': code_output
                        }
                    else:
                        code_dict[code_language]['blocks'] += code_blocks
                        code_dict[code_language]['lines']  += code_lines
                        code_dict[code_language]['output'] += code_output
                    # reset vars
                    in_code_block = False
                    code_blocks = 0
                    code_lines  = 0
                    code_output = 0
                                                            
            else:
                # Count characters, excluding markdown syntax
                char_count_by_heading[current_heading] += len(re.sub(r'[<>`*_{}[\]()#+-.!|]', '', line))

    return heading_hierarchy, char_count_by_heading, code_dict

def process_blog_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    files_with_weights = []

    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            metadata, _ = frontmatter.parse(f.read())
            weight = metadata.get('weight', 99999)
            files_with_weights.append((weight, file))

    sorted_files = sorted(files_with_weights)
    if len(sorted_files) <= 3:
        print("ERROR: Learning Path has less than 3 .md files, meaning no custom content has been written. Exiting.")
        sys.exit(1)

    # Remove intro, questions, next steps
    sorted_files = sorted_files[1:-2]

    total_char_count = 0
    total_code_dict = {}
    
    all_heading_hierarchy = []
    char_count_by_heading_aggregate = defaultdict(int)

    for weight, file in sorted_files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            _, content = frontmatter.parse(f.read())

            heading_hierarchy, char_count_by_heading, code_dict = extract_metrics_from_content(content)

            all_heading_hierarchy.extend(str(weight-1))
            all_heading_hierarchy.extend(heading_hierarchy)
            for heading, char_count in char_count_by_heading.items():
                char_count_by_heading_aggregate[heading] += char_count
            total_char_count += sum(char_count_by_heading.values())

            ######33 TO DO: Merge dict in automatically to central dict
            for lang, vals in code_dict.items():
                if lang not in total_code_dict:
                    total_code_dict[lang] = vals
                else:
                    total_code_dict[lang]['blocks'] += vals['blocks']
                    total_code_dict[lang]['lines'] += vals['lines']
                    total_code_dict[lang]['output'] += vals['output']
            

    print("Ordered Hierarchy of Headings:")
    for heading in all_heading_hierarchy:
        print(heading)
    
    #print("\nNumber of Characters by Heading:")
    #for heading, char_count in char_count_by_heading_aggregate.items():
    #    print(f"{heading}: {char_count} characters")

    
    print("\nTotal Number of Characters:", total_char_count)
    
    
    print("\nTotal Number of Code Blocks and Lines of Code:")
    for language, metrics_dic in total_code_dict.items():
        print(language)
        print("   Blocks: "+str(metrics_dic['blocks']))
        print("   Lines: "+str(metrics_dic['lines']))
    
    
if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the markdown files: ")
    process_blog_files(directory)



















'''
import os
import re
import frontmatter
from collections import defaultdict, Counter

def extract_metrics_from_content(content):
    heading_hierarchy = []
    heading_stack = []
    char_count_by_heading = defaultdict(int)
    code_blocks = Counter()
    total_code_lines = 0

    code_block_pattern = re.compile(r'```(\w+)?\n(.*?)```', re.DOTALL)
    lines = content.split('\n')

    current_heading = None
    in_code_block = False
    code_block_language = None
    code_lines = []

    for line in lines:
        heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)

            # Adjust heading stack to match the current level
            while len(heading_stack) >= heading_level:
                heading_stack.pop()

            heading_stack.append(heading_text)
            heading_hierarchy.append((' ' * (heading_level - 1) * 2) + '- ' + heading_text)

            current_heading = '/'.join(heading_stack)
            continue

        if current_heading:
            # Code block detection and processing
            code_block_match = code_block_pattern.search(line)
            if code_block_match:
                if not in_code_block:
                    in_code_block = True
                    code_block_language = code_block_match.group(1) or 'plaintext'
                    code_lines = code_block_match.group(2).strip().split('\n')
                    code_blocks[code_block_language] += len(code_lines)
                    total_code_lines += len(code_lines)
                else:
                    in_code_block = False
                    code_block_language = None
                    code_lines = []
            else:
                # Count characters, excluding markdown syntax
                char_count_by_heading[current_heading] += len(re.sub(r'[<>`*_{}[\]()#+-.!|]', '', line))

    return heading_hierarchy, char_count_by_heading, code_blocks, total_code_lines

def process_blog_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    files_with_weights = []

    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            metadata, _ = frontmatter.parse(f.read())
            weight = metadata.get('weight', 99999)
            files_with_weights.append((weight, file))

    sorted_files = sorted(files_with_weights)
    if len(sorted_files) <= 3:
        print("Not enough files to process.")
        return

    sorted_files = sorted_files[1:-2]

    total_char_count = 0
    total_code_blocks = Counter()
    total_code_lines = 0
    all_heading_hierarchy = []

    for weight, file in sorted_files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            _, content = frontmatter.parse(f.read())
            heading_hierarchy, char_count_by_heading, code_blocks, code_lines = extract_metrics_from_content(content)

            all_heading_hierarchy.extend(heading_hierarchy)
            total_char_count += sum(char_count_by_heading.values())
            total_code_blocks.update(code_blocks)
            total_code_lines += code_lines

    print("Ordered Hierarchy of Headings:")
    for heading in all_heading_hierarchy:
        print(heading)

    print("\nTotal Number of Characters:", total_char_count)
    print("\nTotal Number of Code Blocks and Lines of Code:")
    for language, count in total_code_blocks.items():
        print(f"Language: {language}, Code Blocks: {count}")
    print(f"Total Lines of Code: {total_code_lines}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the markdown files: ")
    process_blog_files(directory)
'''









'''
import os
import re
import frontmatter
from collections import defaultdict, Counter

def extract_metrics_from_content(content):
    heading_hierarchy = []
    heading_stack = []
    char_count_by_heading = defaultdict(int)
    code_blocks = Counter()
    total_code_lines = 0

    code_block_pattern = re.compile(r'```(\w+)?\n(.*?)```', re.DOTALL)
    lines = content.split('\n')

    current_heading = None
    in_code_block = False
    code_block_language = None
    code_lines = []

    for line in lines:
        heading_match = re.match(r'^(#{1,6})\s+(.*)', line)
        if heading_match:
            heading_level = len(heading_match.group(1))
            heading_text = heading_match.group(2)

            # Adjust heading stack to match the current level
            while len(heading_stack) >= heading_level:
                heading_stack.pop()

            heading_stack.append(heading_text)
            heading_hierarchy.append((' ' * (heading_level - 1) * 2) + '- ' + heading_text)

            current_heading = '/'.join(heading_stack)
            continue

        if current_heading:
            # Code block detection and processing
            code_block_match = code_block_pattern.match(line)
            if code_block_match:
                if not in_code_block:
                    in_code_block = True
                    code_block_language = code_block_match.group(1) or 'plaintext'
                    code_lines = code_block_match.group(2).strip().split('\n')
                else:
                    in_code_block = False
                    code_block_language = None
                    code_lines = []

            if in_code_block and code_block_language:
                code_lines.append(line)
            else:
                # Count characters, excluding markdown syntax
                char_count_by_heading[current_heading] += len(re.sub(r'[<>`*_{}[\]()#+-.!|]', '', line))

            if not in_code_block and code_block_language:
                code_blocks[code_block_language] += len(code_lines)
                total_code_lines += len(code_lines)

    return heading_hierarchy, char_count_by_heading, code_blocks, total_code_lines

def process_blog_files(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.md')]
    files_with_weights = []

    for file in files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            metadata, _ = frontmatter.parse(f.read())
            weight = metadata.get('weight', 99999)
            files_with_weights.append((weight, file))

    sorted_files = sorted(files_with_weights)
    if len(sorted_files) <= 3:
        print("Not enough files to process.")
        return

    sorted_files = sorted_files[1:-2]

    total_char_count = 0
    total_code_blocks = Counter()
    total_code_lines = 0
    all_heading_hierarchy = []

    for weight, file in sorted_files:
        with open(os.path.join(directory, file), 'r', encoding='utf-8') as f:
            _, content = frontmatter.parse(f.read())
            heading_hierarchy, char_count_by_heading, code_blocks, code_lines = extract_metrics_from_content(content)

            all_heading_hierarchy.extend(heading_hierarchy)
            total_char_count += sum(char_count_by_heading.values())
            total_code_blocks.update(code_blocks)
            total_code_lines += code_lines

    print("Ordered Hierarchy of Headings:")
    for heading in all_heading_hierarchy:
        print(heading)

    print("\nTotal Number of Characters:", total_char_count)
    print("\nTotal Number of Code Blocks and Lines of Code:")
    for language, count in total_code_blocks.items():
        print(f"Language: {language}, Code Blocks: {count}, Lines of Code: {total_code_lines}")

if __name__ == "__main__":
    directory = input("Enter the path to the directory containing the markdown files: ")
    process_blog_files(directory)
'''