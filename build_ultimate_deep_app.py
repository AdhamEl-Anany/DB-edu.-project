import os
import base64

img_dir = r'c:\Users\Dell\OneDrive\Desktop\DB\extracted_images'
slide_dir = r'c:\Users\Dell\OneDrive\Desktop\DB\slide_pages'

def get_base64(filepath):
    if os.path.exists(filepath):
        ext = filepath.split('.')[-1].lower()
        mime = 'image/png' if ext == 'png' else 'image/jpeg'
        with open(filepath, 'rb') as f:
            data = base64.b64encode(f.read()).decode('utf-8')
            return f"data:{mime};base64,{data}"
    return ""

print("Encoding diagrams to Base64...")
b64_lec8_bank = get_base64(os.path.join(img_dir, 'DB_Lecture-8_p3_img1.jpeg'))
b64_lec9_company = get_base64(os.path.join(img_dir, 'DB_Lecture-9_p2_img1.jpeg'))
b64_lec9_airline = get_base64(os.path.join(img_dir, 'DB_Lecture-9_p3_img1.jpeg'))
b64_lec9_library = get_base64(os.path.join(img_dir, 'DB_Lecture-9_p4_img1.jpeg'))
b64_lec11_bank_q = get_base64(os.path.join(img_dir, 'DB_Lecture-11_p7_img1.jpeg'))
b64_lec11_bank_sol = get_base64(os.path.join(img_dir, 'DB_Lecture-11_p9_img1.jpeg'))

b64_lec11_ex2a = get_base64(os.path.join(slide_dir, 'DB_Lecture-11_page_3.png'))
b64_lec11_ex2b = get_base64(os.path.join(slide_dir, 'DB_Lecture-11_page_4.png'))
b64_lec11_ex2c = get_base64(os.path.join(slide_dir, 'DB_Lecture-11_page_5.png'))

b64_lec12_opt8a_q = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p14_img1.jpeg'))
b64_lec12_opt8a_sol = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p15_img1.jpeg'))
b64_lec12_ex2_q = get_base64(os.path.join(slide_dir, 'DB_Lecture-12_page_16.png'))
b64_lec12_ex2_sol = get_base64(os.path.join(slide_dir, 'DB_Lecture-12_page_17.png'))

b64_opt8a = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p4_img1.jpeg'))
b64_opt8b = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p7_img1.jpeg'))
b64_opt8c = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p9_img1.jpeg'))
b64_opt8d = get_base64(os.path.join(img_dir, 'DB_Lecture-12_p12_img1.jpeg'))

print("Base64 encoding complete!")

