# Style and Grammar Checking Tools for Arm Learning Paths

This directory contains tools for checking and enforcing the writing style guidelines and grammar for Arm Learning Paths content.

## Available Tools

1. **enhanced_style_check.py**: Check markdown files against writing style guidelines and provide suggestions. Uses both rule-based checks and NLP-based passive voice detection.
2. **grammar_check.py**: Check markdown files for grammar issues using the LanguageTool API.
3. **combined_check.py**: Run both style and grammar checks and combine the results.
4. **github_suggestion.py**: Format style suggestions as GitHub review comments.
5. **style_rules.json**: JSON file containing style rules and patterns.

## Local Testing

### Prerequisites

For basic functionality, no special dependencies are required.

For advanced passive voice detection, you'll need:
- spaCy library
- English language model for spaCy

For grammar checking, you'll need:
- requests
- markdown
- beautifulsoup4

You can install these with:
```bash
pip install spacy requests markdown beautifulsoup4
python -m spacy download en_core_web_sm
```

Or use the built-in installer for spaCy:
```bash
python3 tools/enhanced_style_check.py --install-spacy
```

### Usage

#### Check style for a single file:

```bash
python3 tools/enhanced_style_check.py --file path/to/file.md
```

#### Check grammar for a single file:

```bash
python3 tools/grammar_check.py --file path/to/file.md
```

#### Run combined style and grammar check:

```bash
python3 tools/combined_check.py --file path/to/file.md
```

#### Check all markdown files in a directory:

```bash
python3 tools/combined_check.py --dir path/to/directory
```

## GitHub Actions Integration

The style and grammar checkers are integrated with GitHub Actions and can be run manually on a PR:

1. Go to the "Actions" tab in the GitHub repository
2. Select one of the following workflows:
   - "Style Check" - for style issues only
   - "Grammar Check" - for grammar issues only
   - "Combined Style and Grammar Check" - for both style and grammar issues
3. Click "Run workflow"
4. Enter the PR number and click "Run workflow"

The workflow will check the PR content and add review comments with suggestions that you can directly commit or dismiss.

## Style Rules

Style rules are defined in `style_rules.json`. Each rule has:

- **pattern**: Regular expression pattern to match
- **replacement**: Text to replace the matched pattern
- **reason**: Explanation for the suggestion

To add or modify rules, edit the `style_rules.json` file.

### Types of Style Checks

The style checker performs several types of checks:

1. **Word Choice**: Replaces complex words with simpler alternatives (e.g., "utilize" → "use")
2. **Passive Voice**: Converts passive voice to active voice for clarity and directness
3. **Wordiness**: Simplifies wordy phrases (e.g., "in order to" → "to")
4. **Tone**: Replaces "we" with "you" to address the reader directly
5. **Neutrality**: Replaces phrases like "we recommend" with "it is recommended" for a more neutral tone

## Passive Voice Detection

The style checker uses two methods to detect passive voice:

1. **spaCy NLP (Advanced)**: Uses spaCy's dependency parsing to identify passive voice constructions and suggest active voice alternatives. This method is more accurate but requires additional dependencies.

2. **Regular Expressions (Basic)**: Falls back to regex patterns if spaCy is not available. This method is less accurate but has no dependencies.

## Grammar Checking

The grammar checker uses the LanguageTool API to identify grammar, spelling, and style issues. It:

1. Extracts plain text from markdown files
2. Sends the text to the LanguageTool API
3. Maps the API responses back to the original markdown lines
4. Generates suggestions for fixing the issues

## Examples

### Word Choice Example:
Input:
```markdown
In order to utilize this feature, you should follow these steps.
```

Output suggestion:
```
Use 'use' instead of 'utilize' for simplicity.

```suggestion
To use this feature, follow these steps.
```
```

### Passive Voice Example:
Input:
```markdown
The data is processed by the system.
```

Output suggestion:
```
Convert passive voice to active voice for clarity and directness.

```suggestion
The system processes the data.
```
```

### Grammar Example:
Input:
```markdown
The system have many features.
```

Output suggestion:
```
Grammar: Subject-verb agreement error: The subject 'system' is singular, so the verb should be 'has'.

```suggestion
The system has many features.
```
```
