# 咖啡馆原创美术（issue #16）

- `counter.webp`：1280×853，原创暖色咖啡馆背景。窗外塞纳河、石桥与街屋；室内吊灯、木质吧台、挂杯、唱片机及空白菜单板。用图像生成工具按 `french-quiz/tools/idle/counter-prompt.txt` 创作，无人物、文字或真实品牌；图中留空的吧台供状态器具叠加。
- `icons.svg`：由 `node french-quiz/tools/idle/art.cjs` 重建的矢量 sprite，共86个 symbol（68件知识器具、6个工作台、12杯饮品）。形状和配色由仓库内脚本原创绘制，无外部字体或图标库。
- `src/js/cafe/art.js`：同一脚本生成的标签 / 饮品与 sprite ID 对照。

运行时仅加载这两份图片。`browser-results.json` 记录实际字节数，并验证 WebP <150,000字节、全部运行图片 <500,000字节；QA截图放在 `tools/idle/screenshots/`，不是运行资产。

原始生成 PNG 保留在本次会话的 `/workspace/generated_images/exec-f80a228c-a1bd-46be-bfbe-4628eb2041ea.png`，未作为网页资产提交。压缩命令（在仓库根目录）：

```sh
magick /workspace/generated_images/exec-f80a228c-a1bd-46be-bfbe-4628eb2041ea.png -resize 1280x -strip -quality 76 skins/cafe/counter.webp
node french-quiz/tools/idle/art.cjs
node french-quiz/tools/idle/browser.cjs
```

背景为日间底图，前景器具、饮品、夜间遮罩和营业动画由SVG / CSS分层绘制。知识点亮状态只读取当前派生状态；未解锁器具变灰，结垢器具卡片叠加水垢，打烊时灯光变暗且停止杯子、热气动画；冷饮没有热气。减少动态效果设置下全部停用循环动画。

本次不改变经济、数值或记录格式，不构建发布HTML。
