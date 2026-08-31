import os

assets_dir = r"C:\Users\ADMIN\OneDrive\Documents\readmekavi\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. header.svg - Full Cyber Animations + Anime Boy Coding
header_svg = """<svg width="850" height="240" viewBox="0 0 850 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hBg" x1="0" y1="0" x2="850" y2="240" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="50%" stop-color="#0b1411"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>

    <!-- Animated Border Gradient -->
    <linearGradient id="hBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#ef4444;#10b981;#22c55e" dur="8s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#10b981" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#ef4444">
        <animate attributeName="stop-color" values="#ef4444;#22c55e;#f43f5e;#ef4444" dur="8s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>

    <linearGradient id="nameGrad" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#86efac"/>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>

    <linearGradient id="screenGlow" x1="0" y1="0" x2="0" y2="35" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#4ade80" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#22c55e" stop-opacity="0.1"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
    
    @keyframes pulse {
      0%, 100% { opacity: 0.3; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.1); }
    }
    .pulse-dot { animation: pulse 2s infinite ease-in-out; transform-origin: 6px 6px; }

    @keyframes orbGlow {
      0%, 100% { opacity: 0.06; transform: translate(0, 0); }
      50% { opacity: 0.14; transform: translate(15px, -10px); }
    }
    .orb-1 { animation: orbGlow 6s infinite ease-in-out; }
    .orb-2 { animation: orbGlow 7s infinite ease-in-out reverse; }

    @keyframes codeFlicker {
      0%, 100% { opacity: 0.7; }
      50% { opacity: 1; }
    }
    .screen-flicker { animation: codeFlicker 1.5s infinite ease-in-out; }

    @keyframes typeHands {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-2px); }
      100% { transform: translateY(0px); }
    }
    .typing-hand { animation: typeHands 0.3s infinite ease-in-out; }

    @keyframes steamFloat {
      0% { opacity: 0; transform: translateY(0px) scale(0.8); }
      50% { opacity: 0.7; }
      100% { opacity: 0; transform: translateY(-7px) scale(1.2); }
    }
    .steam { animation: steamFloat 2.5s infinite linear; }
  </style>

  <!-- Outer Card Frame -->
  <rect x="1" y="1" width="848" height="238" rx="16" fill="url(#hBg)"/>
  <rect x="1" y="1" width="848" height="238" rx="16" stroke="url(#hBorder)" stroke-width="1.8"/>

  <!-- Glowing Orbs -->
  <circle cx="120" cy="60" r="110" fill="#22c55e" class="orb-1" filter="blur(40px)"/>
  <circle cx="750" cy="180" r="120" fill="#ef4444" class="orb-2" filter="blur(40px)"/>

  <!-- Top Status Bar -->
  <g transform="translate(35, 28)">
    <circle cx="6" cy="6" r="5" fill="#22c55e" class="pulse-dot"/>
    <circle cx="6" cy="6" r="8" stroke="#22c55e" stroke-width="1" opacity="0.4"/>
    <text x="22" y="10" fill="#4ade80" font-size="12" font-weight="600" class="font-mono" letter-spacing="1">SYSTEM ACTIVE // OPEN TO OPPORTUNITIES</text>
  </g>

  <!-- Portfolio Badge -->
  <g transform="translate(640, 24)">
    <rect x="0" y="0" width="175" height="26" rx="13" fill="#131e17" stroke="#22c55e" stroke-width="1" stroke-opacity="0.8"/>
    <circle cx="15" cy="13" r="3.5" fill="#22c55e" class="pulse-dot"/>
    <text x="30" y="17" fill="#86efac" font-size="11.5" font-weight="700" class="font-mono">🌐 developerkavi.in</text>
  </g>

  <!-- Avatar Container (Anime Boy Coding in front of Laptop) -->
  <g transform="translate(35, 66)">
    <rect x="0" y="0" width="92" height="92" rx="18" fill="#08100c" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="92" height="92" rx="18" stroke="#ef4444" stroke-width="1" stroke-dasharray="6 4" opacity="0.5"/>

    <g transform="translate(2, 6)">
      <!-- Ambient Screen Ray -->
      <polygon points="18,65 70,65 62,38 26,38" fill="url(#screenGlow)" class="screen-flicker"/>

      <!-- Body / Hoodie -->
      <path d="M22 68 C22 55, 30 50, 44 50 C58 50, 66 55, 66 68 Z" fill="#1e293b"/>
      <path d="M40 50 L44 58 L48 50" stroke="#ef4444" stroke-width="1.5" fill="none"/>
      
      <!-- Head / Face -->
      <circle cx="44" cy="34" r="14" fill="#fed7aa"/>
      
      <!-- Cyber Neon Glasses / HUD -->
      <rect x="35" y="31" width="8" height="5" rx="1.5" fill="#064e3b" stroke="#22c55e" stroke-width="1"/>
      <rect x="45" y="31" width="8" height="5" rx="1.5" fill="#064e3b" stroke="#22c55e" stroke-width="1"/>
      <line x1="43" y1="33" x2="45" y2="33" stroke="#22c55e" stroke-width="1"/>

      <!-- Anime Spiky Hair -->
      <path d="M28 32 C28 20, 36 14, 44 14 C52 14, 60 20, 60 32 C58 26, 52 22, 44 22 C36 22, 30 26, 28 32 Z" fill="#1e1b4b"/>
      <path d="M30 26 L24 20 L33 21 Z" fill="#1e1b4b"/>
      <path d="M36 18 L32 10 L41 15 Z" fill="#312e81"/>
      <path d="M44 15 L46 8 L50 16 Z" fill="#1e1b4b"/>
      <path d="M52 18 L58 11 L54 22 Z" fill="#312e81"/>
      <path d="M58 25 L64 22 L58 30 Z" fill="#1e1b4b"/>
      <path d="M32 10 L41 15 L46 8 L50 16 L58 11" stroke="#ef4444" stroke-width="0.8" fill="none" opacity="0.8"/>

      <!-- Cyber Neon Headphones -->
      <path d="M27 34 C27 23, 61 23, 61 34" stroke="#ef4444" stroke-width="2.5" fill="none"/>
      <rect x="25" y="30" width="4" height="10" rx="2" fill="#0f172a" stroke="#22c55e" stroke-width="1.2"/>
      <rect x="59" y="30" width="4" height="10" rx="2" fill="#0f172a" stroke="#22c55e" stroke-width="1.2"/>

      <!-- Typing Arms -->
      <g class="typing-hand">
        <path d="M25 62 Q 33 60, 37 63" stroke="#fed7aa" stroke-width="3.5" stroke-linecap="round"/>
        <path d="M63 62 Q 55 60, 51 63" stroke="#fed7aa" stroke-width="3.5" stroke-linecap="round"/>
      </g>

      <!-- Laptop Base -->
      <path d="M22 66 L66 66 L62 70 L26 70 Z" fill="#334155" stroke="#475569" stroke-width="0.8"/>
      <line x1="28" y1="67" x2="60" y2="67" stroke="#22c55e" stroke-width="1" opacity="0.8"/>

      <!-- Laptop Screen -->
      <rect x="29" y="44" width="30" height="20" rx="2" fill="#031f13" stroke="#22c55e" stroke-width="1.2" class="screen-flicker"/>
      <line x1="32" y1="48" x2="48" y2="48" stroke="#4ade80" stroke-width="1"/>
      <line x1="32" y1="52" x2="55" y2="52" stroke="#22c55e" stroke-width="1"/>
      <line x1="32" y1="56" x2="44" y2="56" stroke="#ef4444" stroke-width="1"/>
      <line x1="32" y1="60" x2="52" y2="60" stroke="#86efac" stroke-width="1"/>

      <!-- Steaming Mug -->
      <rect x="69" y="63" width="7" height="7" rx="1.5" fill="#ef4444"/>
      <path d="M76 65 Q 78 66.5, 76 68" stroke="#ef4444" stroke-width="0.8" fill="none"/>
      <path d="M72 61 Q 70 59, 72 57" stroke="#ffffff" stroke-width="0.7" fill="none" class="steam"/>
    </g>
  </g>

  <!-- Name & Professional Title -->
  <g transform="translate(148, 75)">
    <text x="0" y="16" fill="#f87171" font-size="13" font-weight="700" letter-spacing="2" class="font-mono">HELLO WORLD, I AM</text>
    <text x="0" y="52" fill="url(#nameGrad)" font-size="36" font-weight="900" class="font-sans" letter-spacing="-0.5">KAVIYARASAN M</text>
    <text x="0" y="76" fill="#94a3b8" font-size="14" font-weight="500" class="font-sans">
      Full Stack Software Engineer &amp; Web Architect
    </text>
  </g>

  <!-- Bottom Badges -->
  <g transform="translate(35, 178)">
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="180" height="36" rx="8" fill="#0c1611" stroke="#1b3826" stroke-width="1"/>
      <text x="14" y="22" fill="#86efac" font-size="11" font-weight="600" class="font-mono">EXP:</text>
      <text x="45" y="22" fill="#f8fafc" font-size="11" font-weight="700" class="font-mono">FULL STACK DEV</text>
    </g>

    <g transform="translate(195, 0)">
      <rect x="0" y="0" width="220" height="36" rx="8" fill="#180c0e" stroke="#3d1519" stroke-width="1"/>
      <text x="14" y="22" fill="#f87171" font-size="11" font-weight="600" class="font-mono">CORE:</text>
      <text x="56" y="22" fill="#fca5a5" font-size="11" font-weight="700" class="font-mono">PHP • REACT • LARAVEL</text>
    </g>

    <g transform="translate(430, 0)">
      <rect x="0" y="0" width="190" height="36" rx="8" fill="#0c1611" stroke="#1b3826" stroke-width="1"/>
      <text x="14" y="22" fill="#86efac" font-size="11" font-weight="600" class="font-mono">FOCUS:</text>
      <text x="65" y="22" fill="#4ade80" font-size="11" font-weight="700" class="font-mono">CLEAN &amp; SCALE</text>
    </g>

    <g transform="translate(635, 0)">
      <rect x="0" y="0" width="145" height="36" rx="8" fill="#064e3b" stroke="#059669" stroke-width="1"/>
      <circle cx="16" cy="18" r="4" fill="#34d399" class="pulse-dot"/>
      <text x="28" y="22" fill="#a7f3d0" font-size="11" font-weight="700" class="font-mono">READY TO BUILD</text>
    </g>
  </g>
</svg>"""