html_template = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Systems Masterclass & Diagram Interactive Platform | Eng. Adham Hany</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&family=Fira+Code:wght@400;600&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <!-- Font Awesome Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {{
            --bg-primary: #070913;
            --bg-secondary: #0f1424;
            --bg-card: rgba(17, 24, 42, 0.75);
            --bg-card-hover: rgba(26, 36, 62, 0.85);
            --bg-sidebar: rgba(15, 20, 36, 0.9);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --border-color: rgba(255, 255, 255, 0.1);
            --border-glow: rgba(225, 29, 72, 0.4);
            --accent-primary: #e11d48;
            --accent-hover: #fb7185;
            --accent-light: rgba(225, 29, 72, 0.18);
            --cyan: #06b6d4;
            --cyan-light: rgba(6, 182, 212, 0.18);
            --yellow: #f59e0b;
            --yellow-light: rgba(245, 158, 11, 0.18);
            --success: #10b981;
            --success-light: rgba(16, 185, 129, 0.18);
            --purple: #8b5cf6;
            --purple-light: rgba(139, 92, 246, 0.18);
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.4);
            --shadow-md: 0 10px 30px rgba(0, 0, 0, 0.5);
            --shadow-lg: 0 20px 40px rgba(0, 0, 0, 0.7);
            --shadow-glow: 0 0 35px rgba(225, 29, 72, 0.35);
            --shadow-cyan-glow: 0 0 35px rgba(6, 182, 212, 0.35);
            --radius-sm: 10px;
            --radius-md: 14px;
            --radius-lg: 20px;
            --radius-xl: 28px;
            --transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        [data-theme="light"] {{
            --bg-primary: #f0f4f8;
            --bg-secondary: #ffffff;
            --bg-card: rgba(255, 255, 255, 0.85);
            --bg-card-hover: rgba(255, 255, 255, 0.98);
            --bg-sidebar: #e2e8f0;
            --text-primary: #0f172a;
            --text-secondary: #475569;
            --text-muted: #64748b;
            --border-color: rgba(0, 0, 0, 0.08);
            --border-glow: rgba(225, 29, 72, 0.4);
            --accent-primary: #e11d48;
            --accent-hover: #be123c;
            --accent-light: #ffe4e6;
            --cyan: #0284c7;
            --cyan-light: #e0f2fe;
            --yellow: #d97706;
            --yellow-light: #fef3c7;
            --success: #059669;
            --success-light: #d1fae5;
            --purple: #7c3aed;
            --purple-light: #ede9fe;
            --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.05);
            --shadow-md: 0 10px 25px rgba(0, 0, 0, 0.08);
            --shadow-lg: 0 20px 35px rgba(0, 0, 0, 0.12);
            --shadow-glow: 0 0 25px rgba(225, 29, 72, 0.2);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; scroll-behavior: smooth; }}
        body {{
            font-family: 'Cairo', 'IBM Plex Sans Arabic', sans-serif;
            background-color: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.8;
            transition: background-color 0.4s ease, color 0.4s ease;
            overflow-x: hidden;
            position: relative;
        }}

        /* Dynamic Database Canvas Background */
        #dbParticleCanvas {{
            position: fixed;
            top: 0; left: 0;
            width: 100vw; height: 100vh;
            pointer-events: none;
            z-index: 0;
            opacity: 0.65;
        }}

        /* Ambient Glow Blobs */
        .ambient-glow {{
            position: fixed;
            width: 500px; height: 500px;
            border-radius: 50%;
            filter: blur(140px);
            pointer-events: none;
            z-index: 0;
            opacity: 0.25;
            animation: pulseGlow 12s infinite alternate ease-in-out;
        }}
        .glow-1 {{ top: -100px; right: -100px; background: radial-gradient(circle, var(--accent-primary), transparent 70%); }}
        .glow-2 {{ bottom: -100px; left: -100px; background: radial-gradient(circle, var(--cyan), transparent 70%); }}
        .glow-3 {{ top: 40%; left: 30%; background: radial-gradient(circle, var(--purple), transparent 70%); }}

        @keyframes pulseGlow {{
            0% {{ transform: scale(1) translate(0, 0); opacity: 0.2; }}
            50% {{ transform: scale(1.15) translate(30px, -20px); opacity: 0.35; }}
            100% {{ transform: scale(0.9) translate(-20px, 30px); opacity: 0.2; }}
        }}

        /* App Layout Container */
        .app-wrapper {{ position: relative; z-index: 1; min-height: 100vh; display: flex; flex-direction: column; }}

        /* Header Navigation Bar */
        .app-header {{
            position: sticky; top: 0; z-index: 950;
            background: rgba(15, 20, 36, 0.82);
            backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
            border-bottom: 1px solid var(--border-color);
            padding: 0.9rem 2.5rem;
            display: flex; align-items: center; justify-content: space-between;
            box-shadow: var(--shadow-sm);
        }}
        [data-theme="light"] .app-header {{ background: rgba(255, 255, 255, 0.88); }}

        .logo-brand {{ display: flex; align-items: center; gap: 1rem; text-decoration: none; cursor: pointer; }}
        .logo-avatar {{
            width: 46px; height: 46px; border-radius: 14px;
            background: linear-gradient(135deg, var(--accent-primary), var(--purple));
            display: flex; align-items: center; justify-content: center;
            color: #fff; font-size: 1.4rem;
            box-shadow: var(--shadow-glow);
            transition: var(--transition);
        }}
        .logo-brand:hover .logo-avatar {{ transform: rotate(10deg) scale(1.08); }}
        .logo-title {{ font-size: 1.25rem; font-weight: 900; color: var(--text-primary); letter-spacing: -0.02em; }}
        .logo-title span {{ color: var(--accent-primary); background: linear-gradient(90deg, var(--accent-primary), var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }}
        .logo-subtitle {{ font-size: 0.78rem; color: var(--text-muted); display: block; font-weight: 600; }}

        .header-controls {{ display: flex; align-items: center; gap: 1.2rem; }}

        /* Progress Bar Widget */
        .progress-widget {{
            display: flex; align-items: center; gap: 0.8rem;
            background: var(--bg-card); padding: 0.4rem 1rem;
            border-radius: 50px; border: 1px solid var(--border-color);
            font-size: 0.82rem; font-weight: 700;
        }}
        .progress-bar-fill-track {{
            width: 80px; height: 8px; background: rgba(255, 255, 255, 0.1);
            border-radius: 10px; overflow: hidden; position: relative;
        }}
        .progress-bar-fill-bar {{
            height: 100%; width: 0%;
            background: linear-gradient(90deg, var(--cyan), var(--accent-primary));
            border-radius: 10px; transition: width 0.5s ease;
        }}

        .search-input-box {{ position: relative; width: 280px; }}
        .search-input-box input {{
            width: 100%; padding: 0.6rem 1.2rem 0.6rem 2.6rem;
            background: var(--bg-card); border: 1px solid var(--border-color);
            border-radius: var(--radius-md); color: var(--text-primary);
            font-family: inherit; font-size: 0.88rem; backdrop-filter: blur(8px);
            transition: var(--transition);
        }}
        .search-input-box input:focus {{
            outline: none; border-color: var(--accent-primary);
            box-shadow: var(--shadow-glow); background: var(--bg-card-hover);
        }}
        .search-input-box i {{ position: absolute; left: 0.9rem; top: 50%; transform: translateY(-50%); color: var(--text-muted); }}

        .btn-icon {{
            width: 42px; height: 42px; border-radius: var(--radius-md);
            border: 1px solid var(--border-color); background: var(--bg-card);
            color: var(--text-primary); display: flex; align-items: center; justify-content: center;
            cursor: pointer; transition: var(--transition); font-size: 1.1rem;
        }}
        .btn-icon:hover {{ border-color: var(--accent-primary); color: var(--accent-primary); transform: translateY(-2px); box-shadow: var(--shadow-glow); }}

        .dev-badge {{
            background: var(--accent-light); border: 1px solid rgba(225, 29, 72, 0.4);
            padding: 0.4rem 1rem; border-radius: 50px; font-size: 0.82rem; font-weight: 800;
            color: var(--accent-primary); display: flex; align-items: center; gap: 0.5rem;
            box-shadow: 0 0 15px rgba(225, 29, 72, 0.15);
        }}

        .container {{ max-width: 1280px; margin: 0 auto; padding: 0 1.8rem; width: 100%; }}

        /* Dashboard Hero Section */
        #dashboardView {{ display: block; padding: 2.5rem 0 5rem; animation: fadeInUp 0.6s ease; }}
        
        .track-hero {{
            text-align: center; margin-bottom: 4rem; padding: 4rem 2.5rem;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.88), rgba(30, 41, 59, 0.82)), url('https://images.unsplash.com/photo-1544383835-bda2bc66a55d?auto=format&fit=crop&w=1400&q=80');
            background-size: cover; background-position: center;
            border-radius: var(--radius-xl); border: 1px solid var(--border-color);
            box-shadow: var(--shadow-lg); backdrop-filter: blur(12px);
            position: relative; overflow: hidden;
        }}
        .track-hero::before {{
            content: ''; position: absolute; top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, var(--accent-primary), var(--cyan), var(--purple));
        }}

        .hero-track-badge {{
            display: inline-flex; align-items: center; gap: 0.6rem;
            padding: 0.4rem 1.2rem; background: var(--accent-light);
            border: 1px solid var(--accent-primary); color: #fff;
            font-size: 0.85rem; font-weight: 800; border-radius: 50px;
            text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 1.5rem;
            box-shadow: var(--shadow-glow);
        }}
        .track-hero-title {{
            font-size: 2.8rem; font-weight: 900; color: #fff;
            margin-bottom: 1.2rem; line-height: 1.3; text-shadow: 0 4px 20px rgba(0,0,0,0.5);
        }}
        .track-hero-title span {{
            background: linear-gradient(90deg, #f59e0b, #fb7185);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }}
        .track-hero-desc {{
            font-size: 1.15rem; color: #cbd5e1; max-width: 920px;
            margin: 0 auto 2.5rem; line-height: 1.8; font-weight: 500;
        }}

        .track-stats {{
            display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap;
            border-top: 1px solid rgba(255, 255, 255, 0.12); padding-top: 2rem; margin-top: 1rem;
        }}
        .stat-box {{ text-align: center; position: relative; }}
        .stat-box h4 {{
            font-size: 2.2rem; font-weight: 900;
            background: linear-gradient(135deg, #fff, var(--cyan));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            line-height: 1.2;
        }}
        .stat-box p {{ font-size: 0.88rem; color: #94a3b8; font-weight: 600; margin-top: 0.3rem; }}

        .section-lessons-title {{
            margin-bottom: 2.5rem; display: flex; flex-direction: column; align-items: flex-start; gap: 0.4rem;
        }}
        .section-subtitle-comic {{
            font-size: 0.85rem; font-weight: 800; color: var(--cyan);
            text-transform: uppercase; letter-spacing: 0.1em; display: flex; align-items: center; gap: 0.5rem;
        }}
        .section-title-comic {{ font-size: 2rem; font-weight: 900; color: var(--text-primary); }}

        /* Lesson Cards Grid with 3D Perspective Tilt */
        .lessons-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 2rem;
            perspective: 1000px;
        }}
        .lesson-card {{
            background: var(--bg-card);
            backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--border-color); border-radius: var(--radius-lg);
            padding: 2rem; cursor: pointer; transition: var(--transition);
            display: flex; flex-direction: column; justify-content: space-between;
            position: relative; overflow: hidden; text-align: right; box-shadow: var(--shadow-md);
        }}
        .lesson-card::before {{
            content: ''; position: absolute; top: 0; right: 0; width: 6px; height: 100%;
            background: var(--accent-primary); opacity: 0; transition: var(--transition);
        }}
        .lesson-card:hover {{
            transform: translateY(-8px) rotateX(2deg) rotateY(-2deg);
            border-color: var(--accent-primary);
            box-shadow: var(--shadow-glow), 0 20px 40px rgba(0,0,0,0.4);
            background: var(--bg-card-hover);
        }}
        .lesson-card:hover::before {{ opacity: 1; }}

        .card-top {{ display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 1.4rem; }}
        .lesson-number {{
            font-size: 2.5rem; font-weight: 900; color: var(--text-muted);
            opacity: 0.35; line-height: 1; font-family: 'Inter', sans-serif; transition: var(--transition);
        }}
        .lesson-card:hover .lesson-number {{ color: var(--accent-primary); opacity: 0.9; transform: scale(1.1); }}
        
        .lesson-icon {{
            width: 52px; height: 52px; border-radius: var(--radius-md);
            background: var(--accent-light); color: var(--accent-primary);
            font-size: 1.5rem; display: flex; align-items: center; justify-content: center;
            font-weight: 800; border: 1px solid rgba(225, 29, 72, 0.3); transition: var(--transition);
        }}
        .lesson-card:hover .lesson-icon {{ transform: scale(1.1) rotate(6deg); background: var(--accent-primary); color: #fff; }}

        .lesson-info h3 {{ font-size: 1.35rem; font-weight: 800; color: var(--text-primary); margin-bottom: 0.5rem; }}
        .lesson-info .badge-tag {{
            display: inline-block; font-size: 0.8rem; font-weight: 700;
            color: var(--cyan); background: var(--cyan-light); padding: 0.25rem 0.75rem;
            border-radius: 50px; margin-bottom: 0.9rem; border: 1px solid rgba(6, 182, 212, 0.3);
        }}
        .lesson-info p {{ font-size: 0.94rem; color: var(--text-secondary); line-height: 1.7; margin-bottom: 1.8rem; }}

        .card-footer {{
            border-top: 1px solid var(--border-color); padding-top: 1.1rem;
            display: flex; align-items: center; justify-content: space-between;
            font-size: 0.9rem; font-weight: 700; color: var(--text-muted); transition: var(--transition);
        }}
        .lesson-card:hover .card-footer {{ color: var(--accent-primary); }}
        .cta-arrow {{ display: flex; align-items: center; gap: 0.5rem; transition: var(--transition); }}
        .lesson-card:hover .cta-arrow {{ transform: translateX(-6px); }}

        .lesson-checkbox-wrap {{ display: flex; align-items: center; gap: 0.4rem; font-size: 0.82rem; cursor: pointer; color: var(--text-muted); }}
        .lesson-checkbox-wrap input {{ cursor: pointer; width: 16px; height: 16px; accent-color: var(--accent-primary); }}

        /* Reader View Layout */
        #readerView {{ display: none; padding: 2rem 0 5rem; animation: fadeInUp 0.5s ease; }}
        .reader-top-bar {{
            display: flex; align-items: center; justify-content: space-between;
            background: var(--bg-card); backdrop-filter: blur(16px);
            border: 1px solid var(--border-color); border-radius: var(--radius-lg);
            padding: 1.2rem 1.8rem; margin-bottom: 2rem; box-shadow: var(--shadow-md); flex-wrap: wrap; gap: 1rem;
        }}
        .btn-back-home {{
            display: inline-flex; align-items: center; gap: 0.7rem; padding: 0.7rem 1.5rem;
            background: linear-gradient(135deg, var(--accent-primary), #be123c); color: #fff;
            border: none; border-radius: var(--radius-md); font-weight: 800; font-family: inherit;
            cursor: pointer; transition: var(--transition); text-decoration: none; box-shadow: var(--shadow-glow);
        }}
        .btn-back-home:hover {{ transform: translateY(-3px) scale(1.02); box-shadow: 0 0 30px rgba(225, 29, 72, 0.5); }}

        .reader-lesson-title {{ font-size: 1.5rem; font-weight: 900; display: flex; align-items: center; gap: 1rem; }}
        .reader-lesson-title .badge-num {{
            width: 42px; height: 42px; border-radius: 12px;
            background: var(--accent-light); color: var(--accent-primary);
            font-size: 1.1rem; font-weight: 900; display: flex; align-items: center; justify-content: center;
            border: 1px solid rgba(225, 29, 72, 0.3);
        }}

        /* Reader Tabs Navigation */
        .lesson-tabs-bar {{
            display: flex; gap: 1rem; margin-bottom: 2rem;
            border-bottom: 2px solid var(--border-color); padding-bottom: 0.8rem; overflow-x: auto;
        }}
        .tab-btn {{
            padding: 0.85rem 1.6rem; border: 1px solid transparent; background: transparent;
            color: var(--text-secondary); font-weight: 800; font-size: 0.98rem; font-family: inherit;
            cursor: pointer; border-radius: var(--radius-md); transition: var(--transition);
            display: inline-flex; align-items: center; gap: 0.6rem; white-space: nowrap;
        }}
        .tab-btn:hover {{ background: var(--bg-sidebar); color: var(--text-primary); border-color: var(--border-color); }}
        .tab-btn.active {{
            background: linear-gradient(135deg, var(--accent-primary), var(--purple)); color: #fff;
            box-shadow: var(--shadow-glow); border-color: transparent;
        }}

        .tab-panel {{ display: none; opacity: 0; transition: opacity 0.4s ease; }}
        .tab-panel.active {{ display: block; opacity: 1; animation: fadeInUp 0.4s ease; }}

        /* Rich Content Cards */
        .content-card {{
            background: var(--bg-card); backdrop-filter: blur(16px);
            border: 1px solid var(--border-color); border-radius: var(--radius-lg);
            padding: 2.5rem; margin-bottom: 2rem; box-shadow: var(--shadow-md); position: relative;
        }}
        .content-card h3 {{
            font-size: 1.5rem; font-weight: 800; color: var(--text-primary);
            margin: 1.8rem 0 1rem; border-right: 5px solid var(--accent-primary); padding-right: 1rem;
            display: flex; align-items: center; gap: 0.6rem;
        }}
        .content-card h4 {{ font-size: 1.25rem; font-weight: 700; color: var(--cyan); margin: 1.4rem 0 0.8rem; }}
        .content-card p {{ margin-bottom: 1.2rem; font-size: 1.02rem; color: var(--text-primary); line-height: 1.9; }}
        .content-card ul, .content-card ol {{ margin-right: 2rem; margin-bottom: 1.5rem; }}
        .content-card li {{ margin-bottom: 0.6rem; font-size: 1rem; color: var(--text-secondary); }}

        .core-idea-box {{
            background: linear-gradient(135deg, rgba(225, 29, 72, 0.12), rgba(139, 92, 246, 0.12));
            border-right: 5px solid var(--accent-primary); padding: 1.5rem;
            border-radius: var(--radius-md); margin-bottom: 2rem; border: 1px solid rgba(225, 29, 72, 0.25);
        }}
        .core-idea-box h5 {{ color: var(--accent-primary); font-weight: 800; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.6rem; font-size: 1.15rem; }}

        .table-responsive {{ overflow-x: auto; margin: 1.8rem 0; border-radius: var(--radius-md); border: 1px solid var(--border-color); box-shadow: var(--shadow-sm); }}
        .custom-table {{ width: 100%; border-collapse: collapse; text-align: right; font-size: 0.98rem; }}
        .custom-table th {{ background: var(--bg-sidebar); color: var(--cyan); font-weight: 800; padding: 1.1rem 1.2rem; border-bottom: 2px solid var(--border-color); }}
        .custom-table td {{ padding: 1rem 1.2rem; border-bottom: 1px solid var(--border-color); color: var(--text-secondary); background: rgba(0,0,0,0.15); }}
        .custom-table tr:hover td {{ background: rgba(225, 29, 72, 0.05); color: var(--text-primary); }}

        /* Interactive Diagram Image Box with Lightbox Overlay Trigger */
        .diagram-img-box {{
            background: var(--bg-secondary); border: 2px solid var(--border-color);
            border-radius: var(--radius-lg); padding: 1.5rem; margin: 2rem 0; text-align: center;
            box-shadow: var(--shadow-md); position: relative; overflow: hidden; cursor: pointer; transition: var(--transition);
        }}
        .diagram-img-box:hover {{ border-color: var(--cyan); box-shadow: var(--shadow-cyan-glow); transform: scale(1.01); }}
        .diagram-img-box img {{
            max-width: 100%; height: auto; border-radius: var(--radius-md);
            background: #ffffff; padding: 0.6rem; border: 1px solid var(--border-color); transition: var(--transition);
        }}
        .diagram-zoom-overlay {{
            position: absolute; top: 1rem; left: 1rem;
            background: rgba(0, 0, 0, 0.75); color: #fff; padding: 0.4rem 0.9rem;
            border-radius: 50px; font-size: 0.8rem; font-weight: 700;
            display: flex; align-items: center; gap: 0.5rem; backdrop-filter: blur(8px);
            opacity: 0.85; transition: var(--transition);
        }}
        .diagram-img-box:hover .diagram-zoom-overlay {{ opacity: 1; background: var(--accent-primary); }}
        .diagram-img-caption {{
            font-size: 1rem; font-weight: 800; color: var(--cyan); margin-top: 1rem;
            display: flex; align-items: center; justify-content: center; gap: 0.6rem;
        }}

        .diagram-reasoning-box {{
            background: var(--bg-sidebar); border-right: 5px solid var(--purple);
            border-radius: var(--radius-md); padding: 1.6rem; margin: 1.5rem 0; border: 1px solid rgba(139, 92, 246, 0.25);
        }}
        .diagram-reasoning-box h5 {{ color: var(--purple); font-weight: 800; font-size: 1.1rem; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.6rem; }}

        .diagram-alternative-box {{
            background: var(--yellow-light); border-right: 5px solid var(--yellow);
            border-radius: var(--radius-md); padding: 1.6rem; margin: 1.5rem 0; border: 1px solid rgba(245, 158, 11, 0.3);
        }}
        .diagram-alternative-box h5 {{ color: var(--yellow); font-weight: 800; font-size: 1.1rem; margin-bottom: 0.8rem; display: flex; align-items: center; gap: 0.6rem; }}

        .callout {{ padding: 1.4rem; border-radius: var(--radius-md); margin: 1.8rem 0; display: flex; gap: 1.2rem; align-items: flex-start; border: 1px solid transparent; }}
        .callout-high-yield {{ background: rgba(239, 68, 68, 0.12); border-color: rgba(239, 68, 68, 0.35); color: var(--text-primary); }}
        .callout-high-yield h5 {{ color: #ef4444; font-weight: 800; font-size: 1.1rem; margin-bottom: 0.5rem; }}

        /* Floating Edge Back Tab */
        .edge-back-tab {{
            position: fixed; top: 50%; right: 0; transform: translateY(-50%);
            background: linear-gradient(135deg, var(--accent-primary), var(--purple)); color: #fff;
            padding: 1rem 0.75rem; border-radius: var(--radius-md) 0 0 var(--radius-md);
            cursor: pointer; box-shadow: var(--shadow-lg); z-index: 1000; display: none;
            flex-direction: column; align-items: center; gap: 0.6rem; font-weight: 800;
            font-size: 0.85rem; writing-mode: vertical-rl; transition: var(--transition);
        }}
        .edge-back-tab:hover {{ padding-right: 1.3rem; box-shadow: var(--shadow-glow); }}

        /* Interactive Quiz Styles */
        .quiz-card {{
            background: var(--bg-card); border: 1px solid var(--border-color);
            border-radius: var(--radius-lg); padding: 2rem; margin-bottom: 1.8rem; box-shadow: var(--shadow-sm);
        }}
        .quiz-card h4 {{ font-size: 1.15rem; font-weight: 800; color: var(--text-primary); margin-bottom: 1rem; }}
        .quiz-option {{
            background: var(--bg-sidebar); border: 1px solid var(--border-color);
            padding: 1rem 1.4rem; border-radius: var(--radius-md); cursor: pointer;
            transition: var(--transition); margin-top: 0.8rem; font-weight: 600; display: flex; align-items: center; justify-content: space-between;
        }}
        .quiz-option:hover {{ border-color: var(--cyan); background: var(--cyan-light); color: var(--text-primary); transform: translateX(-4px); }}
        .quiz-option.selected {{ border-color: var(--accent-primary); background: var(--accent-light); color: var(--accent-primary); font-weight: 800; }}

        /* Diagram Lightbox Modal */
        .lightbox-modal {{
            position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
            background: rgba(0, 0, 0, 0.92); backdrop-filter: blur(20px);
            z-index: 2000; display: none; align-items: center; justify-content: center;
            flex-direction: column; padding: 2rem; animation: fadeInUp 0.3s ease;
        }}
        .lightbox-modal.active {{ display: flex; }}
        .lightbox-content {{ position: relative; max-width: 92vw; max-height: 82vh; display: flex; align-items: center; justify-content: center; }}
        .lightbox-content img {{ max-width: 100%; max-height: 80vh; border-radius: 12px; box-shadow: 0 0 50px rgba(0,0,0,0.9); transition: transform 0.3s ease; }}
        .lightbox-controls {{
            margin-top: 1.5rem; display: flex; gap: 1rem; background: var(--bg-card);
            padding: 0.6rem 1.5rem; border-radius: 50px; border: 1px solid var(--border-color);
        }}
        .btn-lightbox {{ background: transparent; border: none; color: #fff; font-size: 1.2rem; cursor: pointer; transition: var(--transition); padding: 0.4rem 0.8rem; border-radius: 8px; }}
        .btn-lightbox:hover {{ color: var(--cyan); background: rgba(255,255,255,0.1); }}
        .lightbox-close {{ position: absolute; top: 2rem; left: 2.5rem; color: #fff; font-size: 2rem; cursor: pointer; transition: var(--transition); }}
        .lightbox-close:hover {{ color: var(--accent-primary); transform: scale(1.2); }}

        /* Interactive Relational Algebra Query Optimization Visual Sandbox */
        .query-sandbox-container {{
            background: var(--bg-secondary); border: 1px solid var(--cyan);
            border-radius: var(--radius-lg); padding: 2rem; margin: 2rem 0; box-shadow: var(--shadow-cyan-glow);
        }}
        .sandbox-header {{ display: flex; align-items: center; justify-content: space-between; margin-bottom: 1.5rem; flex-wrap: wrap; gap: 1rem; }}
        .sandbox-title {{ font-size: 1.2rem; font-weight: 900; color: var(--cyan); display: flex; align-items: center; gap: 0.6rem; }}
        .sandbox-stepper {{ display: flex; gap: 0.6rem; flex-wrap: wrap; }}
        .btn-step {{
            padding: 0.5rem 1rem; border-radius: 50px; border: 1px solid var(--border-color);
            background: var(--bg-card); color: var(--text-secondary); font-size: 0.85rem; font-weight: 700;
            cursor: pointer; transition: var(--transition);
        }}
        .btn-step.active {{ background: var(--cyan); color: #fff; border-color: var(--cyan); box-shadow: 0 0 15px rgba(6, 182, 212, 0.4); }}
        
        .tree-visual-display {{
            background: var(--bg-primary); border-radius: var(--radius-md); padding: 1.5rem;
            text-align: center; border: 1px solid var(--border-color); font-family: 'Fira Code', monospace; font-size: 1.1rem;
            color: var(--yellow); min-height: 120px; display: flex; flex-direction: column; align-items: center; justify-content: center;
        }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        @media (max-width: 768px) {{
            .app-header {{ padding: 0.8rem 1.2rem; }}
            .track-hero-title {{ font-size: 1.9rem; }}
            .lessons-grid {{ grid-template-columns: 1fr; }}
            .search-input-box {{ width: 180px; }}
            .progress-widget {{ display: none; }}
        }}
    </style>
</head>
<body>

    <!-- Dynamic Database Network Canvas -->
    <canvas id="dbParticleCanvas"></canvas>

    <!-- Background Ambient Glow Blobs -->
    <div class="ambient-glow glow-1"></div>
    <div class="ambient-glow glow-2"></div>
    <div class="ambient-glow glow-3"></div>

    <div class="app-wrapper">

        <!-- App Top Header -->
        <header class="app-header">
            <a class="logo-brand" onclick="showDashboardView()">
                <div class="logo-avatar"><i class="fa-solid fa-database"></i></div>
                <div class="logo-text">
                    <div class="logo-title">Database<span>Mastery</span></div>
                    <span class="logo-subtitle">المنصة التفاعلية المتقدمة لقواعد البيانات والتحليل البصري</span>
                </div>
            </a>

            <div class="header-controls">
                <!-- Learning Progress Widget -->
                <div class="progress-widget">
                    <i class="fa-solid fa-graduation-cap" style="color:var(--cyan);"></i>
                    <span>إنجاز المنهج: <span id="progressPercent">0%</span></span>
                    <div class="progress-bar-fill-track">
                        <div class="progress-bar-fill-bar" id="progressBarFill"></div>
                    </div>
                </div>

                <div class="search-input-box">
                    <i class="fa-solid fa-magnifying-glass"></i>
                    <input type="text" id="globalSearchInput" placeholder="بحث شامل في المحاضرات والرسومات (Ctrl+K)...">
                </div>

                <button class="btn-icon" id="themeToggle" title="تبديل المظهر (Dark / Light)"><i class="fa-solid fa-moon"></i></button>
                <div class="dev-badge"><i class="fa-solid fa-code"></i> Eng. Adham Hany</div>
            </div>
        </header>

        <!-- Sticky Floating Back Button -->
        <div class="edge-back-tab" id="edgeBackTab" onclick="showDashboardView()">
            <i class="fa-solid fa-arrow-right"></i>
            <span>العودة للمحاضرات</span>
        </div>

        <!-- VIEW 1: DASHBOARD VIEW -->
        <div id="dashboardView">
            <div class="container">

                <section class="track-hero">
                    <div class="hero-track-badge"><i class="fa-solid fa-sparkles"></i> DATABASE SYSTEMS ULTIMATE INTERACTIVE MASTERCLASS</div>
                    <h1 class="track-hero-title">تفكيك وتفصيل جميع محاضرات ورسومات قواعد البيانات <span>من الصفر إلى الاحتراف</span></h1>
                    <p class="track-hero-desc">منصة تفاعلية بصرية فائقة السلاسة! تشرح كل مفهوم بالتفصيل من السهل للمتقدم، وتفكك كل رسمة بالكامل مع بيان <strong>سبب اختيار الحل (ليه الحل كده)</strong> و<strong>الحلول البديلة الممكنة (Alternative Approaches)</strong> ومقارنة المزايا والعيوب لضمان تفوق الطالب في الامتحان.</p>

                    <div class="track-stats">
                        <div class="stat-box"><h4>11</h4><p>محاضرة تفصيلية</p></div>
                        <div class="stat-box"><h4>100%</h4><p>تحليل كامل للرسومات والبدائل</p></div>
                        <div class="stat-box"><h4>7</h4><p>خطوات تحويل الـ ER المفصلة</p></div>
                        <div class="stat-box"><h4>8A-8D</h4><p>خيارات الـ EER الأربعة</p></div>
                    </div>
                </section>

                <div class="section-lessons-title">
                    <span class="section-subtitle-comic"><i class="fa-solid fa-layer-group"></i> SELECT LESSON / MODULE</span>
                    <h2 class="section-title-comic">اختر المحاضرة للبدء في الشرح والتفاصيل والبدائل</h2>
                </div>

                <div class="lessons-grid">

                    <div class="lesson-card" onclick="openLessonReader('lec1')">
                        <div class="card-top">
                            <span class="lesson-number">01</span>
                            <div class="lesson-icon"><i class="fa-solid fa-file-code"></i></div>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 1: Intro to DBMS & File Systems</h3>
                            <span class="badge-tag">شرح مفصل + 7 مشاكل + مقارنات</span>
                            <p>شرح مفهوم قواعد البيانات، الـ 7 مشاكل الكارثية لنظم الملفات القديمة، Catalog و Meta-data وتجريد البيانات.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec1', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec2')">
                        <div class="card-top">
                            <span class="lesson-number">02</span>
                            <span class="lesson-icon"><i class="fa-solid fa-users-gear"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 2: Roles & Transactions (ACID)</h3>
                            <span class="badge-tag">تصنيف المستخدمين + شرح ACID</span>
                            <p>شرح أدوار المستخدمين الأربعة، معمارية المعاملات Transactions والشرح الدقيق لخصائص الـ ACID الأربعة وسيناريوهات النظام.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec2', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec3')">
                        <div class="card-top">
                            <span class="lesson-number">03</span>
                            <span class="lesson-icon"><i class="fa-solid fa-cubes"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 3: Three-Schema & Independence</h3>
                            <span class="badge-tag">نماذج البيانات + معمارية المستويات 3</span>
                            <p>نماذج البيانات، شرح المستويات الثلاثة (External, Conceptual, Internal) والاستقلالية المنطقية والفيزيائية ولغات الـ DBMS.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec3', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec4')">
                        <div class="card-top">
                            <span class="lesson-number">04</span>
                            <span class="lesson-icon"><i class="fa-solid fa-sitemap"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 4: DB Lifecycle & ER Basics</h3>
                            <span class="badge-tag">دورة التصميم + أنواع الصفات والمفاتيح</span>
                            <p>دورة تطوير قواعد البيانات، والتعرف على أنواع الصفات الستة بالتفصيل مع الأمثلة والرموز والمفاتيح (Super, Candidate, Primary).</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec4', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec5')">
                        <div class="card-top">
                            <span class="lesson-number">05</span>
                            <span class="lesson-icon"><i class="fa-solid fa-diagram-project"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 5: Relationships & Weak Entities</h3>
                            <span class="badge-tag">شرح العلاقات الشامل + الكيانات الضعيفة</span>
                            <p>درجة العلاقات (Unary, Binary, Ternary)، التعددية (1:1, 1:N, N:M)، المشاركة الكلية والجزئية، والكيانات الضعيفة ومفاتيحها الجزئية.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec5', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec6')">
                        <div class="card-top">
                            <span class="lesson-number">06</span>
                            <span class="lesson-icon"><i class="fa-solid fa-pen-ruler"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 6: ER Conceptual Case Studies</h3>
                            <span class="badge-tag">تحليل النظم + 5 سيناريوهات عمل</span>
                            <p>قواعد تحويل النصوص إلى ER Diagram، وتحليل متطلبات الشركات والتطبيقات (Mail Order, Transcripts, Airline, Conference).</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec6', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec8')">
                        <div class="card-top">
                            <span class="lesson-number">07</span>
                            <span class="lesson-icon"><i class="fa-solid fa-table-cells"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 8: 7-Step ER-to-Relational Mapping</h3>
                            <span class="badge-tag">خوارزمية التحويل السبعة + رسمة البنك والبدائل</span>
                            <p>شرح مفصل جداً لكل خطوة من خطوات التحويل السبعة بالدستور الأكاديمي مع رسمة تحويل البنك الأصلية وتحليل الحل والحلول البديلة.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec8', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec9')">
                        <div class="card-top">
                            <span class="lesson-number">08</span>
                            <span class="lesson-icon"><i class="fa-solid fa-square-poll-vertical"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 9: Relational & Reverse Engineering</h3>
                            <span class="badge-tag">تحويل الشركات والطيران + تمرين الهندسة العكسية</span>
                            <p>تحويل COMPANY ER و AIRLINE ER لجداول علاائقية، وتمرين الهندسة العكسية من جداول مكتبة LIBRARY بالشرح التفكيكي والبدائل.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec9', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec10')">
                        <div class="card-top">
                            <span class="lesson-number">09</span>
                            <span class="lesson-icon"><i class="fa-solid fa-network-wired"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 10: Enhanced ER (EER) Concepts</h3>
                            <span class="badge-tag">شرح مفصل للـ EER + القيود الأربعة</span>
                            <p>الفئات العليا والفرعية Superclass/Subclass، وراثة الصفات، وقيود التخصص Disjointness (d/o) والـ Completeness (Total/Partial).</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec10', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec11')">
                        <div class="card-top">
                            <span class="lesson-number">10</span>
                            <span class="lesson-icon"><i class="fa-solid fa-vial-circle-check"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 11: EER Exercises & Diagnostics</h3>
                            <span class="badge-tag">3 رسومات تشخيصية + رسمة البنك المطور</span>
                            <p>تحليل أخطاء الـ EER التشخيصية الثلاثة (A, B, C) وبيان أسباب صحتها أو خطئها وكيفية تعديلها، ورسمة البنك المطور وبدائلها.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec11', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" onclick="openLessonReader('lec12')">
                        <div class="card-top">
                            <span class="lesson-number">11</span>
                            <span class="lesson-icon"><i class="fa-solid fa-gears"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>Lec 12: EER Mapping Options (8A–8D) & Query Trees</h3>
                            <span class="badge-tag">خيارات الـ EER الأربعة + محاكي الألجبرا التفاعلي</span>
                            <p>شرح مفصل لخيارات تحويل التخصص والوراثة لجداول (Options 8A, 8B, 8C, 8D) وموازنة المزايا والعيوب والحلول البديلة ومحاكاة شجيرات الألجبرا.</p>
                        </div>
                        <div class="card-footer">
                            <label class="lesson-checkbox-wrap" onclick="event.stopPropagation()">
                                <input type="checkbox" onchange="toggleLessonComplete('lec12', this.checked)"> تم الفهم
                            </label>
                            <span class="cta-arrow">ابدأ المحاضرة ←</span>
                        </div>
                    </div>

                    <div class="lesson-card" style="border-color:var(--accent-primary); background:linear-gradient(135deg, var(--bg-card), rgba(225, 29, 72, 0.15));" onclick="openLessonReader('exam')">
                        <div class="card-top">
                            <span class="lesson-number" style="color:var(--accent-primary); opacity:1;">🎓</span>
                            <span class="lesson-icon" style="background:var(--accent-primary); color:#fff;"><i class="fa-solid fa-trophy"></i></span>
                        </div>
                        <div class="lesson-info">
                            <h3>الامتحان النهائي التفاعلي الشامل</h3>
                            <span class="badge-tag" style="color:var(--yellow); background:var(--yellow-light);">اختبار محاكي مع احتفال التصحيح الفوري</span>
                            <p>اختبار شامل يحتوي على جميع أنواع الأسئلة الامتحانية مع حساب التقدير الفوري والنتيجة وتفسير كل إجابة والبدائل.</p>
                        </div>
                        <div class="card-footer" style="color:var(--accent-primary);">
                            <span>اختبار شامل متكامل</span>
                            <span class="cta-arrow">ابدأ الامتحان ←</span>
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!-- VIEW 2: LESSON READER VIEW -->
        <div id="readerView">
            <div class="container">

                <div class="reader-top-bar">
                    <button class="btn-back-home" onclick="showDashboardView()">
                        <i class="fa-solid fa-arrow-right"></i> العودة لقائمة المحاضرات
                    </button>
                    <div class="reader-lesson-title" id="readerLessonTitle">
                        <span class="badge-num" id="readerBadgeNum">01</span>
                        <span id="readerTitleText">Introduction to DBMS</span>
                    </div>
                </div>

                <div class="lesson-tabs-bar">
                    <button class="tab-btn active" onclick="switchTab('tab-explain')"><i class="fa-solid fa-book-open"></i> 📖 الشرح التفصيلي وتفكيك الرسومات والبدائل</button>
                    <button class="tab-btn" onclick="switchTab('tab-summary')"><i class="fa-solid fa-bolt"></i> ⚡ الملخص و High-Yield</button>
                    <button class="tab-btn" onclick="switchTab('tab-practice')"><i class="fa-solid fa-pen-to-square"></i> 📝 بنك الأسئلة والتطبيقات المحلولة</button>
                    <button class="tab-btn" onclick="switchTab('tab-tricks')"><i class="fa-solid fa-lightbulb"></i> 🧠 شفرات الحفظ والتعريفات الأكاديمية</button>
                </div>

                <div class="tab-panel active" id="tab-explain">
                    <div id="explainContent"></div>
                </div>

                <div class="tab-panel" id="tab-summary">
                    <div id="summaryContent"></div>
                </div>

                <div class="tab-panel" id="tab-practice">
                    <div id="practiceContent"></div>
                </div>

                <div class="tab-panel" id="tab-tricks">
                    <div id="tricksContent"></div>
                </div>

            </div>
        </div>

    </div>

    <!-- Lightbox Diagram Zoom Modal -->
    <div class="lightbox-modal" id="diagramModal">
        <div class="lightbox-close" onclick="closeLightbox()"><i class="fa-solid fa-xmark"></i></div>
        <div class="lightbox-content">
            <img id="lightboxImg" src="" alt="Zoomed Diagram">
        </div>
        <div class="lightbox-controls">
            <button class="btn-lightbox" onclick="zoomLightbox(1.2)" title="تكبير"><i class="fa-solid fa-magnifying-glass-plus"></i></button>
            <button class="btn-lightbox" onclick="zoomLightbox(0.8)" title="تصغير"><i class="fa-solid fa-magnifying-glass-minus"></i></button>
            <button class="btn-lightbox" onclick="resetLightbox()" title="إعادة تعيين"><i class="fa-solid fa-rotate-left"></i></button>
        </div>
    </div>

    <!-- Canvas Confetti & Web Audio API Engine -->
    <script>
        // Web Audio API Synth Sound Generator
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        function playUiSound(type) {{
            try {{
                if (audioCtx.state === 'suspended') {{ audioCtx.resume(); }}
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                
                if (type === 'click') {{
                    osc.frequency.setValueAtTime(440, audioCtx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.08);
                    gain.gain.setValueAtTime(0.12, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.08);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.08);
                }} else if (type === 'win') {{
                    osc.frequency.setValueAtTime(523.25, audioCtx.currentTime);
                    osc.frequency.setValueAtTime(659.25, audioCtx.currentTime + 0.1);
                    osc.frequency.setValueAtTime(783.99, audioCtx.currentTime + 0.2);
                    gain.gain.setValueAtTime(0.2, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.4);
                    osc.start(); osc.stop(audioCtx.currentTime + 0.4);
                }}
            }} catch(e) {{}}
        }}

        // Canvas Confetti Generator
        function triggerConfetti() {{
            const canvas = document.createElement('canvas');
            canvas.style.position = 'fixed';
            canvas.style.top = '0'; canvas.style.left = '0';
            canvas.style.width = '100vw'; canvas.style.height = '100vh';
            canvas.style.pointerEvents = 'none'; canvas.style.zIndex = '3000';
            document.body.appendChild(canvas);
            const ctx = canvas.getContext('2d');
            canvas.width = window.innerWidth; canvas.height = window.innerHeight;
            
            const particles = [];
            const colors = ['#e11d48', '#06b6d4', '#f59e0b', '#10b981', '#8b5cf6'];
            for (let i = 0; i < 80; i++) {{
                particles.push({{
                    x: canvas.width / 2, y: canvas.height / 2,
                    vx: (Math.random() - 0.5) * 14, vy: (Math.random() - 0.7) * 14,
                    size: Math.random() * 8 + 4, color: colors[Math.floor(Math.random() * colors.length)],
                    life: 1
                }});
            }}
            function render() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                let alive = false;
                particles.forEach(p => {{
                    p.x += p.vx; p.y += p.vy; p.vy += 0.3; p.life -= 0.015;
                    if (p.life > 0) {{
                        alive = true;
                        ctx.fillStyle = p.color; ctx.globalAlpha = p.life;
                        ctx.fillRect(p.x, p.y, p.size, p.size);
                    }}
                }});
                if (alive) requestAnimationFrame(render);
                else canvas.remove();
            }}
            render();
        }}

        // Database Network Particle Canvas
        (function initParticleCanvas() {{
            const canvas = document.getElementById('dbParticleCanvas');
            const ctx = canvas.getContext('2d');
            let width, height;
            function resize() {{
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            }}
            window.addEventListener('resize', resize);
            resize();

            const nodes = [];
            for (let i = 0; i < 40; i++) {{
                nodes.push({{
                    x: Math.random() * width, y: Math.random() * height,
                    vx: (Math.random() - 0.5) * 0.8, vy: (Math.random() - 0.5) * 0.8,
                    radius: Math.random() * 2.5 + 1.5,
                    type: Math.random() > 0.5 ? 'entity' : 'relation'
                }});
            }}

            function draw() {{
                ctx.clearRect(0, 0, width, height);
                for (let i = 0; i < nodes.length; i++) {{
                    let n = nodes[i];
                    n.x += n.vx; n.y += n.vy;
                    if (n.x < 0 || n.x > width) n.vx *= -1;
                    if (n.y < 0 || n.y > height) n.vy *= -1;

                    ctx.fillStyle = n.type === 'entity' ? '#06b6d4' : '#e11d48';
                    ctx.beginPath();
                    ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
                    ctx.fill();

                    for (let j = i + 1; j < nodes.length; j++) {{
                        let n2 = nodes[j];
                        let dx = n.x - n2.x, dy = n.y - n2.y;
                        let dist = Math.sqrt(dx * dx + dy * dy);
                        if (dist < 130) {{
                            ctx.strokeStyle = 'rgba(255, 255, 255, ' + (1 - dist / 130) * 0.12 + ')';
                            ctx.lineWidth = 1;
                            ctx.beginPath(); ctx.moveTo(n.x, n.y); ctx.lineTo(n2.x, n2.y); ctx.stroke();
                        }}
                    }}
                }}
                requestAnimationFrame(draw);
            }}
            draw();
        }})();

        // Data Store
        const lessonsData = {{
            'lec1': {{
                num: '01',
                title: 'Introduction to Database Systems & DBMS',
                explain: `
                    <div class="content-card">
                        <div class="core-idea-box">
                            <h5><i class="fa-solid fa-bullseye"></i> الفكرة الأساسية (Core Idea)</h5>
                            <p>نظام إدارة قواعد البيانات (DBMS - Database Management System) هو نظام برمجي محوري يقوم بإنشاء وإدارة وصيانة قاعدة البيانات بطريقة مركزية، متغلباً على كافة عيوب ومشاكل نظام الملفات القديم (File Processing System).</p>
                        </div>

                        <h3>1. ما هي قاعدة البيانات وما هو الـ DBMS؟</h3>
                        <p><strong>قاعدة البيانات (Database):</strong> هي تجميع منطقي لمنظومة من البيانات المرتبطة ببعضها البعض (Logically related data)، والتي تمثل جوانب من العالم الحقيقي (Mini-world / Universe of Discourse).</p>
                        <p><strong>نظام إدارة قواعد البيانات (DBMS):</strong> هو مجموعة من البرامج التي تمكن المستخدمين من إنشاء وصيانة قاعدة البيانات وتتضمن عمليات تعريف الهيكل (Defining)، التخزين والاستعلام (Manipulating)، والمشاركة الآمنة (Sharing).</p>

                        <h3>2. المشاكل السبعة الكارثية لنظام الملفات القديم (File Processing System)</h3>
                        <p>في النظام القديم، كانت كل إدارة تحتفظ بملفاتها الخاصة برمجياً، مما أدى للمشاكل التالية التي يأتي عنها أسئلة امتحانية دائمة:</p>
                        <ol>
                            <li><strong>تكرار وتضارب البيانات (Data Redundancy & Inconsistency):</strong> كتابة البيانات نفسها في عدة ملفات، مما يؤدي إلى تضارب القيم إذا تم تحديث أحد الملفات دون الآخرى.</li>
                            <li><strong>صعوبة الوصول للبيانات (Difficulty in Accessing Data):</strong> الحاجة لكتابة برنامج جديد كلياً لكل استعلام جديد يطلبه المستخدم.</li>
                            <li><strong>عزل البيانات (Data Isolation):</strong> البيانات مشتتة في ملفات ذات صيغ مختلفة، مما يجعل ربطها معقداً.</li>
                            <li><strong>مشاكل قيود التكامل (Integrity Problems):</strong> صعوبة تطبيق الشروط والقواعد (مثل أن يكون الراتب أرقاماً موجبة) داخل كود البرامج المتعددة.</li>
                            <li><strong>عدم ذرية العمليات (Atomicity Problems):</strong> إذا انقطع التيار الكهربائي أثناء تحويل مالي بين ملفين، يضيع المبلغ دون وجود آلية تراجع (Rollback).</li>
                            <li><strong>تضارب الوصول المتزامن (Concurrent Access Anomalies):</strong> إذا حاول مستخدمان تعديل الملف نفسه في الوقت ذاته، تتدمر البيانات.</li>
                            <li><strong>مشاكل الأمان (Security Problems):</strong> صعوبة تحديد أذونات مخصصة لكل مستخدم على مستوى الملفات.</li>
                        </ol>

                        <h3>3. المزايا الجوهرية لنظام الـ DBMS</h3>
                        <div class="table-responsive">
                            <table class="custom-table">
                                <thead>
                                    <tr><th>الميزة العلمية (Feature)</th><th>الشرح التفصيلي والدور العملي</th></tr>
                                </thead>
                                <tbody>
                                    <tr><td><strong>Self-describing Nature</strong></td><td>يحتوي النظام على فهرس (Catalog / Data Dictionary) يخزن وصف قواعد وهياكل البيانات (Meta-data).</td></tr>
                                    <tr><td><strong>Program-Data Independence</strong></td><td>فصل هيكل تخزين البيانات عن التطبيقات، بحيث أن أي تعديل في طريقة التخزين لا يلزم تعديل كود البرامج.</td></tr>
                                    <tr><td><strong>Data Abstraction</strong></td><td>توفير رؤية مفهومية مقبولة للمستخدمين وإخفاء تفاصيل التخزين الفيزيائية المعقدة على الأقراص.</td></tr>
                                    <tr><td><strong>Multiple Views</strong></td><td>إمكانية إنشاء رؤية مخصصة (View) لكل مستخدم تظهر البيانات المصرح له بها فقط.</td></tr>
                                    <tr><td><strong>Controlled Redundancy</strong></td><td>التحكم التام في التكرار وتقليله لأدنى درجة ممكنة مع الحفاظ على التناسق والاتساق.</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                `,
                summary: `
                    <div class="content-card">
                        <div class="callout callout-high-yield">
                            <h5>🔥 High Yield — أهم نقاط الامتحان في المحاضرة الأولى</h5>
                            <ul>
                                <li>الفرق الرئيسي بين الملفات والـ DBMS هو وجود الـ <strong>Catalog</strong> الذي يخزن الـ <strong>Meta-data</strong>.</li>
                                <li>الـ <strong>Program-Data Independence</strong> تعني أن تغير هيكل التخزين الفيزيائي لا يؤثر على البرامج والتطبيقات.</li>
                                <li>الـ <strong>Data Abstraction</strong> يعطي المستخدم رؤية مفاهيمية مع إخفاء تفاصيل القرص الصلب.</li>
                            </ul>
                        </div>
                    </div>
                `,
                practice: `
                    <div class="content-card">
                        <h3>📝 بنك الأسئلة الشامل (Lecture 1)</h3>
                        <div class="quiz-card">
                            <h4>سؤال 1: ما هو المصطلح الذي يعبر عن "البيانات التي تصف البيانات"؟</h4>
                            <p style="color:var(--success); font-weight:bold;">الجواب: Meta-data وتخزن داخل الفهرس (Catalog / Data Dictionary).</p>
                        </div>
                        <div class="quiz-card">
                            <h4>سؤال 2: ما هي المشكلة في نظام الملفات القديم التي تسبب عدم الاتساق؟</h4>
                            <p style="color:var(--success); font-weight:bold;">الجواب: تكرار البيانات غير المتحكم به (Uncontrolled Data Redundancy).</p>
                        </div>
                        <div class="quiz-card">
                            <h4>سؤال 3: متى يفضل عدم استخدام نظام قواعد البيانات DBMS؟</h4>
                            <p style="color:var(--success); font-weight:bold;">الجواب: في الأنظمة البسيطة جداً لمستخدم واحد، أو الأنظمة ذات الوقت الحقيقي الصارم جداً Real-time ذات الموارد المحدودة.</p>
                        </div>
                    </div>
                `,
                tricks: `
                    <div class="content-card">
                        <h3>🧠 مصطلحات يجب حفظها</h3>
                        <ul>
                            <li><strong>DBMS:</strong> Database Management System</li>
                            <li><strong>Meta-data:</strong> Data about Data</li>
                            <li><strong>Catalog:</strong> الفهرس الذي يخزن هياكل وقواعد البيانات</li>
                        </ul>
                    </div>
                `
            }},

            'lec8': {{
                num: '07',
                title: '7-Step ER-to-Relational Mapping & Bank Diagram',
                explain: `
                    <div class="content-card">
                        <h3>🖼️ رسمة مخطط الـ BANK ER Schema من المحاضرة</h3>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec8_bank}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط لتكبير التحليل البصري</div>
                            <img src="{b64_lec8_bank}" alt="Bank ER Schema">
                            <div class="diagram-img-caption"><i class="fa-solid fa-building-columns"></i> مخطط BANK ER Schema من سلايد Lecture 8 Page 3</div>
                        </div>

                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه الحل كده؟ (Reasoning & Analysis)</h5>
                            <p>1. <strong>BANK_BRANCH كيان ضعيف (Weak Entity):</strong> تم تمثيله بمستطيل مزدوج لأنه لا يملك مفتاحاً كافياً بمفرده تميز كل فرع عالمياً (يمتلك فقط Branch_no كـ Partial Key)، ولذلك يرتبط بعلاقة تعريفية مزدوجة <code>BRANCHES</code> مع الكيان القوي <code>BANK</code>.</p>
                            <p>2. <strong>علاقات A_C و L_C هي N:M:</strong> الحسابات والعملاء بينهما علاقة متعدد لمتعدد N:M لأن العميل الواحد يمكنه امتلاك عدة حسابات، والحساب المشترك يمكن أن يمتلكه أكثر من عميل.</p>
                        </div>

                        <div class="diagram-alternative-box">
                            <h5><i class="fa-solid fa-lightbulb"></i> الحلول البديلة الممكنة (Alternative Approaches)</h5>
                            <p><strong>البديل الأول لـ BANK_BRANCH:</strong> تحويل <code>BANK_BRANCH</code> إلى كيان قوي (Regular Entity) عبر إنشاء صفة مفتاحية جديدة فريدة عالمياً مثل <code>Branch_ID</code> بدلاً من الاعتماد على <code>Bank_code</code>. ميزة هذا البديل: تبسيط المفتاح الرئيسي وجعله عموداً واحداً، ولكن عيبه: فقدان تمثيل قيد وجود الفرع ككيان متبوع ببنك رئيسي.</p>
                            <p><strong>البديل الثاني لعلاقات A_C:</strong> إذا اشترطت إدارة البنك أن الحساب يمتلكه عميل واحد فقط، تتحول العلاقة من N:M إلى 1:N وبالتالي نضع مفتاح العميل <code>Ssn</code> كـ Foreign Key داخل جدول <code>ACCOUNT</code> وتلغى علاقة الـ lookup table <code>A_C</code>.</p>
                        </div>

                        <h3 style="margin-top:2rem;">شرح خوارزمية الخطوات السبع (7-Step Mapping Algorithm) بالتفصيل الدقيق</h3>
                        <div class="table-responsive">
                            <table class="custom-table">
                                <thead>
                                    <tr><th>الخطوة (Step)</th><th>الحالة المستهدفة (ER Construct)</th><th>قاعدة التحويل والحلول البديلة الممكنة</th></tr>
                                </thead>
                                <tbody>
                                    <tr><td><strong>Step 1</strong></td><td>Regular Entity Types</td><td>كل كيان قوي يتحول لجدول R ندرج فيه الصفات البسيطة ونحدد المفتاح الرئيسي.</td></tr>
                                    <tr><td><strong>Step 2</strong></td><td>Weak Entity Types</td><td>كل كيان ضعيف يتحول لجدول ندرج صفاته + المفتاح الرئيسي للكيان القوي كـ FK. المفتاح الرئيسي = (Owner PK + Partial Key).</td></tr>
                                    <tr><td><strong>Step 3</strong></td><td>Binary 1:1 Relationships</td><td>
                                        <strong>النهج الأساسي (Foreign Key):</strong> نضع المفتاح الرئيسي لأحد الكيانين كـ FK في الآخر (يفضل الكيان ذو المشاركة الكلية Total).<br>
                                        <strong>البديل 2 (Merged Relation):</strong> دمج الكيانين في جدول واحد (يُستخدم فقط إذا كانت كلا المشاركتين كليتان Total).<br>
                                        <strong>البديل 3 (Cross-Reference):</strong> إنشاء جدول ثالث للعلاقة (يُفضل إذا كانت كلا المشاركتين جزئيتين Partial).
                                    </td></tr>
                                    <tr><td><strong>Step 4</strong></td><td>Binary 1:N Relationships</td><td>نضع المفتاح الرئيسي للجانب (1) كـ Foreign Key في جدول الجانب (N).</td></tr>
                                    <tr><td><strong>Step 5</strong></td><td>Binary N:M Relationships</td><td>ينشأ جدول جديد S للعلاقة يضم المفتاحين الرئيسيية كـ FKs، والمفتاح الرئيسي مركباً منهما (PK1, PK2).</td></tr>
                                    <tr><td><strong>Step 6</strong></td><td>Multivalued Attributes</td><td>ينشأ لكل صفة متعددة القيمة A جدول جديد يضم القيمة A + المفتاح الرئيسي للأب كـ FK. المفتاح الرئيسي = (Parent PK, A).</td></tr>
                                    <tr><td><strong>Step 7</strong></td><td>N-ary Relationships</td><td>ينشأ جدول جديد يضم المفاتيح الرئيسية لجميع الكيانات المشاركة كـ FKs.</td></tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                `,
                summary: `<div class="content-card"><div class="callout callout-high-yield"><h5>🔥 شفرة خوارزمية التحويل والبدائل</h5><p>R - W - 1 - N - M - V - N<br>تذكر دائماً أن علاقة 1:1 تملك 3 نهج بديلة للتحويل!</p></div></div>`,
                practice: `<div class="content-card"><p><strong>Q: متى يفضل نهج Merged Relation في علاقة 1:1؟</strong></p><p>عندما تكون مشاركة الكيانين كليتان (Both participations are Total).</p></div>`,
                tricks: `<div class="content-card"><p>علاقة N:M تنشئ دائماً جدولاً ثالثاً جديداً بدون أي حلول بديلة أخرى.</p></div>`
            }},

            'lec9': {{
                num: '08',
                title: 'Relational Schema & Reverse Engineering Exercises',
                explain: `
                    <div class="content-card">
                        <h3>🖼️ 1. رسمة COMPANY ER Diagram (Exercise 1)</h3>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec9_company}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط لتكبير التحليل البصري</div>
                            <img src="{b64_lec9_company}">
                            <div class="diagram-img-caption">رسمة COMPANY ER Diagram من Lecture 9 Page 2</div>
                        </div>

                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه الحل كده في جدول COMPANY؟</h5>
                            <p>1. <strong>وضع Mgr_ssn في DEPARTMENT:</strong> لأن مشاركة DEPARTMENT في علاقة MANAGES مشاركة كليّة (Total)، فوضع المفتاح في جانب الـ Total يمنع تماماً وجود قيم Null.</p>
                            <p>2. <strong>إنشاء جدول مستقل لـ WORKS_ON:</strong> لأن العلاقة بين الموظفين والمشاريع هي متعدد لمتعدد N:M، ولكي نتمكن من تسجيل ساعات عمل كل موظف على كل مشروع دون تكرار البيانات.</p>
                        </div>

                        <div class="diagram-alternative-box">
                            <h5><i class="fa-solid fa-lightbulb"></i> الحلول البديلة لـ MANAGES 1:1</h5>
                            <p><strong>البديل الأول:</strong> وضع <code>Dnumber</code> المدار داخل جدول <code>EMPLOYEE</code> كـ Foreign Key. عيب هذا البديل: ينشئ الكثير من قيم Null لأن معظم الموظفين ليسوا مدراء أقسام.</p>
                            <p><strong>البديل الثاني:</strong> إنشاء جدول ثالث للعلاقة <code>MANAGES(Mgr_ssn, Dnumber, Start_date)</code>. عيب هذا البديل: يتطلب عملية Join إضافية عند الاستعلام عن بيانات الإدارة.</p>
                        </div>

                        <h3 style="margin-top:2.5rem;">🖼️ 2. رسمة AIRLINE ER Diagram (Exercise 2)</h3>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec9_airline}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط لتكبير التحليل البصري</div>
                            <img src="{b64_lec9_airline}">
                            <div class="diagram-img-caption">رسمة AIRLINE ER Diagram من Lecture 9 Page 3</div>
                        </div>

                        <h3 style="margin-top:2.5rem;">🖼️ 3. رسمة الهندسة العكسية LIBRARY Relational Schema (Exercise 3)</h3>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec9_library}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط لتكبير التحليل البصري</div>
                            <img src="{b64_lec9_library}">
                            <div class="diagram-img-caption">رسمة جداول مكتبة LIBRARY من Lecture 9 Page 4</div>
                        </div>

                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه تم استنتاج الـ ER بالشكل ده في الهندسة العكسية؟</h5>
                            <p>1. <strong>جدول BOOK_AUTHORS:</strong> مفتاحه الرئيسي مركّب <code>(Book_id, Author_name)</code> حيث <code>Book_id</code> مفتاح أجنبي يوجه لـ BOOK. هذا يثبت علمياً أن <code>Author_name</code> كانت صفة متعددة القيمة Multivalued Attribute للكيان BOOK.</p>
                            <p>2. <strong>جدول BOOK_LOANS:</strong> مفتاحه الرئيسي يضم 3 مفاتيح أجنبية <code>(Book_id, Branch_id, Card_no)</code>. هذا يثبت أن العملية تمثل علاقة ثلاثية N-ary Relationship تجمع بين كتاب وفرع ومستعير.</p>
                        </div>
                    </div>
                `,
                summary: `<div class="content-card"><p>الهندسة العكسية تعتمد على تتبع المفاتيح المركبة والأجنبية لاستنتاج طبيعة العلاقة الأصلية.</p></div>`,
                practice: `<div class="content-card"><p>مراجعة استنتاج العلاقات الثلاثية N-ary من الجداول ذات المفاتيح الثلاثية.</p></div>`,
                tricks: `<div class="content-card"><p>المفتاح الأجنبي المضاف لجدول النتيجة دائماً يعود لـ PK للكيان الأب.</p></div>`
            }},

            'lec11': {{
                num: '10',
                title: 'EER Exercises, Diagnostics & Bank EER Diagram',
                explain: `
                    <div class="content-card">
                        <h3>🖼️ رسومات تشخيص أخطاء الـ EER الثلاثة والتفكيك العلمي (Exercise 2)</h3>
                        
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec11_ex2a}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_lec11_ex2a}">
                            <div class="diagram-img-caption">الحالة A: صحيحة (Disjoint/Total)</div>
                        </div>
                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه الرسمة A صحيحة؟</h5>
                            <p>الرسمة تحتوي على Superclass E يتفرع منه دائرة o بتخصص كلي Total، والكيان الفرعي E2 يرتبط بعلاقة R مع الكيان E3. هذا صحيح علمياً لأن الكيانات الفرعية تحافظ على حق إقامة علاقاتها الخاصة.</p>
                        </div>

                        <div class="diagram-img-box" style="margin-top:2rem;" onclick="openLightbox('{b64_lec11_ex2b}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_lec11_ex2b}">
                            <div class="diagram-img-caption">الحالة B: صحيحة (Disjoint/Partial)</div>
                        </div>
                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه الرسمة B صحيحة؟</h5>
                            <p>التخصص d منفصل وجزئي Partial، وتوجد علاقة R بين الكيانين الفرعيين E1 و E2. هذا صحيح لأن الكيانات المستقلة تنتمي لفئات فرعية مختلفة ويمكن ارتباطها بعلاقة ثنائية R.</p>
                        </div>

                        <div class="diagram-img-box" style="margin-top:2rem;" onclick="openLightbox('{b64_lec11_ex2c}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_lec11_ex2c}">
                            <div class="diagram-img-caption">الحالة C: ❌ خاطئة تماماً</div>
                        </div>
                        <div class="diagram-reasoning-box" style="border-color:var(--accent-primary);">
                            <h5 style="color:var(--accent-primary);"><i class="fa-solid fa-triangle-exclamation"></i> ليه الرسمة C خاطئة وما هو التعديل البديل؟</h5>
                            <p><strong>سبب الخطأ:</strong> دائرة التخصص o متصلة بالكيانين E1 و E3 من الأسفل، ولكنها غير مربوطة بأي الكيان أعلى (Superclass) من الأعلى! التخصص والتعميم يقتضي وجود كائن أعلى ترث منه الفئات الفرعية.</p>
                            <p><strong>التعديل البديل الصحيح:</strong> إضافة مستطيل يمثل الـ Superclass E وربطه بأعلى دائرة الـ o.</p>
                        </div>

                        <h3 style="margin-top:2.5rem;">🖼️ رسمة BANK EER Diagram المطورة (Exercise 4)</h3>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_lec11_bank_sol}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_lec11_bank_sol}">
                            <div class="diagram-img-caption">رسمة الحل المطورة لـ BANK EER Diagram من Lecture 11 Page 9</div>
                        </div>

                        <div class="diagram-reasoning-box">
                            <h5><i class="fa-solid fa-circle-question"></i> ليه تم استخدام الكيانات الضعيفة TRANSACTION و PAYMENT؟</h5>
                            <p>لأن المعاملات والمدفوعات لا تملك رقماً فريداً عالمياً بمفردها، بل تتحدد بالاعتماد كلياً على رقم الحساب أو رقم القروض المالك لها.</p>
                        </div>
                    </div>
                `,
                summary: `<div class="content-card"><p>دوائر التخصص o أو d يجب أن ترتبط دائماً بـ Superclass من الأعلى وإلا تصبح رسمة خاطئة.</p></div>`,
                practice: `<div class="content-card"><p>مراجعة حالات الرياضات (Camper, Biker, Runner) الأربعة.</p></div>`,
                tricks: `<div class="content-card"><p>الكيانات الضعيفة TRANSACTION و PAYMENT ترتبط بعلاقات تعريفية double diamond.</p></div>`
            }},

            'lec12': {{
                num: '11',
                title: 'EER Mapping Options (8A–8D) & Query Optimization Sandbox',
                explain: `
                    <div class="content-card">
                        <h3>🖼️ الشرح التفصيلي والبدائل لخيارات الـ EER الأربعة (Options 8A–8D)</h3>

                        <h4 style="margin-top:1.5rem;">1. Option 8A — Multiple Relations: Superclass and Subclasses</h4>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_opt8a}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_opt8a}">
                            <div class="diagram-img-caption">Option 8A (عام وشامل لكافة القيود)</div>
                        </div>

                        <h4 style="margin-top:2rem;">2. Option 8B — Multiple Relations: Subclass Relations Only</h4>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_opt8b}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_opt8b}">
                            <div class="diagram-img-caption">Option 8B (يشترط Total + Disjoint فقط)</div>
                        </div>
                        <div class="diagram-reasoning-box" style="border-color:var(--accent-primary);">
                            <h5 style="color:var(--accent-primary);">🚨 شرط قاطع ومنع الاستخدام</h5>
                            <p>Option 8B <strong>تمنع منعاً باتاً</strong> إذا كان التخصص Partial أو Overlapping! يُشترط وجود قيد <strong>Total + Disjoint</strong> معاً.</p>
                        </div>

                        <h4 style="margin-top:2rem;">3. Option 8C — Single Relation with One Type Attribute</h4>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_opt8c}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_opt8c}">
                            <div class="diagram-img-caption">Option 8C (Disjoint مع صفة تمييزية واحدة)</div>
                        </div>

                        <h4 style="margin-top:2rem;">4. Option 8D — Single Relation with Multiple Type Attributes</h4>
                        <div class="diagram-img-box" onclick="openLightbox('{b64_opt8d}')">
                            <div class="diagram-zoom-overlay"><i class="fa-solid fa-magnifying-glass-plus"></i> اضغط للتكبير</div>
                            <img src="{b64_opt8d}">
                            <div class="diagram-img-caption">Option 8D (Overlapping مع أعلام بولينية)</div>
                        </div>

                        <!-- Interactive Relational Algebra Heuristic Optimizer Visual Sandbox -->
                        <div class="query-sandbox-container">
                            <div class="sandbox-header">
                                <div class="sandbox-title"><i class="fa-solid fa-microchip"></i> محاكي شجيرات استعلامات الألجبرا (Query Tree Heuristic Optimizer)</div>
                                <div class="sandbox-stepper">
                                    <button class="btn-step active" onclick="setQueryStep(1, this)">1. شجرة أولية (Unoptimized)</button>
                                    <button class="btn-step" onclick="setQueryStep(2, this)">2. تطبيق قواعد الـ Selection σ</button>
                                    <button class="btn-step" onclick="setQueryStep(3, this)">3. تطبيق قواعد الـ Projection π</button>
                                    <button class="btn-step" onclick="setQueryStep(4, this)">4. الشجرة المحسنة النهائية (Optimized Tree)</button>
                                </div>
                            </div>
                            <div class="tree-visual-display" id="queryTreeOutput">
                                π_Lname, Fname ( σ_Pnumber=10 AND Dnum=5 AND Hours>10 ( EMPLOYEE ⋈ DEPARTMENT ⋈ WORKS_ON ) )
                            </div>
                            <div style="font-size:0.9rem; color:var(--text-secondary); margin-top:1rem; text-align:right;" id="queryExplanationText">
                                💡 <strong>الشرح:</strong> هذه هي الشجرة الكارتيزية الأولية قبل التحسين، حيث يتم تنفيذ عمليات الـ Join المكلفة أولاً على كافة السجلات قبل فلترة الأسطر.
                            </div>
                        </div>
                    </div>
                `,
                summary: `<div class="content-card"><div class="callout callout-high-yield"><h5>🔥 قيد Option 8B الشديد</h5><p>Option 8B تشترط Total + Disjoint فقط!</p></div></div>`,
                practice: `<div class="content-card"><p>تطبيق خيارات التحويل 8A-8D على تمرين الموظفين والمعلمين.</p></div>`,
                tricks: `<div class="content-card"><p>Option 8C تستخدم صفة تمييزية واحدة Type Attribute بينما 8D تستخدم Boolean Flags.</p></div>`
            }},

            'exam': {{
                num: '🎓',
                title: 'الامتحان النهائي التفاعلي الشامل',
                explain: `
                    <div class="content-card">
                        <div class="quiz-card">
                            <h4>سؤال 1: أي مما يلي يُعد من خصائص الـ DBMS لتقليل التكرار وتسهيل الفهم؟</h4>
                            <div class="quiz-option" onclick="selectOpt(this, 1, false)">A. Data Inconsistency</div>
                            <div class="quiz-option" onclick="selectOpt(this, 1, true)">B. Data Abstraction <i class="fa-solid fa-check" style="display:none;"></i></div>
                            <div class="quiz-option" onclick="selectOpt(this, 1, false)">C. Program Dependency</div>
                        </div>
                        <div class="quiz-card">
                            <h4>سؤال 2: أين يوضع الـ Foreign Key في علاقات 1:N؟</h4>
                            <div class="quiz-option" onclick="selectOpt(this, 2, false)">A. في جدول الجانب 1</div>
                            <div class="quiz-option" onclick="selectOpt(this, 2, true)">B. في جدول الجانب N <i class="fa-solid fa-check" style="display:none;"></i></div>
                        </div>
                        <div class="quiz-card">
                            <h4>سؤال 3: متى يمنع استخدام الخيار Option 8B عند تحويل الـ EER؟</h4>
                            <div class="quiz-option" onclick="selectOpt(this, 3, true)">A. إذا كان التخصص Partial أو Overlapping <i class="fa-solid fa-check" style="display:none;"></i></div>
                            <div class="quiz-option" onclick="selectOpt(this, 3, false)">B. إذا كان Disjoint و Total</div>
                        </div>
                        <button class="btn-back-home" style="margin-top:1.5rem;" onclick="calcExamScore()"><i class="fa-solid fa-award"></i> اعتماد النتيجة واحتفال التقدير</button>
                    </div>
                `,
                summary: `<div class="content-card"><p>الامتحان يغطي كافة جوانب المقرر الأكاديمي.</p></div>`,
                practice: `<div class="content-card"><p>أجب عن كافة الأسئلة أعلاه للحصول على النتيجة.</p></div>`,
                tricks: `<div class="content-card"><p>راجع ملخصات المحاضرات قبل إعادة الامتحان.</p></div>`
            }}
        }};

        let activeLessonKey = 'lec1';
        let currentTab = 'tab-explain';
        let completedLessons = JSON.parse(localStorage.getItem('completedLessons') || '{{}}');

        function updateProgressBar() {{
            const total = 11;
            const count = Object.keys(completedLessons).filter(k => completedLessons[k]).length;
            const pct = Math.round((count / total) * 100);
            document.getElementById('progressPercent').innerText = pct + '%';
            document.getElementById('progressBarFill').style.width = pct + '%';
        }}
        updateProgressBar();

        function toggleLessonComplete(key, isDone) {{
            playUiSound('click');
            completedLessons[key] = isDone;
            localStorage.setItem('completedLessons', JSON.stringify(completedLessons));
            updateProgressBar();
            if (isDone) triggerConfetti();
        }}

        function showDashboardView() {{
            playUiSound('click');
            document.getElementById('dashboardView').style.display = 'block';
            document.getElementById('readerView').style.display = 'none';
            document.getElementById('edgeBackTab').style.display = 'none';
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function openLessonReader(key) {{
            playUiSound('click');
            activeLessonKey = key;
            const data = lessonsData[key] || lessonsData['lec1'];

            document.getElementById('readerBadgeNum').innerText = data.num;
            document.getElementById('readerTitleText').innerText = data.title;

            document.getElementById('explainContent').innerHTML = data.explain;
            document.getElementById('summaryContent').innerHTML = data.summary;
            document.getElementById('practiceContent').innerHTML = data.practice;
            document.getElementById('tricksContent').innerHTML = data.tricks;

            switchTab('tab-explain');

            document.getElementById('dashboardView').style.display = 'none';
            document.getElementById('readerView').style.display = 'block';
            document.getElementById('edgeBackTab').style.display = 'flex';
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function switchTab(tabId) {{
            playUiSound('click');
            currentTab = tabId;
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-panel').forEach(panel => panel.classList.remove('active'));

            const targetBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
            if (targetBtn) targetBtn.classList.add('active');

            const targetPanel = document.getElementById(tabId);
            if (targetPanel) targetPanel.classList.add('active');
        }}

        // Query Sandbox Interactive Steps
        function setQueryStep(step, btn) {{
            playUiSound('click');
            document.querySelectorAll('.btn-step').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const display = document.getElementById('queryTreeOutput');
            const exp = document.getElementById('queryExplanationText');

            if (step === 1) {{
                display.innerHTML = 'π_Lname, Fname ( σ_Pnumber=10 AND Dnum=5 AND Hours>10 ( EMPLOYEE ⋈ DEPARTMENT ⋈ WORKS_ON ) )';
                exp.innerHTML = '💡 <strong>الشرح:</strong> هذه هي الشجرة الكارتيزية الأولية قبل التحسين، حيث يتم تنفيذ عمليات الـ Join المكلفة أولاً على كافة السجلات قبل فلترة الأسطر.';
            }} else if (step === 2) {{
                display.innerHTML = 'π_Lname, Fname ( ( σ_Dnum=5(DEPARTMENT) ⋈ σ_Pnumber=10 AND Hours>10(WORKS_ON) ) ⋈ EMPLOYEE )';
                exp.innerHTML = '⚡ <strong>الشرح (Rule 1):</strong> تمت إنزال شروط الاختيار σ_Dnum=5 و σ_Pnumber=10 لأسفل الشجرة مباشرة فوق الجداول الأصلية لتقليل عدد السجلات بنسبة 90% قبل عملية الـ Join.';
            }} else if (step === 3) {{
                display.innerHTML = 'π_Lname, Fname ( π_Dnum, Mgr_ssn(σ_Dnum=5(DEPARTMENT)) ⋈ π_Pno, Essn(σ_Pnumber=10(WORKS_ON)) ⋈ π_Ssn, Lname(EMPLOYEE) )';
                exp.innerHTML = '🚀 <strong>الشرح (Rule 3):</strong> تم إنزال عمليات الإسقاط π لنطاق الأعمدة المطلوبة فقط وحذف باقي الأعمدة غير المستعملة من الأقراص.';
            }} else if (step === 4) {{
                display.innerHTML = '🏆 [OPTIMIZED QUERY TREE]: Fully Restructured with Hash Joins & Pushed Down Predicates';
                exp.innerHTML = '🎉 <strong>النتيجة النهائية:</strong> تسريع زمن تنفيذ الاستعلام من 12.4 ثانية إلى 45 مللي ثانية فقط!';
                triggerConfetti();
            }}
        }}

        // Diagram Lightbox Controls
        let currentZoom = 1;
        function openLightbox(src) {{
            playUiSound('click');
            document.getElementById('lightboxImg').src = src;
            document.getElementById('diagramModal').classList.add('active');
            currentZoom = 1;
            document.getElementById('lightboxImg').style.transform = 'scale(1)';
        }}
        function closeLightbox() {{
            playUiSound('click');
            document.getElementById('diagramModal').classList.remove('active');
        }}
        function zoomLightbox(factor) {{
            playUiSound('click');
            currentZoom *= factor;
            document.getElementById('lightboxImg').style.transform = 'scale(' + currentZoom + ')';
        }}
        function resetLightbox() {{
            playUiSound('click');
            currentZoom = 1;
            document.getElementById('lightboxImg').style.transform = 'scale(1)';
        }}

        // Theme Switcher
        const themeToggle = document.getElementById('themeToggle');
        const storedTheme = localStorage.getItem('theme') || 'dark';
        document.documentElement.setAttribute('data-theme', storedTheme);

        themeToggle.addEventListener('click', () => {{
            playUiSound('click');
            let t = document.documentElement.getAttribute('data-theme');
            let next = t === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('theme', next);
        }});

        // Global Keyboard Shortcut & Live Search
        document.addEventListener('keydown', function(e) {{
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {{
                e.preventDefault();
                document.getElementById('globalSearchInput').focus();
            }}
        }});

        document.getElementById('globalSearchInput').addEventListener('keyup', function(e) {{
            let term = e.target.value.toLowerCase();
            let cards = document.querySelectorAll('.lesson-card');
            cards.forEach(card => {{
                let txt = card.innerText.toLowerCase();
                card.style.display = txt.includes(term) ? 'flex' : 'none';
            }});
        }});

        // Quiz Engine
        let examAnswers = {{}};
        function selectOpt(el, qId, isCorrect) {{
            playUiSound('click');
            let p = el.parentElement;
            p.querySelectorAll('.quiz-option').forEach(o => o.classList.remove('selected'));
            el.classList.add('selected');
            examAnswers[qId] = isCorrect;
        }}

        function calcExamScore() {{
            let score = 0;
            if (examAnswers[1] === true) score++;
            if (examAnswers[2] === true) score++;
            if (examAnswers[3] === true) score++;

            playUiSound('win');
            triggerConfetti();
            alert('🏆 النتيجة النهائية: ' + score + ' من 3\\nالتقدير: ' + (score === 3 ? '🌟 ممتاز جداً مع مرتبة الشرف!' : '📚 مراجعة سريعة للمفاهيم'));
        }}
    </script>
</body>
</html>
"""

target = r'c:\Users\Dell\OneDrive\Desktop\DB\index.html'
with open(target, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated ultimate deep app {target}! Total size: {len(html_template)} bytes.")
