請依據accordion.png的圖片，生成html, css, javascript的技術需求規格
注意事項如下:
- 1. 這是一個accordion的功能
- 2. 要同時有顯示title和日期
- 3. 預設顯示第一筆的內容
- 4. 這個網頁未來會手動套用自jinjia格式的頁面
- 5. title 的內容有時會很多，可能會是多行
- 6. content的內容我們會限制固定顯示的行數(有固定高)
- 7. 所有資料都是從資料庫取得
- 8. 未來會手動加入至容器內，必須產生一個基本頁面，為了測試
- 9. 請加入到accordion技術需求.md
-10. 請符合RWD 手機版本、桌機版本、平板電腦版本

# Accordion 技術需求規格

## 1. 總覽 (Overview)
本文件定義了「最新訊息」Accordion 元件的 HTML、CSS 和 JavaScript 技術需求。此元件將用於顯示標題、日期和可展開/摺疊的內容區塊。

## 2. 功能需求 (Functional Requirements)
- **FR1: Accordion 機制:** 使用者點擊標題區域時，對應的內容區域應展開或摺疊。
- **FR2: 標題與日期顯示:** 每個 Accordion項目都必須同時顯示標題和日期。
- **FR3: 預設展開:** 預設情況下，第一個 Accordion 項目的內容應為展開狀態。
- **FR4: 多行標題:** 標題內容可能較長，需要支援多行顯示且不破壞排版。
- **FR5: 固定行數內容:** 內容區域應限制顯示固定的行數（即固定高度），超出部分將被隱藏或可滾動。
- **FR6: 響應式設計 (RWD):** 元件需適應手機、平板和桌面裝置的螢幕尺寸。

## 3. 資料需求 (Data Requirements)
- **DR1: 資料來源:** 所有 Accordion 項目的資料（標題、日期、內容）將從資料庫獲取。
- **DR2: Jinja 整合:** HTML 結構需設計為易於透過 Jinja 模板引擎進行資料綁定。

## 4. HTML 結構 (HTML Structure)
```html
<!-- 範例 HTML 結構 -->
<div class="accordion-container">
  <!-- Jinja 迴圈開始: {% for item in news_items %} -->
  <div class="accordion-item">
    <button class="accordion-header" aria-expanded="false" aria-controls="accordion-content-{{ loop.index }}" id="accordion-header-{{ loop.index }}">
      <span class="accordion-title">{{ item.title }}</span>
      <span class="accordion-date">{{ item.date }}</span>
      <span class="accordion-icon" aria-hidden="true"></span>
    </button>
    <div class="accordion-content" id="accordion-content-{{ loop.index }}" role="region" aria-labelledby="accordion-header-{{ loop.index }}">
      <p>{{ item.content }}</p>
    </div>
  </div>
  <!-- Jinja 迴圈結束: {% endfor %} -->

  <!-- 測試用靜態範例 (第一個項目預設展開) -->
  <div class="accordion-item is-open">
    <button class="accordion-header" aria-expanded="true" aria-controls="accordion-content-static-1" id="accordion-header-static-1">
      <span class="accordion-title">這是第一個標題，這個標題可能會非常長，需要換行顯示也不會影響到旁邊的日期或其他元素的排版。</span>
      <span class="accordion-date">2024-07-30</span>
      <span class="accordion-icon" aria-hidden="true"></span>
    </button>
    <div class="accordion-content" id="accordion-content-static-1" role="region" aria-labelledby="accordion-header-static-1">
      <p>這是第一筆內容。這段內容將會被限制顯示固定的行數，例如三行。如果內容超過三行，多餘的部分將會被隱藏起來，以保持整體排版的一致性與美觀。這是為了確保即使內容長度不一，每個項目在摺疊時的高度也能夠得到控制。</p>
    </div>
  </div>
  <div class="accordion-item">
    <button class="accordion-header" aria-expanded="false" aria-controls="accordion-content-static-2" id="accordion-header-static-2">
      <span class="accordion-title">這是第二個標題</span>
      <span class="accordion-date">2024-07-29</span>
      <span class="accordion-icon" aria-hidden="true"></span>
    </button>
    <div class="accordion-content" id="accordion-content-static-2" role="region" aria-labelledby="accordion-header-static-2">
      <p>這是第二筆內容。</p>
    </div>
  </div>
</div>
```
**HTML 說明:**
- `.accordion-container`: Accordion 的主容器。
- `.accordion-item`: 單個 Accordion 項目。
  - `is-open` class: 用於標識預設展開的項目。
