#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Sep 20 17:03:49 2024
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# MIT License
# 
# Copyright (c) [2014] [Thomas Quettier]
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#   
#   The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# Additional Note:
#   While not legally binding, the author would appreciate an acknowledgment or citation
# where possible if this software is used in the development of new software, publications,
# or research. For citation guidelines, please refer to the CITATION file in this repository.


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'SST'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
    'training': '1',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/thomasquettier/Library/Mobile Documents/com~apple~CloudDocs/01.WORK/02GITHUB/Stop_signal_task/PsychoPy3 SST Task 2/SST_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "INFO"
INFOClock = core.Clock()
# This section sets essential parameters for the experiment based on user input 
# and predefined settings. These parameters determine the number of trials and blocks, 
# include optional training, and set the duration between trials.

# Number of blocks to loop through in the experiment
nb_loop_blocks = 4 # default 4

# Number of trials per block. Each block contains 16 trials,
# cumulatively 128 trials across all blocks with a distribution of 
# 32 stop trials and 96 go trials (stop:go ratio = 1:4 please refer to the conditions.xlsx file)
nb_loop_trial = 16  # default 16
# 16 trials per block x 8 blocks = 128 total trials

# Inter-Trial Interval (ITI): This is the time delay between the end of one trial 
# and the start of the next trial, set to 1.6 seconds
iti = 1.6

