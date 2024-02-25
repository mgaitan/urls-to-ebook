import subprocess
import markdownify
import json
import os 
from pathlib import Path
from glob import glob
import tempfile
from datetime import datetime


def parse(url):
    cmd = ["mercury-parser", url]
    data = json.loads(subprocess.check_output(cmd, text=True))
    md = f"<h1>{data['title']}</h1>\n<p>{data['author'] or ''} - {data['url']}</p><hr>{data['content']}"
    return markdownify.markdownify(md)


def main():
    urls = [url.strip() for url in os.getenv("URLS").split(";")]
    with tempfile.TemporaryDirectory() as d:
        for i, url in enumerate(urls):
            if not url:
                continue
            print(f"processing {url}")
            md = parse(url)
            (Path(d) / f"{i:02}.md").write_text(md)

        date = datetime.now().strftime('%Y-%m-%d')
        output = f"news_{date}.epub"
        title = f"News {date}"
        subprocess.run(["pandoc", *glob(f"{d}/*.md"), "--metadata", f'title="{title}"', '--toc', '--toc-depth=1', '-o', output])
        subprocess.run(["ebook-convert", output, f"{output}.mobi"])
        print(list(Path(d).iterdir()))


if __name__ == '__main__':
    main()