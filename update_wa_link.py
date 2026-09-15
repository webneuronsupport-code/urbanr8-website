import glob
import urllib.parse

phone = "523328418117"
message = "Hola, me interesa conocer más sobre sus proyectos y servicios de Urban R8."
encoded_message = urllib.parse.quote(message)
new_url = f"https://wa.me/{phone}?text={encoded_message}"
old_url = f"https://wa.me/{phone}"

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace the exact href. We know the current href is just the old_url.
    # To be safe, we replace href="old_url" with href="new_url"
    content = content.replace(f'href="{old_url}" class="whatsapp-float"', f'href="{new_url}" class="whatsapp-float"')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("WhatsApp message update complete.")