# Training flag obtained from the experiment info dialogue box:
# '1' means the experiment includes a training phase,
# '0' means the training phase is skipped
nb_training = expInfo['training']
info_txt = visual.TextStim(win=win, name='info_txt',
    text='Your task will be to respond to the green arrow that will appear on the screen.\n\nIn some trials, immediately after the arrow, the letters "XX" will appear. In this case, your task will be NOT to press the key, thus stopping your response.\n\nSometimes it will be very easy to stop, other times more difficult, because the test adapts to your performance.\n\nAttention! We ask you not to wait for the appearance of the stimulus, but to respond as quickly and accurately as possible. Don\'t worry about making mistakes, the test will adapt.\n\nPress \'space\' to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
info_kb = keyboard.Keyboard()

# Initialize components for Routine "ISTRUCTIONS"
ISTRUCTIONSClock = core.Clock()
istr_txt = visual.TextStim(win=win, name='istr_txt',
    text='It is still very important that you respond as QUICKLY and ACCURATELY as possible.\n\nThe experiment lasts about 20 minutes.\nThe experiment consists of a practice block and 4 experimental blocks. During the practice block, you will receive feedback on your performance ("too slow", "correct stop").\n\nBetween each block, there will be an opportunity for a short break.\n\nPress \'space\' to begin',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
istr_kb = keyboard.Keyboard()

# Initialize components for Routine "TRIAL_SST"
TRIAL_SSTClock = core.Clock()
# Trial Routine:
# This routine manages the sequence of events in a single trial, including
# handling stop signals, recording response times, and adjusting stop-signal delays.

# Hides the mouse cursor for the duration of the experiment to avoid distractions.
event.Mouse(visible=False)

# The predefined timing for the interval between the Go signal and the Stop signal start.
StopSignal_start = 0.95  # Stop signal starts at 950 ms after the Go signal

# Initial Stop Signal Delay (SSD) set to 150 milliseconds.
ssd = 0.15
ssd_1 = 0.15
ssd_2 = 0.15

dot_img = visual.ImageStim(
    win=win,
    name='dot_img', units='norm', 
    image='images/fix.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
go_img = visual.ImageStim(
    win=win,
    name='go_img', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
stop_img = visual.ImageStim(
    win=win,
    name='stop_img', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "FEEDBACK"
FEEDBACKClock = core.Clock()
# Feedback Routine:
# This routine provides feedback to participants based on their responses in the trial.
# It displays messages corresponding to their performance, differentiating between
# correct, incorrect, too fast, too slow, and stop-signal responses.

# Define the feedback messages for various response outcomes.
msg = ""  # Initializes the message variable to be empty
correct_msg = 'Correct'  # Message displayed for correct responses in Go trials
incorrect_msg = 'Oops'  # Message for incorrect responses
too_slow_msg = 'Too slow'  # Message when response is slower than expected
too_fast_msg = 'Too fast'  # Message when response is faster than expected
correct_stop_msg = 'Perfect stop'  # Message for successful inhibition in a Stop trial
incorrect_stop_msg = 'You must Stop!'  # Message when failing to inhibit in a Stop trial

feedback_txt = visual.TextStim(win=win, name='feedback_txt',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
iti_txt = visual.TextStim(win=win, name='iti_txt',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BEGIN_EXP"
BEGIN_EXPClock = core.Clock()
begin_txt = visual.TextStim(win=win, name='begin_txt',
    text="Training is finished. \n\nYou will begin the expreriment. From now, you will not receive any feedback. \n\nPress 'space' to begin",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
begin_kb = keyboard.Keyboard()

# Initialize components for Routine "TRIAL_SST"
TRIAL_SSTClock = core.Clock()
# Trial Routine:
# This routine manages the sequence of events in a single trial, including
# handling stop signals, recording response times, and adjusting stop-signal delays.

# Hides the mouse cursor for the duration of the experiment to avoid distractions.
event.Mouse(visible=False)

# The predefined timing for the interval between the Go signal and the Stop signal start.
StopSignal_start = 0.95  # Stop signal starts at 950 ms after the Go signal

# Initial Stop Signal Delay (SSD) set to 150 milliseconds.
ssd = 0.15
ssd_1 = 0.15
ssd_2 = 0.15

dot_img = visual.ImageStim(
    win=win,
    name='dot_img', units='norm', 
    image='images/fix.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
go_img = visual.ImageStim(
    win=win,
    name='go_img', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
stop_img = visual.ImageStim(
    win=win,
    name='stop_img', units='norm', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp = keyboard.Keyboard()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
iti_txt = visual.TextStim(win=win, name='iti_txt',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BREAK"
BREAKClock = core.Clock()
break_txt = visual.TextStim(win=win, name='break_txt',
    text="Pause.\n\nPress 'space' to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
break_kb = keyboard.Keyboard()

# Initialize components for Routine "THANKS"
THANKSClock = core.Clock()
thanks_txt = visual.TextStim(win=win, name='thanks_txt',
    text='Thank you for your time.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
thanks_kb = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "INFO"-------
continueRoutine = True
# update component parameters for each repeat
info_kb.keys = []
info_kb.rt = []
_info_kb_allKeys = []
# keep track of which components have finished
INFOComponents = [info_txt, info_kb]
for thisComponent in INFOComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
INFOClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "INFO"-------
while continueRoutine:
    # get current time
    t = INFOClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=INFOClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *info_txt* updates
    if info_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info_txt.frameNStart = frameN  # exact frame index
        info_txt.tStart = t  # local t and not account for scr refresh
        info_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info_txt, 'tStartRefresh')  # time at next scr refresh
        info_txt.setAutoDraw(True)
    
    # *info_kb* updates
    waitOnFlip = False
    if info_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        info_kb.frameNStart = frameN  # exact frame index
        info_kb.tStart = t  # local t and not account for scr refresh
        info_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(info_kb, 'tStartRefresh')  # time at next scr refresh
        info_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(info_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(info_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if info_kb.status == STARTED and not waitOnFlip:
        theseKeys = info_kb.getKeys(keyList=['space'], waitRelease=False)
        _info_kb_allKeys.extend(theseKeys)
        if len(_info_kb_allKeys):
            info_kb.keys = _info_kb_allKeys[-1].name  # just the last key pressed
            info_kb.rt = _info_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in INFOComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "INFO"-------
for thisComponent in INFOComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "INFO" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ISTRUCTIONS"-------
continueRoutine = True
# update component parameters for each repeat
istr_kb.keys = []
istr_kb.rt = []
_istr_kb_allKeys = []
# keep track of which components have finished
ISTRUCTIONSComponents = [istr_txt, istr_kb]
for thisComponent in ISTRUCTIONSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ISTRUCTIONSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ISTRUCTIONS"-------
while continueRoutine:
    # get current time
    t = ISTRUCTIONSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ISTRUCTIONSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *istr_txt* updates
    if istr_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        istr_txt.frameNStart = frameN  # exact frame index
        istr_txt.tStart = t  # local t and not account for scr refresh
        istr_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(istr_txt, 'tStartRefresh')  # time at next scr refresh
        istr_txt.setAutoDraw(True)
    
    # *istr_kb* updates
    waitOnFlip = False
    if istr_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        istr_kb.frameNStart = frameN  # exact frame index
        istr_kb.tStart = t  # local t and not account for scr refresh
        istr_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(istr_kb, 'tStartRefresh')  # time at next scr refresh
        istr_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(istr_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(istr_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if istr_kb.status == STARTED and not waitOnFlip:
        theseKeys = istr_kb.getKeys(keyList=['space'], waitRelease=False)
        _istr_kb_allKeys.extend(theseKeys)
        if len(_istr_kb_allKeys):
            istr_kb.keys = _istr_kb_allKeys[-1].name  # just the last key pressed
            istr_kb.rt = _istr_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ISTRUCTIONSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ISTRUCTIONS"-------
for thisComponent in ISTRUCTIONSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "ISTRUCTIONS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Loop_practice = data.TrialHandler(nReps=nb_training, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.xlsx'),
    seed=None, name='Loop_practice')
thisExp.addLoop(Loop_practice)  # add the loop to the experiment
thisLoop_practice = Loop_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
if thisLoop_practice != None:
    for paramName in thisLoop_practice:
        exec('{} = thisLoop_practice[paramName]'.format(paramName))

for thisLoop_practice in Loop_practice:
    currentLoop = Loop_practice
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_practice.rgb)
    if thisLoop_practice != None:
        for paramName in thisLoop_practice:
            exec('{} = thisLoop_practice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TRIAL_SST"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Records the SSD at the beginning of each trial in milliseconds.
    thisExp.addData("SSD", ssd * 1000)  # SSD is stored in milliseconds
    
    
    
    go_img.setImage("images/" + go_file)
    stop_img.setImage("images/"  + stop_file)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    TRIAL_SSTComponents = [dot_img, go_img, stop_img, key_resp, ISI]
    for thisComponent in TRIAL_SSTComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TRIAL_SSTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TRIAL_SST"-------
    while continueRoutine:
        # get current time
        t = TRIAL_SSTClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TRIAL_SSTClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dot_img* updates
        if dot_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            dot_img.frameNStart = frameN  # exact frame index
            dot_img.tStart = t  # local t and not account for scr refresh
            dot_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dot_img, 'tStartRefresh')  # time at next scr refresh
            dot_img.setAutoDraw(True)
        if dot_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > dot_img.tStartRefresh + 0.8-frameTolerance:
                # keep track of stop time/frame for later
                dot_img.tStop = t  # not accounting for scr refresh
                dot_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(dot_img, 'tStopRefresh')  # time at next scr refresh
                dot_img.setAutoDraw(False)
        
        # *go_img* updates
        if go_img.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
            # keep track of start time/frame for later
            go_img.frameNStart = frameN  # exact frame index
            go_img.tStart = t  # local t and not account for scr refresh
            go_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_img, 'tStartRefresh')  # time at next scr refresh
            go_img.setAutoDraw(True)
        if go_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > go_img.tStartRefresh + 0.9-frameTolerance:
                # keep track of stop time/frame for later
                go_img.tStop = t  # not accounting for scr refresh
                go_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(go_img, 'tStopRefresh')  # time at next scr refresh
                go_img.setAutoDraw(False)
        
        # *stop_img* updates
        if stop_img.status == NOT_STARTED and tThisFlip >= StopSignal_start + ssd-frameTolerance:
            # keep track of start time/frame for later
            stop_img.frameNStart = frameN  # exact frame index
            stop_img.tStart = t  # local t and not account for scr refresh
            stop_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stop_img, 'tStartRefresh')  # time at next scr refresh
            stop_img.setAutoDraw(True)
        if stop_img.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stop_img.tStartRefresh + 0.07-frameTolerance:
                # keep track of stop time/frame for later
                stop_img.tStop = t  # not accounting for scr refresh
                stop_img.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stop_img, 'tStopRefresh')  # time at next scr refresh
                stop_img.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 1.7-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # was this correct?
                if (key_resp.keys == str(correct_key)) or (key_resp.keys == correct_key):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.8)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.8  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRIAL_SSTComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TRIAL_SST"-------
    for thisComponent in TRIAL_SSTComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Code to log and handle premature responses.
    if key_resp.rt:  # Checks if there was a response
        if signal == 1:  # For Stop trials
            # Checks if the response was made before the sum of StopSignal was presented
            if key_resp.rt <= (StopSignal_start + ssd):
                thisExp.addData("premature", 1)  # Logs response as premature
            else:
                thisExp.addData("premature", 0)  # Logs response as not premature
        elif signal == 0:  # For Go trials
            # Checks if the response was made before the Go signal was fully presented
            if key_resp.rt <= (StopSignal_start):
                thisExp.addData("premature", 1)
            else:
                thisExp.addData("premature", 0)
    
    # Calculates and logs the Reaction Time (RT) from the end of the Go signal to the response.
    if key_resp.rt:
        rt = (key_resp.rt - StopSignal_start) * 1000  # Converts seconds to milliseconds
        thisExp.addData("RT", rt)
    
    # Dynamic SSD adjustment:
    # Adjusts the SSD based on the participant's performance in Stop trials.
    if signal == 1:
        if len(key_resp.keys) > 0:  # If the participant responded
            ssd -= 0.050  # Decreases SSD by 50 ms to make stopping easier next time
            if ssd <= 0.050:  # Ensures SSD doesn't go below 50 ms
                ssd = 0.050
        else:  # If the participant did not respond
            ssd += 0.050  # Increases SSD by 50 ms to make stopping harder next time
            if ssd >= 0.650:  # Ensures SSD doesn't exceed 650 ms
                ssd = 0.650
    
        
    
    Loop_practice.addData('dot_img.started', dot_img.tStartRefresh)
    Loop_practice.addData('dot_img.stopped', dot_img.tStopRefresh)
    Loop_practice.addData('go_img.started', go_img.tStartRefresh)
    Loop_practice.addData('go_img.stopped', go_img.tStopRefresh)
    Loop_practice.addData('stop_img.started', stop_img.tStartRefresh)
    Loop_practice.addData('stop_img.stopped', stop_img.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(correct_key).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for Loop_practice (TrialHandler)
    Loop_practice.addData('key_resp.keys',key_resp.keys)
    Loop_practice.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        Loop_practice.addData('key_resp.rt', key_resp.rt)
    Loop_practice.addData('key_resp.started', key_resp.tStartRefresh)
    Loop_practice.addData('key_resp.stopped', key_resp.tStopRefresh)
    Loop_practice.addData('ISI.started', ISI.tStart)
    Loop_practice.addData('ISI.stopped', ISI.tStop)
    # the Routine "TRIAL_SST" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FEEDBACK"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # Determines the feedback message based on the trial type and response characteristics.
    if signal == 0:  # For Go trials
        if key_resp.keys is not None:  # If there was a response
            if key_resp.rt <= StopSignal_start - 0.05:
                msg = too_fast_msg  # If response is premature
            elif key_resp.corr == 1:
                msg = correct_msg  # If response is correct
            elif key_resp.corr == 0:
                msg = incorrect_msg  # If response is incorrect
            elif key_resp.rt >= (StopSignal_start - 0.05 + ssd):
                msg = too_slow_msg  # If response is too slow
        else:
            msg = too_slow_msg  # If no response, considered too slow
    elif signal == 1:  # For Stop trials
        if key_resp.keys is not None:
            msg = incorrect_stop_msg  # If there was a response, it's incorrect (failed to stop)
        else:
            msg = correct_stop_msg  # If no response, it's a perfect stop
        
    
    feedback_txt.setText(msg)
    # keep track of which components have finished
    FEEDBACKComponents = [feedback_txt]
    for thisComponent in FEEDBACKComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FEEDBACKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FEEDBACK"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FEEDBACKClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FEEDBACKClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_txt* updates
        if feedback_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_txt.frameNStart = frameN  # exact frame index
            feedback_txt.tStart = t  # local t and not account for scr refresh
            feedback_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_txt, 'tStartRefresh')  # time at next scr refresh
            feedback_txt.setAutoDraw(True)
        if feedback_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_txt.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                feedback_txt.tStop = t  # not accounting for scr refresh
                feedback_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_txt, 'tStopRefresh')  # time at next scr refresh
                feedback_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FEEDBACKComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FEEDBACK"-------
    for thisComponent in FEEDBACKComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_practice.addData('feedback_txt.started', feedback_txt.tStartRefresh)
    Loop_practice.addData('feedback_txt.stopped', feedback_txt.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ITIComponents = [iti_txt]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iti_txt* updates
        if iti_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iti_txt.frameNStart = frameN  # exact frame index
            iti_txt.tStart = t  # local t and not account for scr refresh
            iti_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iti_txt, 'tStartRefresh')  # time at next scr refresh
            iti_txt.setAutoDraw(True)
        if iti_txt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iti_txt.tStartRefresh + iti-frameTolerance:
                # keep track of stop time/frame for later
                iti_txt.tStop = t  # not accounting for scr refresh
                iti_txt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iti_txt, 'tStopRefresh')  # time at next scr refresh
                iti_txt.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_practice.addData('iti_txt.started', iti_txt.tStartRefresh)
    Loop_practice.addData('iti_txt.stopped', iti_txt.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed nb_training repeats of 'Loop_practice'


# set up handler to look after randomisation of conditions etc
Loop_begin = data.TrialHandler(nReps=nb_training, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Loop_begin')
thisExp.addLoop(Loop_begin)  # add the loop to the experiment
thisLoop_begin = Loop_begin.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_begin.rgb)
if thisLoop_begin != None:
    for paramName in thisLoop_begin:
        exec('{} = thisLoop_begin[paramName]'.format(paramName))

for thisLoop_begin in Loop_begin:
    currentLoop = Loop_begin
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_begin.rgb)
    if thisLoop_begin != None:
        for paramName in thisLoop_begin:
            exec('{} = thisLoop_begin[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BEGIN_EXP"-------
    continueRoutine = True
    # update component parameters for each repeat
    begin_kb.keys = []
    begin_kb.rt = []
    _begin_kb_allKeys = []
    # keep track of which components have finished
    BEGIN_EXPComponents = [begin_txt, begin_kb]
    for thisComponent in BEGIN_EXPComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BEGIN_EXPClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BEGIN_EXP"-------
    while continueRoutine:
        # get current time
        t = BEGIN_EXPClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BEGIN_EXPClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *begin_txt* updates
        if begin_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_txt.frameNStart = frameN  # exact frame index
            begin_txt.tStart = t  # local t and not account for scr refresh
            begin_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_txt, 'tStartRefresh')  # time at next scr refresh
            begin_txt.setAutoDraw(True)
        
        # *begin_kb* updates
        waitOnFlip = False
        if begin_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            begin_kb.frameNStart = frameN  # exact frame index
            begin_kb.tStart = t  # local t and not account for scr refresh
            begin_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(begin_kb, 'tStartRefresh')  # time at next scr refresh
            begin_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(begin_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(begin_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if begin_kb.status == STARTED and not waitOnFlip:
            theseKeys = begin_kb.getKeys(keyList=['space'], waitRelease=False)
            _begin_kb_allKeys.extend(theseKeys)
            if len(_begin_kb_allKeys):
                begin_kb.keys = _begin_kb_allKeys[-1].name  # just the last key pressed
                begin_kb.rt = _begin_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BEGIN_EXPComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BEGIN_EXP"-------
    for thisComponent in BEGIN_EXPComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_begin.addData('begin_txt.started', begin_txt.tStartRefresh)
    Loop_begin.addData('begin_txt.stopped', begin_txt.tStopRefresh)
    # check responses
    if begin_kb.keys in ['', [], None]:  # No response was made
        begin_kb.keys = None
    Loop_begin.addData('begin_kb.keys',begin_kb.keys)
    if begin_kb.keys != None:  # we had a response
        Loop_begin.addData('begin_kb.rt', begin_kb.rt)
    Loop_begin.addData('begin_kb.started', begin_kb.tStartRefresh)
    Loop_begin.addData('begin_kb.stopped', begin_kb.tStopRefresh)
    # the Routine "BEGIN_EXP" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed nb_training repeats of 'Loop_begin'


# set up handler to look after randomisation of conditions etc
Loop_blocchi = data.TrialHandler(nReps=nb_loop_blocks, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='Loop_blocchi')
thisExp.addLoop(Loop_blocchi)  # add the loop to the experiment
thisLoop_blocchi = Loop_blocchi.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_blocchi.rgb)
if thisLoop_blocchi != None:
    for paramName in thisLoop_blocchi:
        exec('{} = thisLoop_blocchi[paramName]'.format(paramName))

for thisLoop_blocchi in Loop_blocchi:
    currentLoop = Loop_blocchi
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_blocchi.rgb)
    if thisLoop_blocchi != None:
        for paramName in thisLoop_blocchi:
            exec('{} = thisLoop_blocchi[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    loop_trials = data.TrialHandler(nReps=nb_loop_trial, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions.xlsx'),
        seed=None, name='loop_trials')
    thisExp.addLoop(loop_trials)  # add the loop to the experiment
    thisLoop_trial = loop_trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
    if thisLoop_trial != None:
        for paramName in thisLoop_trial:
            exec('{} = thisLoop_trial[paramName]'.format(paramName))
    
    for thisLoop_trial in loop_trials:
        currentLoop = loop_trials
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_trial.rgb)
        if thisLoop_trial != None:
            for paramName in thisLoop_trial:
                exec('{} = thisLoop_trial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "TRIAL_SST"-------
        continueRoutine = True
        # update component parameters for each repeat
        # Records the SSD at the beginning of each trial in milliseconds.
        thisExp.addData("SSD", ssd * 1000)  # SSD is stored in milliseconds
        
        
        
        go_img.setImage("images/" + go_file)
        stop_img.setImage("images/"  + stop_file)
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        TRIAL_SSTComponents = [dot_img, go_img, stop_img, key_resp, ISI]
        for thisComponent in TRIAL_SSTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TRIAL_SSTClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TRIAL_SST"-------
        while continueRoutine:
            # get current time
            t = TRIAL_SSTClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TRIAL_SSTClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *dot_img* updates
            if dot_img.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                dot_img.frameNStart = frameN  # exact frame index
                dot_img.tStart = t  # local t and not account for scr refresh
                dot_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dot_img, 'tStartRefresh')  # time at next scr refresh
                dot_img.setAutoDraw(True)
            if dot_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dot_img.tStartRefresh + 0.8-frameTolerance:
                    # keep track of stop time/frame for later
                    dot_img.tStop = t  # not accounting for scr refresh
                    dot_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(dot_img, 'tStopRefresh')  # time at next scr refresh
                    dot_img.setAutoDraw(False)
            
            # *go_img* updates
            if go_img.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                # keep track of start time/frame for later
                go_img.frameNStart = frameN  # exact frame index
                go_img.tStart = t  # local t and not account for scr refresh
                go_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go_img, 'tStartRefresh')  # time at next scr refresh
                go_img.setAutoDraw(True)
            if go_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > go_img.tStartRefresh + 0.9-frameTolerance:
                    # keep track of stop time/frame for later
                    go_img.tStop = t  # not accounting for scr refresh
                    go_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(go_img, 'tStopRefresh')  # time at next scr refresh
                    go_img.setAutoDraw(False)
            
            # *stop_img* updates
            if stop_img.status == NOT_STARTED and tThisFlip >= StopSignal_start + ssd-frameTolerance:
                # keep track of start time/frame for later
                stop_img.frameNStart = frameN  # exact frame index
                stop_img.tStart = t  # local t and not account for scr refresh
                stop_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stop_img, 'tStartRefresh')  # time at next scr refresh
                stop_img.setAutoDraw(True)
            if stop_img.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > stop_img.tStartRefresh + 0.07-frameTolerance:
                    # keep track of stop time/frame for later
                    stop_img.tStop = t  # not accounting for scr refresh
                    stop_img.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(stop_img, 'tStopRefresh')  # time at next scr refresh
                    stop_img.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp.tStartRefresh + 1.7-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp.tStop = t  # not accounting for scr refresh
                    key_resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                    key_resp.status = FINISHED
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['left','right'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    # was this correct?
                    if (key_resp.keys == str(correct_key)) or (key_resp.keys == correct_key):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # *ISI* period
            if ISI.status == NOT_STARTED and t >= 0-frameTolerance:
                # keep track of start time/frame for later
                ISI.frameNStart = frameN  # exact frame index
                ISI.tStart = t  # local t and not account for scr refresh
                ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                ISI.start(0.8)
            elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                ISI.complete()  # finish the static period
                ISI.tStop = ISI.tStart + 0.8  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TRIAL_SSTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TRIAL_SST"-------
        for thisComponent in TRIAL_SSTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Code to log and handle premature responses.
        if key_resp.rt:  # Checks if there was a response
            if signal == 1:  # For Stop trials
                # Checks if the response was made before the sum of StopSignal was presented
                if key_resp.rt <= (StopSignal_start + ssd):
                    thisExp.addData("premature", 1)  # Logs response as premature
                else:
                    thisExp.addData("premature", 0)  # Logs response as not premature
            elif signal == 0:  # For Go trials
                # Checks if the response was made before the Go signal was fully presented
                if key_resp.rt <= (StopSignal_start):
                    thisExp.addData("premature", 1)
                else:
                    thisExp.addData("premature", 0)
        
        # Calculates and logs the Reaction Time (RT) from the end of the Go signal to the response.
        if key_resp.rt:
            rt = (key_resp.rt - StopSignal_start) * 1000  # Converts seconds to milliseconds
            thisExp.addData("RT", rt)
        
        # Dynamic SSD adjustment:
        # Adjusts the SSD based on the participant's performance in Stop trials.
        if signal == 1:
            if len(key_resp.keys) > 0:  # If the participant responded
                ssd -= 0.050  # Decreases SSD by 50 ms to make stopping easier next time
                if ssd <= 0.050:  # Ensures SSD doesn't go below 50 ms
                    ssd = 0.050
            else:  # If the participant did not respond
                ssd += 0.050  # Increases SSD by 50 ms to make stopping harder next time
                if ssd >= 0.650:  # Ensures SSD doesn't exceed 650 ms
                    ssd = 0.650
        
            
        
        loop_trials.addData('dot_img.started', dot_img.tStartRefresh)
        loop_trials.addData('dot_img.stopped', dot_img.tStopRefresh)
        loop_trials.addData('go_img.started', go_img.tStartRefresh)
        loop_trials.addData('go_img.stopped', go_img.tStopRefresh)
        loop_trials.addData('stop_img.started', stop_img.tStartRefresh)
        loop_trials.addData('stop_img.stopped', stop_img.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(correct_key).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for loop_trials (TrialHandler)
        loop_trials.addData('key_resp.keys',key_resp.keys)
        loop_trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            loop_trials.addData('key_resp.rt', key_resp.rt)
        loop_trials.addData('key_resp.started', key_resp.tStartRefresh)
        loop_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        loop_trials.addData('ISI.started', ISI.tStart)
        loop_trials.addData('ISI.stopped', ISI.tStop)
        # the Routine "TRIAL_SST" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ITI"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        ITIComponents = [iti_txt]
        for thisComponent in ITIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ITI"-------
        while continueRoutine:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iti_txt* updates
            if iti_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iti_txt.frameNStart = frameN  # exact frame index
                iti_txt.tStart = t  # local t and not account for scr refresh
                iti_txt.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iti_txt, 'tStartRefresh')  # time at next scr refresh
                iti_txt.setAutoDraw(True)
            if iti_txt.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iti_txt.tStartRefresh + iti-frameTolerance:
                    # keep track of stop time/frame for later
                    iti_txt.tStop = t  # not accounting for scr refresh
                    iti_txt.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(iti_txt, 'tStopRefresh')  # time at next scr refresh
                    iti_txt.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ITI"-------
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        loop_trials.addData('iti_txt.started', iti_txt.tStartRefresh)
        loop_trials.addData('iti_txt.stopped', iti_txt.tStopRefresh)
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nb_loop_trial repeats of 'loop_trials'
    
    
    # ------Prepare to start Routine "BREAK"-------
    continueRoutine = True
    # update component parameters for each repeat
    # Break Between Blocks Code:
    # This code controls the transition between blocks of trials. Specifically, it
    # checks the current block number and skips the break if it's the last block,
    # allowing the experiment to proceed directly to the concluding routine.
    
    # Check if the current block is the last block in the experiment.
    # Loop_blocchi.thisRepN returns the zero-based index of the current repetition,
    # so we compare it against (nb_loop_blocks - 1) which is the index of the last block.
    if Loop_blocchi.thisRepN == (nb_loop_blocks - 1):
        Loop_blocchi.finished = True  # Ends the loop after the current block finishes
        continueRoutine = False  # Immediately ends the current routine to skip the break
    
    break_kb.keys = []
    break_kb.rt = []
    _break_kb_allKeys = []
    # keep track of which components have finished
    BREAKComponents = [break_txt, break_kb]
    for thisComponent in BREAKComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BREAKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "BREAK"-------
    while continueRoutine:
        # get current time
        t = BREAKClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BREAKClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *break_txt* updates
        if break_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_txt.frameNStart = frameN  # exact frame index
            break_txt.tStart = t  # local t and not account for scr refresh
            break_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_txt, 'tStartRefresh')  # time at next scr refresh
            break_txt.setAutoDraw(True)
        
        # *break_kb* updates
        waitOnFlip = False
        if break_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            break_kb.frameNStart = frameN  # exact frame index
            break_kb.tStart = t  # local t and not account for scr refresh
            break_kb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(break_kb, 'tStartRefresh')  # time at next scr refresh
            break_kb.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(break_kb.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(break_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if break_kb.status == STARTED and not waitOnFlip:
            theseKeys = break_kb.getKeys(keyList=['space'], waitRelease=False)
            _break_kb_allKeys.extend(theseKeys)
            if len(_break_kb_allKeys):
                break_kb.keys = _break_kb_allKeys[-1].name  # just the last key pressed
                break_kb.rt = _break_kb_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BREAKComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BREAK"-------
    for thisComponent in BREAKComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Loop_blocchi.addData('break_txt.started', break_txt.tStartRefresh)
    Loop_blocchi.addData('break_txt.stopped', break_txt.tStopRefresh)
    # the Routine "BREAK" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed nb_loop_blocks repeats of 'Loop_blocchi'


# ------Prepare to start Routine "THANKS"-------
continueRoutine = True
# update component parameters for each repeat
thanks_kb.keys = []
thanks_kb.rt = []
_thanks_kb_allKeys = []
# keep track of which components have finished
THANKSComponents = [thanks_txt, thanks_kb]
for thisComponent in THANKSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
THANKSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "THANKS"-------
while continueRoutine:
    # get current time
    t = THANKSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=THANKSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks_txt* updates
    if thanks_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_txt.frameNStart = frameN  # exact frame index
        thanks_txt.tStart = t  # local t and not account for scr refresh
        thanks_txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_txt, 'tStartRefresh')  # time at next scr refresh
        thanks_txt.setAutoDraw(True)
    
    # *thanks_kb* updates
    waitOnFlip = False
    if thanks_kb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanks_kb.frameNStart = frameN  # exact frame index
        thanks_kb.tStart = t  # local t and not account for scr refresh
        thanks_kb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanks_kb, 'tStartRefresh')  # time at next scr refresh
        thanks_kb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(thanks_kb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(thanks_kb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if thanks_kb.status == STARTED and not waitOnFlip:
        theseKeys = thanks_kb.getKeys(keyList=['space'], waitRelease=False)
        _thanks_kb_allKeys.extend(theseKeys)
        if len(_thanks_kb_allKeys):
            thanks_kb.keys = _thanks_kb_allKeys[-1].name  # just the last key pressed
            thanks_kb.rt = _thanks_kb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in THANKSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "THANKS"-------
for thisComponent in THANKSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanks_txt.started', thanks_txt.tStartRefresh)
thisExp.addData('thanks_txt.stopped', thanks_txt.tStopRefresh)
# check responses
if thanks_kb.keys in ['', [], None]:  # No response was made
    thanks_kb.keys = None
thisExp.addData('thanks_kb.keys',thanks_kb.keys)
if thanks_kb.keys != None:  # we had a response
    thisExp.addData('thanks_kb.rt', thanks_kb.rt)
thisExp.addData('thanks_kb.started', thanks_kb.tStartRefresh)
thisExp.addData('thanks_kb.stopped', thanks_kb.tStopRefresh)
thisExp.nextEntry()
# the Routine "THANKS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
