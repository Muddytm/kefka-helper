# Kefka Helper

A little tool to help with Dancing Mad (Ultimate) phase 4, AKA Kefka Says.

## How to run it

You'll need python installed to run the script. You can find python installers here: https://www.python.org/downloads/

When installed, open up a terminal (command prompt, Powershell, etc.), navigate to the location of the file, and run `python kefkasays.py`.

## How to use it

By default, most of the listed data is what you'll *generally* get when all Grand Crosses, Inferno, and Tsunami are **true**. The one exception is that you may have stack instead of spread.

In order of casts during the P4 setup:

- Grand Cross #1: **if fake**, check the box next to **? FIRST GAZE**. If you get a spread from either Grand Cross (either a real one, or a fake water-stack), mark **SPREAD**. If you get Acceleration Bomb and the cast was fake, mark **MOTION**.
- Chaos cast #1: **if fake**, check the box for the appropriate element (**? WATER** or **? FIRE**).
- Grand Cross #2: **same as with Grand Cross #1**. Note that if you received a spread/stack on Grand Cross #1, you should get Acceleration Bomb this time, and vice versa.
- Chaos cast #2: **same as with Chaos cast #1**.

There are no settings currently included for Grand Cross #3 or Mana Charges, but...

## How to modify it

You can add your own settings to this or change it completely for other mechanics with very little work, as the script is simple and the UI elements are easily replicable. I might add a tiny tutorial here later, but try copy-pasting things and renaming them and see what happens.