- `.accordion-header`: 可點擊的標題區域，使用 `<button>` 以符合無障礙性。
  - `id`: 唯一標識符，用於 `aria-labelledby`。
  - `aria-expanded`: 指示內容是否展開。
  - `aria-controls`: 關聯標題與內容面板。
  - `.accordion-title`: 顯示標題文字。
  - `.accordion-date`: 顯示日期文字。
  - `.accordion-icon`: 用於顯示展開/摺疊的圖示 (例如 +/- 或箭頭)。
- `.accordion-content`: 包含詳細內容的區域。
  - `id`: 唯一標識符，被 `aria-controls` 引用。
  - `role="region"` 和 `aria-labelledby`: 增強無障礙性。
- **Jinja 整合:**
  - 註解中標示了 Jinja 迴圈 (`{% for item in news_items %}`) 和變數 (`{{ item.title }}`, `{{ item.date }}`, `{{ item.content }}`, `{{ loop.index }}`) 的使用方式。
  - `loop.index` 用於生成唯一的 `id` 和 `aria-controls` 值。

## 5. CSS 樣式 (CSS Styling)
```css
/* 基本樣式 */
.accordion-container {
  width: 100%;
  max-width: 800px; /* 可依設計調整 */
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

.accordion-item {
  border: 1px solid #ddd;
  margin-bottom: -1px; /* 避免雙邊框 */
}

.accordion-item:first-child {
  border-top-left-radius: 4px;
  border-top-right-radius: 4px;
}

.accordion-item:last-child {
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  margin-bottom: 0;
}

.accordion-header {
  background-color: #f7f7f7;
  color: #333;
  cursor: pointer;
  padding: 15px 20px;
  width: 100%;
  text-align: left;
  border: none;
  outline: none;
  transition: background-color 0.3s ease;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1em;
  position: relative; /* For icon positioning in RWD */
}

.accordion-header:hover,
.accordion-item.is-open .accordion-header {
  background-color: #e9e9e9;
}

.accordion-title {
  flex-grow: 1;
  margin-right: 15px; /* 標題和日期之間的間距 */
  /* 支援多行標題 */
  word-wrap: break-word;
  overflow-wrap: break-word;
  white-space: normal; /* 確保可以換行 */
}

.accordion-date {
  font-size: 0.9em;
  color: #666;
  white-space: nowrap; /* 日期不換行 */
  margin-left: auto; 
  padding-left: 10px; 
}

.accordion-icon {
  width: 20px; 
  height: 20px; 
  margin-left: 15px; 
  transition: transform 0.3s ease;
  background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>'); /* Plus icon */
  background-repeat: no-repeat;
  background-position: center;
  background-size: contain;
  flex-shrink: 0; /* 防止圖標被壓縮 */
}

.accordion-item.is-open .accordion-header .accordion-icon {
  background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 13H5v-2h14v2z"/></svg>'); /* Minus icon */
  /* transform: rotate(45deg); 如果使用相同的加號圖標並旋轉成叉號 */
}

.accordion-content {
  padding: 0 20px;
  background-color: white;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out, padding 0.3s ease-out;
}

.accordion-content p {
  margin: 0; /* 重置 p 標籤的預設 margin */
  padding: 15px 0; /* 將上下間距改用 padding 控制 */
  line-height: 1.6;
  color: #555;
}

.accordion-item.is-open .accordion-content {
  /* 內容固定行數 (範例：約3行) */
  /* 計算方式: (line-height * font-size * 行數) + (p 的 padding-top + padding-bottom) */
  /* 假設 p 的 line-height: 1.6, font-size: 1em (約16px) -> 1.6 * 16px = 25.6px per line */
  /* 3 行內容高度約 3 * 25.6px = 76.8px */
  /* 加上 p 的 padding (15px * 2 = 30px) -> 76.8px + 30px = 106.8px */
  /* 實際 max-height 需依據最終字體大小、行高和內容 padding/margin 調整 */
  max-height: 150px; /* 範例高度，請根據實際內容調整 */
  padding-top: 1px; /* 修正展開時的輕微跳動，確保有 padding */
  padding-bottom: 1px;
  padding-left: 20px;
  padding-right: 20px;
  overflow-y: auto; /* 如果內容真的超出固定高度，允許滾動 */
  /* 若要嚴格限制行數並截斷文字 (純CSS，需瀏覽器支援):
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  max-height: none;  -- 這種情況下 max-height 會被 -webkit-line-clamp 控制
  p { padding: 15px 0; } -- 內部 p 仍需 padding
  */
}

/* RWD 樣式 */
/* 手機 (Mobile) - 小於 600px */
@media (max-width: 599px) {
  .accordion-header {
    padding: 12px 15px;
    padding-right: 45px; /* 留出空間給絕對定位的圖標 */
    flex-wrap: wrap; /* 允許標題和日期換行 */
  }

  .accordion-title {
    width: 100%; /* 標題佔滿寬度 */
    margin-right: 0;
    margin-bottom: 8px; 
    font-size: 0.95em;
  }

  .accordion-date {
    font-size: 0.8em;
    padding-left: 0;
    margin-left: 0; 
    width: 100%; /* 日期也佔滿寬度，在標題下方 */
  }

  .accordion-icon {
    position: absolute;
    top: 50%;
    right: 15px;
    transform: translateY(-50%);
    margin-left: 0; 
  }
  .accordion-item.is-open .accordion-header .accordion-icon {
     /* transform: translateY(-50%) rotate(45deg);  如果使用旋轉 */
  }

  .accordion-content {
    padding-left: 15px;
    padding-right: 15px;
  }
  .accordion-item.is-open .accordion-content {
    max-height: 120px; /* 手機版可能需要調整高度 */
  }
  .accordion-content p {
    font-size: 0.9em;
    padding: 12px 0;
  }
}

/* 平板 (Tablet) - 600px 到 899px */
@media (min-width: 600px) and (max-width: 899px) {
  .accordion-header {
    padding: 15px 18px;
  }
  .accordion-title {
    font-size: 1em;
  }
  .accordion-date {
    font-size: 0.85em;
  }
   .accordion-item.is-open .accordion-content {
    max-height: 140px; /* 平板版可能需要調整高度 */
  }
}

/* 桌機 (Desktop) - 大於 900px (基本樣式已涵蓋) */

```
**CSS 說明:**
- **基本佈局:** 使用 Flexbox 排列標題、日期和圖示。
- **多行標題:** `.accordion-title` 使用 `word-wrap: break-word;` 和 `white-space: normal;`。
- **固定行數內容:** `.accordion-item.is-open .accordion-content` 透過 `max-height` 和 `overflow-y: auto` 來限制內容高度並允許滾動。
- **圖示:** 使用 Base64 編碼的 SVG 作為背景圖示。建議可替換為外部 SVG 檔案或圖示字型。
- **RWD:**
  - **手機:** 標題和日期垂直堆疊，圖示移至右側垂直居中。
  - **平板/桌面:** 標題、日期、圖示水平排列。

