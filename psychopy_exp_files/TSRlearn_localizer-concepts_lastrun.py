#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2025.2.4),
    on July 23, 2026, at 10:59
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2025')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
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

# Run 'Before Experiment' code from exp_settings

## all important task parameters to set ##

# response prompt positions
possible_prompt_positions = [-0.1, 0.1] # x coordinates

# duration of image presentation  [s]
image_dur = 0.75

# time to make response [s] 
response_time = 1.5

# is there feedback or not
fdback = 1 # [0 = no, 1 = yes]

# feedback duration [s]
fdback_dur = 0.2
 
# duration of rest breaks [s]
break_dur = 15

# interval of the breaks (every x trials)
break_interval = 50
total_block_number = 10 # how many blocks in total

# response - key mapping
left_key = 'g'
right_key = 'b'
center_key = 'r'
down_key = 'y'
nonmatch_key = center_key

possible_keys = [left_key, right_key, center_key, down_key]

# language for instruction
language = 'english' # 'english', 'french' or 'german' 

# match /non-match responses or just non-match
match_responses = 0 # [no "match" responses = 0, match and nonmatch responses = 1]

font_name = "Sans Sherif"
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2025.2.4'
expName = 'TSRlearn_localizer-concepts'  # from the Builder filename that created this script
expVersion = ''
# a list of functions to run when the experiment ends (starts off blank)
runAtExit = []
# information about this experiment
expInfo = {
    'participant': '0',
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
    # replace default participant ID
    if prefs.piloting['replaceParticipantID']:
        expInfo['participant'] = 'pilot'

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
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version=expVersion,
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\sync_folder\\TSRlearn-task\\psychopy_exp_files\\TSRlearn_localizer-concepts_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='alphabetical'
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
        logging.console.setLevel('exp')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('exp')
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
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0.0000, 0.0000, 0.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0.0000, 0.0000, 0.0000]
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
    # update experiment info
    expInfo['date'] = data.getDateStr()
    expInfo['expName'] = expName
    expInfo['expVersion'] = expVersion
    expInfo['psychopyVersion'] = psychopyVersion
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
    
    # --- Initialize components for Routine "settings" ---
    # Run 'Begin Experiment' code from functions_imports
    
    # log function that saves variables to log file
    def log(*msgs, sep=' ', end='\n'):
        log_file = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'] + '_print.log')
        print(*msgs, sep=sep, end=end, flush=True)
    
        # Append to log file
        with open(log_file, 'a') as f:
            f.write(sep.join(str(msg) for msg in msgs) + end)
    
    
    import meg_triggers
    from meg_triggers import send_trigger
    meg_triggers.set_default_duration(0.005)
    meg_triggers.set_default_reset_value(0)  # set the value the trigger channel returns to for neutral state
    # meg_triggers.enable_printing()     
    # Run 'Begin Experiment' code from exp_settings
    
    
    
    # Run 'Begin Experiment' code from bids_logging_functions
    # --- BIDS event logger (no Builder BIDS components needed) ---
    from pathlib import Path
    import csv
    import numpy as np
    import atexit
    
    class BIDSLogger:
        def __init__(self, win, clock, default_cols=None):
            self.win = win
            self.clock = clock
            self.rows = []          # list of dicts -> will become events.tsv
            self.active = {}        # stim -> row index (for duration)
            self.defaults = default_cols or {}
    
            # fixed column order (add any you want to see in the TSV)
            self.col_order = [
                "subject", "block_num", "trial_num",
                "component_label", "onset", "duration",
                "type_of_stimulus", "concept_label",
                "concept_examplar",
                "response_time", "response",
                "expected_response", "wrd_img_match",
                "correct"
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
        def add_instant(self, trial_type, **extra_cols):
            row = {"onset": float(self.clock.getTime()), "duration": 0.0,
                   "type_of_stimulus": trial_type}
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
    # Run 'Begin Experiment' code from set_trigger_numbers
    
    # define which trigger numbers to send
    trigger_numbers_dict = {
    "start/end": 255,
    "word presentation": 99,
    "response (button press)": 127,
    "feedback": 96,
    "fixation cross ITI": 94,
    "break_start": 81, 
    "break_end": 82
    }
    # Run 'Begin Experiment' code from set_sound_library
    import importlib.metadata as im
    
    if im.entry_points.__code__.co_argcount == 0:  # entry_points() takes no args
        _orig_entry_points = im.entry_points
    
        def _entry_points(*args, **kwargs):
            # PsychoPy calls: entry_points(group="psychopy.sound.backends")
            group = kwargs.get("group", None)
            eps = _orig_entry_points()
    
            # Old API may return dict-like: {'groupname': [EntryPoint,...], ...}
            if isinstance(eps, dict):
                return eps.get(group, []) if group else eps
    
            # If it returns a list, we can filter by .group if present
            if group:
                return [ep for ep in eps if getattr(ep, "group", None) == group]
            return eps
    
        im.entry_points = _entry_points
    
    
    
    # Run 'Begin Experiment' code from set_cond_file
    # zero-pad participant number for 0–9
    p_num = int(expInfo['participant'])
    conditions_file = f"sequences/localizer_conditions_{p_num:02d}_old.xlsx"
    
    # --- Initialize components for Routine "instructions" ---
    instruction_part1 = visual.TextStim(win=win, name='instruction_part1',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_part1_text
    
    
    continue_button = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions_02" ---
    instruction_part2 = visual.TextStim(win=win, name='instruction_part2',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_part2_text
    
    
    continue_button_3 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions_03" ---
    instruction_part3 = visual.TextStim(win=win, name='instruction_part3',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_part3_text
    
    
    continue_button_4 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions_04" ---
    instruction_part4 = visual.TextStim(win=win, name='instruction_part4',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_part4_text
    
    
    continue_button_9 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "image_pres_prc" ---
    image_prc = visual.ImageStim(
        win=win,
        name='image_prc', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    
    # --- Initialize components for Routine "sound_pres_prc" ---
    # set audio backend
    sound.Sound.backend = 'ptb'
    spoken_word_prc = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='spoken_word_prc'
    )
    spoken_word_prc.setVolume(1.0)
    fix_cross_prc = visual.TextStim(win=win, name='fix_cross_prc',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    key_resp_prc = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI_prc" ---
    fix_cross_2_prc = visual.TextStim(win=win, name='fix_cross_2_prc',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "instructions_startexp" ---
    instruction_startexp = visual.TextStim(win=win, name='instruction_startexp',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_startexp_text
    
    
    continue_button_6 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "instructions_startexp_02" ---
    instruction_startexp_2 = visual.TextStim(win=win, name='instruction_startexp_2',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    # Run 'Begin Experiment' code from instruction_startexp_text_2
    
    
    continue_button_8 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "image_pres" ---
    # Run 'Begin Experiment' code from set_trigger_image
    
    
    image = visual.ImageStim(
        win=win,
        name='image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "sound_pres" ---
    spoken_word = sound.Sound(
        'A', 
        secs=-1, 
        stereo=True, 
        hamming=True, 
        speaker=None,    name='spoken_word'
    )
    spoken_word.setVolume(1.0)
    fix_cross = visual.TextStim(win=win, name='fix_cross',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp = keyboard.Keyboard(deviceName='defaultKeyboard')
    
    # --- Initialize components for Routine "ITI" ---
    fix_cross_2 = visual.TextStim(win=win, name='fix_cross_2',
        text='+',
        font=font_name,
        pos=(0, 0), draggable=False, height=0.03, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "break_3" ---
    breaks_instruction = visual.TextStim(win=win, name='breaks_instruction',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    progress_bar_breaks = visual.Progress(
        win, name='progress_bar_breaks',
        progress=0.0,
        pos=(-0.2, -0.05), size=(0.4, 0.015), anchor='center-left', units='height',
        barColor='white', backColor=None, borderColor='white', colorSpace='rgb',
        lineWidth=4.0, opacity=1.0, ori=0.0,
        depth=-6
    )
    continue_button_break = keyboard.Keyboard(deviceName='defaultKeyboard')
    instruction_continuebreak = visual.TextStim(win=win, name='instruction_continuebreak',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    
    # --- Initialize components for Routine "instructions_end" ---
    instruction_end = visual.TextStim(win=win, name='instruction_end',
        text=None,
        font=font_name,
        pos=(0, 0), draggable=False, height=0.02, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    # Run 'Begin Experiment' code from instruction_end_text
    
    
    continue_button_7 = keyboard.Keyboard(deviceName='defaultKeyboard')
    
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
    if eyetracker is not None:
        eyetracker.enableEventReporting()
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "settings" ---
    # create an object to store info about Routine settings
    settings = data.Routine(
        name='settings',
        components=[],
    )
    settings.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from bids_logging_functions
    # ---- Create the logger once ----
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
    
    # Run 'Begin Routine' code from set_trigger_startexp
    
    send_trigger(value=trigger_numbers_dict["start/end"])
    # store start times for settings
    settings.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    settings.tStart = globalClock.getTime(format='float')
    settings.status = STARTED
    thisExp.addData('settings.started', settings.tStart)
    settings.maxDuration = None
    # keep track of which components have finished
    settingsComponents = settings.components
    for thisComponent in settings.components:
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
    
    # --- Run Routine "settings" ---
    thisExp.currentRoutine = settings
    settings.forceEnded = routineForceEnded = not continueRoutine
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
                currentRoutine=settings,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            settings.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if settings.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in settings.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "settings" ---
    for thisComponent in settings.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for settings
    settings.tStop = globalClock.getTime(format='float')
    settings.tStopRefresh = tThisFlipGlobal
    thisExp.addData('settings.stopped', settings.tStop)
    thisExp.nextEntry()
    # the Routine "settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions" ---
    # create an object to store info about Routine instructions
    instructions = data.Routine(
        name='instructions',
        components=[instruction_part1, continue_button],
    )
    instructions.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part1_text
    if language == "english": 
        instruction_part1.text = (
       "Welcome to the first part of the experiment.\n"
        "In this part, you will see different images\n"
        "and hear words.\n"
        "Your task is to decide if the words describe\n"
        "what you see in the images.\n\n"
        "[Press any key to continue.]"
    )
       
    if language == "german": 
        instruction_part1.text = (
        "Willkommen zum ersten Teil des Experiments.\n"
        "In diesem Teil sehen Sie verschiedene Bilder\n"
        "und hören Wörter.\n"
        "Ihre Aufgabe ist es zu entscheiden, ob die Wörter\n"
        "die Dinge beschreiben, die Sie auf den Bildern sehen.\n\n"
        "[Drücken Sie eine beliebige Taste, um fortzufahren.]"
    )
    
    if language == "french": 
        instruction_part1.text = (
    "Bienvenue dans la première partie de l'expérience. "
    "Dans cette partie, vous verrez différentes images et entendrez des mots. "
    "Votre tâche consiste à déterminer "
    "si les mots décrivent ce que vous voyez dans les images.\n"
    " [Appuyez sur la touche Entrée pour continuer.] "
    )
    # create starting attributes for continue_button
    continue_button.keys = []
    continue_button.rt = []
    _continue_button_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
    # store start times for instructions
    instructions.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions.tStart = globalClock.getTime(format='float')
    instructions.status = STARTED
    thisExp.addData('instructions.started', instructions.tStart)
    instructions.maxDuration = None
    # keep track of which components have finished
    instructionsComponents = instructions.components
    for thisComponent in instructions.components:
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
    
    # --- Run Routine "instructions" ---
    thisExp.currentRoutine = instructions
    instructions.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_01
        ## schedule bids trigger setting
        
        bids.schedule_onset(instruction_part1,
                                type_of_stimulus="instructions",
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
        
        # *continue_button* updates
        waitOnFlip = False
        
        # if continue_button is starting this frame...
        if continue_button.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button.frameNStart = frameN  # exact frame index
            continue_button.tStart = t  # local t and not account for scr refresh
            continue_button.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button.started')
            # update status
            continue_button.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button.status == STARTED and not waitOnFlip:
            theseKeys = continue_button.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_allKeys.extend(theseKeys)
            if len(_continue_button_allKeys):
                continue_button.keys = _continue_button_allKeys[-1].name  # just the last key pressed
                continue_button.rt = _continue_button_allKeys[-1].rt
                continue_button.duration = _continue_button_allKeys[-1].duration
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
                currentRoutine=instructions,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructions.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions
    instructions.tStop = globalClock.getTime(format='float')
    instructions.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions.stopped', instructions.tStop)
    # Run 'End Routine' code from bids_instruc_01
    # log offset at last frame of routine
    
    bids.mark_offset(instruction_part1)
    
    # check responses
    if continue_button.keys in ['', [], None]:  # No response was made
        continue_button.keys = None
    thisExp.addData('continue_button.keys',continue_button.keys)
    if continue_button.keys != None:  # we had a response
        thisExp.addData('continue_button.rt', continue_button.rt)
        thisExp.addData('continue_button.duration', continue_button.duration)
    thisExp.nextEntry()
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
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
    "You will first see an image.\n"
    "Then you will hear a spoken word.\n"
    "Decide whether the word matches the image or not.\n\n"
    "[Press any key to continue.]"
    )
       
    if language == "german": 
        instruction_part2.text = (
       "Sie sehen zuerst ein Bild.\n"
       "Danach hören Sie ein gesprochenes Wort.\n"
    "Entscheiden Sie, ob das Wort zu dem Bild passt oder nicht.\n\n"
    "[Drücken Sie eine beliebige Taste, um fortzufahren.]"
    )
    
    if language == "french": 
        instruction_part2.text = (
    "Après chaque image, vous entendrez un mot. Lorsque "
    "le mot apparaît, vous êtes invité à réfléchir si le "
    "mot correspond à l'objet que vous avez vu dans l'image "
    "précédente ou non. \n "
    "[Appuyez sur la touche Entrée pour continuer.] ")
    # create starting attributes for continue_button_3
    continue_button_3.keys = []
    continue_button_3.rt = []
    _continue_button_3_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
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
    thisExp.currentRoutine = instructions_02
    instructions_02.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_02
        # log onset at first frame
        #if frameN == 0:
            #bids.schedule_onset(instruction_part2,
                                #trial_type="localizer",
                                #stim_label="instruction_02")
        
        bids.schedule_onset(instruction_part2,
                                type_of_stimulus="instructions",
                                component_label="instruction_part2")
        
        
        # *instruction_part2* updates
        
        # if instruction_part2 is starting this frame...
        if instruction_part2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *continue_button_3* updates
        waitOnFlip = False
        
        # if continue_button_3 is starting this frame...
        if continue_button_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_3.frameNStart = frameN  # exact frame index
            continue_button_3.tStart = t  # local t and not account for scr refresh
            continue_button_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_3.started')
            # update status
            continue_button_3.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_3.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_3.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_3_allKeys.extend(theseKeys)
            if len(_continue_button_3_allKeys):
                continue_button_3.keys = _continue_button_3_allKeys[-1].name  # just the last key pressed
                continue_button_3.rt = _continue_button_3_allKeys[-1].rt
                continue_button_3.duration = _continue_button_3_allKeys[-1].duration
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
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_02.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_02.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
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
    # Run 'End Routine' code from bids_instruc_02
    
    # log offset at last frame of routine
    #if not continueRoutine:  
        #bids.mark_offset(instruction_part2)
        
    bids.mark_offset(instruction_part2)
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
    "If the word does not match the image, please respond immediately.\n"
    "Press the upper key (red) if the word does not match\n"
    "the image you just saw.\n\n"
    "If the word matches the image, do not press any key.\n\n"
    "The fixation cross will briefly change color\n"
    "to show whether your response was correct.\n\n"
    "[Press any key to continue.]"
    )
       
    if language == "german": 
        instruction_part3.text = (
    "Wenn das Wort nicht zu dem Bild passt, reagieren Sie bitte sofort.\n"
    "Drücken Sie die obere Taste (rot), wenn das Wort\n"
    "nicht zu dem Bild passt, das Sie gerade gesehen haben.\n\n"
    "Wenn das Wort zu dem Bild passt, drücken Sie keine Taste.\n\n"
    "Das Fixationskreuz verändert kurz seine Farbe,\n"
    "um anzuzeigen, ob Ihre Antwort richtig war.\n\n"
    "[Drücken Sie eine beliebige Taste, um fortzufahren.]"
    )
    
    if language == "french": 
        instruction_part3.text = (
    "Si l'image et le mot ne correspondent pas, vous devez réagir immédiatement. "
    "Appuyez sur la flèche droite si le mot ne correspond pas à l'image précédente. S'ils correspondent, vous n'avez rien à faire. "
    "La croix de fixation changera rapidement de couleur pour vous indiquer si vous avez bien réagi.\n"
    "[Appuyez sur Entrée pour continuer.] "
    )
    
    # create starting attributes for continue_button_4
    continue_button_4.keys = []
    continue_button_4.rt = []
    _continue_button_4_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
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
    thisExp.currentRoutine = instructions_03
    instructions_03.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_03
        ## schedule bids trigger setting
        # log onset at first frame
        #if frameN == 0:
            #bids.schedule_onset(instruction_part3,
                                #trial_type="localizer",
                                #stim_label="instruction_03")
        
        
        bids.schedule_onset(instruction_part3,
                                type_of_stimulus="instructions",
                                component_label="instruction_part3")
        
        
        # *instruction_part3* updates
        
        # if instruction_part3 is starting this frame...
        if instruction_part3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        
        # *continue_button_4* updates
        waitOnFlip = False
        
        # if continue_button_4 is starting this frame...
        if continue_button_4.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_4.frameNStart = frameN  # exact frame index
            continue_button_4.tStart = t  # local t and not account for scr refresh
            continue_button_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_4.started')
            # update status
            continue_button_4.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_4.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_4.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_4_allKeys.extend(theseKeys)
            if len(_continue_button_4_allKeys):
                continue_button_4.keys = _continue_button_4_allKeys[-1].name  # just the last key pressed
                continue_button_4.rt = _continue_button_4_allKeys[-1].rt
                continue_button_4.duration = _continue_button_4_allKeys[-1].duration
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
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_03.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_03.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
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
    # Run 'End Routine' code from bids_instruc_03
    
    # log offset at last frame of routine
    #if not continueRoutine:  
        #bids.mark_offset(instruction_part3)
    bids.mark_offset(instruction_part3)
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
        components=[instruction_part4, continue_button_9],
    )
    instructions_04.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_part4_text
    if language == "english": 
        instruction_part4.text = (
    "Please respond as quickly and accurately as possible.\n"
    "We’ll start with some practice trials.\n"
    "Use the upper key (red) for mismatches.\n\n"
    "[Press any key to continue.] "
    )
       
    if language == "german": 
        instruction_part4.text = (
    "Bitte antworten Sie so schnell und genau wie möglich.\n"
    "Wir beginnen nun mit einigen Übungsdurchgängen.\n"
    "Nutzen Sie die obere Taste (rot) für Nicht-Übereinstimmungen.\n\n"
    "[Drücken Sie eine beliebige Taste, um fortzufahren.]"
    )
    
    if language == "french": 
        instruction_part4.text = (
    "Veuillez répondre aussi rapidement et précisément que possible. "
    "Nous allons commencer par quelques essais. "
    "Utilisez la flèche droite pour les non-correspondances. \n"
    "[Appuyez sur la touche Entrée pour continuer.] "
    )
    # create starting attributes for continue_button_9
    continue_button_9.keys = []
    continue_button_9.rt = []
    _continue_button_9_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
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
    thisExp.currentRoutine = instructions_04
    instructions_04.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_04
        ## schedule bids trigger setting
        # log onset at first frame
        #if frameN == 0:
            #bids.schedule_onset(instruction_part3,
                                #trial_type="localizer",
                                #stim_label="instruction_03")
        
        
        bids.schedule_onset(instruction_part4,
                                type_of_stimulus="instructions",
                                component_label="instruction_part4")
        
        
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
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_9.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_9.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_9_allKeys.extend(theseKeys)
            if len(_continue_button_9_allKeys):
                continue_button_9.keys = _continue_button_9_allKeys[-1].name  # just the last key pressed
                continue_button_9.rt = _continue_button_9_allKeys[-1].rt
                continue_button_9.duration = _continue_button_9_allKeys[-1].duration
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
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_04.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_04.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
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
    # Run 'End Routine' code from bids_instruc_04
    
    # log offset at last frame of routine
    #if not continueRoutine:  
        #bids.mark_offset(instruction_part3)
    bids.mark_offset(instruction_part4)
    # check responses
    if continue_button_9.keys in ['', [], None]:  # No response was made
        continue_button_9.keys = None
    thisExp.addData('continue_button_9.keys',continue_button_9.keys)
    if continue_button_9.keys != None:  # we had a response
        thisExp.addData('continue_button_9.rt', continue_button_9.rt)
        thisExp.addData('continue_button_9.duration', continue_button_9.duration)
    thisExp.nextEntry()
    # the Routine "instructions_04" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_practice = data.TrialHandler2(
        name='trials_practice',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('sequences/localiser_trials_prc.xlsx'), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials_practice)  # add the loop to the experiment
    thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            globals()[paramName] = thisTrials_practice[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrials_practice in trials_practice:
        trials_practice.status = STARTED
        if hasattr(thisTrials_practice, 'status'):
            thisTrials_practice.status = STARTED
        currentLoop = trials_practice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
        if thisTrials_practice != None:
            for paramName in thisTrials_practice:
                globals()[paramName] = thisTrials_practice[paramName]
        
        # --- Prepare to start Routine "image_pres_prc" ---
        # create an object to store info about Routine image_pres_prc
        image_pres_prc = data.Routine(
            name='image_pres_prc',
            components=[image_prc],
        )
        image_pres_prc.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        image_prc.setImage( "stimuli\\practice_images\\" + image_shown)
        # store start times for image_pres_prc
        image_pres_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        image_pres_prc.tStart = globalClock.getTime(format='float')
        image_pres_prc.status = STARTED
        thisExp.addData('image_pres_prc.started', image_pres_prc.tStart)
        image_pres_prc.maxDuration = None
        # keep track of which components have finished
        image_pres_prcComponents = image_pres_prc.components
        for thisComponent in image_pres_prc.components:
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
        
        # --- Run Routine "image_pres_prc" ---
        thisExp.currentRoutine = image_pres_prc
        image_pres_prc.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_practice, 'status') and thisTrials_practice.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_prc* updates
            
            # if image_prc is starting this frame...
            if image_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_prc.frameNStart = frameN  # exact frame index
                image_prc.tStart = t  # local t and not account for scr refresh
                image_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image_prc.started')
                # update status
                image_prc.status = STARTED
                image_prc.setAutoDraw(True)
            
            # if image_prc is active this frame...
            if image_prc.status == STARTED:
                # update params
                pass
            
            # if image_prc is stopping this frame...
            if image_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_prc.tStartRefresh + image_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    image_prc.tStop = t  # not accounting for scr refresh
                    image_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    image_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_prc.stopped')
                    # update status
                    image_prc.status = FINISHED
                    image_prc.setAutoDraw(False)
            
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
                    currentRoutine=image_pres_prc,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                image_pres_prc.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if image_pres_prc.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in image_pres_prc.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_pres_prc" ---
        for thisComponent in image_pres_prc.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for image_pres_prc
        image_pres_prc.tStop = globalClock.getTime(format='float')
        image_pres_prc.tStopRefresh = tThisFlipGlobal
        thisExp.addData('image_pres_prc.stopped', image_pres_prc.tStop)
        # the Routine "image_pres_prc" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "sound_pres_prc" ---
        # create an object to store info about Routine sound_pres_prc
        sound_pres_prc = data.Routine(
            name='sound_pres_prc',
            components=[spoken_word_prc, fix_cross_prc, key_resp_prc],
        )
        sound_pres_prc.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from set_word_prc
        
        
        if language == 'english':
            part1 = (word_shown_english)
            part2 = "_en"
            word_shown = part1 + part2
        
            
        elif language == 'german':     
            part1 = word_shown_german
            part2 = "_german"
            word_shown = (part1 + part2)
        
        elif language == 'french':   
            part1 = (word_shown_french)
            part2 = "_fr"
            word_shown = part1 + part2
        spoken_word_prc.setSound( "sounds//" + word_shown + ".mp3", hamming=True)
        spoken_word_prc.setVolume(1.0, log=False)
        spoken_word_prc.seek(0)
        fix_cross_prc.setColor('white', colorSpace='rgb')
        # Run 'Begin Routine' code from allowed_keys_prc
        
        if match_responses == 0:
            allowed_key_list = [nonmatch_key]  # list of allowed keys
        else:
            # default: allow both match and nonmatch responses
            allowed_key_list = [match_key, nonmatch_key]
        # create starting attributes for key_resp_prc
        key_resp_prc.keys = []
        key_resp_prc.rt = []
        _key_resp_prc_allKeys = []
        # Run 'Begin Routine' code from code_key_resp_prc
        
        # reset key resp and correct answer
        key_resp_prc.keys = None
        key_resp_prc.corr = None 
        
        
        
        
        # Run 'Begin Routine' code from feedback_control_2
        
        # prepare feedback in form of word color change or too slow message
        feedback_given = False
        show_until = None
        # store start times for sound_pres_prc
        sound_pres_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        sound_pres_prc.tStart = globalClock.getTime(format='float')
        sound_pres_prc.status = STARTED
        thisExp.addData('sound_pres_prc.started', sound_pres_prc.tStart)
        sound_pres_prc.maxDuration = None
        # keep track of which components have finished
        sound_pres_prcComponents = sound_pres_prc.components
        for thisComponent in sound_pres_prc.components:
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
        
        # --- Run Routine "sound_pres_prc" ---
        thisExp.currentRoutine = sound_pres_prc
        sound_pres_prc.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_practice, 'status') and thisTrials_practice.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *spoken_word_prc* updates
            
            # if spoken_word_prc is starting this frame...
            if spoken_word_prc.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                spoken_word_prc.frameNStart = frameN  # exact frame index
                spoken_word_prc.tStart = t  # local t and not account for scr refresh
                spoken_word_prc.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('spoken_word_prc.started', tThisFlipGlobal)
                # update status
                spoken_word_prc.status = STARTED
                spoken_word_prc.play(when=win)  # sync with win flip
            
            # if spoken_word_prc is stopping this frame...
            if spoken_word_prc.status == STARTED:
                if bool(False) or spoken_word_prc.isFinished:
                    # keep track of stop time/frame for later
                    spoken_word_prc.tStop = t  # not accounting for scr refresh
                    spoken_word_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    spoken_word_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'spoken_word_prc.stopped')
                    # update status
                    spoken_word_prc.status = FINISHED
                    spoken_word_prc.stop()
            
            # *fix_cross_prc* updates
            
            # if fix_cross_prc is starting this frame...
            if fix_cross_prc.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_prc.frameNStart = frameN  # exact frame index
                fix_cross_prc.tStart = t  # local t and not account for scr refresh
                fix_cross_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_prc.started')
                # update status
                fix_cross_prc.status = STARTED
                fix_cross_prc.setAutoDraw(True)
            
            # if fix_cross_prc is active this frame...
            if fix_cross_prc.status == STARTED:
                # update params
                pass
            
            # *key_resp_prc* updates
            waitOnFlip = False
            
            # if key_resp_prc is starting this frame...
            if key_resp_prc.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_prc.frameNStart = frameN  # exact frame index
                key_resp_prc.tStart = t  # local t and not account for scr refresh
                key_resp_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_prc.started')
                # update status
                key_resp_prc.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_prc.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_prc.clearEvents, eventType='keyboard')  # clear events on next screen flip
            
            # if key_resp_prc is stopping this frame...
            if key_resp_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_prc.tStartRefresh + response_time-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_prc.tStop = t  # not accounting for scr refresh
                    key_resp_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    key_resp_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_prc.stopped')
                    # update status
                    key_resp_prc.status = FINISHED
                    key_resp_prc.status = FINISHED
            if key_resp_prc.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_prc.getKeys(keyList=[nonmatch_key], ignoreKeys=["escape"], waitRelease=True)
                _key_resp_prc_allKeys.extend(theseKeys)
                if len(_key_resp_prc_allKeys):
                    key_resp_prc.keys = _key_resp_prc_allKeys[0].name  # just the first key pressed
                    key_resp_prc.rt = _key_resp_prc_allKeys[0].rt
                    key_resp_prc.duration = _key_resp_prc_allKeys[0].duration
            # Run 'Each Frame' code from code_key_resp_prc
            if match_responses == 1: 
            
                if match_idx == 1:
                    answer_correct = match_key
                elif match_idx == 0:
                    answer_correct = nonmatch_key
                # Evaluate participant response
                if key_resp_prc.keys is None:
                    key_resp_prc.corr = "m"   # no response
                elif key_resp_prc.keys == answer_correct:
                    key_resp_prc.corr = 1      # correct response
                else:
                    key_resp_prc.corr = 0      # wrong key
                    
                
            if match_responses == 0: 
                
                if match_idx == 1:
                    answer_correct = None
                elif match_idx == 0:
                    answer_correct = nonmatch_key
            
                # Evaluate participant response  
                if key_resp_prc.keys == answer_correct:
                    key_resp_prc.corr = 1      # correct response
                else:
                    key_resp_prc.corr = 0      # wrong key
                    
                    
            # Run 'Each Frame' code from feedback_control_2
            
            if fdback == 1:
                if match_idx==0:  # Mismatch trial - button press required
                    if (not feedback_given):
                        # Case 1: Button was pressed before deadline
                        if (key_resp_prc.keys is not None):
                            if getattr(key_resp_prc, 'corr', None) == 1:
                                fix_cross_prc.setColor('green')
                            else:
                                fix_cross_prc.setColor('red')
                            feedback_given = True
                            feedback_end = t + 0.2
                        # Case 2: No response by deadline
                        elif (t >= response_time):
                            fix_cross_prc.setColor('red')  # No response on mismatch = incorrect
                            feedback_given = True
                            feedback_end = t + 0.2
                    
                    # feedback for 0.2s 
                    if feedback_given:
                        try:
                            if not fix_cross_prc.autoDraw:
                                fix_cross_prc.setAutoDraw(True)
                        except Exception:
                            pass
                        if t >= feedback_end:
                            continueRoutine = False
            
                elif match_idx==1: # no button should be pressed
                    
                    if (not feedback_given):
                        # Case 1: Button was pressed (incorrect on match trial)
                        if (key_resp_prc.keys is not None):
                            fix_cross_prc.setColor('red')
                            feedback_given = True
                            feedback_end = t + 0.2
                        # Case 2: No response by deadline (correct on match trial)
                        elif (t >= response_time):
                            fix_cross_prc.setColor('green')
                            feedback_given = True
                            feedback_end = t + 0.2
                    
                    # Hold feedback for 0.2s then end 
                    if feedback_given:
                        try:
                            if not fix_cross_prc.autoDraw:
                                fix_cross_prc.setAutoDraw(True)
                        except Exception:
                            pass
                        if t >= feedback_end:
                            continueRoutine = False
            
            else:
                # no feedback: end on response or timeout
                if (key_resp_prc.keys is not None) or (t >= response_time):
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
                    currentRoutine=sound_pres_prc,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                sound_pres_prc.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if sound_pres_prc.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in sound_pres_prc.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sound_pres_prc" ---
        for thisComponent in sound_pres_prc.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for sound_pres_prc
        sound_pres_prc.tStop = globalClock.getTime(format='float')
        sound_pres_prc.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sound_pres_prc.stopped', sound_pres_prc.tStop)
        spoken_word_prc.pause()  # ensure sound has stopped at end of Routine
        # check responses
        if key_resp_prc.keys in ['', [], None]:  # No response was made
            key_resp_prc.keys = None
        trials_practice.addData('key_resp_prc.keys',key_resp_prc.keys)
        if key_resp_prc.keys != None:  # we had a response
            trials_practice.addData('key_resp_prc.rt', key_resp_prc.rt)
            trials_practice.addData('key_resp_prc.duration', key_resp_prc.duration)
        # the Routine "sound_pres_prc" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI_prc" ---
        # create an object to store info about Routine ITI_prc
        ITI_prc = data.Routine(
            name='ITI_prc',
            components=[fix_cross_2_prc],
        )
        ITI_prc.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for ITI_prc
        ITI_prc.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI_prc.tStart = globalClock.getTime(format='float')
        ITI_prc.status = STARTED
        thisExp.addData('ITI_prc.started', ITI_prc.tStart)
        ITI_prc.maxDuration = None
        # keep track of which components have finished
        ITI_prcComponents = ITI_prc.components
        for thisComponent in ITI_prc.components:
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
        
        # --- Run Routine "ITI_prc" ---
        thisExp.currentRoutine = ITI_prc
        ITI_prc.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrials_practice, 'status') and thisTrials_practice.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_cross_2_prc* updates
            
            # if fix_cross_2_prc is starting this frame...
            if fix_cross_2_prc.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_2_prc.frameNStart = frameN  # exact frame index
                fix_cross_2_prc.tStart = t  # local t and not account for scr refresh
                fix_cross_2_prc.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_2_prc, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_2_prc.started')
                # update status
                fix_cross_2_prc.status = STARTED
                fix_cross_2_prc.setAutoDraw(True)
            
            # if fix_cross_2_prc is active this frame...
            if fix_cross_2_prc.status == STARTED:
                # update params
                pass
            
            # if fix_cross_2_prc is stopping this frame...
            if fix_cross_2_prc.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_2_prc.tStartRefresh + ITI_length-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_2_prc.tStop = t  # not accounting for scr refresh
                    fix_cross_2_prc.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_cross_2_prc.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_2_prc.stopped')
                    # update status
                    fix_cross_2_prc.status = FINISHED
                    fix_cross_2_prc.setAutoDraw(False)
            
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
                    currentRoutine=ITI_prc,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI_prc.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI_prc.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI_prc.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_prc" ---
        for thisComponent in ITI_prc.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI_prc
        ITI_prc.tStop = globalClock.getTime(format='float')
        ITI_prc.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI_prc.stopped', ITI_prc.tStop)
        # the Routine "ITI_prc" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrials_practice as finished
        if hasattr(thisTrials_practice, 'status'):
            thisTrials_practice.status = FINISHED
        # if awaiting a pause, pause now
        if trials_practice.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials_practice.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials_practice'
    trials_practice.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials_practice.trialList in ([], [None], None):
        params = []
    else:
        params = trials_practice.trialList[0].keys()
    # save data for this loop
    trials_practice.saveAsExcel(filename + '.xlsx', sheetName='trials_practice',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials_practice.saveAsText(filename + '_trials_practice.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "instructions_startexp" ---
    # create an object to store info about Routine instructions_startexp
    instructions_startexp = data.Routine(
        name='instructions_startexp',
        components=[instruction_startexp, continue_button_6],
    )
    instructions_startexp.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from bids_instruc_startexp
    ## schedule bids trigger setting
    # log onset at first frame
    #if frameN == 0:
        #bids.schedule_onset(instruction_startexp,
                            #trial_type="localizer",
                            #stim_label="instruction_startexp")
    
    
    
    # Run 'Begin Routine' code from instruction_startexp_text
    if language == "english": 
        instruction_startexp.text = (
    "You have completed all practice trials.\n"
    "The main task will now begin.\n"
    "Always press the upper key (red) when the word\n"
    "does not match the previous image.\n\n"
    "[Press any key to continue.]"
    )
       
    if language == "german": 
        instruction_startexp.text = (
    "Sie haben alle Übungsdurchgänge abgeschlossen.\n\n"
    "Die Hauptaufgabe beginnt jetzt.\n\n"
    "Drücken Sie immer die obere Taste (rot), wenn das Wort\n"
    "nicht zu dem vorherigen Bild passt.\n\n"
    "[Drücken Sie eine beliebige Taste, um weiterzumachen.]"
    )
    
    if language == "french": 
        instruction_startexp.text = (
    "Vous avez terminé tous les essais pratiques. La tâche principale va maintenant commencer. "
    "Appuyez toujours sur la flèche droite lorsque le mot ne correspond pas à l'image précédente. "
    "Il y aura des pauses régulières pendant lesquelles vous pourrez vous reposer un instant. \n"
    "[Appuyez sur la touche Entrée pour commencer la tâche principale.] "
    )
    # create starting attributes for continue_button_6
    continue_button_6.keys = []
    continue_button_6.rt = []
    _continue_button_6_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
    # store start times for instructions_startexp
    instructions_startexp.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_startexp.tStart = globalClock.getTime(format='float')
    instructions_startexp.status = STARTED
    thisExp.addData('instructions_startexp.started', instructions_startexp.tStart)
    instructions_startexp.maxDuration = None
    # keep track of which components have finished
    instructions_startexpComponents = instructions_startexp.components
    for thisComponent in instructions_startexp.components:
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
    
    # --- Run Routine "instructions_startexp" ---
    thisExp.currentRoutine = instructions_startexp
    instructions_startexp.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_startexp
        # log offset at last frame of routine
        #if not continueRoutine:  
            #bids.mark_offset(instruction_startexp)
        
        bids.schedule_onset(instruction_startexp,
                            type_of_stimulus="instructions",
                            component_label="instruction_start")
        
        
        # *instruction_startexp* updates
        
        # if instruction_startexp is starting this frame...
        if instruction_startexp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_startexp.frameNStart = frameN  # exact frame index
            instruction_startexp.tStart = t  # local t and not account for scr refresh
            instruction_startexp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_startexp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_startexp.started')
            # update status
            instruction_startexp.status = STARTED
            instruction_startexp.setAutoDraw(True)
        
        # if instruction_startexp is active this frame...
        if instruction_startexp.status == STARTED:
            # update params
            pass
        
        # *continue_button_6* updates
        waitOnFlip = False
        
        # if continue_button_6 is starting this frame...
        if continue_button_6.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_6.frameNStart = frameN  # exact frame index
            continue_button_6.tStart = t  # local t and not account for scr refresh
            continue_button_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_6.started')
            # update status
            continue_button_6.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_6.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_6.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_6_allKeys.extend(theseKeys)
            if len(_continue_button_6_allKeys):
                continue_button_6.keys = _continue_button_6_allKeys[-1].name  # just the last key pressed
                continue_button_6.rt = _continue_button_6_allKeys[-1].rt
                continue_button_6.duration = _continue_button_6_allKeys[-1].duration
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
                currentRoutine=instructions_startexp,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_startexp.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_startexp.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions_startexp.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_startexp" ---
    for thisComponent in instructions_startexp.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_startexp
    instructions_startexp.tStop = globalClock.getTime(format='float')
    instructions_startexp.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_startexp.stopped', instructions_startexp.tStop)
    # Run 'End Routine' code from bids_instruc_startexp
    bids.mark_offset(instruction_startexp)
    # check responses
    if continue_button_6.keys in ['', [], None]:  # No response was made
        continue_button_6.keys = None
    thisExp.addData('continue_button_6.keys',continue_button_6.keys)
    if continue_button_6.keys != None:  # we had a response
        thisExp.addData('continue_button_6.rt', continue_button_6.rt)
        thisExp.addData('continue_button_6.duration', continue_button_6.duration)
    thisExp.nextEntry()
    # the Routine "instructions_startexp" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_startexp_02" ---
    # create an object to store info about Routine instructions_startexp_02
    instructions_startexp_02 = data.Routine(
        name='instructions_startexp_02',
        components=[instruction_startexp_2, continue_button_8],
    )
    instructions_startexp_02.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from instruction_startexp_text_2
    if language == "english": 
        instruction_startexp_2.text = (
    "The MEG signal is very sensitive to eye and body\n"
    "movements. Please move and blink as little as possible\n"
    "during the task blocks.\n\n"
    "After each block, there will be a short break during\n"
    "which you can move and rest.\n\n"
    "As soon as the task begins again, please sit still again.\n\n"
    "[Press any key to start the main task.]"
    )
       
    if language == "german":
        instruction_startexp_2.text = (
            "Das MEG-Signal ist sehr empfindlich gegenüber\n"
            "Augen- und Körperbewegungen. Bitte bewegen und blinzeln Sie\n"
            "während der Aufgabenblöcke so wenig wie möglich.\n\n"
            "Nach jedem Block gibt es eine kurze Pause, in der Sie sich\n"
            "bewegen und ausruhen können.\n\n"
            "Sobald die Aufgabe wieder beginnt, sitzen Sie bitte wieder still.\n\n"
            "[Drücken Sie eine beliebige Taste, um die Hauptaufgabe zu starten.]"
        )
    
    
    
    if language == "french": 
        instruction_startexp.text = (
    "Vous avez terminé tous les essais pratiques. La tâche principale va maintenant commencer. "
    "Appuyez toujours sur la flèche droite lorsque le mot ne correspond pas à l'image précédente. "
    "Il y aura des pauses régulières pendant lesquelles vous pourrez vous reposer un instant. \n"
    "[Appuyez sur la touche Entrée pour commencer la tâche principale.] "
    )
    # create starting attributes for continue_button_8
    continue_button_8.keys = []
    continue_button_8.rt = []
    _continue_button_8_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
    # store start times for instructions_startexp_02
    instructions_startexp_02.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    instructions_startexp_02.tStart = globalClock.getTime(format='float')
    instructions_startexp_02.status = STARTED
    thisExp.addData('instructions_startexp_02.started', instructions_startexp_02.tStart)
    instructions_startexp_02.maxDuration = None
    # keep track of which components have finished
    instructions_startexp_02Components = instructions_startexp_02.components
    for thisComponent in instructions_startexp_02.components:
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
    
    # --- Run Routine "instructions_startexp_02" ---
    thisExp.currentRoutine = instructions_startexp_02
    instructions_startexp_02.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from bids_instruc_startexp_2
        
        
        bids.schedule_onset(instruction_startexp_2,
                            type_of_stimulus="instructions",
                            component_label="instruction_start_2")
        
        
        # *instruction_startexp_2* updates
        
        # if instruction_startexp_2 is starting this frame...
        if instruction_startexp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_startexp_2.frameNStart = frameN  # exact frame index
            instruction_startexp_2.tStart = t  # local t and not account for scr refresh
            instruction_startexp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_startexp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_startexp_2.started')
            # update status
            instruction_startexp_2.status = STARTED
            instruction_startexp_2.setAutoDraw(True)
        
        # if instruction_startexp_2 is active this frame...
        if instruction_startexp_2.status == STARTED:
            # update params
            pass
        
        # *continue_button_8* updates
        waitOnFlip = False
        
        # if continue_button_8 is starting this frame...
        if continue_button_8.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_8.frameNStart = frameN  # exact frame index
            continue_button_8.tStart = t  # local t and not account for scr refresh
            continue_button_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_8.started')
            # update status
            continue_button_8.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_8.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_8.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_8_allKeys.extend(theseKeys)
            if len(_continue_button_8_allKeys):
                continue_button_8.keys = _continue_button_8_allKeys[-1].name  # just the last key pressed
                continue_button_8.rt = _continue_button_8_allKeys[-1].rt
                continue_button_8.duration = _continue_button_8_allKeys[-1].duration
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
                currentRoutine=instructions_startexp_02,
            )
            # skip the frame we paused on
            continue
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_startexp_02.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_startexp_02.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
        for thisComponent in instructions_startexp_02.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_startexp_02" ---
    for thisComponent in instructions_startexp_02.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for instructions_startexp_02
    instructions_startexp_02.tStop = globalClock.getTime(format='float')
    instructions_startexp_02.tStopRefresh = tThisFlipGlobal
    thisExp.addData('instructions_startexp_02.stopped', instructions_startexp_02.tStop)
    # Run 'End Routine' code from bids_instruc_startexp_2
    bids.mark_offset(instruction_startexp)
    # check responses
    if continue_button_8.keys in ['', [], None]:  # No response was made
        continue_button_8.keys = None
    thisExp.addData('continue_button_8.keys',continue_button_8.keys)
    if continue_button_8.keys != None:  # we had a response
        thisExp.addData('continue_button_8.rt', continue_button_8.rt)
        thisExp.addData('continue_button_8.duration', continue_button_8.duration)
    thisExp.nextEntry()
    # the Routine "instructions_startexp_02" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions(conditions_file), 
        seed=None, 
        isTrials=True, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        trials.status = STARTED
        if hasattr(thisTrial, 'status'):
            thisTrial.status = STARTED
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "image_pres" ---
        # create an object to store info about Routine image_pres
        image_pres = data.Routine(
            name='image_pres',
            components=[image],
        )
        image_pres.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from compute_block_trial_num
        
        current_trial_number = trials.thisN + 1 # make it start at 1
        # block number should increase one trial AFTER a break_interval trial
        if current_trial_number == 1:
            block_num = 1
        elif (current_trial_number - 1) % break_interval == 0:
            block_num = int((current_trial_number - 1) / break_interval) + 1
        else:
            # otherwise keep previous value
            block_num = block_num
            
        trial_num = current_trial_number
        
        log("Block number: ", block_num)
        log("Trial number: ", trial_num)
        image.setImage( "stimuli\\" + image_shown)
        # store start times for image_pres
        image_pres.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        image_pres.tStart = globalClock.getTime(format='float')
        image_pres.status = STARTED
        thisExp.addData('image_pres.started', image_pres.tStart)
        image_pres.maxDuration = None
        # keep track of which components have finished
        image_presComponents = image_pres.components
        for thisComponent in image_pres.components:
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
        
        # --- Run Routine "image_pres" ---
        thisExp.currentRoutine = image_pres
        image_pres.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from set_trigger_image
            if frameN == 0: 
                send_trigger(concept_num)
            # Run 'Each Frame' code from bids_image
            
            concept_label_img = image_shown.split("\\")[0]
            concept_examplar_img =  image_shown.split("\\")[1]
            bids.schedule_onset(image,
                                    block_num=block_num,
                                    trial_num=trial_num, 
                                    type_of_stimulus="image",
                                    component_label="image",
                                    concept_label = concept_label_img,
                                    wrd_img_match = int(1-is_mismatch),
                                    concept_examplar = concept_examplar_img)
            
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + image_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.tStopRefresh = tThisFlipGlobal  # on global time
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
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
                    currentRoutine=image_pres,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                image_pres.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if image_pres.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in image_pres.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "image_pres" ---
        for thisComponent in image_pres.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for image_pres
        image_pres.tStop = globalClock.getTime(format='float')
        image_pres.tStopRefresh = tThisFlipGlobal
        thisExp.addData('image_pres.stopped', image_pres.tStop)
        # Run 'End Routine' code from bids_image
        
            
        bids.mark_offset(image)
        # the Routine "image_pres" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "sound_pres" ---
        # create an object to store info about Routine sound_pres
        sound_pres = data.Routine(
            name='sound_pres',
            components=[spoken_word, fix_cross, key_resp],
        )
        sound_pres.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from set_trigger_word
        trigNumber = int(concept_num_word + 100)
        
        
        spoken_word.stop()  # make sure nothing is still playing from the previous trial
        soundScheduled = False
        trigOnFlipTime = None
        # Run 'Begin Routine' code from set_word
        
        
        if language == 'english':
            part1 = (word_shown_english)
            part2 = "_en"
            word_shown = part1 + part2
        
            
        elif language == 'german':   
            part1 = (word_shown_german)
            part2 = "_german"
            word_shown = part1 + part2
        
        spoken_word.setSound(f"sounds/{word_shown}.mp3", hamming=True)
        spoken_word.setVolume(1.0, log=False)
        spoken_word.seek(0)
        fix_cross.setColor([1.0000, 1.0000, 1.0000], colorSpace='rgb')
        # Run 'Begin Routine' code from allowed_keys
        
        if match_responses == 0:
            allowed_key_list = [nonmatch_key]  # list of allowed keys
        else:
            # default: allow both match and nonmatch responses
            allowed_key_list = [match_key, nonmatch_key]
        # create starting attributes for key_resp
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # Run 'Begin Routine' code from code_key_resp
        
        # reset key resp and correct answer
        key_resp.keys = None
        key_resp.corr = None 
        
        
        
        
        # Run 'Begin Routine' code from set_trigger_response
        response_trigger = trigger_numbers_dict["response (button press)"]
        resp_trig_giv = False
        
        # Run 'Begin Routine' code from feedback_control_trigger
        
        # prepare feedback in form of word color change or too slow message
        feedback_given = False
        
        feedback_trigger_sent = False
        feedback_trigger_code = trigger_numbers_dict["feedback"]
        
        
        
        # store start times for sound_pres
        sound_pres.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        sound_pres.tStart = globalClock.getTime(format='float')
        sound_pres.status = STARTED
        thisExp.addData('sound_pres.started', sound_pres.tStart)
        sound_pres.maxDuration = None
        # keep track of which components have finished
        sound_presComponents = sound_pres.components
        for thisComponent in sound_pres.components:
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
        
        # --- Run Routine "sound_pres" ---
        thisExp.currentRoutine = sound_pres
        sound_pres.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from set_trigger_word
            if (not soundScheduled) and tThisFlip >= 0.0 - frameTolerance:
                spoken_word.stop()
                spoken_word.setSound(f"sounds/{word_shown}.mp3", secs=1)
            
                nextFlipPTB = win.getFutureFlipTime(clock='ptb')
                win.callOnFlip(send_trigger, trigNumber)
                spoken_word.play(when=nextFlipPTB)
            
            
                soundScheduled = True
            
            
            # *spoken_word* updates
            
            # if spoken_word is starting this frame...
            if spoken_word.status == NOT_STARTED and 9999:
                # keep track of start time/frame for later
                spoken_word.frameNStart = frameN  # exact frame index
                spoken_word.tStart = t  # local t and not account for scr refresh
                spoken_word.tStartRefresh = tThisFlipGlobal  # on global time
                # add timestamp to datafile
                thisExp.addData('spoken_word.started', tThisFlipGlobal)
                # update status
                spoken_word.status = STARTED
                spoken_word.play(when=win)  # sync with win flip
            
            # if spoken_word is stopping this frame...
            if spoken_word.status == STARTED:
                if bool(False) or spoken_word.isFinished:
                    # keep track of stop time/frame for later
                    spoken_word.tStop = t  # not accounting for scr refresh
                    spoken_word.tStopRefresh = tThisFlipGlobal  # on global time
                    spoken_word.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'spoken_word.stopped')
                    # update status
                    spoken_word.status = FINISHED
                    spoken_word.stop()
            # Run 'Each Frame' code from bids_word_logging
            bids.schedule_onset(spoken_word,
                                    block_num = block_num,
                                    trial_num = trial_num,
                                    type_of_stimulus="word",
                                    component_label="word",
                                    wrd_img_match = int(1-is_mismatch),
                                    concept_label = word_shown)
            
            # *fix_cross* updates
            
            # if fix_cross is starting this frame...
            if fix_cross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
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
                if tThisFlipGlobal > fix_cross.tStartRefresh + response_time-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross.tStop = t  # not accounting for scr refresh
                    fix_cross.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross.stopped')
                    # update status
                    fix_cross.status = FINISHED
                    fix_cross.setAutoDraw(False)
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=[nonmatch_key], ignoreKeys=["escape"], waitRelease=True)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                    key_resp.rt = _key_resp_allKeys[0].rt
                    key_resp.duration = _key_resp_allKeys[0].duration
            # Run 'Each Frame' code from code_key_resp
            if match_responses == 1: 
            
                if is_mismatch == 0:
                    answer_correct = match_key
                elif is_mismatch == 1:
                    answer_correct = nonmatch_key
                # Evaluate participant response
                if key_resp.keys is None:
                    key_resp.corr = "m"   # no response
                elif key_resp.keys == answer_correct:
                    key_resp.corr = 1      # correct response
                else:
                    key_resp.corr = 0      # wrong key
                    
                
            if match_responses == 0: 
                
                if is_mismatch == 0:
                    answer_correct = None
                elif is_mismatch == 1:
                    answer_correct = nonmatch_key
            
                # Evaluate participant response  
                if key_resp.keys == answer_correct:
                    key_resp.corr = 1      # correct response
                else:
                    key_resp.corr = 0      # wrong key
                    
            # Run 'Each Frame' code from set_trigger_response
            if (key_resp.keys is not None) and (not resp_trig_giv):
                
                if key_resp.corr == 1:      # correct response
                    response_trigger = 127
                elif key_resp.corr == 0:      # correct response
                    response_trigger = 128
            
                send_trigger(response_trigger)
                resp_trig_giv = True
                core.wait(0.01) # wait a bit so that feedback trigger doesnt start immediately
            
            
            
            # Run 'Each Frame' code from feedback_control_trigger
            
            if fdback == 1:
                if is_mismatch==1:  # Mismatch trial - button press required
                    if (not feedback_given):
                        # Case 1: Button was pressed before deadline
                        if (key_resp.keys is not None):
                            if getattr(key_resp, 'corr', None) == 1:
                                fix_cross.setColor('green')
                                feedback_given = True
                                feedback_end = t + 0.2
                            else:
                                fix_cross.setColor('red')
                                feedback_given = True
                                feedback_end = t + 0.2
                        # Case 2: No response by deadline
                        elif (t >= response_time) and (key_resp.keys is None):
                            fix_cross.setColor('red')  # No response on mismatch = incorrect
                            feedback_given = True
                            feedback_end = t + 0.2
                    
                    # Send trigger ONCE when feedback starts
                    if feedback_given and not feedback_trigger_sent:
                       send_trigger(feedback_trigger_code)
                       feedback_trigger_sent = True
            
                    
                    # feedback for 0.2s 
                    if feedback_given:
                        try:
                            if not fix_cross.autoDraw:
                                fix_cross.setAutoDraw(True)
                        except Exception:
                            pass
                        if t >= feedback_end:
                            spoken_word.stop()
                            continueRoutine = False
                            
                elif is_mismatch==0: # no button should be pressed
                    
                    if (not feedback_given):
                        # Case 1: Button was pressed (incorrect on match trial)
                        if (key_resp.keys is not None):
                            fix_cross.setColor('red')
                            feedback_given = True
                            feedback_end = t + 0.2
                        # Case 2: No response by deadline (correct on match trial)
                        elif (t >= response_time) and (key_resp.keys is None):
                            fix_cross.setColor('green')
                            feedback_given = True
                            feedback_end = t + 0.2
                    
                    # Send trigger ONCE when feedback starts
                    if feedback_given and not feedback_trigger_sent:
                        send_trigger(feedback_trigger_code)
                        feedback_trigger_sent = True
            
                    if feedback_given:
                        try:
                            if not fix_cross.autoDraw:
                                fix_cross.setAutoDraw(True)
                        except Exception:
                            pass
                        if t >= feedback_end:
                            spoken_word.stop()
                            continueRoutine = False
            
            else:
                # no feedback: end on response or timeout
                if (key_resp.keys is not None) or (t >= response_time):
                    spoken_word.stop()
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
                    currentRoutine=sound_pres,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                sound_pres.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if sound_pres.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in sound_pres.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "sound_pres" ---
        for thisComponent in sound_pres.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for sound_pres
        sound_pres.tStop = globalClock.getTime(format='float')
        sound_pres.tStopRefresh = tThisFlipGlobal
        thisExp.addData('sound_pres.stopped', sound_pres.tStop)
        # Run 'End Routine' code from set_trigger_word
        spoken_word.stop()
        spoken_word.pause()  # ensure sound has stopped at end of Routine
        # Run 'End Routine' code from bids_word_logging
        bids.mark_offset(spoken_word)
        
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
            trials.addData('key_resp.duration', key_resp.duration)
        # Run 'End Routine' code from bids_resp_logging
        
        # response neeeds to be saved at end of trial
        bids.add_instant(
            "response",
            response=(key_resp.keys if key_resp.keys else "m"),
            response_time=(key_resp.rt if hasattr(key_resp, "rt") else None),
            correct=(key_resp.corr if hasattr(key_resp, "corr") else "m"),
            expected_response = ("m" if answer_correct == None else answer_correct),
            block_num = block_num,
            trial_num = trial_num,
            wrd_img_match = int(1-is_mismatch),
            component_label = "possible_button_press"
        )
        
        
        # the Routine "sound_pres" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "ITI" ---
        # create an object to store info about Routine ITI
        ITI = data.Routine(
            name='ITI',
            components=[fix_cross_2],
        )
        ITI.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from set_trigger_fix_cross
        fixcross_trigger = trigger_numbers_dict["fixation cross ITI"]
        
        
        
        
        # Run 'Begin Routine' code from set_dur_ITI
        if key_resp.keys == None:
            length_of_ITI = ITI_length
        elif key_resp.keys:
            length_of_ITI = ITI_length + 1
        # store start times for ITI
        ITI.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        ITI.tStart = globalClock.getTime(format='float')
        ITI.status = STARTED
        thisExp.addData('ITI.started', ITI.tStart)
        ITI.maxDuration = None
        # keep track of which components have finished
        ITIComponents = ITI.components
        for thisComponent in ITI.components:
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
        
        # --- Run Routine "ITI" ---
        thisExp.currentRoutine = ITI
        ITI.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from set_trigger_fix_cross
            if frameN==0:
                send_trigger(fixcross_trigger)
            
            
            # Run 'Each Frame' code from bids_ITI_logging
            
            
            bids.schedule_onset(fix_cross_2,
                                    block_num = block_num,
                                    trial_num = trial_num,
                                    type_of_stimulus="fixation cross",
                                    component_label="fix_cross_after_trial")
                                   
            
                                   
            
            
            
            # *fix_cross_2* updates
            
            # if fix_cross_2 is starting this frame...
            if fix_cross_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                fix_cross_2.frameNStart = frameN  # exact frame index
                fix_cross_2.tStart = t  # local t and not account for scr refresh
                fix_cross_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_cross_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fix_cross_2.started')
                # update status
                fix_cross_2.status = STARTED
                fix_cross_2.setAutoDraw(True)
            
            # if fix_cross_2 is active this frame...
            if fix_cross_2.status == STARTED:
                # update params
                pass
            
            # if fix_cross_2 is stopping this frame...
            if fix_cross_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_cross_2.tStartRefresh + length_of_ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_cross_2.tStop = t  # not accounting for scr refresh
                    fix_cross_2.tStopRefresh = tThisFlipGlobal  # on global time
                    fix_cross_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fix_cross_2.stopped')
                    # update status
                    fix_cross_2.status = FINISHED
                    fix_cross_2.setAutoDraw(False)
            
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
                    currentRoutine=ITI,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                ITI.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if ITI.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in ITI.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI" ---
        for thisComponent in ITI.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for ITI
        ITI.tStop = globalClock.getTime(format='float')
        ITI.tStopRefresh = tThisFlipGlobal
        thisExp.addData('ITI.stopped', ITI.tStop)
        # Run 'End Routine' code from bids_ITI_logging
        
        # log offset at last frame of routine
        bids.mark_offset(fix_cross_2)
        
        # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "break_3" ---
        # create an object to store info about Routine break_3
        break_3 = data.Routine(
            name='break_3',
            components=[breaks_instruction, progress_bar_breaks, continue_button_break, instruction_continuebreak],
        )
        break_3.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from definition_breaks
        if trials.thisN == 0:
           continueRoutine = False
        elif current_trial_number % break_interval!= 0:
            continueRoutine = False
        elif block_num == total_block_number:
             continueRoutine = False
        
        # Run 'Begin Routine' code from control_trigger_break
        run_break = False
        end_trig_send = False
        
        if continueRoutine == True: 
            run_break = True 
        
        
        
        # Run 'Begin Routine' code from set_break_instruction_text
        
        if language=="english":
            breaks_instruction.text = (
            "Break, the task will continue soon.\n"
            f"There are {int(total_block_number - block_num)} blocks left."
            )
        elif language=="german":
             breaks_instruction.text =(
            "Pause, die Aufgabe geht gleich weiter.\n"
             f"Es sind noch {int(total_block_number - block_num)} Blöcke übrig."
        )
        elif language=="french":
             breaks_instruction.text =(
            "Pause, l'exercice reprend tout de suite.")
            
        
        # Run 'Begin Routine' code from set_progress
        timer_break = core.CountdownTimer(break_dur)
        
        # create starting attributes for continue_button_break
        continue_button_break.keys = []
        continue_button_break.rt = []
        _continue_button_break_allKeys = []
        # allowedKeys looks like a variable, so make sure it exists locally
        if 'possible_keys' in globals():
            possible_keys = globals()['possible_keys']
        # Run 'Begin Routine' code from set_instruction_continuebreak_text
        
        if language=="english":
            instruction_continuebreak.text = (
            "The break is over.\nPress any key to continue once you are ready.")
        elif language=="german":
             instruction_continuebreak.text =(
            "Die Pause ist vorbei.\nBitte drücken Sie eine beliebige Taste,\n"
            "sobald sie bereit sind, weiterzumachen.")
        
            
        
        # store start times for break_3
        break_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_3.tStart = globalClock.getTime(format='float')
        break_3.status = STARTED
        thisExp.addData('break_3.started', break_3.tStart)
        break_3.maxDuration = None
        # keep track of which components have finished
        break_3Components = break_3.components
        for thisComponent in break_3.components:
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
        
        # --- Run Routine "break_3" ---
        thisExp.currentRoutine = break_3
        break_3.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # if trial has changed, end Routine now
            if hasattr(thisTrial, 'status') and thisTrial.status == STOPPING:
                continueRoutine = False
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from control_trigger_break
            
            stim = "break_start"
            breakstart_trigger = trigger_numbers_dict[stim]
            
            if frameN == 0 and run_break:
                send_trigger(breakstart_trigger)
            
            # Run 'Each Frame' code from bids_break_logging
            
            bids.schedule_onset(breaks_instruction,
                                block_num = block_num,
                                trial_num = trial_num,
                                type_of_stimulus="break",
                                component_label="break_instruction")
            
            
            
            
            
            # *breaks_instruction* updates
            
            # if breaks_instruction is starting this frame...
            if breaks_instruction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                breaks_instruction.frameNStart = frameN  # exact frame index
                breaks_instruction.tStart = t  # local t and not account for scr refresh
                breaks_instruction.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(breaks_instruction, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'breaks_instruction.started')
                # update status
                breaks_instruction.status = STARTED
                breaks_instruction.setAutoDraw(True)
            
            # if breaks_instruction is active this frame...
            if breaks_instruction.status == STARTED:
                # update params
                pass
            
            # if breaks_instruction is stopping this frame...
            if breaks_instruction.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > breaks_instruction.tStartRefresh + break_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    breaks_instruction.tStop = t  # not accounting for scr refresh
                    breaks_instruction.tStopRefresh = tThisFlipGlobal  # on global time
                    breaks_instruction.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'breaks_instruction.stopped')
                    # update status
                    breaks_instruction.status = FINISHED
                    breaks_instruction.setAutoDraw(False)
            # Run 'Each Frame' code from set_progress
            frac = 1.0 - (int(timer_break.getTime()) / break_dur)  # 0→1
            progress_bar_breaks.progress = frac
            
            
            # *progress_bar_breaks* updates
            
            # if progress_bar_breaks is starting this frame...
            if progress_bar_breaks.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                progress_bar_breaks.frameNStart = frameN  # exact frame index
                progress_bar_breaks.tStart = t  # local t and not account for scr refresh
                progress_bar_breaks.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(progress_bar_breaks, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'progress_bar_breaks.started')
                # update status
                progress_bar_breaks.status = STARTED
                progress_bar_breaks.setAutoDraw(True)
            
            # if progress_bar_breaks is active this frame...
            if progress_bar_breaks.status == STARTED:
                # update params
                progress_bar_breaks.setProgress(frac, log=False)
            
            # if progress_bar_breaks is stopping this frame...
            if progress_bar_breaks.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > progress_bar_breaks.tStartRefresh + break_dur-frameTolerance:
                    # keep track of stop time/frame for later
                    progress_bar_breaks.tStop = t  # not accounting for scr refresh
                    progress_bar_breaks.tStopRefresh = tThisFlipGlobal  # on global time
                    progress_bar_breaks.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'progress_bar_breaks.stopped')
                    # update status
                    progress_bar_breaks.status = FINISHED
                    progress_bar_breaks.setAutoDraw(False)
            
            # *continue_button_break* updates
            waitOnFlip = False
            
            # if continue_button_break is starting this frame...
            if continue_button_break.status == NOT_STARTED and tThisFlip >= break_dur-frameTolerance:
                # keep track of start time/frame for later
                continue_button_break.frameNStart = frameN  # exact frame index
                continue_button_break.tStart = t  # local t and not account for scr refresh
                continue_button_break.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(continue_button_break, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'continue_button_break.started')
                # update status
                continue_button_break.status = STARTED
                # allowed keys looks like a variable named `possible_keys`
                if not type(possible_keys) in [list, tuple, np.ndarray]:
                    if not isinstance(possible_keys, str):
                        possible_keys = str(possible_keys)
                    elif not ',' in possible_keys:
                        possible_keys = (possible_keys,)
                    else:
                        possible_keys = eval(possible_keys)
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(continue_button_break.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(continue_button_break.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if continue_button_break.status == STARTED and not waitOnFlip:
                theseKeys = continue_button_break.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
                _continue_button_break_allKeys.extend(theseKeys)
                if len(_continue_button_break_allKeys):
                    continue_button_break.keys = _continue_button_break_allKeys[-1].name  # just the last key pressed
                    continue_button_break.rt = _continue_button_break_allKeys[-1].rt
                    continue_button_break.duration = _continue_button_break_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *instruction_continuebreak* updates
            
            # if instruction_continuebreak is starting this frame...
            if instruction_continuebreak.status == NOT_STARTED and tThisFlip >= break_dur-frameTolerance:
                # keep track of start time/frame for later
                instruction_continuebreak.frameNStart = frameN  # exact frame index
                instruction_continuebreak.tStart = t  # local t and not account for scr refresh
                instruction_continuebreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_continuebreak, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_continuebreak.started')
                # update status
                instruction_continuebreak.status = STARTED
                instruction_continuebreak.setAutoDraw(True)
            
            # if instruction_continuebreak is active this frame...
            if instruction_continuebreak.status == STARTED:
                # update params
                pass
            
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
                    currentRoutine=break_3,
                )
                # skip the frame we paused on
                continue
            
            # has a Component requested the Routine to end?
            if not continueRoutine:
                break_3.forceEnded = routineForceEnded = True
            # has the Routine been forcibly ended?
            if break_3.forceEnded or routineForceEnded:
                break
            # has every Component finished?
            continueRoutine = False
            for thisComponent in break_3.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_3" ---
        for thisComponent in break_3.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_3
        break_3.tStop = globalClock.getTime(format='float')
        break_3.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_3.stopped', break_3.tStop)
        # Run 'End Routine' code from control_trigger_break
        # send trigger for end break
        stim = "break_end"
        breakend_trigger = trigger_numbers_dict[stim]
        
        if run_break and not end_trig_send:
            send_trigger(breakend_trigger)
            end_trig_send = True
            core.wait(0.01) # wait so no overlap with next img trigger
        
        
        
        
        
        # Run 'End Routine' code from bids_break_logging
        
            
        bids.mark_offset(breaks_instruction)
        
        # check responses
        if continue_button_break.keys in ['', [], None]:  # No response was made
            continue_button_break.keys = None
        trials.addData('continue_button_break.keys',continue_button_break.keys)
        if continue_button_break.keys != None:  # we had a response
            trials.addData('continue_button_break.rt', continue_button_break.rt)
            trials.addData('continue_button_break.duration', continue_button_break.duration)
        # the Routine "break_3" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        # mark thisTrial as finished
        if hasattr(thisTrial, 'status'):
            thisTrial.status = FINISHED
        # if awaiting a pause, pause now
        if trials.status == PAUSED:
            thisExp.status = PAUSED
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[globalClock], 
            )
            # once done pausing, restore running status
            trials.status = STARTED
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trials'
    trials.status = FINISHED
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    trials.saveAsText(filename + '_trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "instructions_end" ---
    # create an object to store info about Routine instructions_end
    instructions_end = data.Routine(
        name='instructions_end',
        components=[instruction_end, continue_button_7],
    )
    instructions_end.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from set_trigger_end
    
     
    # Run 'Begin Routine' code from bids_instruc_end
    
    
    
    # Run 'Begin Routine' code from instruction_end_text
    if language == "english": 
        instruction_end.text = (
        "You have finished the first part of the task.\n"
        "Press any key to exit. "
    )
       
    if language == "german": 
        instruction_end.text = (
        "Sie haben den ersten Teil der Aufgabe beendet.\n"
        "Drücken Sie eine beliebige Taste, um zu beenden. "
    )
    
    if language == "french": 
        instruction_end.text = (
        "Vous avez terminé la première partie de la tâche. Appuyez sur la touche Entrée pour quitter. "
    )
    # create starting attributes for continue_button_7
    continue_button_7.keys = []
    continue_button_7.rt = []
    _continue_button_7_allKeys = []
    # allowedKeys looks like a variable, so make sure it exists locally
    if 'possible_keys' in globals():
        possible_keys = globals()['possible_keys']
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
    thisExp.currentRoutine = instructions_end
    instructions_end.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from set_trigger_end
        if frameN==0:
            send_trigger(trigger_numbers_dict["start/end"])
        # Run 'Each Frame' code from bids_instruc_end
        ## schedule bids trigger setting
        # log onset at first frame
        #if frameN == 0:
            #bids.schedule_onset(instruction_end,
                                #trial_type="localizer",
                                #stim_label="instruction_end")
                                
        bids.schedule_onset(instruction_end,
                                type_of_stimulus="instructions",
                                component_label="instruction_end")
        
        
        # *instruction_end* updates
        
        # if instruction_end is starting this frame...
        if instruction_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_end.frameNStart = frameN  # exact frame index
            instruction_end.tStart = t  # local t and not account for scr refresh
            instruction_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_end.started')
            # update status
            instruction_end.status = STARTED
            instruction_end.setAutoDraw(True)
        
        # if instruction_end is active this frame...
        if instruction_end.status == STARTED:
            # update params
            pass
        
        # *continue_button_7* updates
        waitOnFlip = False
        
        # if continue_button_7 is starting this frame...
        if continue_button_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            continue_button_7.frameNStart = frameN  # exact frame index
            continue_button_7.tStart = t  # local t and not account for scr refresh
            continue_button_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(continue_button_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'continue_button_7.started')
            # update status
            continue_button_7.status = STARTED
            # allowed keys looks like a variable named `possible_keys`
            if not type(possible_keys) in [list, tuple, np.ndarray]:
                if not isinstance(possible_keys, str):
                    possible_keys = str(possible_keys)
                elif not ',' in possible_keys:
                    possible_keys = (possible_keys,)
                else:
                    possible_keys = eval(possible_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(continue_button_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(continue_button_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if continue_button_7.status == STARTED and not waitOnFlip:
            theseKeys = continue_button_7.getKeys(keyList=list(possible_keys), ignoreKeys=["escape"], waitRelease=True)
            _continue_button_7_allKeys.extend(theseKeys)
            if len(_continue_button_7_allKeys):
                continue_button_7.keys = _continue_button_7_allKeys[-1].name  # just the last key pressed
                continue_button_7.rt = _continue_button_7_allKeys[-1].rt
                continue_button_7.duration = _continue_button_7_allKeys[-1].duration
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
        
        # has a Component requested the Routine to end?
        if not continueRoutine:
            instructions_end.forceEnded = routineForceEnded = True
        # has the Routine been forcibly ended?
        if instructions_end.forceEnded or routineForceEnded:
            break
        # has every Component finished?
        continueRoutine = False
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
    # Run 'End Routine' code from bids_instruc_end
    # log offset at last frame of routine
    #if not continueRoutine:  
        #bids.mark_offset(instruction_end)
    bids.mark_offset(instruction_end)
    # check responses
    if continue_button_7.keys in ['', [], None]:  # No response was made
        continue_button_7.keys = None
    thisExp.addData('continue_button_7.keys',continue_button_7.keys)
    if continue_button_7.keys != None:  # we had a response
        thisExp.addData('continue_button_7.rt', continue_button_7.rt)
        thisExp.addData('continue_button_7.duration', continue_button_7.duration)
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
    thisExp.saveAsWideText(filename + '.csv', delim='comma')
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
        globalClock='iso'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
