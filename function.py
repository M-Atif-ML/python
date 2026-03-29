import pygame
import sys
import math
import time

pygame.init()

W, H = 1100, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("pthreads in C — Step-by-Step Visual Explanation")
clock = pygame.time.Clock()

# ── Fonts ──────────────────────────────────────────────────────────────────
try:
    FONT_MONO  = pygame.font.SysFont("monospace",   15, bold=False)
    FONT_MONO_B= pygame.font.SysFont("monospace",   15, bold=True)
    FONT_SM    = pygame.font.SysFont("sans-serif",  13)
    FONT_MD    = pygame.font.SysFont("sans-serif",  15)
    FONT_MD_B  = pygame.font.SysFont("sans-serif",  15, bold=True)
    FONT_LG    = pygame.font.SysFont("sans-serif",  19, bold=True)
    FONT_XL    = pygame.font.SysFont("sans-serif",  24, bold=True)
    FONT_TITLE = pygame.font.SysFont("sans-serif",  28, bold=True)
except:
    FONT_MONO = FONT_MONO_B = FONT_SM = FONT_MD = FONT_MD_B = FONT_LG = FONT_XL = FONT_TITLE = pygame.font.Font(None, 20)

# ── Palette ────────────────────────────────────────────────────────────────
BG          = (15,  16,  28)
PANEL       = (24,  26,  44)
PANEL2      = (30,  33,  55)
BORDER      = (60,  65, 100)

PURPLE      = (127, 119, 221)
PURPLE_DARK = ( 83,  74, 183)
PURPLE_BG   = ( 30,  28,  60)

TEAL        = ( 29, 158, 117)
TEAL_DARK   = ( 15, 110,  86)
TEAL_BG     = ( 20,  55,  45)

AMBER       = (239, 159,  39)
AMBER_DARK  = (186, 117,  23)
AMBER_BG    = ( 55,  40,  10)

CORAL       = (216,  90,  48)
CORAL_DARK  = (153,  60,  29)
CORAL_BG    = ( 55,  25,  15)

GREEN       = ( 80, 220, 130)
GREEN_BG    = ( 15,  55,  30)
RED         = (230,  75,  75)
RED_BG      = ( 55,  20,  20)

WHITE       = (230, 232, 245)
GRAY        = (120, 122, 145)
GRAY_DARK   = ( 60,  62,  85)
MUTED       = ( 85,  87, 110)

CODE_BG     = ( 20,  22,  38)
CODE_HL     = ( 45,  42,  85)
CODE_DONE   = ( 20,  45,  35)

# ── Code lines ─────────────────────────────────────────────────────────────
CODE_LINES = [
    ("int sq = 0;",                                     "global"),
    ("",                                                 "blank"),
    ("void * calc_sq(void * ptr){",                     "fn_head"),
    ("    int val = *(int*) ptr;",                       "fn_body"),
    ("    sq = val * val;",                              "fn_body"),
    ('    printf("In new thread, sq=%d\\n", sq);',       "fn_body"),
    ("    pthread_exit(0);",                             "fn_body"),
    ("}",                                                "fn_head"),
    ("",                                                 "blank"),
    ("int main(){",                                      "main_head"),
    ("    pthread_t tid;",                               "main_body"),
    ("    int n;",                                       "main_body"),
    ('    printf("Enter the number: ");',                "main_body"),
    ("    scanf(\"%d\", &n);",                           "main_body"),
    ("    pthread_create(&tid,NULL,calc_sq,&n);",        "key"),
    ("    pthread_join(tid, NULL);",                     "key"),
    ('    printf("In original thread,sq=%d\\n",sq);',   "main_body"),
    ("    return 0;",                                    "main_body"),
    ("}",                                                "main_head"),
]

# ── Step definitions ────────────────────────────────────────────────────────
STEPS = [
    {
        "title":   "Step 1 — Global Variable",
        "line":    0,
        "color":   PURPLE,
        "bg":      PURPLE_BG,
        "tag":     "GLOBAL MEMORY",
        "tag_col": PURPLE,
        "desc":    [
            "int sq = 0  goes into the DATA SEGMENT",
            "of the process — shared memory visible",
            "to ALL threads. Both threads will use",
            "this as their communication channel.",
        ],
        "scene":   "global",
    },
    {
        "title":   "Step 2 — main() Starts",
        "line":    9,
        "color":   TEAL,
        "bg":      TEAL_BG,
        "tag":     "1 THREAD",
        "tag_col": TEAL,
        "desc":    [
            "OS creates the main thread automatically.",
            "pthread_t tid  is just a variable to hold",
            "the new thread's ID (like a name tag).",
            "Only ONE thread exists right now.",
        ],
        "scene":   "one_thread",
    },
    {
        "title":   "Step 3 — scanf Blocks",
        "line":    13,
        "color":   AMBER,
        "bg":      AMBER_BG,
        "tag":     "BLOCKED",
        "tag_col": AMBER,
        "desc":    [
            "Main thread PAUSES waiting for input.",
            "User types: 5",
            "n = 5 is stored on main thread's stack.",
            "&n  = address pointing to where 5 lives.",
        ],
        "scene":   "scanf",
    },
    {
        "title":   "Step 4 — pthread_create!",
        "line":    14,
        "color":   CORAL,
        "bg":      CORAL_BG,
        "tag":     "KEY MOMENT",
        "tag_col": CORAL,
        "desc":    [
            "OS does 5 things instantly:",
            "  1. Allocates new stack for new thread",
            "  2. Creates Thread Control Block (TCB)",
            "  3. Sets start function → calc_sq()",
            "  4. Passes &n as argument",
            "  5. Writes thread ID into tid",
            "NOW TWO THREADS RUN IN PARALLEL!",
        ],
        "scene":   "two_threads",
    },
    {
        "title":   "Step 5 — Dereference Pointer",
        "line":    3,
        "color":   PURPLE,
        "bg":      PURPLE_BG,
        "tag":     "NEW THREAD",
        "tag_col": PURPLE,
        "desc":    [
            "New thread gets ptr = &n (address of n).",
            "*(int*) ptr  dereferences it to read 5.",
            "val = 5 is copied to new thread's OWN",
            "stack — separate from main's stack.",
        ],
        "scene":   "deref",
    },
    {
        "title":   "Step 6 — Compute & Write Shared",
        "line":    4,
        "color":   CORAL,
        "bg":      CORAL_BG,
        "tag":     "SHARED WRITE",
        "tag_col": CORAL,
        "desc":    [
            "val * val = 5 × 5 = 25",
            "sq = 25  written to GLOBAL shared memory.",
            "Main thread can now see this change too!",
            "This is inter-thread communication.",
        ],
        "scene":   "write_shared",
    },
    {
        "title":   "Step 7 — New Thread Exits",
        "line":    6,
        "color":   RED,
        "bg":      RED_BG,
        "tag":     "THREAD EXIT",
        "tag_col": RED,
        "desc":    [
            "printf prints: 'In new thread, sq = 25'",
            "pthread_exit(0) terminates the thread.",
            "Its stack is DESTROYED, resources freed.",
            "Exit code 0 is stored for pthread_join.",
        ],
        "scene":   "thread_exit",
    },
    {
        "title":   "Step 8 — pthread_join Unblocks",
        "line":    15,
        "color":   TEAL,
        "bg":      TEAL_BG,
        "tag":     "SYNC POINT",
        "tag_col": TEAL,
        "desc":    [
            "pthread_join blocked main since Step 4.",
            "New thread finished → join() returns!",
            "Main resumes. This GUARANTEES ordering:",
            "main reads sq ONLY AFTER it's written.",
        ],
        "scene":   "join",
    },
    {
        "title":   "Step 9 — Main Reads & Exits",
        "line":    16,
        "color":   GREEN,
        "bg":      GREEN_BG,
        "tag":     "DONE",
        "tag_col": GREEN,
        "desc":    [
            "main reads sq = 25 from shared memory.",
            "Prints: 'In original thread, sq = 25'",
            "return 0  ends the entire process.",
            "Both threads done. Program complete!",
        ],
        "scene":   "done",
    },
]

