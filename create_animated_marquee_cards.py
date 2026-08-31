import os

assets_dir = r"C:\Users\ADMIN\OneDrive\Documents\readmekavi\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. featured-repos.svg with Animated Bash Terminal & Marquee Flow
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

    <!-- Clip Paths for Terminal Marquees -->
    <clipPath id="termClip1">
      <rect x="0" y="0" width="208" height="50" rx="6"/>
    </clipPath>
    <clipPath id="termClip2">
      <rect x="0" y="0" width="208" height="50" rx="6"/>
    </clipPath>
    <clipPath id="termClip3">
      <rect x="0" y="0" width="208" height="50" rx="6"/>
    </clipPath>
  </defs>

  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
    
    @keyframes marqueeMove1 {
      0%, 20% { transform: translateX(0px); }
      50%, 70% { transform: translateX(-110px); }
      90%, 100% { transform: translateX(0px); }
    }
    @keyframes marqueeMove2 {
      0%, 20% { transform: translateX(0px); }
      50%, 70% { transform: translateX(-125px); }
      90%, 100% { transform: translateX(0px); }
    }
    @keyframes marqueeMove3 {
      0%, 20% { transform: translateX(0px); }
      50%, 70% { transform: translateX(-115px); }
      90%, 100% { transform: translateX(0px); }
    }

    .marquee-1 { animation: marqueeMove1 7s ease-in-out infinite; }
    .marquee-2 { animation: marqueeMove2 7.5s ease-in-out infinite; }
    .marquee-3 { animation: marqueeMove3 7s ease-in-out infinite; }

    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    .cursor { animation: blink 0.8s infinite; }

    @keyframes pulseInd { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }
    .pulse-indicator { animation: pulseInd 2s infinite ease-in-out; }
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

  <!-- Card 1 -->
  <g transform="translate(35, 68)">
    <rect width="245" height="250" rx="12" fill="#0d1813" stroke="#22c55e" stroke-width="1.3"/>
    <circle cx="25" cy="28" r="10" fill="#052e16"/>
    <text x="25" y="32" fill="#4ade80" font-size="12" text-anchor="middle" class="font-mono">📦</text>
    <text x="45" y="32" fill="#f8fafc" font-size="14.5" font-weight="700" class="font-sans">developerkavi-portal</text>
    
    <!-- Mini Terminal Box with Animated Bash Marquee -->
    <g transform="translate(18, 55)">
      <rect width="209" height="50" rx="8" fill="#040e08" stroke="#166534" stroke-width="1"/>
      <g clip-path="url(#termClip1)">
        <g class="marquee-1">
          <text x="12" y="22" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">
            <tspan fill="#ef4444">➜ </tspan>coolify deploy --prod --live
          </text>
          <text x="12" y="38" fill="#86efac" font-size="10.5" class="font-mono">
            ⚡ Automated Ecosystem Setup
          </text>
        </g>
      </g>
    </g>
    
    <!-- Badges -->
    <g transform="translate(20, 155)">
      <rect width="90" height="24" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="45" y="16" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">COOLIFY</text>
    </g>
    <g transform="translate(120, 155)">
      <rect width="85" height="24" rx="6" fill="#1f2937"/>
      <text x="42" y="16" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">UBUNTU</text>
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
    
    <!-- Mini Terminal Box with Animated Bash Marquee -->
    <g transform="translate(18, 55)">
      <rect width="209" height="50" rx="8" fill="#130608" stroke="#991b1b" stroke-width="1"/>
      <g clip-path="url(#termClip2)">
        <g class="marquee-2">
          <text x="12" y="22" fill="#f87171" font-size="11" font-weight="600" class="font-mono">
            <tspan fill="#4ade80">➜ </tspan>php artisan db:verify --schema
          </text>
          <text x="12" y="38" fill="#fca5a5" font-size="10.5" class="font-mono">
            🗄️ MySQL Schema &amp; Migration Check
          </text>
        </g>
      </g>
    </g>
    
    <!-- Badges -->
    <g transform="translate(20, 155)">
      <rect width="90" height="24" rx="6" fill="#450a0a" stroke="#ef4444" stroke-width="1"/>
      <text x="45" y="16" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">LARAVEL</text>
    </g>
    <g transform="translate(120, 155)">
      <rect width="85" height="24" rx="6" fill="#1f2937"/>
      <text x="42" y="16" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">MYSQL</text>
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
    
    <!-- Mini Terminal Box with Animated Bash Marquee -->
    <g transform="translate(18, 55)">
      <rect width="209" height="50" rx="8" fill="#040e08" stroke="#166534" stroke-width="1"/>
      <g clip-path="url(#termClip3)">
        <g class="marquee-3">
          <text x="12" y="22" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">
            <tspan fill="#ef4444">➜ </tspan>docker-compose up -d --build
          </text>
          <text x="12" y="38" fill="#86efac" font-size="10.5" class="font-mono">
            🐳 Jenkins Automated Pipeline
          </text>
        </g>
      </g>
    </g>
    
    <!-- Badges -->
    <g transform="translate(20, 155)">
      <rect width="90" height="24" rx="6" fill="#052e16" stroke="#22c55e" stroke-width="1"/>
      <text x="45" y="16" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">DOCKER</text>
    </g>
    <g transform="translate(120, 155)">
      <rect width="85" height="24" rx="6" fill="#1f2937"/>
      <text x="42" y="16" fill="#cbd5e1" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">JENKINS</text>
    </g>

    <g transform="translate(20, 215)">
      <circle cx="6" cy="6" r="4" fill="#22c55e" class="pulse-indicator"/>
      <text x="18" y="10" fill="#4ade80" font-size="11" font-weight="600" class="font-mono">ONLINE</text>
    </g>
  </g>