# 2. featured-repos.svg - FIXED OVERFLOW WITH MULTILINE TSPANS & ANIMATED GRADIENT BORDERS
featured_repos_svg = """<svg width="850" height="350" viewBox="0 0 850 350" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="repoBg" x1="0" y1="0" x2="850" y2="350" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#120a0c"/>
    </linearGradient>
    <linearGradient id="repoBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#ef4444;#22c55e" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#ef4444">
        <animate attributeName="stop-color" values="#ef4444;#22c55e;#ef4444" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
    
    @keyframes glowPulse {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }
    .pulse-indicator { animation: glowPulse 2s infinite ease-in-out; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="348" rx="16" fill="url(#repoBg)"/>
  <rect x="1" y="1" width="848" height="348" rx="16" stroke="url(#repoBorder)" stroke-width="1.6"/>

  <!-- Title Header -->
  <g transform="translate(35, 36)">
    <circle cx="6" cy="6" r="6" fill="#ef4444" class="pulse-indicator"/>
    <text x="22" y="10" fill="#f8fafc" font-size="15" font-weight="800" class="font-sans">FEATURED PRODUCTION ARCHITECTURES</text>
    <text x="780" y="10" fill="#4ade80" font-size="12" font-weight="600" text-anchor="end" class="font-mono">developerkavi.in // CODEBASE</text>
  </g>

  <!-- 3 Project Cards - Perfectly sized with No Text Overflow -->
  <!-- Card 1 -->
  <g transform="translate(35, 68)">
    <rect width="245" height="250" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.3"/>
    <circle cx="25" cy="28" r="10" fill="#052e16"/>
    <text x="25" y="32" fill="#4ade80" font-size="12" text-anchor="middle" class="font-mono">📦</text>
    <text x="45" y="32" fill="#f8fafc" font-size="14.5" font-weight="700" class="font-sans">developerkavi-portal</text>
    
    <!-- Clean wrapped description -->
    <text x="20" y="66" fill="#94a3b8" font-size="11.5" class="font-sans">
      <tspan x="20" dy="0">Production web portfolio</tspan>
      <tspan x="20" dy="16">ecosystem with automated</tspan>
      <tspan x="20" dy="16">CI/CD pipeline &amp; Coolify.</tspan>
    </text>
    
    <g transform="translate(20, 160)">
      <rect width="90" height="22" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="45" y="15" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">COOLIFY</text>
    </g>
    <g transform="translate(120, 160)">
      <rect width="85" height="22" rx="6" fill="#1f2937"/>
      <text x="42" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">UBUNTU</text>
    </g>

    <g transform="translate(20, 215)">
      <circle cx="6" cy="6" r="4" fill="#22c55e" class="pulse-indicator"/>
      <text x="18" y="10" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">LIVE // STABLE</text>
    </g>
  </g>

  <!-- Card 2 -->
  <g transform="translate(300, 68)">
    <rect width="245" height="250" rx="12" fill="#180d0f" stroke="#ef4444" stroke-width="1.3"/>
    <circle cx="25" cy="28" r="10" fill="#450a0a"/>
    <text x="25" y="32" fill="#f87171" font-size="12" text-anchor="middle" class="font-mono">⚛️</text>
    <text x="45" y="32" fill="#f8fafc" font-size="14.5" font-weight="700" class="font-sans">vps-db-verifier</text>
    
    <!-- Clean wrapped description -->
    <text x="20" y="66" fill="#94a3b8" font-size="11.5" class="font-sans">
      <tspan x="20" dy="0">Automated MySQL schema</tspan>
      <tspan x="20" dy="16">validator, column tester &amp;</tspan>
      <tspan x="20" dy="16">migration checker tool.</tspan>
    </text>
    
    <g transform="translate(20, 160)">
      <rect width="90" height="22" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="45" y="15" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">LARAVEL</text>
    </g>
    <g transform="translate(120, 160)">
      <rect width="85" height="22" rx="6" fill="#1f2937"/>
      <text x="42" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">MYSQL</text>
    </g>

    <g transform="translate(20, 215)">
      <circle cx="6" cy="6" r="4" fill="#ef4444" class="pulse-indicator"/>
      <text x="18" y="10" fill="#f87171" font-size="11" font-weight="600" class="font-mono">CI/CD // ACTIVE</text>
    </g>
  </g>

  <!-- Card 3 -->
  <g transform="translate(565, 68)">
    <rect width="245" height="250" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.3"/>
    <circle cx="25" cy="28" r="10" fill="#052e16"/>
    <text x="25" y="32" fill="#4ade80" font-size="12" text-anchor="middle" class="font-mono">⚡</text>
    <text x="45" y="32" fill="#f8fafc" font-size="14.5" font-weight="700" class="font-sans">docker-pipeline-hub</text>
    
    <!-- Clean wrapped description -->
    <text x="20" y="66" fill="#94a3b8" font-size="11.5" class="font-sans">
      <tspan x="20" dy="0">Multi-container Docker</tspan>
      <tspan x="20" dy="16">pipeline with Jenkins CI</tspan>
      <tspan x="20" dy="16">&amp; Linux CLI tooling.</tspan>
    </text>
    
    <g transform="translate(20, 160)">
      <rect width="90" height="22" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="45" y="15" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">DOCKER</text>
    </g>
    <g transform="translate(120, 160)">
      <rect width="85" height="22" rx="6" fill="#1f2937"/>
      <text x="42" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">JENKINS</text>
    </g>

    <g transform="translate(20, 215)">
      <circle cx="6" cy="6" r="4" fill="#22c55e" class="pulse-indicator"/>
      <text x="18" y="10" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">ONLINE</text>
    </g>
  </g>
</svg>"""

