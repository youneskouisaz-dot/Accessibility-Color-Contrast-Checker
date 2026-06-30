def hex_to_rgb(hex_color):
    hex_color = hex_color.replace("#", "")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def linearize(value):
    value = value / 255
    if value <= 0.03928:
        return value / 12.92
    return ((value + 0.055) / 1.055) ** 2.4

def relative_luminance(rgb):
    r, g, b = [linearize(v) for v in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast_ratio(color1, color2):
    lum1 = relative_luminance(hex_to_rgb(color1))
    lum2 = relative_luminance(hex_to_rgb(color2))
    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)
    return (lighter + 0.05) / (darker + 0.05)

foreground = input("Enter text color hex code, example #000000: ")
background = input("Enter background color hex code, example #FFFFFF: ")

ratio = contrast_ratio(foreground, background)

print(f"\nContrast Ratio: {ratio:.2f}:1")

if ratio >= 7:
    print("Passes WCAG AAA standard.")
elif ratio >= 4.5:
    print("Passes WCAG AA standard for normal text.")
elif ratio >= 3:
    print("Passes only for large text.")
else:
    print("Fails accessibility contrast standards.")
