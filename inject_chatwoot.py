import glob

snippet = """
<!-- Chatwoot Widget -->
<script>
  window.chatwootSettings = {"position":"right","type":"standard","launcherTitle":""};
  (function(d,t) {
    var BASE_URL="https://crm.urbanr8.com.mx";
    var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
    g.src=BASE_URL+"/packs/js/sdk.js";
    g.async = true;
    s.parentNode.insertBefore(g,s);
    g.onload=function(){
      window.chatwootSDK.run({
        websiteToken: 'KPjV3uhAnkjFtgJ6rRkvyZBF',
        baseUrl: BASE_URL
      })
    }
  })(document,"script");
</script>
"""

for filepath in glob.glob("*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    if "Chatwoot Widget" not in content:
        # Inject right before </body>
        content = content.replace("</body>", snippet + "\n</body>")
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
            
print("Chatwoot widget injected into all HTML files.")
