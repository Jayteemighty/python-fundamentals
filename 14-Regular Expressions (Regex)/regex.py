"""
REGULAR EXPRESSIONS (REGEX)
Pattern-matching language for text processing using the `re` module.

Key Concepts:
- Patterns: Special strings that define search criteria
- Metacharacters: . ^ $ * + ? { } [ ] \ | ( )
- Flags: Modify matching behavior (case sensitivity, etc.)
"""

import re

# ==============================================================================
# 1. BASIC PATTERN MATCHING
# ==============================================================================
text = "The quick brown fox jumps over 42 lazy dogs."

# Search for pattern
match = re.search(r'fox', text)
if match:
    print(f"Found '{match.group()}' at position {match.start()}")  # Found 'fox' at position 16

# Check if pattern exists
print("'cat' exists:", bool(re.search(r'cat', text)))  # False

# ==============================================================================
# 2. COMMON METACHARACTERS
# ==============================================================================
# . (any character except newline)
print("Match 'q..ck':", re.search(r'q..ck', text).group())  # quick

# \d (digit), \w (word char), \s (whitespace)
print("First digit:", re.search(r'\d+', text).group())  # 42

# [] (character set)
print("Vowel followed by 'x':", re.search(r'[aeiou]x', text).group())  # ox

# ==============================================================================
# 3. REPETITION QUANTIFIERS
# ==============================================================================
# * (0 or more), + (1 or more), ? (0 or 1)
print("Words ending with 's':", re.findall(r'\w+s\b', text))  # ['jumps', 'dogs']

# {n,m} (between n and m repetitions)
print("3-5 letter words:", re.findall(r'\b\w{3,5}\b', text))  # ['The', 'quick', 'brown', 'fox', 'over', 'lazy', 'dogs']

# ==============================================================================
# 4. ANCHORS AND BOUNDARIES
# ==============================================================================
# ^ (start of string), $ (end of string)
print("Starts with 'The':", bool(re.match(r'^The', text)))  # True
print("Ends with 'dogs':", bool(re.search(r'dogs\.$', text)))  # True (escaped dot)

# \b (word boundary)
print("Whole word 'fox':", re.search(r'\bfox\b', text).group())  # fox

# ==============================================================================
# 5. GROUPS AND CAPTURING
# ==============================================================================
# () (capturing group)
date_text = "Today is 2023-08-20"
match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_text)
print(f"Year: {match.group(1)}, Month: {match.group(2)}")  # Year: 2023, Month: 08

# Named groups (?P<name>...)
match = re.search(r'(?P<year>\d{4})-(?P<month>\d{2})', date_text)
print(f"Named groups: {match.groupdict()}")  # {'year': '2023', 'month': '08'}

# ==============================================================================
# 6. SUBSTITUTION AND SPLITTING
# ==============================================================================
# re.sub() (replace matches)
redacted = re.sub(r'\d+', '[NUMBER]', text)
print("Redacted:", redacted)  # The quick brown fox jumps over [NUMBER] lazy dogs.

# re.split() (split by pattern)
words = re.split(r'\W+', text)  # \W = non-word characters
print("Split words:", words)  # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', '42', 'lazy', 'dogs', '']

# ==============================================================================
# 7. FLAGS
# ==============================================================================
case_sensitive = "Python is FUN"
print("Case insensitive 'fun':", re.search(r'fun', case_sensitive, re.IGNORECASE).group())  # FUN

# Multiline mode
multiline_text = "First line\nSecond line"
print("Start of lines:", re.findall(r'^\w+', multiline_text, re.MULTILINE))  # ['First', 'Second']

# ==============================================================================
# 8. REAL-WORLD EXAMPLES
# ==============================================================================
# Email validation
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

print("\nEmail validation:")
print("test@example.com:", is_valid_email("test@example.com"))  # True
print("invalid@email:", is_valid_email("invalid@email"))  # False

# URL extraction
html = '<a href="https://example.com">Link</a>'
url = re.search(r'href="(https?://[^"]+)"', html).group(1)
print("Extracted URL:", url)  # https://example.com

# ==============================================================================
# 9. BEST PRACTICES
# ==============================================================================
"""
1. Use raw strings (r'pattern') to avoid escaping backslashes
2. Precompile patterns with re.compile() for repeated use
3. Be specific - avoid greedy patterns like .* when possible
4. Test patterns with online tools like regex101.com
5. Consider readability - complex regex can be hard to maintain
"""

# ==============================================================================
# EXERCISES
# ==============================================================================
# 1. Create a phone number validator (###-###-####)
# 2. Extract all hashtags from text (#regex #python)
# 3. Redact credit card numbers (XXXX-XXXX-XXXX-1234)