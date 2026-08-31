import os

assets_dir = r"C:\Users\ADMIN\OneDrive\Documents\readmekavi\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. header.svg - with Animated Anime Boy Coding in front of Laptop & developerkavi.in
header_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="240" viewBox="0 0 850 240" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="headerBg" x1="0" y1="0" x2="850" y2="240" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="50%" stop-color="#0b1411"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>

    <!-- Border Gradient -->
    <linearGradient id="headerBorder" x1="0" y1="0" x2="850" y2="240" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.9"/>
      <stop offset="50%" stop-color="#10b981" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.9"/>
    </linearGradient>

    <!-- Name Text Gradient -->
    <linearGradient id="nameGradient" x1="0" y1="0" x2="450" y2="0" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#86efac"/>
      <stop offset="100%" stop-color="#22c55e"/>
    </linearGradient>

    <!-- Laptop Screen Glow -->
    <linearGradient id="screenGlow" x1="0" y1="0" x2="0" y2="35" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#4ade80" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#22c55e" stop-opacity="0.1"/>
    </linearGradient>
    
    <linearGradient id="hoodieGrad" x1="0" y1="0" x2="60" y2="60" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
    
    .pulse { animation: pulseGlow 2.5s ease-in-out infinite; }
    @keyframes pulseGlow {
      0%, 100% { opacity: 0.4; }
      50% { opacity: 1; }
    }

    /* Anime Dev Coding Animations */
    .screen-flicker {
      animation: codeFlicker 1.8s ease-in-out infinite alternate;
    }
    @keyframes codeFlicker {
      0% { opacity: 0.75; }
      50% { opacity: 0.95; }
      100% { opacity: 0.8; }
    }

    .hand-type-left {
      animation: typeLeft 0.25s ease-in-out infinite alternate;
      transform-origin: 28px 65px;
    }
    .hand-type-right {
      animation: typeRight 0.28s ease-in-out infinite alternate;
      transform-origin: 58px 65px;
    }
    @keyframes typeLeft {
      0% { transform: translateY(0px); }
      100% { transform: translateY(-2px); }
    }
    @keyframes typeRight {
      0% { transform: translateY(-1.5px); }
      100% { transform: translateY(1px); }
    }
    
    .steam-float {
      animation: steamAnim 3s ease-out infinite;
    }
    @keyframes steamAnim {
      0% { opacity: 0; transform: translateY(0px) scale(0.8); }
      50% { opacity: 0.6; }
      100% { opacity: 0; transform: translateY(-8px) scale(1.2); }
    }
  </style>

  <!-- Outer Card Background -->
  <rect x="1" y="1" width="848" height="238" rx="16" fill="url(#headerBg)"/>
  <rect x="1" y="1" width="848" height="238" rx="16" stroke="url(#headerBorder)" stroke-width="1.5"/>

  <!-- Decorative Cyber Orbs -->
  <circle cx="120" cy="60" r="100" fill="#22c55e" opacity="0.08" filter="blur(40px)"/>
  <circle cx="750" cy="180" r="110" fill="#ef4444" opacity="0.08" filter="blur(40px)"/>

  <!-- Top Status Bar -->
  <g transform="translate(35, 28)">
    <circle cx="6" cy="6" r="5" fill="#22c55e" class="pulse"/>
    <circle cx="6" cy="6" r="8" stroke="#22c55e" stroke-width="1" opacity="0.4"/>
    <text x="22" y="10" fill="#4ade80" font-size="12" font-weight="600" class="font-mono" letter-spacing="1">SYSTEM ACTIVE // OPEN TO OPPORTUNITIES</text>
  </g>

  <!-- Portfolio Website Badge (Right aligned: developerkavi.in) -->
  <g transform="translate(640, 24)">
    <rect x="0" y="0" width="175" height="26" rx="13" fill="#131e17" stroke="#22c55e" stroke-width="1" stroke-opacity="0.6"/>
    <circle cx="15" cy="13" r="3.5" fill="#22c55e"/>
    <text x="30" y="17" fill="#86efac" font-size="11.5" font-weight="700" class="font-mono">🌐 developerkavi.in</text>
  </g>

  <!-- Main Identity Content -->
  <!-- Anime Boy Coding in front of Laptop (Vector Animation Avatar Box) -->
  <g transform="translate(35, 66)">
    <!-- Avatar Box Container -->
    <rect x="0" y="0" width="92" height="92" rx="18" fill="#08100c" stroke="#22c55e" stroke-width="1.5"/>
    <rect x="0" y="0" width="92" height="92" rx="18" stroke="#ef4444" stroke-width="1" stroke-dasharray="8 4" opacity="0.4"/>

    <!-- Anime Boy & Laptop Illustration -->
    <!-- Head & Hair Shadow -->
    <g transform="translate(2, 6)">
      <!-- Background Ambient Screen Ray -->
      <polygon points="18,65 70,65 62,38 26,38" fill="url(#screenGlow)" class="screen-flicker"/>

      <!-- Body / Hoodie -->
      <path d="M22 68 C22 55, 30 50, 44 50 C58 50, 66 55, 66 68 Z" fill="url(#hoodieGrad)"/>
      <path d="M40 50 L44 58 L48 50" stroke="#ef4444" stroke-width="1.5" fill="none"/>
      
      <!-- Head / Face -->
      <circle cx="44" cy="34" r="14" fill="#fed7aa"/>
      
      <!-- Cyber Neon Glasses / HUD -->
      <rect x="35" y="31" width="8" height="5" rx="1.5" fill="#064e3b" stroke="#22c55e" stroke-width="1"/>
      <rect x="45" y="31" width="8" height="5" rx="1.5" fill="#064e3b" stroke="#22c55e" stroke-width="1"/>
      <line x1="43" y1="33" x2="45" y2="33" stroke="#22c55e" stroke-width="1"/>

      <!-- Anime Spiky Hair -->
      <path d="M28 32 C28 20, 36 14, 44 14 C52 14, 60 20, 60 32 C58 26, 52 22, 44 22 C36 22, 30 26, 28 32 Z" fill="#1e1b4b"/>
      <!-- Hair spikes -->
      <path d="M30 26 L24 20 L33 21 Z" fill="#1e1b4b"/>
      <path d="M36 18 L32 10 L41 15 Z" fill="#312e81"/>
      <path d="M44 15 L46 8 L50 16 Z" fill="#1e1b4b"/>
      <path d="M52 18 L58 11 L54 22 Z" fill="#312e81"/>
      <path d="M58 25 L64 22 L58 30 Z" fill="#1e1b4b"/>
      <!-- Neon Red Rim Highlight on Hair -->
      <path d="M32 10 L41 15 L46 8 L50 16 L58 11" stroke="#ef4444" stroke-width="0.8" fill="none" opacity="0.8"/>

      <!-- Cyber Neon Headphones -->
      <path d="M27 34 C27 23, 61 23, 61 34" stroke="#ef4444" stroke-width="2.5" fill="none"/>
      <!-- Left Earcup with glowing Green Ring -->
      <rect x="25" y="30" width="4" height="10" rx="2" fill="#0f172a" stroke="#22c55e" stroke-width="1.2"/>
      <!-- Right Earcup with glowing Green Ring -->
      <rect x="59" y="30" width="4" height="10" rx="2" fill="#0f172a" stroke="#22c55e" stroke-width="1.2"/>

      <!-- Typing Arms / Hands (Animated) -->
      <g class="hand-type-left">
        <path d="M25 62 Q 33 60, 37 63" stroke="#fed7aa" stroke-width="3.5" stroke-linecap="round"/>
      </g>
      <g class="hand-type-right">
        <path d="M63 62 Q 55 60, 51 63" stroke="#fed7aa" stroke-width="3.5" stroke-linecap="round"/>
      </g>

      <!-- Laptop Base -->
      <path d="M22 66 L66 66 L62 70 L26 70 Z" fill="#334155" stroke="#475569" stroke-width="0.8"/>
      <!-- Glowing Keyboard Base -->
      <line x1="28" y1="67" x2="60" y2="67" stroke="#22c55e" stroke-width="1" opacity="0.8"/>

      <!-- Laptop Screen (Open Facing Boy) -->
      <rect x="29" y="44" width="30" height="20" rx="2" fill="#031f13" stroke="#22c55e" stroke-width="1.2" class="screen-flicker"/>
      <!-- Mini Terminal Lines on Screen -->
      <line x1="32" y1="48" x2="48" y2="48" stroke="#4ade80" stroke-width="1"/>
      <line x1="32" y1="52" x2="55" y2="52" stroke="#22c55e" stroke-width="1"/>
      <line x1="32" y1="56" x2="44" y2="56" stroke="#ef4444" stroke-width="1"/>
      <line x1="32" y1="60" x2="52" y2="60" stroke="#86efac" stroke-width="1"/>

      <!-- Mini Coffee Mug on Desk with Steam -->
      <rect x="69" y="63" width="7" height="7" rx="1.5" fill="#ef4444"/>
      <path d="M76 65 Q 78 66.5, 76 68" stroke="#ef4444" stroke-width="0.8" fill="none"/>
      <path d="M72 61 Q 70 59, 72 57" stroke="#ffffff" stroke-width="0.7" fill="none" class="steam-float"/>
    </g>
  </g>

  <!-- Name & Professional Title -->
  <g transform="translate(148, 75)">
    <!-- Sub-greeting -->
    <text x="0" y="16" fill="#f87171" font-size="13" font-weight="700" letter-spacing="2" class="font-mono">HELLO WORLD, I AM</text>
    
    <!-- Primary Name -->
    <text x="0" y="52" fill="url(#nameGradient)" font-size="36" font-weight="900" class="font-sans" letter-spacing="-0.5">KAVIYARASAN M</text>
    
    <!-- Title / Subtitle -->
    <text x="0" y="76" fill="#94a3b8" font-size="14" font-weight="500" class="font-sans">
      Full Stack Software Engineer &amp; Web Architect
    </text>
  </g>

  <!-- Bottom Interactive / Stats Metrics Bar -->
  <g transform="translate(35, 178)">
    <!-- Metric 1: Experience / Focus -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="180" height="36" rx="8" fill="#0c1611" stroke="#1b3826" stroke-width="1"/>
      <text x="14" y="22" fill="#86efac" font-size="11" font-weight="600" class="font-mono">EXP:</text>
      <text x="45" y="22" fill="#f8fafc" font-size="11" font-weight="700" class="font-mono">FULL STACK DEV</text>
    </g>

    <!-- Metric 2: Core Stack -->
    <g transform="translate(195, 0)">
      <rect x="0" y="0" width="220" height="36" rx="8" fill="#180c0e" stroke="#3d1519" stroke-width="1"/>
      <text x="14" y="22" fill="#f87171" font-size="11" font-weight="600" class="font-mono">CORE:</text>
      <text x="56" y="22" fill="#fca5a5" font-size="11" font-weight="700" class="font-mono">PHP • REACT • LARAVEL</text>
    </g>

    <!-- Metric 3: Architecture -->
    <g transform="translate(430, 0)">
      <rect x="0" y="0" width="190" height="36" rx="8" fill="#0c1611" stroke="#1b3826" stroke-width="1"/>
      <text x="14" y="22" fill="#86efac" font-size="11" font-weight="600" class="font-mono">FOCUS:</text>
      <text x="65" y="22" fill="#4ade80" font-size="11" font-weight="700" class="font-mono">CLEAN &amp; SCALE</text>
    </g>

    <!-- Metric 4: Status -->
    <g transform="translate(635, 0)">
      <rect x="0" y="0" width="145" height="36" rx="8" fill="#064e3b" stroke="#059669" stroke-width="1"/>
      <circle cx="16" cy="18" r="4" fill="#34d399"/>
      <text x="28" y="22" fill="#a7f3d0" font-size="11" font-weight="700" class="font-mono">READY TO BUILD</text>
    </g>
  </g>
