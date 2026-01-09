from tika import parser
import sys

# Suppress processing logs
try:
    parsed = parser.from_file(r'c:\Users\lechi\Documents\Curriculum Vitae\CV\Bach Le - CV.pdf')
    content = parsed["content"]
    if content:
        with open('extracted_cv.txt', 'w', encoding='utf-8') as f:
            f.write(content.strip())
        print("Extraction successful")
    else:
        print("No content found")
except Exception as e:
    print(f"Error: {e}")