# 3. repo-deploymentmethod.svg - Animated Pinned Repo Card
repo_deploy_svg = """<svg width="415" height="135" viewBox="0 0 415 135" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="depBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#10b981;#22c55e" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#16a34a"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
  </style>
  <rect width="415" height="135" rx="12" fill="#060c09" stroke="url(#depBorder)" stroke-width="1.4"/>
  
  <g transform="translate(20, 28)">
    <text x="0" y="0" font-size="14">📦</text>
    <text x="24" y="0" fill="#4ade80" font-size="15" font-weight="700" class="font-sans">deploymentmethod</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="0.8"/>
    <text x="342" y="0" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <text x="20" y="58" fill="#94a3b8" font-size="11.5" class="font-sans">
    <tspan x="20" dy="0">Automated production deployment, Docker scripts &amp;</tspan>
    <tspan x="20" dy="16">VPS infrastructure configuration.</tspan>
  </text>

  <g transform="translate(20, 108)">
    <circle cx="5" cy="5" r="4" fill="#22c55e"/>
    <text x="16" y="9" fill="#86efac" font-size="11" class="font-mono">Docker / Shell</text>

    <text x="170" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="230" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

# 4. repo-kaviyarasan033.svg - Animated Pinned Profile Repo Card
repo_profile_svg = """<svg width="415" height="135" viewBox="0 0 415 135" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="kaviBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444">
        <animate attributeName="stop-color" values="#ef4444;#f87171;#ef4444" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
  </style>
  <rect width="415" height="135" rx="12" fill="#080c0a" stroke="url(#kaviBorder)" stroke-width="1.4"/>
  
  <g transform="translate(20, 28)">
    <text x="0" y="0" font-size="14">⚡</text>
    <text x="24" y="0" fill="#f87171" font-size="15" font-weight="700" class="font-sans">kaviyarasan033</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="0.8"/>
    <text x="342" y="0" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <text x="20" y="58" fill="#94a3b8" font-size="11.5" class="font-sans">
    <tspan x="20" dy="0">Special GitHub Profile Hub, native vector telemetry</tspan>
    <tspan x="20" dy="16">cards &amp; automated contribution snake pipeline.</tspan>
  </text>

  <g transform="translate(20, 108)">
    <circle cx="5" cy="5" r="4" fill="#3572A5"/>
    <text x="16" y="9" fill="#93c5fd" font-size="11" class="font-mono">Python / SVG</text>

    <text x="170" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="230" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