</svg>"""

# 2. repo-deploymentmethod.svg with Animated Bash Terminal Marquee
repo_deploy_svg = """<svg width="415" height="135" viewBox="0 0 415 135" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="depBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#22c55e">
        <animate attributeName="stop-color" values="#22c55e;#10b981;#22c55e" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#16a34a"/>
    </linearGradient>
    <clipPath id="depClip">
      <rect x="0" y="0" width="375" height="34" rx="6"/>
    </clipPath>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
    @keyframes depMarquee {
      0%, 25% { transform: translateX(0px); }
      50%, 75% { transform: translateX(-120px); }
      100% { transform: translateX(0px); }
    }
    .dep-marquee { animation: depMarquee 7s ease-in-out infinite; }
  </style>

  <rect width="415" height="135" rx="12" fill="#060c09" stroke="url(#depBorder)" stroke-width="1.4"/>
  
  <g transform="translate(20, 26)">
    <text x="0" y="0" font-size="14">📦</text>
    <text x="24" y="0" fill="#4ade80" font-size="15" font-weight="700" class="font-sans">deploymentmethod</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="0.8"/>
    <text x="342" y="0" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <!-- Animated Bash Line Container -->
  <g transform="translate(20, 44)">
    <rect width="375" height="34" rx="6" fill="#031208" stroke="#166534" stroke-width="1"/>
    <g clip-path="url(#depClip)">
      <g class="dep-marquee">
        <text x="12" y="21" fill="#4ade80" font-size="11.5" font-weight="600" class="font-mono">
          <tspan fill="#ef4444">➜ </tspan>bash ./deploy-vps.sh --coolify --docker --schema-verify
        </text>
      </g>
    </g>
  </g>

  <g transform="translate(20, 110)">
    <circle cx="5" cy="5" r="4" fill="#22c55e"/>
    <text x="16" y="9" fill="#86efac" font-size="11" class="font-mono">Docker / Shell</text>

    <text x="170" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="230" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

# 3. repo-kaviyarasan033.svg with Animated Bash Terminal Marquee
repo_profile_svg = """<svg width="415" height="135" viewBox="0 0 415 135" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="kaviBorder" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ef4444">
        <animate attributeName="stop-color" values="#ef4444;#f87171;#ef4444" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#dc2626"/>
    </linearGradient>
    <clipPath id="kaviClip">
      <rect x="0" y="0" width="375" height="34" rx="6"/>
    </clipPath>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', Consolas, monospace; }
    @keyframes kaviMarquee {
      0%, 25% { transform: translateX(0px); }
      50%, 75% { transform: translateX(-140px); }
      100% { transform: translateX(0px); }
    }
    .kavi-marquee { animation: kaviMarquee 7s ease-in-out infinite; }
  </style>

  <rect width="415" height="135" rx="12" fill="#080c0a" stroke="url(#kaviBorder)" stroke-width="1.4"/>
  
  <g transform="translate(20, 26)">
    <text x="0" y="0" font-size="14">⚡</text>
    <text x="24" y="0" fill="#f87171" font-size="15" font-weight="700" class="font-sans">kaviyarasan033</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="0.8"/>
    <text x="342" y="0" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <!-- Animated Bash Line Container -->
  <g transform="translate(20, 44)">
    <rect width="375" height="34" rx="6" fill="#130608" stroke="#991b1b" stroke-width="1"/>
    <g clip-path="url(#kaviClip)">
      <g class="kavi-marquee">
        <text x="12" y="21" fill="#f87171" font-size="11.5" font-weight="600" class="font-mono">
          <tspan fill="#4ade80">➜ </tspan>git push origin main --live-profile-telemetry --snake-game
        </text>
      </g>
    </g>
  </g>

  <g transform="translate(20, 110)">
    <circle cx="5" cy="5" r="4" fill="#3572A5"/>
    <text x="16" y="9" fill="#93c5fd" font-size="11" class="font-mono">Python / SVG</text>

    <text x="170" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="230" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

cards = {
    "featured-repos.svg": featured_repos_svg,
    "repo-deploymentmethod.svg": repo_deploy_svg,
    "repo-kaviyarasan033.svg": repo_profile_svg,
}

for fname, content in cards.items():
    fpath = os.path.join(assets_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {fname} with Animated Marquee Terminal")

print("All marquee animated cards generated!")