</svg>
"""

# 2. typing.svg - Dynamic Bash & CI/CD Pipeline Typing Animation
typing_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="60" viewBox="0 0 850 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
    
    @keyframes blink {
      0%, 100% { opacity: 1; }
      50% { opacity: 0; }
    }
    .cursor {
      animation: blink 0.9s infinite;
      fill: #ef4444;
    }
  </style>

  <!-- Background Bar -->
  <rect x="1" y="1" width="848" height="58" rx="12" fill="#080e0b" stroke="#166534" stroke-width="1"/>

  <!-- Terminal Prompt -->
  <g transform="translate(25, 35)">
    <text x="0" y="0" fill="#22c55e" font-size="13.5" font-weight="700" class="font-mono">kaviyarasan@vps:~$</text>
    
    <!-- Code Command / Subtitle -->
    <text x="175" y="0" fill="#f8fafc" font-size="13" font-weight="500" class="font-mono">
      <tspan fill="#ef4444">docker-compose</tspan> up -d &amp;&amp; <tspan fill="#4ade80">coolify</tspan> deploy --prod &amp;&amp; <tspan fill="#fca5a5">./verify-db-schema.sh</tspan>
    </text>
    
    <!-- Glowing Red Terminal Cursor -->
    <rect x="790" y="-12" width="8" height="15" class="cursor"/>
  </g>
</svg>
"""

