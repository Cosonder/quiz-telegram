# 生成 Telegram 小程序用的网页：把网站版（Cosonder/quiz 仓库的 french/）复制过来，加上 Telegram 适配。
# 用法：python3 tools/build.py <quiz 仓库路径>
# 输出到仓库根目录的 index.html、img/ 和 skins/（GitHub Pages 直接发布根目录）。
import os, re, shutil, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, "..", "quiz")
page = open(os.path.join(src, "french", "index.html"), encoding="utf-8").read()
def rep(a, b):
    global page
    assert a in page, a[:60]
    page = page.replace(a, b, 1)
# 不注册离线缓存（Telegram 里每次都从网络加载最新版），也不要网站的 manifest
page = re.sub(r'<link rel="manifest"[^>]*>', "", page)
rep('serviceWorker" in navigator) || location.protocol === "file:") return', 'serviceWorker" in navigator) || location.protocol === "file:" || true) return')
# 去掉“全部练习”的链接（Telegram 里只有法语页）
page = re.sub(r'<a class="home" href="\.\./">[^<]*</a>', "", page)
# 皮肤背景图：网站版在 french/ 的上一层（../skins/），这里放在根目录的 skins/
page = page.replace("../skins/", "skins/")
adapter = open(os.path.join(root, "src", "tg-adapter.js"), encoding="utf-8").read()
css = open(os.path.join(root, "src", "tg.css"), encoding="utf-8").read()
rep("</head>", '<script src="https://telegram.org/js/telegram-web-app.js"></script>\n<style>\n' + css + "</style>\n</head>")
i = page.rindex("</body>") if "</body>" in page else len(page)
page = page[:i] + "<script>\n" + adapter + "</script>\n" + page[i:]
open(os.path.join(root, "index.html"), "w", encoding="utf-8").write(page)
img = os.path.join(root, "img")
if os.path.exists(img): shutil.rmtree(img)
shutil.copytree(os.path.join(src, "french", "img"), img)
sk = os.path.join(root, "skins")
if os.path.exists(sk): shutil.rmtree(sk)
if os.path.isdir(os.path.join(src, "skins")): shutil.copytree(os.path.join(src, "skins"), sk)
# 英文、法语语言包（选了这个语言才下载），和页面放在一起
for f in os.listdir(root):
    if re.fullmatch(r"lang-\w+\.js", f): os.remove(os.path.join(root, f))
for f in os.listdir(os.path.join(src, "french")):
    if re.fullmatch(r"lang-\w+\.js", f): shutil.copy(os.path.join(src, "french", f), os.path.join(root, f))
open(os.path.join(root, ".nojekyll"), "w").close()
print("index.html", round(os.path.getsize(os.path.join(root, "index.html")) / 1e6, 1), "MB ·", len(os.listdir(img)), "images")
