// App icons and favicons: a small book whose lower half echoes the cover pattern.
// Usage: node icons.mjs (writes ../assets/icons)
import puppeteer from 'puppeteer-core';
const INK = '#111318', RED = '#D9482B', PAPER = '#F6F4EF', GHOST = '#9E998D', CYAN = '#00A3CF';
// A 64-unit book: frame, title plate, traces.
function book() {
  const br = (d, c, w) => `<path d="${d}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round"/>`;
  return `<rect x="9" y="2" width="46" height="60" rx="4" fill="${PAPER}" stroke="${INK}" stroke-width="3"/>` +
    `<rect x="13" y="7" width="38" height="16" rx="1.5" fill="#fff" stroke="${INK}" stroke-width="1.6"/>` +
    `<rect x="16" y="10" width="26" height="3.2" fill="${INK}"/><rect x="16" y="14.6" width="18" height="2.2" fill="${INK}"/><rect x="16" y="18.6" width="32" height="1.6" fill="${RED}"/>` +
    `<clipPath id="pg"><rect x="11" y="25" width="42" height="35" rx="2"/></clipPath><g clip-path="url(#pg)">` +
    br('M18 26 L18 40 L14 48 M18 40 L22 50 M26 26 L27 36 L24 44 M27 36 L31 46 M38 26 L37 34 L41 42 L40 52 M37 34 L33 40 M46 26 L46 38 L50 46 M46 38 L42 48', GHOST, 1.4) +
    br('M31 25 L30 33 L34 41 L32 50 M34 41 L38 46', RED, 2.6) + br('M32 50 L30 57', CYAN, 2.4) +
    `</g>`;
}
const svg = (size, scale, bg) => `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 64 64">${bg ? `<rect width="64" height="64" fill="${bg}"/>` : ''}<g transform="translate(32 32) scale(${scale}) translate(-32 -32)">${book()}</g></svg>`;
const OUT = [
  ['../assets/icons/favicon-64.png', 64, 1, null], ['../assets/icons/favicon-32.png', 32, 1, null],
  ['../assets/icons/apple-touch-icon.png', 180, 0.86, '#f3f1ec'], ['../assets/icons/icon-192.png', 192, 1, null],
  ['../assets/icons/icon-512.png', 512, 1, null], ['../assets/icons/icon-512-maskable.png', 512, 0.68, '#f3f1ec'],
];
const b = await puppeteer.launch({ executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', headless: true });
const p = await b.newPage();
for (const [file, size, scale, bg] of OUT) {
  await p.setViewport({ width: size, height: size });
  await p.setContent(`<html><body style="margin:0;background:transparent">${svg(size, scale, bg)}</body></html>`);
  await p.screenshot({ path: file, omitBackground: true, clip: { x: 0, y: 0, width: size, height: size } });
  console.log('wrote', file);
}
await b.close();