# ── Animation state ────────────────────────────────────────────────────────
current_step = 0
anim_t       = 0.0        # 0→1 transition progress
transitioning= False
arrow_pulse  = 0.0
particle_t   = 0.0

# ── Helpers ────────────────────────────────────────────────────────────────
def lerp(a, b, t):
    return a + (b - a) * t

def ease_out(t):
    return 1 - (1 - t) ** 3

def ease_in_out(t):
    return t * t * (3 - 2 * t)

def draw_rect_rounded(surf, color, rect, radius=8, border=0, border_color=None):
    pygame.draw.rect(surf, color, rect, border_radius=radius)
    if border > 0 and border_color:
        pygame.draw.rect(surf, border_color, rect, border, border_radius=radius)

def draw_text(surf, text, font, color, x, y, anchor="topleft"):
    s = font.render(text, True, color)
    r = s.get_rect()
    setattr(r, anchor, (x, y))
    surf.blit(s, r)
    return r

def draw_text_wrapped(surf, lines, font, color, x, y, line_h=22):
    for i, line in enumerate(lines):
        draw_text(surf, line, font, color, x, y + i * line_h)

def draw_arrow(surf, color, start, end, width=2, head=10):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    dist = math.hypot(dx, dy)
    if dist < 1:
        return
    ux, uy = dx/dist, dy/dist
    # shaft
    pygame.draw.line(surf, color, start, (end[0]-ux*head*0.7, end[1]-uy*head*0.7), width)
    # head
    lx = -uy * head * 0.5
    ly =  ux * head * 0.5
    tip = end
    left  = (end[0]-ux*head+lx, end[1]-uy*head+ly)
    right = (end[0]-ux*head-lx, end[1]-uy*head-ly)
    pygame.draw.polygon(surf, color, [tip, left, right])

def glowing_rect(surf, color, rect, radius=10, alpha=60):
    glow = pygame.Surface((rect[2]+20, rect[3]+20), pygame.SRCALPHA)
    c = (*color[:3], alpha)
    pygame.draw.rect(glow, c, (10,10,rect[2],rect[3]), border_radius=radius+4)
    surf.blit(glow, (rect[0]-10, rect[1]-10))

def pulse_alpha(base, amp, speed, t):
    return int(base + amp * math.sin(t * speed))

# ── Draw code panel (left side) ────────────────────────────────────────────
CODE_X, CODE_Y = 20, 100
CODE_W, CODE_H = 390, 560
LINE_H = 26

def draw_code_panel(step_idx):
    active_line = STEPS[step_idx]["line"]
    color_hl    = STEPS[step_idx]["color"]
    bg_hl       = STEPS[step_idx]["bg"]

    # Panel background
    draw_rect_rounded(screen, PANEL, (CODE_X, CODE_Y, CODE_W, CODE_H), 12)
    draw_rect_rounded(screen, BORDER, (CODE_X, CODE_Y, CODE_W, CODE_H), 12, 1, BORDER)

    # Header bar
    draw_rect_rounded(screen, PANEL2, (CODE_X, CODE_Y, CODE_W, 36), 12)
    pygame.draw.rect(screen, PANEL2, (CODE_X, CODE_Y+20, CODE_W, 16))
    draw_text(screen, "pthread_demo.c", FONT_MD_B, GRAY, CODE_X+14, CODE_Y+10)

    # Determine "done" lines
    done_lines = set()
    if step_idx >= 1:  done_lines.add(0)
    if step_idx >= 2:  done_lines.update([9,10,11,12])
    if step_idx >= 3:  done_lines.update([13])
    if step_idx >= 4:  done_lines.update([14])
    if step_idx >= 5:  done_lines.update([2,3])
    if step_idx >= 6:  done_lines.update([4,5])
    if step_idx >= 7:  done_lines.update([6,7])
    if step_idx >= 8:  done_lines.update([15])
    if step_idx >= 9:  done_lines.update([16,17,18])

    for i, (line_text, line_type) in enumerate(CODE_LINES):
        lx = CODE_X + 12
        ly = CODE_Y + 44 + i * LINE_H
        lw = CODE_W - 24
        lh = LINE_H - 2

        if i == active_line:
            # Active highlight with glow
            draw_rect_rounded(screen, bg_hl, (lx-4, ly, lw+8, lh), 6)
            draw_rect_rounded(screen, color_hl, (lx-4, ly, 3, lh), 2)
            glowing_rect(screen, color_hl, (lx-4, ly, lw+8, lh), 6, 30)
        elif i in done_lines:
            draw_rect_rounded(screen, CODE_DONE, (lx-4, ly, lw+8, lh), 4)

        # Line number
        ln_color = color_hl if i == active_line else MUTED
        draw_text(screen, f"{i+1:2d}", FONT_MONO, ln_color, lx, ly+5)

        # Code text color
        if i == active_line:
            txt_color = WHITE
        elif i in done_lines:
            txt_color = TEAL
        elif line_type == "key":
            txt_color = AMBER
        elif line_type in ("fn_head", "main_head"):
            txt_color = PURPLE
        elif line_type == "global":
            txt_color = CORAL
        else:
            txt_color = GRAY

        if line_text:
            draw_text(screen, line_text, FONT_MONO, txt_color, lx+26, ly+5)

