import glob

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    content = content.replace('urban-style-cinematic-final.css?v=2.6', 'urban-style-cinematic-final.css?v=2.7')
    content = content.replace('urban-style-final.css?v=2.6', 'urban-style-final.css?v=2.7')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Version bump to v2.7 complete.")
