// ---------- Telegram Mini App 适配 ----------
// 在 Telegram 里打开时：通知 Telegram 页面已就绪、展开到全高、主题跟随 Telegram 的深色 / 浅色、
// 用 Telegram 自带的返回按钮返回上一级、答对答错时轻微震动。不在 Telegram 里打开时什么都不做。
(function () {
  const tg = window.Telegram && window.Telegram.WebApp;
  if (!tg || !tg.initData) return;   // 普通浏览器打开：initData 是空的
  document.documentElement.classList.add("in-telegram");
  tg.ready();
  tg.expand();
  if (tg.disableVerticalSwipes) tg.disableVerticalSwipes();   // 上下滑动时不要误关小程序

  // 主题：跟随 Telegram 的深色 / 浅色，顶栏和背景色也一起设好
  const applyTheme = () => {
    const dark = tg.colorScheme === "dark";
    document.documentElement.dataset.theme = dark ? "dark" : "light";
    const bg = getComputedStyle(document.body).backgroundColor;
    try { tg.setHeaderColor(bg); tg.setBackgroundColor(bg); } catch (e) {}
  };
  applyTheme();
  tg.onEvent("themeChanged", applyTheme);

  // 返回按钮：做题全屏时 → 退出全屏；在板块里 → 回到板块选择页；在首页时隐藏
  const back = tg.BackButton;
  const canBack = () => document.getElementById("qfBack") || (typeof view !== "undefined" && view !== "home");
  const syncBack = () => { if (canBack()) back.show(); else back.hide(); };
  back.onClick(() => {
    const qb = document.getElementById("qfBack");
    if (qb) { qb.click(); return; }
    if (typeof goHome === "function" && typeof curMod === "function") {
      const m = curMod();
      goHome(m === "game" ? "game" : "practice");
    }
  });
  new MutationObserver(syncBack).observe(document.body, { childList: true, subtree: true });
  syncBack();

  // 震动反馈：选项变成“对 / 错”时
  const hap = tg.HapticFeedback;
  if (hap) {
    new MutationObserver(ms => {
      for (const m of ms) {
        const el = m.target;
        if (m.attributeName !== "class" || !el.classList) continue;
        if (el.classList.contains("wrong") && !(m.oldValue || "").includes("wrong")) { hap.notificationOccurred("error"); return; }
        if (el.classList.contains("correct") && !(m.oldValue || "").includes("correct") && !document.querySelector(".opt.wrong, .v-pic.wrong")) { hap.notificationOccurred("success"); return; }
      }
    }).observe(document.body, { attributes: true, attributeFilter: ["class"], attributeOldValue: true, subtree: true });
  }
})();