# ── Scene renderers ─────────────────────────────────────────────────────────
SX = 440   # scene area start x
SW = W - SX - 20
SY = 100
SH = 560

def scene_base():
    draw_rect_rounded(screen, PANEL, (SX, SY, SW, SH), 12)
    draw_rect_rounded(screen, BORDER, (SX, SY, SW, SH), 12, 1, BORDER)

def draw_memory_box(x, y, w, h, title, items, color, bg_color, val_overrides=None):
    draw_rect_rounded(screen, bg_color, (x, y, w, h), 10)
    draw_rect_rounded(screen, color, (x, y, w, h), 10, 1, color)
    # Title bar
    draw_rect_rounded(screen, color, (x, y, w, 28), 10)
    pygame.draw.rect(screen, color, (x, y+14, w, 14))
    draw_text(screen, title, FONT_MD_B, (10,10,20), x + w//2, y+14, anchor="center")
    for i, item in enumerate(items):
        iy = y + 36 + i * 24
        if val_overrides and item[0] in val_overrides:
            val = val_overrides[item[0]]
            draw_text(screen, item[0], FONT_MD, GRAY, x+12, iy)
            draw_text(screen, "=", FONT_MD, MUTED, x+60, iy)
            draw_text(screen, str(val), FONT_MD_B, color, x+76, iy)
        else:
            draw_text(screen, item[0], FONT_MD, GRAY, x+12, iy)
            draw_text(screen, "=", FONT_MD, MUTED, x+60, iy)
            draw_text(screen, item[1], FONT_MD_B, GRAY, x+76, iy)

def draw_shared_mem(x, y, sq_val, highlight=False, pulse=0):
    w, h = 260, 80
    col   = CORAL if not highlight else WHITE
    bg    = (40, 20, 15) if not highlight else CORAL_BG
    alpha = pulse_alpha(80, 40, 3, pulse) if highlight else 80
    if highlight:
        glowing_rect(screen, CORAL, (x,y,w,h), 10, alpha)
    draw_rect_rounded(screen, bg, (x,y,w,h), 10)
    draw_rect_rounded(screen, CORAL, (x,y,w,h), 10, 1, CORAL)
    draw_rect_rounded(screen, CORAL_DARK, (x,y,w,28), 10)
    pygame.draw.rect(screen, CORAL_DARK, (x,y+14,w,14))
    draw_text(screen, "SHARED MEMORY (Global)", FONT_MD_B, (255,200,180), x+w//2, y+14, anchor="center")
    sq_color = GREEN if highlight else AMBER
    draw_text(screen, "sq", FONT_MD_B, GRAY, x+18, y+38)
    draw_text(screen, "=", FONT_MD, MUTED, x+50, y+38)
    sv = str(sq_val)
    draw_text(screen, sv, FONT_XL, sq_color, x+70, y+32)
    draw_text(screen, "← both threads can see this", FONT_SM, MUTED, x+18, y+58)

def draw_thread_box(x, y, w, h, title, lines, color, bg, active=True, fading=False):
    alpha_mod = 80 if fading else 255
    s = pygame.Surface((w,h), pygame.SRCALPHA)
    bg_a   = (*bg[:3],   alpha_mod)
    col_a  = (*color[:3], alpha_mod)
    pygame.draw.rect(s, bg_a,  (0,0,w,h), border_radius=10)
    pygame.draw.rect(s, col_a, (0,0,w,h), 1, border_radius=10)
    pygame.draw.rect(s, col_a, (0,0,w,28), border_radius=10)
    pygame.draw.rect(s, col_a, (0,14,w,14))
    screen.blit(s, (x,y))
    txt_col = (10,10,20) if not fading else (80,80,100)
    draw_text(screen, title, FONT_MD_B, txt_col if not fading else MUTED, x+w//2, y+14, anchor="center")
    for i, (label, val, vc) in enumerate(lines):
        ly = y + 36 + i * 22
        vc2 = vc if not fading else MUTED
        draw_text(screen, label, FONT_SM, GRAY if not fading else MUTED, x+10, ly)
        draw_text(screen, "=", FONT_SM, MUTED, x+70, ly)
        draw_text(screen, val, FONT_MD_B, vc2, x+88, ly)
    if active and not fading:
        # Running indicator
        r = 5
        cx2, cy2 = x+w-14, y+14
        pygame.draw.circle(screen, GREEN, (cx2,cy2), r)

# ── Individual scenes ────────────────────────────────────────────────────────

def scene_global(t, pulse):
    scene_base()
    draw_text(screen, "Process Memory Layout", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    # Process container
    px, py, pw, ph = SX+30, SY+55, SW-60, SH-80
    draw_rect_rounded(screen, (20,22,40), (px,py,pw,ph), 14)
    draw_rect_rounded(screen, PURPLE_DARK, (px,py,pw,ph), 14, 1, PURPLE_DARK)
    draw_text(screen, "PROCESS", FONT_SM, PURPLE, px+10, py+8)

    # Global memory — highlighted
    gx, gy = px+pw//2-130, py+40
    glowing_rect(screen, CORAL, (gx,gy,260,90), 10, pulse_alpha(60,40,2.5,pulse))
    draw_rect_rounded(screen, CORAL_BG, (gx,gy,260,90), 10)
    draw_rect_rounded(screen, CORAL, (gx,gy,260,90), 10, 2, CORAL)
    draw_rect_rounded(screen, CORAL_DARK, (gx,gy,260,30), 10)
    pygame.draw.rect(screen, CORAL_DARK, (gx,gy+16,260,14))
    draw_text(screen, "Data Segment (Global)", FONT_MD_B, (255,200,180), gx+130, gy+15, anchor="center")

    sq_scale = ease_out(min(t*2, 1))
    sq_size  = int(lerp(12, 32, sq_scale))
    try:
        f = pygame.font.SysFont("sans-serif", sq_size, bold=True)
    except:
        f = FONT_XL
    draw_text(screen, "sq", FONT_MD_B, GRAY, gx+20, gy+40)
    draw_text(screen, "=", FONT_MD, MUTED, gx+52, gy+40)
    draw_text(screen, "0", f, CORAL, gx+72, gy+33)
    draw_text(screen, "← visible to ALL threads", FONT_SM, MUTED, gx+20, gy+65)

    # Stack areas (ghosted)
    for i, (lbl, col) in enumerate([("Main Thread Stack", TEAL_DARK),("New Thread Stack", PURPLE_DARK)]):
        bx = px+40 + i*(pw//2-20)
        by = py+160
        draw_rect_rounded(screen, (22,25,42), (bx,by,pw//2-60,100), 8)
        draw_rect_rounded(screen, col, (bx,by,pw//2-60,100), 8, 1, col)
        draw_text(screen, lbl, FONT_SM, col, bx+(pw//2-60)//2, by+46, anchor="center")
        draw_text(screen, "(empty for now)", FONT_SM, MUTED, bx+(pw//2-60)//2, by+66, anchor="center")

    # Bottom explanation
    draw_text(screen, "int sq = 0  is placed in the DATA SEGMENT — shared by all threads", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_one_thread(t, pulse):
    scene_base()
    draw_text(screen, "Process starts — 1 thread only", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    cx = SX + SW//2
    # Single thread box
    bw, bh = 300, 180
    bx, by = cx - bw//2, SY + 60
    alpha = int(ease_out(t) * 255)
    surf = pygame.Surface((bw,bh), pygame.SRCALPHA)
    pygame.draw.rect(surf, (*TEAL_BG, alpha), (0,0,bw,bh), border_radius=10)
    pygame.draw.rect(surf, (*TEAL, alpha), (0,0,bw,bh), 2, border_radius=10)
    pygame.draw.rect(surf, (*TEAL_DARK, alpha), (0,0,bw,28), border_radius=10)
    pygame.draw.rect(surf, (*TEAL_DARK, alpha), (0,14,bw,14))
    screen.blit(surf, (bx,by))
    draw_text(screen, "Main Thread", FONT_LG, (10,10,20), bx+bw//2, by+14, anchor="center")
    pygame.draw.circle(screen, GREEN, (bx+bw-14, by+14), 6)

    items = [
        ("tid",       "unset",   MUTED),
        ("n",         "unset",   MUTED),
        ("PC",        "main()",  TEAL),
        ("Status",    "RUNNING", GREEN),
    ]
    for i,(lbl,val,vc) in enumerate(items):
        ly = by + 36 + i * 28
        draw_text(screen, lbl, FONT_MD, GRAY, bx+14, ly)
        draw_text(screen, ":", FONT_MD, MUTED, bx+54, ly)
        draw_text(screen, val, FONT_MD_B, vc, bx+70, ly)

    # Arrow from OS to thread
    ox, oy = cx, SY + 290
    draw_text(screen, "OS Scheduler", FONT_SM, MUTED, ox, oy, anchor="center")
    draw_arrow(screen, TEAL, (ox, oy-16), (bx+bw//2, by+bh+2), 2, 8)

    # Shared mem — small
    draw_shared_mem(SX + SW//2 - 130, SY + 340, 0)
    draw_text(screen, "1 thread — NO parallelism yet", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_scanf(t, pulse):
    scene_base()
    draw_text(screen, "scanf() — main thread blocks", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    # Main thread (blocked / amber)
    bx,by,bw,bh = SX+SW//2-150, SY+55, 300, 160
    draw_rect_rounded(screen, AMBER_BG, (bx,by,bw,bh), 10)
    draw_rect_rounded(screen, AMBER, (bx,by,bw,bh), 10, 2, AMBER)
    draw_rect_rounded(screen, AMBER_DARK, (bx,by,bw,28), 10)
    pygame.draw.rect(screen, AMBER_DARK, (bx,by+14,bw,14))
    draw_text(screen, "Main Thread", FONT_LG, (10,10,20), bx+bw//2, by+14, anchor="center")
    # Waiting spinner
    angle = (pulse * 60) % 360
    cx2,cy2 = bx+bw-18, by+14
    for i in range(8):
        a = math.radians(angle + i*45)
        r2 = 7
        px2 = cx2 + int(r2 * math.cos(a))
        py2 = cy2 + int(r2 * math.sin(a))
        al = int(255 * (i+1)/8)
        pygame.draw.circle(screen, (*AMBER, al), (px2,py2), 2)

    lines = [("PC","scanf()",AMBER),("Status","WAITING...",AMBER),("n","???",MUTED)]
    for i,(lbl,val,vc) in enumerate(lines):
        ly = by+38+i*28
        draw_text(screen, lbl, FONT_MD, GRAY, bx+14, ly)
        draw_text(screen, ":", FONT_MD, MUTED, bx+54, ly)
        draw_text(screen, val, FONT_MD_B, vc, bx+70, ly)

    # Keyboard input arrow
    ky = by + bh + 30
    draw_rect_rounded(screen, (25,25,35), (SX+SW//2-80, ky, 160, 44), 8)
    draw_rect_rounded(screen, AMBER_DARK, (SX+SW//2-80, ky, 160, 44), 8, 1, AMBER_DARK)
    draw_text(screen, "keyboard: 5", FONT_MD_B, AMBER, SX+SW//2, ky+22, anchor="center")
    draw_arrow(screen, AMBER, (SX+SW//2, ky+44+2), (bx+bw//2, by+bh-2), 2, 8)

    # Stack showing n=5 appearing
    n_alpha = ease_out(min(t*3,1))
    nx, ny = SX+SW//2-130, ky+70
    draw_rect_rounded(screen, TEAL_BG, (nx,ny,260,70), 8)
    draw_rect_rounded(screen, TEAL_DARK, (nx,ny,260,70), 8, 1, TEAL_DARK)
    draw_text(screen, "main stack:", FONT_SM, GRAY, nx+10, ny+8)
    col_n = (*TEAL, int(n_alpha*255))
    s2 = pygame.Surface((200,30), pygame.SRCALPHA)
    f = FONT_MD_B.render("n = 5   &n = 0xFF42A0", True, TEAL)
    s2.blit(f,(0,0))
    s2.set_alpha(int(n_alpha*255))
    screen.blit(s2,(nx+10,ny+32))

    draw_text(screen, "Main thread BLOCKED until user presses Enter", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_two_threads(t, pulse):
    scene_base()
    draw_text(screen, "pthread_create — TWO threads now!", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    prog = ease_out(min(t*1.5, 1))

    # Main thread (left)
    mx,my,mw,mh = SX+35, SY+65, 220, 175
    draw_rect_rounded(screen, TEAL_BG, (mx,my,mw,mh), 10)
    draw_rect_rounded(screen, TEAL, (mx,my,mw,mh), 10, 2, TEAL)
    draw_rect_rounded(screen, TEAL_DARK, (mx,my,mw,28), 10)
    pygame.draw.rect(screen, TEAL_DARK, (mx,my+14,mw,14))
    draw_text(screen, "Main Thread", FONT_MD_B, (10,10,20), mx+mw//2, my+14, anchor="center")
    # blocked indicator
    angle = (pulse * 60) % 360
    for i in range(8):
        a = math.radians(angle + i*45)
        r2 = 6
        px2 = mx+mw-14 + int(r2*math.cos(a))
        py2 = my+14    + int(r2*math.sin(a))
        al = int(255*(i+1)/8)
        pygame.draw.circle(screen, (*AMBER[:3], al), (px2,py2), 2)
    for i,(lbl,val,vc) in enumerate([("tid",f"T{id(1)%999}",TEAL),("n","5",TEAL),("PC","pthread_join",AMBER),("Status","WAITING",AMBER)]):
        ly = my+36+i*26
        draw_text(screen, lbl, FONT_SM, GRAY, mx+10, ly)
        draw_text(screen, ":", FONT_SM, MUTED, mx+48, ly)
        draw_text(screen, val, FONT_MD_B, vc, mx+62, ly)

    # New thread (right) — slides in
    slide_x = int(lerp(SX+SW, SX+SW-255, prog))
    nx,ny,nw,nh = slide_x, SY+65, 220, 175
    if prog > 0.05:
        draw_rect_rounded(screen, PURPLE_BG, (nx,ny,nw,nh), 10)
        draw_rect_rounded(screen, PURPLE, (nx,ny,nw,nh), 10, 2, PURPLE)
        draw_rect_rounded(screen, PURPLE_DARK, (nx,ny,nw,28), 10)
        pygame.draw.rect(screen, PURPLE_DARK, (nx,ny+14,nw,14))
        draw_text(screen, "New Thread", FONT_MD_B, (10,10,20), nx+nw//2, ny+14, anchor="center")
        pygame.draw.circle(screen, GREEN, (nx+nw-14, ny+14), 6)
        for i,(lbl,val,vc) in enumerate([("ptr","&n=0xFF42",PURPLE),("PC","calc_sq()",PURPLE),("stack","new alloc",GREEN),("Status","RUNNING",GREEN)]):
            ly = ny+36+i*26
            draw_text(screen, lbl, FONT_SM, GRAY, nx+10, ly)
            draw_text(screen, ":", FONT_SM, MUTED, nx+48, ly)
            draw_text(screen, val, FONT_MD_B, vc, nx+62, ly)

    # Shared memory
    draw_shared_mem(SX+SW//2-130, SY+270, 0, False, pulse)

    # Arrows from threads to shared mem
    mem_top_y = SY+270
    draw_arrow(screen, TEAL,   (mx+mw//2, my+mh+2),  (SX+SW//2-50,  mem_top_y-2), 1, 6)
    if prog > 0.3:
        draw_arrow(screen, PURPLE, (nx+nw//2, ny+nh+2), (SX+SW//2+50,  mem_top_y-2), 1, 6)

    # "BORN" label
    if prog > 0.5:
        ba = int(ease_out((prog-0.5)*2)*255)
        born_surf = FONT_LG.render("NEW THREAD BORN!", True, (*CORAL[:3],))
        born_surf.set_alpha(ba)
        screen.blit(born_surf, (nx+nw//2-born_surf.get_width()//2, ny+nh+8))

    draw_text(screen, "Both threads run in PARALLEL from this point", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_deref(t, pulse):
    scene_base()
    draw_text(screen, "New thread dereferences the pointer", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    # Main stack (left, faded)
    mx,my = SX+30, SY+60
    draw_rect_rounded(screen, (20,40,35), (mx,my,190,140), 10)
    draw_rect_rounded(screen, TEAL_DARK, (mx,my,190,140), 10, 1, TEAL_DARK)
    draw_rect_rounded(screen, TEAL_DARK, (mx,my,190,28), 10)
    pygame.draw.rect(screen, TEAL_DARK, (mx,my+14,190,14))
    draw_text(screen, "Main Stack", FONT_MD_B, MUTED, mx+95, my+14, anchor="center")
    draw_text(screen, "n", FONT_MD, GRAY, mx+14, my+40)
    draw_text(screen, "=", FONT_MD, MUTED, mx+38, my+40)
    draw_text(screen, "5", FONT_MD_B, TEAL, mx+56, my+40)
    draw_text(screen, "Address: 0xFF42A0", FONT_SM, MUTED, mx+14, my+65)
    draw_text(screen, "(waiting in join)", FONT_SM, AMBER, mx+14, my+95)
    draw_text(screen, "BLOCKED", FONT_SM, AMBER, mx+14, my+112)

    # Pointer arrow
    arrow_prog = ease_out(min(t*2,1))
    ax1, ay1 = SX+SW-215, SY+90
    ax2, ay2 = mx+190, my+46
    if arrow_prog > 0.1:
        mid_x = (ax1+ax2)//2
        pts = [(ax1,ay1),(mid_x-20,ay1),(mid_x-20,ay2),(ax2,ay2)]
        for i in range(len(pts)-1):
            p1 = pts[i]; p2 = pts[i+1]
            draw_arrow(screen, PURPLE, p1, p2, 2, 7)

    # New thread stack (right)
    nx, ny = SX+SW-220, SY+55
    nw, nh = 200, 215
    draw_rect_rounded(screen, PURPLE_BG, (nx,ny,nw,nh), 10)
    draw_rect_rounded(screen, PURPLE, (nx,ny,nw,nh), 10, 2, PURPLE)
    draw_rect_rounded(screen, PURPLE_DARK, (nx,ny,nw,28), 10)
    pygame.draw.rect(screen, PURPLE_DARK, (nx,ny+14,nw,14))
    draw_text(screen, "New Thread Stack", FONT_MD_B, (10,10,20), nx+nw//2, ny+14, anchor="center")
    pygame.draw.circle(screen, GREEN, (nx+nw-14, ny+14), 6)

    draw_text(screen, "ptr",  FONT_MD, GRAY,   nx+12, ny+38)
    draw_text(screen, "=",   FONT_MD, MUTED,  nx+46, ny+38)
    draw_text(screen, "0xFF42A0", FONT_MD_B, PURPLE, nx+62, ny+38)

    # val appearing
    val_alpha = ease_out(min(t*3,1))
    draw_text(screen, "*(int*)ptr", FONT_SM, MUTED, nx+12, ny+68)
    draw_text(screen, "= read value at address →", FONT_SM, MUTED, nx+12, ny+84)

    s2 = pygame.Surface((180,30), pygame.SRCALPHA)
    f = FONT_MD_B.render("val = 5", True, (*GREEN,))
    s2.blit(f,(0,0))
    s2.set_alpha(int(val_alpha*255))
    screen.blit(s2,(nx+12,ny+108))

    draw_text(screen, "val is on new thread's OWN stack", FONT_SM, PURPLE, nx+12, ny+145)
    draw_text(screen, "(separate from main's n)", FONT_SM, MUTED, nx+12, ny+162)

    draw_shared_mem(SX+40, SY+300, 0)
    draw_text(screen, "Pointer lets threads share data across stack boundaries", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_write_shared(t, pulse):
    scene_base()
    draw_text(screen, "sq = val * val  — writing to shared memory", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    prog = ease_out(min(t*2, 1))
    sq_val = int(lerp(0, 25, prog))

    # New thread
    nx,ny = SX+SW-215, SY+60
    draw_rect_rounded(screen, PURPLE_BG, (nx,ny,195,160), 10)
    draw_rect_rounded(screen, PURPLE, (nx,ny,195,160), 10, 2, PURPLE)
    draw_rect_rounded(screen, PURPLE_DARK, (nx,ny,195,28), 10)
    pygame.draw.rect(screen, PURPLE_DARK, (nx,ny+14,195,14))
    draw_text(screen, "New Thread", FONT_MD_B, (10,10,20), nx+98, ny+14, anchor="center")
    pygame.draw.circle(screen, GREEN, (nx+195-14, ny+14), 6)
    draw_text(screen, "val", FONT_MD, GRAY, nx+12, ny+38)
    draw_text(screen, "=", FONT_MD, MUTED, nx+46, ny+38)
    draw_text(screen, "5", FONT_MD_B, PURPLE, nx+64, ny+38)
    draw_text(screen, "val * val", FONT_MD_B, CORAL, nx+12, ny+64)
    draw_text(screen, "= 5 × 5 = 25", FONT_MD_B, CORAL, nx+12, ny+84)

    # Write arrow
    if prog > 0.1:
        ax1,ay1 = nx+30, ny+160
        ax2,ay2 = SX+SW//2-50, SY+310
        draw_arrow(screen, CORAL, (ax1,ay1), (ax2,ay2), 2, 8)
        draw_text(screen, "writes 25", FONT_SM, CORAL, (ax1+ax2)//2-10, (ay1+ay2)//2-12)

    # Shared mem — pulsing with new value
    hl = prog > 0.3
    draw_shared_mem(SX+30, SY+300, sq_val, highlight=hl, pulse=pulse)

    # Main thread sees it too
    if prog > 0.6:
        ma = int(ease_out((prog-0.6)/0.4)*255)
        s = FONT_SM.render("Main thread will see sq=25 too!", True, (*TEAL,))
        s.set_alpha(ma)
        screen.blit(s, (SX+30, SY+415))
        draw_arrow(screen, TEAL, (SX+30, SY+300+40), (SX+30, SY+412), 1, 6)

    draw_text(screen, "Global variable = inter-thread communication channel", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_thread_exit(t, pulse):
    scene_base()
    draw_text(screen, "pthread_exit(0) — new thread terminates", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    prog = ease_out(min(t*2,1))
    fade = 1.0 - ease_out(min(max(t-0.3,0)*2,1))

    # New thread fading out
    alpha = int(fade * 200)
    nx,ny = SX+SW//2+10, SY+65
    if alpha > 10:
        s = pygame.Surface((200,165), pygame.SRCALPHA)
        pygame.draw.rect(s, (*RED_BG, alpha), (0,0,200,165), border_radius=10)
        pygame.draw.rect(s, (*RED[:3], alpha), (0,0,200,165), 2, border_radius=10)
        pygame.draw.rect(s, (*RED[:3], alpha), (0,0,200,28), border_radius=10)
        pygame.draw.rect(s, (*RED[:3], alpha), (0,14,200,14))
        screen.blit(s, (nx,ny))
        f = FONT_MD_B.render("New Thread", True, (10,10,20))
        f.set_alpha(alpha)
        screen.blit(f, (nx+100-f.get_width()//2, ny+8))
        for i,(lbl,val,vc) in enumerate([("sq","25",CORAL),("exit","0",RED),("stack","FREED",RED)]):
            ly = ny+36+i*28
            f2 = FONT_SM.render(f"{lbl} : {val}", True, (*vc,))
            f2.set_alpha(alpha)
            screen.blit(f2,(nx+12,ly))

    # X mark
    if t > 0.4:
        xa = int(ease_out(min((t-0.4)*3,1))*200)
        xs = FONT_XL.render("✕ TERMINATED", True, (*RED[:3],))
        xs.set_alpha(xa)
        screen.blit(xs, (nx+100-xs.get_width()//2, ny+170))

    # Main thread — still blocked
    mx,my = SX+30, SY+65
    draw_rect_rounded(screen, AMBER_BG, (mx,my,210,165), 10)
    draw_rect_rounded(screen, AMBER, (mx,my,210,165), 10, 2, AMBER)
    draw_rect_rounded(screen, AMBER_DARK, (mx,my,210,28), 10)
    pygame.draw.rect(screen, AMBER_DARK, (mx,my+14,210,14))
    draw_text(screen, "Main Thread", FONT_MD_B, (10,10,20), mx+105, my+14, anchor="center")
    angle = (pulse*60)%360
    for i in range(8):
        a = math.radians(angle+i*45)
        r2=6; px2=mx+210-14+int(r2*math.cos(a)); py2=my+14+int(r2*math.sin(a))
        pygame.draw.circle(screen, (*AMBER[:3],int(255*(i+1)/8)),(px2,py2),2)
    draw_text(screen, "pthread_join()",FONT_MD_B, AMBER, mx+14, my+40)
    draw_text(screen, "WAITING for new thread...", FONT_SM, AMBER, mx+14, my+65)
    draw_text(screen, "will unblock soon!", FONT_SM, GREEN, mx+14, my+85)

    draw_shared_mem(SX+SW//2-130, SY+300, 25, True, pulse)
    draw_text(screen, "New thread stack is DESTROYED — sq=25 lives on in shared memory", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_join(t, pulse):
    scene_base()
    draw_text(screen, "pthread_join returns — main unblocks!", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    prog = ease_out(min(t*2, 1))

    # Dead thread (ghost)
    nx,ny = SX+SW-215, SY+65
    draw_rect_rounded(screen, (18,18,28), (nx,ny,200,140), 10)
    draw_rect_rounded(screen, GRAY_DARK, (nx,ny,200,140), 10, 1, GRAY_DARK)
    draw_text(screen, "New Thread", FONT_MD_B, MUTED, nx+100, ny+14, anchor="center")
    draw_text(screen, "[TERMINATED]", FONT_SM, MUTED, nx+100, ny+55, anchor="center")
    draw_text(screen, "exit code: 0", FONT_SM, GRAY_DARK, nx+100, ny+75, anchor="center")

    # Main thread — waking up
    mx,my = SX+30, SY+55
    mw,mh = 220, 185
    draw_rect_rounded(screen, TEAL_BG, (mx,my,mw,mh), 10)
    draw_rect_rounded(screen, TEAL, (mx,my,mw,mh), 10, 2, TEAL)
    draw_rect_rounded(screen, TEAL_DARK, (mx,my,mw,28), 10)
    pygame.draw.rect(screen, TEAL_DARK, (mx,my+14,mw,14))
    draw_text(screen, "Main Thread", FONT_MD_B, (10,10,20), mx+mw//2, my+14, anchor="center")
    pygame.draw.circle(screen, GREEN, (mx+mw-14, my+14), 6)

    status = "UNBLOCKED!" if prog > 0.5 else "WAKING UP..."
    sc     = GREEN if prog > 0.5 else AMBER
    draw_text(screen, "pthread_join returned", FONT_SM, TEAL, mx+14, my+38)
    draw_text(screen, status, FONT_MD_B, sc, mx+14, my+60)
    draw_text(screen, "Can now safely read sq", FONT_SM, GREEN, mx+14, my+85)
    draw_text(screen, "because new thread", FONT_SM, GREEN, mx+14, my+103)
    draw_text(screen, "already wrote it!", FONT_SM, GREEN, mx+14, my+121)

    # Unlock animation
    if prog > 0.3:
        unlock_a = int(ease_out((prog-0.3)/0.7)*255)
        us = FONT_LG.render("UNLOCKED", True, (*GREEN,))
        us.set_alpha(unlock_a)
        screen.blit(us, (mx+mw//2-us.get_width()//2, my+mh+8))

    draw_shared_mem(SX+SW//2-130, SY+310, 25, True, pulse)
    draw_text(screen, "pthread_join = synchronization gate — guarantees correct ordering", FONT_SM, AMBER, SX+SW//2, SY+SH-30, anchor="center")

def scene_done(t, pulse):
    scene_base()
    draw_text(screen, "Program complete!", FONT_LG, WHITE, SX+SW//2, SY+22, anchor="center")

    prog = ease_out(min(t*1.5, 1))

    # Terminal output box
    tx,ty = SX+30, SY+55
    tw,th = SW-60, 160
    draw_rect_rounded(screen, (8,12,10), (tx,ty,tw,th), 10)
    draw_rect_rounded(screen, GREEN, (tx,ty,tw,th), 10, 1, GREEN)
    draw_rect_rounded(screen, (15,30,15), (tx,ty,tw,28), 10)
    pygame.draw.rect(screen, (15,30,15), (tx,ty+14,tw,14))
    draw_text(screen, "terminal output", FONT_MD_B, GREEN, tx+14, ty+14)
    draw_text(screen, "$ ./pthread_demo", FONT_MONO, GRAY, tx+14, ty+36)
    draw_text(screen, "Enter the number: 5", FONT_MONO, GRAY, tx+14, ty+56)
    if prog > 0.3:
        draw_text(screen, "In the new thread,   sq = 25", FONT_MONO_B, GREEN, tx+14, ty+76)
    if prog > 0.6:
        draw_text(screen, "IN the original thread, sq = 25", FONT_MONO_B, (130,220,255), tx+14, ty+98)

    # Final memory state
    draw_shared_mem(SX+30, SY+240, 25, True, pulse)

    # Summary
    sy2 = SY+360
    draw_text(screen, "What happened:", FONT_MD_B, WHITE, SX+30, sy2)
    summaries = [
        (TEAL,   "1. main created new thread via pthread_create"),
        (PURPLE, "2. New thread computed sq = 5×5 = 25 in shared memory"),
        (CORAL,  "3. pthread_join ensured ordering (main waited)"),
        (GREEN,  "4. Both threads read sq = 25 correctly"),
    ]
    for i,(col,txt) in enumerate(summaries):
        a = int(ease_out(min(max(t - 0.3 - i*0.15, 0)*3, 1))*255)
        s = FONT_MD.render(txt, True, (*col,))
        s.set_alpha(a)
        screen.blit(s, (SX+30, sy2+26+i*26))


SCENE_MAP = {
    "global":       scene_global,
    "one_thread":   scene_one_thread,
    "scanf":        scene_scanf,
    "two_threads":  scene_two_threads,
    "deref":        scene_deref,
    "write_shared": scene_write_shared,
    "thread_exit":  scene_thread_exit,
    "join":         scene_join,
    "done":         scene_done,
}

# ── Navigation UI ──────────────────────────────────────────────────────────
BTN_PREV = pygame.Rect(20,  H-56, 130, 40)
BTN_NEXT = pygame.Rect(160, H-56, 130, 40)

def draw_ui():
    s = STEPS[current_step]

    # Top bar
    pygame.draw.rect(screen, PANEL, (0, 0, W, 88))
    pygame.draw.line(screen, BORDER, (0, 88), (W, 88), 1)

    # Step indicator dots
    total = len(STEPS)
    dot_w = 12
    dot_gap = 6
    dots_total = total * dot_w + (total-1) * dot_gap
    dot_start_x = W//2 - dots_total//2
    for i in range(total):
        cx2 = dot_start_x + i*(dot_w+dot_gap) + dot_w//2
        col = s["color"] if i == current_step else (i < current_step and GRAY_DARK or PANEL2)
        if i == current_step:
            pygame.draw.circle(screen, col, (cx2, 18), 7)
        elif i < current_step:
            pygame.draw.circle(screen, GRAY, (cx2, 18), 5)
        else:
            pygame.draw.circle(screen, GRAY_DARK, (cx2, 18), 4)

    # Title
    draw_text(screen, s["title"], FONT_TITLE, s["color"], W//2, 44, anchor="center")

    # Tag badge
    tw2 = FONT_MD_B.size(s["tag"])[0] + 24
    tx2 = W//2 - tw2//2
    draw_rect_rounded(screen, (*s["tag_col"], 40), (tx2, 63, tw2, 22), 11)
    pygame.draw.rect(screen, s["tag_col"], (tx2, 63, tw2, 22), 1, border_radius=11)
    draw_text(screen, s["tag"], FONT_MD_B, s["tag_col"], W//2, 74, anchor="center")

    # Description panel (right-side small)
    dx, dy, dw, dh = SX, H-170, SW, 115
    draw_rect_rounded(screen, PANEL, (dx, dy, dw, dh), 10)
    draw_rect_rounded(screen, s["color"], (dx, dy, dw, dh), 10, 1, s["color"])
    draw_rect_rounded(screen, (*s["color"][:3], 40), (dx, dy, dw, 26), 10)
    pygame.draw.rect(screen, (*s["color"][:3], 40), (dx, dy+13, dw, 13))
    draw_text(screen, "What's happening", FONT_MD_B, s["color"], dx+10, dy+9)
    for i, line in enumerate(s["desc"]):
        color = WHITE if i == 0 else GRAY
        if "WARNING" in line or "DANGER" in line or "race" in line.lower():
            color = CORAL
        elif "PARALLEL" in line or "TWO" in line or "BORN" in line or "UNLOCK" in line:
            color = GREEN
        draw_text(screen, line, FONT_SM, color, dx+10, dy+30 + i*19)

    # Prev / Next buttons
    hover = pygame.mouse.get_pos()
    for btn, lbl, enabled in [(BTN_PREV, "← Prev", current_step > 0),
                               (BTN_NEXT, "Next →", current_step < len(STEPS)-1)]:
        col_bg = PANEL2 if not enabled else (PANEL2 if not btn.collidepoint(hover) else (*s["color"][:3],80))
        col_bd = GRAY_DARK if not enabled else s["color"]
        col_tx = MUTED if not enabled else (WHITE if btn.collidepoint(hover) else s["color"])
        draw_rect_rounded(screen, col_bg, btn, 8)
        draw_rect_rounded(screen, col_bd, btn, 8, 1, col_bd)
        draw_text(screen, lbl, FONT_MD_B, col_tx, btn.centerx, btn.centery, anchor="center")

    # Step counter
    draw_text(screen, f"{current_step+1} / {len(STEPS)}", FONT_MD_B, GRAY,
              BTN_NEXT.right + 20, BTN_NEXT.centery, anchor="midleft")

    # Keyboard hint
    draw_text(screen, "← → arrow keys or click buttons", FONT_SM, MUTED,
              W - 20, H-38, anchor="midright")

# ── Main loop ─────────────────────────────────────────────────────────────
scene_time = 0.0

def main():
    global current_step, anim_t, transitioning, arrow_pulse, particle_t, scene_time

    while True:
        dt = clock.tick(60) / 1000.0
        arrow_pulse  += dt
        particle_t   += dt
        scene_time   += dt

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RIGHT, pygame.K_SPACE, pygame.K_d):
                    if current_step < len(STEPS)-1:
                        current_step += 1; scene_time = 0.0
                if event.key in (pygame.K_LEFT, pygame.K_a):
                    if current_step > 0:
                        current_step -= 1; scene_time = 0.0
                if event.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BTN_NEXT.collidepoint(event.pos) and current_step < len(STEPS)-1:
                    current_step += 1; scene_time = 0.0
                if BTN_PREV.collidepoint(event.pos) and current_step > 0:
                    current_step -= 1; scene_time = 0.0

        screen.fill(BG)

        s = STEPS[current_step]
        fn = SCENE_MAP.get(s["scene"], scene_global)
        fn(scene_time, arrow_pulse)

        draw_code_panel(current_step)
        draw_ui()

        pygame.display.flip()

if __name__ == "__main__":
    main()
