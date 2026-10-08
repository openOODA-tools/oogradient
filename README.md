# oogradient: Sovereign TrueColor Gradient Interpolation Engine

<div align="center">

```
================================================================================
                                oogradient
             Sovereign openOODA TrueColor Gradient Engine
================================================================================
```

**Sovereign TrueColor Gradient Interpolation Engine**  
*Applies smooth TrueColor color gradient interpolation across lines of text.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64](https://img.shields.io/badge/Arch-x86__64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64)
```bash
curl -fsSL https://openooda-tools.github.io/oogradient/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oogradient-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openooda-tools.github.io/oogradient/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openooda-tools.github.io/oogradient/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oogradient-uninstall
# or: curl -fsSL https://openooda-tools.github.io/oogradient/uninstall.sh | bash
```

---

## 2. CLI Usage

```
usage: oogradient [options] [<text>...]

Applies smooth TrueColor color gradient interpolation across lines of text.

Options:
  -h, --help               display this help and exit
  -v, --version            output version information and exit
  -p, --preset <NAME>      select gradient preset (rainbow, sunset, cyberpunk, neon, aurora, plasma, ocean, fire)
      --from <HEX>         custom starting RGB color (e.g. #ff007f or 0x00ffff)
      --to <HEX>           custom ending RGB color (e.g. #00ffff)
      --presets            list all registered gradient presets
  -j, --json               output structured JSON metrics
  -D, --demo               interactive TrueColor gradient showcase
      --no-color           suppress ANSI escape codes
      --test               execute internal multi-tier verification suite
      --mcp                run as Model Context Protocol stdio server
```

---

## 3. Registered Gradient Presets

| Preset | Colors & Stops | Description |
|---|---|---|
| `rainbow` | Red, Orange, Yellow, Green, Cyan, Blue, Violet (7 stops) | Full visible spectrum rainbow transition |
| `sunset` | Deep purple `#8a2387`, crimson `#e94057`, gold `#f27121` (3 stops) | Deep dusk to radiant amber |
| `cyberpunk` | Electric cyan `#00f0ff`, neon purple `#b000ff`, hot pink `#ff007f` (3 stops) | High-contrast neon synthesis |
| `neon` | Fluorescent lime `#39ff14`, electric cyan `#00ffff`, magenta `#ff00ff` (3 stops) | High-intensity luminous glow |
| `aurora` | Emerald `#00ff87`, sky cyan `#60efff`, night blue `#0061ff` (3 stops) | Boreal atmospheric ionisation |
| `plasma` | Violet-indigo `#6a11cb`, cobalt blue `#2575fc` (2 stops) | Electric energetic discharge |
| `ocean` | Turquoise `#00c6ff`, deep blue `#0072ff` (2 stops) | Abyssal pelagic depth |
| `fire` | Solar yellow `#ffe600`, flame orange `#ff5e00`, incandescent red `#ff0000` (3 stops) | Thermal combustion ramp |

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oogradient` runs a streaming JSON-RPC 2.0 stdio server providing 5 tools:

* **`gradient_apply`**: Style text with TrueColor ANSI gradient escape sequences using presets or hex endpoints.
* **`gradient_interpolate`**: Generate discrete RGB steps along a color ramp.
* **`gradient_presets`**: Introspect all available gradient palettes with stop coordinates.
* **`gradient_preview`**: Generate color block swatch previews.
* **`gradient_demo`**: Run interactive terminal showcase demonstrating all palettes.

```bash
oogradient --mcp
```

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Demands explicit capability tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`).
* **Negative-Trust Architecture:** Strict parameter unescaping and bounds-checked interpolation mathematics.
* **Hermetic Binary:** Standalone executable requiring zero external shared libraries beyond standard glibc.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
