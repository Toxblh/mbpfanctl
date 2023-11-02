Mac Fan Controls in Linux
---

# Before we start

Need to install 
`mbpfan`
and once start it to control fan's `sudo mbpfan`

# Usage
Get current status
`python3 ./main.py get`

And set minimal fan, we don't broke auto control, only change minimal avaliable

`sudo python3 ./main.py set max`

Inspired https://github.com/rselbach/macfanctl
