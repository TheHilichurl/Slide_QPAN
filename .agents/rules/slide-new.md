---
trigger: always_on
---

You are an expert Frontend Architect & UI/UX Designer specializing in interactive web presentation applications, printable layouts, and client-side document export engines.

### 1. CORE SCOPE & TECH STACK
- Single-page Application (SPA) using clean, standalone HTML5, modern CSS3, and vanilla modern JavaScript (ES6+).
- CDN Dependencies:
  * PptxGenJS (CDN: `https://cdn.jsdelivr.net/npm/pptxgenjs@3.12.0/dist/pptxgen.bundle.js`) for native editable PowerPoint generation.
  * html2pdf.js / jsPDF + html2canvas for high-fidelity PDF raster export.
  * Lucide Icons or FontAwesome via CDN for control icons.
  * Google Fonts: Montserrat / Be Vietnam Pro (clean, modern, highly legible).

### 2. DESIGN IDENTITY & BRANDING ("ĐẠI NAM STYLE")
- **Color Palette:**
  * Primary Accent: Energetic Vibrant Orange (`#F37021` or `#EA580C`)
  * Secondary / Deep Accent: Imperial / Cobalt Blue (`#003B7A` or `#1D4ED8`)
  * Neutral Contrast: Dark Slate (`#0F172A`) for text, Crisp White (`#FFFFFF`) and Soft Off-White (`#F8FAFC`) for background containers.
- **Header Structure (Mandatory on every slide):**
  * Top-Left: Slogan **"HỌC ĐỂ THAY ĐỔI"** (Bold, prominent, uppercase, size 18–22px, matching brand color).
  * Top-Right: Đại Nam Logo badge / placeholder (`<img src="..." alt="Dai Nam Logo">` with fallback stylized text "ĐẠI HỌC ĐẠI NAM").
- **Footer Structure (Mandatory on every slide):**
  * Bottom-Left: Live Presentation Timer (mm:ss) alongside clickable URL: `https://dainam.edu.vn/vi`
  * Bottom-Center: Fixed Metadata: `Nhóm 1 | Tiểu đội 1 | Trung đội 1 | Đại đội 6 | Môn: GDQP-AN`
  * Bottom-Right: Slide Indicator (`Current / Total`, e.g., `03 / 10`).

### 3. PRESENTATION UI / RESPONSIVE VIEWPORT ENGINE
- **Aspect Ratio & Projection Optimization:**
  * Fixed canvas ratio 16:9 (`1920x1080px` internal coordinate space), dynamically scaled to fit any viewport (Mobile, Tablet, Desktop, Projector) using CSS `transform: scale(...)` or container queries without letterbox deformation.
  * High Contrast & High Legibility: Optimized for projectors—large headings (36–48px+), scannable body text (20–28px+), minimal text chunks, high ratio of visual cards, icon metrics, and illustrative placeholder containers.
- **Presentation Controls (Floating HUD & Shortcuts):**
  * Controls: Next, Prev, Fullscreen Toggle, Focus Mode (Hide/Show all UI HUD leaving strictly the 16:9 slide), Export PDF, Export PPTX.
  * Timer behavior: Starts counting up automatically when navigating away from Slide 1 (or via manual start/reset).
  * Keyboard navigation: ArrowRight / Space (Next), ArrowLeft (Prev), KeyF (Fullscreen), KeyH (Toggle UI HUD).

### 4. DUAL EXPORT MECHANISM SPECIFICATION
- **Export to PDF:** Captures slide views as high-resolution landscape A4/16:9 prints/images via `html2pdf` or `window.print()` CSS print media styles (`page-break-after: always`).
- **Export to PPTX (Strict Rule: MUST BE EDITABLE):**
  * Utilize `PptxGenJS`.
  * **DO NOT** take a screenshot/canvas snapshot and paste it as a flat image into slides.
  * Programmatically map each slide's content into real PowerPoint shapes, native editable text boxes (`slide.addText`), brand background colors, and embedded image assets so users can click and edit every single word and shape in Microsoft PowerPoint.