"""data/*.json 을 읽어 index.html(최신) 과 archive/YYYY-MM-DD.html 을 만든다.
데이터는 HTML 안의 <script type="application/json"> 에 그대로 들어간다."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data"
ARCHIVE = ROOT / "archive"
TEMPLATE = (ROOT / "template.html").read_text(encoding="utf-8")


def embed(obj):
    # </script> 등으로 HTML이 깨지지 않도록 '<' 를 이스케이프
    return json.dumps(obj, ensure_ascii=False).replace("<", "\\u003c")


def render(report, dates, base):
    return (TEMPLATE
            .replace("__DATE__", report["date"])
            .replace("__BASE__", base)
            .replace("__ARCHIVE__", embed(dates))
            .replace("__DATA__", embed(report)))


def main():
    ARCHIVE.mkdir(exist_ok=True)
    files = sorted(DATA.glob("*.json"), reverse=True)
    if not files:
        raise SystemExit("data/ 에 리포트가 없습니다")
    dates = [f.stem for f in files]
    for f in files:
        report = json.loads(f.read_text(encoding="utf-8"))
        (ARCHIVE / f"{f.stem}.html").write_text(render(report, dates, "../"), encoding="utf-8")
    latest = json.loads(files[0].read_text(encoding="utf-8"))
    (ROOT / "index.html").write_text(render(latest, dates, ""), encoding="utf-8")
    print(f"built index.html + {len(files)} archive page(s); latest = {dates[0]}")


if __name__ == "__main__":
    main()
