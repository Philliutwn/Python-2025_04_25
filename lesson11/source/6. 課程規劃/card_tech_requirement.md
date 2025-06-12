# 課程卡片組件 - 技術需求文件

## 專案概述
基於 Figma 設計實作課程卡片組件，用於職能發展學院網站的課程資訊展示。此組件將作為網頁內的局部元素，支援響應式設計，並採用網格佈局展示多個課程卡片。

## 設計規格

### 整體佈局
- **容器類型**: 響應式網格佈局
- **背景色**: #FFFFFF (白色)
- **容器寬度**: 1233px (桌面版基準)
- **內距**: 64px (桌面版)
- **卡片間距**: 64px (水平) × 48px (垂直)

### 單張卡片規格
#### 卡片容器
- **佈局方式**: 水平排列 (圖標 + 內容)
- **卡片寬度**: 301.33px (桌面版基準，自適應)
- **背景色**: #FFFFFF (白色)
- **內部間距**: 24px (圖標與內容間距)

#### 圖標區域
- **容器尺寸**: 32px × 32px
- **圖標尺寸**: 26.67px × 26.67px
- **圖標位置**: 居中對齊
- **邊框樣式**: 3px 實線
- **邊框顏色**: #1E1E1E (深灰色)
- **圖標格式**: SVG

#### 內容區域
##### 標題樣式
- **字體**: Inter
- **字重**: 600 (Semi-bold)
- **字號**: 24px
- **行高**: 1.2倍
- **字距**: -2%
- **顏色**: #1E1E1E (深灰色)
- **對齊**: 左對齊

##### 內文樣式
- **字體**: Inter
- **字重**: 400 (Regular)
- **字號**: 16px
- **行高**: 1.4倍
- **顏色**: #757575 (中灰色)
- **對齊**: 左對齊
- **內容**: "Body text for whatever you'd like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story."

##### 內容區域間距
- **標題與內文間距**: 8px
- **整體內容區間距**: 16px

## 響應式設計需求 (RWD)

### 桌面版 (≥768px)
- 容器寬度: 1233px
- 內距: 64px
- 網格排列: 3-4 欄
- 卡片間距: 64px × 48px
- 字體大小: 標題 24px，內文 16px
- 圖標尺寸: 32px × 32px 容器，26.67px × 26.67px 圖標

### 手機版 (≤767px)
- 容器寬度: 100%
- 內距: 16px
- 網格排列: 1 欄
- 卡片間距: 24px × 16px
- 字體大小: 標題 18px，內文 14px
- 圖標尺寸調整: 28px × 28px 容器，24px × 24px 圖標

## 技術實作要求

### HTML 結構建議
```html
<div class="course-cards-container">
  <div class="cards-grid">
    <div class="course-card">
      <div class="card-icon">
        <svg class="icon-svg">
          <!-- SVG 圖標內容 -->
        </svg>
      </div>
      <div class="card-content">
        <h3 class="card-title">Title</h3>
        <p class="card-description">Body text for whatever you'd like to say. Add main takeaway points, quotes, anecdotes, or even a very very short story.</p>
      </div>
    </div>
    <!-- 重複卡片結構 -->
  </div>
</div>
```

### CSS 關鍵樣式 (不使用變數)
```css
/* 基礎容器樣式 */
.course-cards-container {
  background-color: #ffffff;
  padding: 64px;
  width: 1233px;
  margin: 0 auto;
}

.cards-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 48px 64px;
  justify-content: flex-start;
  align-items: flex-start;
}

/* 卡片樣式 */
.course-card {
  display: flex;
  gap: 24px;
  width: 301.33px;
  background-color: #ffffff;
}

.card-icon {
  width: 32px;
  height: 32px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.icon-svg {
  width: 26.67px;
  height: 26.67px;
  stroke: #1e1e1e;
  stroke-width: 3px;
}

.card-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.card-title {
  font-family: Inter, sans-serif;
  font-weight: 600;
  font-size: 24px;
  line-height: 1.2;
  letter-spacing: -0.02em;
  color: #1e1e1e;
  margin: 0;
}

.card-description {
  font-family: Inter, sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 1.4;
  color: #757575;
  margin: 0;
}
```

### 響應式媒體查詢
```css
/* 手機版 */
@media (max-width: 767px) {
  .course-cards-container {
    width: 100%;
    padding: 16px;
  }
  .cards-grid {
    gap: 16px 24px;
  }
  .course-card {
    width: 100%;
    gap: 16px;
  }
  .card-icon {
    width: 28px;
    height: 28px;
  }
  .icon-svg {
    width: 24px;
    height: 24px;
  }
  .card-title {
    font-size: 18px;
  }
  .card-description {
    font-size: 14px;
  }
}
```

## 互動功能需求
- **懸停效果**: 卡片懸停時提供視覺反饋
- **點擊功能**: 支援整張卡片點擊跳轉
- **鍵盤導航**: 支援 Tab 鍵導航
- **觸控支援**: 移動設備觸控友好

## 內容管理需求
- **動態內容**: 支援從後端 API 載入卡片資料
- **圖標管理**: 支援 SVG 圖標的動態載入
- **內容長度**: 標題建議 1-3 個詞，描述文字建議 50-100 字
- **圖標庫**: 建議使用統一的圖標設計系統

## 無障礙設計
- **語義化標籤**: 使用適當的 HTML 標籤
- **Alt 文字**: 為圖標提供適當的 alt 屬性
- **色彩對比**: 確保文字與背景的對比度符合 WCAG 標準
- **鍵盤操作**: 所有互動元素支援鍵盤操作
- **螢幕閱讀器**: 提供適當的 ARIA 標籤

## 效能要求
- **載入時間**: 整個組件載入時間 < 200ms
- **圖片最佳化**: SVG 圖標檔案大小控制在 2KB 以內
- **CSS 最佳化**: 樣式檔案壓縮後 < 10KB
- **渲染效能**: 支援大量卡片 (100+) 的流暢渲染

## 瀏覽器支援
- Chrome 70+
- Firefox 70+
- Safari 12+
- Edge 79+
- iOS Safari 12+
- Android Chrome 70+

## 開發注意事項
1. **不使用 CSS 變數**: 所有樣式值直接寫入，便於維護和除錯
2. **模組化設計**: 組件具備良好的獨立性和可重用性
3. **樣式隔離**: 避免樣式污染其他頁面元素
4. **圖標系統**: 建立統一的 SVG 圖標管理機制
5. **內容溢出**: 處理長文字的溢出和截斷
6. **載入狀態**: 提供載入中的骨架屏效果

## 測試需求
- [ ] 桌面版瀏覽器測試 (Chrome, Firefox, Safari, Edge)
- [ ] 移動設備測試 (iOS, Android)
- [ ] 響應式設計測試 (不同螢幕尺寸)
- [ ] 無障礙功能測試 (鍵盤導航、螢幕閱讀器)
- [ ] 效能測試 (載入時間、渲染效能)
- [ ] 跨瀏覽器兼容性測試

## 交付物
1. HTML 模板檔案
2. CSS 樣式檔案 (不含變數)
3. JavaScript 互動邏輯 (如需要)
4. SVG 圖標資源檔案
5. 響應式測試報告
6. 無障礙測試報告
7. 使用說明文件
8. 維護指南