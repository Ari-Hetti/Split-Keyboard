<h1 align="center">
Split Keyboard
</h1>

<h3 align="center">
A Split Keyboard With Wireless Capabilities
</h3>

<p align="center">
  <a href="#key-features">Key Features</a> -
  <a href="#description">Description</a> -
  <a href="#components">Components</a> -
  <a href="#board-design">Board Design</a> -
  <a href="#cad">CAD</a> -
  <a href="#bom">BOM</a> -
  <a href="#software">Software</a> -
  <a href="#credits">Credits</a> -
  <a href="#my-other-projects">My Other Projects</a> -
</p>

## Key Features
- **XIAO nRF52840**
- **Rotary Encoder**
- **Hotswapable Keys**

## Description
A small 32 key split keyboard with thumb knobs that can be powered wired or wirelessly.

## Components
- 2 XIAO nRF52840
- 2 Rotary Encoders
- 32 Hotswap Sockets
- 32 MX Style Switches
- 32 Diodes

## Board Design
### Schematics
<img width="1152" height="523" alt="Schematic Left" src="https://github.com/user-attachments/assets/a5d71b91-63c0-405f-b08f-bb18f5d1abc1" />
<img width="1629" height="672" alt="Schematic Right" src="https://github.com/user-attachments/assets/88a70f96-f22f-4c73-8247-be192efe08b8" />
<img width="740" height="753" alt="Root Page" src="https://github.com/user-attachments/assets/40129fb2-80c5-4515-88e0-031d47139466" />


### PCB
<img width="1023" height="843" alt="PCB Left" src="https://github.com/user-attachments/assets/acfa2b9d-631a-460b-bcda-8de486a8b8f8" />
<img width="901" height="865" alt="PCB Right" src="https://github.com/user-attachments/assets/7d5b38a0-9902-43ab-a1f6-37d3f970c934" />

### 3D View
<img width="891" height="895" alt="3d Left" src="https://github.com/user-attachments/assets/e186d1fe-5e10-4781-99b1-a817333a9b55" />
<img width="944" height="899" alt="3d Right" src="https://github.com/user-attachments/assets/5a2b8a22-3fe3-44a3-ac14-a215be666eac" />


## CAD
<img width="1235" height="649" alt="Corner View Onshape" src="https://github.com/user-attachments/assets/8276d79b-1c74-429d-aa63-22377b54c49f" />
<img width="1250" height="695" alt="Top View Onshape" src="https://github.com/user-attachments/assets/c711f8db-87b3-48f5-a7ff-5ced928e9a0b" />



## BOM
Name |	Purpose |	Quantity |	Total Cost (USD) |	Link |	Distributor
-----|-------------|----------|-------------------|-------|-------------|
Switches |	The buttons - I will buy myself as the ones I want are around $40 with shipping |	30 |	0 | |		Cherry
Keycaps |	To press |	104 |	$7.14 |	[Aliexpress](https://www.aliexpress.com/item/1005008295250376.html?spm=a2g0o.cart.0.0.6dc738dafAtEzr&mp=1&pdp_npi=6%40dis%21USD%21USD+7.21%21USD+7.21%21%21USD+7.21%21%21%21%40210311c217777118378842309e2cb9%2112000044523183096%21ct%21CA%217286041038%21%211%210%21) | Aliexpress
Hotswap Sockets |	Holds the Switch |	30 |	1.29 |	[LCSC](https://www.lcsc.com/product-detail/C49352235.html?s_z=n_q_CPG151101S11%2520&spm=wm.ssy.bg.0.xh&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVhXVlFTQVRXVTsOAxUeFF5JWBYZEEoKFBINSQcJGk4eFQsCAgIaSgADAwAHC0slQlBbUVBeR08GEwkK) |	LCSC
Seeed Studio XIAO nRF52840 |	MCU - I will buy myself as by itself is $40 with shipping |	2 |	0 |	[Aliexpress](https://www.aliexpress.com/item/1005006988954136.html?spm=a2g0o.cart.0.0.141238da8PxZYU&mp=1&pdp_npi=6%40dis%21CAD%21CAD+51.66%21CAD+27.38%21%21CAD+27.38%21%21%21%402101d49617769317249153178e7174%2112000042942288178%21ct%21CA%217286041038%21%211%210%21) |	Aliexpress
EC11E Rotary Encoder |	Knob |	2 |	3.96 |	[LCSC](https://www.lcsc.com/product-detail/C470754.html?spm=wm.gwc.xh.6.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
10k Resistor |	Encoder Resistors |	100 |	0.3 |	[LCSC](https://www.lcsc.com/product-detail/C17414.html?spm=wm.gwc.xh.5.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
2M Resistor |	VBAT Sense |	100 |	0.17 |	[LCSC](https://www.lcsc.com/product-detail/C2907316.html?spm=wm.gwc.xh.4.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
806k Resistor |	VBAT Sense |	10 |	0.79 |	[LCSC](https://www.lcsc.com/product-detail/C2849350.html?spm=wm.gwc.xh.3.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
Diode |	Keyboard Matrix |	100 |	0.57 |	[LCSC](https://www.lcsc.com/product-detail/C917030.html?spm=wm.gwc.xh.2.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
2 Pin Connector |	Battery Connection |	10 |	0.43 |	[LCSC](https://www.lcsc.com/product-detail/C2906268.html?spm=wm.gwc.xh.1.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
10nF Capacitor |	Decoupling |	50 |	0.34 |	[LCSC](https://www.lcsc.com/product-detail/C1710.html?spm=wm.gwc.xh.0.cbm___wm.sy.ssl.gwc&lcsc_vid=RAcKAlZfRgcIX1ReFQJbUgBSRQMIXgJTTgVcAwJURlQxVlNRQVlWUlNSQ1BcVTtW) |	LCSC
PCBs |	The PCB order (split up to save cost - 5 each side) |	10 |	6	| |	JLCPCP

## Software
For this project I will be using KMK, which is an open-source keyboard firmware. I decided to use this instead of ZMK or QMK even with the split keyboard feature still being in devlopment, because I was already familiar with the process due to my experience from my previous keyboard project [Hexpad_Highway](https://github.com/Ari-Hetti/Hexpad_Highway). For the firmware part I landed on a simple keymap with just letters and couple of punctuation symbols as I just want the keyboard to type. I do plan on adding more in the future when I get to the build and can tinker with the possiblities that entail.
### Code:
<img width="644" height="982" alt="Code" src="https://github.com/user-attachments/assets/013386bf-3c51-4737-9a2f-3935283969a0" />


## Credits
This was made using:
- [KiCAD](https://www.kicad.org/) - PCB Design
- [JLCPCB](https://jlcpcb.com/) - PCB Manufacturing
- [LCSC](https://www.lcsc.com/) - Component Sourcing
- [Statis Guide](https://stasis.hackclub.com/starter-projects/split-keyboard) - Split Keyboard Guide

## My Other Projects
- [Hexpad_Highway](https://github.com/Ari-Hetti/Hexpad_Highway) - 6 key Macropad with a knob and OLED
- [Quadcopter Flight Controller](https://github.com/Ari-Hetti/Quadcopter-Flight-Controller) - Flight controller for a 5in quadcopter
- [FRC Badge V2](https://github.com/Ari-Hetti/FRC-Badge-V2) - Hexagonal 555 timer LED chaser keychain