# 5. github-stats.svg - Animated Stats Card
github_stats_svg = """<svg width="415" height="195" viewBox="0 0 415 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="statBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#10b981;#22c55e" dur="5s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
    @keyframes pulse { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
    .pulse { animation: pulse 2s infinite ease-in-out; }
  </style>

  <rect width="415" height="195" rx="12" fill="#060c09" stroke="url(#statBorder)" stroke-width="1.4"/>
  
  <text x="25" y="32" fill="#4ade80" font-size="14" font-weight="700" class="font-sans">⚡ Kaviyarasan's GitHub Telemetry</text>
  <line x1="25" y1="42" x2="390" y2="42" stroke="#1b3826" stroke-width="1"/>

  <g transform="translate(25, 65)">
    <g transform="translate(0, 0)">
      <circle cx="10" cy="10" r="8" fill="#052e16"/>
      <text x="10" y="14" fill="#4ade80" font-size="10" text-anchor="middle">★</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Total Stars Earned:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">2 ★</text>
    </g>

    <g transform="translate(0, 28)">
      <circle cx="10" cy="10" r="8" fill="#450a0a"/>
      <text x="10" y="14" fill="#ef4444" font-size="10" text-anchor="middle">⚡</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Total Contributions:</text>
      <text x="365" y="14" fill="#4ade80" font-size="12" font-weight="800" text-anchor="end" class="font-mono">459+ (2026)</text>
    </g>

    <g transform="translate(0, 56)">
      <circle cx="10" cy="10" r="8" fill="#052e16"/>
      <text x="10" y="14" fill="#4ade80" font-size="10" text-anchor="middle">⌥</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Pull Requests &amp; Merges:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">98.5% Rate</text>
    </g>

    <g transform="translate(0, 84)">
      <circle cx="10" cy="10" r="8" fill="#450a0a"/>
      <text x="10" y="14" fill="#ef4444" font-size="10" text-anchor="middle">📦</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Production Repositories:</text>
      <text x="365" y="14" fill="#86efac" font-size="12" font-weight="700" text-anchor="end" class="font-mono">All Systems Online</text>
    </g>
  </g>
</svg>"""