## 6. JavaScript 行為 (JavaScript Behavior)
```javascript
document.addEventListener('DOMContentLoaded', function () {
  const accordionItems = document.querySelectorAll('.accordion-item');

  accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    const content = item.querySelector('.accordion-content'); // Not strictly needed if only toggling class

    if (!header) {
      console.warn('Accordion item missing header:', item);
      return;
    }

    header.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');

      // Optional: Close other open items if you want only one open at a time
      // if (!isOpen) { // Only run if we are trying to open this one
      //   accordionItems.forEach(otherItem => {
      //     if (otherItem !== item && otherItem.classList.contains('is-open')) {
      //       otherItem.classList.remove('is-open');
      //       otherItem.querySelector('.accordion-header').setAttribute('aria-expanded', 'false');
      //     }
      //   });
      // }

      item.classList.toggle('is-open');
      header.setAttribute('aria-expanded', String(!isOpen));
    });

    // Ensure ARIA attribute matches class on load (if set by HTML)
    if (item.classList.contains('is-open')) {
      header.setAttribute('aria-expanded', 'true');
    } else {
      header.setAttribute('aria-expanded', 'false');
    }
  });

  // FR3: Default open first item - This is best handled by adding 'is-open' class
  // and aria-expanded="true" directly in the HTML for the first item.
  // The JS above will respect that. If not set in HTML, you could do:
  // const firstItem = document.querySelector('.accordion-container .accordion-item:first-child');
  // if (firstItem && !firstItem.classList.contains('is-open')) {
  //   firstItem.classList.add('is-open');
  //   const firstHeader = firstItem.querySelector('.accordion-header');
  //   if (firstHeader) {
  //     firstHeader.setAttribute('aria-expanded', 'true');
  //   }
  // }
});
```
**JavaScript 說明:**
- **事件監聽:** 為每個 `.accordion-header` 添加點擊事件。
- **切換狀態:** 點擊時，切換父層 `.accordion-item` 的 `is-open` class，並更新 `aria-expanded` 屬性。
- **動畫:** CSS 的 `transition` 負責動畫效果。
- **預設展開 (FR3):** 最佳實踐是在 HTML 中為第一個項目添加 `is-open` class 和 `aria-expanded="true"`。

