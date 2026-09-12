from pathlib import Path
import re, shutil

root = Path(__file__).parent
p = root / 'index.html'
old = p.read_text(encoding='utf-8')
backup = root / 'previous-design'
backup.mkdir(exist_ok=True)
for name in ['index.html', '특성화고_진로진학상담.html']:
    if not (backup/name).exists():
        shutil.copy2(root/name, backup/name)
fontroot = root.parent / 'slide-master/.claude/skills/ppt-master/assets/fonts/Pretendard'
for name in ['Pretendard-Regular.otf','Pretendard-SemiBold.otf']:
    shutil.copy2(fontroot/name, root/'assets'/name)
shutil.copy2(fontroot/'LICENSE.txt', root/'assets/Pretendard-LICENSE.txt')
s = re.sub(r'<style>.*?</style>', '<style>\n'+(root/'design-v2.css').read_text(encoding='utf-8')+'\n</style>', old, flags=re.S)
s = s.replace('<header class="topbar">','<header class="topbar"><div class="global-nav"><div class="global-inner"><span>순천향대학교 · 진로진학상담전공 특강</span><span>천안제일고등학교 최훈석 &nbsp; / &nbsp; 9월 22일</span></div></div>')
s = s.replace('<span class="mark" aria-hidden="true"></span>진로의 다음 페이지','<span class="mark" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none"><path d="M3 4.5c3.5-1 6.5-.4 9 2 2.5-2.4 5.5-3 9-2v15c-3.5-1-6.5-.4-9 2-2.5-2.4-5.5-3-9-2zM12 6.5v15" stroke="currentColor" stroke-width="1.5" stroke-linejoin="round"/></svg></span>진로진학상담')

def section(id, markup):
    global s
    s = re.sub(r'<section\b[^>]*id="'+id+r'".*?</section>', markup, s, flags=re.S)