# 6. github-streak.svg - Animated Streak Card
github_streak_svg = """<svg width="415" height="195" viewBox="0 0 415 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="fireBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444">
        <animate attributeName="stop-color" values="#ef4444;#dc2626;#ef4444" dur="3s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
    
    @keyframes fireGlow {
      0%, 100% { transform: scale(1); filter: drop-shadow(0 0 4px #ef4444); }
      50% { transform: scale(1.1); filter: drop-shadow(0 0 10px #ef4444); }
    }
    .fire-pulse { animation: fireGlow 1.8s infinite ease-in-out; transform-origin: 0 0; }
  </style>

  <rect width="415" height="195" rx="12" fill="#080c0a" stroke="url(#fireBorder)" stroke-width="1.4"/>

  <!-- Center Circle Streak Icon -->
  <g transform="translate(207, 45)">
    <circle cx="0" cy="0" r="24" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <text x="0" y="7" font-size="18" text-anchor="middle" class="fire-pulse">🔥</text>
  </g>

  <!-- 3 Streak Columns -->
  <g transform="translate(75, 115)">
    <text x="0" y="0" fill="#f8fafc" font-size="22" font-weight="800" text-anchor="middle" class="font-sans">459</text>
    <text x="0" y="18" fill="#f87171" font-size="11" font-weight="600" text-anchor="middle" class="font-mono">Total Commits</text>
    <text x="0" y="32" fill="#64748b" font-size="9" text-anchor="middle" class="font-mono">2026 Cycle</text>
  </g>

  <g transform="translate(207, 115)">
    <text x="0" y="0" fill="#22c55e" font-size="24" font-weight="900" text-anchor="middle" class="font-sans">ACTIVE</text>
    <text x="0" y="18" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle" class="font-mono">Current Streak</text>
    <text x="0" y="32" fill="#86efac" font-size="9" text-anchor="middle" class="font-mono">Daily Consistency</text>
  </g>

  <g transform="translate(340, 115)">
    <text x="0" y="0" fill="#f8fafc" font-size="22" font-weight="800" text-anchor="middle" class="font-sans">99.8%</text>
    <text x="0" y="18" fill="#f87171" font-size="11" font-weight="600" text-anchor="middle" class="font-mono">Success Rate</text>
    <text x="0" y="32" fill="#64748b" font-size="9" text-anchor="middle" class="font-mono">Deployment SLA</text>
  </g>
</svg>"""

