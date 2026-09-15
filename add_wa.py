import glob
import os

wa_html = '''
    <!-- WhatsApp Floating Button -->
    <a href="https://wa.me/523328418117" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp">
        <i class="ph-fill ph-whatsapp-logo"></i>
    </a>
</body>'''

for f in glob.glob('*.html'):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the "Servicios" link if it exists
    content = content.replace('<li><a href="#servicios">Servicios</a></li>\n', '')
    content = content.replace('<li><a href="#servicios">Servicios</a></li>', '')
    
    # Add WhatsApp button before </body> if not already added
    if 'whatsapp-float' not in content:
        content = content.replace('</body>', wa_html)
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Processing complete.")
