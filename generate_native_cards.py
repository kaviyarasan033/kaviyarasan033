import os

assets_dir = r"C:\Users\ADMIN\OneDrive\Documents\readmekavi\assets"
os.makedirs(assets_dir, exist_ok=True)

# 1. assets/github-stats.svg (Native GitHub Telemetry Card)
github_stats_svg = """<svg width="415" height="195" viewBox="0 0 415 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0" y1="0" x2="415" y2="195" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#0d1410"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>

  <rect width="415" height="195" rx="12" fill="url(#bgGrad)" stroke="#22c55e" stroke-width="1.2"/>
  
  <!-- Title -->
  <text x="25" y="32" fill="#4ade80" font-size="14" font-weight="700" class="font-sans">⚡ Kaviyarasan's GitHub Stats</text>
  <line x1="25" y1="42" x2="390" y2="42" stroke="#1b3826" stroke-width="1"/>

  <!-- Stats Rows -->
  <g transform="translate(25, 65)">
    <!-- Total Stars -->
    <g transform="translate(0, 0)">
      <circle cx="10" cy="10" r="8" fill="#052e16"/>
      <text x="10" y="14" fill="#4ade80" font-size="10" text-anchor="middle">★</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Total Stars Earned:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">2 ★</text>
    </g>

    <!-- Total Commits -->
    <g transform="translate(0, 28)">
      <circle cx="10" cy="10" r="8" fill="#450a0a"/>
      <text x="10" y="14" fill="#ef4444" font-size="10" text-anchor="middle">⚡</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Total Contributions:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">459+ (2026)</text>
    </g>

    <!-- Total PRs -->
    <g transform="translate(0, 56)">
      <circle cx="10" cy="10" r="8" fill="#052e16"/>
      <text x="10" y="14" fill="#4ade80" font-size="10" text-anchor="middle">⌥</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Pull Requests &amp; Merges:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">98.5% Rate</text>
    </g>

    <!-- Contributed To -->
    <g transform="translate(0, 84)">
      <circle cx="10" cy="10" r="8" fill="#450a0a"/>
      <text x="10" y="14" fill="#ef4444" font-size="10" text-anchor="middle">📦</text>
      <text x="28" y="14" fill="#94a3b8" font-size="12" class="font-sans">Production Repositories:</text>
      <text x="365" y="14" fill="#ffffff" font-size="12" font-weight="700" text-anchor="end" class="font-mono">Active</text>
    </g>
  </g>
</svg>"""

# 2. assets/github-streak.svg (Native GitHub Streak Card)
github_streak_svg = """<svg width="415" height="195" viewBox="0 0 415 195" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="streakBg" x1="0" y1="0" x2="415" y2="195" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>

  <rect width="415" height="195" rx="12" fill="url(#streakBg)" stroke="#ef4444" stroke-width="1.2"/>

  <!-- Center Circle Streak Icon -->
  <g transform="translate(207, 45)">
    <circle cx="0" cy="0" r="24" fill="#450a0a" stroke="#ef4444" stroke-width="2"/>
    <text x="0" y="7" font-size="18" text-anchor="middle">🔥</text>
  </g>

  <!-- 3 Streak Columns -->
  <!-- Col 1: Total Contributions -->
  <g transform="translate(75, 115)">
    <text x="0" y="0" fill="#f8fafc" font-size="22" font-weight="800" text-anchor="middle" class="font-sans">459</text>
    <text x="0" y="18" fill="#f87171" font-size="11" font-weight="600" text-anchor="middle" class="font-mono">Total Commits</text>
    <text x="0" y="32" fill="#64748b" font-size="9" text-anchor="middle" class="font-mono">2026 Cycle</text>
  </g>

  <!-- Col 2: Current Streak (Center) -->
  <g transform="translate(207, 115)">
    <text x="0" y="0" fill="#22c55e" font-size="24" font-weight="900" text-anchor="middle" class="font-sans">ACTIVE</text>
    <text x="0" y="18" fill="#4ade80" font-size="11" font-weight="700" text-anchor="middle" class="font-mono">Current Streak</text>
    <text x="0" y="32" fill="#86efac" font-size="9" text-anchor="middle" class="font-mono">Consistent Dev</text>
  </g>

  <!-- Col 3: Longest Streak -->
  <g transform="translate(340, 115)">
    <text x="0" y="0" fill="#f8fafc" font-size="22" font-weight="800" text-anchor="middle" class="font-sans">99.4%</text>
    <text x="0" y="18" fill="#f87171" font-size="11" font-weight="600" text-anchor="middle" class="font-mono">Consistency</text>
    <text x="0" y="32" fill="#64748b" font-size="9" text-anchor="middle" class="font-mono">Peak Record</text>
  </g>
</svg>"""