# 7. top-languages.svg - Animated Shimmer Languages Bar
top_languages_svg = """<svg width="850" height="150" viewBox="0 0 850 150" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="langBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#ef4444;#22c55e" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>

  <rect width="850" height="150" rx="14" fill="#060c09" stroke="url(#langBorder)" stroke-width="1.4"/>

  <g transform="translate(35, 30)">
    <circle cx="6" cy="6" r="5" fill="#22c55e"/>
    <text x="20" y="10" fill="#f8fafc" font-size="14" font-weight="700" class="font-sans">Most Used Languages &amp; Stacks across All Repositories</text>
  </g>

  <g transform="translate(35, 55)">
    <rect x="0" y="0" width="312" height="10" rx="5" fill="#4f5d95"/>
    <rect x="316" y="0" width="195" height="10" rx="5" fill="#f1e05a"/>
    <rect x="515" y="0" width="117" height="10" rx="5" fill="#3572A5"/>
    <rect x="636" y="0" width="78" height="10" rx="5" fill="#89e051"/>
    <rect x="718" y="0" width="62" height="10" rx="5" fill="#e34c26"/>
  </g>

  <g transform="translate(35, 90)">
    <g transform="translate(0, 0)">
      <circle cx="6" cy="6" r="5" fill="#4f5d95"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">PHP <tspan fill="#94a3b8">40.2%</tspan></text>
    </g>

    <g transform="translate(155, 0)">
      <circle cx="6" cy="6" r="5" fill="#f1e05a"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">JavaScript <tspan fill="#94a3b8">25.0%</tspan></text>
    </g>

    <g transform="translate(325, 0)">
      <circle cx="6" cy="6" r="5" fill="#3572A5"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">Python <tspan fill="#94a3b8">15.4%</tspan></text>
    </g>

    <g transform="translate(485, 0)">
      <circle cx="6" cy="6" r="5" fill="#89e051"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">Shell / Bash <tspan fill="#94a3b8">10.6%</tspan></text>
    </g>

    <g transform="translate(650, 0)">
      <circle cx="6" cy="6" r="5" fill="#e34c26"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">HTML/CSS <tspan fill="#94a3b8">8.8%</tspan></text>
    </g>
  </g>
</svg>"""

all_svgs = {
    "header.svg": header_svg,
    "featured-repos.svg": featured_repos_svg,
    "repo-deploymentmethod.svg": repo_deploy_svg,
    "repo-kaviyarasan033.svg": repo_profile_svg,
    "github-stats.svg": github_stats_svg,
    "github-streak.svg": github_streak_svg,
    "top-languages.svg": top_languages_svg,
}

for name, code in all_svgs.items():
    p = os.path.join(assets_dir, name)
    with open(p, "w", encoding="utf-8") as f:
        f.write(code.strip())
    print(f"Updated {name}")

print("All animated SVGs successfully generated with NO text overflow!")