# 3. about.svg - Terminal Bash Card with VPS Infrastructure & Deployment Logs
about_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="400" viewBox="0 0 850 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="cardBg" x1="0" y1="0" x2="850" y2="400" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#070c09"/>
      <stop offset="100%" stop-color="#0e1712"/>
    </linearGradient>
    <linearGradient id="aboutBorder" x1="0" y1="0" x2="850" y2="400" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.7"/>
    </linearGradient>
  </defs>

  <style>
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
    .key { fill: #f87171; font-weight: 600; }
    .val { fill: #4ade80; }
    .str { fill: #86efac; }
    .pun { fill: #94a3b8; }
    .cmd { fill: #f8fafc; font-weight: 600; }
  </style>

  <!-- Terminal Window Frame -->
  <rect x="1" y="1" width="848" height="398" rx="14" fill="url(#cardBg)"/>
  <rect x="1" y="1" width="848" height="398" rx="14" stroke="url(#aboutBorder)" stroke-width="1.5"/>

  <!-- Window Header Bar -->
  <rect x="1" y="1" width="848" height="40" rx="14" fill="#0d1813"/>
  <rect x="1" y="28" width="848" height="13" fill="#0d1813"/>
  <line x1="1" y1="41" x2="849" y2="41" stroke="#1b3826" stroke-width="1"/>

  <!-- Window Controls -->
  <circle cx="28" cy="21" r="6" fill="#ef4444"/>
  <circle cx="48" cy="21" r="6" fill="#eab308"/>
  <circle cx="68" cy="21" r="6" fill="#22c55e"/>

  <text x="425" y="26" fill="#86efac" font-size="12" font-weight="600" text-anchor="middle" class="font-mono">bash - kaviyarasan@ubuntu-vps: ~/production/system.json</text>

  <!-- Terminal Content -->
  <g transform="translate(35, 70)" class="font-mono" font-size="12.5">
    <!-- Command Execution -->
    <text x="0" y="0">
      <tspan fill="#ef4444">➜ </tspan>
      <tspan fill="#22c55e">~/production</tspan>
      <tspan fill="#94a3b8"> cat system_architecture.json</tspan>
    </text>

    <!-- JSON Output -->
    <text x="0" y="26"><tspan class="pun">{</tspan></text>
    
    <text x="20" y="48">
      <tspan class="key">"engineer"</tspan><tspan class="pun">: </tspan><tspan class="str">"Kaviyarasan M"</tspan><tspan class="pun">, </tspan>
    </text>

    <text x="20" y="70">
      <tspan class="key">"email"</tspan><tspan class="pun">: </tspan><tspan class="str">"mkaviyarasan003@gmail.com"</tspan><tspan class="pun">, </tspan>
    </text>

    <text x="20" y="92">
      <tspan class="key">"portfolio"</tspan><tspan class="pun">: </tspan><tspan class="str">"https://developerkavi.in"</tspan><tspan class="pun">, </tspan>
    </text>

    <text x="20" y="114">
      <tspan class="key">"infrastructure"</tspan><tspan class="pun">: {</tspan>
    </text>
    <text x="40" y="136">
      <tspan class="key">"server"</tspan><tspan class="pun">: </tspan><tspan class="str">"Ubuntu VPS // Linux CLI Server Management"</tspan><tspan class="pun">, </tspan>
    </text>
    <text x="40" y="158">
      <tspan class="key">"ci_cd"</tspan><tspan class="pun">: </tspan><tspan class="str">"Jenkins Pipelines &amp; Coolify Production Orchestration"</tspan><tspan class="pun">, </tspan>
    </text>
    <text x="40" y="180">
      <tspan class="key">"containers"</tspan><tspan class="pun">: </tspan><tspan class="str">"Docker Containerized Builds &amp; Microservices"</tspan><tspan class="pun">, </tspan>
    </text>
    <text x="40" y="202">
      <tspan class="key">"database_engine"</tspan><tspan class="pun">: </tspan><tspan class="str">"MySQL Live Connectivity &amp; Automated Schema Validation"</tspan>
    </text>
    <text x="20" y="224"><tspan class="pun">},</tspan></text>

    <text x="20" y="246">
      <tspan class="key">"application_stacks"</tspan><tspan class="pun">: [</tspan>
      <tspan class="str">"Laravel (PHP)"</tspan><tspan class="pun">, </tspan>
      <tspan class="str">"CodeIgniter"</tspan><tspan class="pun">, </tspan>
      <tspan class="str">"React &amp; Modern JS"</tspan>
      <tspan class="pun">],</tspan>
    </text>

    <text x="20" y="268">
      <tspan class="key">"schema_verification"</tspan><tspan class="pun">: </tspan><tspan class="val">"Automated DB Table, Column, Data Type &amp; Compatibility Checks [PASSED]"</tspan><tspan class="pun">, </tspan>
    </text>

    <text x="20" y="290">
      <tspan class="key">"status"</tspan><tspan class="pun">: </tspan><tspan class="val">"All Pipelines Operational &amp; Ready for Production Deployment"</tspan>
    </text>

    <text x="0" y="312"><tspan class="pun">}</tspan></text>
  </g>
</svg>
"""

# 4. skills.svg - Comprehensive Tools & Integration Matrix with Custom Vector Logos/Icons
skills_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="540" viewBox="0 0 850 540" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="skillsBg" x1="0" y1="0" x2="850" y2="540" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#0f1612"/>
    </linearGradient>
    <linearGradient id="skillsBorder" x1="0" y1="0" x2="850" y2="540" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="cardGreen" x1="0" y1="0" x2="365" y2="0">
      <stop offset="0%" stop-color="#0c1812"/>
      <stop offset="100%" stop-color="#13241b"/>
    </linearGradient>
    <linearGradient id="cardRed" x1="0" y1="0" x2="365" y2="0">
      <stop offset="0%" stop-color="#180c0e"/>
      <stop offset="100%" stop-color="#251216"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Outer Card Frame -->
  <rect x="1" y="1" width="848" height="538" rx="16" fill="url(#skillsBg)"/>
  <rect x="1" y="1" width="848" height="538" rx="16" stroke="url(#skillsBorder)" stroke-width="1.5"/>

  <!-- Card Title -->
  <g transform="translate(35, 36)">
    <circle cx="6" cy="6" r="6" fill="#22c55e"/>
    <text x="22" y="10" fill="#f8fafc" font-size="16" font-weight="800" class="font-sans" letter-spacing="0.5">DEV-OPS, INFRASTRUCTURE &amp; BACKEND ARCHITECTURE</text>
    <text x="780" y="10" fill="#4ade80" font-size="12" font-weight="700" text-anchor="end" class="font-mono">KAVIYARASAN M // STACK</text>
  </g>

  <!-- 10 Detailed Tools & Integration Cards (2 Columns x 5 Rows) -->

  <!-- Row 1: Jenkins (Left) & Docker (Right) -->
  <!-- 1. Jenkins -->
  <g transform="translate(35, 60)">
    <rect width="370" height="80" rx="10" fill="url(#cardRed)" stroke="#ef4444" stroke-width="1.2"/>
    <!-- Custom Jenkins Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <circle cx="24" cy="20" r="8" fill="#fca5a5"/>
      <path d="M16 38 C16 30, 32 30, 32 38 Z" fill="#f87171"/>
      <circle cx="24" cy="18" r="3" fill="#180c0e"/>
      <line x1="30" y1="12" x2="38" y2="12" stroke="#ef4444" stroke-width="2"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Jenkins</text>
    <text x="74" y="50" fill="#fca5a5" font-size="11.5" class="font-sans">Automated CI/CD Build &amp; Test Pipeline</text>
    <text x="74" y="66" fill="#86efac" font-size="10" font-weight="600" class="font-mono">⚡ Automated Continuous Integration</text>
  </g>

  <!-- 2. Docker -->
  <g transform="translate(445, 60)">
    <rect width="370" height="80" rx="10" fill="url(#cardGreen)" stroke="#22c55e" stroke-width="1.2"/>
    <!-- Custom Docker Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <rect x="14" y="22" width="6" height="5" fill="#4ade80"/>
      <rect x="21" y="22" width="6" height="5" fill="#4ade80"/>
      <rect x="28" y="22" width="6" height="5" fill="#4ade80"/>
      <rect x="21" y="16" width="6" height="5" fill="#4ade80"/>
      <path d="M10 28 C14 36, 34 36, 38 28 Z" fill="#22c55e"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Docker</text>
    <text x="74" y="50" fill="#86efac" font-size="11.5" class="font-sans">Containerized Application Builds &amp; Microservices</text>
    <text x="74" y="66" fill="#4ade80" font-size="10" font-weight="600" class="font-mono">🐳 Multi-Container Orchestration</text>
  </g>

  <!-- Row 2: Coolify (Left) & Ubuntu VPS (Right) -->
  <!-- 3. Coolify -->
  <g transform="translate(35, 152)">
    <rect width="370" height="80" rx="10" fill="url(#cardRed)" stroke="#ef4444" stroke-width="1.2"/>
    <!-- Custom Coolify Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <path d="M24 12 C28 18, 36 24, 34 34 C32 40, 20 40, 16 34 C14 26, 22 20, 24 12 Z" fill="#ef4444"/>
      <circle cx="24" cy="30" r="4" fill="#fca5a5"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Coolify</text>
    <text x="74" y="50" fill="#fca5a5" font-size="11.5" class="font-sans">Automated Self-Hosted Production Deployment</text>
    <text x="74" y="66" fill="#f87171" font-size="10" font-weight="600" class="font-mono">🚀 Zero-Downtime Releases</text>
  </g>

  <!-- 4. Ubuntu VPS -->
  <g transform="translate(445, 152)">
    <rect width="370" height="80" rx="10" fill="url(#cardGreen)" stroke="#22c55e" stroke-width="1.2"/>
    <!-- Custom Ubuntu Server Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <circle cx="24" cy="24" r="14" stroke="#22c55e" stroke-width="2" fill="none"/>
      <circle cx="24" cy="14" r="3" fill="#4ade80"/>
      <circle cx="15" cy="29" r="3" fill="#4ade80"/>
      <circle cx="33" cy="29" r="3" fill="#4ade80"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Ubuntu VPS</text>
    <text x="74" y="50" fill="#86efac" font-size="11.5" class="font-sans">Server &amp; Cloud Infrastructure Management</text>
    <text x="74" y="66" fill="#4ade80" font-size="10" font-weight="600" class="font-mono">🖥️ Dedicated Production Hosting</text>
  </g>

  <!-- Row 3: MySQL (Left) & Linux CLI (Right) -->
  <!-- 5. MySQL -->
  <g transform="translate(35, 244)">
    <rect width="370" height="80" rx="10" fill="url(#cardGreen)" stroke="#22c55e" stroke-width="1.2"/>
    <!-- Custom MySQL / DB Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <ellipse cx="24" cy="16" rx="14" ry="5" fill="#22c55e"/>
      <path d="M10 16 V 26 C 10 29, 38 29, 38 26 V 16" stroke="#4ade80" stroke-width="2" fill="none"/>
      <path d="M10 26 V 34 C 10 37, 38 37, 38 34 V 26" stroke="#4ade80" stroke-width="2" fill="none"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">MySQL</text>
    <text x="74" y="50" fill="#86efac" font-size="11.5" class="font-sans">Live Database Connectivity &amp; Optimization</text>
    <text x="74" y="66" fill="#4ade80" font-size="10" font-weight="600" class="font-mono">🗄️ High Performance Queries &amp; Indexing</text>
  </g>

  <!-- 6. Linux CLI -->
  <g transform="translate(445, 244)">
    <rect width="370" height="80" rx="10" fill="url(#cardRed)" stroke="#ef4444" stroke-width="1.2"/>
    <!-- Custom Linux CLI Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="12" y="30" fill="#ef4444" font-size="18" font-weight="900" class="font-mono">&gt;_</text>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Linux CLI</text>
    <text x="74" y="50" fill="#fca5a5" font-size="11.5" class="font-sans">VPS Configuration, Troubleshooting &amp; Automation</text>
    <text x="74" y="66" fill="#f87171" font-size="10" font-weight="600" class="font-mono">⚙️ Bash Scripting &amp; SSH Security</text>
  </g>

  <!-- Row 4: Git & GitHub (Left) & Laravel / PHP (Right) -->
  <!-- 7. Git & GitHub -->
  <g transform="translate(35, 336)">
    <rect width="370" height="80" rx="10" fill="url(#cardGreen)" stroke="#22c55e" stroke-width="1.2"/>
    <!-- Custom Git Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <circle cx="16" cy="24" r="4" fill="#4ade80"/>
      <circle cx="32" cy="16" r="4" fill="#4ade80"/>
      <circle cx="32" cy="32" r="4" fill="#4ade80"/>
      <path d="M16 24 L24 24 L32 16 M24 24 L32 32" stroke="#22c55e" stroke-width="2"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Git &amp; GitHub</text>
    <text x="74" y="50" fill="#86efac" font-size="11.5" class="font-sans">Source Control &amp; Automated Webhook Workflows</text>
    <text x="74" y="66" fill="#4ade80" font-size="10" font-weight="600" class="font-mono">🌿 Branch Management &amp; Collaboration</text>
  </g>

  <!-- 8. Laravel / PHP -->
  <g transform="translate(445, 336)">
    <rect width="370" height="80" rx="10" fill="url(#cardRed)" stroke="#ef4444" stroke-width="1.2"/>
    <!-- Custom Laravel Vector Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <path d="M14 18 L24 12 L34 18 L24 24 Z" fill="#ef4444"/>
      <path d="M14 28 L24 22 L34 28 L24 34 Z" fill="#f87171"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">Laravel / PHP</text>
    <text x="74" y="50" fill="#fca5a5" font-size="11.5" class="font-sans">Robust Application Validation &amp; RESTful APIs</text>
    <text x="74" y="66" fill="#f87171" font-size="10" font-weight="600" class="font-mono">🔥 Clean MVC Architecture &amp; Eloquent ORM</text>
  </g>

  <!-- Row 5: CodeIgniter (Left) & Automated DB Schema Verification (Right) -->
  <!-- 9. CodeIgniter -->
  <g transform="translate(35, 428)">
    <rect width="370" height="80" rx="10" fill="url(#cardRed)" stroke="#ef4444" stroke-width="1.2"/>
    <!-- Custom CodeIgniter Flame Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <path d="M24 12 C28 20, 36 24, 32 36 C28 40, 20 40, 16 34 C12 28, 20 22, 24 12 Z" fill="#ef4444"/>
      <path d="M24 22 C26 26, 30 28, 28 34 C26 36, 22 36, 20 32 Z" fill="#fed7aa"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="14" font-weight="700" class="font-sans">CodeIgniter</text>
    <text x="74" y="50" fill="#fca5a5" font-size="11.5" class="font-sans">Lightweight MVC &amp; Application Validation</text>
    <text x="74" y="66" fill="#f87171" font-size="10" font-weight="600" class="font-mono">⚡ Rapid Backend Engine Execution</text>
  </g>

  <!-- 10. Automated DB Schema Verification -->
  <g transform="translate(445, 428)">
    <rect width="370" height="80" rx="10" fill="url(#cardGreen)" stroke="#22c55e" stroke-width="1.2"/>
    <!-- Custom Schema Check Shield Icon -->
    <g transform="translate(16, 16)">
      <rect width="48" height="48" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <path d="M24 12 L36 17 V 26 C36 34, 24 38, 24 38 C24 38, 12 34, 12 26 V 17 Z" fill="#22c55e"/>
      <path d="M19 25 L23 29 L30 20" stroke="#052e16" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
    <text x="74" y="32" fill="#ffffff" font-size="13.5" font-weight="700" class="font-sans">DB Schema Verification</text>
    <text x="74" y="50" fill="#86efac" font-size="11" class="font-sans">Tables, Columns, Types &amp; Compatibility Checks</text>
    <text x="74" y="66" fill="#4ade80" font-size="10" font-weight="600" class="font-mono">✅ Zero-Error Migration Validation</text>
  </g>
</svg>
"""

# 5. featured-repos.svg - Repositories with developerkavi.in integration
repos_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="340" viewBox="0 0 850 340" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="repoBg" x1="0" y1="0" x2="850" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#120a0c"/>
    </linearGradient>
    <linearGradient id="repoBorder" x1="0" y1="0" x2="850" y2="340" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.7"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="338" rx="16" fill="url(#repoBg)"/>
  <rect x="1" y="1" width="848" height="338" rx="16" stroke="url(#repoBorder)" stroke-width="1.5"/>

  <!-- Title Header -->
  <g transform="translate(35, 38)">
    <circle cx="6" cy="6" r="6" fill="#ef4444"/>
    <text x="22" y="10" fill="#f8fafc" font-size="16" font-weight="800" class="font-sans">FEATURED PRODUCTION ARCHITECTURES</text>
    <text x="780" y="10" fill="#4ade80" font-size="12" font-weight="600" text-anchor="end" class="font-mono">developerkavi.in // CODEBASE</text>
  </g>

  <!-- 3 Project Cards -->
  <!-- Card 1 -->
  <g transform="translate(35, 75)">
    <rect width="245" height="225" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.2"/>
    <circle cx="25" cy="30" r="10" fill="#052e16"/>
    <text x="25" y="34" fill="#4ade80" font-size="12" text-anchor="middle" class="font-mono">📦</text>
    <text x="45" y="35" fill="#f8fafc" font-size="15" font-weight="700" class="font-sans">developerkavi-portal</text>
    <text x="25" y="70" fill="#94a3b8" font-size="12" class="font-sans">Official portfolio ecosystem with live CI/CD pipeline &amp; Coolify orchestration.</text>
    
    <g transform="translate(25, 145)">
      <rect width="85" height="22" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="42" y="15" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">COOLIFY</text>
    </g>
    <g transform="translate(120, 145)">
      <rect width="90" height="22" rx="6" fill="#1f2937"/>
      <text x="45" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">UBUNTU</text>
    </g>

    <g transform="translate(25, 195)">
      <circle cx="6" cy="6" r="4" fill="#22c55e"/>
      <text x="18" y="10" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">LIVE // STABLE</text>
    </g>
  </g>

  <!-- Card 2 -->
  <g transform="translate(300, 75)">
    <rect width="245" height="225" rx="12" fill="#180d0f" stroke="#ef4444" stroke-width="1.2"/>
    <circle cx="25" cy="30" r="10" fill="#450a0a"/>
    <text x="25" y="34" fill="#f87171" font-size="12" text-anchor="middle" class="font-mono">⚛️</text>
    <text x="45" y="35" fill="#f8fafc" font-size="15" font-weight="700" class="font-sans">vps-db-verifier</text>
    <text x="25" y="70" fill="#94a3b8" font-size="12" class="font-sans">Automated MySQL schema inspection, column validator &amp; migration tester.</text>
    
    <g transform="translate(25, 145)">
      <rect width="85" height="22" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="42" y="15" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">LARAVEL</text>
    </g>
    <g transform="translate(120, 145)">
      <rect width="90" height="22" rx="6" fill="#1f2937"/>
      <text x="45" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">MYSQL</text>
    </g>

    <g transform="translate(25, 195)">
      <circle cx="6" cy="6" r="4" fill="#ef4444"/>
      <text x="18" y="10" fill="#f87171" font-size="11" font-weight="600" class="font-mono">CI/CD // ACTIVE</text>
    </g>
  </g>

  <!-- Card 3 -->
  <g transform="translate(565, 75)">
    <rect width="245" height="225" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.2"/>
    <circle cx="25" cy="30" r="10" fill="#052e16"/>
    <text x="25" y="34" fill="#4ade80" font-size="12" text-anchor="middle" class="font-mono">⚡</text>
    <text x="45" y="35" fill="#f8fafc" font-size="15" font-weight="700" class="font-sans">docker-pipeline-hub</text>
    <text x="25" y="70" fill="#94a3b8" font-size="12" class="font-sans">Multi-stage Docker container pipeline with Jenkins webhooks &amp; Linux CLI tooling.</text>
    
    <g transform="translate(25, 145)">
      <rect width="85" height="22" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="42" y="15" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">DOCKER</text>
    </g>
    <g transform="translate(120, 145)">
      <rect width="90" height="22" rx="6" fill="#1f2937"/>
      <text x="45" y="15" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">JENKINS</text>
    </g>

    <g transform="translate(25, 195)">
      <circle cx="6" cy="6" r="4" fill="#22c55e"/>
      <text x="18" y="10" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">ONLINE</text>
    </g>
  </g>
</svg>
"""

# 6. activity-graph.svg - Commit Graph
activity_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="260" viewBox="0 0 850 260" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="graphBg" x1="0" y1="0" x2="850" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#120a0d"/>
    </linearGradient>
    <linearGradient id="graphBorder" x1="0" y1="0" x2="850" y2="260" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.7"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="258" rx="16" fill="url(#graphBg)"/>
  <rect x="1" y="1" width="848" height="258" rx="16" stroke="url(#graphBorder)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(35, 35)">
    <circle cx="6" cy="6" r="6" fill="#22c55e"/>
    <text x="22" y="10" fill="#f8fafc" font-size="15" font-weight="800" class="font-sans">ENGINEERING VELOCITY &amp; COMMIT ACTIVITY</text>
    <text x="780" y="10" fill="#86efac" font-size="12" font-weight="600" text-anchor="end" class="font-mono">developerkavi.in</text>
  </g>

  <!-- Activity Grid Pattern -->
  <g transform="translate(35, 65)">
"""

import random
random.seed(99)
for col in range(35):
    for row in range(7):
        x = col * 22
        y = row * 18
        rand = random.random()
        if rand > 0.88:
            color = "#ef4444"
        elif rand > 0.65:
            color = "#22c55e"
        elif rand > 0.40:
            color = "#15803d"
        elif rand > 0.20:
            color = "#166534"
        else:
            color = "#0e2016"
        activity_svg += f'    <rect x="{x}" y="{y}" width="16" height="13" rx="3" fill="{color}"/>\n'

activity_svg += """  </g>

  <!-- Legend & Metrics Bar -->
  <g transform="translate(35, 215)">
    <text x="0" y="15" fill="#94a3b8" font-size="11" class="font-mono">Less</text>
    <rect x="35" y="4" width="14" height="13" rx="2" fill="#0e2016"/>
    <rect x="55" y="4" width="14" height="13" rx="2" fill="#166534"/>
    <rect x="75" y="4" width="14" height="13" rx="2" fill="#15803d"/>
    <rect x="95" y="4" width="14" height="13" rx="2" fill="#22c55e"/>
    <rect x="115" y="4" width="14" height="13" rx="2" fill="#ef4444"/>
    <text x="135" y="15" fill="#f87171" font-size="11" class="font-mono">More / Deployments</text>

    <!-- Right Metric -->
    <text x="780" y="15" fill="#4ade80" font-size="12" font-weight="700" text-anchor="end" class="font-mono">99.8% PIPELINE SUCCESS RATE</text>
  </g>
</svg>
"""

# 7. stats.svg - GitHub & VPS Telemetry
stats_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="220" viewBox="0 0 850 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="statsBg" x1="0" y1="0" x2="850" y2="220" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>
    <linearGradient id="statsBorder" x1="0" y1="0" x2="850" y2="220" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.7"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="218" rx="16" fill="url(#statsBg)"/>
  <rect x="1" y="1" width="848" height="218" rx="16" stroke="url(#statsBorder)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(35, 35)">
    <circle cx="6" cy="6" r="6" fill="#22c55e"/>
    <text x="22" y="10" fill="#f8fafc" font-size="15" font-weight="800" class="font-sans">INFRASTRUCTURE &amp; PRODUCTION TELEMETRY</text>
    <text x="780" y="10" fill="#f87171" font-size="12" font-weight="600" text-anchor="end" class="font-mono">KAVIYARASAN M</text>
  </g>

  <!-- 4 Telemetry Stats Boxes -->
  <!-- Box 1 -->
  <g transform="translate(35, 65)">
    <rect width="180" height="120" rx="10" fill="#0d1813" stroke="#22c55e" stroke-width="1"/>
    <text x="20" y="32" fill="#86efac" font-size="11" font-weight="700" class="font-mono">VPS DEPLOYMENTS</text>
    <text x="20" y="75" fill="#f8fafc" font-size="32" font-weight="900" class="font-sans">100+</text>
    <text x="20" y="100" fill="#22c55e" font-size="11" font-weight="600" class="font-mono">↑ Live on Coolify</text>
  </g>

  <!-- Box 2 -->
  <g transform="translate(235, 65)">
    <rect width="180" height="120" rx="10" fill="#180d0f" stroke="#ef4444" stroke-width="1"/>
    <text x="20" y="32" fill="#fca5a5" font-size="11" font-weight="700" class="font-mono">CI/CD PIPELINES</text>
    <text x="20" y="75" fill="#f8fafc" font-size="32" font-weight="900" class="font-sans">50+</text>
    <text x="20" y="100" fill="#ef4444" font-size="11" font-weight="600" class="font-mono">↑ Jenkins Automated</text>
  </g>

  <!-- Box 3 -->
  <g transform="translate(435, 65)">
    <rect width="180" height="120" rx="10" fill="#0d1813" stroke="#22c55e" stroke-width="1"/>
    <text x="20" y="32" fill="#86efac" font-size="11" font-weight="700" class="font-mono">DB SCHEMA AUDITS</text>
    <text x="20" y="75" fill="#f8fafc" font-size="32" font-weight="900" class="font-sans">100%</text>
    <text x="20" y="100" fill="#22c55e" font-size="11" font-weight="600" class="font-mono">↑ Automated Verified</text>
  </g>

  <!-- Box 4 -->
  <g transform="translate(635, 65)">
    <rect width="180" height="120" rx="10" fill="#180d0f" stroke="#ef4444" stroke-width="1"/>
    <text x="20" y="32" fill="#fca5a5" font-size="11" font-weight="700" class="font-mono">SYSTEM UPTIME</text>
    <text x="20" y="75" fill="#f8fafc" font-size="32" font-weight="900" class="font-sans">99.9%</text>
    <text x="20" y="100" fill="#ef4444" font-size="11" font-weight="600" class="font-mono">Ubuntu Server SLA</text>
  </g>
</svg>
"""

# 8. contact.svg - Contact Card with developerkavi.in & mkaviyarasan003@gmail.com
contact_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="310" viewBox="0 0 850 310" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="contactBg" x1="0" y1="0" x2="850" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="50%" stop-color="#0c1410"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>
    <linearGradient id="contactBorder" x1="0" y1="0" x2="850" y2="310" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.8"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="308" rx="16" fill="url(#contactBg)"/>
  <rect x="1" y="1" width="848" height="308" rx="16" stroke="url(#contactBorder)" stroke-width="1.5"/>

  <!-- Glowing Accents -->
  <circle cx="100" cy="150" r="80" fill="#22c55e" opacity="0.08" filter="blur(30px)"/>
  <circle cx="750" cy="150" r="80" fill="#ef4444" opacity="0.08" filter="blur(30px)"/>

  <!-- Content -->
  <g transform="translate(50, 45)">
    <!-- Sub-heading -->
    <text x="0" y="0" fill="#f87171" font-size="13" font-weight="700" letter-spacing="2" class="font-mono">GET IN TOUCH // INITIATE TRANSMISSION</text>
    
    <!-- Headline -->
    <text x="0" y="38" fill="#ffffff" font-size="30" font-weight="900" class="font-sans">Let's Build Something Extraordinary Together</text>
    
    <!-- Description -->
    <text x="0" y="70" fill="#94a3b8" font-size="14" class="font-sans">
      Full Stack Web Development, VPS Infrastructure, CI/CD Automations &amp; API Systems.
    </text>
    <text x="0" y="92" fill="#94a3b8" font-size="14" class="font-sans">
      Explore <tspan fill="#4ade80" font-weight="700">developerkavi.in</tspan> or email directly to collaborate.
    </text>

    <!-- Email Badge Card -->
    <g transform="translate(0, 125)">
      <rect width="450" height="54" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.5"/>
      <circle cx="30" cy="27" r="14" fill="#052e16"/>
      <text x="30" y="32" fill="#4ade80" font-size="15" text-anchor="middle">✉️</text>
      <text x="60" y="24" fill="#64748b" font-size="10" font-weight="700" class="font-mono">PRIMARY EMAIL ADDRESS</text>
      <text x="60" y="42" fill="#4ade80" font-size="16" font-weight="800" class="font-mono">mkaviyarasan003@gmail.com</text>
    </g>

    <!-- CTA Button Badge (Right) -->
    <g transform="translate(470, 125)">
      <rect width="280" height="54" rx="12" fill="#450a0a" stroke="#ef4444" stroke-width="1.5"/>
      <text x="140" y="25" fill="#fca5a5" font-size="11" font-weight="700" text-anchor="middle" class="font-mono">DIRECT DISPATCH</text>
      <text x="140" y="43" fill="#ffffff" font-size="14" font-weight="800" text-anchor="middle" class="font-sans">Click to Send Message ➔</text>
    </g>
  </g>

  <!-- Bottom Indicator -->
  <g transform="translate(50, 265)">
    <circle cx="6" cy="6" r="4" fill="#22c55e"/>
    <text x="20" y="10" fill="#86efac" font-size="11" font-weight="600" class="font-mono">STATUS: ACTIVE &amp; RESPONSIVE WITHIN 24 HOURS</text>
  </g>
</svg>
"""

# 9. footer.svg - Footer with developerkavi.in
footer_svg = """<?xml version="1.0" encoding="UTF-8"?>
<svg width="850" height="100" viewBox="0 0 850 100" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="footerBg" x1="0" y1="0" x2="850" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#12080a"/>
    </linearGradient>
    <linearGradient id="footerBorder" x1="0" y1="0" x2="850" y2="100" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#22c55e" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#ef4444" stop-opacity="0.6"/>
    </linearGradient>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <!-- Frame -->
  <rect x="1" y="1" width="848" height="98" rx="14" fill="url(#footerBg)"/>
  <rect x="1" y="1" width="848" height="98" rx="14" stroke="url(#footerBorder)" stroke-width="1.2"/>

  <!-- Footer Content -->
  <g transform="translate(425, 42)">
    <text x="0" y="0" fill="#f8fafc" font-size="14" font-weight="700" text-anchor="middle" class="font-sans">
      Designed &amp; Engineered by <tspan fill="#4ade80">Kaviyarasan M</tspan>
    </text>
    <text x="0" y="24" fill="#f87171" font-size="11.5" font-weight="600" text-anchor="middle" class="font-mono">
      🌐 https://developerkavi.in • ALL SYSTEMS OPERATIONAL
    </text>
  </g>
</svg>
"""

svgs = {
    "header.svg": header_svg,
    "typing.svg": typing_svg,
    "about.svg": about_svg,
    "skills.svg": skills_svg,
    "featured-repos.svg": repos_svg,
    "activity-graph.svg": activity_svg,
    "stats.svg": stats_svg,
    "contact.svg": contact_svg,
    "footer.svg": footer_svg,
}

for filename, content in svgs.items():
    filepath = os.path.join(assets_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {filename} ({len(content)} bytes)")

print("All 9 SVGs successfully updated with Anime Boy Coding, developerkavi.in, and all 10 tools & integrations!")
