#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.1.1),
    on July 23, 2026, at 11:30
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2025.1')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (
    NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, STOPPING, FINISHED, PRESSED, 
    RELEASED, FOREVER, priority
)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.1.1'
expName = 'TSRlearn_main-blocks'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant_ID': '',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'expVersion|hid': expVersion,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1536, 864]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = "data/" + expInfo['participant_ID'] + "_" + expName + "_" + expInfo['date']
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\sync_folder\\TSRlearn-task\\psychopy_exp_files\\TSRlearn_main-blocks_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=1,
            winType='pyglet', allowGUI=False, allowStencil=True,
            monitor='testMonitor', color=[0.3255, 0.3255, 0.3255], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=False,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.3255, 0.3255, 0.3255]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    if PILOTING:
        # show a visual indicator if we're in piloting mode
        if prefs.piloting['showPilotingIndicator']:
            win.showPilotingIndicator()
        # always show the mouse in piloting mode
        if prefs.piloting['forceMouseVisible']:
            win.mouseVisible = True
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    ioSession = ioServer = eyetracker = None
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ptb'
        )
    if deviceManager.getDevice('continue_button') is None:
        # initialise continue_button
        continue_button = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button',
        )
    if deviceManager.getDevice('continue_button_3') is None:
        # initialise continue_button_3
        continue_button_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_3',
        )
    if deviceManager.getDevice('continue_button_4') is None:
        # initialise continue_button_4
        continue_button_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_4',
        )
    if deviceManager.getDevice('continue_button_5') is None:
        # initialise continue_button_5
        continue_button_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_5',
        )
    if deviceManager.getDevice('continue_button_6') is None:
        # initialise continue_button_6
        continue_button_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_6',
        )
    if deviceManager.getDevice('continue_button_7') is None:
        # initialise continue_button_7
        continue_button_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_7',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('continue_button_8') is None:
        # initialise continue_button_8
        continue_button_8 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_8',
        )
    if deviceManager.getDevice('continue_button_10') is None:
        # initialise continue_button_10
        continue_button_10 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_10',
        )
    if deviceManager.getDevice('continue_button_11') is None:
        # initialise continue_button_11
        continue_button_11 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_11',
        )
    if deviceManager.getDevice('continue_button_14') is None:
        # initialise continue_button_14
        continue_button_14 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_14',
        )
    if deviceManager.getDevice('continue_button_15') is None:
        # initialise continue_button_15
        continue_button_15 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_15',
        )
    if deviceManager.getDevice('continue_button_9') is None:
        # initialise continue_button_9
        continue_button_9 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_9',
        )
    if deviceManager.getDevice('resp_3') is None:
        # initialise resp_3
        resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_3',
        )
    if deviceManager.getDevice('resp_2') is None:
        # initialise resp_2
        resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_2',
        )
    if deviceManager.getDevice('continue_button_16') is None:
        # initialise continue_button_16
        continue_button_16 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_16',
        )
    if deviceManager.getDevice('continue_button_13') is None:
        # initialise continue_button_13
        continue_button_13 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_13',
        )
    if deviceManager.getDevice('continue_button_17') is None:
        # initialise continue_button_17
        continue_button_17 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_17',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('continue_button_18') is None:
        # initialise continue_button_18
        continue_button_18 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_18',
        )
    if deviceManager.getDevice('resp') is None:
        # initialise resp
        resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp',
        )
    if deviceManager.getDevice('resp_4') is None:
        # initialise resp_4
        resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='resp_4',
        )
    if deviceManager.getDevice('continue_button_2') is None:
        # initialise continue_button_2
        continue_button_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='continue_button_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], currentRoutine=None):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    currentRoutine : psychopy.data.Routine
        Current Routine we are in at time of pausing, if any. This object tells PsychoPy what Components to pause/play/dispatch.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='PsychToolbox',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # dispatch messages on response components
        if currentRoutine is not None:
            for comp in currentRoutine.getDispatchComponents():
                comp.device.dispatchMessages()
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    if currentRoutine is not None:
        for comp in currentRoutine.getPlaybackComponents():
            comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='PsychToolbox'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "startup_settings" ---
    # Run 'Begin Experiment' code from import_packages
    
    
    from pathlib import Path
    import csv
    import numpy as np
    import atexit
    import random
    # Run 'Begin Experiment' code from function_definitions
    # log function that saves when task events happen to log file
    def log(*msgs, sep=' ', end='\n'):
        log_file = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'] + '_print.log')
        print(*msgs, sep=sep, end=end, flush=True)
    
        # Append to log file
        with open(log_file, 'a') as f:
            f.write(sep.join(str(msg) for msg in msgs) + end)
            
    # function for setting triggers when comps appear
    # def send_onset_trigger(stim, trig_number):
        #record exact onset on the global clock 
        # win.timeOnFlip(stim, 'tStartRefresh')
        #send_trigger(trig_number)
    
    import meg_triggers
    from meg_triggers import send_trigger
    meg_triggers.set_default_duration(0.005)
    meg_triggers.set_default_reset_value(0)  # set the value the trigger channel returns to for neutral state
    # meg_triggers.enable_printing()       
       
    from ast import literal_eval
    # function that matches position keywords to position (x,y - coord) tuples
    def resolve_pos(val):
        """Return a (x,y) tuple from various spreadsheet formats."""
        #Already a tuple/list/ndarray -> normalize to tuple
        if isinstance(val, (list, tuple, np.ndarray)):
            return tuple(val)
        # Name like "left_pos" -> look up
        if isinstance(val, str):
            name = val.strip()
            if name in POS:
                return POS[name]
            # Or literal like "(-0.4, 0.2)" in the cell
            try:
                parsed = literal_eval(name)
                if isinstance(parsed, (list, tuple)) and len(parsed) == 2:
                    return tuple(parsed)
            except Exception:
                pass
                raise ValueError(f"Unrecognized position value: {val!r}")
                raise TypeError(f"Unsupported position type: {type(val)}")
    
    # Run 'Begin Experiment' code from exp_settings
    ## set main experimental variables
    
    # set exp ppt id
    participant_ID = expInfo['participant_ID']
    
    # instruction language
    language = "german" # "french" or "english"
    font_name = "Sans Sherif"
    
    # "Left" "right" etc. are the arrow keys on the key board
    # these are the keys for selecting the images in different positions
    left_key = "g"
    center_key = "r"
    right_key = "b" 
    down_key = "y"
    
    # pos of images (x-coord, y-coord)
    #left_pos   = (-0.2, 0.1)
    #right_pos  = (0.2, 0.1)
    #center_pos = (0.0, 0.1)
    prompt_pos = (0, -0.1) 
    
    # pos on retrieval trials
    leftside_retr = (-0.06,0)
    rightside_retr = (0.06,0)
    
    # pos of instructions to choose the next image
    instruc_pos = (0,0.2)
    
    # response time on learning trials
    max_response_time = 5 # [s]
     
    # feedback on learning trials
    feedback_steps  =  0.06   # steps out of 1 (percent)
    rest_jump       =  0.004 # abs distance to target pos
    animation_time   = 1    # [s]
     
    # breaks (indicate after which learning route you want task break)
    break_after_route = 4
    break_dur = 30 # [s]
    
    # replay breaks during learning
    replay_break_dur = 5
    trials_per_run = 13 # after 13 trials because we have 14 image sequences
    
    # number of learning runs
    # one run is 13 trials (learn 14-image sequence in pairs)
    n_learn_route = 4
    
    # duration of response time on retrieval trials
    retr_dur = 3 # [s]
    
    # too slow message duration
    too_slow_dur = 0.5 # [s]
    
    retr_dur_slider = 3 # [s] response time on retrieval questions with slider
    instr_newroute_dur = 1 # [s]
    image_dur_retr_new = 1
    #fix_dur_retr = 0.5 are defined in condition file
    
    # timing for fast image presentations at the end
    fast_img_dur = 0.075 # [s]
    mask_dur = 0.05 # [s]
    
    max_read_dur = 180; 
    # Run 'Begin Experiment' code from bids_logging_functions
    # BIDS event logger (no Builder BIDS components needed bc they don't work that well)
    
    class BIDSLogger:
        def __init__(self, win, clock, default_cols=None):
            self.win = win
            self.clock = clock
            self.rows = []          # list of dicts -> will become events.tsv
            self.active = {}        # stim -> row index (for duration)
            self.defaults = default_cols or {}
    
            # fixed column order (for the .tsv file)
            self.col_order = [
                "subject", "trial_type", "block_name", "sequence_name", 
                "route_num",
                "trial_num", 
                "component_label", 
                "concept_label", "concept_exemplar", 
                "onset", "duration",
                "type_of_stimulus",
                "response_time", "response",
                "response_meaning", "expected_response",
                "correct", "distance_correct"
            ]
    
        # schedule logging of onset on the *next* flip (exactly when the stim appears)
        def schedule_onset(self, stim, **extra_cols):
             # Onset: first frame it is STARTED
            if getattr(stim, "status", None) == STARTED and stim not in self.active:
                # Builder already records exact onset on flip into tStartRefresh;
                # fall back to current clock if that isn't available.
                t_on = getattr(stim, "tStartRefresh", None)
                if t_on is None:
                    t_on = self.clock.getTime()
                row = {
                    "onset": float(t_on),
                    "duration": np.nan,
                }
                row.update(self.defaults)
                row.update(extra_cols)
                self.rows.append(row)
                self.active[stim] = len(self.rows) - 1
        
        # to log the offset and therefore compute durations of components
        def mark_offset(self, stim):
            if getattr(stim, "status", None) == FINISHED and stim in self.active:
                idx = self.active.pop(stim)
                t_off = getattr(stim, "tStopRefresh", None)
                if t_off is None:
                    t_off = self.clock.getTime()
                self.rows[idx]["duration"] = float(t_off - self.rows[idx]["onset"])
                
        # log a one-shot event right now (no duration), e.g., button press
        def add_instant(self, given_name, **extra_cols):
            row = {"onset": float(self.clock.getTime()), "duration": 0.0,
                   "type_of_stimulus": given_name}
            row.update(self.defaults)
            row.update(extra_cols)
            self.rows.append(row)
    
        # write out a BIDS-like events.tsv
        def save(self, filename_base):
            out = Path(filename_base).with_suffix("")  # strip .csv/.log if present
            out = out.parent / (out.name + "_events.tsv")
    
            # union of all keys, but keep preferred order first
            all_keys = list(self.col_order)
            for r in self.rows:
                for k in r.keys():
                    if k not in all_keys:
                        all_keys.append(k)
    
            with open(out, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=all_keys, delimiter="\t", extrasaction="ignore")
                w.writeheader()
                for r in self.rows:
                    # convert Nones to "n/a" for BIDS friendliness
                    out_row = {k: ("n/a" if (r.get(k) is None or (isinstance(r.get(k), float) and np.isnan(r.get(k)))) else r.get(k))
                               for k in all_keys}
                    w.writerow(out_row)
    
            return str(out)
    # set global clock as default because we need it for timing
    bids = None
    
    # atexit autosave: runs on normal finish AND on ESC (core.quit)
    def _bids_autosave():
        try:
            if bids and hasattr(bids, "rows"):
                out = bids.save(thisExp.dataFileName)
                print(f"[autosave] BIDS events written to: {out}")
        except Exception as e:
            print(f"[autosave] Failed to save BIDS events: {e}")
    
    
    # Run 'Begin Experiment' code from set_arc_img_pos
    import math
    
    # The arc is centered on the prompt, so every top image is exactly `r` from it.
    cx, cy = prompt_pos
    r = 0.2          # distance of every top image from the prompt 
    spread_deg = 45   # how far left/right swing from straight-up 
    
    def _on_arc(angle_deg):
        a = math.radians(angle_deg)
        return (cx + r * math.cos(a), cy + r * math.sin(a))
    
    # 90 deg = straight up above the prompt; symmetric left/right around it
    center_pos = _on_arc(90)
    left_pos   = _on_arc(90 + spread_deg)
    right_pos  = _on_arc(90 - spread_deg)
    
    # --- Initialize components for Routine "instructions_01" ---
    instruction_part1 = visual.TextStim(win=win, name='instruction_part1',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    continue_button = keyboard.Keyboard(deviceName='continue_button')
    
    # --- Initialize components for Routine "instructions_02" ---
    instruction_part2 = visual.TextStim(win=win, name='instruction_part2',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part2_text
    
    
    continue_button_3 = keyboard.Keyboard(deviceName='continue_button_3')
    
    # --- Initialize components for Routine "instructions_03" ---
    instruction_part3 = visual.TextStim(win=win, name='instruction_part3',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part3_text
    
    
    continue_button_4 = keyboard.Keyboard(deviceName='continue_button_4')
    
    # --- Initialize components for Routine "instructions_04" ---
    instruction_part4 = visual.TextStim(win=win, name='instruction_part4',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part4_text
    
    
    continue_button_5 = keyboard.Keyboard(deviceName='continue_button_5')
    
    # --- Initialize components for Routine "instructions_05" ---
    instruction_part5 = visual.TextStim(win=win, name='instruction_part5',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part5_text
    
    
    continue_button_6 = keyboard.Keyboard(deviceName='continue_button_6')
    
    # --- Initialize components for Routine "instructions_06" ---
    instruction_part6 = visual.TextStim(win=win, name='instruction_part6',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part6_text
    
    
    continue_button_7 = keyboard.Keyboard(deviceName='continue_button_7')
    
    # --- Initialize components for Routine "practice_choice_display" ---
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.11, 0.11)[0], height=(0.11, 0.11)[1],
        ori=0.0, pos=[0,0], draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=1.0, depth=-1.0, interpolate=True)
    prompt_prc = visual.ImageStim(
        win=win,
        name='prompt_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    dist_01_prc = visual.ImageStim(
        win=win,
        name='dist_01_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    dist_02_prc = visual.ImageStim(
        win=win,
        name='dist_02_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    correct_prc = visual.ImageStim(
        win=win,
        name='correct_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    instructions_choose_2 = visual.TextStim(win=win, name='instructions_choose_2',
        text=None,
        font=font_name,
        pos=instruc_pos, draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "practice_feedback" ---
    polygon_7 = visual.Rect(
        win=win, name='polygon_7',
        width=(0.11, 0.11)[0], height=(0.11, 0.11)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0,0,0],
        opacity=0.0, depth=-2.0, interpolate=True)
    prompt_prc_2 = visual.ImageStim(
        win=win,
        name='prompt_prc_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    dist_01_prc_2 = visual.ImageStim(
        win=win,
        name='dist_01_prc_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    dist_02_prc_2 = visual.ImageStim(
        win=win,
        name='dist_02_prc_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    correct_prc_2 = visual.ImageStim(
        win=win,
        name='correct_prc_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    
    # --- Initialize components for Routine "instruction_retrieval_trials" ---
    instruction_part7 = visual.TextStim(win=win, name='instruction_part7',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part7_text
    
    
    continue_button_8 = keyboard.Keyboard(deviceName='continue_button_8')
    
    # --- Initialize components for Routine "instruction_retrievalques1" ---
    instruction_part10 = visual.TextStim(win=win, name='instruction_part10',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part7_text_3
    
    
    continue_button_10 = keyboard.Keyboard(deviceName='continue_button_10')
    
    # --- Initialize components for Routine "instruction_retrievalques2" ---
    instruction_part11 = visual.TextStim(win=win, name='instruction_part11',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part7_text_4
    
    
    continue_button_11 = keyboard.Keyboard(deviceName='continue_button_11')
    
    # --- Initialize components for Routine "instruction_refl_period" ---
    instruction_part12 = visual.TextStim(win=win, name='instruction_part12',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part7_text_5
    
    
    continue_button_14 = keyboard.Keyboard(deviceName='continue_button_14')
    
    # --- Initialize components for Routine "retrieval_backg_info" ---
    instruction_info = visual.TextStim(win=win, name='instruction_info',
        text=None,
        font=font_name,
        pos=(0.0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    continue_button_15 = keyboard.Keyboard(deviceName='continue_button_15')
    
    # --- Initialize components for Routine "instruction_practice_type1" ---
    instruction_part8 = visual.TextStim(win=win, name='instruction_part8',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    continue_button_9 = keyboard.Keyboard(deviceName='continue_button_9')
    
    # --- Initialize components for Routine "retrieval_type1_practice" ---
    fix_cross_retrbegin = visual.TextStim(win=win, name='fix_cross_retrbegin',
        text='',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "first_image_prc" ---
    image_1_prc = visual.ImageStim(
        win=win,
        name='image_1_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    info_example_3 = visual.ImageStim(
        win=win,
        name='info_example_3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "mask_retr1_prc" ---
    mask_img1 = visual.ImageStim(
        win=win,
        name='mask_img1', 
        image='stimuli/mask_images/mask_00.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    info_example_4 = visual.ImageStim(
        win=win,
        name='info_example_4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "second_image_prc" ---
    image_2_prc = visual.ImageStim(
        win=win,
        name='image_2_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    info_example_5 = visual.ImageStim(
        win=win,
        name='info_example_5', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "mask_retr2_prc" ---
    mask_img2 = visual.ImageStim(
        win=win,
        name='mask_img2', 
        image='stimuli/mask_images/mask_01.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.11, 0.11),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    info_example_6 = visual.ImageStim(
        win=win,
        name='info_example_6', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "reflection_period" ---
    fix_cross_reflretr_2 = visual.TextStim(win=win, name='fix_cross_reflretr_2',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text = visual.TextStim(win=win, name='text',
        text='Denken Sie jetzt über die Antworten nach. ',
        font=font_name,
        pos=(0, 0.1), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "retr_response_order_prc" ---
    yes_txt_3 = visual.TextStim(win=win, name='yes_txt_3',
        text=None,
        font=font_name,
        pos=[0,0], draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    no_txt_3 = visual.TextStim(win=win, name='no_txt_3',
        text=None,
        font=font_name,
        pos=[0,0], draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    polygon_9 = visual.Rect(
        win=win, name='polygon_9',
        width=(0.05, 0.03)[0], height=(0.05, 0.03)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=2.0,
        colorSpace='rgb', lineColor=[0.0039, 0.0039, 0.0039], fillColor=None,
        opacity=0.0, depth=-3.0, interpolate=True)
    resp_3 = keyboard.Keyboard(deviceName='resp_3')
    info_example_7 = visual.ImageStim(
        win=win,
        name='info_example_7', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    
    # --- Initialize components for Routine "retr_response_distance_prc" ---
    resp_2 = keyboard.Keyboard(deviceName='resp_2')
    info_example = visual.ImageStim(
        win=win,
        name='info_example', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.2), draggable=False, size=(0.8,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    opt_2_prc = visual.TextStim(win=win, name='opt_2_prc',
        text='2',
        font=font_name,
        pos=(0, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    opt_3_prc = visual.TextStim(win=win, name='opt_3_prc',
        text='3',
        font=font_name,
        pos=(0.05, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    opt_4_prc = visual.TextStim(win=win, name='opt_4_prc',
        text='4',
        font=font_name,
        pos=(0, -0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    opt_5_prc = visual.TextStim(win=win, name='opt_5_prc',
        text='5',
        font=font_name,
        pos=(-0.05,0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
    # --- Initialize components for Routine "retr_response_feedback" ---
    textbox_feedback = visual.TextBox2(
         win, text=None, placeholder='Type here...', font=font_name,
         ori=0.0, pos=(0, 0.2), draggable=False,      letterHeight=0.02,
         size=(0.9, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_feedback',
         depth=0, autoLog=True,
    )
    info_example_2 = visual.ImageStim(
        win=win,
        name='info_example_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.85,0.15),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    continue_button_16 = keyboard.Keyboard(deviceName='continue_button_16')
    textbox_continue = visual.TextBox2(
         win, text=None, placeholder='Type here...', font=font_name,
         ori=0.0, pos=(0, -0.15), draggable=False,      letterHeight=0.02,
         size=(0.9, 0.2), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox_continue',
         depth=-5, autoLog=True,
    )
    
    # --- Initialize components for Routine "instructions_07" ---
    instructions_part7 = visual.TextStim(win=win, name='instructions_part7',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part7_text_2
    
    
    continue_button_13 = keyboard.Keyboard(deviceName='continue_button_13')
    
    # --- Initialize components for Routine "instructions_08" ---
    instructions_part8 = visual.TextStim(win=win, name='instructions_part8',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from instruction_part8_text_2
    
    
    continue_button_17 = keyboard.Keyboard(deviceName='continue_button_17')
    
    # --- Initialize components for Routine "reset_rows_to_select" ---
    # Run 'Begin Experiment' code from define_number_trials
    
    
    def take_block(pool, ptr, n):
        if ptr + n > len(pool):
            raise RuntimeError(f"Not enough unique trials left to take {n} rows.")
        rows = pool[ptr:ptr+n]
        ptr += n
        return rows, ptr
    
    # --- Initialize components for Routine "set_learning_rows" ---
    
    # --- Initialize components for Routine "choice_display" ---
    # Run 'Begin Experiment' code from set_trigger_image
    
    
    
    polygon_4 = visual.Rect(
        win=win, name='polygon_4',
        width=(0.11, 0.11)[0], height=(0.11, 0.11)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='white', fillColor='white',
        opacity=0.0, depth=-3.0, interpolate=True)
    prompt = visual.ImageStim(
        win=win,
        name='prompt', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    dist_01 = visual.ImageStim(
        win=win,
        name='dist_01', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    dist_02 = visual.ImageStim(
        win=win,
        name='dist_02', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    correct = visual.ImageStim(
        win=win,
        name='correct', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    chooseNowText = visual.TextStim(win=win, name='chooseNowText',
        text='Bitte antworten Sie jetzt',
        font=font_name,
        pos=(0, 0.7), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-9.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "feedback" ---
    polygon_8 = visual.Rect(
        win=win, name='polygon_8',
        width=(0.11, 0.11)[0], height=(0.11, 0.11)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[0.0039, 0.0039, 0.0039], fillColor=[0.0000, 0.0000, 0.0000],
        opacity=0.0, depth=-2.0, interpolate=True)
    prompt_2 = visual.ImageStim(
        win=win,
        name='prompt_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    dist_01_2 = visual.ImageStim(
        win=win,
        name='dist_01_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    dist_02_2 = visual.ImageStim(
        win=win,
        name='dist_02_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    correct_2 = visual.ImageStim(
        win=win,
        name='correct_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    
    # --- Initialize components for Routine "too_slow_routine" ---
    tooSlowtext = visual.TextStim(win=win, name='tooSlowtext',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "rest_period" ---
    # Run 'Begin Experiment' code from set_trigger_rest
    
    
    
    fix_cross = visual.TextStim(win=win, name='fix_cross',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "instruction_retr_start" ---
    instruction_now_retr = visual.TextStim(win=win, name='instruction_now_retr',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    continue_button_18 = keyboard.Keyboard(deviceName='continue_button_18')
    
    # --- Initialize components for Routine "set_retrieval_rows" ---
    
    # --- Initialize components for Routine "retr_ITI" ---
    fix_cross_retrbegin_2 = visual.TextStim(win=win, name='fix_cross_retrbegin_2',
        text='',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "first_image" ---
    # Run 'Begin Experiment' code from set_trigger_image_1
    
    
    
    image_1 = visual.ImageStim(
        win=win,
        name='image_1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "mask_retr1" ---
    mask_img1_2 = visual.ImageStim(
        win=win,
        name='mask_img1_2', 
        image='stimuli/mask_images/mask_00.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "second_image" ---
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0,0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    
    # --- Initialize components for Routine "mask_retr2" ---
    mask_img2_2 = visual.ImageStim(
        win=win,
        name='mask_img2_2', 
        image='stimuli/mask_images/mask_01.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "reflection_period_retr" ---
    fix_cross_reflretr = visual.TextStim(win=win, name='fix_cross_reflretr',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "retr_response_order" ---
    polygon_6 = visual.Rect(
        win=win, name='polygon_6',
        width=(0.05, 0.03)[0], height=(0.05, 0.03)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.5,
        colorSpace='rgb', lineColor=[0.0039, 0.0039, 0.0039], fillColor=None,
        opacity=0.0, depth=-2.0, interpolate=True)
    yes_txt = visual.TextStim(win=win, name='yes_txt',
        text=None,
        font=font_name,
        pos=[0,0], draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    no_txt = visual.TextStim(win=win, name='no_txt',
        text=None,
        font=font_name,
        pos=[0,0], draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    chooseNowText_2 = visual.TextStim(win=win, name='chooseNowText_2',
        text='Bitte antworten Sie jetzt',
        font=font_name,
        pos=(0, 0.7), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-7.0);
    resp = keyboard.Keyboard(deviceName='resp')
    
    # --- Initialize components for Routine "too_slow_routine_1" ---
    tooSlowtext_4 = visual.TextStim(win=win, name='tooSlowtext_4',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "retr_response_distance" ---
    chooseNowText_3 = visual.TextStim(win=win, name='chooseNowText_3',
        text='Bitte antworten Sie jetzt',
        font=font_name,
        pos=(0, 0.7), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=1.0, 
        languageStyle='LTR',
        depth=-3.0);
    resp_4 = keyboard.Keyboard(deviceName='resp_4')
    opt_2 = visual.TextStim(win=win, name='opt_2',
        text='2',
        font=font_name,
        pos=(0, 0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    opt_3 = visual.TextStim(win=win, name='opt_3',
        text='3',
        font=font_name,
        pos=(0.05, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    opt_4 = visual.TextStim(win=win, name='opt_4',
        text='4',
        font=font_name,
        pos=(0, -0.05), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    opt_5 = visual.TextStim(win=win, name='opt_5',
        text='5',
        font=font_name,
        pos=(-0.05,0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "too_slow_routine_2" ---
    tooSlowtext_2 = visual.TextStim(win=win, name='tooSlowtext_2',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "retr_task_break" ---
    break_instruction = visual.TextStim(win=win, name='break_instruction',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    # Run 'Begin Experiment' code from set_break_text
    if language == "german":
        break_instruction.text = (
            "Kurze Pause. Es geht gleich weiter."
        )
    
    if language == "english":
        break_instruction.text = (
            "Short break. The task will continue soon."
        )
    
    if language == "french":
        break_instruction.text = (
            "Courte pause. La tâche reprendra bientôt."
        )
    
    
    # --- Initialize components for Routine "instructions_new_learn" ---
    instruction_text_newroute = visual.TextStim(win=win, name='instruction_text_newroute',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "instructions_end" ---
    instructions_end_text = visual.TextStim(win=win, name='instructions_end_text',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    continue_button_2 = keyboard.Keyboard(deviceName='continue_button_2')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "startup_settings" ---
    # create an object to store info about Routine startup_settings
    startup_settings = data.Routine(
        name='startup_settings',
        components=[],
    )
    startup_settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from bids_logging_functions
    # Create the logger once
    bids = BIDSLogger(
        win=win,
        clock=globalClock,
        default_cols=dict(
            subject=expInfo.get("participant")
        )
    )
    
    # write a header-only file immediately so each start creates a file
    _ = bids.save(thisExp.dataFileName)
    
    # atexit autosave: runs on normal finish AND on ESC (core.quit)
    atexit.register(_bids_autosave)
    # Run 'Begin Routine' code from refine_positions
    # make coordinates match with position description in excel file 
    POS = {
        'left':   left_pos,
        'center': center_pos,
        'right':  right_pos
    }
    
    # Map positions to keys
    # (just so it's easier to access later)
    posToKey = {
        right_pos: right_key,
        center_pos: center_key,
        left_pos: left_key
    }
    
    # Run 'Begin Routine' code from set_trigger_numbers
    # trigger numbers
    # always event - number pairs
    
    trigger_dict = {
    "start/end": 255,
    "image_selected": 51,
    "feedback": 52,
    "replay_break": 53,
    "replay_break_end": 54,
    "order_retrieval_options": 59,
    "distance_retrieval_options": 58,
    "distance_retrieval_response": 56,
    "order_retrieval_response": 55,
    "task_break_begin": 81, 
    "task_break_end": 82, 
    "reflection_per": 31,
    "reflection_per_end": 32,
    
    }
    
    # store start times for startup_settings
    startup_settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    startup_settings.tStart = globalClock.getTime(format='float')
    startup_settings.status = STARTED
    thisExp.addData('startup_settings.started', startup_settings.tStart)
    startup_settings.maxDuration = None
    # keep track of which components have finished
    startup_settingsComponents = startup_settings.components
    for thisComponent in startup_settings.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "startup_settings" ---
    startup_settings.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=startup_settings,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            startup_settings.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startup_settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startup_settings" ---
    for thisComponent in startup_settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for startup_settings
    startup_settings.tStop = globalClock.getTime(format='float')
    startup_settings.tStopRefresh = tThisFlipGlobal
    thisExp.addData('startup_settings.stopped', startup_settings.tStop)
    thisExp.nextEntry()
    # the Routine "startup_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_01" ---
    # create an object to store info about Routine instructions_01
    instructions_01 = data.Routine(
        name='instructions_01',
        components=[instruction_part1, continue_button],
    )
    instructions_01.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from set_trigger_start
    trigNumber = trigger_dict["start/end"]
    
    # Run 'Begin Routine' code from instruction_part1_text
    if language == "english": 
        instruction_part1.text = (
        "Welcome to the task.\n\n"
    "In this experiment, you will learn sequences of images.\n\n"
    "Learning phases are interleaved with retrieval phases, in which you will answer questions about the sequences you learned.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part1.text = (
    "Willkommen zu der Aufgabe.\n\n"
    "In diesem Experiment werden Sie Bildsequenzen lernen.\n\n"
    "Die Lernphasen werden mit Abrufphasen abgewechselt, in denen Sie\n"
    "Fragen zu den gelernten Sequenzen beantworten.\n\n"
    "Drücke Sie eine beliebige Taste, um weiterzumachen."
    )
    
    
    # create starting attributes for continue_button
    continue_button.keys = []
    continue_button.rt = []
    _continue_button_allKeys = []
    # store start times for instructions_01
    instructions_01.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_01.tStart = globalClock.getTime(format='float')
    instructions_01.status = STARTED
    thisExp.addData('instructions_01.started', instructions_01.tStart)
    instructions_01.maxDuration = None
    # keep track of which components have finished
    instructions_01Components = instructions_01.components
    for thisComponent in instructions_01.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_01" ---
    instructions_01.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from set_trigger_start
        
        if frameN == 0: 
            send_trigger(trigNumber)
        
        # Run 'Each Frame' code from bids_instruc
        bids.schedule_onset(instruction_part1,
                                trial_type="instruction",
                                type_of_stimulus="instruction_text",
                                component_label="instruction_part1")
        
        # *instruction_part1* updates
        
        # if instruction_part1 is starting this frame...
        if instruction_part1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part1.frameNStart = frameN  # exact frame index
            instruction_part1.tStart = t  # local t and not account for scr refresh
            instruction_part1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part1.started')
            # update status
            instruction_part1.status = STARTED
            instruction_part1.setAutoDraw(True)
        
        # if instruction_part1 is active this frame...
        if instruction_part1.status == STARTED:
            # update params
            pass
        
        # if instruction_part1 is stopping this frame...
        if instruction_part1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part1.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part1.tStop = t  # not accounting for scr refresh
                instruction_part1.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part1.stopped')
                # update status
                instruction_part1.status = FINISHED
                instruction_part1.setAutoDraw(False)
        
        # *continue_button* updates
        waitOnFlip = False
        
        # if continue_button is starting this frame...
        if continue_button.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button.frameNStart = frameN  # exact frame index
            continue_button.tStart = t  # local t and not account for scr refresh
            continue_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button.started')
            # update status
            continue_button.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button is stopping this frame...
        if continue_button.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button.tStop = t  # not accounting for scr refresh
                continue_button.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button.stopped')
                # update status
                continue_button.status = FINISHED
                continue_button.status = FINISHED
        if continue_button.status == STARTED and not waitOnFlip:
            theseKeys = continue_button.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_allKeys.extend(theseKeys)
            if len(_continue_button_allKeys):
                continue_button.keys = _continue_button_allKeys[0].name  # just the first key pressed
                continue_button.rt = _continue_button_allKeys[0].rt
                continue_button.duration = _continue_button_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_01,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_01.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_01.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_01" ---
    for thisComponent in instructions_01.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_01
    instructions_01.tStop = globalClock.getTime(format='float')
    instructions_01.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_01.stopped', instructions_01.tStop)
    # Run 'End Routine' code from bids_instruc
    bids.mark_offset(instruction_part1)
    # check responses
    if continue_button.keys in ['', [], None]:  # No response was made
        continue_button.keys = None
    thisExp.addData('continue_button.keys',continue_button.keys)
    if continue_button.keys != None:  # we had a response
        thisExp.addData('continue_button.rt', continue_button.rt)
        thisExp.addData('continue_button.duration', continue_button.duration)
    thisExp.nextEntry()
    # the Routine "instructions_01" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_02" ---
    # create an object to store info about Routine instructions_02
    instructions_02 = data.Routine(
        name='instructions_02',
        components=[instruction_part2, continue_button_3],
    )
    instructions_02.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part2_text
    if language == "english": 
        instruction_part2.text = (
    "To help you remember the order of the images, please try to connect them into a story in your head.\n\n"
    "For example: the dog is playing guitar, and then the lamp turns on.\n\n"
    "You will now first practice the learning phases.\n\n"
    "Press any key to learn how the learning phases work."
    )
    
       
    if language == "german": 
        instruction_part2.text = (
    "Um sich die Reihenfolge der Bilder besser zu merken, versuchen Sie bitte,\n"
    "die Bilder zu einer Geschichte in Ihrem Kopf zu verbinden.\n\n"
    "Zum Beispiel: Der Hund spielt Gitarre und dann geht die Lampe an.\n\n"
    "Zunächst werden Sie die Lernphasen üben.\n\n"
    "Drücken Sie eine beliebige Taste, um zu erfahren, wie die Lernphasen funktionieren."
    )
    
    
    
    
    # create starting attributes for continue_button_3
    continue_button_3.keys = []
    continue_button_3.rt = []
    _continue_button_3_allKeys = []
    # store start times for instructions_02
    instructions_02.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_02.tStart = globalClock.getTime(format='float')
    instructions_02.status = STARTED
    thisExp.addData('instructions_02.started', instructions_02.tStart)
    instructions_02.maxDuration = None
    # keep track of which components have finished
    instructions_02Components = instructions_02.components
    for thisComponent in instructions_02.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_02" ---
    instructions_02.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part2* updates
        
        # if instruction_part2 is starting this frame...
        if instruction_part2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part2.frameNStart = frameN  # exact frame index
            instruction_part2.tStart = t  # local t and not account for scr refresh
            instruction_part2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part2.started')
            # update status
            instruction_part2.status = STARTED
            instruction_part2.setAutoDraw(True)
        
        # if instruction_part2 is active this frame...
        if instruction_part2.status == STARTED:
            # update params
            pass
        
        # if instruction_part2 is stopping this frame...
        if instruction_part2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part2.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part2.tStop = t  # not accounting for scr refresh
                instruction_part2.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part2.stopped')
                # update status
                instruction_part2.status = FINISHED
                instruction_part2.setAutoDraw(False)
        
        # *continue_button_3* updates
        waitOnFlip = False
        
        # if continue_button_3 is starting this frame...
        if continue_button_3.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_3.frameNStart = frameN  # exact frame index
            continue_button_3.tStart = t  # local t and not account for scr refresh
            continue_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_3.started')
            # update status
            continue_button_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_3 is stopping this frame...
        if continue_button_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_3.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_3.tStop = t  # not accounting for scr refresh
                continue_button_3.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_3.stopped')
                # update status
                continue_button_3.status = FINISHED
                continue_button_3.status = FINISHED
        if continue_button_3.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_3.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_3_allKeys.extend(theseKeys)
            if len(_continue_button_3_allKeys):
                continue_button_3.keys = _continue_button_3_allKeys[0].name  # just the first key pressed
                continue_button_3.rt = _continue_button_3_allKeys[0].rt
                continue_button_3.duration = _continue_button_3_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_02,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_02.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_02.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_02" ---
    for thisComponent in instructions_02.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_02
    instructions_02.tStop = globalClock.getTime(format='float')
    instructions_02.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_02.stopped', instructions_02.tStop)
    # check responses
    if continue_button_3.keys in ['', [], None]:  # No response was made
        continue_button_3.keys = None
    thisExp.addData('continue_button_3.keys',continue_button_3.keys)
    if continue_button_3.keys != None:  # we had a response
        thisExp.addData('continue_button_3.rt', continue_button_3.rt)
        thisExp.addData('continue_button_3.duration', continue_button_3.duration)
    thisExp.nextEntry()
    # the Routine "instructions_02" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_03" ---
    # create an object to store info about Routine instructions_03
    instructions_03 = data.Routine(
        name='instructions_03',
        components=[instruction_part3, continue_button_4],
    )
    instructions_03.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part3_text
    if language == "english": 
        instruction_part3.text = (
    "In each learning trial, you start with the current image\n"
    "in the sequence. This image is shown at the bottom of the\n"
    "screen. At the top of the screen, you will see three\n"
    "different images. Your task is to choose which of these\n"
    "images comes next in the sequence.\n\n"
    "Press any key to continue. "
    )
    
       
    if language == "german": 
        instruction_part3.text = (
    "In jedem Lerndurchgang beginnen Sie mit dem aktuellen Bild\n"
    "der Sequenz. Dieses Bild wird unten auf dem Bildschirm angezeigt.\n\n"
    "Oben auf dem Bildschirm sehen Sie drei verschiedene Bilder.\n\n"
    "Ihre Aufgabe ist es, auszuwählen, welches Bild als\n"
    "nächstes in der Sequenz folgt.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    )
    
    
    # create starting attributes for continue_button_4
    continue_button_4.keys = []
    continue_button_4.rt = []
    _continue_button_4_allKeys = []
    # store start times for instructions_03
    instructions_03.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_03.tStart = globalClock.getTime(format='float')
    instructions_03.status = STARTED
    thisExp.addData('instructions_03.started', instructions_03.tStart)
    instructions_03.maxDuration = None
    # keep track of which components have finished
    instructions_03Components = instructions_03.components
    for thisComponent in instructions_03.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_03" ---
    instructions_03.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part3* updates
        
        # if instruction_part3 is starting this frame...
        if instruction_part3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part3.frameNStart = frameN  # exact frame index
            instruction_part3.tStart = t  # local t and not account for scr refresh
            instruction_part3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part3.started')
            # update status
            instruction_part3.status = STARTED
            instruction_part3.setAutoDraw(True)
        
        # if instruction_part3 is active this frame...
        if instruction_part3.status == STARTED:
            # update params
            pass
        
        # if instruction_part3 is stopping this frame...
        if instruction_part3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part3.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part3.tStop = t  # not accounting for scr refresh
                instruction_part3.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part3.stopped')
                # update status
                instruction_part3.status = FINISHED
                instruction_part3.setAutoDraw(False)
        
        # *continue_button_4* updates
        waitOnFlip = False
        
        # if continue_button_4 is starting this frame...
        if continue_button_4.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_4.frameNStart = frameN  # exact frame index
            continue_button_4.tStart = t  # local t and not account for scr refresh
            continue_button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_4.started')
            # update status
            continue_button_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_4 is stopping this frame...
        if continue_button_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_4.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_4.tStop = t  # not accounting for scr refresh
                continue_button_4.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_4.stopped')
                # update status
                continue_button_4.status = FINISHED
                continue_button_4.status = FINISHED
        if continue_button_4.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_4.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_4_allKeys.extend(theseKeys)
            if len(_continue_button_4_allKeys):
                continue_button_4.keys = _continue_button_4_allKeys[0].name  # just the first key pressed
                continue_button_4.rt = _continue_button_4_allKeys[0].rt
                continue_button_4.duration = _continue_button_4_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_03,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_03.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_03.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_03" ---
    for thisComponent in instructions_03.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_03
    instructions_03.tStop = globalClock.getTime(format='float')
    instructions_03.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_03.stopped', instructions_03.tStop)
    # check responses
    if continue_button_4.keys in ['', [], None]:  # No response was made
        continue_button_4.keys = None
    thisExp.addData('continue_button_4.keys',continue_button_4.keys)
    if continue_button_4.keys != None:  # we had a response
        thisExp.addData('continue_button_4.rt', continue_button_4.rt)
        thisExp.addData('continue_button_4.duration', continue_button_4.duration)
    thisExp.nextEntry()
    # the Routine "instructions_03" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_04" ---
    # create an object to store info about Routine instructions_04
    instructions_04 = data.Routine(
        name='instructions_04',
        components=[instruction_part4, continue_button_5],
    )
    instructions_04.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part4_text
    if language == "english": 
        instruction_part4.text = (
    "Use the left, right, and up keys to select the image in the left, right, or middle position.\n\n"
    "The position of the images on the screen does not indicate their order in the sequence.\n"
    "Any image can appear in any position.\n\n"
    "Please do not write down the associations you learn. Try to keep the sequences in your head.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part4.text = (
    "Verwenden Sie die linke (grün), rechte (blau) und\n"
    "obere (rot) Taste, um das Bild links, rechts oder in der\n"
    "Mitte auszuwählen. Die Position der Bilder auf dem Bildschirm\n"
    "hat keine Bedeutung für die Struktur der Sequenz.\n"
    "Jedes Bild kann an jeder Position erscheinen\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen. "
    )
    
    
    # create starting attributes for continue_button_5
    continue_button_5.keys = []
    continue_button_5.rt = []
    _continue_button_5_allKeys = []
    # store start times for instructions_04
    instructions_04.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_04.tStart = globalClock.getTime(format='float')
    instructions_04.status = STARTED
    thisExp.addData('instructions_04.started', instructions_04.tStart)
    instructions_04.maxDuration = None
    # keep track of which components have finished
    instructions_04Components = instructions_04.components
    for thisComponent in instructions_04.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_04" ---
    instructions_04.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part4* updates
        
        # if instruction_part4 is starting this frame...
        if instruction_part4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part4.frameNStart = frameN  # exact frame index
            instruction_part4.tStart = t  # local t and not account for scr refresh
            instruction_part4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part4.started')
            # update status
            instruction_part4.status = STARTED
            instruction_part4.setAutoDraw(True)
        
        # if instruction_part4 is active this frame...
        if instruction_part4.status == STARTED:
            # update params
            pass
        
        # if instruction_part4 is stopping this frame...
        if instruction_part4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part4.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part4.tStop = t  # not accounting for scr refresh
                instruction_part4.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part4.stopped')
                # update status
                instruction_part4.status = FINISHED
                instruction_part4.setAutoDraw(False)
        
        # *continue_button_5* updates
        waitOnFlip = False
        
        # if continue_button_5 is starting this frame...
        if continue_button_5.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_5.frameNStart = frameN  # exact frame index
            continue_button_5.tStart = t  # local t and not account for scr refresh
            continue_button_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_5.started')
            # update status
            continue_button_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_5 is stopping this frame...
        if continue_button_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_5.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_5.tStop = t  # not accounting for scr refresh
                continue_button_5.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_5.stopped')
                # update status
                continue_button_5.status = FINISHED
                continue_button_5.status = FINISHED
        if continue_button_5.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_5.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_5_allKeys.extend(theseKeys)
            if len(_continue_button_5_allKeys):
                continue_button_5.keys = _continue_button_5_allKeys[0].name  # just the first key pressed
                continue_button_5.rt = _continue_button_5_allKeys[0].rt
                continue_button_5.duration = _continue_button_5_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_04,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_04.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_04.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_04" ---
    for thisComponent in instructions_04.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_04
    instructions_04.tStop = globalClock.getTime(format='float')
    instructions_04.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_04.stopped', instructions_04.tStop)
    # check responses
    if continue_button_5.keys in ['', [], None]:  # No response was made
        continue_button_5.keys = None
    thisExp.addData('continue_button_5.keys',continue_button_5.keys)
    if continue_button_5.keys != None:  # we had a response
        thisExp.addData('continue_button_5.rt', continue_button_5.rt)
        thisExp.addData('continue_button_5.duration', continue_button_5.duration)
    thisExp.nextEntry()
    # the Routine "instructions_04" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_05" ---
    # create an object to store info about Routine instructions_05
    instructions_05 = data.Routine(
        name='instructions_05',
        components=[instruction_part5, continue_button_6],
    )
    instructions_05.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part5_text
    if language == "english": 
        instruction_part5.text = (
    "After you make a choice, you will receive feedback:\n"
    "The correct next image in the sequence will move down \n"
    "and replace the current image.\n\n"
    "The next learning trial then starts from this new current image.\n\n"
    "Press any key to continue. "
    )
    
       
    if language == "german": 
        instruction_part5.text = (
    "Nachdem Sie eine Auswahl getroffen haben, erhalten Sie Feedback:\n"
    "Das korrekte nächste Bild der Sequenz bewegt sich nach unten\n"
    "und ersetzt das aktuelle Bild. Der nächste Lerndurchgang beginnt\n"
    "dann mit diesem neuen aktuellen Bild.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen. "
    )
    
    
    # create starting attributes for continue_button_6
    continue_button_6.keys = []
    continue_button_6.rt = []
    _continue_button_6_allKeys = []
    # store start times for instructions_05
    instructions_05.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_05.tStart = globalClock.getTime(format='float')
    instructions_05.status = STARTED
    thisExp.addData('instructions_05.started', instructions_05.tStart)
    instructions_05.maxDuration = None
    # keep track of which components have finished
    instructions_05Components = instructions_05.components
    for thisComponent in instructions_05.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_05" ---
    instructions_05.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part5* updates
        
        # if instruction_part5 is starting this frame...
        if instruction_part5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part5.frameNStart = frameN  # exact frame index
            instruction_part5.tStart = t  # local t and not account for scr refresh
            instruction_part5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part5.started')
            # update status
            instruction_part5.status = STARTED
            instruction_part5.setAutoDraw(True)
        
        # if instruction_part5 is active this frame...
        if instruction_part5.status == STARTED:
            # update params
            pass
        
        # if instruction_part5 is stopping this frame...
        if instruction_part5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part5.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part5.tStop = t  # not accounting for scr refresh
                instruction_part5.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part5.stopped')
                # update status
                instruction_part5.status = FINISHED
                instruction_part5.setAutoDraw(False)
        
        # *continue_button_6* updates
        waitOnFlip = False
        
        # if continue_button_6 is starting this frame...
        if continue_button_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_6.frameNStart = frameN  # exact frame index
            continue_button_6.tStart = t  # local t and not account for scr refresh
            continue_button_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_6.started')
            # update status
            continue_button_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_6 is stopping this frame...
        if continue_button_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_6.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_6.tStop = t  # not accounting for scr refresh
                continue_button_6.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_6.stopped')
                # update status
                continue_button_6.status = FINISHED
                continue_button_6.status = FINISHED
        if continue_button_6.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_6.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_6_allKeys.extend(theseKeys)
            if len(_continue_button_6_allKeys):
                continue_button_6.keys = _continue_button_6_allKeys[0].name  # just the first key pressed
                continue_button_6.rt = _continue_button_6_allKeys[0].rt
                continue_button_6.duration = _continue_button_6_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_05,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_05.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_05.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_05" ---
    for thisComponent in instructions_05.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_05
    instructions_05.tStop = globalClock.getTime(format='float')
    instructions_05.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_05.stopped', instructions_05.tStop)
    # check responses
    if continue_button_6.keys in ['', [], None]:  # No response was made
        continue_button_6.keys = None
    thisExp.addData('continue_button_6.keys',continue_button_6.keys)
    if continue_button_6.keys != None:  # we had a response
        thisExp.addData('continue_button_6.rt', continue_button_6.rt)
        thisExp.addData('continue_button_6.duration', continue_button_6.duration)
    thisExp.nextEntry()
    # the Routine "instructions_05" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_06" ---
    # create an object to store info about Routine instructions_06
    instructions_06 = data.Routine(
        name='instructions_06',
        components=[instruction_part6, continue_button_7],
    )
    instructions_06.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part6_text
    if language == "english": 
        instruction_part6.text = (
    "Importantly, the image that moves down is always the correct next image, even if you chose incorrectly.\n"
    "In this way, you will learn the entire sequence step by step through trial and error.\n\n"
    "Please respond as quickly and accurately as possible.\n\n"
    "Press any key to start practicing the learning trials."
    )
    
       
    if language == "german": 
        instruction_part6.text = (
    "Wichtig ist, dass immer das korrekte nächste Bild\n"
    "nach unten bewegt wird – auch dann, wenn Sie falsch gewählt haben.\n"
    "Auf diese Weise lernen Sie die gesamte Sequenz schrittweise durch Versuch\n"
    "und Irrtum. Bitte reagieren Sie so schnell und so genau wie möglich.\n\n"
    "Drücken Sie eine beliebige Taste, um mit der Übung der Lernphasen zu beginnen. "
    
    )
    
    
    # create starting attributes for continue_button_7
    continue_button_7.keys = []
    continue_button_7.rt = []
    _continue_button_7_allKeys = []
    # store start times for instructions_06
    instructions_06.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_06.tStart = globalClock.getTime(format='float')
    instructions_06.status = STARTED
    thisExp.addData('instructions_06.started', instructions_06.tStart)
    instructions_06.maxDuration = None
    # keep track of which components have finished
    instructions_06Components = instructions_06.components
    for thisComponent in instructions_06.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_06" ---
    instructions_06.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part6* updates
        
        # if instruction_part6 is starting this frame...
        if instruction_part6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part6.frameNStart = frameN  # exact frame index
            instruction_part6.tStart = t  # local t and not account for scr refresh
            instruction_part6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part6.started')
            # update status
            instruction_part6.status = STARTED
            instruction_part6.setAutoDraw(True)
        
        # if instruction_part6 is active this frame...
        if instruction_part6.status == STARTED:
            # update params
            pass
        
        # if instruction_part6 is stopping this frame...
        if instruction_part6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part6.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part6.tStop = t  # not accounting for scr refresh
                instruction_part6.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part6.stopped')
                # update status
                instruction_part6.status = FINISHED
                instruction_part6.setAutoDraw(False)
        
        # *continue_button_7* updates
        waitOnFlip = False
        
        # if continue_button_7 is starting this frame...
        if continue_button_7.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_7.frameNStart = frameN  # exact frame index
            continue_button_7.tStart = t  # local t and not account for scr refresh
            continue_button_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_7.started')
            # update status
            continue_button_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_7 is stopping this frame...
        if continue_button_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_7.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_7.tStop = t  # not accounting for scr refresh
                continue_button_7.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_7.stopped')
                # update status
                continue_button_7.status = FINISHED
                continue_button_7.status = FINISHED
        if continue_button_7.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_7.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_7_allKeys.extend(theseKeys)
            if len(_continue_button_7_allKeys):
                continue_button_7.keys = _continue_button_7_allKeys[0].name  # just the first key pressed
                continue_button_7.rt = _continue_button_7_allKeys[0].rt
                continue_button_7.duration = _continue_button_7_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_06,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_06.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_06.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_06" ---
    for thisComponent in instructions_06.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_06
    instructions_06.tStop = globalClock.getTime(format='float')
    instructions_06.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_06.stopped', instructions_06.tStop)
    # check responses
    if continue_button_7.keys in ['', [], None]:  # No response was made
        continue_button_7.keys = None
    thisExp.addData('continue_button_7.keys',continue_button_7.keys)
    if continue_button_7.keys != None:  # we had a response
        thisExp.addData('continue_button_7.rt', continue_button_7.rt)
        thisExp.addData('continue_button_7.duration', continue_button_7.duration)
    thisExp.nextEntry()
    # the Routine "instructions_06" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_learning = data.TrialHandler2(
        name='practice_learning',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequences/main_trials_prc.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(practice_learning)  # add the loop to the experiment
    thisPractice_learning = practice_learning.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_learning.rgb)
    if thisPractice_learning != None:
        for paramName in thisPractice_learning:
            globals()[paramName] = thisPractice_learning[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisPractice_learning in practice_learning:
        practice_learning.status = STARTED
        if hasattr(thisPractice_learning, 'status'):
            thisPractice_learning.status = STARTED
        currentLoop = practice_learning
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_learning.rgb)
        if thisPractice_learning != None:
            for paramName in thisPractice_learning:
                globals()[paramName] = thisPractice_learning[paramName]
        
        # --- Prepare to start Routine "practice_choice_display" ---
        # create an object to store info about Routine practice_choice_display
        practice_choice_display = data.Routine(
            name='practice_choice_display',
            components=[polygon, prompt_prc, dist_01_prc, dist_02_prc, correct_prc, key_resp_2, instructions_choose_2],
        )
        practice_choice_display.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from Init_routeClock
        
        routClock = core.Clock()
        routClock.reset()
        
        key_resp_2_allKeys = None
        key_resp_2.clearEvents()
        polygon.setOpacity(0.0)
        polygon.setPos((0, 0))
        prompt_prc.setPos(prompt_pos)
        prompt_prc.setImage(promptFile)
        dist_01_prc.setPos([resolve_pos(dist01_pos)])
        dist_01_prc.setImage(dist_01File)
        dist_02_prc.setPos([resolve_pos(dist02_pos)])
        dist_02_prc.setImage(dist_02File)
        correct_prc.setPos([resolve_pos(correct_pos)])
        correct_prc.setImage(correctFile)
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # Run 'Begin Routine' code from get_response_parameters_3
        responded = False
        delayClock = None
        delayDone = False
        chosenPos = None
        # Run 'Begin Routine' code from set_instructions_choose_2
        if language == "english": 
            instructions_choose_2.text = ("Choose the next image in the sequence with the keys. ")
        if language == "german": 
            instructions_choose_2.text = ("Wählen Sie das nächste Bild in der Sequenz.")
        # store start times for practice_choice_display
        practice_choice_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_choice_display.tStart = globalClock.getTime(format='float')
        practice_choice_display.status = STARTED
        thisExp.addData('practice_choice_display.started', practice_choice_display.tStart)
        practice_choice_display.maxDuration = None
        # keep track of which components have finished
        practice_choice_displayComponents = practice_choice_display.components
        for thisComponent in practice_choice_display.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_choice_display" ---
        practice_choice_display.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_learning, 'status') and thisPractice_learning.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                polygon.setFillColor([0.0000, 0.0000, 0.0000], log=False)
                polygon.setLineColor([0.0039, 0.0039, 0.0039], log=False)
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # *prompt_prc* updates
            
            # if prompt_prc is starting this frame...
            if prompt_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_prc.frameNStart = frameN  # exact frame index
                prompt_prc.tStart = t  # local t and not account for scr refresh
                prompt_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_prc.started')
                # update status
                prompt_prc.status = STARTED
                prompt_prc.setAutoDraw(True)
            
            # if prompt_prc is active this frame...
            if prompt_prc.status == STARTED:
                # update params
                pass
            
            # if prompt_prc is stopping this frame...
            if prompt_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prompt_prc.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    prompt_prc.tStop = t  # not accounting for scr refresh
                    prompt_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    prompt_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prompt_prc.stopped')
                    # update status
                    prompt_prc.status = FINISHED
                    prompt_prc.setAutoDraw(False)
            
            # *dist_01_prc* updates
            
            # if dist_01_prc is starting this frame...
            if dist_01_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dist_01_prc.frameNStart = frameN  # exact frame index
                dist_01_prc.tStart = t  # local t and not account for scr refresh
                dist_01_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dist_01_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist_01_prc.started')
                # update status
                dist_01_prc.status = STARTED
                dist_01_prc.setAutoDraw(True)
            
            # if dist_01_prc is active this frame...
            if dist_01_prc.status == STARTED:
                # update params
                pass
            
            # if dist_01_prc is stopping this frame...
            if dist_01_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dist_01_prc.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    dist_01_prc.tStop = t  # not accounting for scr refresh
                    dist_01_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    dist_01_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist_01_prc.stopped')
                    # update status
                    dist_01_prc.status = FINISHED
                    dist_01_prc.setAutoDraw(False)
            
            # *dist_02_prc* updates
            
            # if dist_02_prc is starting this frame...
            if dist_02_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dist_02_prc.frameNStart = frameN  # exact frame index
                dist_02_prc.tStart = t  # local t and not account for scr refresh
                dist_02_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dist_02_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist_02_prc.started')
                # update status
                dist_02_prc.status = STARTED
                dist_02_prc.setAutoDraw(True)
            
            # if dist_02_prc is active this frame...
            if dist_02_prc.status == STARTED:
                # update params
                pass
            
            # if dist_02_prc is stopping this frame...
            if dist_02_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dist_02_prc.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    dist_02_prc.tStop = t  # not accounting for scr refresh
                    dist_02_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    dist_02_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist_02_prc.stopped')
                    # update status
                    dist_02_prc.status = FINISHED
                    dist_02_prc.setAutoDraw(False)
            
            # *correct_prc* updates
            
            # if correct_prc is starting this frame...
            if correct_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                correct_prc.frameNStart = frameN  # exact frame index
                correct_prc.tStart = t  # local t and not account for scr refresh
                correct_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(correct_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correct_prc.started')
                # update status
                correct_prc.status = STARTED
                correct_prc.setAutoDraw(True)
            
            # if correct_prc is active this frame...
            if correct_prc.status == STARTED:
                # update params
                pass
            
            # if correct_prc is stopping this frame...
            if correct_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correct_prc.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    correct_prc.tStop = t  # not accounting for scr refresh
                    correct_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    correct_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'correct_prc.stopped')
                    # update status
                    correct_prc.status = FINISHED
                    correct_prc.setAutoDraw(False)
            
            # *key_resp_2* updates
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('key_resp_2.started', t)
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                key_resp_2.clearEvents(eventType='keyboard')
            
            # if key_resp_2 is stopping this frame...
            if key_resp_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_2.tStop = t  # not accounting for scr refresh
                    key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('key_resp_2.stopped', t)
                    # update status
                    key_resp_2.status = FINISHED
                    key_resp_2.status = FINISHED
            if key_resp_2.status == STARTED:
                theseKeys = key_resp_2.getKeys(keyList=[left_key, right_key, center_key], ignoreKeys=["escape"], waitRelease=True)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
            # Run 'Each Frame' code from get_response_parameters_3
            if not responded:
                key_list = key_resp_2.getKeys(keyList=[left_key, right_key, center_key], waitRelease=False)
            
                if len(key_list) > 0:
                    responded = True
                    thisResp = key_list[0]
                    key_resp_2.keys = thisResp.name
                    key_resp_2.rt = thisResp.rt
                    key_resp_2.duration = thisResp.duration
            
            
                    if thisResp.name == left_key:
                        chosenPos = left_pos
                        KeyMeaning = "left"
                    elif thisResp.name == right_key:
                        chosenPos = right_pos
                        KeyMeaning = "right"
                    elif thisResp.name == center_key:
                        chosenPos = center_pos
                        KeyMeaning = "center"
            
                    print(chosenPos) 
                    print(KeyMeaning)
                    key_resp_2.corr = 1 if (KeyMeaning == correct_pos) else 0
                    print(key_resp_2.corr)
                    polygon.setPos(chosenPos)
                    polygon.setOpacity(1.0)
            
                    # change color of polygon for correct responses
                    if key_resp_2.corr == 1:
                        polygonCol = [0, 1, 0]
                        polygon.setFillColor(polygonCol)
                        polygon.setLineColor(polygonCol)
                    elif key_resp_2.corr == 0:
                        polygonCol = [1, -1, -1]
                        polygon.setFillColor(polygonCol)
                        polygon.setLineColor(polygonCol)
                    else:
                        polygonCol = [0, 0, 0]
                        polygon.setFillColor(polygonCol)
                        polygon.setLineColor(polygonCol)
            
                    delayClock = core.Clock()
            
            if responded and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                delayDone = True
                continueRoutine = False
            
            # *instructions_choose_2* updates
            
            # if instructions_choose_2 is starting this frame...
            if instructions_choose_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instructions_choose_2.frameNStart = frameN  # exact frame index
                instructions_choose_2.tStart = t  # local t and not account for scr refresh
                instructions_choose_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instructions_choose_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructions_choose_2.started')
                # update status
                instructions_choose_2.status = STARTED
                instructions_choose_2.setAutoDraw(True)
            
            # if instructions_choose_2 is active this frame...
            if instructions_choose_2.status == STARTED:
                # update params
                pass
            
            # if instructions_choose_2 is stopping this frame...
            if instructions_choose_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > instructions_choose_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    instructions_choose_2.tStop = t  # not accounting for scr refresh
                    instructions_choose_2.tStopRefresh = tThisFlipGlobal  # on global time
                    instructions_choose_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instructions_choose_2.stopped')
                    # update status
                    instructions_choose_2.status = FINISHED
                    instructions_choose_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_choice_display,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_choice_display.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_choice_display.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_choice_display" ---
        for thisComponent in practice_choice_display.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_choice_display
        practice_choice_display.tStop = globalClock.getTime(format='float')
        practice_choice_display.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_choice_display.stopped', practice_choice_display.tStop)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        practice_learning.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            practice_learning.addData('key_resp_2.rt', key_resp_2.rt)
            practice_learning.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "practice_choice_display" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "practice_feedback" ---
        # create an object to store info about Routine practice_feedback
        practice_feedback = data.Routine(
            name='practice_feedback',
            components=[polygon_7, prompt_prc_2, dist_01_prc_2, dist_02_prc_2, correct_prc_2],
        )
        practice_feedback.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from control__polygon
        polygon_7.setOpacity(0.0)
        if chosenPos:
            polygon_7.setPos(chosenPos)
            polygon_7.setOpacity(1.0)
            polygon_7.setFillColor(polygonCol)
            polygon_7.setLineColor(polygonCol)
        # Run 'Begin Routine' code from animation_control_js
        # Initialize animation control
        endY = prompt_pos[1]   # end y-coord of moving image
        endX = prompt_pos[0]   # end x-coord of moving image
        maxAnimationDur = round(animation_time * expInfo['frameRate'])
        animationTimer = 0      # initialize variable
        animationDone = False   # initialize variable
        moveCorrect = False     # initialize variable
        prompt_prc_2.setPos(prompt_pos)
        prompt_prc_2.setImage(promptFile)
        dist_01_prc_2.setPos([resolve_pos(dist01_pos)])
        dist_01_prc_2.setImage(dist_01File)
        dist_02_prc_2.setPos([resolve_pos(dist02_pos)])
        dist_02_prc_2.setImage(dist_02File)
        correct_prc_2.setPos([resolve_pos(correct_pos)])
        correct_prc_2.setImage(correctFile)
        # store start times for practice_feedback
        practice_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        practice_feedback.tStart = globalClock.getTime(format='float')
        practice_feedback.status = STARTED
        thisExp.addData('practice_feedback.started', practice_feedback.tStart)
        practice_feedback.maxDuration = None
        # keep track of which components have finished
        practice_feedbackComponents = practice_feedback.components
        for thisComponent in practice_feedback.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "practice_feedback" ---
        practice_feedback.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisPractice_learning, 'status') and thisPractice_learning.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from animation_control_js
            # Start animation
            if not moveCorrect and not animationDone:
                moveCorrect = True
            
            # Run animation
            if moveCorrect and not animationDone:
                animationTimer += 1
                # Current position
                current_x, current_y = correct_prc_2.pos
                # Compute direction toward target
                dx = endX - current_x
                dy = endY - current_y
                # Move a small fraction toward target
                move_fraction = feedback_steps  # fraction of remaining distance each frame
                new_x = current_x + dx * move_fraction
                new_y = current_y + dy * move_fraction
                # Update position
                correct_prc_2.setPos([new_x, new_y])
                if key_resp_2.corr:
                    polygon_7.setPos([new_x, new_y])
                # Stop when close enough to target (or if max duration exceeded)
                if (abs(dx) < rest_jump and abs(dy) < rest_jump) or animationTimer > maxAnimationDur:
                    correct_prc_2.setPos([endX, endY])
                    if key_resp_2.corr:
                        polygon_7.setPos([new_x, new_y])
                    animationDone = True
                    moveCorrect = False
                    continueRoutine = False
            
            # *polygon_7* updates
            
            # if polygon_7 is starting this frame...
            if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_7.frameNStart = frameN  # exact frame index
                polygon_7.tStart = t  # local t and not account for scr refresh
                polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_7.started')
                # update status
                polygon_7.status = STARTED
                polygon_7.setAutoDraw(True)
            
            # if polygon_7 is active this frame...
            if polygon_7.status == STARTED:
                # update params
                pass
            
            # if polygon_7 is stopping this frame...
            if polygon_7.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_7.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_7.tStop = t  # not accounting for scr refresh
                    polygon_7.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_7.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                    # update status
                    polygon_7.status = FINISHED
                    polygon_7.setAutoDraw(False)
            
            # *prompt_prc_2* updates
            
            # if prompt_prc_2 is starting this frame...
            if prompt_prc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                prompt_prc_2.frameNStart = frameN  # exact frame index
                prompt_prc_2.tStart = t  # local t and not account for scr refresh
                prompt_prc_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(prompt_prc_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'prompt_prc_2.started')
                # update status
                prompt_prc_2.status = STARTED
                prompt_prc_2.setAutoDraw(True)
            
            # if prompt_prc_2 is active this frame...
            if prompt_prc_2.status == STARTED:
                # update params
                pass
            
            # if prompt_prc_2 is stopping this frame...
            if prompt_prc_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > prompt_prc_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    prompt_prc_2.tStop = t  # not accounting for scr refresh
                    prompt_prc_2.tStopRefresh = tThisFlipGlobal  # on global time
                    prompt_prc_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'prompt_prc_2.stopped')
                    # update status
                    prompt_prc_2.status = FINISHED
                    prompt_prc_2.setAutoDraw(False)
            
            # *dist_01_prc_2* updates
            
            # if dist_01_prc_2 is starting this frame...
            if dist_01_prc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dist_01_prc_2.frameNStart = frameN  # exact frame index
                dist_01_prc_2.tStart = t  # local t and not account for scr refresh
                dist_01_prc_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dist_01_prc_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist_01_prc_2.started')
                # update status
                dist_01_prc_2.status = STARTED
                dist_01_prc_2.setAutoDraw(True)
            
            # if dist_01_prc_2 is active this frame...
            if dist_01_prc_2.status == STARTED:
                # update params
                pass
            
            # if dist_01_prc_2 is stopping this frame...
            if dist_01_prc_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dist_01_prc_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    dist_01_prc_2.tStop = t  # not accounting for scr refresh
                    dist_01_prc_2.tStopRefresh = tThisFlipGlobal  # on global time
                    dist_01_prc_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist_01_prc_2.stopped')
                    # update status
                    dist_01_prc_2.status = FINISHED
                    dist_01_prc_2.setAutoDraw(False)
            
            # *dist_02_prc_2* updates
            
            # if dist_02_prc_2 is starting this frame...
            if dist_02_prc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                dist_02_prc_2.frameNStart = frameN  # exact frame index
                dist_02_prc_2.tStart = t  # local t and not account for scr refresh
                dist_02_prc_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(dist_02_prc_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dist_02_prc_2.started')
                # update status
                dist_02_prc_2.status = STARTED
                dist_02_prc_2.setAutoDraw(True)
            
            # if dist_02_prc_2 is active this frame...
            if dist_02_prc_2.status == STARTED:
                # update params
                pass
            
            # if dist_02_prc_2 is stopping this frame...
            if dist_02_prc_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > dist_02_prc_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    dist_02_prc_2.tStop = t  # not accounting for scr refresh
                    dist_02_prc_2.tStopRefresh = tThisFlipGlobal  # on global time
                    dist_02_prc_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'dist_02_prc_2.stopped')
                    # update status
                    dist_02_prc_2.status = FINISHED
                    dist_02_prc_2.setAutoDraw(False)
            
            # *correct_prc_2* updates
            
            # if correct_prc_2 is starting this frame...
            if correct_prc_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                correct_prc_2.frameNStart = frameN  # exact frame index
                correct_prc_2.tStart = t  # local t and not account for scr refresh
                correct_prc_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(correct_prc_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'correct_prc_2.started')
                # update status
                correct_prc_2.status = STARTED
                correct_prc_2.setAutoDraw(True)
            
            # if correct_prc_2 is active this frame...
            if correct_prc_2.status == STARTED:
                # update params
                pass
            
            # if correct_prc_2 is stopping this frame...
            if correct_prc_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > correct_prc_2.tStartRefresh + max_read_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    correct_prc_2.tStop = t  # not accounting for scr refresh
                    correct_prc_2.tStopRefresh = tThisFlipGlobal  # on global time
                    correct_prc_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'correct_prc_2.stopped')
                    # update status
                    correct_prc_2.status = FINISHED
                    correct_prc_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=practice_feedback,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                practice_feedback.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in practice_feedback.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "practice_feedback" ---
        for thisComponent in practice_feedback.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for practice_feedback
        practice_feedback.tStop = globalClock.getTime(format='float')
        practice_feedback.tStopRefresh = tThisFlipGlobal
        thisExp.addData('practice_feedback.stopped', practice_feedback.tStop)
        # the Routine "practice_feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisPractice_learning as finished
        if hasattr(thisPractice_learning, 'status'):
            thisPractice_learning.status = FINISHED
        # if awaiting a pause, pause now
        if practice_learning.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            practice_learning.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'practice_learning'
    practice_learning.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instruction_retrieval_trials" ---
    # create an object to store info about Routine instruction_retrieval_trials
    instruction_retrieval_trials = data.Routine(
        name='instruction_retrieval_trials',
        components=[instruction_part7, continue_button_8],
    )
    instruction_retrieval_trials.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part7_text
    if language == "english": 
        instruction_part7.text = (
       "Good job!\n\n"
    "The learning phases are interleaved with retrieval phases, in which you will answer questions about the learned sequences.\n"
    "In a retrieval trial, you will always be presented with two images from the sequence.\n"
    "One is presented after the other\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part7.text = (
    "Gut gemacht!\n\n"
    "Die Lernphasen werden mit Abrufphasen abgewechselt, in denen Sie Fragen\n"
    "zu den gelernten Sequenzen beantworten. In den Abrufdurchgängen sehen sie\n"
    "immer zwei Bilder aus der Sequenz nacheinander.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    
    )
    
    
    # create starting attributes for continue_button_8
    continue_button_8.keys = []
    continue_button_8.rt = []
    _continue_button_8_allKeys = []
    # store start times for instruction_retrieval_trials
    instruction_retrieval_trials.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_retrieval_trials.tStart = globalClock.getTime(format='float')
    instruction_retrieval_trials.status = STARTED
    thisExp.addData('instruction_retrieval_trials.started', instruction_retrieval_trials.tStart)
    instruction_retrieval_trials.maxDuration = None
    # keep track of which components have finished
    instruction_retrieval_trialsComponents = instruction_retrieval_trials.components
    for thisComponent in instruction_retrieval_trials.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_retrieval_trials" ---
    instruction_retrieval_trials.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part7* updates
        
        # if instruction_part7 is starting this frame...
        if instruction_part7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part7.frameNStart = frameN  # exact frame index
            instruction_part7.tStart = t  # local t and not account for scr refresh
            instruction_part7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part7.started')
            # update status
            instruction_part7.status = STARTED
            instruction_part7.setAutoDraw(True)
        
        # if instruction_part7 is active this frame...
        if instruction_part7.status == STARTED:
            # update params
            pass
        
        # if instruction_part7 is stopping this frame...
        if instruction_part7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part7.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part7.tStop = t  # not accounting for scr refresh
                instruction_part7.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part7.stopped')
                # update status
                instruction_part7.status = FINISHED
                instruction_part7.setAutoDraw(False)
        
        # *continue_button_8* updates
        waitOnFlip = False
        
        # if continue_button_8 is starting this frame...
        if continue_button_8.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_8.frameNStart = frameN  # exact frame index
            continue_button_8.tStart = t  # local t and not account for scr refresh
            continue_button_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_8.started')
            # update status
            continue_button_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_8 is stopping this frame...
        if continue_button_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_8.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_8.tStop = t  # not accounting for scr refresh
                continue_button_8.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_8.stopped')
                # update status
                continue_button_8.status = FINISHED
                continue_button_8.status = FINISHED
        if continue_button_8.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_8.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_8_allKeys.extend(theseKeys)
            if len(_continue_button_8_allKeys):
                continue_button_8.keys = _continue_button_8_allKeys[0].name  # just the first key pressed
                continue_button_8.rt = _continue_button_8_allKeys[0].rt
                continue_button_8.duration = _continue_button_8_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_retrieval_trials,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_retrieval_trials.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_retrieval_trials.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_retrieval_trials" ---
    for thisComponent in instruction_retrieval_trials.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_retrieval_trials
    instruction_retrieval_trials.tStop = globalClock.getTime(format='float')
    instruction_retrieval_trials.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_retrieval_trials.stopped', instruction_retrieval_trials.tStop)
    # check responses
    if continue_button_8.keys in ['', [], None]:  # No response was made
        continue_button_8.keys = None
    thisExp.addData('continue_button_8.keys',continue_button_8.keys)
    if continue_button_8.keys != None:  # we had a response
        thisExp.addData('continue_button_8.rt', continue_button_8.rt)
        thisExp.addData('continue_button_8.duration', continue_button_8.duration)
    thisExp.nextEntry()
    # the Routine "instruction_retrieval_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_retrievalques1" ---
    # create an object to store info about Routine instruction_retrievalques1
    instruction_retrievalques1 = data.Routine(
        name='instruction_retrievalques1',
        components=[instruction_part10, continue_button_10],
    )
    instruction_retrievalques1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part7_text_3
    if language == "english": 
        instruction_part10.text = (
       "Retrieval Part 1: Order\n\n"
    "After seeing the two images, your first task is to indicate\n"
    "if the two images were presented in the learned sequence in the presented order\n"
    "or not. For this, use the left (green) and right (blue) button\n."
    "The assignment of correct / incorrect to left / right can change, so please\n"
    "check on the screen which side corresponds to correct / incorrect on this trial.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part10.text = (
    "Abruf Teil 1: Reihenfolge\n\n"
    "Nachdem die beiden Bilder präsentiert wurden, ist die erste Aufgabe, \n"
    "anzugeben, ob die beiden Bilder in der gelernten Sequenz in der präsentierten\n"
    "Reihenfolge vorkamen oder nicht. Dafür nutzen Sie die linke (grün) und rechte\n"
    " (blau) Taste für ja/nein. Die Zuordnung von ja/nein zu links/rechts verändert\n"
    "sich je nach Durchgang, daher schauen sie bitte auf dem Bildschirm nach, \n"
    "welche Seite welcher Antwortoption zuzuordnen ist.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    
    )
    
    
    # create starting attributes for continue_button_10
    continue_button_10.keys = []
    continue_button_10.rt = []
    _continue_button_10_allKeys = []
    # store start times for instruction_retrievalques1
    instruction_retrievalques1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_retrievalques1.tStart = globalClock.getTime(format='float')
    instruction_retrievalques1.status = STARTED
    thisExp.addData('instruction_retrievalques1.started', instruction_retrievalques1.tStart)
    instruction_retrievalques1.maxDuration = None
    # keep track of which components have finished
    instruction_retrievalques1Components = instruction_retrievalques1.components
    for thisComponent in instruction_retrievalques1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_retrievalques1" ---
    instruction_retrievalques1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part10* updates
        
        # if instruction_part10 is starting this frame...
        if instruction_part10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part10.frameNStart = frameN  # exact frame index
            instruction_part10.tStart = t  # local t and not account for scr refresh
            instruction_part10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part10.started')
            # update status
            instruction_part10.status = STARTED
            instruction_part10.setAutoDraw(True)
        
        # if instruction_part10 is active this frame...
        if instruction_part10.status == STARTED:
            # update params
            pass
        
        # if instruction_part10 is stopping this frame...
        if instruction_part10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part10.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part10.tStop = t  # not accounting for scr refresh
                instruction_part10.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part10.stopped')
                # update status
                instruction_part10.status = FINISHED
                instruction_part10.setAutoDraw(False)
        
        # *continue_button_10* updates
        waitOnFlip = False
        
        # if continue_button_10 is starting this frame...
        if continue_button_10.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_10.frameNStart = frameN  # exact frame index
            continue_button_10.tStart = t  # local t and not account for scr refresh
            continue_button_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_10.started')
            # update status
            continue_button_10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_10 is stopping this frame...
        if continue_button_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_10.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_10.tStop = t  # not accounting for scr refresh
                continue_button_10.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_10.stopped')
                # update status
                continue_button_10.status = FINISHED
                continue_button_10.status = FINISHED
        if continue_button_10.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_10.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_10_allKeys.extend(theseKeys)
            if len(_continue_button_10_allKeys):
                continue_button_10.keys = _continue_button_10_allKeys[0].name  # just the first key pressed
                continue_button_10.rt = _continue_button_10_allKeys[0].rt
                continue_button_10.duration = _continue_button_10_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_retrievalques1,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_retrievalques1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_retrievalques1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_retrievalques1" ---
    for thisComponent in instruction_retrievalques1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_retrievalques1
    instruction_retrievalques1.tStop = globalClock.getTime(format='float')
    instruction_retrievalques1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_retrievalques1.stopped', instruction_retrievalques1.tStop)
    # check responses
    if continue_button_10.keys in ['', [], None]:  # No response was made
        continue_button_10.keys = None
    thisExp.addData('continue_button_10.keys',continue_button_10.keys)
    if continue_button_10.keys != None:  # we had a response
        thisExp.addData('continue_button_10.rt', continue_button_10.rt)
        thisExp.addData('continue_button_10.duration', continue_button_10.duration)
    thisExp.nextEntry()
    # the Routine "instruction_retrievalques1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_retrievalques2" ---
    # create an object to store info about Routine instruction_retrievalques2
    instruction_retrievalques2 = data.Routine(
        name='instruction_retrievalques2',
        components=[instruction_part11, continue_button_11],
    )
    instruction_retrievalques2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part7_text_4
    if language == "english": 
        instruction_part11.text = (
       "Retrieval Part 2: Distance\n\n"
    "After seeing the two images, your first task is to indicate\n"
    "if the two images were presented in the learned sequence in the presented order\n"
    "or not. For this, use the left (green) and right (blue) button\n."
    "The assignment of correct / incorrect to left / right can change, so please\n"
    "check on the screen which side corresponds to correct / incorrect on this trial.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part11.text = (
    "Abruf Teil 2: Distanz\n\n"
    "Unmittelbar nach der Antwort, ob die präsentierte Reihenfolge\n"
    "der Bilder der Sequenzreihenfolge entspricht, soll eine weitere Frage\n"
    "beantworten werden. Und zwar sollen Sie angeben, wie weit die beiden Bilder\n"
    "in der Sequenz voneinander entfernt liegen. Mögliche Distanzen sind 2 \n"
    "(ein Bild liegt dazwischen) bis 5 (4 Bilder liegen dazwischen).\n"
    "Antworten sie mit den vier Tasten, die Tastenbelegungen erscheinen wieder auf dem Bildschirm.\n\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    
    )
    
    
    # create starting attributes for continue_button_11
    continue_button_11.keys = []
    continue_button_11.rt = []
    _continue_button_11_allKeys = []
    # store start times for instruction_retrievalques2
    instruction_retrievalques2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_retrievalques2.tStart = globalClock.getTime(format='float')
    instruction_retrievalques2.status = STARTED
    thisExp.addData('instruction_retrievalques2.started', instruction_retrievalques2.tStart)
    instruction_retrievalques2.maxDuration = None
    # keep track of which components have finished
    instruction_retrievalques2Components = instruction_retrievalques2.components
    for thisComponent in instruction_retrievalques2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_retrievalques2" ---
    instruction_retrievalques2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part11* updates
        
        # if instruction_part11 is starting this frame...
        if instruction_part11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part11.frameNStart = frameN  # exact frame index
            instruction_part11.tStart = t  # local t and not account for scr refresh
            instruction_part11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part11.started')
            # update status
            instruction_part11.status = STARTED
            instruction_part11.setAutoDraw(True)
        
        # if instruction_part11 is active this frame...
        if instruction_part11.status == STARTED:
            # update params
            pass
        
        # if instruction_part11 is stopping this frame...
        if instruction_part11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part11.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part11.tStop = t  # not accounting for scr refresh
                instruction_part11.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part11.stopped')
                # update status
                instruction_part11.status = FINISHED
                instruction_part11.setAutoDraw(False)
        
        # *continue_button_11* updates
        waitOnFlip = False
        
        # if continue_button_11 is starting this frame...
        if continue_button_11.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_11.frameNStart = frameN  # exact frame index
            continue_button_11.tStart = t  # local t and not account for scr refresh
            continue_button_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_11.started')
            # update status
            continue_button_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_11 is stopping this frame...
        if continue_button_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_11.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_11.tStop = t  # not accounting for scr refresh
                continue_button_11.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_11.stopped')
                # update status
                continue_button_11.status = FINISHED
                continue_button_11.status = FINISHED
        if continue_button_11.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_11.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_11_allKeys.extend(theseKeys)
            if len(_continue_button_11_allKeys):
                continue_button_11.keys = _continue_button_11_allKeys[0].name  # just the first key pressed
                continue_button_11.rt = _continue_button_11_allKeys[0].rt
                continue_button_11.duration = _continue_button_11_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_retrievalques2,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_retrievalques2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_retrievalques2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_retrievalques2" ---
    for thisComponent in instruction_retrievalques2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_retrievalques2
    instruction_retrievalques2.tStop = globalClock.getTime(format='float')
    instruction_retrievalques2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_retrievalques2.stopped', instruction_retrievalques2.tStop)
    # check responses
    if continue_button_11.keys in ['', [], None]:  # No response was made
        continue_button_11.keys = None
    thisExp.addData('continue_button_11.keys',continue_button_11.keys)
    if continue_button_11.keys != None:  # we had a response
        thisExp.addData('continue_button_11.rt', continue_button_11.rt)
        thisExp.addData('continue_button_11.duration', continue_button_11.duration)
    thisExp.nextEntry()
    # the Routine "instruction_retrievalques2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_refl_period" ---
    # create an object to store info about Routine instruction_refl_period
    instruction_refl_period = data.Routine(
        name='instruction_refl_period',
        components=[instruction_part12, continue_button_14],
    )
    instruction_refl_period.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part7_text_5
    if language == "english": 
        instruction_part12.text = (
       "Retrieval: Reflection Period\n\n"
    "After seeing the two images, your first task is to indicate\n"
    "if the two images were presented in the learned sequence in the presented order\n"
    "or not. For this, use the left (green) and right (blue) button\n."
    "The assignment of correct / incorrect to left / right can change, so please\n"
    "check on the screen which side corresponds to correct / incorrect on this trial.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instruction_part12.text = (
    "Abruf: Reflektionsperiode\n\n"
    "Vor der Antwort auf die Reihenfolgen- und Distanzfrage liegt eine\n"
    "kurze Reflektionsperiode. Hier wird nur ein Fixationskreuz präsentiert und Sie\n"
    "sollen schon einmal überlegen, ob die Bilder in dieser Reihenfolge in der\n"
    "Sequenz auftraten (Antwort 1) und welche Distanz die Bilder in der Sequenz haben\n"
    "(Antwort 2). Es ist wichtig, dass sie hier schon über die Fragen nachdenken,\n"
    "da die Antwortzeiten für die Reihenfolgen und Distanzfragen relativ kurz sind.\n\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    
    )
    
    
    # create starting attributes for continue_button_14
    continue_button_14.keys = []
    continue_button_14.rt = []
    _continue_button_14_allKeys = []
    # store start times for instruction_refl_period
    instruction_refl_period.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_refl_period.tStart = globalClock.getTime(format='float')
    instruction_refl_period.status = STARTED
    thisExp.addData('instruction_refl_period.started', instruction_refl_period.tStart)
    instruction_refl_period.maxDuration = None
    # keep track of which components have finished
    instruction_refl_periodComponents = instruction_refl_period.components
    for thisComponent in instruction_refl_period.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_refl_period" ---
    instruction_refl_period.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part12* updates
        
        # if instruction_part12 is starting this frame...
        if instruction_part12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part12.frameNStart = frameN  # exact frame index
            instruction_part12.tStart = t  # local t and not account for scr refresh
            instruction_part12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part12.started')
            # update status
            instruction_part12.status = STARTED
            instruction_part12.setAutoDraw(True)
        
        # if instruction_part12 is active this frame...
        if instruction_part12.status == STARTED:
            # update params
            pass
        
        # if instruction_part12 is stopping this frame...
        if instruction_part12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part12.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part12.tStop = t  # not accounting for scr refresh
                instruction_part12.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part12.stopped')
                # update status
                instruction_part12.status = FINISHED
                instruction_part12.setAutoDraw(False)
        
        # *continue_button_14* updates
        waitOnFlip = False
        
        # if continue_button_14 is starting this frame...
        if continue_button_14.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            continue_button_14.frameNStart = frameN  # exact frame index
            continue_button_14.tStart = t  # local t and not account for scr refresh
            continue_button_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_14.started')
            # update status
            continue_button_14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_14 is stopping this frame...
        if continue_button_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_14.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_14.tStop = t  # not accounting for scr refresh
                continue_button_14.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_14.stopped')
                # update status
                continue_button_14.status = FINISHED
                continue_button_14.status = FINISHED
        if continue_button_14.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_14.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_14_allKeys.extend(theseKeys)
            if len(_continue_button_14_allKeys):
                continue_button_14.keys = _continue_button_14_allKeys[0].name  # just the first key pressed
                continue_button_14.rt = _continue_button_14_allKeys[0].rt
                continue_button_14.duration = _continue_button_14_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_refl_period,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_refl_period.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_refl_period.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_refl_period" ---
    for thisComponent in instruction_refl_period.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_refl_period
    instruction_refl_period.tStop = globalClock.getTime(format='float')
    instruction_refl_period.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_refl_period.stopped', instruction_refl_period.tStop)
    # check responses
    if continue_button_14.keys in ['', [], None]:  # No response was made
        continue_button_14.keys = None
    thisExp.addData('continue_button_14.keys',continue_button_14.keys)
    if continue_button_14.keys != None:  # we had a response
        thisExp.addData('continue_button_14.rt', continue_button_14.rt)
        thisExp.addData('continue_button_14.duration', continue_button_14.duration)
    thisExp.nextEntry()
    # the Routine "instruction_refl_period" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "retrieval_backg_info" ---
    # create an object to store info about Routine retrieval_backg_info
    retrieval_backg_info = data.Routine(
        name='retrieval_backg_info',
        components=[instruction_info, continue_button_15],
    )
    retrieval_backg_info.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_info_text
    
    if language == "english": 
        instruction_info.text = (
        "In the practice of the retrieval trials, you will get some background information on how the sequence of images is structured.\n"
        "This will appear at the bottom.\n\nIn the main trials, there will be no additional information.\n" 
        "You should extract this information from the pairwise associations learned.\n\n"
        "Press any key to continue."
    )  
    if language == "german": 
        instruction_info.text = (
    "In der Übungsphase zu den Abrufdurchgängen erhalten Sie einige\n"
    "Hintergrundinformationen darüber, wie die Bildsequenz aufgebaut ist.\n"
    "Dies wird unten am Bildschirm angezeigt. In der Hauptaufgabe gibt\n"
    "es keine zusätzlichen Informationen. Sie sollten diese Informationen\n"
    "aus den gelernten paarweisen Assoziationen extrahieren.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    )  
    # create starting attributes for continue_button_15
    continue_button_15.keys = []
    continue_button_15.rt = []
    _continue_button_15_allKeys = []
    # store start times for retrieval_backg_info
    retrieval_backg_info.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    retrieval_backg_info.tStart = globalClock.getTime(format='float')
    retrieval_backg_info.status = STARTED
    thisExp.addData('retrieval_backg_info.started', retrieval_backg_info.tStart)
    retrieval_backg_info.maxDuration = None
    # keep track of which components have finished
    retrieval_backg_infoComponents = retrieval_backg_info.components
    for thisComponent in retrieval_backg_info.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "retrieval_backg_info" ---
    retrieval_backg_info.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_info* updates
        
        # if instruction_info is starting this frame...
        if instruction_info.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_info.frameNStart = frameN  # exact frame index
            instruction_info.tStart = t  # local t and not account for scr refresh
            instruction_info.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_info, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_info.started')
            # update status
            instruction_info.status = STARTED
            instruction_info.setAutoDraw(True)
        
        # if instruction_info is active this frame...
        if instruction_info.status == STARTED:
            # update params
            pass
        
        # if instruction_info is stopping this frame...
        if instruction_info.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_info.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_info.tStop = t  # not accounting for scr refresh
                instruction_info.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_info.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_info.stopped')
                # update status
                instruction_info.status = FINISHED
                instruction_info.setAutoDraw(False)
        
        # *continue_button_15* updates
        waitOnFlip = False
        
        # if continue_button_15 is starting this frame...
        if continue_button_15.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_15.frameNStart = frameN  # exact frame index
            continue_button_15.tStart = t  # local t and not account for scr refresh
            continue_button_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_15.started')
            # update status
            continue_button_15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_15 is stopping this frame...
        if continue_button_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_15.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_15.tStop = t  # not accounting for scr refresh
                continue_button_15.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_15.stopped')
                # update status
                continue_button_15.status = FINISHED
                continue_button_15.status = FINISHED
        if continue_button_15.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_15.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_15_allKeys.extend(theseKeys)
            if len(_continue_button_15_allKeys):
                continue_button_15.keys = _continue_button_15_allKeys[0].name  # just the first key pressed
                continue_button_15.rt = _continue_button_15_allKeys[0].rt
                continue_button_15.duration = _continue_button_15_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=retrieval_backg_info,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            retrieval_backg_info.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in retrieval_backg_info.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "retrieval_backg_info" ---
    for thisComponent in retrieval_backg_info.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for retrieval_backg_info
    retrieval_backg_info.tStop = globalClock.getTime(format='float')
    retrieval_backg_info.tStopRefresh = tThisFlipGlobal
    thisExp.addData('retrieval_backg_info.stopped', retrieval_backg_info.tStop)
    # check responses
    if continue_button_15.keys in ['', [], None]:  # No response was made
        continue_button_15.keys = None
    thisExp.addData('continue_button_15.keys',continue_button_15.keys)
    if continue_button_15.keys != None:  # we had a response
        thisExp.addData('continue_button_15.rt', continue_button_15.rt)
        thisExp.addData('continue_button_15.duration', continue_button_15.duration)
    thisExp.nextEntry()
    # the Routine "retrieval_backg_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction_practice_type1" ---
    # create an object to store info about Routine instruction_practice_type1
    instruction_practice_type1 = data.Routine(
        name='instruction_practice_type1',
        components=[instruction_part8, continue_button_9],
    )
    instruction_practice_type1.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part8_text
    if language == "english": 
        instruction_part8.text = (
        "You are now ready to practice the retrieval trials.\n\n"
        "Plese remember to use the periods after the two images were shown to think\n"
        "about the order and distance questions.\n\n"
        "Press any key to start the retrieval practice")  
    if language == "german": 
        instruction_part8.text = (
        "Sie sind nun bereit, die Abrufdurchgänge zu üben.\n\n"
        "Denken Sie daran, in der kurzen Pause nach dem Präsentieren der Bilder,\n"
        "über die Reihenfolgefrage und die Distanzfrage nachzudenken.\n\n\n"
        "Drücken Sie eine beliebige Taste, um das Üben des Abrufs zu starten."
    )
    # create starting attributes for continue_button_9
    continue_button_9.keys = []
    continue_button_9.rt = []
    _continue_button_9_allKeys = []
    # Run 'Begin Routine' code from initialize_practice_errors
    practice_errors = 0
    # store start times for instruction_practice_type1
    instruction_practice_type1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instruction_practice_type1.tStart = globalClock.getTime(format='float')
    instruction_practice_type1.status = STARTED
    thisExp.addData('instruction_practice_type1.started', instruction_practice_type1.tStart)
    instruction_practice_type1.maxDuration = None
    # keep track of which components have finished
    instruction_practice_type1Components = instruction_practice_type1.components
    for thisComponent in instruction_practice_type1.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instruction_practice_type1" ---
    instruction_practice_type1.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_part8* updates
        
        # if instruction_part8 is starting this frame...
        if instruction_part8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_part8.frameNStart = frameN  # exact frame index
            instruction_part8.tStart = t  # local t and not account for scr refresh
            instruction_part8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_part8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_part8.started')
            # update status
            instruction_part8.status = STARTED
            instruction_part8.setAutoDraw(True)
        
        # if instruction_part8 is active this frame...
        if instruction_part8.status == STARTED:
            # update params
            pass
        
        # if instruction_part8 is stopping this frame...
        if instruction_part8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instruction_part8.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instruction_part8.tStop = t  # not accounting for scr refresh
                instruction_part8.tStopRefresh = tThisFlipGlobal  # on global time
                instruction_part8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_part8.stopped')
                # update status
                instruction_part8.status = FINISHED
                instruction_part8.setAutoDraw(False)
        
        # *continue_button_9* updates
        waitOnFlip = False
        
        # if continue_button_9 is starting this frame...
        if continue_button_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_9.frameNStart = frameN  # exact frame index
            continue_button_9.tStart = t  # local t and not account for scr refresh
            continue_button_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_9.started')
            # update status
            continue_button_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_9 is stopping this frame...
        if continue_button_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_9.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_9.tStop = t  # not accounting for scr refresh
                continue_button_9.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_9.stopped')
                # update status
                continue_button_9.status = FINISHED
                continue_button_9.status = FINISHED
        if continue_button_9.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_9.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_9_allKeys.extend(theseKeys)
            if len(_continue_button_9_allKeys):
                continue_button_9.keys = _continue_button_9_allKeys[0].name  # just the first key pressed
                continue_button_9.rt = _continue_button_9_allKeys[0].rt
                continue_button_9.duration = _continue_button_9_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instruction_practice_type1,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instruction_practice_type1.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction_practice_type1.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_practice_type1" ---
    for thisComponent in instruction_practice_type1.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instruction_practice_type1
    instruction_practice_type1.tStop = globalClock.getTime(format='float')
    instruction_practice_type1.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instruction_practice_type1.stopped', instruction_practice_type1.tStop)
    # check responses
    if continue_button_9.keys in ['', [], None]:  # No response was made
        continue_button_9.keys = None
    thisExp.addData('continue_button_9.keys',continue_button_9.keys)
    if continue_button_9.keys != None:  # we had a response
        thisExp.addData('continue_button_9.rt', continue_button_9.rt)
        thisExp.addData('continue_button_9.duration', continue_button_9.duration)
    thisExp.nextEntry()
    # the Routine "instruction_practice_type1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    retrieval_prc_loop = data.TrialHandler2(
        name='retrieval_prc_loop',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequences/retr_trials_prc_03.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(retrieval_prc_loop)  # add the loop to the experiment
    thisRetrieval_prc_loop = retrieval_prc_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRetrieval_prc_loop.rgb)
    if thisRetrieval_prc_loop != None:
        for paramName in thisRetrieval_prc_loop:
            globals()[paramName] = thisRetrieval_prc_loop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisRetrieval_prc_loop in retrieval_prc_loop:
        retrieval_prc_loop.status = STARTED
        if hasattr(thisRetrieval_prc_loop, 'status'):
            thisRetrieval_prc_loop.status = STARTED
        currentLoop = retrieval_prc_loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisRetrieval_prc_loop.rgb)
        if thisRetrieval_prc_loop != None:
            for paramName in thisRetrieval_prc_loop:
                globals()[paramName] = thisRetrieval_prc_loop[paramName]
        
        # set up handler to look after randomisation of conditions etc
        retry_loop = data.TrialHandler2(
            name='retry_loop',
            nReps=999.0, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(retry_loop)  # add the loop to the experiment
        thisRetry_loop = retry_loop.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRetry_loop.rgb)
        if thisRetry_loop != None:
            for paramName in thisRetry_loop:
                globals()[paramName] = thisRetry_loop[paramName]
        
        for thisRetry_loop in retry_loop:
            retry_loop.status = STARTED
            if hasattr(thisRetry_loop, 'status'):
                thisRetry_loop.status = STARTED
            currentLoop = retry_loop
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisRetry_loop.rgb)
            if thisRetry_loop != None:
                for paramName in thisRetry_loop:
                    globals()[paramName] = thisRetry_loop[paramName]
            
            # --- Prepare to start Routine "retrieval_type1_practice" ---
            # create an object to store info about Routine retrieval_type1_practice
            retrieval_type1_practice = data.Routine(
                name='retrieval_type1_practice',
                components=[fix_cross_retrbegin],
            )
            retrieval_type1_practice.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            fix_cross_retrbegin.setText('+')
            # store start times for retrieval_type1_practice
            retrieval_type1_practice.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            retrieval_type1_practice.tStart = globalClock.getTime(format='float')
            retrieval_type1_practice.status = STARTED
            thisExp.addData('retrieval_type1_practice.started', retrieval_type1_practice.tStart)
            retrieval_type1_practice.maxDuration = None
            # keep track of which components have finished
            retrieval_type1_practiceComponents = retrieval_type1_practice.components
            for thisComponent in retrieval_type1_practice.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "retrieval_type1_practice" ---
            retrieval_type1_practice.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix_cross_retrbegin* updates
                
                # if fix_cross_retrbegin is starting this frame...
                if fix_cross_retrbegin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_cross_retrbegin.frameNStart = frameN  # exact frame index
                    fix_cross_retrbegin.tStart = t  # local t and not account for scr refresh
                    fix_cross_retrbegin.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_cross_retrbegin, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_retrbegin.started')
                    # update status
                    fix_cross_retrbegin.status = STARTED
                    fix_cross_retrbegin.setAutoDraw(True)
                
                # if fix_cross_retrbegin is active this frame...
                if fix_cross_retrbegin.status == STARTED:
                    # update params
                    pass
                
                # if fix_cross_retrbegin is stopping this frame...
                if fix_cross_retrbegin.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_cross_retrbegin.tStartRefresh + iti_dur_retr-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_cross_retrbegin.tStop = t  # not accounting for scr refresh
                        fix_cross_retrbegin.tStopRefresh = tThisFlipGlobal  # on global time
                        fix_cross_retrbegin.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross_retrbegin.stopped')
                        # update status
                        fix_cross_retrbegin.status = FINISHED
                        fix_cross_retrbegin.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=retrieval_type1_practice,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    retrieval_type1_practice.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in retrieval_type1_practice.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "retrieval_type1_practice" ---
            for thisComponent in retrieval_type1_practice.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for retrieval_type1_practice
            retrieval_type1_practice.tStop = globalClock.getTime(format='float')
            retrieval_type1_practice.tStopRefresh = tThisFlipGlobal
            thisExp.addData('retrieval_type1_practice.stopped', retrieval_type1_practice.tStop)
            # the Routine "retrieval_type1_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "first_image_prc" ---
            # create an object to store info about Routine first_image_prc
            first_image_prc = data.Routine(
                name='first_image_prc',
                components=[image_1_prc, info_example_3],
            )
            first_image_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_1_prc.setImage(img_first)
            info_example_3.setImage(ImageExamplePath)
            # store start times for first_image_prc
            first_image_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            first_image_prc.tStart = globalClock.getTime(format='float')
            first_image_prc.status = STARTED
            thisExp.addData('first_image_prc.started', first_image_prc.tStart)
            first_image_prc.maxDuration = None
            # keep track of which components have finished
            first_image_prcComponents = first_image_prc.components
            for thisComponent in first_image_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "first_image_prc" ---
            first_image_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_1_prc* updates
                
                # if image_1_prc is starting this frame...
                if image_1_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_1_prc.frameNStart = frameN  # exact frame index
                    image_1_prc.tStart = t  # local t and not account for scr refresh
                    image_1_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_1_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_1_prc.started')
                    # update status
                    image_1_prc.status = STARTED
                    image_1_prc.setAutoDraw(True)
                
                # if image_1_prc is active this frame...
                if image_1_prc.status == STARTED:
                    # update params
                    pass
                
                # if image_1_prc is stopping this frame...
                if image_1_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_1_prc.tStartRefresh + image_dur_retr_new + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_1_prc.tStop = t  # not accounting for scr refresh
                        image_1_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        image_1_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_1_prc.stopped')
                        # update status
                        image_1_prc.status = FINISHED
                        image_1_prc.setAutoDraw(False)
                
                # *info_example_3* updates
                
                # if info_example_3 is starting this frame...
                if info_example_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example_3.frameNStart = frameN  # exact frame index
                    info_example_3.tStart = t  # local t and not account for scr refresh
                    info_example_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_3.started')
                    # update status
                    info_example_3.status = STARTED
                    info_example_3.setAutoDraw(True)
                
                # if info_example_3 is active this frame...
                if info_example_3.status == STARTED:
                    # update params
                    pass
                
                # if info_example_3 is stopping this frame...
                if info_example_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_3.tStartRefresh + image_dur_retr_new + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_3.tStop = t  # not accounting for scr refresh
                        info_example_3.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_3.stopped')
                        # update status
                        info_example_3.status = FINISHED
                        info_example_3.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=first_image_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    first_image_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in first_image_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "first_image_prc" ---
            for thisComponent in first_image_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for first_image_prc
            first_image_prc.tStop = globalClock.getTime(format='float')
            first_image_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('first_image_prc.stopped', first_image_prc.tStop)
            # the Routine "first_image_prc" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "mask_retr1_prc" ---
            # create an object to store info about Routine mask_retr1_prc
            mask_retr1_prc = data.Routine(
                name='mask_retr1_prc',
                components=[mask_img1, info_example_4],
            )
            mask_retr1_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            info_example_4.setImage(ImageExamplePath)
            # store start times for mask_retr1_prc
            mask_retr1_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            mask_retr1_prc.tStart = globalClock.getTime(format='float')
            mask_retr1_prc.status = STARTED
            thisExp.addData('mask_retr1_prc.started', mask_retr1_prc.tStart)
            mask_retr1_prc.maxDuration = None
            # keep track of which components have finished
            mask_retr1_prcComponents = mask_retr1_prc.components
            for thisComponent in mask_retr1_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mask_retr1_prc" ---
            mask_retr1_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *mask_img1* updates
                
                # if mask_img1 is starting this frame...
                if mask_img1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mask_img1.frameNStart = frameN  # exact frame index
                    mask_img1.tStart = t  # local t and not account for scr refresh
                    mask_img1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mask_img1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mask_img1.started')
                    # update status
                    mask_img1.status = STARTED
                    mask_img1.setAutoDraw(True)
                
                # if mask_img1 is active this frame...
                if mask_img1.status == STARTED:
                    # update params
                    pass
                
                # if mask_img1 is stopping this frame...
                if mask_img1.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mask_img1.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        mask_img1.tStop = t  # not accounting for scr refresh
                        mask_img1.tStopRefresh = tThisFlipGlobal  # on global time
                        mask_img1.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'mask_img1.stopped')
                        # update status
                        mask_img1.status = FINISHED
                        mask_img1.setAutoDraw(False)
                
                # *info_example_4* updates
                
                # if info_example_4 is starting this frame...
                if info_example_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example_4.frameNStart = frameN  # exact frame index
                    info_example_4.tStart = t  # local t and not account for scr refresh
                    info_example_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_4.started')
                    # update status
                    info_example_4.status = STARTED
                    info_example_4.setAutoDraw(True)
                
                # if info_example_4 is active this frame...
                if info_example_4.status == STARTED:
                    # update params
                    pass
                
                # if info_example_4 is stopping this frame...
                if info_example_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_4.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_4.tStop = t  # not accounting for scr refresh
                        info_example_4.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_4.stopped')
                        # update status
                        info_example_4.status = FINISHED
                        info_example_4.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=mask_retr1_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    mask_retr1_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mask_retr1_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mask_retr1_prc" ---
            for thisComponent in mask_retr1_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for mask_retr1_prc
            mask_retr1_prc.tStop = globalClock.getTime(format='float')
            mask_retr1_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('mask_retr1_prc.stopped', mask_retr1_prc.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if mask_retr1_prc.maxDurationReached:
                routineTimer.addTime(-mask_retr1_prc.maxDuration)
            elif mask_retr1_prc.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "second_image_prc" ---
            # create an object to store info about Routine second_image_prc
            second_image_prc = data.Routine(
                name='second_image_prc',
                components=[image_2_prc, info_example_5],
            )
            second_image_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_2_prc.setImage(img_second)
            info_example_5.setImage(ImageExamplePath)
            # store start times for second_image_prc
            second_image_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            second_image_prc.tStart = globalClock.getTime(format='float')
            second_image_prc.status = STARTED
            thisExp.addData('second_image_prc.started', second_image_prc.tStart)
            second_image_prc.maxDuration = None
            # keep track of which components have finished
            second_image_prcComponents = second_image_prc.components
            for thisComponent in second_image_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "second_image_prc" ---
            second_image_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_2_prc* updates
                
                # if image_2_prc is starting this frame...
                if image_2_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2_prc.frameNStart = frameN  # exact frame index
                    image_2_prc.tStart = t  # local t and not account for scr refresh
                    image_2_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2_prc.started')
                    # update status
                    image_2_prc.status = STARTED
                    image_2_prc.setAutoDraw(True)
                
                # if image_2_prc is active this frame...
                if image_2_prc.status == STARTED:
                    # update params
                    pass
                
                # if image_2_prc is stopping this frame...
                if image_2_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2_prc.tStartRefresh + image_dur_retr_new + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2_prc.tStop = t  # not accounting for scr refresh
                        image_2_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2_prc.stopped')
                        # update status
                        image_2_prc.status = FINISHED
                        image_2_prc.setAutoDraw(False)
                
                # *info_example_5* updates
                
                # if info_example_5 is starting this frame...
                if info_example_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example_5.frameNStart = frameN  # exact frame index
                    info_example_5.tStart = t  # local t and not account for scr refresh
                    info_example_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_5.started')
                    # update status
                    info_example_5.status = STARTED
                    info_example_5.setAutoDraw(True)
                
                # if info_example_5 is active this frame...
                if info_example_5.status == STARTED:
                    # update params
                    pass
                
                # if info_example_5 is stopping this frame...
                if info_example_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_5.tStartRefresh + image_dur_retr_new + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_5.tStop = t  # not accounting for scr refresh
                        info_example_5.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_5.stopped')
                        # update status
                        info_example_5.status = FINISHED
                        info_example_5.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=second_image_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    second_image_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in second_image_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "second_image_prc" ---
            for thisComponent in second_image_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for second_image_prc
            second_image_prc.tStop = globalClock.getTime(format='float')
            second_image_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('second_image_prc.stopped', second_image_prc.tStop)
            # the Routine "second_image_prc" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "mask_retr2_prc" ---
            # create an object to store info about Routine mask_retr2_prc
            mask_retr2_prc = data.Routine(
                name='mask_retr2_prc',
                components=[mask_img2, info_example_6],
            )
            mask_retr2_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            info_example_6.setImage(ImageExamplePath)
            # store start times for mask_retr2_prc
            mask_retr2_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            mask_retr2_prc.tStart = globalClock.getTime(format='float')
            mask_retr2_prc.status = STARTED
            thisExp.addData('mask_retr2_prc.started', mask_retr2_prc.tStart)
            mask_retr2_prc.maxDuration = None
            # keep track of which components have finished
            mask_retr2_prcComponents = mask_retr2_prc.components
            for thisComponent in mask_retr2_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "mask_retr2_prc" ---
            mask_retr2_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.25:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *mask_img2* updates
                
                # if mask_img2 is starting this frame...
                if mask_img2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    mask_img2.frameNStart = frameN  # exact frame index
                    mask_img2.tStart = t  # local t and not account for scr refresh
                    mask_img2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(mask_img2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'mask_img2.started')
                    # update status
                    mask_img2.status = STARTED
                    mask_img2.setAutoDraw(True)
                
                # if mask_img2 is active this frame...
                if mask_img2.status == STARTED:
                    # update params
                    pass
                
                # if mask_img2 is stopping this frame...
                if mask_img2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > mask_img2.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        mask_img2.tStop = t  # not accounting for scr refresh
                        mask_img2.tStopRefresh = tThisFlipGlobal  # on global time
                        mask_img2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'mask_img2.stopped')
                        # update status
                        mask_img2.status = FINISHED
                        mask_img2.setAutoDraw(False)
                
                # *info_example_6* updates
                
                # if info_example_6 is starting this frame...
                if info_example_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example_6.frameNStart = frameN  # exact frame index
                    info_example_6.tStart = t  # local t and not account for scr refresh
                    info_example_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_6.started')
                    # update status
                    info_example_6.status = STARTED
                    info_example_6.setAutoDraw(True)
                
                # if info_example_6 is active this frame...
                if info_example_6.status == STARTED:
                    # update params
                    pass
                
                # if info_example_6 is stopping this frame...
                if info_example_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_6.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_6.tStop = t  # not accounting for scr refresh
                        info_example_6.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_6.stopped')
                        # update status
                        info_example_6.status = FINISHED
                        info_example_6.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=mask_retr2_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    mask_retr2_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in mask_retr2_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "mask_retr2_prc" ---
            for thisComponent in mask_retr2_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for mask_retr2_prc
            mask_retr2_prc.tStop = globalClock.getTime(format='float')
            mask_retr2_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('mask_retr2_prc.stopped', mask_retr2_prc.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if mask_retr2_prc.maxDurationReached:
                routineTimer.addTime(-mask_retr2_prc.maxDuration)
            elif mask_retr2_prc.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.250000)
            
            # --- Prepare to start Routine "reflection_period" ---
            # create an object to store info about Routine reflection_period
            reflection_period = data.Routine(
                name='reflection_period',
                components=[fix_cross_reflretr_2, text],
            )
            reflection_period.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for reflection_period
            reflection_period.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            reflection_period.tStart = globalClock.getTime(format='float')
            reflection_period.status = STARTED
            thisExp.addData('reflection_period.started', reflection_period.tStart)
            reflection_period.maxDuration = None
            # keep track of which components have finished
            reflection_periodComponents = reflection_period.components
            for thisComponent in reflection_period.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "reflection_period" ---
            reflection_period.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *fix_cross_reflretr_2* updates
                
                # if fix_cross_reflretr_2 is starting this frame...
                if fix_cross_reflretr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_cross_reflretr_2.frameNStart = frameN  # exact frame index
                    fix_cross_reflretr_2.tStart = t  # local t and not account for scr refresh
                    fix_cross_reflretr_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_cross_reflretr_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_reflretr_2.started')
                    # update status
                    fix_cross_reflretr_2.status = STARTED
                    fix_cross_reflretr_2.setAutoDraw(True)
                
                # if fix_cross_reflretr_2 is active this frame...
                if fix_cross_reflretr_2.status == STARTED:
                    # update params
                    pass
                
                # if fix_cross_reflretr_2 is stopping this frame...
                if fix_cross_reflretr_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_cross_reflretr_2.tStartRefresh + reflection_win_dur + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_cross_reflretr_2.tStop = t  # not accounting for scr refresh
                        fix_cross_reflretr_2.tStopRefresh = tThisFlipGlobal  # on global time
                        fix_cross_reflretr_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross_reflretr_2.stopped')
                        # update status
                        fix_cross_reflretr_2.status = FINISHED
                        fix_cross_reflretr_2.setAutoDraw(False)
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    pass
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + reflection_win_dur + 2-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=reflection_period,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    reflection_period.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in reflection_period.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "reflection_period" ---
            for thisComponent in reflection_period.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for reflection_period
            reflection_period.tStop = globalClock.getTime(format='float')
            reflection_period.tStopRefresh = tThisFlipGlobal
            thisExp.addData('reflection_period.stopped', reflection_period.tStop)
            # the Routine "reflection_period" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "retr_response_order_prc" ---
            # create an object to store info about Routine retr_response_order_prc
            retr_response_order_prc = data.Routine(
                name='retr_response_order_prc',
                components=[yes_txt_3, no_txt_3, polygon_9, resp_3, info_example_7],
            )
            retr_response_order_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from clear_clock
            _resp_3_allKeys = None
            resp_3.clearEvents()
            retrClock = core.Clock()
            retrClock.reset()
            
            polygon_9.setPos((0,0))
            polygon_9.setOpacity(0)
            yes_txt_3.setPos([leftside_retr if opt_left=="yes" else rightside_retr])
            no_txt_3.setPos([rightside_retr if opt_right=="no" else leftside_retr])
            # create starting attributes for resp_3
            resp_3.keys = []
            resp_3.rt = []
            _resp_3_allKeys = []
            # Run 'Begin Routine' code from set_option_text
            
            if language == "english": 
                yes_txt_3.text = ("yes")
                no_txt_3.text = ("no")
            if language == "german":
                yes_txt_3.text = ("ja")
                no_txt_3.text = ("nein")
            if language == "french": 
                yes_txt_3.text = ("oui")
                no_txt_3.text = ("non")
            # Run 'Begin Routine' code from end_routine_after_resp_2
            responded_retr = False
            delayClock = None
            delayDone = False
            info_example_7.setImage(ImageExamplePath)
            # store start times for retr_response_order_prc
            retr_response_order_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            retr_response_order_prc.tStart = globalClock.getTime(format='float')
            retr_response_order_prc.status = STARTED
            thisExp.addData('retr_response_order_prc.started', retr_response_order_prc.tStart)
            retr_response_order_prc.maxDuration = None
            # keep track of which components have finished
            retr_response_order_prcComponents = retr_response_order_prc.components
            for thisComponent in retr_response_order_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "retr_response_order_prc" ---
            retr_response_order_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *yes_txt_3* updates
                
                # if yes_txt_3 is starting this frame...
                if yes_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    yes_txt_3.frameNStart = frameN  # exact frame index
                    yes_txt_3.tStart = t  # local t and not account for scr refresh
                    yes_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(yes_txt_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'yes_txt_3.started')
                    # update status
                    yes_txt_3.status = STARTED
                    yes_txt_3.setAutoDraw(True)
                
                # if yes_txt_3 is active this frame...
                if yes_txt_3.status == STARTED:
                    # update params
                    pass
                
                # if yes_txt_3 is stopping this frame...
                if yes_txt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > yes_txt_3.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        yes_txt_3.tStop = t  # not accounting for scr refresh
                        yes_txt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        yes_txt_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yes_txt_3.stopped')
                        # update status
                        yes_txt_3.status = FINISHED
                        yes_txt_3.setAutoDraw(False)
                
                # *no_txt_3* updates
                
                # if no_txt_3 is starting this frame...
                if no_txt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    no_txt_3.frameNStart = frameN  # exact frame index
                    no_txt_3.tStart = t  # local t and not account for scr refresh
                    no_txt_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(no_txt_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'no_txt_3.started')
                    # update status
                    no_txt_3.status = STARTED
                    no_txt_3.setAutoDraw(True)
                
                # if no_txt_3 is active this frame...
                if no_txt_3.status == STARTED:
                    # update params
                    pass
                
                # if no_txt_3 is stopping this frame...
                if no_txt_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > no_txt_3.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        no_txt_3.tStop = t  # not accounting for scr refresh
                        no_txt_3.tStopRefresh = tThisFlipGlobal  # on global time
                        no_txt_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'no_txt_3.stopped')
                        # update status
                        no_txt_3.status = FINISHED
                        no_txt_3.setAutoDraw(False)
                
                # *polygon_9* updates
                
                # if polygon_9 is starting this frame...
                if polygon_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_9.frameNStart = frameN  # exact frame index
                    polygon_9.tStart = t  # local t and not account for scr refresh
                    polygon_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_9.started')
                    # update status
                    polygon_9.status = STARTED
                    polygon_9.setAutoDraw(True)
                
                # if polygon_9 is active this frame...
                if polygon_9.status == STARTED:
                    # update params
                    pass
                
                # if polygon_9 is stopping this frame...
                if polygon_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_9.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_9.tStop = t  # not accounting for scr refresh
                        polygon_9.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_9.stopped')
                        # update status
                        polygon_9.status = FINISHED
                        polygon_9.setAutoDraw(False)
                
                # *resp_3* updates
                
                # if resp_3 is starting this frame...
                if resp_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_3.frameNStart = frameN  # exact frame index
                    resp_3.tStart = t  # local t and not account for scr refresh
                    resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('resp_3.started', t)
                    # update status
                    resp_3.status = STARTED
                    # keyboard checking is just starting
                    resp_3.clock.reset()  # now t=0
                    resp_3.clearEvents(eventType='keyboard')
                
                # if resp_3 is stopping this frame...
                if resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > resp_3.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        resp_3.tStop = t  # not accounting for scr refresh
                        resp_3.tStopRefresh = tThisFlipGlobal  # on global time
                        resp_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('resp_3.stopped', t)
                        # update status
                        resp_3.status = FINISHED
                        resp_3.status = FINISHED
                if resp_3.status == STARTED:
                    theseKeys = resp_3.getKeys(keyList=[left_key, right_key], ignoreKeys=["escape"], waitRelease=True)
                    _resp_3_allKeys.extend(theseKeys)
                    if len(_resp_3_allKeys):
                        resp_3.keys = _resp_3_allKeys[-1].name  # just the last key pressed
                        resp_3.rt = _resp_3_allKeys[-1].rt
                        resp_3.duration = _resp_3_allKeys[-1].duration
                # Run 'Each Frame' code from end_routine_after_resp_2
                if retrClock.getTime() >= max_read_dur:
                    # Timeout
                    responded_retr = False
                    continueRoutine = False
                
                if not responded_retr:
                    key_list = resp_3.getKeys(keyList=[left_key, right_key], waitRelease=False)
                    if len(key_list) > 0:
                        responded_retr = True
                        thisResp = key_list[0]
                        if thisResp.name == left_key:
                            chosenPos = [-0.06, 0]
                        elif thisResp.name == right_key:
                            chosenPos = [0.06, 0]
                        resp_3.keys = thisResp.name
                        resp_3.rt = thisResp.rt
                        resp_3.duration = thisResp.duration
                        if thisResp.name == correct_key:
                            resp_3.corr = 1
                        else:
                            resp_3.corr = 0
                            practice_errors += 1
                        polygon_9.setPos(chosenPos)
                        polygon_9.setOpacity(1.0)
                        delayClock = core.Clock()
                
                if responded_retr and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                    delayDone = True
                    continueRoutine = False
                
                # *info_example_7* updates
                
                # if info_example_7 is starting this frame...
                if info_example_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example_7.frameNStart = frameN  # exact frame index
                    info_example_7.tStart = t  # local t and not account for scr refresh
                    info_example_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_7.started')
                    # update status
                    info_example_7.status = STARTED
                    info_example_7.setAutoDraw(True)
                
                # if info_example_7 is active this frame...
                if info_example_7.status == STARTED:
                    # update params
                    pass
                
                # if info_example_7 is stopping this frame...
                if info_example_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_7.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_7.tStop = t  # not accounting for scr refresh
                        info_example_7.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_7.stopped')
                        # update status
                        info_example_7.status = FINISHED
                        info_example_7.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=retr_response_order_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    retr_response_order_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in retr_response_order_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "retr_response_order_prc" ---
            for thisComponent in retr_response_order_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for retr_response_order_prc
            retr_response_order_prc.tStop = globalClock.getTime(format='float')
            retr_response_order_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('retr_response_order_prc.stopped', retr_response_order_prc.tStop)
            # check responses
            if resp_3.keys in ['', [], None]:  # No response was made
                resp_3.keys = None
            retry_loop.addData('resp_3.keys',resp_3.keys)
            if resp_3.keys != None:  # we had a response
                retry_loop.addData('resp_3.rt', resp_3.rt)
                retry_loop.addData('resp_3.duration', resp_3.duration)
            # the Routine "retr_response_order_prc" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "retr_response_distance_prc" ---
            # create an object to store info about Routine retr_response_distance_prc
            retr_response_distance_prc = data.Routine(
                name='retr_response_distance_prc',
                components=[resp_2, info_example, opt_2_prc, opt_3_prc, opt_4_prc, opt_5_prc],
            )
            retr_response_distance_prc.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from clear_clock_2
            _resp_2_allKeys = None
            resp_2.clearEvents()
            retrClock = core.Clock()
            retrClock.reset()
            # create starting attributes for resp_2
            resp_2.keys = []
            resp_2.rt = []
            _resp_2_allKeys = []
            # Run 'Begin Routine' code from controlslider_pos_js_2
            responded_retr_slider = False
            delayClock = None
            delayDone = False
            info_example.setImage(ImageExamplePath)
            opt_2_prc.setColor('white', colorSpace='rgb')
            opt_3_prc.setColor('white', colorSpace='rgb')
            opt_4_prc.setColor('white', colorSpace='rgb')
            opt_5_prc.setColor('white', colorSpace='rgb')
            # store start times for retr_response_distance_prc
            retr_response_distance_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            retr_response_distance_prc.tStart = globalClock.getTime(format='float')
            retr_response_distance_prc.status = STARTED
            thisExp.addData('retr_response_distance_prc.started', retr_response_distance_prc.tStart)
            retr_response_distance_prc.maxDuration = None
            # keep track of which components have finished
            retr_response_distance_prcComponents = retr_response_distance_prc.components
            for thisComponent in retr_response_distance_prc.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "retr_response_distance_prc" ---
            retr_response_distance_prc.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *resp_2* updates
                
                # if resp_2 is starting this frame...
                if resp_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    resp_2.frameNStart = frameN  # exact frame index
                    resp_2.tStart = t  # local t and not account for scr refresh
                    resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.addData('resp_2.started', t)
                    # update status
                    resp_2.status = STARTED
                    # keyboard checking is just starting
                    resp_2.clock.reset()  # now t=0
                    resp_2.clearEvents(eventType='keyboard')
                
                # if resp_2 is stopping this frame...
                if resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > resp_2.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        resp_2.tStop = t  # not accounting for scr refresh
                        resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.addData('resp_2.stopped', t)
                        # update status
                        resp_2.status = FINISHED
                        resp_2.status = FINISHED
                if resp_2.status == STARTED:
                    theseKeys = resp_2.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=True)
                    _resp_2_allKeys.extend(theseKeys)
                    if len(_resp_2_allKeys):
                        resp_2.keys = _resp_2_allKeys[-1].name  # just the last key pressed
                        resp_2.rt = _resp_2_allKeys[-1].rt
                        resp_2.duration = _resp_2_allKeys[-1].duration
                # Run 'Each Frame' code from controlslider_pos_js_2
                
                
                keysPressed = resp_2.getKeys(keyList=[left_key, right_key, center_key, down_key], waitRelease=False) # from event.getKeys
                if len(keysPressed) > 0:
                    
                    chosen_key = keysPressed[0]  # extract the string from the KeyPress object
                    if chosen_key.name == left_key:
                        chosenDis = 5
                        opt_5_prc.color = "blue"
                    elif chosen_key.name == right_key:
                        chosenDis = 3
                        opt_3_prc.color = "blue"
                
                    elif chosen_key.name == center_key:
                        chosenDis = 2
                        opt_2_prc.color = "blue"
                
                    elif chosen_key.name == down_key:
                        chosenDis = 4
                        opt_4_prc.color = "blue"
                
                        
                    resp_2.keys = chosenDis
                    resp_2.rt = chosen_key.rt
                    resp_2.duration = chosen_key.duration
                    if chosenDis == distance_correct:
                        resp_2.corr = 1
                    else:
                        resp_2.corr = 0
                        
                    responded_retr_slider = True
                    delayClock = core.Clock()
                    
                if responded_retr_slider and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                    delayDone = True
                    continueRoutine = False
                
                # *info_example* updates
                
                # if info_example is starting this frame...
                if info_example.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    info_example.frameNStart = frameN  # exact frame index
                    info_example.tStart = t  # local t and not account for scr refresh
                    info_example.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example.started')
                    # update status
                    info_example.status = STARTED
                    info_example.setAutoDraw(True)
                
                # if info_example is active this frame...
                if info_example.status == STARTED:
                    # update params
                    pass
                
                # if info_example is stopping this frame...
                if info_example.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example.tStop = t  # not accounting for scr refresh
                        info_example.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example.stopped')
                        # update status
                        info_example.status = FINISHED
                        info_example.setAutoDraw(False)
                
                # *opt_2_prc* updates
                
                # if opt_2_prc is starting this frame...
                if opt_2_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt_2_prc.frameNStart = frameN  # exact frame index
                    opt_2_prc.tStart = t  # local t and not account for scr refresh
                    opt_2_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt_2_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt_2_prc.started')
                    # update status
                    opt_2_prc.status = STARTED
                    opt_2_prc.setAutoDraw(True)
                
                # if opt_2_prc is active this frame...
                if opt_2_prc.status == STARTED:
                    # update params
                    pass
                
                # if opt_2_prc is stopping this frame...
                if opt_2_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > opt_2_prc.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        opt_2_prc.tStop = t  # not accounting for scr refresh
                        opt_2_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        opt_2_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_2_prc.stopped')
                        # update status
                        opt_2_prc.status = FINISHED
                        opt_2_prc.setAutoDraw(False)
                
                # *opt_3_prc* updates
                
                # if opt_3_prc is starting this frame...
                if opt_3_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt_3_prc.frameNStart = frameN  # exact frame index
                    opt_3_prc.tStart = t  # local t and not account for scr refresh
                    opt_3_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt_3_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt_3_prc.started')
                    # update status
                    opt_3_prc.status = STARTED
                    opt_3_prc.setAutoDraw(True)
                
                # if opt_3_prc is active this frame...
                if opt_3_prc.status == STARTED:
                    # update params
                    pass
                
                # if opt_3_prc is stopping this frame...
                if opt_3_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > opt_3_prc.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        opt_3_prc.tStop = t  # not accounting for scr refresh
                        opt_3_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        opt_3_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_3_prc.stopped')
                        # update status
                        opt_3_prc.status = FINISHED
                        opt_3_prc.setAutoDraw(False)
                
                # *opt_4_prc* updates
                
                # if opt_4_prc is starting this frame...
                if opt_4_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt_4_prc.frameNStart = frameN  # exact frame index
                    opt_4_prc.tStart = t  # local t and not account for scr refresh
                    opt_4_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt_4_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt_4_prc.started')
                    # update status
                    opt_4_prc.status = STARTED
                    opt_4_prc.setAutoDraw(True)
                
                # if opt_4_prc is active this frame...
                if opt_4_prc.status == STARTED:
                    # update params
                    pass
                
                # if opt_4_prc is stopping this frame...
                if opt_4_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > opt_4_prc.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        opt_4_prc.tStop = t  # not accounting for scr refresh
                        opt_4_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        opt_4_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_4_prc.stopped')
                        # update status
                        opt_4_prc.status = FINISHED
                        opt_4_prc.setAutoDraw(False)
                
                # *opt_5_prc* updates
                
                # if opt_5_prc is starting this frame...
                if opt_5_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt_5_prc.frameNStart = frameN  # exact frame index
                    opt_5_prc.tStart = t  # local t and not account for scr refresh
                    opt_5_prc.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt_5_prc, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt_5_prc.started')
                    # update status
                    opt_5_prc.status = STARTED
                    opt_5_prc.setAutoDraw(True)
                
                # if opt_5_prc is active this frame...
                if opt_5_prc.status == STARTED:
                    # update params
                    pass
                
                # if opt_5_prc is stopping this frame...
                if opt_5_prc.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > opt_5_prc.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        opt_5_prc.tStop = t  # not accounting for scr refresh
                        opt_5_prc.tStopRefresh = tThisFlipGlobal  # on global time
                        opt_5_prc.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_5_prc.stopped')
                        # update status
                        opt_5_prc.status = FINISHED
                        opt_5_prc.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=retr_response_distance_prc,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    retr_response_distance_prc.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in retr_response_distance_prc.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "retr_response_distance_prc" ---
            for thisComponent in retr_response_distance_prc.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for retr_response_distance_prc
            retr_response_distance_prc.tStop = globalClock.getTime(format='float')
            retr_response_distance_prc.tStopRefresh = tThisFlipGlobal
            thisExp.addData('retr_response_distance_prc.stopped', retr_response_distance_prc.tStop)
            # check responses
            if resp_2.keys in ['', [], None]:  # No response was made
                resp_2.keys = None
            retry_loop.addData('resp_2.keys',resp_2.keys)
            if resp_2.keys != None:  # we had a response
                retry_loop.addData('resp_2.rt', resp_2.rt)
                retry_loop.addData('resp_2.duration', resp_2.duration)
            # Run 'End Routine' code from controlslider_pos_js_2
            if not responded_retr_slider:
                practice_errors += 1
            
            # the Routine "retr_response_distance_prc" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "retr_response_feedback" ---
            # create an object to store info about Routine retr_response_feedback
            retr_response_feedback = data.Routine(
                name='retr_response_feedback',
                components=[textbox_feedback, info_example_2, continue_button_16, textbox_continue],
            )
            retr_response_feedback.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            textbox_feedback.reset()
            # Run 'Begin Routine' code from set_text_feedback
            if language == "english" and resp_2.corr==1:
                textbox_feedback.text = (f"Good job! You understood the retrieval task.")
                
            if language == "german" and resp_2.corr==1:
                textbox_feedback.text = (f"Gut gemacht! Sie haben Abruf verstanden.")
                
                    
            if resp_2.corr==0:
                if language == "english":
                    textbox_feedback.text = (
            "Your answer was incorrect.\n"
            "Please review the background information again and look at the full image sequence. "
            "Determine how many images appear between the two prompted images in that sequence. "
            "Only count the images in between them — do NOT include the two prompted images themselves."
            )
                if language=="german":
                    textbox_feedback.text = (
            "Ihre Antwort war falsch.\n"
            "Bitte schauen Sie sich die Hintergrundinformationen noch einmal an. Bestimmen Sie, "
            "wie weit die Bilder in der gezeigten Sequenz auseinanderliegen.")
            
            
            info_example_2.setImage(ImageExamplePath)
            # create starting attributes for continue_button_16
            continue_button_16.keys = []
            continue_button_16.rt = []
            _continue_button_16_allKeys = []
            # Run 'Begin Routine' code from control_retry_loop
            prc_fdbackClock = core.Clock()
            prc_fdbackClock.reset()
            textbox_continue.reset()
            # Run 'Begin Routine' code from set_text_continue
            if language == "english" and resp_2.corr==1:
                textbox_continue.text = (
                "Press RETURN to continue.")
                
            if language == "german" and resp_2.corr==1:
                textbox_continue.text = (
                "Drücken Sie eine beliebige Taste, um weiterzumachen.")
                
                    
            if resp_2.corr==0:
                if language == "english":
                    textbox_continue.text = (
                    "When you know the correct answer, press RETURN to answer the question again.")
                if language=="german":
                    textbox_continue.text = (
                    "Wenn Sie die richtige Antwort wissen, drücken Sie eine beliebige Taste, um die Frage noch einmal zu beantworten."
                    )
            
            
            # store start times for retr_response_feedback
            retr_response_feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            retr_response_feedback.tStart = globalClock.getTime(format='float')
            retr_response_feedback.status = STARTED
            thisExp.addData('retr_response_feedback.started', retr_response_feedback.tStart)
            retr_response_feedback.maxDuration = None
            # keep track of which components have finished
            retr_response_feedbackComponents = retr_response_feedback.components
            for thisComponent in retr_response_feedback.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "retr_response_feedback" ---
            retr_response_feedback.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisRetry_loop, 'status') and thisRetry_loop.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *textbox_feedback* updates
                
                # if textbox_feedback is starting this frame...
                if textbox_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_feedback.frameNStart = frameN  # exact frame index
                    textbox_feedback.tStart = t  # local t and not account for scr refresh
                    textbox_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_feedback, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_feedback.started')
                    # update status
                    textbox_feedback.status = STARTED
                    textbox_feedback.setAutoDraw(True)
                
                # if textbox_feedback is active this frame...
                if textbox_feedback.status == STARTED:
                    # update params
                    pass
                
                # if textbox_feedback is stopping this frame...
                if textbox_feedback.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textbox_feedback.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        textbox_feedback.tStop = t  # not accounting for scr refresh
                        textbox_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                        textbox_feedback.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_feedback.stopped')
                        # update status
                        textbox_feedback.status = FINISHED
                        textbox_feedback.setAutoDraw(False)
                
                # *info_example_2* updates
                
                # if info_example_2 is starting this frame...
                if info_example_2.status == NOT_STARTED and resp_2.corr==0:
                    # keep track of start time/frame for later
                    info_example_2.frameNStart = frameN  # exact frame index
                    info_example_2.tStart = t  # local t and not account for scr refresh
                    info_example_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(info_example_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'info_example_2.started')
                    # update status
                    info_example_2.status = STARTED
                    info_example_2.setAutoDraw(True)
                
                # if info_example_2 is active this frame...
                if info_example_2.status == STARTED:
                    # update params
                    pass
                
                # if info_example_2 is stopping this frame...
                if info_example_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > info_example_2.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        info_example_2.tStop = t  # not accounting for scr refresh
                        info_example_2.tStopRefresh = tThisFlipGlobal  # on global time
                        info_example_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'info_example_2.stopped')
                        # update status
                        info_example_2.status = FINISHED
                        info_example_2.setAutoDraw(False)
                
                # *continue_button_16* updates
                waitOnFlip = False
                
                # if continue_button_16 is starting this frame...
                if continue_button_16.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                    # keep track of start time/frame for later
                    continue_button_16.frameNStart = frameN  # exact frame index
                    continue_button_16.tStart = t  # local t and not account for scr refresh
                    continue_button_16.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(continue_button_16, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_button_16.started')
                    # update status
                    continue_button_16.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(continue_button_16.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(continue_button_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if continue_button_16 is stopping this frame...
                if continue_button_16.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > continue_button_16.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        continue_button_16.tStop = t  # not accounting for scr refresh
                        continue_button_16.tStopRefresh = tThisFlipGlobal  # on global time
                        continue_button_16.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_button_16.stopped')
                        # update status
                        continue_button_16.status = FINISHED
                        continue_button_16.status = FINISHED
                if continue_button_16.status == STARTED and not waitOnFlip:
                    theseKeys = continue_button_16.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
                    _continue_button_16_allKeys.extend(theseKeys)
                    if len(_continue_button_16_allKeys):
                        continue_button_16.keys = _continue_button_16_allKeys[0].name  # just the first key pressed
                        continue_button_16.rt = _continue_button_16_allKeys[0].rt
                        continue_button_16.duration = _continue_button_16_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                # Run 'Each Frame' code from control_retry_loop
                if prc_fdbackClock.getTime() >= max_read_dur:
                    # Timeout
                    continueRoutine = False
                
                # *textbox_continue* updates
                
                # if textbox_continue is starting this frame...
                if textbox_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    textbox_continue.frameNStart = frameN  # exact frame index
                    textbox_continue.tStart = t  # local t and not account for scr refresh
                    textbox_continue.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(textbox_continue, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textbox_continue.started')
                    # update status
                    textbox_continue.status = STARTED
                    textbox_continue.setAutoDraw(True)
                
                # if textbox_continue is active this frame...
                if textbox_continue.status == STARTED:
                    # update params
                    pass
                
                # if textbox_continue is stopping this frame...
                if textbox_continue.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > textbox_continue.tStartRefresh + max_read_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        textbox_continue.tStop = t  # not accounting for scr refresh
                        textbox_continue.tStopRefresh = tThisFlipGlobal  # on global time
                        textbox_continue.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'textbox_continue.stopped')
                        # update status
                        textbox_continue.status = FINISHED
                        textbox_continue.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=retr_response_feedback,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    retr_response_feedback.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in retr_response_feedback.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "retr_response_feedback" ---
            for thisComponent in retr_response_feedback.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for retr_response_feedback
            retr_response_feedback.tStop = globalClock.getTime(format='float')
            retr_response_feedback.tStopRefresh = tThisFlipGlobal
            thisExp.addData('retr_response_feedback.stopped', retr_response_feedback.tStop)
            # check responses
            if continue_button_16.keys in ['', [], None]:  # No response was made
                continue_button_16.keys = None
            retry_loop.addData('continue_button_16.keys',continue_button_16.keys)
            if continue_button_16.keys != None:  # we had a response
                retry_loop.addData('continue_button_16.rt', continue_button_16.rt)
                retry_loop.addData('continue_button_16.duration', continue_button_16.duration)
            # Run 'End Routine' code from control_retry_loop
            print(resp_2.corr)
            if resp_2.corr == 1:
                retry_loop.finished = True
            else:
                retry_loop.finished = False
            # the Routine "retr_response_feedback" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisRetry_loop as finished
            if hasattr(thisRetry_loop, 'status'):
                thisRetry_loop.status = FINISHED
            # if awaiting a pause, pause now
            if retry_loop.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                retry_loop.status = STARTED
        # completed 999.0 repeats of 'retry_loop'
        retry_loop.status = FINISHED
        
        # mark thisRetrieval_prc_loop as finished
        if hasattr(thisRetrieval_prc_loop, 'status'):
            thisRetrieval_prc_loop.status = FINISHED
        # if awaiting a pause, pause now
        if retrieval_prc_loop.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            retrieval_prc_loop.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'retrieval_prc_loop'
    retrieval_prc_loop.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "instructions_07" ---
    # create an object to store info about Routine instructions_07
    instructions_07 = data.Routine(
        name='instructions_07',
        components=[instructions_part7, continue_button_13],
    )
    instructions_07.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part7_text_2
    if language == "english": 
        instructions_part7.text = (
    "You finished all the practice trials.\nThe main task starts now.\n\n"
    "Please minimize movement during the main task phases.\n\n"
    "Reminder: At the beginning, you will not yet know the correct sequence and will learn through trial and error over time.\n\n"
    "Press any key to continue."
    )
    
       
    if language == "german": 
        instructions_part7.text = (
    "Sie haben alle Übungsdurchgänge beendet.\nNun beginnt die Hauptaufgabe.\n\n"
    "Bitte stellen Sie sicher, dass Sie Bewegungen des Körpers und der\n"
    "Augen in den Aufgabenphasen so weit wie möglich reduzieren.\n\n"
    "Zur Erinnerung: Zu Beginn werden Sie die korrekte Sequenz noch nicht kennen\n"
    "und mit der Zeit über Versuch und Irrtum lernen.\n\n"
    "Drücken Sie eine beliebige Taste, um weiterzumachen."
    )
    
    
    # create starting attributes for continue_button_13
    continue_button_13.keys = []
    continue_button_13.rt = []
    _continue_button_13_allKeys = []
    # store start times for instructions_07
    instructions_07.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_07.tStart = globalClock.getTime(format='float')
    instructions_07.status = STARTED
    thisExp.addData('instructions_07.started', instructions_07.tStart)
    instructions_07.maxDuration = None
    # keep track of which components have finished
    instructions_07Components = instructions_07.components
    for thisComponent in instructions_07.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_07" ---
    instructions_07.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_part7* updates
        
        # if instructions_part7 is starting this frame...
        if instructions_part7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_part7.frameNStart = frameN  # exact frame index
            instructions_part7.tStart = t  # local t and not account for scr refresh
            instructions_part7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_part7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_part7.started')
            # update status
            instructions_part7.status = STARTED
            instructions_part7.setAutoDraw(True)
        
        # if instructions_part7 is active this frame...
        if instructions_part7.status == STARTED:
            # update params
            pass
        
        # if instructions_part7 is stopping this frame...
        if instructions_part7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_part7.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instructions_part7.tStop = t  # not accounting for scr refresh
                instructions_part7.tStopRefresh = tThisFlipGlobal  # on global time
                instructions_part7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructions_part7.stopped')
                # update status
                instructions_part7.status = FINISHED
                instructions_part7.setAutoDraw(False)
        
        # *continue_button_13* updates
        waitOnFlip = False
        
        # if continue_button_13 is starting this frame...
        if continue_button_13.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            continue_button_13.frameNStart = frameN  # exact frame index
            continue_button_13.tStart = t  # local t and not account for scr refresh
            continue_button_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_13.started')
            # update status
            continue_button_13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_13 is stopping this frame...
        if continue_button_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_13.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_13.tStop = t  # not accounting for scr refresh
                continue_button_13.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_13.stopped')
                # update status
                continue_button_13.status = FINISHED
                continue_button_13.status = FINISHED
        if continue_button_13.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_13.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_13_allKeys.extend(theseKeys)
            if len(_continue_button_13_allKeys):
                continue_button_13.keys = _continue_button_13_allKeys[0].name  # just the first key pressed
                continue_button_13.rt = _continue_button_13_allKeys[0].rt
                continue_button_13.duration = _continue_button_13_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_07,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_07.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_07.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_07" ---
    for thisComponent in instructions_07.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_07
    instructions_07.tStop = globalClock.getTime(format='float')
    instructions_07.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_07.stopped', instructions_07.tStop)
    # check responses
    if continue_button_13.keys in ['', [], None]:  # No response was made
        continue_button_13.keys = None
    thisExp.addData('continue_button_13.keys',continue_button_13.keys)
    if continue_button_13.keys != None:  # we had a response
        thisExp.addData('continue_button_13.rt', continue_button_13.rt)
        thisExp.addData('continue_button_13.duration', continue_button_13.duration)
    thisExp.nextEntry()
    # the Routine "instructions_07" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_08" ---
    # create an object to store info about Routine instructions_08
    instructions_08 = data.Routine(
        name='instructions_08',
        components=[instructions_part8, continue_button_17],
    )
    instructions_08.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part8_text_2
    if language == "english": 
        instructions_part8.text = (
    "After each learning run, there will be short waiting periods, in which you will see a fixation cross.\n"
    "These periods are not a break. Please just wait for a short moment, but don't take a break.\n\n"
    "Press any key to start the main task."
    )
    
       
    if language == "german": 
        instructions_part8.text = (
    "Nach jedem Lerndurchlauf gibt es kurze Wartezeiten, in denen ein\n"
    "Fixationskreuz präsentiert wird. Diese Wartezeiten sind keine Pause.\n"
    "Bitte warten Sie nur einen kurzen Moment, machen Sie aber keine Pause.\n\n"
    "Drücken Sie eine beliebige Taste, um die Hauptaufgabe zu beginnen."
    )
    
    
    # create starting attributes for continue_button_17
    continue_button_17.keys = []
    continue_button_17.rt = []
    _continue_button_17_allKeys = []
    # store start times for instructions_08
    instructions_08.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_08.tStart = globalClock.getTime(format='float')
    instructions_08.status = STARTED
    thisExp.addData('instructions_08.started', instructions_08.tStart)
    instructions_08.maxDuration = None
    # keep track of which components have finished
    instructions_08Components = instructions_08.components
    for thisComponent in instructions_08.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_08" ---
    instructions_08.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_part8* updates
        
        # if instructions_part8 is starting this frame...
        if instructions_part8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_part8.frameNStart = frameN  # exact frame index
            instructions_part8.tStart = t  # local t and not account for scr refresh
            instructions_part8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_part8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_part8.started')
            # update status
            instructions_part8.status = STARTED
            instructions_part8.setAutoDraw(True)
        
        # if instructions_part8 is active this frame...
        if instructions_part8.status == STARTED:
            # update params
            pass
        
        # if instructions_part8 is stopping this frame...
        if instructions_part8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_part8.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instructions_part8.tStop = t  # not accounting for scr refresh
                instructions_part8.tStopRefresh = tThisFlipGlobal  # on global time
                instructions_part8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructions_part8.stopped')
                # update status
                instructions_part8.status = FINISHED
                instructions_part8.setAutoDraw(False)
        
        # *continue_button_17* updates
        waitOnFlip = False
        
        # if continue_button_17 is starting this frame...
        if continue_button_17.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            continue_button_17.frameNStart = frameN  # exact frame index
            continue_button_17.tStart = t  # local t and not account for scr refresh
            continue_button_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_17.started')
            # update status
            continue_button_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_17 is stopping this frame...
        if continue_button_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_17.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_17.tStop = t  # not accounting for scr refresh
                continue_button_17.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_17.stopped')
                # update status
                continue_button_17.status = FINISHED
                continue_button_17.status = FINISHED
        if continue_button_17.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_17.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_17_allKeys.extend(theseKeys)
            if len(_continue_button_17_allKeys):
                continue_button_17.keys = _continue_button_17_allKeys[0].name  # just the first key pressed
                continue_button_17.rt = _continue_button_17_allKeys[0].rt
                continue_button_17.duration = _continue_button_17_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_08,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_08.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_08.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_08" ---
    for thisComponent in instructions_08.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_08
    instructions_08.tStop = globalClock.getTime(format='float')
    instructions_08.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_08.stopped', instructions_08.tStop)
    # check responses
    if continue_button_17.keys in ['', [], None]:  # No response was made
        continue_button_17.keys = None
    thisExp.addData('continue_button_17.keys',continue_button_17.keys)
    if continue_button_17.keys != None:  # we had a response
        thisExp.addData('continue_button_17.rt', continue_button_17.rt)
        thisExp.addData('continue_button_17.duration', continue_button_17.duration)
    thisExp.nextEntry()
    # the Routine "instructions_08" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    Block = data.TrialHandler2(
        name='Block',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequences/block_conditions.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(Block)  # add the loop to the experiment
    thisBlock = Block.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            globals()[paramName] = thisBlock[paramName]
    
    for thisBlock in Block:
        Block.status = STARTED
        if hasattr(thisBlock, 'status'):
            thisBlock.status = STARTED
        currentLoop = Block
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
        if thisBlock != None:
            for paramName in thisBlock:
                globals()[paramName] = thisBlock[paramName]
        
        # --- Prepare to start Routine "reset_rows_to_select" ---
        # create an object to store info about Routine reset_rows_to_select
        reset_rows_to_select = data.Routine(
            name='reset_rows_to_select',
            components=[],
        )
        reset_rows_to_select.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from define_number_trials
        if Block.thisN == 0: 
            N_LEARN = trials_per_run * n_routes_block # number of learning trials to use
            N_RETR = n_routes_block * 20 * 2 # number of retrieval trials to use
        elif Block.thisN > 0:
            N_LEARN = trials_per_run * (n_routes_block) * 2# number of learning trials to use
            N_RETR = 2* (n_routes_block) * 20 * 2 # number of retrieval trials to use
        
        learn_pool = list(range(N_LEARN))
        retr_pool  = list(range(N_RETR))
        learn_ptr = 0
        retr_ptr = 0
        # Run 'Begin Routine' code from set_conditionFiles_routes
        # Begin Routine (inside outer loop, before inner loop starts)
        cond_file_learning = condFileLearning.format(participant_ID=expInfo['participant_ID'])
        
        # Begin Routine (inside outer loop, before inner loop starts)
        cond_file_retrieval = condFileRetrieval.format(participant_ID=expInfo['participant_ID'])
        # store start times for reset_rows_to_select
        reset_rows_to_select.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        reset_rows_to_select.tStart = globalClock.getTime(format='float')
        reset_rows_to_select.status = STARTED
        thisExp.addData('reset_rows_to_select.started', reset_rows_to_select.tStart)
        reset_rows_to_select.maxDuration = None
        # keep track of which components have finished
        reset_rows_to_selectComponents = reset_rows_to_select.components
        for thisComponent in reset_rows_to_select.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "reset_rows_to_select" ---
        reset_rows_to_select.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisBlock, 'status') and thisBlock.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer, globalClock], 
                    currentRoutine=reset_rows_to_select,
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                reset_rows_to_select.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in reset_rows_to_select.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "reset_rows_to_select" ---
        for thisComponent in reset_rows_to_select.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for reset_rows_to_select
        reset_rows_to_select.tStop = globalClock.getTime(format='float')
        reset_rows_to_select.tStopRefresh = tThisFlipGlobal
        thisExp.addData('reset_rows_to_select.stopped', reset_rows_to_select.tStop)
        # the Routine "reset_rows_to_select" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        miniblocks = data.TrialHandler2(
            name='miniblocks',
            nReps=n_routes_block, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(miniblocks)  # add the loop to the experiment
        thisMiniblock = miniblocks.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisMiniblock.rgb)
        if thisMiniblock != None:
            for paramName in thisMiniblock:
                globals()[paramName] = thisMiniblock[paramName]
        
        for thisMiniblock in miniblocks:
            miniblocks.status = STARTED
            if hasattr(thisMiniblock, 'status'):
                thisMiniblock.status = STARTED
            currentLoop = miniblocks
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # abbreviate parameter names if possible (e.g. rgb = thisMiniblock.rgb)
            if thisMiniblock != None:
                for paramName in thisMiniblock:
                    globals()[paramName] = thisMiniblock[paramName]
            
            # --- Prepare to start Routine "set_learning_rows" ---
            # create an object to store info about Routine set_learning_rows
            set_learning_rows = data.Routine(
                name='set_learning_rows',
                components=[],
            )
            set_learning_rows.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from take_learn_routes_from_list
            selected_rows, learn_ptr = take_block(learn_pool, learn_ptr, trials_per_run)
            print(selected_rows)
            # store start times for set_learning_rows
            set_learning_rows.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            set_learning_rows.tStart = globalClock.getTime(format='float')
            set_learning_rows.status = STARTED
            thisExp.addData('set_learning_rows.started', set_learning_rows.tStart)
            set_learning_rows.maxDuration = None
            # keep track of which components have finished
            set_learning_rowsComponents = set_learning_rows.components
            for thisComponent in set_learning_rows.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "set_learning_rows" ---
            set_learning_rows.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=set_learning_rows,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    set_learning_rows.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in set_learning_rows.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "set_learning_rows" ---
            for thisComponent in set_learning_rows.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for set_learning_rows
            set_learning_rows.tStop = globalClock.getTime(format='float')
            set_learning_rows.tStopRefresh = tThisFlipGlobal
            thisExp.addData('set_learning_rows.stopped', set_learning_rows.tStop)
            # the Routine "set_learning_rows" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            learning_trials = data.TrialHandler2(
                name='learning_trials',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                cond_file_learning, 
                selection=selected_rows
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(learning_trials)  # add the loop to the experiment
            thisLearning_trial = learning_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
            if thisLearning_trial != None:
                for paramName in thisLearning_trial:
                    globals()[paramName] = thisLearning_trial[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisLearning_trial in learning_trials:
                learning_trials.status = STARTED
                if hasattr(thisLearning_trial, 'status'):
                    thisLearning_trial.status = STARTED
                currentLoop = learning_trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisLearning_trial.rgb)
                if thisLearning_trial != None:
                    for paramName in thisLearning_trial:
                        globals()[paramName] = thisLearning_trial[paramName]
                
                # --- Prepare to start Routine "choice_display" ---
                # create an object to store info about Routine choice_display
                choice_display = data.Routine(
                    name='choice_display',
                    components=[polygon_4, prompt, dist_01, dist_02, correct, chooseNowText, key_resp],
                )
                choice_display.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from Init_routeClock_2
                
                routClock = core.Clock()
                routClock.reset()
                
                key_resp_allKeys = None
                key_resp.clearEvents()
                
                polygon_4.setPos((0,0))
                polygon_4.setOpacity(0)
                # Run 'Begin Routine' code from bids_choice_disp
                # which item sits where on THIS trial
                pos2item = {}
                pos2item[correct_pos]   = 'target'
                pos2item[dist01_pos] = 'distractor_01'
                pos2item[dist02_pos] = 'distractor_02'
                
                # key -> position mapping
                key2pos = {
                    left_key:   'left',
                    right_key:  'right',
                    center_key: 'center'
                }
                
                prompt.setPos(prompt_pos)
                prompt.setImage(promptFile)
                dist_01.setPos([resolve_pos(dist01_pos)])
                dist_01.setImage(dist_01File)
                dist_02.setPos([resolve_pos(dist02_pos)])
                dist_02.setImage(dist_02File)
                correct.setPos([resolve_pos(correct_pos)])
                correct.setImage(correctFile)
                # Run 'Begin Routine' code from get_response_parameters
                responded = False
                delayClock = None
                delayDone = False
                chosenPos = None
                chooseNowText.setOpacity(0.0)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # Run 'Begin Routine' code from set_trigger_response
                response_trigger = trigger_dict["image_selected"]
                resp_trig_giv = False
                
                
                
                # store start times for choice_display
                choice_display.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                choice_display.tStart = globalClock.getTime(format='float')
                choice_display.status = STARTED
                thisExp.addData('choice_display.started', choice_display.tStart)
                choice_display.maxDuration = None
                # keep track of which components have finished
                choice_displayComponents = choice_display.components
                for thisComponent in choice_display.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "choice_display" ---
                choice_display.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisLearning_trial, 'status') and thisLearning_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_image
                    
                    if frameN == 0: 
                        send_trigger(correctTrigNumber)
                        core.wait(0.01)
                    
                        
                    
                    
                    # Run 'Each Frame' code from bids_choice_disp
                    ## schedule bids trigger setting
                    bids.schedule_onset(prompt, type_of_stimulus="image", 
                    component_label="current_image", 
                    trial_type = "learn",
                    concept_label = promptFile.partition("/")[-1],
                    concept_exemplar = promptFile.partition("/")[-1], 
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq)
                    
                    bids.schedule_onset(correct, type_of_stimulus="image", 
                    component_label="corr_next_image", 
                    trial_type = "learn",
                    concept_label = correctFile.partition("/")[-1],
                    concept_exemplar = correctFile.partition("/")[2], 
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq)
                    
                    bids.schedule_onset(dist_01, type_of_stimulus="image", 
                    component_label="distractor 01 (close)", 
                    concept_label = dist_01File.partition("/")[-1],
                    trial_type = "learn",
                    concept_exemplar = dist_01File.partition("/")[-1], 
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq)
                    
                    bids.schedule_onset(dist_02, type_of_stimulus="image", 
                    component_label="distractor 02 (far)", 
                    concept_label = dist_02File.partition("/")[-1],
                    trial_type = "learn",
                    concept_exemplar = dist_02File.partition("/")[-1], 
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq)
                    
                    
                    # *polygon_4* updates
                    
                    # if polygon_4 is starting this frame...
                    if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        polygon_4.frameNStart = frameN  # exact frame index
                        polygon_4.tStart = t  # local t and not account for scr refresh
                        polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_4.started')
                        # update status
                        polygon_4.status = STARTED
                        polygon_4.setAutoDraw(True)
                    
                    # if polygon_4 is active this frame...
                    if polygon_4.status == STARTED:
                        # update params
                        polygon_4.setFillColor([0.0000, 0.0000, 0.0000], log=False)
                        polygon_4.setLineColor([0.0039, 0.0039, 0.0039], log=False)
                    
                    # *prompt* updates
                    
                    # if prompt is starting this frame...
                    if prompt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        prompt.frameNStart = frameN  # exact frame index
                        prompt.tStart = t  # local t and not account for scr refresh
                        prompt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(prompt, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'prompt.started')
                        # update status
                        prompt.status = STARTED
                        prompt.setAutoDraw(True)
                    
                    # if prompt is active this frame...
                    if prompt.status == STARTED:
                        # update params
                        pass
                    
                    # *dist_01* updates
                    
                    # if dist_01 is starting this frame...
                    if dist_01.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        dist_01.frameNStart = frameN  # exact frame index
                        dist_01.tStart = t  # local t and not account for scr refresh
                        dist_01.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(dist_01, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist_01.started')
                        # update status
                        dist_01.status = STARTED
                        dist_01.setAutoDraw(True)
                    
                    # if dist_01 is active this frame...
                    if dist_01.status == STARTED:
                        # update params
                        pass
                    
                    # *dist_02* updates
                    
                    # if dist_02 is starting this frame...
                    if dist_02.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        dist_02.frameNStart = frameN  # exact frame index
                        dist_02.tStart = t  # local t and not account for scr refresh
                        dist_02.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(dist_02, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist_02.started')
                        # update status
                        dist_02.status = STARTED
                        dist_02.setAutoDraw(True)
                    
                    # if dist_02 is active this frame...
                    if dist_02.status == STARTED:
                        # update params
                        pass
                    
                    # *correct* updates
                    
                    # if correct is starting this frame...
                    if correct.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        correct.frameNStart = frameN  # exact frame index
                        correct.tStart = t  # local t and not account for scr refresh
                        correct.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(correct, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'correct.started')
                        # update status
                        correct.status = STARTED
                        correct.setAutoDraw(True)
                    
                    # if correct is active this frame...
                    if correct.status == STARTED:
                        # update params
                        pass
                    # Run 'Each Frame' code from get_response_parameters
                    if routClock.getTime() >= max_response_time:
                        # Timeout
                        responded = False
                        continueRoutine = False
                    
                    if not responded:
                        key_list = key_resp.getKeys(keyList=[left_key, right_key, center_key], waitRelease=False)
                    
                        if len(key_list) > 0:
                            responded = True
                            thisResp = key_list[0]
                            key_resp.keys = thisResp.name
                            key_resp.rt = thisResp.rt
                            key_resp.duration = thisResp.duration
                    
                    
                            if thisResp.name == left_key:
                                chosenPos = left_pos
                                KeyMeaning = "left"
                            elif thisResp.name == right_key:
                                chosenPos = right_pos
                                KeyMeaning = "right"
                            elif thisResp.name == center_key:
                                chosenPos = center_pos
                                KeyMeaning = "center"
                    
                            print(chosenPos) 
                            print(KeyMeaning)
                            key_resp.corr = 1 if (KeyMeaning == correct_pos) else 0
                            print(key_resp.corr)
                            polygon_4.setPos(chosenPos)
                            polygon_4.setOpacity(1.0)
                    
                            # change color of polygon for correct responses
                            if key_resp.corr == 1:
                                polygonCol = [0, 1, 0]
                                polygon_4.setFillColor(polygonCol)
                                polygon_4.setLineColor(polygonCol)
                            elif key_resp.corr == 0:
                                polygonCol = [1, -1, -1]
                                polygon_4.setFillColor(polygonCol)
                                polygon_4.setLineColor(polygonCol)
                            else:
                                polygonCol = [0, 0, 0]
                                polygon_4.setFillColor(polygonCol)
                                polygon_4.setLineColor(polygonCol)
                    
                            delayClock = core.Clock()
                    
                    if responded and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                        delayDone = True
                        continueRoutine = False
                    
                    # *chooseNowText* updates
                    
                    # if chooseNowText is starting this frame...
                    if chooseNowText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        chooseNowText.frameNStart = frameN  # exact frame index
                        chooseNowText.tStart = t  # local t and not account for scr refresh
                        chooseNowText.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(chooseNowText, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'chooseNowText.started')
                        # update status
                        chooseNowText.status = STARTED
                        chooseNowText.setAutoDraw(True)
                    
                    # if chooseNowText is active this frame...
                    if chooseNowText.status == STARTED:
                        # update params
                        pass
                    
                    # *key_resp* updates
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and t >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.addData('key_resp.started', t)
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        key_resp.clock.reset()  # now t=0
                        key_resp.clearEvents(eventType='keyboard')
                    
                    # if key_resp is stopping this frame...
                    if key_resp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > key_resp.tStartRefresh + max_response_time-frameTolerance:
                            # keep track of stop time/frame for later
                            key_resp.tStop = t  # not accounting for scr refresh
                            key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                            key_resp.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.addData('key_resp.stopped', t)
                            # update status
                            key_resp.status = FINISHED
                            key_resp.status = FINISHED
                    if key_resp.status == STARTED:
                        theseKeys = key_resp.getKeys(keyList=[left_key, right_key, center_key], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                            key_resp.rt = _key_resp_allKeys[0].rt
                            key_resp.duration = _key_resp_allKeys[0].duration
                    # Run 'Each Frame' code from set_trigger_response
                    if key_resp.keys and not resp_trig_giv:
                        send_trigger(response_trigger)
                        trigOn = True
                        resp_trig_giv=True
                        core.wait(0.01)
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=choice_display,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        choice_display.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in choice_display.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "choice_display" ---
                for thisComponent in choice_display.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for choice_display
                choice_display.tStop = globalClock.getTime(format='float')
                choice_display.tStopRefresh = tThisFlipGlobal
                thisExp.addData('choice_display.stopped', choice_display.tStop)
                # Run 'End Routine' code from bids_choice_disp
                
                bids.mark_offset(prompt)
                bids.mark_offset(correct)
                bids.mark_offset(dist_01)
                bids.mark_offset(dist_02)
                
                # response neeeds to be saved at end of trial
                pressed = key_resp.keys
                if isinstance(pressed, list):
                    pressed = pressed[-1] if pressed else "m"
                
                chosen_pos  = key2pos.get(pressed, None)
                chosen_item = pos2item.get(chosen_pos, None)
                
                is_correct = (chosen_item == 'target') if chosen_item is not None else None
                
                bids.add_instant(
                    "choice",
                    trial_type = "learn",
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq,
                    response=(key_resp.keys if key_resp.keys else "m"),
                    response_time=(key_resp.rt if hasattr(key_resp, "rt") else None),
                    correct=is_correct,
                    expected_response = correct_ans, 
                    response_meaning = chosen_item
                )
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                learning_trials.addData('key_resp.keys',key_resp.keys)
                if key_resp.keys != None:  # we had a response
                    learning_trials.addData('key_resp.rt', key_resp.rt)
                    learning_trials.addData('key_resp.duration', key_resp.duration)
                # the Routine "choice_display" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "feedback" ---
                # create an object to store info about Routine feedback
                feedback = data.Routine(
                    name='feedback',
                    components=[polygon_8, prompt_2, dist_01_2, dist_02_2, correct_2],
                )
                feedback.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from control__polygon_2
                polygon_8.setOpacity(0.0)
                if chosenPos:
                    polygon_8.setPos(chosenPos)
                    polygon_8.setOpacity(1.0)
                    polygon_8.setFillColor(polygonCol)
                    polygon_8.setLineColor(polygonCol)
                # Run 'Begin Routine' code from animation_control_2
                # Initialize animation control
                endY = prompt_pos[1]   # end y-coord of moving image
                endX = prompt_pos[0]   # end x-coord of moving image
                maxAnimationDur = round(animation_time * expInfo['frameRate'])
                animationTimer = 0      # initialize variable
                animationDone = False   # initialize variable
                moveCorrect = False     # initialize variable
                # Run 'Begin Routine' code from bids_feedback_disp
                
                
                prompt_2.setPos(prompt_pos)
                prompt_2.setImage(promptFile)
                dist_01_2.setPos([resolve_pos(dist01_pos)])
                dist_01_2.setImage(dist_01File)
                dist_02_2.setPos([resolve_pos(dist02_pos)])
                dist_02_2.setImage(dist_02File)
                correct_2.setPos([resolve_pos(correct_pos)])
                correct_2.setImage(correctFile)
                # Run 'Begin Routine' code from trigger_feedback_disp
                feedback_trigger_sent = False
                # store start times for feedback
                feedback.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                feedback.tStart = globalClock.getTime(format='float')
                feedback.status = STARTED
                thisExp.addData('feedback.started', feedback.tStart)
                feedback.maxDuration = None
                # keep track of which components have finished
                feedbackComponents = feedback.components
                for thisComponent in feedback.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "feedback" ---
                feedback.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisLearning_trial, 'status') and thisLearning_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from animation_control_2
                    # Start animation
                    if not moveCorrect and not animationDone:
                        moveCorrect = True
                    
                    # Run animation
                    if moveCorrect and not animationDone:
                        animationTimer += 1
                        # Current position
                        current_x, current_y = correct_2.pos
                        # Compute direction toward target
                        dx = endX - current_x
                        dy = endY - current_y
                        # Move a small fraction toward target
                        move_fraction = feedback_steps  # fraction of remaining distance each frame
                        new_x = current_x + dx * move_fraction
                        new_y = current_y + dy * move_fraction
                        # Update position
                        correct_2.setPos([new_x, new_y])
                        if key_resp.corr:
                            polygon_8.setPos([new_x, new_y])
                        # Stop when close enough to target (or if max duration exceeded)
                        if (abs(dx) < rest_jump and abs(dy) < rest_jump) or animationTimer > maxAnimationDur:
                            correct_2.setPos([endX, endY])
                            if key_resp.corr:
                                polygon_8.setPos([new_x, new_y])
                            animationDone = True
                            moveCorrect = False
                            continueRoutine = False
                    
                    # *polygon_8* updates
                    
                    # if polygon_8 is starting this frame...
                    if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        polygon_8.frameNStart = frameN  # exact frame index
                        polygon_8.tStart = t  # local t and not account for scr refresh
                        polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_8.started')
                        # update status
                        polygon_8.status = STARTED
                        polygon_8.setAutoDraw(True)
                    
                    # if polygon_8 is active this frame...
                    if polygon_8.status == STARTED:
                        # update params
                        pass
                    # Run 'Each Frame' code from bids_feedback_disp
                    ## schedule bids trigger setting
                    bids.schedule_onset(correct_2,
                    type_of_stimulus="feedback", 
                    component_label="correct_moving",
                    trial_type = "learn",
                    block_name=block,
                    sequence_name=learningSeq,
                    route_num=runIndexWithinSeq, 
                    trial_num=currPosInSeq)
                    
                    
                    # *prompt_2* updates
                    
                    # if prompt_2 is starting this frame...
                    if prompt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        prompt_2.frameNStart = frameN  # exact frame index
                        prompt_2.tStart = t  # local t and not account for scr refresh
                        prompt_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(prompt_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'prompt_2.started')
                        # update status
                        prompt_2.status = STARTED
                        prompt_2.setAutoDraw(True)
                    
                    # if prompt_2 is active this frame...
                    if prompt_2.status == STARTED:
                        # update params
                        pass
                    
                    # *dist_01_2* updates
                    
                    # if dist_01_2 is starting this frame...
                    if dist_01_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        dist_01_2.frameNStart = frameN  # exact frame index
                        dist_01_2.tStart = t  # local t and not account for scr refresh
                        dist_01_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(dist_01_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist_01_2.started')
                        # update status
                        dist_01_2.status = STARTED
                        dist_01_2.setAutoDraw(True)
                    
                    # if dist_01_2 is active this frame...
                    if dist_01_2.status == STARTED:
                        # update params
                        pass
                    
                    # *dist_02_2* updates
                    
                    # if dist_02_2 is starting this frame...
                    if dist_02_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        dist_02_2.frameNStart = frameN  # exact frame index
                        dist_02_2.tStart = t  # local t and not account for scr refresh
                        dist_02_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(dist_02_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'dist_02_2.started')
                        # update status
                        dist_02_2.status = STARTED
                        dist_02_2.setAutoDraw(True)
                    
                    # if dist_02_2 is active this frame...
                    if dist_02_2.status == STARTED:
                        # update params
                        pass
                    
                    # *correct_2* updates
                    
                    # if correct_2 is starting this frame...
                    if correct_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        correct_2.frameNStart = frameN  # exact frame index
                        correct_2.tStart = t  # local t and not account for scr refresh
                        correct_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(correct_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'correct_2.started')
                        # update status
                        correct_2.status = STARTED
                        correct_2.setAutoDraw(True)
                    
                    # if correct_2 is active this frame...
                    if correct_2.status == STARTED:
                        # update params
                        pass
                    # Run 'Each Frame' code from trigger_feedback_disp
                    # feedback onset
                    feedback_trigger = trigger_dict["feedback"]
                    if moveCorrect and not feedback_trigger_sent: 
                        send_trigger(feedback_trigger)
                        feedback_trigger_sent = True 
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=feedback,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        feedback.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in feedback.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "feedback" ---
                for thisComponent in feedback.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for feedback
                feedback.tStop = globalClock.getTime(format='float')
                feedback.tStopRefresh = tThisFlipGlobal
                thisExp.addData('feedback.stopped', feedback.tStop)
                # Run 'End Routine' code from bids_feedback_disp
                #bids.add_instant(
                #    "feedback",
                #    feedback_duration = animationTimer
                #)
                
                bids.mark_offset(correct_2)
                # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "too_slow_routine" ---
                # create an object to store info about Routine too_slow_routine
                too_slow_routine = data.Routine(
                    name='too_slow_routine',
                    components=[tooSlowtext],
                )
                too_slow_routine.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from determine_start
                if responded:
                    continueRoutine = False
                tooSlowtext.setText('')
                # Run 'Begin Routine' code from set_slow_msg_text
                if language == "english":
                    tooSlowtext.text = (
                        "Too slow. You need to respond faster."
                    )
                
                if language == "german":
                    tooSlowtext.text = (
                        "Zu langsam. Sie müssen schneller antworten."
                    )
                
                if language == "french":
                    tooSlowtext.text = (
                        "Trop lent. Vous devez répondre plus rapidement. "
                    )
                
                # store start times for too_slow_routine
                too_slow_routine.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                too_slow_routine.tStart = globalClock.getTime(format='float')
                too_slow_routine.status = STARTED
                thisExp.addData('too_slow_routine.started', too_slow_routine.tStart)
                too_slow_routine.maxDuration = None
                # keep track of which components have finished
                too_slow_routineComponents = too_slow_routine.components
                for thisComponent in too_slow_routine.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "too_slow_routine" ---
                too_slow_routine.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisLearning_trial, 'status') and thisLearning_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *tooSlowtext* updates
                    
                    # if tooSlowtext is starting this frame...
                    if tooSlowtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        tooSlowtext.frameNStart = frameN  # exact frame index
                        tooSlowtext.tStart = t  # local t and not account for scr refresh
                        tooSlowtext.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(tooSlowtext, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'tooSlowtext.started')
                        # update status
                        tooSlowtext.status = STARTED
                        tooSlowtext.setAutoDraw(True)
                    
                    # if tooSlowtext is active this frame...
                    if tooSlowtext.status == STARTED:
                        # update params
                        pass
                    
                    # if tooSlowtext is stopping this frame...
                    if tooSlowtext.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > tooSlowtext.tStartRefresh + too_slow_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            tooSlowtext.tStop = t  # not accounting for scr refresh
                            tooSlowtext.tStopRefresh = tThisFlipGlobal  # on global time
                            tooSlowtext.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'tooSlowtext.stopped')
                            # update status
                            tooSlowtext.status = FINISHED
                            tooSlowtext.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=too_slow_routine,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        too_slow_routine.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in too_slow_routine.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "too_slow_routine" ---
                for thisComponent in too_slow_routine.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for too_slow_routine
                too_slow_routine.tStop = globalClock.getTime(format='float')
                too_slow_routine.tStopRefresh = tThisFlipGlobal
                thisExp.addData('too_slow_routine.stopped', too_slow_routine.tStop)
                # the Routine "too_slow_routine" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                # mark thisLearning_trial as finished
                if hasattr(thisLearning_trial, 'status'):
                    thisLearning_trial.status = FINISHED
                # if awaiting a pause, pause now
                if learning_trials.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    learning_trials.status = STARTED
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'learning_trials'
            learning_trials.status = FINISHED
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "rest_period" ---
            # create an object to store info about Routine rest_period
            rest_period = data.Routine(
                name='rest_period',
                components=[fix_cross],
            )
            rest_period.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from set_trigger_rest
            replay_endtrig_sent = False
            # store start times for rest_period
            rest_period.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            rest_period.tStart = globalClock.getTime(format='float')
            rest_period.status = STARTED
            thisExp.addData('rest_period.started', rest_period.tStart)
            rest_period.maxDuration = None
            # keep track of which components have finished
            rest_periodComponents = rest_period.components
            for thisComponent in rest_period.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "rest_period" ---
            rest_period.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from set_trigger_rest
                
                replayTrigger = trigger_dict["replay_break"]
                if frameN == 0: 
                    send_trigger(replayTrigger)
                
                
                # Run 'Each Frame' code from bids_break_logging
                # log onset at first frame
                bids.schedule_onset(
                    fix_cross,
                    type_of_stimulus="replay_break",
                    block_name = block,
                    route_num=runIndexWithinSeq,
                    component_label="fix_cross_replay_break",
                    trial_type = "learn",
                    sequence_name=learningSeq,
                    trial_num=currPosInSeq)
                
                
                
                
                
                # *fix_cross* updates
                
                # if fix_cross is starting this frame...
                if fix_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    fix_cross.frameNStart = frameN  # exact frame index
                    fix_cross.tStart = t  # local t and not account for scr refresh
                    fix_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(fix_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross.started')
                    # update status
                    fix_cross.status = STARTED
                    fix_cross.setAutoDraw(True)
                
                # if fix_cross is active this frame...
                if fix_cross.status == STARTED:
                    # update params
                    pass
                
                # if fix_cross is stopping this frame...
                if fix_cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > fix_cross.tStartRefresh + replay_break_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        fix_cross.tStop = t  # not accounting for scr refresh
                        fix_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        fix_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross.stopped')
                        # update status
                        fix_cross.status = FINISHED
                        fix_cross.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=rest_period,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    rest_period.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in rest_period.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "rest_period" ---
            for thisComponent in rest_period.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for rest_period
            rest_period.tStop = globalClock.getTime(format='float')
            rest_period.tStopRefresh = tThisFlipGlobal
            thisExp.addData('rest_period.stopped', rest_period.tStop)
            # Run 'End Routine' code from set_trigger_rest
            endTrigger = trigger_dict["replay_break_end"]
            
            if not replay_endtrig_sent:
                    send_trigger(endTrigger)
            
            
            # Run 'End Routine' code from bids_break_logging
            # log offset at last frame of routine
                
            bids.mark_offset(fix_cross)
            
            # the Routine "rest_period" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "instruction_retr_start" ---
            # create an object to store info about Routine instruction_retr_start
            instruction_retr_start = data.Routine(
                name='instruction_retr_start',
                components=[instruction_now_retr, continue_button_18],
            )
            instruction_retr_start.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from set_instruction_now_retr_text
            if language == "english":
                instruction_now_retr.text = (
                "You will now retrieve the learned associations.")
                
            if language == "german": 
                instruction_now_retr.text = (
                "Sie werden nun die gelernten Assoziationen abrufen.")
            
            # create starting attributes for continue_button_18
            continue_button_18.keys = []
            continue_button_18.rt = []
            _continue_button_18_allKeys = []
            # store start times for instruction_retr_start
            instruction_retr_start.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            instruction_retr_start.tStart = globalClock.getTime(format='float')
            instruction_retr_start.status = STARTED
            thisExp.addData('instruction_retr_start.started', instruction_retr_start.tStart)
            instruction_retr_start.maxDuration = None
            # keep track of which components have finished
            instruction_retr_startComponents = instruction_retr_start.components
            for thisComponent in instruction_retr_start.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instruction_retr_start" ---
            instruction_retr_start.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.0:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *instruction_now_retr* updates
                
                # if instruction_now_retr is starting this frame...
                if instruction_now_retr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_now_retr.frameNStart = frameN  # exact frame index
                    instruction_now_retr.tStart = t  # local t and not account for scr refresh
                    instruction_now_retr.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_now_retr, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_now_retr.started')
                    # update status
                    instruction_now_retr.status = STARTED
                    instruction_now_retr.setAutoDraw(True)
                
                # if instruction_now_retr is active this frame...
                if instruction_now_retr.status == STARTED:
                    # update params
                    pass
                
                # if instruction_now_retr is stopping this frame...
                if instruction_now_retr.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > instruction_now_retr.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        instruction_now_retr.tStop = t  # not accounting for scr refresh
                        instruction_now_retr.tStopRefresh = tThisFlipGlobal  # on global time
                        instruction_now_retr.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instruction_now_retr.stopped')
                        # update status
                        instruction_now_retr.status = FINISHED
                        instruction_now_retr.setAutoDraw(False)
                
                # *continue_button_18* updates
                waitOnFlip = False
                
                # if continue_button_18 is starting this frame...
                if continue_button_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    continue_button_18.frameNStart = frameN  # exact frame index
                    continue_button_18.tStart = t  # local t and not account for scr refresh
                    continue_button_18.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(continue_button_18, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'continue_button_18.started')
                    # update status
                    continue_button_18.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(continue_button_18.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(continue_button_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if continue_button_18 is stopping this frame...
                if continue_button_18.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > continue_button_18.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        continue_button_18.tStop = t  # not accounting for scr refresh
                        continue_button_18.tStopRefresh = tThisFlipGlobal  # on global time
                        continue_button_18.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'continue_button_18.stopped')
                        # update status
                        continue_button_18.status = FINISHED
                        continue_button_18.status = FINISHED
                if continue_button_18.status == STARTED and not waitOnFlip:
                    theseKeys = continue_button_18.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
                    _continue_button_18_allKeys.extend(theseKeys)
                    if len(_continue_button_18_allKeys):
                        continue_button_18.keys = _continue_button_18_allKeys[0].name  # just the first key pressed
                        continue_button_18.rt = _continue_button_18_allKeys[0].rt
                        continue_button_18.duration = _continue_button_18_allKeys[0].duration
                        # a response ends the routine
                        continueRoutine = False
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=instruction_retr_start,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    instruction_retr_start.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instruction_retr_start.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instruction_retr_start" ---
            for thisComponent in instruction_retr_start.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for instruction_retr_start
            instruction_retr_start.tStop = globalClock.getTime(format='float')
            instruction_retr_start.tStopRefresh = tThisFlipGlobal
            thisExp.addData('instruction_retr_start.stopped', instruction_retr_start.tStop)
            # check responses
            if continue_button_18.keys in ['', [], None]:  # No response was made
                continue_button_18.keys = None
            miniblocks.addData('continue_button_18.keys',continue_button_18.keys)
            if continue_button_18.keys != None:  # we had a response
                miniblocks.addData('continue_button_18.rt', continue_button_18.rt)
                miniblocks.addData('continue_button_18.duration', continue_button_18.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if instruction_retr_start.maxDurationReached:
                routineTimer.addTime(-instruction_retr_start.maxDuration)
            elif instruction_retr_start.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.000000)
            
            # --- Prepare to start Routine "set_retrieval_rows" ---
            # create an object to store info about Routine set_retrieval_rows
            set_retrieval_rows = data.Routine(
                name='set_retrieval_rows',
                components=[],
            )
            set_retrieval_rows.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from take_retr_routes_from_route
            selected_rows, retr_ptr = take_block(retr_pool, retr_ptr, 20*2)
            print(selected_rows)
            # store start times for set_retrieval_rows
            set_retrieval_rows.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            set_retrieval_rows.tStart = globalClock.getTime(format='float')
            set_retrieval_rows.status = STARTED
            thisExp.addData('set_retrieval_rows.started', set_retrieval_rows.tStart)
            set_retrieval_rows.maxDuration = None
            # keep track of which components have finished
            set_retrieval_rowsComponents = set_retrieval_rows.components
            for thisComponent in set_retrieval_rows.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "set_retrieval_rows" ---
            set_retrieval_rows.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=set_retrieval_rows,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    set_retrieval_rows.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in set_retrieval_rows.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "set_retrieval_rows" ---
            for thisComponent in set_retrieval_rows.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for set_retrieval_rows
            set_retrieval_rows.tStop = globalClock.getTime(format='float')
            set_retrieval_rows.tStopRefresh = tThisFlipGlobal
            thisExp.addData('set_retrieval_rows.stopped', set_retrieval_rows.tStop)
            # the Routine "set_retrieval_rows" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # set up handler to look after randomisation of conditions etc
            retrieval_trials = data.TrialHandler2(
                name='retrieval_trials',
                nReps=1.0, 
                method='sequential', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                cond_file_retrieval, 
                selection=selected_rows[0:-1:2]
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(retrieval_trials)  # add the loop to the experiment
            thisRetrieval_trial = retrieval_trials.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisRetrieval_trial.rgb)
            if thisRetrieval_trial != None:
                for paramName in thisRetrieval_trial:
                    globals()[paramName] = thisRetrieval_trial[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisRetrieval_trial in retrieval_trials:
                retrieval_trials.status = STARTED
                if hasattr(thisRetrieval_trial, 'status'):
                    thisRetrieval_trial.status = STARTED
                currentLoop = retrieval_trials
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisRetrieval_trial.rgb)
                if thisRetrieval_trial != None:
                    for paramName in thisRetrieval_trial:
                        globals()[paramName] = thisRetrieval_trial[paramName]
                
                # --- Prepare to start Routine "retr_ITI" ---
                # create an object to store info about Routine retr_ITI
                retr_ITI = data.Routine(
                    name='retr_ITI',
                    components=[fix_cross_retrbegin_2],
                )
                retr_ITI.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                fix_cross_retrbegin_2.setText('+')
                # store start times for retr_ITI
                retr_ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                retr_ITI.tStart = globalClock.getTime(format='float')
                retr_ITI.status = STARTED
                thisExp.addData('retr_ITI.started', retr_ITI.tStart)
                retr_ITI.maxDuration = None
                # keep track of which components have finished
                retr_ITIComponents = retr_ITI.components
                for thisComponent in retr_ITI.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "retr_ITI" ---
                retr_ITI.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from bids_retr_question
                    bids.schedule_onset(
                        fix_cross_retrbegin_2,
                        type_of_stimulus="fixcross",
                        component_label="retrieval_ITIcross",
                        trial_type="retr_" + str(trial_type),
                        block_name=block,
                        sequence_name=learningSeq,
                        trial_num=retrieval_trials.thisN,
                        distance_correct=distance_correct
                    )
                    
                    
                    # *fix_cross_retrbegin_2* updates
                    
                    # if fix_cross_retrbegin_2 is starting this frame...
                    if fix_cross_retrbegin_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fix_cross_retrbegin_2.frameNStart = frameN  # exact frame index
                        fix_cross_retrbegin_2.tStart = t  # local t and not account for scr refresh
                        fix_cross_retrbegin_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fix_cross_retrbegin_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross_retrbegin_2.started')
                        # update status
                        fix_cross_retrbegin_2.status = STARTED
                        fix_cross_retrbegin_2.setAutoDraw(True)
                    
                    # if fix_cross_retrbegin_2 is active this frame...
                    if fix_cross_retrbegin_2.status == STARTED:
                        # update params
                        pass
                    
                    # if fix_cross_retrbegin_2 is stopping this frame...
                    if fix_cross_retrbegin_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fix_cross_retrbegin_2.tStartRefresh + iti_dur_retr-frameTolerance:
                            # keep track of stop time/frame for later
                            fix_cross_retrbegin_2.tStop = t  # not accounting for scr refresh
                            fix_cross_retrbegin_2.tStopRefresh = tThisFlipGlobal  # on global time
                            fix_cross_retrbegin_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fix_cross_retrbegin_2.stopped')
                            # update status
                            fix_cross_retrbegin_2.status = FINISHED
                            fix_cross_retrbegin_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=retr_ITI,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        retr_ITI.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in retr_ITI.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "retr_ITI" ---
                for thisComponent in retr_ITI.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for retr_ITI
                retr_ITI.tStop = globalClock.getTime(format='float')
                retr_ITI.tStopRefresh = tThisFlipGlobal
                thisExp.addData('retr_ITI.stopped', retr_ITI.tStop)
                # Run 'End Routine' code from bids_retr_question
                bids.mark_offset(fix_cross_retrbegin_2)
                # the Routine "retr_ITI" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "first_image" ---
                # create an object to store info about Routine first_image
                first_image = data.Routine(
                    name='first_image',
                    components=[image_1],
                )
                first_image.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                image_1.setImage(img_first)
                # Run 'Begin Routine' code from bids_first_retr
                
                
                
                # store start times for first_image
                first_image.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                first_image.tStart = globalClock.getTime(format='float')
                first_image.status = STARTED
                thisExp.addData('first_image.started', first_image.tStart)
                first_image.maxDuration = None
                # keep track of which components have finished
                first_imageComponents = first_image.components
                for thisComponent in first_image.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "first_image" ---
                first_image.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_image_1
                    # ImgTrig = img_firstTrigNumber
                    ImgTrig = 101
                    
                    if frameN == 0:
                        send_trigger(ImgTrig)
                    
                    
                    # *image_1* updates
                    
                    # if image_1 is starting this frame...
                    if image_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_1.frameNStart = frameN  # exact frame index
                        image_1.tStart = t  # local t and not account for scr refresh
                        image_1.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_1, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_1.started')
                        # update status
                        image_1.status = STARTED
                        image_1.setAutoDraw(True)
                    
                    # if image_1 is active this frame...
                    if image_1.status == STARTED:
                        # update params
                        pass
                    
                    # if image_1 is stopping this frame...
                    if image_1.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_1.tStartRefresh + image_dur_retr_new-frameTolerance:
                            # keep track of stop time/frame for later
                            image_1.tStop = t  # not accounting for scr refresh
                            image_1.tStopRefresh = tThisFlipGlobal  # on global time
                            image_1.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_1.stopped')
                            # update status
                            image_1.status = FINISHED
                            image_1.setAutoDraw(False)
                    # Run 'Each Frame' code from bids_first_retr
                    ## schedule bids trigger setting
                    bids.schedule_onset(image_1, type_of_stimulus="image", 
                    component_label="image_1_retr", 
                    trial_type = "retr_" + str(trial_type),
                    concept_label = img_first.partition("/")[-1],
                    concept_exemplar = img_first.partition("/")[-1], 
                    block_name=block,
                    sequence_name=learningSeq,
                    trial_num=retrieval_trials.thisN)
                    
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=first_image,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        first_image.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in first_image.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "first_image" ---
                for thisComponent in first_image.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for first_image
                first_image.tStop = globalClock.getTime(format='float')
                first_image.tStopRefresh = tThisFlipGlobal
                thisExp.addData('first_image.stopped', first_image.tStop)
                # Run 'End Routine' code from bids_first_retr
                
                bids.mark_offset(image_1)
                
                # the Routine "first_image" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "mask_retr1" ---
                # create an object to store info about Routine mask_retr1
                mask_retr1 = data.Routine(
                    name='mask_retr1',
                    components=[mask_img1_2],
                )
                mask_retr1.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for mask_retr1
                mask_retr1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                mask_retr1.tStart = globalClock.getTime(format='float')
                mask_retr1.status = STARTED
                thisExp.addData('mask_retr1.started', mask_retr1.tStart)
                mask_retr1.maxDuration = None
                # keep track of which components have finished
                mask_retr1Components = mask_retr1.components
                for thisComponent in mask_retr1.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "mask_retr1" ---
                mask_retr1.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.25:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *mask_img1_2* updates
                    
                    # if mask_img1_2 is starting this frame...
                    if mask_img1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mask_img1_2.frameNStart = frameN  # exact frame index
                        mask_img1_2.tStart = t  # local t and not account for scr refresh
                        mask_img1_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mask_img1_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'mask_img1_2.started')
                        # update status
                        mask_img1_2.status = STARTED
                        mask_img1_2.setAutoDraw(True)
                    
                    # if mask_img1_2 is active this frame...
                    if mask_img1_2.status == STARTED:
                        # update params
                        pass
                    
                    # if mask_img1_2 is stopping this frame...
                    if mask_img1_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > mask_img1_2.tStartRefresh + 0.25-frameTolerance:
                            # keep track of stop time/frame for later
                            mask_img1_2.tStop = t  # not accounting for scr refresh
                            mask_img1_2.tStopRefresh = tThisFlipGlobal  # on global time
                            mask_img1_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'mask_img1_2.stopped')
                            # update status
                            mask_img1_2.status = FINISHED
                            mask_img1_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=mask_retr1,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        mask_retr1.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in mask_retr1.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "mask_retr1" ---
                for thisComponent in mask_retr1.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for mask_retr1
                mask_retr1.tStop = globalClock.getTime(format='float')
                mask_retr1.tStopRefresh = tThisFlipGlobal
                thisExp.addData('mask_retr1.stopped', mask_retr1.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if mask_retr1.maxDurationReached:
                    routineTimer.addTime(-mask_retr1.maxDuration)
                elif mask_retr1.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.250000)
                
                # --- Prepare to start Routine "second_image" ---
                # create an object to store info about Routine second_image
                second_image = data.Routine(
                    name='second_image',
                    components=[image_2],
                )
                second_image.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                image_2.setImage(img_second)
                # Run 'Begin Routine' code from bids_second_retr
                
                
                # store start times for second_image
                second_image.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                second_image.tStart = globalClock.getTime(format='float')
                second_image.status = STARTED
                thisExp.addData('second_image.started', second_image.tStart)
                second_image.maxDuration = None
                # keep track of which components have finished
                second_imageComponents = second_image.components
                for thisComponent in second_image.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "second_image" ---
                second_image.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_image_2
                    # ImgTrig = img_secondTrigNumber
                    ImgTrig = 102
                    if frameN == 0:
                        send_trigger(ImgTrig)
                    
                    
                    # *image_2* updates
                    
                    # if image_2 is starting this frame...
                    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        image_2.frameNStart = frameN  # exact frame index
                        image_2.tStart = t  # local t and not account for scr refresh
                        image_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.started')
                        # update status
                        image_2.status = STARTED
                        image_2.setAutoDraw(True)
                    
                    # if image_2 is active this frame...
                    if image_2.status == STARTED:
                        # update params
                        pass
                    
                    # if image_2 is stopping this frame...
                    if image_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > image_2.tStartRefresh + image_dur_retr_new-frameTolerance:
                            # keep track of stop time/frame for later
                            image_2.tStop = t  # not accounting for scr refresh
                            image_2.tStopRefresh = tThisFlipGlobal  # on global time
                            image_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image_2.stopped')
                            # update status
                            image_2.status = FINISHED
                            image_2.setAutoDraw(False)
                    # Run 'Each Frame' code from bids_second_retr
                    ## schedule bids trigger setting
                    bids.schedule_onset(image_2, type_of_stimulus="image", 
                    component_label="image_2_retr", 
                    trial_type = "retr_" + str(trial_type),
                    concept_label = img_second.partition("/")[-1],
                    concept_exemplar = img_second.partition("/")[-1], 
                    block_name=block,
                    sequence_name=learningSeq,
                    trial_num=retrieval_trials.thisN)
                    
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=second_image,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        second_image.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in second_image.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "second_image" ---
                for thisComponent in second_image.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for second_image
                second_image.tStop = globalClock.getTime(format='float')
                second_image.tStopRefresh = tThisFlipGlobal
                thisExp.addData('second_image.stopped', second_image.tStop)
                # Run 'End Routine' code from bids_second_retr
                
                bids.mark_offset(image_2)
                
                # the Routine "second_image" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "mask_retr2" ---
                # create an object to store info about Routine mask_retr2
                mask_retr2 = data.Routine(
                    name='mask_retr2',
                    components=[mask_img2_2],
                )
                mask_retr2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # store start times for mask_retr2
                mask_retr2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                mask_retr2.tStart = globalClock.getTime(format='float')
                mask_retr2.status = STARTED
                thisExp.addData('mask_retr2.started', mask_retr2.tStart)
                mask_retr2.maxDuration = None
                # keep track of which components have finished
                mask_retr2Components = mask_retr2.components
                for thisComponent in mask_retr2.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "mask_retr2" ---
                mask_retr2.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 0.25:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *mask_img2_2* updates
                    
                    # if mask_img2_2 is starting this frame...
                    if mask_img2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        mask_img2_2.frameNStart = frameN  # exact frame index
                        mask_img2_2.tStart = t  # local t and not account for scr refresh
                        mask_img2_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mask_img2_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'mask_img2_2.started')
                        # update status
                        mask_img2_2.status = STARTED
                        mask_img2_2.setAutoDraw(True)
                    
                    # if mask_img2_2 is active this frame...
                    if mask_img2_2.status == STARTED:
                        # update params
                        pass
                    
                    # if mask_img2_2 is stopping this frame...
                    if mask_img2_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > mask_img2_2.tStartRefresh + 0.25-frameTolerance:
                            # keep track of stop time/frame for later
                            mask_img2_2.tStop = t  # not accounting for scr refresh
                            mask_img2_2.tStopRefresh = tThisFlipGlobal  # on global time
                            mask_img2_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'mask_img2_2.stopped')
                            # update status
                            mask_img2_2.status = FINISHED
                            mask_img2_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=mask_retr2,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        mask_retr2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in mask_retr2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "mask_retr2" ---
                for thisComponent in mask_retr2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for mask_retr2
                mask_retr2.tStop = globalClock.getTime(format='float')
                mask_retr2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('mask_retr2.stopped', mask_retr2.tStop)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if mask_retr2.maxDurationReached:
                    routineTimer.addTime(-mask_retr2.maxDuration)
                elif mask_retr2.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-0.250000)
                
                # --- Prepare to start Routine "reflection_period_retr" ---
                # create an object to store info about Routine reflection_period_retr
                reflection_period_retr = data.Routine(
                    name='reflection_period_retr',
                    components=[fix_cross_reflretr],
                )
                reflection_period_retr.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from set_trigger_reflection
                end_trig_send = False
                # store start times for reflection_period_retr
                reflection_period_retr.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                reflection_period_retr.tStart = globalClock.getTime(format='float')
                reflection_period_retr.status = STARTED
                thisExp.addData('reflection_period_retr.started', reflection_period_retr.tStart)
                reflection_period_retr.maxDuration = None
                # keep track of which components have finished
                reflection_period_retrComponents = reflection_period_retr.components
                for thisComponent in reflection_period_retr.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "reflection_period_retr" ---
                reflection_period_retr.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_reflection
                    ReflTrig = trigger_dict["reflection_per"]
                    
                    if frameN == 0:
                        send_trigger(ReflTrig)
                    
                    
                    # *fix_cross_reflretr* updates
                    
                    # if fix_cross_reflretr is starting this frame...
                    if fix_cross_reflretr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        fix_cross_reflretr.frameNStart = frameN  # exact frame index
                        fix_cross_reflretr.tStart = t  # local t and not account for scr refresh
                        fix_cross_reflretr.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(fix_cross_reflretr, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'fix_cross_reflretr.started')
                        # update status
                        fix_cross_reflretr.status = STARTED
                        fix_cross_reflretr.setAutoDraw(True)
                    
                    # if fix_cross_reflretr is active this frame...
                    if fix_cross_reflretr.status == STARTED:
                        # update params
                        pass
                    
                    # if fix_cross_reflretr is stopping this frame...
                    if fix_cross_reflretr.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > fix_cross_reflretr.tStartRefresh + reflection_win_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            fix_cross_reflretr.tStop = t  # not accounting for scr refresh
                            fix_cross_reflretr.tStopRefresh = tThisFlipGlobal  # on global time
                            fix_cross_reflretr.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'fix_cross_reflretr.stopped')
                            # update status
                            fix_cross_reflretr.status = FINISHED
                            fix_cross_reflretr.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=reflection_period_retr,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        reflection_period_retr.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in reflection_period_retr.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "reflection_period_retr" ---
                for thisComponent in reflection_period_retr.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for reflection_period_retr
                reflection_period_retr.tStop = globalClock.getTime(format='float')
                reflection_period_retr.tStopRefresh = tThisFlipGlobal
                thisExp.addData('reflection_period_retr.stopped', reflection_period_retr.tStop)
                # Run 'End Routine' code from set_trigger_reflection
                ReflTrigEnd = trigger_dict["reflection_per_end"]
                
                if not end_trig_send:
                    send_trigger(ReflTrigEnd)
                    end_trig_send = True
                    core.wait(0.01) # wait so no overlap with next img trigger
                
                # the Routine "reflection_period_retr" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "retr_response_order" ---
                # create an object to store info about Routine retr_response_order
                retr_response_order = data.Routine(
                    name='retr_response_order',
                    components=[polygon_6, yes_txt, no_txt, chooseNowText_2, resp],
                )
                retr_response_order.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from set_trigger_opt_onset
                
                
                # Run 'Begin Routine' code from clear_clock_3
                _resp_allKeys = None
                resp.clearEvents()
                retrClock = core.Clock()
                retrClock.reset()
                
                polygon_6.setPos((0,0))
                polygon_6.setOpacity(0)
                yes_txt.setPos([leftside_retr if opt_left=="yes" else rightside_retr])
                no_txt.setPos([rightside_retr if opt_right=="no" else leftside_retr])
                # Run 'Begin Routine' code from set_option_text_2
                
                if language == "english": 
                    yes_txt.text = ("yes")
                    no_txt.text = ("no")
                if language == "german":
                    yes_txt.text = ("ja")
                    no_txt.text = ("nein")
                if language == "french": 
                    yes_txt.text = ("oui")
                    no_txt.text = ("non")
                # Run 'Begin Routine' code from end_routine_after_resp
                # initialize
                responded_retr = False
                delayClock = None
                delayDone = False
                chooseNowText_2.setOpacity(0.0)
                # create starting attributes for resp
                resp.keys = []
                resp.rt = []
                _resp_allKeys = []
                # Run 'Begin Routine' code from set_trigger_retr_response
                
                retr_trig_sent = False
                
                # store start times for retr_response_order
                retr_response_order.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                retr_response_order.tStart = globalClock.getTime(format='float')
                retr_response_order.status = STARTED
                thisExp.addData('retr_response_order.started', retr_response_order.tStart)
                retr_response_order.maxDuration = None
                # keep track of which components have finished
                retr_response_orderComponents = retr_response_order.components
                for thisComponent in retr_response_order.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "retr_response_order" ---
                retr_response_order.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_opt_onset
                    OptTrig = trigger_dict["order_retrieval_options"]
                    
                    if frameN == 0:
                        send_trigger(OptTrig)
                        core.wait(0.01)
                    
                    
                    # *polygon_6* updates
                    
                    # if polygon_6 is starting this frame...
                    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        polygon_6.frameNStart = frameN  # exact frame index
                        polygon_6.tStart = t  # local t and not account for scr refresh
                        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.started')
                        # update status
                        polygon_6.status = STARTED
                        polygon_6.setAutoDraw(True)
                    
                    # if polygon_6 is active this frame...
                    if polygon_6.status == STARTED:
                        # update params
                        pass
                    
                    # *yes_txt* updates
                    
                    # if yes_txt is starting this frame...
                    if yes_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        yes_txt.frameNStart = frameN  # exact frame index
                        yes_txt.tStart = t  # local t and not account for scr refresh
                        yes_txt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(yes_txt, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'yes_txt.started')
                        # update status
                        yes_txt.status = STARTED
                        yes_txt.setAutoDraw(True)
                    
                    # if yes_txt is active this frame...
                    if yes_txt.status == STARTED:
                        # update params
                        pass
                    
                    # if yes_txt is stopping this frame...
                    if yes_txt.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > yes_txt.tStartRefresh + retr_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            yes_txt.tStop = t  # not accounting for scr refresh
                            yes_txt.tStopRefresh = tThisFlipGlobal  # on global time
                            yes_txt.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'yes_txt.stopped')
                            # update status
                            yes_txt.status = FINISHED
                            yes_txt.setAutoDraw(False)
                    
                    # *no_txt* updates
                    
                    # if no_txt is starting this frame...
                    if no_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        no_txt.frameNStart = frameN  # exact frame index
                        no_txt.tStart = t  # local t and not account for scr refresh
                        no_txt.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(no_txt, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'no_txt.started')
                        # update status
                        no_txt.status = STARTED
                        no_txt.setAutoDraw(True)
                    
                    # if no_txt is active this frame...
                    if no_txt.status == STARTED:
                        # update params
                        pass
                    
                    # if no_txt is stopping this frame...
                    if no_txt.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > no_txt.tStartRefresh + retr_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            no_txt.tStop = t  # not accounting for scr refresh
                            no_txt.tStopRefresh = tThisFlipGlobal  # on global time
                            no_txt.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'no_txt.stopped')
                            # update status
                            no_txt.status = FINISHED
                            no_txt.setAutoDraw(False)
                    # Run 'Each Frame' code from end_routine_after_resp
                    if retrClock.getTime() >= retr_dur and not responded_retr:
                        # Timeout
                        responded_retr = False
                        continueRoutine = False
                    
                    if not responded_retr:
                        key_list = resp.getKeys(keyList=[left_key, right_key], waitRelease=False)
                        if len(key_list) > 0:
                            responded_retr = True
                            thisResp = key_list[0]
                            if thisResp.name == left_key:
                                chosenPos = [-0.06, 0]
                            elif thisResp.name == right_key:
                                chosenPos = [0.06, 0]
                            resp.keys = thisResp.name
                            resp.rt = thisResp.rt
                            resp.duration = thisResp.duration
                            if thisResp.name == correct_key:
                                resp.corr = 1
                            else:
                                resp.corr = 0
                                practice_errors += 1
                            polygon_6.setPos(chosenPos)
                            polygon_6.setOpacity(1.0)
                            delayClock = core.Clock()
                    
                    if responded_retr and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                        delayDone = True
                        continueRoutine = False
                    
                    if retrClock.getTime() >= (retr_dur-1) and not responded_retr:
                        chooseNowText_2.setOpacity(1)
                    
                    # *chooseNowText_2* updates
                    
                    # if chooseNowText_2 is starting this frame...
                    if chooseNowText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        chooseNowText_2.frameNStart = frameN  # exact frame index
                        chooseNowText_2.tStart = t  # local t and not account for scr refresh
                        chooseNowText_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(chooseNowText_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'chooseNowText_2.started')
                        # update status
                        chooseNowText_2.status = STARTED
                        chooseNowText_2.setAutoDraw(True)
                    
                    # if chooseNowText_2 is active this frame...
                    if chooseNowText_2.status == STARTED:
                        # update params
                        pass
                    
                    # *resp* updates
                    waitOnFlip = False
                    
                    # if resp is starting this frame...
                    if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        resp.frameNStart = frameN  # exact frame index
                        resp.tStart = t  # local t and not account for scr refresh
                        resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp.started')
                        # update status
                        resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if resp is stopping this frame...
                    if resp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > resp.tStartRefresh + retr_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            resp.tStop = t  # not accounting for scr refresh
                            resp.tStopRefresh = tThisFlipGlobal  # on global time
                            resp.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'resp.stopped')
                            # update status
                            resp.status = FINISHED
                            resp.status = FINISHED
                    if resp.status == STARTED and not waitOnFlip:
                        theseKeys = resp.getKeys(keyList=[left_key, right_key], ignoreKeys=["escape"], waitRelease=False)
                        _resp_allKeys.extend(theseKeys)
                        if len(_resp_allKeys):
                            resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                            resp.rt = _resp_allKeys[-1].rt
                            resp.duration = _resp_allKeys[-1].duration
                    # Run 'Each Frame' code from set_trigger_retr_response
                    RespTrig = trigger_dict["order_retrieval_response"]
                    
                    if not retr_trig_sent:
                            if resp.keys:
                                retr_trig_sent = True
                    
                                send_trigger(RespTrig)
                                core.wait(0.01) # need to wait a bit to avoid overlap with question trigger
                    
                    
                               
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=retr_response_order,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        retr_response_order.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in retr_response_order.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "retr_response_order" ---
                for thisComponent in retr_response_order.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for retr_response_order
                retr_response_order.tStop = globalClock.getTime(format='float')
                retr_response_order.tStopRefresh = tThisFlipGlobal
                thisExp.addData('retr_response_order.stopped', retr_response_order.tStop)
                # check responses
                if resp.keys in ['', [], None]:  # No response was made
                    resp.keys = None
                retrieval_trials.addData('resp.keys',resp.keys)
                if resp.keys != None:  # we had a response
                    retrieval_trials.addData('resp.rt', resp.rt)
                    retrieval_trials.addData('resp.duration', resp.duration)
                # Run 'End Routine' code from bids_retr_response
                
                # response neeeds to be saved at end of trial
                pressed = resp.keys
                if isinstance(pressed, list):
                    pressed = pressed[-1] if pressed else "m"
                
                chosen_pos  = key2pos.get(pressed, None)
                is_correct = (str(chosen_pos) == str(correct_key))
                
                bids.add_instant(
                "choice",
                distance_correct = distance_correct,
                trial_type = "retr_order", 
                block_name=block,
                sequence_name=learningSeq,
                trial_num=retrieval_trials.thisN,
                response=(resp.keys if resp.keys else "m"),
                response_time=(resp.rt if hasattr(resp, "rt") else None),
                correct=is_correct,
                expected_response = correct_key, 
                response_meaning = chosen_pos
                )
                
                # the Routine "retr_response_order" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "too_slow_routine_1" ---
                # create an object to store info about Routine too_slow_routine_1
                too_slow_routine_1 = data.Routine(
                    name='too_slow_routine_1',
                    components=[tooSlowtext_4],
                )
                too_slow_routine_1.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from determine_start_4
                if responded_retr:
                    continueRoutine = False
                tooSlowtext_4.setText('')
                # Run 'Begin Routine' code from set_slow_msg_text_4
                if language == "english":
                    tooSlowtext_4.text = (
                        "Too slow. You need to respond faster."
                    )
                
                if language == "german":
                    tooSlowtext_4.text = (
                        "Zu langsam. Sie müssen schneller antworten."
                    )
                
                if language == "french":
                    tooSlowtext_4.text = (
                        "Trop lent. Vous devez répondre plus rapidement. "
                    )
                
                # store start times for too_slow_routine_1
                too_slow_routine_1.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                too_slow_routine_1.tStart = globalClock.getTime(format='float')
                too_slow_routine_1.status = STARTED
                thisExp.addData('too_slow_routine_1.started', too_slow_routine_1.tStart)
                too_slow_routine_1.maxDuration = None
                # keep track of which components have finished
                too_slow_routine_1Components = too_slow_routine_1.components
                for thisComponent in too_slow_routine_1.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "too_slow_routine_1" ---
                too_slow_routine_1.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *tooSlowtext_4* updates
                    
                    # if tooSlowtext_4 is starting this frame...
                    if tooSlowtext_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        tooSlowtext_4.frameNStart = frameN  # exact frame index
                        tooSlowtext_4.tStart = t  # local t and not account for scr refresh
                        tooSlowtext_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(tooSlowtext_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'tooSlowtext_4.started')
                        # update status
                        tooSlowtext_4.status = STARTED
                        tooSlowtext_4.setAutoDraw(True)
                    
                    # if tooSlowtext_4 is active this frame...
                    if tooSlowtext_4.status == STARTED:
                        # update params
                        pass
                    
                    # if tooSlowtext_4 is stopping this frame...
                    if tooSlowtext_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > tooSlowtext_4.tStartRefresh + too_slow_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            tooSlowtext_4.tStop = t  # not accounting for scr refresh
                            tooSlowtext_4.tStopRefresh = tThisFlipGlobal  # on global time
                            tooSlowtext_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'tooSlowtext_4.stopped')
                            # update status
                            tooSlowtext_4.status = FINISHED
                            tooSlowtext_4.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=too_slow_routine_1,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        too_slow_routine_1.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in too_slow_routine_1.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "too_slow_routine_1" ---
                for thisComponent in too_slow_routine_1.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for too_slow_routine_1
                too_slow_routine_1.tStop = globalClock.getTime(format='float')
                too_slow_routine_1.tStopRefresh = tThisFlipGlobal
                thisExp.addData('too_slow_routine_1.stopped', too_slow_routine_1.tStop)
                # the Routine "too_slow_routine_1" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "retr_response_distance" ---
                # create an object to store info about Routine retr_response_distance
                retr_response_distance = data.Routine(
                    name='retr_response_distance',
                    components=[chooseNowText_3, resp_4, opt_2, opt_3, opt_4, opt_5],
                )
                retr_response_distance.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from clear_clock_4
                _resp_4_allKeys = None
                resp_4.clearEvents()
                retrClock = core.Clock()
                retrClock.reset()
                
                
                # Run 'Begin Routine' code from controlslider_pos_js
                responded_retr_slider = False
                delayClock = None
                delayDone = False
                chosenDis = None
                chooseNowText_3.setOpacity(0.0)
                # create starting attributes for resp_4
                resp_4.keys = []
                resp_4.rt = []
                _resp_4_allKeys = []
                opt_2.setColor('white', colorSpace='rgb')
                opt_3.setColor('white', colorSpace='rgb')
                opt_4.setColor('white', colorSpace='rgb')
                opt_5.setColor('white', colorSpace='rgb')
                # Run 'Begin Routine' code from set_trigger_retr_response_2
                
                retr_trig_sent = False
                
                # store start times for retr_response_distance
                retr_response_distance.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                retr_response_distance.tStart = globalClock.getTime(format='float')
                retr_response_distance.status = STARTED
                thisExp.addData('retr_response_distance.started', retr_response_distance.tStart)
                retr_response_distance.maxDuration = None
                # keep track of which components have finished
                retr_response_distanceComponents = retr_response_distance.components
                for thisComponent in retr_response_distance.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "retr_response_distance" ---
                retr_response_distance.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    # Run 'Each Frame' code from set_trigger_opt_onset_2
                    OptTrig = trigger_dict["distance_retrieval_options"]
                    
                    if frameN == 0:
                        send_trigger(OptTrig)
                        core.wait(0.01)
                    
                    # Run 'Each Frame' code from controlslider_pos_js
                    #if slider_main.markerPos is None:
                        #possible_positions = [0, 1, 2, 3, 4]
                        #slider_main.markerPos = random.choice(possible_positions)
                    
                    #slider_main.markerPos = max(0, min(4, slider_main.markerPos))
                    
                           
                    keysPressed = resp_4.getKeys(keyList=[left_key, right_key, center_key, down_key], waitRelease=False) # from event.getKeys
                    if len(keysPressed) > 0:
                        chosen_key = keysPressed[0]  # extract the string from the KeyPress object
                        if chosen_key.name == left_key:
                            chosenDis = 5
                            opt_5.color = "blue"
                        elif chosen_key.name == right_key:
                            chosenDis = 3
                            opt_3.color = "blue"
                        elif chosen_key.name == center_key:
                            chosenDis = 2
                            opt_2.color = "blue"
                    
                        elif chosen_key.name == down_key:
                            chosenDis = 4
                            opt_4.color = "blue"
                    
                            
                            
                        resp_4.keys = chosenDis
                        resp_4.rt = chosen_key.rt
                        resp_4.duration = chosen_key.duration
                        if chosenDis == distance_correct:
                            resp_4.corr = 1
                        else:
                            resp_4.corr = 0
                        
                        responded_retr_slider = True
                        delayClock = core.Clock()
                    
                    if responded_retr_slider and not delayDone and delayClock is not None and delayClock.getTime() >= 0.1:
                        delayDone = True
                        continueRoutine = False
                    
                    if not responded_retr_slider and retrClock.getTime() >= (retr_dur_slider-1):
                        chooseNowText_3.setOpacity(1)
                    
                    # *chooseNowText_3* updates
                    
                    # if chooseNowText_3 is starting this frame...
                    if chooseNowText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        chooseNowText_3.frameNStart = frameN  # exact frame index
                        chooseNowText_3.tStart = t  # local t and not account for scr refresh
                        chooseNowText_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(chooseNowText_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'chooseNowText_3.started')
                        # update status
                        chooseNowText_3.status = STARTED
                        chooseNowText_3.setAutoDraw(True)
                    
                    # if chooseNowText_3 is active this frame...
                    if chooseNowText_3.status == STARTED:
                        # update params
                        pass
                    
                    # if chooseNowText_3 is stopping this frame...
                    if chooseNowText_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > chooseNowText_3.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            chooseNowText_3.tStop = t  # not accounting for scr refresh
                            chooseNowText_3.tStopRefresh = tThisFlipGlobal  # on global time
                            chooseNowText_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'chooseNowText_3.stopped')
                            # update status
                            chooseNowText_3.status = FINISHED
                            chooseNowText_3.setAutoDraw(False)
                    
                    # *resp_4* updates
                    waitOnFlip = False
                    
                    # if resp_4 is starting this frame...
                    if resp_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                        # keep track of start time/frame for later
                        resp_4.frameNStart = frameN  # exact frame index
                        resp_4.tStart = t  # local t and not account for scr refresh
                        resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(resp_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'resp_4.started')
                        # update status
                        resp_4.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(resp_4.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if resp_4 is stopping this frame...
                    if resp_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > resp_4.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            resp_4.tStop = t  # not accounting for scr refresh
                            resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                            resp_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'resp_4.stopped')
                            # update status
                            resp_4.status = FINISHED
                            resp_4.status = FINISHED
                    if resp_4.status == STARTED and not waitOnFlip:
                        theseKeys = resp_4.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
                        _resp_4_allKeys.extend(theseKeys)
                        if len(_resp_4_allKeys):
                            resp_4.keys = _resp_4_allKeys[-1].name  # just the last key pressed
                            resp_4.rt = _resp_4_allKeys[-1].rt
                            resp_4.duration = _resp_4_allKeys[-1].duration
                    
                    # *opt_2* updates
                    
                    # if opt_2 is starting this frame...
                    if opt_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        opt_2.frameNStart = frameN  # exact frame index
                        opt_2.tStart = t  # local t and not account for scr refresh
                        opt_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(opt_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_2.started')
                        # update status
                        opt_2.status = STARTED
                        opt_2.setAutoDraw(True)
                    
                    # if opt_2 is active this frame...
                    if opt_2.status == STARTED:
                        # update params
                        pass
                    
                    # if opt_2 is stopping this frame...
                    if opt_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > opt_2.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            opt_2.tStop = t  # not accounting for scr refresh
                            opt_2.tStopRefresh = tThisFlipGlobal  # on global time
                            opt_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'opt_2.stopped')
                            # update status
                            opt_2.status = FINISHED
                            opt_2.setAutoDraw(False)
                    
                    # *opt_3* updates
                    
                    # if opt_3 is starting this frame...
                    if opt_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        opt_3.frameNStart = frameN  # exact frame index
                        opt_3.tStart = t  # local t and not account for scr refresh
                        opt_3.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(opt_3, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_3.started')
                        # update status
                        opt_3.status = STARTED
                        opt_3.setAutoDraw(True)
                    
                    # if opt_3 is active this frame...
                    if opt_3.status == STARTED:
                        # update params
                        pass
                    
                    # if opt_3 is stopping this frame...
                    if opt_3.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > opt_3.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            opt_3.tStop = t  # not accounting for scr refresh
                            opt_3.tStopRefresh = tThisFlipGlobal  # on global time
                            opt_3.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'opt_3.stopped')
                            # update status
                            opt_3.status = FINISHED
                            opt_3.setAutoDraw(False)
                    
                    # *opt_4* updates
                    
                    # if opt_4 is starting this frame...
                    if opt_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        opt_4.frameNStart = frameN  # exact frame index
                        opt_4.tStart = t  # local t and not account for scr refresh
                        opt_4.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(opt_4, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_4.started')
                        # update status
                        opt_4.status = STARTED
                        opt_4.setAutoDraw(True)
                    
                    # if opt_4 is active this frame...
                    if opt_4.status == STARTED:
                        # update params
                        pass
                    
                    # if opt_4 is stopping this frame...
                    if opt_4.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > opt_4.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            opt_4.tStop = t  # not accounting for scr refresh
                            opt_4.tStopRefresh = tThisFlipGlobal  # on global time
                            opt_4.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'opt_4.stopped')
                            # update status
                            opt_4.status = FINISHED
                            opt_4.setAutoDraw(False)
                    
                    # *opt_5* updates
                    
                    # if opt_5 is starting this frame...
                    if opt_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        opt_5.frameNStart = frameN  # exact frame index
                        opt_5.tStart = t  # local t and not account for scr refresh
                        opt_5.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(opt_5, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'opt_5.started')
                        # update status
                        opt_5.status = STARTED
                        opt_5.setAutoDraw(True)
                    
                    # if opt_5 is active this frame...
                    if opt_5.status == STARTED:
                        # update params
                        pass
                    
                    # if opt_5 is stopping this frame...
                    if opt_5.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > opt_5.tStartRefresh + retr_dur_slider-frameTolerance:
                            # keep track of stop time/frame for later
                            opt_5.tStop = t  # not accounting for scr refresh
                            opt_5.tStopRefresh = tThisFlipGlobal  # on global time
                            opt_5.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'opt_5.stopped')
                            # update status
                            opt_5.status = FINISHED
                            opt_5.setAutoDraw(False)
                    # Run 'Each Frame' code from set_trigger_retr_response_2
                    RespTrig = trigger_dict["distance_retrieval_response"]
                    
                    if not retr_trig_sent:
                            if resp_4.keys:
                                retr_trig_sent = True
                    
                                send_trigger(RespTrig)
                                core.wait(0.01) # need to wait a bit to avoid overlap with question trigger
                    
                    
                               
                    
                    
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=retr_response_distance,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        retr_response_distance.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in retr_response_distance.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "retr_response_distance" ---
                for thisComponent in retr_response_distance.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for retr_response_distance
                retr_response_distance.tStop = globalClock.getTime(format='float')
                retr_response_distance.tStopRefresh = tThisFlipGlobal
                thisExp.addData('retr_response_distance.stopped', retr_response_distance.tStop)
                # check responses
                if resp_4.keys in ['', [], None]:  # No response was made
                    resp_4.keys = None
                retrieval_trials.addData('resp_4.keys',resp_4.keys)
                if resp_4.keys != None:  # we had a response
                    retrieval_trials.addData('resp_4.rt', resp_4.rt)
                    retrieval_trials.addData('resp_4.duration', resp_4.duration)
                # Run 'End Routine' code from bids_retr_response_2
                
                # response neeeds to be saved at end of trial
                if resp_4.keys:
                    
                    chosen_num = chosenDis
                    is_correct = (chosen_num == distance_correct)
                
                bids.add_instant(
                "choice",
                distance_correct = distance_correct,
                trial_type = "retr_distance",
                block_name=block,
                sequence_name=learningSeq,
                trial_num=retrieval_trials.thisN,
                response=chosen_num if chosenDis else "m",
                response_time=(resp.rt if hasattr(resp, "rt") else None),
                correct=is_correct,
                expected_response = distance_correct, 
                response_meaning = chosenDis
                )
                
                # the Routine "retr_response_distance" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "too_slow_routine_2" ---
                # create an object to store info about Routine too_slow_routine_2
                too_slow_routine_2 = data.Routine(
                    name='too_slow_routine_2',
                    components=[tooSlowtext_2],
                )
                too_slow_routine_2.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                # Run 'Begin Routine' code from determine_start_2
                if responded_retr_slider:
                    continueRoutine = False
                tooSlowtext_2.setText('')
                # Run 'Begin Routine' code from set_slow_msg_text_2
                if language == "english":
                    tooSlowtext_2.text = (
                        "Too slow. You need to respond faster."
                    )
                
                if language == "german":
                    tooSlowtext_2.text = (
                        "Zu langsam. Sie müssen schneller antworten."
                    )
                
                if language == "french":
                    tooSlowtext_2.text = (
                        "Trop lent. Vous devez répondre plus rapidement. "
                    )
                
                # store start times for too_slow_routine_2
                too_slow_routine_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                too_slow_routine_2.tStart = globalClock.getTime(format='float')
                too_slow_routine_2.status = STARTED
                thisExp.addData('too_slow_routine_2.started', too_slow_routine_2.tStart)
                too_slow_routine_2.maxDuration = None
                # keep track of which components have finished
                too_slow_routine_2Components = too_slow_routine_2.components
                for thisComponent in too_slow_routine_2.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "too_slow_routine_2" ---
                too_slow_routine_2.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine:
                    # if trial has changed, end Routine now
                    if hasattr(thisRetrieval_trial, 'status') and thisRetrieval_trial.status == STOPPING:
                        continueRoutine = False
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *tooSlowtext_2* updates
                    
                    # if tooSlowtext_2 is starting this frame...
                    if tooSlowtext_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        tooSlowtext_2.frameNStart = frameN  # exact frame index
                        tooSlowtext_2.tStart = t  # local t and not account for scr refresh
                        tooSlowtext_2.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(tooSlowtext_2, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'tooSlowtext_2.started')
                        # update status
                        tooSlowtext_2.status = STARTED
                        tooSlowtext_2.setAutoDraw(True)
                    
                    # if tooSlowtext_2 is active this frame...
                    if tooSlowtext_2.status == STARTED:
                        # update params
                        pass
                    
                    # if tooSlowtext_2 is stopping this frame...
                    if tooSlowtext_2.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > tooSlowtext_2.tStartRefresh + too_slow_dur-frameTolerance:
                            # keep track of stop time/frame for later
                            tooSlowtext_2.tStop = t  # not accounting for scr refresh
                            tooSlowtext_2.tStopRefresh = tThisFlipGlobal  # on global time
                            tooSlowtext_2.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'tooSlowtext_2.stopped')
                            # update status
                            tooSlowtext_2.status = FINISHED
                            tooSlowtext_2.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer, globalClock], 
                            currentRoutine=too_slow_routine_2,
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        too_slow_routine_2.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in too_slow_routine_2.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "too_slow_routine_2" ---
                for thisComponent in too_slow_routine_2.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for too_slow_routine_2
                too_slow_routine_2.tStop = globalClock.getTime(format='float')
                too_slow_routine_2.tStopRefresh = tThisFlipGlobal
                thisExp.addData('too_slow_routine_2.stopped', too_slow_routine_2.tStop)
                # the Routine "too_slow_routine_2" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                # mark thisRetrieval_trial as finished
                if hasattr(thisRetrieval_trial, 'status'):
                    thisRetrieval_trial.status = FINISHED
                # if awaiting a pause, pause now
                if retrieval_trials.status == PAUSED:
                    thisExp.status = PAUSED
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[globalClock], 
                    )
                    # once done pausing, restore running status
                    retrieval_trials.status = STARTED
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'retrieval_trials'
            retrieval_trials.status = FINISHED
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            # --- Prepare to start Routine "retr_task_break" ---
            # create an object to store info about Routine retr_task_break
            retr_task_break = data.Routine(
                name='retr_task_break',
                components=[break_instruction],
            )
            retr_task_break.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from determine_break_start
            continueRoutine = (miniblocks.thisN + 1) % break_after_route == 0
            
            if continueRoutine:
                run_break = True
            else:
                run_break = False 
            # Run 'Begin Routine' code from trigger_long_break_start
            end_trig_send = False
            # store start times for retr_task_break
            retr_task_break.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            retr_task_break.tStart = globalClock.getTime(format='float')
            retr_task_break.status = STARTED
            thisExp.addData('retr_task_break.started', retr_task_break.tStart)
            retr_task_break.maxDuration = None
            # keep track of which components have finished
            retr_task_breakComponents = retr_task_break.components
            for thisComponent in retr_task_break.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "retr_task_break" ---
            retr_task_break.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # Run 'Each Frame' code from bids_longbreak_logging
                # log onset at first frame
                
                bids.schedule_onset(break_instruction,
                    trial_type = "break",
                    type_of_stimulus="long_break_retrieval",
                    block_name = block,
                    component_label="instruction_task_break_ret")
                
                
                
                
                
                # *break_instruction* updates
                
                # if break_instruction is starting this frame...
                if break_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    break_instruction.frameNStart = frameN  # exact frame index
                    break_instruction.tStart = t  # local t and not account for scr refresh
                    break_instruction.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(break_instruction, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'break_instruction.started')
                    # update status
                    break_instruction.status = STARTED
                    break_instruction.setAutoDraw(True)
                
                # if break_instruction is active this frame...
                if break_instruction.status == STARTED:
                    # update params
                    pass
                
                # if break_instruction is stopping this frame...
                if break_instruction.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > break_instruction.tStartRefresh + break_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        break_instruction.tStop = t  # not accounting for scr refresh
                        break_instruction.tStopRefresh = tThisFlipGlobal  # on global time
                        break_instruction.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'break_instruction.stopped')
                        # update status
                        break_instruction.status = FINISHED
                        break_instruction.setAutoDraw(False)
                # Run 'Each Frame' code from trigger_long_break_start
                # break start
                break_start_trig = trigger_dict["task_break_begin"]
                if frameN == 0:
                    send_trigger(break_start_trig)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=retr_task_break,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    retr_task_break.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in retr_task_break.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "retr_task_break" ---
            for thisComponent in retr_task_break.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for retr_task_break
            retr_task_break.tStop = globalClock.getTime(format='float')
            retr_task_break.tStopRefresh = tThisFlipGlobal
            thisExp.addData('retr_task_break.stopped', retr_task_break.tStop)
            # Run 'End Routine' code from bids_longbreak_logging
            # log offset at last frame of routine
                
            bids.mark_offset(break_instruction)
            
            # Run 'End Routine' code from trigger_long_break_start
            # send trigger for end break
            break_end_trig = trigger_dict["task_break_end"]
            if run_break and not end_trig_send:
                send_trigger(break_end_trig)
                end_trig_send = True
                core.wait(0.01) # wait so no overlap with next img trigger
            
            # the Routine "retr_task_break" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "instructions_new_learn" ---
            # create an object to store info about Routine instructions_new_learn
            instructions_new_learn = data.Routine(
                name='instructions_new_learn',
                components=[instruction_text_newroute],
            )
            instructions_new_learn.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # Run 'Begin Routine' code from control_routine
            #if miniblocks.thisN == n_learn_rout * 3 - 1:
                #continueRoutine = False 
            # Run 'Begin Routine' code from set_instruction_newroute
            
            if language == "french":
                instruction_text_newroute.text = ("Vous allez maintenant réapprendre les associations entre les images.")
            if language == "english":
                instruction_text_newroute.text = ("The learning of associations will continue now.")
            if language == "german": 
                instruction_text_newroute.text = ("Jetzt geht das Assoziationslernen weiter.")
            # store start times for instructions_new_learn
            instructions_new_learn.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            instructions_new_learn.tStart = globalClock.getTime(format='float')
            instructions_new_learn.status = STARTED
            thisExp.addData('instructions_new_learn.started', instructions_new_learn.tStart)
            instructions_new_learn.maxDuration = None
            # keep track of which components have finished
            instructions_new_learnComponents = instructions_new_learn.components
            for thisComponent in instructions_new_learn.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "instructions_new_learn" ---
            instructions_new_learn.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine:
                # if trial has changed, end Routine now
                if hasattr(thisMiniblock, 'status') and thisMiniblock.status == STOPPING:
                    continueRoutine = False
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *instruction_text_newroute* updates
                
                # if instruction_text_newroute is starting this frame...
                if instruction_text_newroute.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_text_newroute.frameNStart = frameN  # exact frame index
                    instruction_text_newroute.tStart = t  # local t and not account for scr refresh
                    instruction_text_newroute.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_text_newroute, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_text_newroute.started')
                    # update status
                    instruction_text_newroute.status = STARTED
                    instruction_text_newroute.setAutoDraw(True)
                
                # if instruction_text_newroute is active this frame...
                if instruction_text_newroute.status == STARTED:
                    # update params
                    pass
                
                # if instruction_text_newroute is stopping this frame...
                if instruction_text_newroute.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > instruction_text_newroute.tStartRefresh + instr_newroute_dur-frameTolerance:
                        # keep track of stop time/frame for later
                        instruction_text_newroute.tStop = t  # not accounting for scr refresh
                        instruction_text_newroute.tStopRefresh = tThisFlipGlobal  # on global time
                        instruction_text_newroute.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instruction_text_newroute.stopped')
                        # update status
                        instruction_text_newroute.status = FINISHED
                        instruction_text_newroute.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer, globalClock], 
                        currentRoutine=instructions_new_learn,
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    instructions_new_learn.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in instructions_new_learn.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "instructions_new_learn" ---
            for thisComponent in instructions_new_learn.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for instructions_new_learn
            instructions_new_learn.tStop = globalClock.getTime(format='float')
            instructions_new_learn.tStopRefresh = tThisFlipGlobal
            thisExp.addData('instructions_new_learn.stopped', instructions_new_learn.tStop)
            # the Routine "instructions_new_learn" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            # mark thisMiniblock as finished
            if hasattr(thisMiniblock, 'status'):
                thisMiniblock.status = FINISHED
            # if awaiting a pause, pause now
            if miniblocks.status == PAUSED:
                thisExp.status = PAUSED
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[globalClock], 
                )
                # once done pausing, restore running status
                miniblocks.status = STARTED
        # completed n_routes_block repeats of 'miniblocks'
        miniblocks.status = FINISHED
        
        # mark thisBlock as finished
        if hasattr(thisBlock, 'status'):
            thisBlock.status = FINISHED
        # if awaiting a pause, pause now
        if Block.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            Block.status = STARTED
    # completed 1.0 repeats of 'Block'
    Block.status = FINISHED
    
    
    # --- Prepare to start Routine "instructions_end" ---
    # create an object to store info about Routine instructions_end
    instructions_end = data.Routine(
        name='instructions_end',
        components=[instructions_end_text, continue_button_2],
    )
    instructions_end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from set_trigger_end
    trigNum = trigger_dict["start/end"]
    # Run 'Begin Routine' code from set_instructions_end_text
    if language == "english":
        instructions_end_text.text = ("The task is almost over now.\n To finish, you are going to have to answer 3 questionnaires. "
        "This will only take 5 minutes.\n\n"
        "You will be redirected to a new browser window, so please accept that the current window will be closed.\n"
        "When the questionnaires are over, you can just close the browser window.\n\n"
        "Please press the RETURN key to continue.")
    if language == "german":
        instructions_end_text.text = ("Die Aufgabe ist nun fast vorbei.\n"
        "Zum Abschluss bitten wir Sie, noch 3 weitere Fragebögen zu beantworten. "
        "Dies dauert nur 5 Minuten.\n\n"
        "Dafür müssen sie warten, bis die Daten hochgeladen sind. Sobald 'thank you for your patience' erscheint, klicken Sie auf 'okay'.\n"
        "Dann werden Sie weitergeleitet. Schließen Sie das Browser-Fenster nicht!\n\n"
        "Bitte drücken Sie die EINGABETASTE, um weiterzukommen. ")
    # create starting attributes for continue_button_2
    continue_button_2.keys = []
    continue_button_2.rt = []
    _continue_button_2_allKeys = []
    # store start times for instructions_end
    instructions_end.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_end.tStart = globalClock.getTime(format='float')
    instructions_end.status = STARTED
    thisExp.addData('instructions_end.started', instructions_end.tStart)
    instructions_end.maxDuration = None
    # keep track of which components have finished
    instructions_endComponents = instructions_end.components
    for thisComponent in instructions_end.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions_end" ---
    instructions_end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from set_trigger_end
        if frameN == 0:
            send_trigger(trigNum)
        
        
        # *instructions_end_text* updates
        
        # if instructions_end_text is starting this frame...
        if instructions_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_end_text.frameNStart = frameN  # exact frame index
            instructions_end_text.tStart = t  # local t and not account for scr refresh
            instructions_end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_end_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_end_text.started')
            # update status
            instructions_end_text.status = STARTED
            instructions_end_text.setAutoDraw(True)
        
        # if instructions_end_text is active this frame...
        if instructions_end_text.status == STARTED:
            # update params
            pass
        
        # if instructions_end_text is stopping this frame...
        if instructions_end_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > instructions_end_text.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                instructions_end_text.tStop = t  # not accounting for scr refresh
                instructions_end_text.tStopRefresh = tThisFlipGlobal  # on global time
                instructions_end_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instructions_end_text.stopped')
                # update status
                instructions_end_text.status = FINISHED
                instructions_end_text.setAutoDraw(False)
        
        # *continue_button_2* updates
        waitOnFlip = False
        
        # if continue_button_2 is starting this frame...
        if continue_button_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            continue_button_2.frameNStart = frameN  # exact frame index
            continue_button_2.tStart = t  # local t and not account for scr refresh
            continue_button_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_2.started')
            # update status
            continue_button_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if continue_button_2 is stopping this frame...
        if continue_button_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > continue_button_2.tStartRefresh + max_read_dur-frameTolerance:
                # keep track of stop time/frame for later
                continue_button_2.tStop = t  # not accounting for scr refresh
                continue_button_2.tStopRefresh = tThisFlipGlobal  # on global time
                continue_button_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_2.stopped')
                # update status
                continue_button_2.status = FINISHED
                continue_button_2.status = FINISHED
        if continue_button_2.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_2.getKeys(keyList=[left_key, right_key, center_key, down_key], ignoreKeys=["escape"], waitRelease=False)
            _continue_button_2_allKeys.extend(theseKeys)
            if len(_continue_button_2_allKeys):
                continue_button_2.keys = _continue_button_2_allKeys[0].name  # just the first key pressed
                continue_button_2.rt = _continue_button_2_allKeys[0].rt
                continue_button_2.duration = _continue_button_2_allKeys[0].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer, globalClock], 
                currentRoutine=instructions_end,
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            instructions_end.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_end.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_end" ---
    for thisComponent in instructions_end.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_end
    instructions_end.tStop = globalClock.getTime(format='float')
    instructions_end.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_end.stopped', instructions_end.tStop)
    # check responses
    if continue_button_2.keys in ['', [], None]:  # No response was made
        continue_button_2.keys = None
    thisExp.addData('continue_button_2.keys',continue_button_2.keys)
    if continue_button_2.keys != None:  # we had a response
        thisExp.addData('continue_button_2.rt', continue_button_2.rt)
        thisExp.addData('continue_button_2.duration', continue_button_2.duration)
    thisExp.nextEntry()
    # the Routine "instructions_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='tab')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # run any 'at exit' functions
    for fcn in runAtExit:
        fcn()
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
