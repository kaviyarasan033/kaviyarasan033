import os
import random

snake_svg_path = r"C:\Users\ADMIN\OneDrive\Documents\readmekavi\assets\github-contribution-grid-snake-dark.svg"

# Create a sleek animated contribution grid snake SVG
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="850" height="200" viewBox="0 0 850 200" fill="none">
  <style>
    .cell { shape-rendering: geometricPrecision; rx: 3px; ry: 3px; }
    .snake-head {
      fill: #22c55e;
      filter: drop-shadow(0 0 6px #22c55e);
      animation: snakeMove 10s infinite linear;
    }
    .snake-body {
      fill: #4ade80;
      animation: snakeMove 10s infinite linear;
    }
    .food {
      fill: #ef4444;
      filter: drop-shadow(0 0 4px #ef4444);
      animation: pulseFood 1.5s infinite alternate;
    }
    @keyframes pulseFood {
      0% { transform: scale(0.9); opacity: 0.7; }
      100% { transform: scale(1.1); opacity: 1; }
    }
    @keyframes snakeMove {
      0% { transform: translate(0px, 0px); }
      25% { transform: translate(240px, 36px); }
      50% { transform: translate(460px, 0px); }
      75% { transform: translate(680px, 54px); }
      100% { transform: translate(0px, 0px); }
    }
    .font-mono { font-family: 'Fira Code', 'Cascadia Code', Consolas, Monaco, monospace; }
  </style>

  <rect width="850" height="200" rx="14" fill="#080c0a" stroke="#1b3826" stroke-width="1.5"/>

  <!-- Title Header -->
  <g transform="translate(30, 26)">
    <circle cx="6" cy="6" r="5" fill="#22c55e"/>
    <text x="20" y="10" fill="#86efac" font-size="13" font-weight="700" class="font-mono">CONTRIBUTION ACTIVITY FLOW // 459+ CONTRIBUTIONS</text>
    <text x="790" y="10" fill="#ef4444" font-size="11" font-weight="600" text-anchor="end" class="font-mono">LIVE SNAKE ENGINE</text>
  </g>

  <!-- Contribution Grid (52 weeks x 7 days) -->
  <g transform="translate(30, 50)">
"""

random.seed(1337)
grid_colors = ['#161b22', '#0e4429', '#006d32', '#26a641', '#39d353']

# 52 columns x 7 rows
for col in range(53):
    for row in range(7):
        x = col * 14.8
        y = row * 14.8
        # Make a realistic distribution matching 459 contributions
        prob = random.random()
        if col > 38: # Recent months heavy activity
            if prob > 0.3:
                c = random.choice(grid_colors[1:])
            else:
                c = grid_colors[0]
        elif col > 25:
            if prob > 0.5:
                c = random.choice(grid_colors[1:4])
            else:
                c = grid_colors[0]
        else:
            if prob > 0.7:
                c = random.choice(grid_colors[1:3])
            else:
                c = grid_colors[0]
        
        svg_content += f'    <rect class="cell" x="{x:.1f}" y="{y:.1f}" width="11" height="11" fill="{c}"/>\n'

svg_content += """
    <!-- Animated Snake Eating Dots -->
    <g class="snake-head">
      <rect class="cell" x="148" y="44.4" width="11" height="11" fill="#4ade80"/>
      <circle cx="151" cy="47.4" r="1.5" fill="#052e16"/>
      <circle cx="156" cy="47.4" r="1.5" fill="#052e16"/>
    </g>
    <g class="snake-body">
      <rect class="cell" x="133.2" y="44.4" width="11" height="11" fill="#22c55e"/>
      <rect class="cell" x="118.4" y="44.4" width="11" height="11" fill="#16a34a"/>
      <rect class="cell" x="103.6" y="44.4" width="11" height="11" fill="#15803d"/>
    </g>

    <!-- Food Nodes -->
    <g transform="translate(444, 29.6)">
      <circle cx="5.5" cy="5.5" r="4.5" class="food"/>
    </g>
    <g transform="translate(680, 59.2)">
      <circle cx="5.5" cy="5.5" r="4.5" class="food"/>
    </g>
  </g>

  <!-- Legend -->
  <g transform="translate(30, 172)">
    <text x="0" y="10" fill="#94a3b8" font-size="11" class="font-mono">Less</text>
    <rect x="35" y="0" width="10" height="10" rx="2" fill="#161b22"/>
    <rect x="50" y="0" width="10" height="10" rx="2" fill="#0e4429"/>
    <rect x="65" y="0" width="10" height="10" rx="2" fill="#006d32"/>
    <rect x="80" y="0" width="10" height="10" rx="2" fill="#26a641"/>
    <rect x="95" y="0" width="10" height="10" rx="2" fill="#39d353"/>
    <text x="115" y="10" fill="#94a3b8" font-size="11" class="font-mono">More</text>

    <text x="790" y="10" fill="#4ade80" font-size="11.5" font-weight="700" text-anchor="end" class="font-mono">⚡ 459+ COMMITS IN 2026</text>
  </g>
</svg>
"""

with open(snake_svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content.strip())

print("Generated assets/github-contribution-grid-snake-dark.svg successfully!")
