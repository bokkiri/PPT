from pathlib import Path
import base64
import re

root = Path(__file__).parent
p = root / 'index.html'
s = p.read_text(encoding='utf-8')
s = re.sub(r'<style>.*?</style>', '<style>\n'+(root/'design-v2.css').read_text(encoding='utf-8')+'\n</style>', s, flags=re.S)
s = s.replace('원문 기준, 보통교과가 학년당 3개 미만이면 부족분을 9등급으로 처리합니다.', '학년별 반영 교과가 3개 미만이면 부족한 교과 수만큼 9등급으로 처리합니다.')
s = s.replace('3학년 1학기에 보통교과가 적은 특성화고는 반영 과목 수와 부족분 처리 방식을 확인해야 합니다.', '반영 교과 수와 부족분 처리 방식을 확인하세요. 단, 특성화고졸업자전형은 학년별 가중치 없이 전 학년 우수 3개 교과로 산출합니다.')
s = s.replace("&&!e.target.matches('button,a')", '')
s = s.replace("(e.key===' '&&presenting)", "(e.key===' '&&presenting&&!e.target.matches('button,a'))")
s = s.replace('교과(군) 이수단위 가중치 · 요강 p.69', '교과(군) 이수단위 가중치 · PDF 69쪽 / 인쇄 67쪽')
p.write_text(s, encoding='utf-8')
assets = {
    'nazareth.png': 'image/png', 'hanbat.png': 'image/png',
    'hero-book.png': 'image/png',
    'Pretendard-Regular.otf': 'font/otf', 'Pretendard-SemiBold.otf': 'font/otf'
}
for name, mime in assets.items():
    data = base64.b64encode((root / 'assets' / name).read_bytes()).decode()
    s = s.replace('assets/'+name, 'data:'+mime+';base64,'+data)
out = root / '특성화고_진로진학상담.html'
s = s.replace('</head>', '<!-- Bundled Pretendard font license\n'+(root/'assets/Pretendard-LICENSE.txt').read_text(encoding='utf-8')+'\n-->\n</head>')
out.write_text(s, encoding='utf-8')
assert len(re.findall(r'<section class="slide', s)) == 17
assert 'assets/' not in s
print('Created self-contained HTML:', out.name, out.stat().st_size, 'bytes; 17 slides')
