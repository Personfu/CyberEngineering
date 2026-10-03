"""Build NIGHTSHIFT: deterministic static pages, indexes, and conceptual SVGs.

No network, hardware, tracking, external scripts, or offensive automation.
"""
import argparse
import csv
import hashlib
import html
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'site'
REPO = 'https://github.com/Personfu/CyberEngineering/blob/main/'
def e(x): return html.escape(str(x), quote=True)
def doc(path, label): return f'<a href="reader.html?doc={e(path)}">{e(label)}</a>'
def panel(title, body, tag=''): return f'<section class="panel"><div class="panel-head"><h2>{e(title)}</h2><span>{e(tag)}</span></div>{body}</section>'
def figure(name, caption): return f'<figure><img src="media/{name}.svg" alt="{e(caption)}" loading="lazy"><figcaption>{e(caption)}</figcaption></figure>'
def photo(src, title, credit, source, cls=''):
    return f'<figure class="photo {cls}"><a href="{e(src)}" aria-label="Open {e(title)} at full size"><img src="{e(src)}" alt="{e(title)}" loading="lazy" referrerpolicy="no-referrer"></a><figcaption><strong>{e(title)}</strong><br><a href="{e(source)}">{e(credit)}</a> · '+doc('site/IMAGE-CREDITS.md','Image credits')+'</figcaption></figure>'
def card(title, body, link, label='Open room', kind=''):
    return f'<article class="card" data-search="{e(title+" "+body)}" data-kind="{e(kind)}"><span class="eyebrow">{e(kind)}</span><h3>{e(title)}</h3><p>{e(body)}</p>{link.replace(">", ">", 1)}</article>'
