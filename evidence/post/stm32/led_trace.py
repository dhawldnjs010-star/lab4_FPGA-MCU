"""시연 영상에서 LED 켜짐/꺼짐 구간을 읽는 스크립트 (실험 후 보고서 표 7·8의 근거).

사용법: python led_trace.py <영상> <task1|task2>
ffmpeg로 원본 영상(1080p)에서 10 fps, 가로 480 px 프레임을 뽑고, LED가 보이는 고정 영역에서
LED 색(과제1: 초록 LD2, 과제2: 빨간 외부 LED)에 해당하는 밝은 화소 수를 센다.
화소 수가 문턱 이상이면 ON으로 보고 연속 구간의 길이를 출력한다. 시간 분해능은 0.1 s.
"""
import glob, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

CFG = {
    # 영역(y0, y1, x0, x1), 색 조건, ON 문턱(화소 수), 분석 시작 시각(s)
    'task1': ((400, 560, 120, 360), lambda r, g, b: (g > 170) & (g - r > 25) & (g - b > 50), 8, 13.0),
    'task2': ((60, 250, 20, 260), lambda r, g, b: (r > 200) & (r - g > 60) & (r - b > 60), 10, 0.0),
}

def main(video, task):
    (y0, y1, x0, x1), cond, th, start = CFG[task]
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(['ffmpeg', '-v', 'error', '-i', video, '-vf', 'fps=10,scale=480:-2',
                        os.path.join(d, '%04d.png')], check=True)
        counts = []
        for f in sorted(glob.glob(os.path.join(d, '*.png'))):
            a = np.asarray(Image.open(f)).astype(int)[y0:y1, x0:x1]
            counts.append(int(cond(a[..., 0], a[..., 1], a[..., 2]).sum()))
    print('t_s,pixels,on')
    for i, n in enumerate(counts):
        print(f'{i/10:.1f},{n},{int(n >= th)}')
    pts = [(i / 10, n >= th) for i, n in enumerate(counts) if i / 10 >= start]
    seg, s = [], pts[0]
    for p in pts[1:]:
        if p[1] != s[1]:
            seg.append((s[0], p[0], s[1])); s = p
    seg.append((s[0], pts[-1][0] + 0.1, s[1]))
    print('# segments: start_s,end_s,duration_s,state', file=sys.stderr)
    for a, b, on in seg:
        print(f'# {a:.1f},{b:.1f},{b-a:.1f},{"ON" if on else "off"}', file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