section('s01', '''<section class="slide hero" id="s01" data-title="표지"><div class="wrap"><div class="eyebrow reveal">특성화고 진로진학상담의 기법과 전략</div><h1 class="reveal">학생의 다음을.<br><span>함께 그리다.</span></h1><p class="hero-label reveal">진학과 취업, 두 갈래 가능성을 잇는 상담.</p><div class="actions reveal"><a class="pill" href="#s02">시작하기</a><button class="pill secondary-pill" data-toc>전체 슬라이드</button></div><img class="hero-image reveal" src="assets/hero-book.png" alt="열린 책의 종이가 두 갈래 길로 이어지는 오브제" fetchpriority="high"><div class="hero-credit reveal">천안제일고등학교 진로교사 최훈석 · 9월 22일</div><div class="hero-bottom reveal"><span>전문대</span><span>4년제</span><span>계약학과 · 폴리텍</span><span>선취업 후진학</span></div></div></section>''')
section('s02', '''<section class="slide dark" id="s02" data-title="왜 상담이 다른가"><div class="wrap"><div class="eyebrow reveal">관점의 전환</div><h2 class="reveal">한 학생 앞에,<br>두 개의 길.</h2><p class="subtitle reveal">특성화고 학생의 진로는 진학, 그리고 취업입니다.</p><div class="duality"><div class="reveal"><div class="context">일반고의 진로</div><div class="words"><span>진로 ≈</span>대학 진학</div><p>대부분 진학으로 가고, 진로지도의 초점도 진학 한 축에 모입니다.</p></div><div class="reveal"><div class="context">특성화고의 진로</div><div class="words">진학 +<br>취업</div><p>한 학생 앞에 두 길이 동시에 열립니다. 어느 한쪽도 작지 않습니다.</p><div class="dual-label"><span>우리 학교 예 · 진학 47%</span><span>취업 31%</span></div></div></div><div class="callout reveal">두 축을 함께 보고, 오늘은 그중 <strong>진학 전략</strong>을 깊이 다룹니다.<br><small>학교 예시 비율 · 제외인정 인원 별도</small></div></div></section>''')
section('s03', '''<section class="slide white" id="s03" data-title="데이터로 보는 현실"><div class="wrap"><div class="eyebrow reveal">데이터로 보는 현실</div><h2 class="reveal">진학이 절반.<br>그중 전문대가 더 많습니다.</h2><div class="grid stats-grid"><div class="stat-main reveal"><span class="dim">천안제일고 2025 졸업 · 요약 기준 140명</span><div class="number"><b data-count="47.1">47.1</b><span>%</span></div><p>졸업생 절반이 대학으로.<br>그만큼 진학 상담의 수요가 큽니다.</p></div><div class="reveal"><div class="stat-chart"><div class="donut" role="img" aria-label="진학자 66명 중 전문대 36명, 4년제 30명"><svg viewBox="0 0 220 220" aria-hidden="true"><circle class="track" cx="110" cy="110" r="90" stroke-width="17" fill="none"/><circle class="arc" cx="110" cy="110" r="90" stroke-width="17" fill="none"/></svg><div class="donut-label"><strong>66</strong><span>전체 진학자</span></div></div><div class="stat-legend"><div class="legend-row"><i></i>전문대학<strong>36명</strong></div><div class="legend-row muted"><i></i>4년제 대학<strong>30명</strong></div></div></div><p class="stat-foot">진학자 66명 중 비중 · 전문대 54.5% / 4년제 45.5%</p></div></div><div class="callout reveal">상담의 무게중심도 <strong>전문대 · 동일계열 진학</strong>에 먼저 놓여야 합니다.</div></div></section>''')
section('s04', '''<section class="slide" id="s04" data-title="진학 경로 지도"><div class="wrap"><div class="eyebrow reveal">진학 경로 한눈에</div><h2 class="reveal">길은 하나가<br>아니니까.</h2><p class="subtitle reveal">학생과 함께 이 지도를 펼치는 것부터가 상담의 시작입니다.</p><div class="route-map"><div class="route-column reveal"><div class="route-head"><span class="route-letter">A</span><h3>졸업 직후<br>바로 진학</h3></div><div class="route-step"><strong>전문대 · 폴리텍</strong><p>가장 큰 실질 경로 · 실무형 학위</p></div><div class="route-step"><strong>4년제 대학</strong><p>교과 · 학종 · 특별전형</p></div><div class="route-step"><strong>조기취업형 계약학과</strong><p>취업과 학위를 함께</p></div></div><div class="route-column reveal"><div class="route-head"><span class="route-letter">B</span><h3>먼저 취업,<br>뒤에 진학</h3></div><div class="route-step"><strong>일학습병행제</strong><p>일하며 학습하는 경로</p></div><div class="route-step"><strong>재직자 특별전형</strong><p>3년 뒤 열리는 문</p></div><p class="route-caption">지금의 선택이<br>마지막 선택은 아닙니다.</p></div></div></div></section>''')
# Deliberate alternating surfaces, retaining the 17 original topics and evidence.
surfaces={'s05':'dark','s06':'white','s07':'','s08':'dark','s09':'white','s10':'dark','s11':'','s12':'dark','s13':'white','s14':'','s15':'dark','s16':'white center','s17':'dark center thanks'}
for id,theme in surfaces.items():
    s=re.sub(r'<section class="[^"]*" id="'+id+r'"', '<section class="slide '+theme+'" id="'+id+'"',s)
s=re.sub(r'(<div class="eyebrow reveal">)\d+ / ',r'\1',s)
s=s.replace('CAREER COUNSELING · NEXT CHAPTER','특성화고 진로진학상담')
s=s.replace("const hero=slides[0];if(!reduce.matches&&hero.getBoundingClientRect().bottom>0){hero.querySelector('.halo').style.transform='translate(-50%,calc(-20% + '+Math.min(scrollY*.12,150)+'px)) rotate('+(-12+scrollY*.012)+'deg)'}",'')
# Fit again after bundled Korean fonts and images have loaded.
s=s.replace("const start=slides.findIndex", "document.fonts.ready.then(fitSlide);document.querySelectorAll('img').forEach(img=>img.addEventListener('load',fitSlide));\nconst start=slides.findIndex")
p.write_text(s,encoding='utf-8')
print('Redesigned all 17 slides; original files preserved in previous-design')
