#!/usr/bin/env python3
"""
Theme override definitions for Catppuccin Blur variants.

Each variant has specific color and transparency overrides to create
the blur effect while maintaining Catppuccin's color scheme.
"""

# Blur intensity levels - higher values = less transparency/more opaque
BLUR_LEVELS = {
    "light": {"main": "99", "surface": "8c", "elements": "80", "active": "90"},  # 60% opacity for main, solid for buttons
    "medium": {"main": "d7", "surface": "d0", "elements": "a0", "active": "b0"},  # 85% opacity for main, solid for buttons
    "heavy": {"main": "e0", "surface": "db", "elements": "c0", "active": "d0"},   # 88% opacity for main, solid for buttons
}

def generate_theme_overrides_for_level(base_overrides, level_config):
    """Generate theme overrides for a specific blur level."""
    overrides = base_overrides.copy()

    # Update transparency values based on blur level
    for key, value in overrides.items():
        if isinstance(value, str) and len(value) == 9 and value.startswith('#'):
            # Extract base color and replace alpha channel
            base_color = value[:7]
            if "background" in key and ("status_bar" in key or "title_bar" in key or key == "background"):
                overrides[key] = base_color + level_config["main"]
            elif "surface" in key:
                overrides[key] = base_color + level_config["surface"]
            elif any(elem in key for elem in ["drop_target", "tab.active"]):
                overrides[key] = base_color + level_config["active"]
            elif any(elem in key for elem in ["thumb", "hover", "selected"]) and "ghost_element" not in key:
                overrides[key] = base_color + level_config["elements"]
            # Note: ghost_element colors are kept as-is for solid buttons

    return overrides