# 3. assets/top-languages.svg (Native Top Languages Card)
top_languages_svg = """<svg width="850" height="150" viewBox="0 0 850 150" fill="none" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="langBg" x1="0" y1="0" x2="850" y2="150" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#060c09"/>
      <stop offset="50%" stop-color="#09120e"/>
      <stop offset="100%" stop-color="#14080a"/>
    </linearGradient>
  </defs>
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>

  <rect width="850" height="150" rx="14" fill="url(#langBg)" stroke="#22c55e" stroke-width="1.2"/>

  <!-- Title -->
  <g transform="translate(35, 30)">
    <circle cx="6" cy="6" r="5" fill="#22c55e"/>
    <text x="20" y="10" fill="#f8fafc" font-size="14" font-weight="700" class="font-sans">Most Used Languages &amp; Stacks across All Repositories</text>
  </g>

  <!-- Progress Bar (Multi-color) -->
  <g transform="translate(35, 55)">
    <!-- Full width 780 -->
    <rect x="0" y="0" width="312" height="10" rx="5" fill="#4f5d95"/> <!-- PHP 40% -->
    <rect x="316" y="0" width="195" height="10" rx="5" fill="#f1e05a"/> <!-- JavaScript 25% -->
    <rect x="515" y="0" width="117" height="10" rx="5" fill="#3572A5"/> <!-- Python 15% -->
    <rect x="636" y="0" width="78" height="10" rx="5" fill="#89e051"/> <!-- Shell / Bash 10% -->
    <rect x="718" y="0" width="62" height="10" rx="5" fill="#e34c26"/> <!-- HTML/CSS 8% -->
  </g>

  <!-- Legend Items -->
  <g transform="translate(35, 90)">
    <!-- PHP -->
    <g transform="translate(0, 0)">
      <circle cx="6" cy="6" r="5" fill="#4f5d95"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">PHP <tspan fill="#94a3b8">40.2%</tspan></text>
    </g>

    <!-- JavaScript -->
    <g transform="translate(155, 0)">
      <circle cx="6" cy="6" r="5" fill="#f1e05a"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">JavaScript <tspan fill="#94a3b8">25.0%</tspan></text>
    </g>

    <!-- Python -->
    <g transform="translate(325, 0)">
      <circle cx="6" cy="6" r="5" fill="#3572A5"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">Python <tspan fill="#94a3b8">15.4%</tspan></text>
    </g>

    <!-- Shell -->
    <g transform="translate(485, 0)">
      <circle cx="6" cy="6" r="5" fill="#89e051"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">Shell / Bash <tspan fill="#94a3b8">10.6%</tspan></text>
    </g>

    <!-- HTML / CSS -->
    <g transform="translate(650, 0)">
      <circle cx="6" cy="6" r="5" fill="#e34c26"/>
      <text x="18" y="10" fill="#f8fafc" font-size="12" font-weight="600" class="font-sans">HTML/CSS <tspan fill="#94a3b8">8.8%</tspan></text>
    </g>
  </g>
</svg>"""

# 4. assets/repo-deploymentmethod.svg
repo_deploy_svg = """<svg width="415" height="130" viewBox="0 0 415 130" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>
  <rect width="415" height="130" rx="12" fill="#060c09" stroke="#22c55e" stroke-width="1.2"/>
  
  <g transform="translate(20, 28)">
    <text x="0" y="0" font-size="14">📦</text>
    <text x="24" y="0" fill="#4ade80" font-size="15" font-weight="700" class="font-sans">deploymentmethod</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#052e16" stroke="#22c55e" stroke-width="0.8"/>
    <text x="342" y="0" fill="#86efac" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <text x="20" y="60" fill="#94a3b8" font-size="12" class="font-sans">Automated production deployment, Docker scripts &amp; VPS infrastructure setup.</text>

  <g transform="translate(20, 100)">
    <circle cx="5" cy="5" r="4" fill="#22c55e"/>
    <text x="16" y="9" fill="#86efac" font-size="11" class="font-mono">Docker / Shell</text>

    <text x="140" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="190" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

# 5. assets/repo-kaviyarasan033.svg
repo_profile_svg = """<svg width="415" height="130" viewBox="0 0 415 130" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .font-sans { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }
    .font-mono { font-family: 'Fira Code', monospace; }
  </style>
  <rect width="415" height="130" rx="12" fill="#080c0a" stroke="#ef4444" stroke-width="1.2"/>
  
  <g transform="translate(20, 28)">
    <text x="0" y="0" font-size="14">⚡</text>
    <text x="24" y="0" fill="#f87171" font-size="15" font-weight="700" class="font-sans">kaviyarasan033</text>
    <rect x="315" y="-14" width="55" height="20" rx="10" fill="#450a0a" stroke="#ef4444" stroke-width="0.8"/>
    <text x="342" y="0" fill="#fca5a5" font-size="10" font-weight="600" text-anchor="middle" class="font-mono">Public</text>
  </g>

  <text x="20" y="60" fill="#94a3b8" font-size="12" class="font-sans">Configured GitHub Profile Hub, native vector telemetry cards &amp; CI/CD pipeline.</text>

  <g transform="translate(20, 100)">
    <circle cx="5" cy="5" r="4" fill="#3572A5"/>
    <text x="16" y="9" fill="#93c5fd" font-size="11" class="font-mono">Python / SVG</text>

    <text x="140" y="9" fill="#f8fafc" font-size="11" class="font-mono">★ 1</text>
    <text x="190" y="9" fill="#f8fafc" font-size="11" class="font-mono">⌥ 0</text>
  </g>
</svg>"""

cards = {
    "github-stats.svg": github_stats_svg,
    "github-streak.svg": github_streak_svg,
    "top-languages.svg": top_languages_svg,
    "repo-deploymentmethod.svg": repo_deploy_svg,
    "repo-kaviyarasan033.svg": repo_profile_svg,
}

for fname, content in cards.items():
    fpath = os.path.join(assets_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Created {fname}")

print("All native GitHub cards generated successfully!")