def svg(title, labels, mode='path'):
    # Schematic stages, not measured signal or manufacturer CAD.
    parts=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 340" role="img">',f'<title>{e(title)}</title>','<rect width="800" height="340" fill="#111622"/>',f'<text x="30" y="42" fill="#f6f0e7" font-family="monospace" font-size="20">{e(title)}</text>','<text x="30" y="68" fill="#9ca8b7" font-family="monospace" font-size="12">CONCEPTUAL DIAGRAM · NO HARDWARE MEASUREMENTS</text>']
    colors=['#ff5c85','#57e1e8','#b89aff','#e6b96c']
    for i,label in enumerate(labels):
        x=30+(i%4)*190;y=105+(i//4)*105
        parts += [f'<rect x="{x}" y="{y}" width="170" height="75" rx="8" fill="#192332" stroke="{colors[i%4]}"/>',f'<text x="{x+12}" y="{y+32}" fill="{colors[i%4]}" font-family="monospace" font-size="12">{i+1:02}</text>',f'<text x="{x+12}" y="{y+55}" fill="#f6f0e7" font-family="sans-serif" font-size="13">{e(label)}</text>']
        if i%4<3 and i<len(labels)-1: parts += [f'<path d="M{x+174} {y+38}h12m-5-5 5 5-5 5" fill="none" stroke="#9ca8b7"/>']
    parts+=['</svg>'];return '\n'.join(parts)+'\n'

NAV=[('index','Profile'),('learn','IT + teams'),('tools','Tool room'),('hardware','Hardware'),('missions','Missions'),('talks','DEF CON'),('community','Credits'),('gallery','Visuals')]
def shell(key, title, body):
    nav=''.join(f'<a href="{k}.html" {"aria-current=page" if k==key else ""}>{e(v)}</a>' for k,v in NAV)
    rail=f'''<aside class="rail"><div class="profile-label">MY PROFILE / NIGHTSHIFT</div><a class="avatar" href="hardware.html" aria-label="Explore the hardware bench"><img src="photos/flipper-zero.jpg" alt="Flipper Zero photograph by Turbospok, CC BY-SA 4.0"></a><div class="avatar-credit">Turbospok · CC BY-SA 4.0 · {doc('site/IMAGE-CREDITS.md','credit')}</div><h2>NIGHTSHIFT</h2><p class="handle">@cyberengineering</p><p class="status"><span></span> CURRENTLY: LEARNING THE STACK</p><blockquote>Packets, hardware,<br>and notes from the bench.</blockquote><dl><dt>Home orbit</dt><dd>Project HELIOS</dd><dt>Current track</dt><dd>IT → red / blue → research</dd><dt>Source review</dt><dd>03 OCT 2026</dd></dl><div class="rail-links">{doc('foundations/KALI.md','Kali orientation')}{doc('foundations/MANUALS.md','Read the manual')}{doc('DELIVERY_STATUS.md','Delivery + known gaps')}<a href="community.html">Community credit wall</a><a href="https://github.com/Personfu/CyberEngineering">GitHub repository ↗</a></div><p class="fine">Personal learning notes stay on this browser.</p></aside>'''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="NIGHTSHIFT cyberengineering learning profile: IT, red and blue teams, hardware, research and source-backed conference metadata."><title>{e(title)} · NIGHTSHIFT</title><link rel="icon" href="media/avatar.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><link rel="stylesheet" href="profile.css"><script src="app.js" defer></script></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="index.html">NIGHT<span>SHIFT</span><small>CYBERENGINEERING / PERSONAL LEARNING SPACE</small></a><div class="header-links"><a href="gallery.html">VISUAL LOG</a><a href="https://github.com/Personfu/CyberEngineering">GITHUB ↗</a><button id="theme" aria-label="Toggle light theme">◐</button></div></header><nav aria-label="Rooms">{nav}</nav><div class="layout">{rail}<main id="main">{body}</main></div><footer><span>NIGHTSHIFT / HELIOS · Original design, NASA-inspired names</span><span>Sources, synthetic data and proposals are labeled. No NASA affiliation.</span></footer></body></html>'''

def build():
    files={}
    def put(path, content): files[ROOT/path]=content if isinstance(content,bytes) else content.encode()
    ideas=json.loads((ROOT/'data/ideas.json').read_text())['ideas']
    community=json.loads((ROOT/'data/community/catalog.json').read_text())
    talks=json.loads((ROOT/'data/conferences/defcon.json').read_text())
    sources={s['id']:s['url'] for s in community['sources']}
    diagrams={
      'team-loop':('RED / BLUE / PURPLE', ['Question a control','Observe evidence','Compare outcomes','Improve + retest']),
      'packet-path':('READ A PACKET', ['Packet bytes','Dissector','Protocol fields','Context + limits']),
      'manual-map':('READ THE MANUAL', ['Name + synopsis','Options','Exit status','Version + examples']),
      'flipper':('FLIPPER ZERO · INTERFACES', ['Physical interface','Front end','Firmware app','Display / host']),
      'proxmark':('PROXMARK3 · MEASUREMENT', ['Reference fixture','RF front end','Signal processing','Host interpretation']),
      'chameleon':('CHAMELEON ULTRA · MODEL', ['Host configuration','Device firmware','Supported interface','Test evidence']),
      'pager':('PINEAPPLE PAGER · MODEL', ['Model + firmware','Radio subsystem','Local interface','Management client']),
      'router':('ROUTER · SERVICE PATH', ['Local device','Wireless access','IP forwarding','Service response']),
      'provenance':('SOURCE / CLAIM / EVIDENCE', ['Publisher source','Pinned version','Bounded claim','Review + uncertainty']),
      'research-loop':('A GRADUATE RESEARCH LOOP', ['Hypothesis','Baseline + split','Estimate uncertainty','Ablation + revision']),
      'talk-coverage':('CONFERENCE COVERAGE', ['Schedule metadata','Session identity','Media availability','Content review']),
    }
    for name,(title,labels) in diagrams.items():put(Path('site/media')/(name+'.svg'),svg(title,labels))
    put(Path('site/media/avatar.svg'),'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#111622"/><circle cx="32" cy="32" r="18" fill="none" stroke="#57e1e8" stroke-width="3"/><ellipse cx="32" cy="32" rx="28" ry="9" transform="rotate(-27 32 32)" fill="none" stroke="#ff5c85" stroke-width="3"/></svg>\n')
    for p in sorted((ROOT/'research/assets').glob('*.svg')):put(Path('site/media/research')/p.name,p.read_bytes())
    # Local fixture is transparently synthetic and fully reproducible.
    out=io.StringIO();w=csv.writer(out,lineterminator='\n');w.writerow(['group','fixture','repeat','latency_ms','provenance'])
    for g,base in [('A',12),('B',10)]:
        for f in range(1,4):
            for r in range(10):w.writerow([g,f,r+1,f'{base+f*.2+((r*7)%9-4)*.15:.2f}','synthetic_arithmetic_not_hardware'])
    put(Path('data/hardware/timing.csv'),out.getvalue())
    docs={}
    for folder in ['foundations','hardware','conferences','community','research','assessment','intelligence','atlas']:
        for p in sorted((ROOT/folder).rglob('*.md')):docs[p.relative_to(ROOT).as_posix()]=p.read_text()
    docs['DELIVERY_STATUS.md']=(ROOT/'DELIVERY_STATUS.md').read_text()
    docs['SOURCES.md']=(ROOT/'SOURCES.md').read_text()
    docs['site/IMAGE-CREDITS.md']=(ROOT/'site/IMAGE-CREDITS.md').read_text()
    put(Path('site/data/documents.json'),json.dumps(docs,ensure_ascii=False,separators=(',',':'))+'\n')
    missionlist=[dict(id=x['id'],title=x['title'],theme=x['theme'],thesis=x['thesis'],doc=f'research/missions/{x["id"]}.md') for x in ideas]
    for p in sorted((ROOT/'research/frontier').glob('*.md')):
        s=p.read_text();title=s.splitlines()[0].lstrip('# ');missionlist.append(dict(id=p.stem,title=title,theme='Frontier / NASA-inspired proposals',thesis='Graduate research proposal; implementation and validation remain future work.',doc='research/frontier/'+p.name))
    assert len(missionlist)==180
    put(Path('site/data/missions.json'),json.dumps(missionlist,ensure_ascii=False,separators=(',',':'))+'\n')
    put(Path('site/data/talks.json'),json.dumps(talks,ensure_ascii=False,separators=(',',':'))+'\n')
    pager_url='https://shop.hak5.org/cdn/shop/files/wifi-pineapple-pager-black-white_bg.png?v=1754446127&width=1200'
    chameleon_url='https://raw.githubusercontent.com/RfidResearchGroup/ChameleonUltra/main/docs/images/ultra-overview.png'
    wireshark_url='https://www.wireshark.org/docs/wsug_html_chunked/images/ws-main.png'
    burp_url='https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-proxy-history.png'
    hero='''<section class="hero"><div class="window-bar"><span>nightshift.profile</span><span aria-hidden="true">— □ ×</span></div><div class="hero-copy"><p class="eyebrow">IT / RED + BLUE / HARDWARE</p><h1>Cyberengineering,<br><em>after hours.</em></h1><p>A corner of the web for the tools, projects and questions worth keeping.</p><div class="hero-actions"><a class="button" href="learn.html">Learn the basics</a><a class="button ghost" href="missions.html">Explore the missions</a></div></div><div class="hero-photo">'''+photo('photos/flipper-zero.jpg','Flipper Zero / real hardware','Turbospok · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Flipper_Zero.jpg')+'''<span class="photo-sticker">HARDWARE / SOFTWARE / CURIOSITY</span></div></section>'''
    stats='<div class="stats">'+''.join(f'<div><strong>{n}</strong><span>{e(t)}</span></div>' for n,t in [(150,'original missions'),(180,'research dossiers'),(20,'core tool guides'),(len(talks['records']),'retrieved sessions')])+'</div>'
    rooms=''.join(card(t,b,f'<a href="{k}.html">Enter {e(t.lower())} →</a>',kind=tag) for k,t,b,tag in [
        ('learn','The learning lounge','Start with IP, DNS, sockets and HTTP. Then learn what red, blue and purple teams each measure.','MERCURY / FOUNDATIONS'),
        ('hardware','The hardware bench','Flipper, Proxmark, Chameleon and Pineapple. Interfaces, measurement limits and graduate challenges.','VOYAGER / DEVICES'),
        ('talks','The signal library','DEF CON 34 session metadata, source coverage and a browser-local reading list.','SIGNAL / CONFERENCES'),
        ('community','The credit wall','RocketGod and ProtoPirate publisher credits, inspected links and source receipts.','ORION / COMMUNITY')])
    notebook='''<label for="note">Your field note</label><textarea id="note" rows="3" maxlength="4000" placeholder="What did you learn? What evidence would change your mind?"></textarea><div class="note-actions"><button id="save-note">Save on this browser</button><button id="clear-note">Clear note</button><span id="note-status" role="status">Private to this browser; not sent to a server.</span></div>'''
    featured=''.join(card(x['title'],x['thesis'],doc(x['doc'],'Read the dossier →'),kind='MISSION '+x['id']) for x in missionlist[:3])
    screenwall='<div class="screen-wall">'+photo(wireshark_url,'Wireshark / packet anatomy','Wireshark user guide','https://www.wireshark.org/docs/wsug_html_chunked/ChapterUsing.html','screen')+photo(burp_url,'Burp / HTTP history','PortSwigger documentation','https://portswigger.net/burp/documentation/desktop/getting-started','screen')+'</div><p class="image-note">Real publisher screenshots. '+doc('foundations/SCREENSHOTS.md','Learn to read the screen regions')+'.</p>'
    album='<div class="album">'+photo('photos/proxmark3.png','Proxmark3 / legacy board','Proxmark.com · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:PM3-Trans.png')+photo(chameleon_url,'Chameleon Ultra','RfidResearchGroup / publisher overview','https://github.com/RfidResearchGroup/ChameleonUltra')+photo(pager_url,'WiFi Pineapple Pager','Hak5 / publisher product image','https://shop.hak5.org/products/pager')+'</div>'
    pages={ 'index':('Profile',hero+stats+panel('My screen album',screenwall,'ACTUAL TOOL INTERFACES')+panel('My spaces','<div class="cards">'+rooms+'</div>','PAGES / SUBPAGES / NOTES')+panel('Hardware album',album,'PHOTOGRAPHS + PUBLISHER IMAGES')+panel('Pinned projects','<div class="cards">'+featured+'</div>','ALL 180 DOSSIERS PRESERVED')+panel('About this notebook','<p>The original 150 HELIOS proposals, thirty frontier proposals and 150 assessment modules stay connected to their models, source ledgers and experiments. Research proposals are questions to investigate; their performance has not been established.</p>'+doc('research/README.md','Browse the research flightbook'))+panel('Field notebook',notebook,'LOCAL ONLY')) }
    learn=panel('Start here','<p class="lead">Before the tools, learn the system.</p><div class="cards">'+''.join(card(t,b,doc(p,'Read the guide →'),kind=k) for t,b,p,k in [
       ('01 / Everyday IT','Interfaces, routes, sockets, DNS, TLS and HTTP. Understand what each layer can tell you.','foundations/IT.md','FOUNDATION'),
       ('02 / Red, blue, purple','Red tests assumptions, blue observes and responds, purple joins the evidence and improves controls.','foundations/TEAMS.md','TEAM CONCEPTS'),
       ('03 / Kali orientation','Kali packages tools. Learn versions, package documentation and a clean local environment.','foundations/KALI.md','WORKSTATION'),
       ('04 / Six local labs','A harmless HTTP service, synthetic event triage, digest verification and manual-reading practice.','foundations/LABS.md','PRACTICE')])+'</div>')
    learn+=panel('Who asks what?','<div class="team-grid"><div><span class="team red">RED</span><h3>Question assumptions</h3><p>What claim about a control deserves an agreed test? What evidence would show a gap?</p></div><div><span class="team blue">BLUE</span><h3>Observe and recover</h3><p>Which events are recorded, which are missing, and can the system recover reliably?</p></div><div><span class="team purple">PURPLE</span><h3>Compare together</h3><p>Join the question to the observation. Fix the gap and repeat the same comparison.</p></div></div>'+figure('team-loop','Shared conceptual workflow; no attack automation.'))
    learn+=panel('A local HTTP tutorial','<p>From the repository root, start the supplied harmless web fixture. Open a second terminal to inspect its response.</p><pre><code>python -m http.server 8765 --bind 127.0.0.1 --directory foundations/fixtures/web\ncurl --noproxy \'*\' --include http://127.0.0.1:8765/health.json</code></pre><p><strong>Read the output:</strong> HTTP status, Content-Type and JSON body describe different parts of the result. Stop the server with Ctrl+C. Use '+doc('foundations/LABS.md','the full lab')+' to compare HTTP errors and transport errors.</p>')
    learn+=panel('Read the manual',figure('manual-map','Four manual-reading checkpoints.')+doc('foundations/MANUALS.md','Man sections, synopsis notation, pager shortcuts and tool-specific help →'))
    pages['learn']=('IT + team concepts',learn)
    raw=(ROOT/'foundations/TOOLS.md').read_text();toolcards=[]
    for m in re.finditer(r'^### (\d+) · ([^\n]+)\n\n(.+?)(?=\n\n|\Z)',raw,re.M|re.S):
        title=m[2];body=m[3];what=re.search(r'\*\*Does:\*\* (.*?)(?=\*\*How:)',body,re.S);how=re.search(r'\*\*How:\*\* (.*?)(?=\*\*Read:)',body,re.S)
        toolcards.append(card(title,(what[1].strip() if what else '')+' How: '+(how[1].strip() if how else ''),doc('foundations/TOOLS.md','Evidence limits + official reference →'),kind='CORE TOOL '+m[1]))
    assert len(toolcards)==20
    pages['tools']=('Tool room',panel('Screen album',screenwall,'LOOK / READ / UNDERSTAND')+panel('Tool room','<p class="lead">What it does. How it works. What the output means.</p><p>Twenty core entries connect everyday IT to security observation. Installed manuals and versions matter.</p><label for="search">Find a tool</label><input id="search" type="search" placeholder="Try DNS, packets, curl or YARA"><p id="result-count" role="status"></p><div class="cards searchable">'+''.join(toolcards)+'</div>')+panel('Packet anatomy',figure('packet-path','A dissector interprets bytes; interpretation still needs capture context.')))
    hardware=[('flipper','Flipper Zero','Portable physical-interface learning; distinguish each radio, RFID/NFC, infrared or wired front end.','https://docs.flipper.net/'),('proxmark','Proxmark3','RFID research architecture: reference fixture, front end, signal processing, firmware and host client.','https://github.com/RfidResearchGroup/proxmark3/wiki'),('chameleon','Chameleon Ultra','Configurable RFID research/emulation platform. Device firmware and compatible host clients must be versioned together.','https://github.com/RfidResearchGroup/ChameleonUltra'),('pager','WiFi Pineapple Pager','A distinct portable Pineapple family with local and management interfaces; use its own documentation.','https://documentation.hak5.org/wifi-pineapple-pager'),('router','WiFi Pineapple Mark VII','Wi-Fi assessment appliance with a browser management interface. Distinguish it from Pager and Enterprise.','https://documentation.hak5.org/wifi-pineapple'),('router','WiFi Pineapple Enterprise','Separate hardware/product family. Confirm the exact manual, installed firmware and supported functions.','https://documentation.hak5.org/wifi-pineapple-enterprise'),('router','Ordinary Wi-Fi router','Learn access, addressing, forwarding and service availability. Exact vendor/model documentation remains unspecified.',None)]
    device_images={
       'Flipper Zero':('photos/flipper-zero.jpg','Turbospok · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Flipper_Zero.jpg'),
       'Proxmark3':('photos/proxmark3.png','Proxmark.com · legacy hardware · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:PM3-Trans.png'),
       'Chameleon Ultra':(chameleon_url,'RfidResearchGroup / publisher overview','https://github.com/RfidResearchGroup/ChameleonUltra'),
       'WiFi Pineapple Pager':(pager_url,'Hak5 / publisher product image','https://shop.hak5.org/products/pager'),
    }
    hw=''
    for k,title,body,url in hardware:
        visual=photo(device_images[title][0],title,device_images[title][1],device_images[title][2]) if title in device_images else figure(k,title+' conceptual architecture; no sourced product image in this entry.')
        hw+='<article class="device">'+visual+f'<div><span class="eyebrow">DEVICE LITERACY</span><h2>{e(title)}</h2><p>{e(body)}</p>'+ (f'<a href="{url}">Official documentation ↗</a>' if url else '<p>Record vendor, model and firmware first.</p>')+'<details><summary>Conceptual data path</summary>'+figure(k,title+' · conceptual model, not manufacturer CAD.')+'</details></div></article>'
    pages['hardware']=('Hardware bench',panel('VOYAGER / hardware bench','<p class="lead">Choose the question before the gadget.</p><p>Seven distinct device/model entries. These are learning references, not an inventory of equipment owned or tested.</p>'+doc('hardware/README.md','Bench session, limits, six graduate challenges and synthetic data →'))+hw+panel('Timing is a measurement problem','<p>The 60-row synthetic fixture has two fictional groups, three fixtures and repeated observations. Compare within-fixture variation before pooling groups. No hardware latency or RF range is measured.</p>'+doc('hardware/README.md','Study V01–V06 →')+'<a class="secondary-link" href="'+REPO+'data/hardware/timing.csv">Download source fixture ↗</a>'))
    pages['missions']=('Mission atlas',panel('180 research dossiers','<p class="lead">Keep every project. Push each question further.</p><p>150 original HELIOS missions + 30 frontier proposals. Models, datasets, experiment contracts, sources and challenges live in each dossier.</p><label for="search">Search missions</label><input id="search" type="search" placeholder="Try firmware, privacy, recovery or spacecraft"><label for="kind">Research domain</label><select id="kind"><option value="">All domains</option>'+''.join('<option>'+e(x)+'</option>' for x in dict.fromkeys(m['theme'] for m in missionlist))+'</select><p id="result-count" role="status"></p><div id="mission-cards" class="cards searchable"></div><noscript><p>JavaScript is needed for the filter. '+doc('research/README.md','Use the full research index')+'.</p></noscript>')+panel('Assessment track',doc('assessment/README.md','150 red / blue assessment modules →')+figure('research-loop','Proposed evaluation workflow: baseline, independent split, uncertainty and ablation.')))
    pages['talks']=('DEF CON library',panel('SIGNAL / DEF CON 34 onward',f'<p class="lead">{len(talks["records"])} retrieved sessions. Coverage stays explicit.</p><p>20 Recon Village schedule entries and 12 Adversary Village creator-stage entries. Main stages, other villages, videos and slides remain unresolved. DEF CON 35 is a future event at the source review date.</p>'+doc('conferences/README.md','Read the coverage ledger →')+'<label for="search">Search session metadata</label><input id="search" type="search" placeholder="Title, public speaker label or village"><label for="kind">Session type</label><select id="kind"><option value="">All types</option><option>Talk</option><option>Workshop</option><option>Panel</option><option value="bookmarked">My bookmarks</option></select><p id="result-count" role="status"></p><div id="talk-cards" class="cards searchable"></div>')+panel('Four different coverage questions',figure('talk-coverage','A scheduled title, a recording and reviewed scientific evidence are different records.')))
    credits=community.get('credits',[])
    if not credits: credits=community.get('public_credits',[])
    assert len(credits)==15,community.keys()
    wall=''.join(f'<article class="credit"><span class="credit-icon" aria-hidden="true">{e(c["label"][:2].upper())}</span><h3>{e(c["label"])}</h3><p>{e(" · ".join(c["roles"]))}</p><a href="{e(sources[c["source_id"]])}">Pinned credit source ↗</a></article>' for c in credits)
    pages['community']=('Community credits',panel('ORION / credit wall','<p class="lead">Public credits. Traceable sources.</p><p>A MySpace-inspired credit wall containing all fifteen unique attribution labels in the pinned ProtoPirate README. These are publisher credits, including a driver reference; they do not verify personal friendships, real identities or current membership.</p><div class="credit-wall">'+wall+'</div>')+panel('Source spaces','<div class="cards">'+''.join(card(t,b,doc(p,'Read the source review →'),kind='PUBLIC SOURCE') for t,b,p in [('RocketGod / BetaSkyNet','Reviewed public website repository and link hub; source receipts record the inspected version and unresolved reuse license.','community/ROCKETGOD.md'),('ProtoPirate','Pinned README, credits and license receipts; publisher-designated upstream access remains blocked.','community/PROTOPIRATE.md'),('Map-source review','Published map descriptions require separate validation. A site name does not establish that anyone is targeted.','community/MAP-SOURCE-REVIEW.md'),('Church of Malware forge','50 distinct repository metadata records across inspected pages and namespace; page three unavailable.','intelligence/CHURCH-FORGE.md')])+'</div>')+panel('Claims need boundaries',figure('provenance','Publisher descriptions are attributed; identity and capability claims need separate evidence.')))
    gallery=''
    for name,caption in [('telemetry','Synthetic telemetry experiment'),('recovery','Synthetic recovery experiment'),('firmware','Synthetic firmware evidence experiment'),('clocks','Synthetic clock alignment experiment'),('privacy','Synthetic privacy experiment'),('contacts','Synthetic contact experiment'),('kev','Pinned CISA known-exploited-vulnerability metadata snapshot')]:
        gallery+=f'<figure class="wide-figure"><img src="media/research/{name}.svg" alt="{e(caption)}" loading="lazy"><figcaption>{e(caption)} · '+doc('research/EXPERIMENTS.md','Methods, units and limits')+'</figcaption></figure>'
    screenshots=[('Wireshark / three panes','https://www.wireshark.org/docs/wsug_html_chunked/images/ws-main.png','https://www.wireshark.org/docs/wsug_html_chunked/ChapterUsing.html'),('Burp / HTTP history','https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-proxy-history.png','https://portswigger.net/burp/documentation/desktop/getting-started'),('Burp / intercepted request','https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-intercepted-request.png','https://portswigger.net/burp/documentation/desktop/getting-started')]
    for title,url,source in screenshots:gallery+=f'<figure class="wide-figure"><img class="publisher-image" src="{e(url)}" alt="{e(title)}: actual publisher screenshot" loading="lazy" referrerpolicy="no-referrer"><figcaption>{e(title)} · Publisher image; rights remain with publisher. <a href="{source}">Documentation ↗</a> · '+doc('foundations/SCREENSHOTS.md','Reading guide + hash receipts')+'</figcaption></figure>'
    pages['gallery']=('Visual log',panel('The photo + screen albums','<p class="lead">Actual hardware. Actual interfaces.</p><p>Credited hardware photographs, publisher product images and software screen captures. '+doc('site/IMAGE-CREDITS.md','Sources, licenses and image receipts')+'.</p>')+panel('Hardware album',photo('photos/flipper-zero.jpg','Flipper Zero photograph','Turbospok · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Flipper_Zero.jpg')+album)+panel('Proxmark manual in the wild',photo('photos/proxmark-help.png','Proxmark3 RDV4 help / 2021 interface','Turbospok · CC BY-SA 4.0','https://commons.wikimedia.org/wiki/File:Proxmark_help.png','screen')+'<p>Read command groups and the help hint first. This is a historical screenshot, not a recipe or a claim about your installed version.</p>')+panel('Data + interface gallery','<p>Seven reproducible research figures and three publisher tool screenshots. Synthetic results and external assets are labeled.</p>')+gallery+panel('Diagram collection','<div class="diagram-grid">'+''.join(figure(n,t+' · conceptual') for n,(t,_) in diagrams.items())+'</div>'))
    pages['reader']=('Document reader',panel('Document room','<p id="reader-status" role="status">Loading the selected repository document…</p><a id="source-link" href="'+REPO+'README.md">Canonical source on GitHub ↗</a><article id="document" class="prose"></article><noscript>Enable JavaScript or use the canonical repository documents.</noscript>'))
    for key,(title,body) in pages.items():put(Path('site')/(key+'.html'),shell(key,title,body))
    put(Path('site/.nojekyll'),'')
    return files

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    files=build();bad=[]
    for p,content in files.items():
        if args.check:
            if not p.exists() or p.read_bytes()!=content:bad.append(str(p.relative_to(ROOT)))
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(content)
    if bad:raise SystemExit('Stale outputs: '+', '.join(bad))
    print(f'NIGHTSHIFT: {len(files)} deterministic outputs; 180 missions; 32 session records; 60 synthetic timing rows')
if __name__=='__main__':main()
