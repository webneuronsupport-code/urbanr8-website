css_to_add = """
/* ===== NEW PUBLICA LAYOUT ===== */
.wrap { max-width: 1120px; margin: 0 auto; padding: 0 24px; }
.eyebrow {
  font-size: 12.5px; text-transform: uppercase; letter-spacing: 0.14em;
  color: var(--primary-gold); font-weight: 600;
}
.hero-new {
  position: relative; overflow: hidden;
  padding: 120px 0 60px;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-main);
}
.hero-grid {
  display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 56px; align-items: center;
}
@media(max-width: 900px){ .hero-grid { grid-template-columns: 1fr; } }
.hero-new h1 { font-size: clamp(34px, 5vw, 54px); line-height: 1.05; margin: 14px 0 20px; color: #fff; }
.hero-new p.lead { font-size: 17.5px; color: var(--text-muted); max-width: 46ch; margin-bottom: 28px; }
.trust-row { display: flex; flex-wrap: wrap; gap: 22px 28px; margin-top: 6px; }
.trust-item { display: flex; align-items: center; gap: 9px; font-size: 14px; color: var(--text-muted); font-weight: 500; }
.trust-dot { width: 7px; height: 7px; border-radius: 50%; background: var(--primary-gold); flex-shrink: 0; }
.skyline {
  position: absolute; right: -40px; bottom: -10px; width: 520px; max-width: 60vw;
  opacity: 0.9; pointer-events: none;
}
@media(max-width:900px){ .skyline{ display: none; } }

.card {
  background: var(--bg-surface); border: 1px solid var(--border-color);
  border-radius: var(--radius-lg); box-shadow: var(--shadow-strong);
  padding: 32px; position: relative; z-index: 2;
}
.card-top { margin-bottom: 20px; }
.card-top .serif { font-size: 22px; color: #fff; margin-bottom: 4px; font-weight: 500; }
.card-top p { font-size: 13.5px; color: var(--text-muted); }
.field { margin-bottom: 14px; }
.field label { display: block; font-size: 12.5px; font-weight: 600; color: #ccc; margin-bottom: 5px; }
.field input, .field select {
  width: 100%; padding: 11px 13px; border: 1px solid var(--border-color); border-radius: 9px;
  background: rgba(255,255,255,0.05); font-family: inherit; font-size: 14.5px; color: #fff;
  transition: all 0.3s ease;
}
.field input:focus, .field select:focus { outline: none; border-color: var(--primary-gold); box-shadow: 0 0 0 2px rgba(250, 204, 21, 0.2); }
.field select option { background: #111; color: #fff; }
.pair { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }
.btn-primary-new {
  width: 100%; background: var(--primary-gold); color: #000; border: none;
  padding: 14px 18px; border-radius: 9px; font-size: 15px; font-weight: 600;
  cursor: pointer; transition: background .15s; margin-top: 6px;
}
.btn-primary-new:hover { background: var(--primary-gold-hover); transform: translateY(-2px); }
.form-note { font-size: 12px; color: var(--text-muted); text-align: center; margin-top: 12px; }
.form-note a { color: var(--primary-gold); text-decoration: underline; }

.section-new { padding: 70px 0; background: var(--bg-main); }
.section-head { max-width: 640px; margin-bottom: 44px; }
.section-head h2 { font-size: clamp(26px, 3.4vw, 36px); margin: 10px 0 12px; color: #fff; font-weight: 500; }
.section-head p { color: var(--text-muted); font-size: 15.5px; }

.steps { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; border-top: 1px solid var(--border-color); }
@media(max-width: 800px) { .steps { grid-template-columns: 1fr 1fr; } }
.step { padding: 26px 20px 26px 0; border-right: 1px solid var(--border-color); }
.step:last-child { border-right: none; }
@media(max-width: 800px) { .step:nth-child(2n) { border-right: none; } .step { border-bottom: 1px solid var(--border-color); } }
.step-num { font-size: 32px; color: var(--primary-gold); opacity: .55; margin-bottom: 10px; font-weight: 500; }
.step h3 { font-size: 16px; margin-bottom: 6px; color: #fff; }
.step p { font-size: 13.8px; color: var(--text-muted); }

.trust-strip { background: var(--bg-surface); color: #fff; padding: 52px 0; border-top: 1px solid var(--border-color); border-bottom: 1px solid var(--border-color); }
.trust-strip .wrap { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }
@media(max-width: 800px) { .trust-strip .wrap { grid-template-columns: 1fr; } }
.quote { font-size: 22px; line-height: 1.4; font-style: italic; color: #fff; }
.quote-attr { margin-top: 14px; font-size: 13.5px; opacity: .75; font-style: normal; }
.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.stat b { display: block; font-size: 34px; color: var(--primary-gold); }
.stat span { font-size: 13px; color: #ccc; }

.detail-section { background: var(--bg-main); border-bottom: 1px solid var(--border-color); padding-bottom: 20px;}
.detail-toggle {
  display: flex; align-items: center; justify-content: space-between;
  padding: 32px 0; cursor: pointer; user-select: none;
}
.detail-toggle h3 { font-size: 18px; color: #fff; }
.detail-toggle .plus { font-size: 24px; color: var(--primary-gold); transition: transform .2s; }
.detail-body { display: none; padding-bottom: 32px; }
.detail-body.open { display: block; }
.detail-toggle.open .plus { transform: rotate(45deg); }
.fieldset-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 18px; }
@media(max-width: 700px) { .fieldset-grid { grid-template-columns: 1fr; } }
.fieldset-label { font-size: 12px; text-transform: uppercase; letter-spacing: .08em; color: var(--primary-gold); font-weight: 700; margin: 22px 0 8px; }
.upload-box {
  border: 1.5px dashed var(--border-color); border-radius: 9px; padding: 22px; text-align: center;
  font-size: 13.5px; color: var(--text-muted); background: rgba(255,255,255,0.02); transition: all 0.3s;
}
.upload-box:hover { border-color: var(--primary-gold); background: rgba(250, 204, 21, 0.05); }
.checkbox-row { display: flex; align-items: center; gap: 8px; font-size: 13.5px; color: var(--text-muted); margin-top: 6px; }

.faq-list { border-top: 1px solid var(--border-color); }
.faq-item { border-bottom: 1px solid var(--border-color); padding: 18px 0; }
.faq-q { display: flex; justify-content: space-between; align-items: center; cursor: pointer; font-weight: 600; font-size: 15.5px; color: #fff; }
.faq-a { display: none; font-size: 14px; color: var(--text-muted); margin-top: 10px; max-width: 65ch; }
.faq-a.open { display: block; }
"""

with open('urban-style-cinematic-final.css', 'a', encoding='utf-8') as f:
    f.write(css_to_add)
print("Appended new styles to CSS.")
