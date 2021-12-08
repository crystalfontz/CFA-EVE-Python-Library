# CFA-EVE-Python-Library
Python example library for Crystalfontz FTDI/BridgeTek EVE graphic accelerators.

This library is currently aimed at using EVE based display modules with Raspberry Pi computers.

Crystalfontz EVE displays can viewed/purchased on the [Crystafontz EVE Accelerated TFT Displays webpage](https://www.crystalfontz.com/products/eve-accelerated-tft-displays.php).

A list of the displays supported by this library are [here in the module support document](module_support.md).

Please consider this library to be a work-in-progress.
Some EVE features are not yet supported, and interfaces for other host computer systems will be added at a later date.

Example connection guide using a Crystalfontz EVE breakout board (CFA10098)

| Raspberry Pi Header Pin | CFA10098 Pin |     Connection Description     |
|-------------------------|--------------|--------------------------------|
|                       1 | +3.3V        | 3.3V Supply to the EVE Module  |
|                       6 | GND          | Power ground to the EVE Module |
|                      19 | MOSI         | SPI MOSI                       |
|                      20 | GND          | Power ground to the EVE Module |
|                      21 | MISO         | SPI MISO                       |
|                      23 | SCLK         | SPI SCLK                       |
|                      24 | CS           | SPI Chip Select                |
|                      29 | INT          | EVE Interrupt                  |
|                      31 | PD           | EVE Power-Down / Reset         |