# Base theme overrides (will be used to generate variants)
BASE_THEME_OVERRIDES = {
    "latte": {
        "background.appearance": "blurred",
        "background": "#f9fafcd7",
        "status_bar.background": "#e6e9efd7",
        "title_bar.background": "#e6e9efd7",
        "elevated_surface.background": "#f9fafc",
        "surface.background": "#f9fafcd0",
        # Visible thin dividers: Overlay2 at ~70% on light base.
        # Focused states use mauve (pane splits) vs sapphire (panel/terminal edge)
        # so editor | terminal | multi-terminal splits are distinguishable by hue.
        "border": "#7c7f93b3",
        "hint.background": "#e8e8e8c0",
        "editor.background": "#00000000",
        "editor.line_number": "#00000038",
        "editor.active_line_number": "#0079ff90",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle mantle scrim: terminal text stays readable over busy
        # wallpapers, and the tint gap vs the clear editor aids editor|terminal separation.
        "terminal.background": "#e6e9ef1a",
        "toolbar.background": "#00000000",
        # Mantle fill (vs transparent inactive) marks the active tab.
        "tab.active_background": "#e6e9ef60",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#209fb5cc",
        "panel.overlay_background": "#f9fafc",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 30% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#dc8a78", "selection": "#dc8a7880", "background": "#dc8a78"},
            {"cursor": "#8839ef", "selection": "#8839ef66", "background": "#8839ef"},
            {"cursor": "#7287fd", "selection": "#7287fd66", "background": "#7287fd"},
            {"cursor": "#209fb5", "selection": "#209fb566", "background": "#209fb5"},
            {"cursor": "#40a02b", "selection": "#40a02b66", "background": "#40a02b"},
            {"cursor": "#df8e1d", "selection": "#df8e1d66", "background": "#df8e1d"},
            {"cursor": "#fe640b", "selection": "#fe640b66", "background": "#fe640b"},
            {"cursor": "#d20f39", "selection": "#d20f3966", "background": "#d20f39"},
        ],
        "element.selected": "#ccd0da80",
        "search.match_background": "#17929980",
        "search.active_match_background": "#d20f3980",
        "editor.document_highlight.bracket_background": "#8839ef4d",
        "editor.document_highlight.read_background": "#6c6f8559",
        "editor.document_highlight.write_background": "#6c6f8559",
        "ghost_element.selected": "#8839ef73",
        "pane_group.border": "#7c7f93b3",
        "pane.focused_border": "#8839efcc",
        "element.active": "#00000000",
        "border.variant": "#bcc0cc80",
        "scrollbar.track.border": "#7c7f934d",
        # Current-line wash bumped from ~7% to ~13%: findable, still quiet.
        "editor.active_line.background": "#007aff22",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#8c8fa130",
        "ghost_element.background": "#f9fafc60",
        "ghost_element.hover": "#f9fafc90",
        "ghost_element.active": "#8839ef30",
        "drop_target.background": "#8839ef20",
        "editor.highlighted_line.background": "#007aff22",
        "error.background": "#ffd7d9",
        "warning.background": "#ffe5c0",
        "info.background": "#cce9f3",
        "success.background": "#d4eecf"
    },
    "iced_latte": {
        "background.appearance": "blurred",
        "background": "#e8f4ffd7",
        "status_bar.background": "#d6e9ffd7",
        "title_bar.background": "#d6e9ffd7",
        "elevated_surface.background": "#ddeeff",
        "surface.background": "#e8f4ffd0",
        # Steel-blue divider visible on light blue base; focused = blue vs sky.
        "border": "#6d8fb3b3",
        "hint.background": "#d0e8ffc0",
        "editor.background": "#00000000",
        "editor.line_number": "#0066cc45",
        "editor.active_line_number": "#0077ee90",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle blue scrim for terminal readability + editor|terminal separation.
        "terminal.background": "#d6e9ff1a",
        "toolbar.background": "#00000000",
        # Stronger blue fill marks the active tab.
        "tab.active_background": "#c9e2ff60",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#04a5e5cc",
        "panel.overlay_background": "#ddeeff",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 30% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#dc8a78", "selection": "#dc8a7880", "background": "#dc8a78"},
            {"cursor": "#8839ef", "selection": "#8839ef66", "background": "#8839ef"},
            {"cursor": "#7287fd", "selection": "#7287fd66", "background": "#7287fd"},
            {"cursor": "#209fb5", "selection": "#209fb566", "background": "#209fb5"},
            {"cursor": "#40a02b", "selection": "#40a02b66", "background": "#40a02b"},
            {"cursor": "#df8e1d", "selection": "#df8e1d66", "background": "#df8e1d"},
            {"cursor": "#fe640b", "selection": "#fe640b66", "background": "#fe640b"},
            {"cursor": "#d20f39", "selection": "#d20f3966", "background": "#d20f39"},
        ],
        "element.selected": "#7287fd80",
        "search.match_background": "#17929980",
        "search.active_match_background": "#d20f3980",
        "editor.document_highlight.bracket_background": "#8839ef4d",
        "editor.document_highlight.read_background": "#6c6f8559",
        "editor.document_highlight.write_background": "#6c6f8559",
        "ghost_element.selected": "#7287fd73",
        "pane_group.border": "#6d8fb3b3",
        "pane.focused_border": "#0066ddcc",
        "element.active": "#00000000",
        "border.variant": "#a8c5e080",
        "scrollbar.track.border": "#6d8fb34d",
        # Current-line wash bumped to ~15%: findable, still quiet.
        "editor.active_line.background": "#0077ee26",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#8cb4ff40",
        "ghost_element.background": "#ddeeff60",
        "ghost_element.hover": "#ddeeff90",
        "ghost_element.active": "#7287fd30",
        "drop_target.background": "#7287fd30",
        "editor.highlighted_line.background": "#0077ee26",
        "error.background": "#ffcad5",
        "warning.background": "#ffd8b8",
        "info.background": "#c0e0ff",
        "success.background": "#c8e8c0",
        "text": "#1a3855",
        "text.muted": "#3a5575",
        "text.accent": "#0066dd",
        "icon": "#1a3855",
        "icon.accent": "#0066dd",
        "element.hover": "#d0e8ffa0",
        "element.selected": "#7287fd40"
    },
    "frappe": {
        "background.appearance": "blurred",
        "background": "#303446d7",
        "status_bar.background": "#292c3cd7",
        "title_bar.background": "#292c3cd7",
        "elevated_surface.background": "#292c3c",
        "surface.background": "#303446d0",
        # Overlay1 divider (~70%) visible on dark blur; mauve = pane splits,
        # sky cyan = terminal/panel edge per request for light-on-dark hairlines.
        "border": "#838ba7b3",
        "hint.background": "#414559c0",
        "editor.background": "#00000000",
        "editor.line_number": "#ffffff38",
        "editor.active_line_number": "#ca9ee690",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle dark scrim for terminal readability + editor|terminal separation.
        "terminal.background": "#292c3c1a",
        "toolbar.background": "#00000000",
        # Surface0 fill (lighter than base) marks the active tab.
        "tab.active_background": "#41455960",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#99d1dbcc",
        "panel.overlay_background": "#303446",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 25% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#f2d5cf", "selection": "#f2d5cf80", "background": "#f2d5cf"},
            {"cursor": "#ca9ee6", "selection": "#ca9ee666", "background": "#ca9ee6"},
            {"cursor": "#babbf1", "selection": "#babbf166", "background": "#babbf1"},
            {"cursor": "#85c1dc", "selection": "#85c1dc66", "background": "#85c1dc"},
            {"cursor": "#a6d189", "selection": "#a6d18966", "background": "#a6d189"},
            {"cursor": "#e5c890", "selection": "#e5c89066", "background": "#e5c890"},
            {"cursor": "#ef9f76", "selection": "#ef9f7666", "background": "#ef9f76"},
            {"cursor": "#e78284", "selection": "#e7828466", "background": "#e78284"},
        ],
        "element.selected": "#41455980",
        "search.match_background": "#81c8be80",
        "search.active_match_background": "#e7828480",
        "editor.document_highlight.bracket_background": "#ca9ee64d",
        "editor.document_highlight.read_background": "#a5adce59",
        "editor.document_highlight.write_background": "#a5adce59",
        "ghost_element.selected": "#ca9ee673",
        "pane_group.border": "#838ba7b3",
        "pane.focused_border": "#ca9ee6cc",
        "element.active": "#00000000",
        "border.variant": "#51576d80",
        "scrollbar.track.border": "#838ba74d",
        # Current-line wash bumped from ~7% to ~15%: findable, still quiet.
        "editor.active_line.background": "#ca9ee626",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#62688030",
        "ghost_element.background": "#292c3c60",
        "ghost_element.hover": "#292c3c90",
        "ghost_element.active": "#ca9ee630",
        "drop_target.background": "#ca9ee630",
        "editor.highlighted_line.background": "#ca9ee626",
        "error.background": "#3f2325",
        "warning.background": "#382d20",
        "info.background": "#1f3137",
        "success.background": "#243427"
    },
    "macchiato": {
        "background.appearance": "blurred",
        "background": "#24273ad7",
        "status_bar.background": "#1e2030d7",
        "title_bar.background": "#1e2030d7",
        "elevated_surface.background": "#1e2030",
        "surface.background": "#24273ad0",
        # Overlay divider + mauve pane focus + sky panel focus.
        "border": "#6e738db3",
        "hint.background": "#363a4fc0",
        "editor.background": "#00000000",
        "editor.line_number": "#ffffff38",
        "editor.active_line_number": "#f4dbd690",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle dark scrim for terminal readability + editor|terminal separation.
        "terminal.background": "#1e20301a",
        "toolbar.background": "#00000000",
        # Surface0 fill (lighter than base) marks the active tab.
        "tab.active_background": "#363a4f60",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#91d7e3cc",
        "panel.overlay_background": "#24273a",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 25% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#f4dbd6", "selection": "#f4dbd680", "background": "#f4dbd6"},
            {"cursor": "#c6a0f6", "selection": "#c6a0f666", "background": "#c6a0f6"},
            {"cursor": "#b7bdf8", "selection": "#b7bdf866", "background": "#b7bdf8"},
            {"cursor": "#7dc4e4", "selection": "#7dc4e466", "background": "#7dc4e4"},
            {"cursor": "#a6da95", "selection": "#a6da9566", "background": "#a6da95"},
            {"cursor": "#eed49f", "selection": "#eed49f66", "background": "#eed49f"},
            {"cursor": "#f5a97f", "selection": "#f5a97f66", "background": "#f5a97f"},
            {"cursor": "#ed8796", "selection": "#ed879666", "background": "#ed8796"},
        ],
        "element.selected": "#363a4f80",
        "search.match_background": "#8bd5ca80",
        "search.active_match_background": "#ed879680",
        "editor.document_highlight.bracket_background": "#c6a0f64d",
        "editor.document_highlight.read_background": "#a5adcb59",
        "editor.document_highlight.write_background": "#a5adcb59",
        "ghost_element.selected": "#c6a0f673",
        "pane_group.border": "#6e738db3",
        "pane.focused_border": "#c6a0f6cc",
        "element.active": "#00000000",
        "border.variant": "#494d6480",
        "scrollbar.track.border": "#6e738d4d",
        # Current-line wash bumped from ~7% to ~15%: findable, still quiet.
        "editor.active_line.background": "#f4dbd626",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#8087a230",
        "ghost_element.background": "#1e203060",
        "ghost_element.hover": "#1e203090",
        "ghost_element.active": "#c6a0f630",
        "drop_target.background": "#c6a0f620",
        "editor.highlighted_line.background": "#f4dbd626",
        "error.background": "#3d2224",
        "warning.background": "#362c1f",
        "info.background": "#1e2f35",
        "success.background": "#233225"
    },
    "mocha": {
        "background.appearance": "blurred",
        "background": "#1e1e2ed7",
        "status_bar.background": "#181825d7",
        "title_bar.background": "#181825d7",
        "elevated_surface.background": "#181825",
        "surface.background": "#1e1e2ed0",
        # Overlay0 divider + mauve pane focus + sky cyan panel focus.
        "border": "#6c7086b3",
        "hint.background": "#313244c0",
        "editor.background": "#00000000",
        "editor.line_number": "#ffffff38",
        "editor.active_line_number": "#f5e0dc90",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle dark scrim for terminal readability + editor|terminal separation.
        "terminal.background": "#1818251a",
        "toolbar.background": "#00000000",
        # Surface0 fill (lighter than base) marks the active tab.
        "tab.active_background": "#31324460",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#89dcebcc",
        "panel.overlay_background": "#1e1e2e",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 25% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#f5e0dc", "selection": "#f5e0dc80", "background": "#f5e0dc"},
            {"cursor": "#cba6f7", "selection": "#cba6f766", "background": "#cba6f7"},
            {"cursor": "#b4befe", "selection": "#b4befe66", "background": "#b4befe"},
            {"cursor": "#74c7ec", "selection": "#74c7ec66", "background": "#74c7ec"},
            {"cursor": "#a6e3a1", "selection": "#a6e3a166", "background": "#a6e3a1"},
            {"cursor": "#f9e2af", "selection": "#f9e2af66", "background": "#f9e2af"},
            {"cursor": "#fab387", "selection": "#fab38766", "background": "#fab387"},
            {"cursor": "#f38ba8", "selection": "#f38ba866", "background": "#f38ba8"},
        ],
        "element.selected": "#31324480",
        "search.match_background": "#94e2d580",
        "search.active_match_background": "#f38ba880",
        "editor.document_highlight.bracket_background": "#cba6f74d",
        "editor.document_highlight.read_background": "#a6adc859",
        "editor.document_highlight.write_background": "#a6adc859",
        "ghost_element.selected": "#cba6f773",
        "pane_group.border": "#6c7086b3",
        "pane.focused_border": "#cba6f7cc",
        "element.active": "#00000000",
        "border.variant": "#585b7080",
        "scrollbar.track.border": "#585b704d",
        # Current-line wash bumped from ~7% to ~15%: findable, still quiet.
        "editor.active_line.background": "#f5e0dc26",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#7f849c30",
        "ghost_element.background": "#18182560",
        "ghost_element.hover": "#18182590",
        "ghost_element.active": "#cba6f730",
        "drop_target.background": "#cba6f720",
        "editor.highlighted_line.background": "#f5e0dc26",
        "error.background": "#3b2022",
        "warning.background": "#342a1e",
        "info.background": "#1c2d33",
        "success.background": "#213023"
    },
    "espresso": {
        "background.appearance": "blurred",
        "background": "#000000d7",
        "status_bar.background": "#0a0a0ad7",
        "title_bar.background": "#0a0a0ad7",
        "elevated_surface.background": "#0a0a0a",
        "surface.background": "#000000d0",
        # Stronger overlay divider for pure-black base + mauve/sky focuses.
        "border": "#6e738db3",
        "hint.background": "#1a1a1ac0",
        "editor.background": "#00000000",
        "editor.line_number": "#ffffff38",
        "editor.active_line_number": "#f4dbd690",
        "editor.gutter.background": "#00000000",
        "tab_bar.background": "#00000000",
        # Subtle scrim for terminal readability + editor|terminal separation.
        "terminal.background": "#0a0a0a1a",
        "toolbar.background": "#00000000",
        # Lighter fill marks the active tab against the black base.
        "tab.active_background": "#1a1a1a60",
        "tab.inactive_background": "#00000000",
        "panel.background": "#00000000",
        "panel.focused_border": "#91d7e3cc",
        "panel.overlay_background": "#1a1a1a",
        # Selection + highlight states: same Catppuccin hues, stronger alphas.
        # Own text selection (players[0]) goes 25% grey -> 50% cursor-rosewater
        # so selected text reads over blur.
        "players": [
            {"cursor": "#f4dbd6", "selection": "#f4dbd680", "background": "#f4dbd6"},
            {"cursor": "#c6a0f6", "selection": "#c6a0f666", "background": "#c6a0f6"},
            {"cursor": "#b7bdf8", "selection": "#b7bdf866", "background": "#b7bdf8"},
            {"cursor": "#7dc4e4", "selection": "#7dc4e466", "background": "#7dc4e4"},
            {"cursor": "#a6da95", "selection": "#a6da9566", "background": "#a6da95"},
            {"cursor": "#eed49f", "selection": "#eed49f66", "background": "#eed49f"},
            {"cursor": "#f5a97f", "selection": "#f5a97f66", "background": "#f5a97f"},
            {"cursor": "#ed8796", "selection": "#ed879666", "background": "#ed8796"},
        ],
        "element.selected": "#363a4f80",
        "search.match_background": "#8bd5ca80",
        "search.active_match_background": "#ed879680",
        "editor.document_highlight.bracket_background": "#c6a0f64d",
        "editor.document_highlight.read_background": "#a5adcb59",
        "editor.document_highlight.write_background": "#a5adcb59",
        "ghost_element.selected": "#c6a0f673",
        "pane_group.border": "#6e738db3",
        "pane.focused_border": "#c6a0f6cc",
        "element.active": "#00000000",
        "border.variant": "#363a4f80",
        "scrollbar.track.border": "#6e738d4d",
        # Current-line wash bumped from ~7% to ~15%: findable, still quiet.
        "editor.active_line.background": "#f4dbd626",
        "scrollbar.track.background": "#00000000",
        "scrollbar.thumb.background": "#8087a230",
        "ghost_element.background": "#0a0a0a60",
        "ghost_element.hover": "#0a0a0a90",
        "ghost_element.active": "#c6a0f630",
        "drop_target.background": "#c6a0f620",
        "editor.highlighted_line.background": "#f4dbd626",
        "error.background": "#391e20",
        "warning.background": "#32281d",
        "info.background": "#1a2b31",
        "success.background": "#1f2e21"
    }
}

# Generate all theme overrides for all blur levels
THEME_OVERRIDES = {}
for level_name, level_config in BLUR_LEVELS.items():
    for variant_name, base_overrides in BASE_THEME_OVERRIDES.items():
        key = f"{variant_name}_{level_name}"
        THEME_OVERRIDES[key] = generate_theme_overrides_for_level(base_overrides, level_config)

"""
Map variant names from upstream to our override keys.
Handles both accented and plain versions of Frappé.
Maps to medium blur level (85% opacity) - this is the default blur level
used for original theme names like "Catppuccin Latte (Blur)".
"""
VARIANT_MAP = {
    "latte": "latte_medium",
    "frappé": "frappe_medium",
    "frappe": "frappe_medium",
    "macchiato": "macchiato_medium",
    "mocha": "mocha_medium"
}
