 Experiment:     	SST
============================================================
 Programmer:     	Thomas Quettier
============================================================
 Date:           	01/05/2024
============================================================
 PsychoPy Version:    	v2022.1.4
============================================================
 Description:    	SST Task
============================================================

## Overview
In this stop signal task each trial start with the presentation of a black dot centered on a blank white screen for 800 ms and end with an empty blank white screen for 1600 ms, acting as an inter-trial interval. In Go-task participant has to press the left key when a green arrow pointing to the left appears, or the right key when the arrow pointing to the right appears, (arrow duration 100 ms). Stop-trials are identical to the Go-trials, except that a "XX" writing (i.e., Stop-signal) is presented for 70 ms, after a variable stop-signal delay (SSD) relative to the onset of the Go-stimulus (arrow), instructing participants to suppress the imminent Go response. The initial value of the SSD is set to 150 ms and adjusted individually and dynamically throughout the experiment (from a minimum of 50 ms to a maximum of 650 ms). Overall, our task was designed based on the recommendations of Verbruggen et al. (2019).

## Requirements
- PsychoPy v2022.1.4

## Installation
1. Install PsychoPy v2022.1.4
2. Clone this repository or download the experiment files.
3. Run the script using Psychopy: `SST.psyexp`

## Customization
The experiment can be customized or adjusted, such as changing the inter-stimulus interval.

## Contact Information
Thomas.quettier2@unibo.it

## References
Verbruggen, F., Aron, A. R., Band, G. P., Beste, C., Bissett, P. G., Brockett, A. T., ... & Boehler, C. N. (2019). A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. elife, 8, e46323.