## 7. 測試頁面 (Test Page)
一個基本的 HTML 頁面 (`test_accordion.html`) 將被創建，包含上述 HTML 結構（使用靜態範例資料）、引入的 CSS 和 JavaScript。
```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accordion Test Page</title>
    <!-- <link rel="stylesheet" href="accordion.css"> -->
    <style>
        h1 {
            max-width: 800px; /* 與 .accordion-container 的 max-width 相同 */
            margin-left: auto;   /* 使 h1 區塊置中 */
            margin-right: auto;  /* 使 h1 區塊置中 */
            margin-top: 20px;    /* 可選：調整上方間距 */
            margin-bottom: 20px; /* 可選：調整下方間距 */
        }
        /* 複製上面 CSS 區塊的內容到這裡或 accordion.css */
        /* 基本樣式 */
        .accordion-container { width: 100%; max-width: 800px; margin: 20px auto; font-family: Arial, sans-serif; }
        .accordion-item { border: 1px solid #ddd; margin-bottom: -1px; }
        .accordion-item:first-child { border-top-left-radius: 4px; border-top-right-radius: 4px; }
        .accordion-item:last-child { border-bottom-left-radius: 4px; border-bottom-right-radius: 4px; margin-bottom: 0; }
        .accordion-header { background-color: #f7f7f7; color: #333; cursor: pointer; padding: 15px 20px; width: 100%; text-align: left; border: none; outline: none; transition: background-color 0.3s ease; display: flex; justify-content: space-between; align-items: center; font-size: 1em; position: relative; }
        .accordion-header:hover, .accordion-item.is-open .accordion-header { background-color: #e9e9e9; }
        .accordion-title { flex-grow: 1; margin-right: 15px; word-wrap: break-word; overflow-wrap: break-word; white-space: normal; }
        .accordion-date { font-size: 0.9em; color: #666; white-space: nowrap; margin-left: auto; padding-left: 10px; }
        .accordion-icon { width: 20px; height: 20px; margin-left: 15px; transition: transform 0.3s ease; background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/></svg>'); background-repeat: no-repeat; background-position: center; background-size: contain; flex-shrink: 0; }
        .accordion-item.is-open .accordion-header .accordion-icon { background-image: url('data:image/svg+xml;charset=UTF-8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M19 13H5v-2h14v2z"/></svg>'); }
        .accordion-content { padding: 0 20px; background-color: white; max-height: 0; overflow: hidden; transition: max-height 0.3s ease-out, padding 0.3s ease-out; }
        .accordion-content p { margin: 0; padding: 15px 0; line-height: 1.6; color: #555; }
        .accordion-item.is-open .accordion-content { max-height: 150px; padding-top:1px; padding-bottom:1px; padding-left:20px; padding-right:20px; overflow-y: auto; }
        @media (max-width: 599px) {
            .accordion-header { padding: 12px 15px; padding-right: 45px; flex-wrap: wrap; }
            .accordion-title { width: 100%; margin-right: 0; margin-bottom: 8px; font-size: 0.95em; }
            .accordion-date { font-size: 0.8em; padding-left: 0; margin-left: 0; width: 100%; }
            .accordion-icon { position: absolute; top: 50%; right: 15px; transform: translateY(-50%); margin-left: 0; }
            .accordion-content { padding-left: 15px; padding-right: 15px; }
            .accordion-item.is-open .accordion-content { max-height: 120px; }
            .accordion-content p { font-size: 0.9em; padding: 12px 0; }
        }
        @media (min-width: 600px) and (max-width: 899px) {
            .accordion-header { padding: 15px 18px; }
            .accordion-title { font-size: 1em; }
            .accordion-date { font-size: 0.85em; }
            .accordion-item.is-open .accordion-content { max-height: 140px; }
        }
    </style>
</head>
<body>
    <h1>最新訊息 Accordion 測試</h1>
    <div class="accordion-container">
      <div class="accordion-item is-open">
        <button class="accordion-header" aria-expanded="true" aria-controls="accordion-content-static-1" id="accordion-header-static-1">
          <span class="accordion-title">這是第一個測試標題，這個標題設計得非常長，目的是為了測試在不同螢幕寬度下，多行文字是否能夠正確換行顯示，並且不會影響到右側日期或其他元素的整體排版佈局。</span>
          <span class="accordion-date">2024-08-01</span>
          <span class="accordion-icon" aria-hidden="true"></span>
        </button>
        <div class="accordion-content" id="accordion-content-static-1" role="region" aria-labelledby="accordion-header-static-1">
          <p>這是第一筆測試內容。這段內容將會被限制顯示固定的行數，例如三行。如果內容超過三行，多餘的部分將會被隱藏起來，以保持整體排版的一致性與美觀。這是為了確保即使內容長度不一，每個項目在摺疊時的高度也能夠得到控制。這是一段額外添加的文字，以確保內容肯定會超出預設的幾行限制，從而可以測試截斷或滾動條的效果。</p>
        </div>
      </div>
      <div class="accordion-item">
        <button class="accordion-header" aria-expanded="false" aria-controls="accordion-content-static-2" id="accordion-header-static-2">
          <span class="accordion-title">這是第二個測試標題</span>
          <span class="accordion-date">2024-07-31</span>
          <span class="accordion-icon" aria-hidden="true"></span>
        </button>
        <div class="accordion-content" id="accordion-content-static-2" role="region" aria-labelledby="accordion-header-static-2">
          <p>這是第二筆測試內容。它比較簡短。</p>
        </div>
      </div>
    </div>
    <script>
        // 複製上面 JavaScript 區塊的內容到這裡或 accordion.js
        document.addEventListener('DOMContentLoaded', function () {
          const accordionItems = document.querySelectorAll('.accordion-item');
          accordionItems.forEach(item => {
            const header = item.querySelector('.accordion-header');
            if (!header) { return; }
            header.addEventListener('click', () => {
              const isOpen = item.classList.contains('is-open');
              item.classList.toggle('is-open');
              header.setAttribute('aria-expanded', String(!isOpen));
            });
            if (item.classList.contains('is-open')) {
              header.setAttribute('aria-expanded', 'true');
            } else {
              header.setAttribute('aria-expanded', 'false');
            }
          });
        });
    </script>
</body>
</html>
```
**測試頁面說明:**
- 包含基本的 HTML 結構和內嵌的 CSS 與 JavaScript，方便快速測試。
- 使用靜態資料模擬 Accordion 項目。

## 8. 注意事項與未來擴展
- **圖示替換:** CSS 中的圖示是 Base64 SVG。可替換為更精緻的圖示 (如 Font Awesome, Material Icons, 或自訂 SVG 檔案)。
- **無障礙性 (A11y):** 已包含 ARIA 屬性。可進一步增強鍵盤導航 (如 Enter/Space 開關)。
- **Jinja 模板:** 整合時，確保 Jinja 變數與後端資料結構一致。
- **內容截斷 UX:** 對於固定高度的內容，`overflow-y: auto` 提供了滾動條。若不希望滾動，可改為 `overflow: hidden` 並考慮加入「閱讀更多」鏈接的方案。