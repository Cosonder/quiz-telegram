# 法语语法小测验 · Telegram 小程序（Mini App）

把网站版（[cosonder.github.io/quiz](https://cosonder.github.io/quiz/)）的法语页包成 Telegram Mini App：在 Telegram 里点机器人的按钮打开。

## 和网站版的区别（`src/`）

- `tg-adapter.js`：在 Telegram 里打开时
  - 通知 Telegram 页面就绪、展开到全高、关掉下滑关闭（免得上下滑动时误关）；
  - 主题跟随 Telegram 的深色 / 浅色，顶栏颜色和页面背景一致；
  - 用 Telegram 自带的返回按钮：做题全屏时退出全屏，在板块里回到板块选择页，在首页时隐藏；
  - 答对 / 答错时轻微震动。
- `tg.css`：隐藏页面自己的大标题和返回图标（Telegram 有自己的标题栏和返回按钮）。
- 不注册离线缓存，每次打开都是最新版。

在普通浏览器里打开时，适配代码什么都不做，页面和网站版一样。

## 更新

网站版发布新版本后：

```bash
python3 tools/build.py <quiz 仓库路径>   # 重新生成根目录的 index.html 和 img/
git add -A && git commit -m "Update from website" && git push
```

## 发布

1. 仓库 Settings → Pages：Deploy from a branch，分支 `main`、目录 `/ (root)`。网址是 `https://cosonder.github.io/quiz-telegram/`。
2. 在 Telegram 里找 **@BotFather**：
   - `/newbot` 建一个机器人；
   - `/mybots` → 选这个机器人 → Bot Settings → Menu Button → 填上面的网址，按钮文字比如“开始练习”；
   - 也可以用 `/newapp` 建一个 Mini App，得到 `t.me/机器人名/应用名` 这样的直达链接。
3. 打开机器人，点菜单按钮就能用。

## 以后可以加

- 用 Telegram 身份免登录同步（需要一个服务端校验 `initData` 的签名，再对接 Supabase）。
- 用 Telegram Stars 卖会员 / 解锁内容。
