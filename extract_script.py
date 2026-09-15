import json
with open(r'C:\Users\javie\.gemini\antigravity\brain\26a82d8c-7d9b-4dc9-a81f-edd4cbb8860b\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if '"step_index":788' in line:
            data = json.loads(line)
            code = data['tool_calls'][0]['args']['CodeContent']
            with open('extract_css.py', 'w', encoding='utf-8') as out:
                out.write(code)
            break
