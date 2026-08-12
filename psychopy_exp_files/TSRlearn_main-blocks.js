/***************************** 
 * Tsrlearn_Main-Blocks *
 *****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2025.1.1.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'TSRlearn_main-blocks';  // from the Builder filename that created this script
let expInfo = {
    'participant_ID': '',
};
let PILOTING = util.getUrlParameters().has('__pilotToken');

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0.3255, 0.3255, 0.3255]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(startup_settingsRoutineBegin());
flowScheduler.add(startup_settingsRoutineEachFrame());
flowScheduler.add(startup_settingsRoutineEnd());
flowScheduler.add(instructions_01RoutineBegin());
flowScheduler.add(instructions_01RoutineEachFrame());
flowScheduler.add(instructions_01RoutineEnd());
flowScheduler.add(instructions_02RoutineBegin());
flowScheduler.add(instructions_02RoutineEachFrame());
flowScheduler.add(instructions_02RoutineEnd());
flowScheduler.add(instructions_03RoutineBegin());
flowScheduler.add(instructions_03RoutineEachFrame());
flowScheduler.add(instructions_03RoutineEnd());
flowScheduler.add(instructions_04RoutineBegin());
flowScheduler.add(instructions_04RoutineEachFrame());
flowScheduler.add(instructions_04RoutineEnd());
flowScheduler.add(instructions_05RoutineBegin());
flowScheduler.add(instructions_05RoutineEachFrame());
flowScheduler.add(instructions_05RoutineEnd());
flowScheduler.add(instructions_06RoutineBegin());
flowScheduler.add(instructions_06RoutineEachFrame());
flowScheduler.add(instructions_06RoutineEnd());
flowScheduler.add(instructions_replay_breakRoutineBegin());
flowScheduler.add(instructions_replay_breakRoutineEachFrame());
flowScheduler.add(instructions_replay_breakRoutineEnd());
const practice_learningLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practice_learningLoopBegin(practice_learningLoopScheduler));
flowScheduler.add(practice_learningLoopScheduler);
flowScheduler.add(practice_learningLoopEnd);



flowScheduler.add(rest_practiceRoutineBegin());
flowScheduler.add(rest_practiceRoutineEachFrame());
flowScheduler.add(rest_practiceRoutineEnd());
flowScheduler.add(instruction_retrieval_trialsRoutineBegin());
flowScheduler.add(instruction_retrieval_trialsRoutineEachFrame());
flowScheduler.add(instruction_retrieval_trialsRoutineEnd());
flowScheduler.add(instruction_retrievalques1RoutineBegin());
flowScheduler.add(instruction_retrievalques1RoutineEachFrame());
flowScheduler.add(instruction_retrievalques1RoutineEnd());
flowScheduler.add(instruction_retrievalques1_02RoutineBegin());
flowScheduler.add(instruction_retrievalques1_02RoutineEachFrame());
flowScheduler.add(instruction_retrievalques1_02RoutineEnd());
flowScheduler.add(instruction_retrievalques2RoutineBegin());
flowScheduler.add(instruction_retrievalques2RoutineEachFrame());
flowScheduler.add(instruction_retrievalques2RoutineEnd());
flowScheduler.add(instruction_retrievalques2_02RoutineBegin());
flowScheduler.add(instruction_retrievalques2_02RoutineEachFrame());
flowScheduler.add(instruction_retrievalques2_02RoutineEnd());
flowScheduler.add(instruction_refl_periodRoutineBegin());
flowScheduler.add(instruction_refl_periodRoutineEachFrame());
flowScheduler.add(instruction_refl_periodRoutineEnd());
flowScheduler.add(instruction_refl_period_02RoutineBegin());
flowScheduler.add(instruction_refl_period_02RoutineEachFrame());
flowScheduler.add(instruction_refl_period_02RoutineEnd());
flowScheduler.add(retrieval_backg_infoRoutineBegin());
flowScheduler.add(retrieval_backg_infoRoutineEachFrame());
flowScheduler.add(retrieval_backg_infoRoutineEnd());
flowScheduler.add(instruction_practice_type1RoutineBegin());
flowScheduler.add(instruction_practice_type1RoutineEachFrame());
flowScheduler.add(instruction_practice_type1RoutineEnd());
const retrieval_prc_loopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(retrieval_prc_loopLoopBegin(retrieval_prc_loopLoopScheduler));
flowScheduler.add(retrieval_prc_loopLoopScheduler);
flowScheduler.add(retrieval_prc_loopLoopEnd);












flowScheduler.add(instructions_07RoutineBegin());
flowScheduler.add(instructions_07RoutineEachFrame());
flowScheduler.add(instructions_07RoutineEnd());
const BlockLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BlockLoopBegin(BlockLoopScheduler));
flowScheduler.add(BlockLoopScheduler);
flowScheduler.add(BlockLoopEnd);




























flowScheduler.add(instructions_endRoutineBegin());
flowScheduler.add(instructions_endRoutineEachFrame());
flowScheduler.add(instructions_endRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'sequences/main_trials_prc.xlsx', 'path': 'sequences/main_trials_prc.xlsx'},
    {'name': 'stimuli/practice_images/anchor.jpg', 'path': 'stimuli/practice_images/anchor.jpg'},
    {'name': 'stimuli/practice_images/cow.jpg', 'path': 'stimuli/practice_images/cow.jpg'},
    {'name': 'stimuli/practice_images/bread.jpg', 'path': 'stimuli/practice_images/bread.jpg'},
    {'name': 'stimuli/practice_images/plane.jpg', 'path': 'stimuli/practice_images/plane.jpg'},
    {'name': 'stimuli/practice_images/ant.jpg', 'path': 'stimuli/practice_images/ant.jpg'},
    {'name': 'stimuli/practice_images/banana.jpg', 'path': 'stimuli/practice_images/banana.jpg'},
    {'name': 'stimuli/practice_images/glasses.jpg', 'path': 'stimuli/practice_images/glasses.jpg'},
    {'name': 'stimuli/practice_images/basket.jpg', 'path': 'stimuli/practice_images/basket.jpg'},
    {'name': 'stimuli/practice_images/axe.jpg', 'path': 'stimuli/practice_images/axe.jpg'},
    {'name': 'stimuli/practice_images/duck.jpg', 'path': 'stimuli/practice_images/duck.jpg'},
    {'name': 'stimuli/practice_images/bed.jpg', 'path': 'stimuli/practice_images/bed.jpg'},
    {'name': 'stimuli/practice_images/belt.jpg', 'path': 'stimuli/practice_images/belt.jpg'},
    {'name': 'stimuli/practice_images/desk.jpg', 'path': 'stimuli/practice_images/desk.jpg'},
    {'name': 'stimuli/practice_images/bird.jpg', 'path': 'stimuli/practice_images/bird.jpg'},
    {'name': 'stimuli/practice_images/crocodile.jpg', 'path': 'stimuli/practice_images/crocodile.jpg'},
    {'name': 'sequences/retr_trials_prc_03.xlsx', 'path': 'sequences/retr_trials_prc_03.xlsx'},
    {'name': 'stimuli/practice_images/cow.jpg', 'path': 'stimuli/practice_images/cow.jpg'},
    {'name': 'stimuli/practice_images/basket.jpg', 'path': 'stimuli/practice_images/basket.jpg'},
    {'name': 'stimuli/practice_images/practice_sequence_overview_t3_01.jpg', 'path': 'stimuli/practice_images/practice_sequence_overview_t3_01.jpg'},
    {'name': 'stimuli/practice_images/belt.jpg', 'path': 'stimuli/practice_images/belt.jpg'},
    {'name': 'stimuli/practice_images/practice_sequence_overview_t3_02.jpg', 'path': 'stimuli/practice_images/practice_sequence_overview_t3_02.jpg'},
    {'name': 'stimuli/practice_images/ant.jpg', 'path': 'stimuli/practice_images/ant.jpg'},
    {'name': 'stimuli/practice_images/practice_sequence_overview_t3_03.jpg', 'path': 'stimuli/practice_images/practice_sequence_overview_t3_03.jpg'},
    {'name': 'sequences/block_conditions.xlsx', 'path': 'sequences/block_conditions.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'stimuli/mask_images/mask_00.png', 'path': 'stimuli/mask_images/mask_00.png'},
    {'name': 'stimuli/mask_images/mask_01.png', 'path': 'stimuli/mask_images/mask_01.png'},
    {'name': 'sequences/block_conditions.xlsx', 'path': 'sequences/block_conditions.xlsx'},
    {'name': 'sequences/main_trials_prc.xlsx', 'path': 'sequences/main_trials_prc.xlsx'},
    {'name': 'sequences/retr_trials_prc.xlsx', 'path': 'sequences/retr_trials_prc.xlsx'},
    {'name': 'sequences/retr_trials_prc_01.xlsx', 'path': 'sequences/retr_trials_prc_01.xlsx'},
    {'name': 'sequences/retr_trials_prc_02.xlsx', 'path': 'sequences/retr_trials_prc_02.xlsx'},
    {'name': 'sequences/retr_trials_prc_03.xlsx', 'path': 'sequences/retr_trials_prc_03.xlsx'},
    {'name': 'sequences/retr_trials_prc_overview.xlsx', 'path': 'sequences/retr_trials_prc_overview.xlsx'},
    {'name': 'sequences/trivia_questions_Block1.xlsx', 'path': 'sequences/trivia_questions_Block1.xlsx'},
    {'name': 'sequences/trivia_questions_Block2.xlsx', 'path': 'sequences/trivia_questions_Block2.xlsx'},
    {'name': 'sequences/block_conditions.xlsx', 'path': 'sequences/block_conditions.xlsx'},
    {'name': 'stimuli/default.png', 'path': 'stimuli/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2025.1.1';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls(('https://run.pavlovia.org/sianna/tsrlearn_questionnaires/?ORSEE_ID=' + expInfo['ORSEE_ID']), '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + ((((("data/" + expInfo["participant_ID"]) + "_") + expName) + "_") + expInfo["date"]));
  psychoJS.experiment.field_separator = '\\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "startup_settings"
  startup_settingsClock = new util.Clock();
  // Run 'Begin Experiment' code from import_packages
  import {Path} from 'pathlib';
  import * as csv from 'csv';
  import * as np from 'numpy';
  import * as atexit from 'atexit';
  import * as random from 'random';
  
  // Run 'Begin Experiment' code from function_definitions
  /* Syntax Error: Fix Python code */
  // Run 'Begin Experiment' code from exp_settings
  language = "english";
  left_key = "left";
  center_key = "up";
  right_key = "right";
  down_key = "down";
  left_pos = [(- 0.2), 0.1];
  right_pos = [0.2, 0.1];
  center_pos = [0.0, 0.1];
  prompt_pos = [0, (- 0.1)];
  instruc_pos = [0, 0];
  max_response_time = 3;
  feedback_steps = 0.06;
  rest_jump = 0.004;
  animation_time = 1.4;
  break_after_route = 10;
  break_dur = 30;
  replay_break_dur = 5;
  trials_per_run = 13;
  n_learn_route = 6;
  retr_dur = 5;
  too_slow_dur = 0.5;
  retrieval_quest_dur = 5.5;
  retr_dur_slider = 5;
  instr_newroute_dur = 1;
  fast_img_dur = 0.075;
  mask_dur = 0.05;
  
  // Run 'Begin Experiment' code from bids_logging_functions
  /* Syntax Error: Fix Python code */
  // Run 'Begin Experiment' code from set_arc_img_pos
  import * as math from 'math';
  [cx, cy] = prompt_pos;
  r = 0.25;
  spread_deg = 45;
  function _on_arc(angle_deg) {
      var a;
      a = math.radians(angle_deg);
      return [(cx + (r * Math.cos(a))), (cy + (r * Math.sin(a)))];
  }
  center_pos = _on_arc(90);
  left_pos = _on_arc((90 + spread_deg));
  right_pos = _on_arc((90 - spread_deg));
  
  // Initialize components for Routine "instructions_01"
  instructions_01Clock = new util.Clock();
  instruction_part1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part1',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  continue_button = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_02"
  instructions_02Clock = new util.Clock();
  instruction_part2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part2',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_03"
  instructions_03Clock = new util.Clock();
  instruction_part3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part3',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_04"
  instructions_04Clock = new util.Clock();
  instruction_part4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part4',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_05"
  instructions_05Clock = new util.Clock();
  instruction_part5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part5',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  continue_button_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_06"
  instructions_06Clock = new util.Clock();
  instruction_part6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part6',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  continue_button_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_replay_break"
  instructions_replay_breakClock = new util.Clock();
  instructions_part16 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_part16',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_choice_display"
  practice_choice_displayClock = new util.Clock();
  window.prompt_prc = null; 
  window.dist_01_prc = null;
  window.dist_02_prc = null;
  window.correct_prc = null;
  window.instructions_choose_2 = null; 
  window.practice_choice_displayMaxDurationReached = null;
  window.key_resp_2 = null; 
  window.polygon = null;
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon', 
    width: [0.11, 0.11][0], height: [0.11, 0.11][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 1.0, 
    depth: -1, 
    interpolate: true, 
  });
  
  prompt_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prompt_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  dist_01_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_01_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  dist_02_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_02_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  correct_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  instructions_choose_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_choose_2',
    text: '',
    font: font_name,
    units: undefined, 
    pos: instruc_pos, draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "practice_feedback"
  practice_feedbackClock = new util.Clock();
  polygon_7 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_7', 
    width: [0.11, 0.11][0], height: [0.11, 0.11][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([0.0039, 0.0039, 0.0039]), 
    fillColor: new util.Color([0, 0, 0]), 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  prompt_prc_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prompt_prc_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  dist_01_prc_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_01_prc_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  dist_02_prc_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_02_prc_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  correct_prc_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_prc_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  // Initialize components for Routine "rest_practice"
  rest_practiceClock = new util.Clock();
  fix_cross_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross_2',
    text: '+',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rest_instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_instruction',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instruction_retrieval_trials"
  instruction_retrieval_trialsClock = new util.Clock();
  instruction_part7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part7',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_retrievalques1"
  instruction_retrievalques1Clock = new util.Clock();
  instruction_part10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part10',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_retrievalques1_02"
  instruction_retrievalques1_02Clock = new util.Clock();
  instruction_part13 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part13',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_retrievalques2"
  instruction_retrievalques2Clock = new util.Clock();
  instruction_part11 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part11',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_retrievalques2_02"
  instruction_retrievalques2_02Clock = new util.Clock();
  instruction_part14 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part14',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_refl_period"
  instruction_refl_periodClock = new util.Clock();
  instruction_part12 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part12',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_14 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_refl_period_02"
  instruction_refl_period_02Clock = new util.Clock();
  instruction_part15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part15',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_21 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "retrieval_backg_info"
  retrieval_backg_infoClock = new util.Clock();
  instruction_info = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_info',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0.0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction_practice_type1"
  instruction_practice_type1Clock = new util.Clock();
  instruction_part8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_part8',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "retrieval_type1_practice"
  retrieval_type1_practiceClock = new util.Clock();
  fix_cross_retrbegin = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross_retrbegin',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "first_image_prc"
  first_image_prcClock = new util.Clock();
  image_1_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  info_example_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "mask_retr1_prc"
  mask_retr1_prcClock = new util.Clock();
  mask_img1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_img1', units : undefined, 
    image : 'stimuli/mask_images/mask_00.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  info_example_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "second_image_prc"
  second_image_prcClock = new util.Clock();
  image_2_prc = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2_prc', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  info_example_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_5', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "mask_retr2_prc"
  mask_retr2_prcClock = new util.Clock();
  mask_img2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_img2', units : undefined, 
    image : 'stimuli/mask_images/mask_01.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  info_example_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_6', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "reflection_period"
  reflection_periodClock = new util.Clock();
  fix_cross_reflretr_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross_reflretr_2',
    text: '+',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Denken Sie jetzt über die Antworten nach. ',
    font: font_name,
    units: undefined, 
    pos: [0, 0.1], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "retr_response_order_prc"
  retr_response_order_prcClock = new util.Clock();
  window.image_1_rpt_2 = null;
  window.opt_left_img_2 = null;
  window.opt_right_img_2 = null;
  window.yes_txt_2 = null; 
  window.no_txt_2 = null; 
  window.fix_cross_12 = null; 
  window.slider_main_2 = null; 
  window.resp_2 = null; 
  window.polygon_2 = null; 
  window.polygon_3 = null; 
  window.retr_response_prcMaxDurationReached = null;
  window.description_left_img = null; 
  window.description_right_img = null; 
  window.info_example = null; 
  window.text_log_in = null; 
  
  yes_txt_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'yes_txt_3',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  no_txt_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_txt_3',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  polygon_9 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_9', 
    width: [0.08, 0.03][0], height: [0.08, 0.03][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 2.0, 
    lineColor: new util.Color([0.0039, 0.0039, 0.0039]), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -3, 
    interpolate: true, 
  });
  
  resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  info_example_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_7', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  // Initialize components for Routine "retr_response_distance_prc"
  retr_response_distance_prcClock = new util.Clock();
  window.image_1_rpt_2 = null;
  window.opt_left_img_2 = null;
  window.opt_right_img_2 = null;
  window.yes_txt_2 = null; 
  window.no_txt_2 = null; 
  window.fix_cross_12 = null; 
  window.slider_main_2 = null; 
  window.resp_2 = null; 
  window.polygon_2 = null; 
  window.polygon_3 = null; 
  window.retr_response_prcMaxDurationReached = null;
  window.description_left_img = null; 
  window.description_right_img = null; 
  window.info_example = null; 
  window.text_log_in = null; 
  
  resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  info_example = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, (- 0.2)], 
    draggable: false,
    size : [0.7, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  opt_2_prc = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_2_prc',
    text: '2',
    font: font_name,
    units: undefined, 
    pos: [0, 0.05], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  opt_3_prc = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_3_prc',
    text: '3',
    font: font_name,
    units: undefined, 
    pos: [0.05, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  opt_4_prc = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_4_prc',
    text: '4',
    font: font_name,
    units: undefined, 
    pos: [0, (- 0.05)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  opt_5_prc = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_5_prc',
    text: '5',
    font: font_name,
    units: undefined, 
    pos: [(- 0.05), 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "retr_response_feedback"
  retr_response_feedbackClock = new util.Clock();
  text_feedback = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_feedback',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  info_example_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'info_example_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.8, null],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  continue_button_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_continue = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_continue',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, (- 0.15)], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "instructions_07"
  instructions_07Clock = new util.Clock();
  instructions_part7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_part7',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_13 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reset_rows_to_select"
  reset_rows_to_selectClock = new util.Clock();
  // Run 'Begin Experiment' code from define_number_trials
  function take_block(pool, ptr, n) {
      var rows;
      if (((ptr + n) > pool.length)) {
          throw new RuntimeError(`Not enough unique trials left to take ${n} rows.`);
      }
      rows = pool.slice(ptr, (ptr + n));
      ptr += n;
      return [rows, ptr];
  }
  
  // Initialize components for Routine "set_learning_rows"
  set_learning_rowsClock = new util.Clock();
  // Initialize components for Routine "show_context"
  show_contextClock = new util.Clock();
  scene_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'scene_image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "choice_display"
  choice_displayClock = new util.Clock();
  scene_image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'scene_image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  window.prompt_prc = null; 
  window.dist_01_prc = null;
  window.dist_02_prc = null;
  window.correct_prc = null;
  window.instructions_choose_2 = null; 
  window.practice_choice_displayMaxDurationReached = null;
  window.key_resp_2 = null; 
  window.polygon = null;
  polygon_4 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_4', 
    width: [0.11, 0.11][0], height: [0.11, 0.11][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -4, 
    interpolate: true, 
  });
  
  prompt = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prompt', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  dist_01 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_01', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  dist_02 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_02', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  correct = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  chooseNowText = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseNowText',
    text: 'Bitte antworten Sie jetzt',
    font: font_name,
    units: undefined, 
    pos: [0, 0.2], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -10.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  scene_image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'scene_image_3', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  polygon_8 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_8', 
    width: [0.11, 0.11][0], height: [0.11, 0.11][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -3, 
    interpolate: true, 
  });
  
  prompt_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prompt_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  dist_01_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_01_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  dist_02_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dist_02_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  correct_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'correct_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "too_slow_routine"
  too_slow_routineClock = new util.Clock();
  scene_image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'scene_image_4', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tooSlowtext = new visual.TextStim({
    win: psychoJS.window,
    name: 'tooSlowtext',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.02,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "rest_period"
  rest_periodClock = new util.Clock();
  fix_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross',
    text: '+',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instruction_retr_start"
  instruction_retr_startClock = new util.Clock();
  instruction_now_retr = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_now_retr',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  continue_button_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "set_retrieval_rows"
  set_retrieval_rowsClock = new util.Clock();
  // Initialize components for Routine "retr_ITI"
  retr_ITIClock = new util.Clock();
  fix_cross_retrbegin_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross_retrbegin_2',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "first_image"
  first_imageClock = new util.Clock();
  image_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_1', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "mask_retr1"
  mask_retr1Clock = new util.Clock();
  mask_img1_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_img1_2', units : undefined, 
    image : 'stimuli/mask_images/mask_00.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "second_image"
  second_imageClock = new util.Clock();
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "mask_retr2"
  mask_retr2Clock = new util.Clock();
  mask_img2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'mask_img2_2', units : undefined, 
    image : 'stimuli/mask_images/mask_01.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [0.15, 0.15],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "reflection_period_retr"
  reflection_period_retrClock = new util.Clock();
  fix_cross_reflretr = new visual.TextStim({
    win: psychoJS.window,
    name: 'fix_cross_reflretr',
    text: '+',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "retr_response_order"
  retr_response_orderClock = new util.Clock();
  window.image_1_rpt_2 = null;
  window.opt_left_img_2 = null;
  window.opt_right_img_2 = null;
  window.yes_txt_2 = null; 
  window.no_txt_2 = null; 
  window.fix_cross_12 = null; 
  window.slider_main_2 = null; 
  window.resp_2 = null; 
  window.polygon_2 = null; 
  window.polygon_3 = null; 
  window.retr_response_prcMaxDurationReached = null;
  window.description_left_img = null; 
  window.description_right_img = null; 
  window.info_example = null; 
  window.text_log_in = null; 
  
  polygon_6 = new visual.Rect ({
    win: psychoJS.window, name: 'polygon_6', 
    width: [0.08, 0.03][0], height: [0.08, 0.03][1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.5, 
    lineColor: new util.Color([0.0039, 0.0039, 0.0039]), 
    fillColor: undefined, 
    colorSpace: 'rgb', 
    opacity: 0.0, 
    depth: -2, 
    interpolate: true, 
  });
  
  yes_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'yes_txt',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  no_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'no_txt',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  chooseNowText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseNowText_2',
    text: 'Bitte antworten Sie jetzt',
    font: font_name,
    units: undefined, 
    pos: [0, 0.15], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -7.0 
  });
  
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "too_slow_routine_1"
  too_slow_routine_1Clock = new util.Clock();
  tooSlowtext_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tooSlowtext_4',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "retr_response_distance"
  retr_response_distanceClock = new util.Clock();
  window.image_1_rpt_2 = null;
  window.opt_left_img_2 = null;
  window.opt_right_img_2 = null;
  window.yes_txt_2 = null; 
  window.no_txt_2 = null; 
  window.fix_cross_12 = null; 
  window.slider_main_2 = null; 
  window.resp_2 = null; 
  window.polygon_2 = null; 
  window.polygon_3 = null; 
  window.retr_response_prcMaxDurationReached = null;
  window.description_left_img = null; 
  window.description_right_img = null; 
  window.info_example = null; 
  window.text_log_in = null; 
  
  chooseNowText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseNowText_3',
    text: 'Bitte antworten Sie jetzt',
    font: font_name,
    units: undefined, 
    pos: [0, 0.15], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: -3.0 
  });
  
  resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  opt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_2',
    text: '2',
    font: font_name,
    units: undefined, 
    pos: [0, 0.05], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  opt_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_3',
    text: '3',
    font: font_name,
    units: undefined, 
    pos: [0.05, 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  opt_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_4',
    text: '4',
    font: font_name,
    units: undefined, 
    pos: [0, (- 0.05)], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -7.0 
  });
  
  opt_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'opt_5',
    text: '5',
    font: font_name,
    units: undefined, 
    pos: [(- 0.05), 0], draggable: false, height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "too_slow_routine_2"
  too_slow_routine_2Clock = new util.Clock();
  tooSlowtext_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tooSlowtext_2',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "retr_task_break"
  retr_task_breakClock = new util.Clock();
  break_instruction = new visual.TextStim({
    win: psychoJS.window,
    name: 'break_instruction',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Run 'Begin Experiment' code from set_break_text
  if ((language === "german")) {
      break_instruction.text = "Kurze Pause. Es geht gleich weiter.";
  }
  if ((language === "english")) {
      break_instruction.text = "Short break. The task will continue soon.";
  }
  if ((language === "french")) {
      break_instruction.text = "Courte pause. La t\u00e2che reprendra bient\u00f4t.";
  }
  
  // Initialize components for Routine "instructions_new_learn"
  instructions_new_learnClock = new util.Clock();
  instruction_text_newroute = new visual.TextStim({
    win: psychoJS.window,
    name: 'instruction_text_newroute',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "instructions_end"
  instructions_endClock = new util.Clock();
  instructions_end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_end_text',
    text: '',
    font: font_name,
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.025,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  continue_button_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function startup_settingsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'startup_settings' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    startup_settingsClock.reset();
    routineTimer.reset();
    startup_settingsMaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from refine_positions
    POS = {"left": left_pos, "center": center_pos, "right": right_pos};
    pos_to_key = {[right_pos]: right_key, [center_pos]: center_key, [left_pos]: left_key};
    
    // Run 'Begin Routine' code from set_trigger_numbers
    trigger_dict = {"start/end": 255, "image_selected": 51, "feedback": 52, "replay_break": 53, "replay_break_end": 54, "order_retrieval_options": 59, "distance_retrieval_options": 58, "distance_retrieval_response": 56, "order_retrieval_response": 55, "task_break_begin": 81, "task_break_end": 82, "reflection_per": 31, "reflection_per_end": 32};
    
    psychoJS.experiment.addData('startup_settings.started', globalClock.getTime());
    startup_settingsMaxDuration = null
    // keep track of which components have finished
    startup_settingsComponents = [];
    
    for (const thisComponent of startup_settingsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function startup_settingsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'startup_settings' ---
    // get current time
    t = startup_settingsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      routineForceEnded = true;
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of startup_settingsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function startup_settingsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'startup_settings' ---
    for (const thisComponent of startup_settingsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('startup_settings.stopped', globalClock.getTime());
    // the Routine "startup_settings" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function instructions_01RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_01' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // keep track of whether this Routine was forcibly ended
    routineForceEnded = false;
    instructions_01Clock.reset();
    routineTimer.reset();
    instructions_01MaxDurationReached = false;
    // update component parameters for each repeat
    // Run 'Begin Routine' code from set_trigger_start
    trigNumber = trigger_dict["start/end"];
    
    // Run 'Begin Routine' code from instruction_part1_text
    if ((language === "english")) {
        instruction_part1.text = "Welcome to the task.\n\nIn this experiment, you will learn sequences of images.\n\nLearning phases are interleaved with retrieval phases, in which you will answer questions about the sequences you learned.\n\nPress any key to continue.";
    }
    if ((language === "german")) {
        instruction_part1.text = "Willkommen zu der Aufgabe.\n\nIn diesem Experiment lernen Sie verschiedene Bildsequenzen.\n\nDie Lernphasen wechseln sich mit Abrufphasen ab.\nIn den Abrufphasen beantworten Sie Fragen zu den zuvor\ngelernten Sequenzen.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
    }
    
    continue_button.keys = undefined;
    continue_button.rt = undefined;
    _continue_button_allKeys = [];
    psychoJS.experiment.addData('instructions_01.started', globalClock.getTime());
    instructions_01MaxDuration = null
    // keep track of which components have finished
    instructions_01Components = [];
    instructions_01Components.push(instruction_part1);
    instructions_01Components.push(continue_button);
    
    for (const thisComponent of instructions_01Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}

function instructions_01RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_01' ---
    // get current time
    t = instructions_01Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from set_trigger_start
    if ((frameN === 0)) {
        bids.trigger(trigNumber, {"stim": instruction_part1, "label": "exp_start"});
    }
    
    // Run 'Each Frame' code from bids_instruc
    bids.schedule_onset(instruction_part1, {"trial_type": "instruction", "type_of_stimulus": "instruction_text", "component_label": "instruction_part1"});
    
    
    // *instruction_part1* updates
    if (t >= 0.0 && instruction_part1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instruction_part1.tStart = t;  // (not accounting for frame time here)
      instruction_part1.frameNStart = frameN;  // exact frame index
      
      instruction_part1.setAutoDraw(true);
    }
    
    
    // if instruction_part1 is active this frame...
    if (instruction_part1.status === PsychoJS.Status.STARTED) {
    }
    
    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (instruction_part1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      instruction_part1.tStop = t;  // not accounting for scr refresh
      instruction_part1.frameNStop = frameN;  // exact frame index
      // update status
      instruction_part1.status = PsychoJS.Status.FINISHED;
      instruction_part1.setAutoDraw(false);
    }
    
    
    // *continue_button* updates
    if (t >= 3 && continue_button.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      continue_button.tStart = t;  // (not accounting for frame time here)
      continue_button.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { continue_button.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { continue_button.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { continue_button.clearEvents(); });
    }
    frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (continue_button.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      // keep track of stop time/frame for later
      continue_button.tStop = t;  // not accounting for scr refresh
      continue_button.frameNStop = frameN;  // exact frame index
      // update status
      continue_button.status = PsychoJS.Status.FINISHED;
      frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (continue_button.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        continue_button.tStop = t;  // not accounting for scr refresh
        continue_button.frameNStop = frameN;  // exact frame index
        // update status
        continue_button.status = PsychoJS.Status.FINISHED;
        continue_button.status = PsychoJS.Status.FINISHED;
          }
        
      }
      
      // if continue_button is active this frame...
      if (continue_button.status === PsychoJS.Status.STARTED) {
        let theseKeys = continue_button.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
        _continue_button_allKeys = _continue_button_allKeys.concat(theseKeys);
        if (_continue_button_allKeys.length > 0) {
          continue_button.keys = _continue_button_allKeys[0].name;  // just the first key pressed
          continue_button.rt = _continue_button_allKeys[0].rt;
          continue_button.duration = _continue_button_allKeys[0].duration;
          // a response ends the routine
          continueRoutine = false;
        }
      }
      
      // check for quit (typically the Esc key)
      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
      }
      
      // check if the Routine should terminate
      if (!continueRoutine) {  // a component has requested a forced-end of Routine
        routineForceEnded = true;
        return Scheduler.Event.NEXT;
      }
      
      continueRoutine = false;  // reverts to True if at least one component still running
      for (const thisComponent of instructions_01Components)
        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
          continueRoutine = true;
          break;
        }
      
      // refresh the screen if continuing
      if (continueRoutine) {
        return Scheduler.Event.FLIP_REPEAT;
      } else {
        return Scheduler.Event.NEXT;
      }
    };
  }
  
  function instructions_01RoutineEnd(snapshot) {
    return async function () {
      //--- Ending Routine 'instructions_01' ---
      for (const thisComponent of instructions_01Components) {
        if (typeof thisComponent.setAutoDraw === 'function') {
          thisComponent.setAutoDraw(false);
        }
      }
      psychoJS.experiment.addData('instructions_01.stopped', globalClock.getTime());
      // Run 'End Routine' code from bids_instruc
      bids.mark_offset(instruction_part1);
      
      // update the trial handler
      if (currentLoop instanceof MultiStairHandler) {
        currentLoop.addResponse(continue_button.corr, level);
      }
      psychoJS.experiment.addData('continue_button.keys', continue_button.keys);
      if (typeof continue_button.keys !== 'undefined') {  // we had a response
          psychoJS.experiment.addData('continue_button.rt', continue_button.rt);
          psychoJS.experiment.addData('continue_button.duration', continue_button.duration);
          routineTimer.reset();
          }
      
      continue_button.stop();
      // the Routine "instructions_01" was not non-slip safe, so reset the non-slip timer
      routineTimer.reset();
      
      // Routines running outside a loop should always advance the datafile row
      if (currentLoop === psychoJS.experiment) {
        psychoJS.experiment.nextEntry(snapshot);
      }
      return Scheduler.Event.NEXT;
    }
  }
  
  function instructions_02RoutineBegin(snapshot) {
    return async function () {
      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
      
      //--- Prepare to start Routine 'instructions_02' ---
      t = 0;
      frameN = -1;
      continueRoutine = true; // until we're told otherwise
      // keep track of whether this Routine was forcibly ended
      routineForceEnded = false;
      instructions_02Clock.reset();
      routineTimer.reset();
      instructions_02MaxDurationReached = false;
      // update component parameters for each repeat
      // Run 'Begin Routine' code from instruction_part2_text
      if ((language === "english")) {
          instruction_part2.text = "To help you remember the order of the images, please try to connect them into a story in your head.\n\nFor example: the dog is playing guitar, and then the lamp turns on.\n\nYou will now first practice the learning phases.\n\nPress any key to learn how the learning phases work.";
      }
      if ((language === "german")) {
          instruction_part2.text = "Um sich die Reihenfolge besser zu merken, verbinden Sie die\nBilder gedanklich zu einer Geschichte.\n\nZum Beispiel: Der Hund spielt Gitarre, danach geht die Lampe an.\n\nZun\u00e4chst \u00fcben Sie die Lernphasen.\n\nDr\u00fccken Sie eine beliebige Taste, um zu erfahren, wie diese ablaufen.";
      }
      
      continue_button_3.keys = undefined;
      continue_button_3.rt = undefined;
      _continue_button_3_allKeys = [];
      psychoJS.experiment.addData('instructions_02.started', globalClock.getTime());
      instructions_02MaxDuration = null
      // keep track of which components have finished
      instructions_02Components = [];
      instructions_02Components.push(instruction_part2);
      instructions_02Components.push(continue_button_3);
      
      for (const thisComponent of instructions_02Components)
        if ('status' in thisComponent)
          thisComponent.status = PsychoJS.Status.NOT_STARTED;
      return Scheduler.Event.NEXT;
    }
  }
  
  function instructions_02RoutineEachFrame() {
    return async function () {
      //--- Loop for each frame of Routine 'instructions_02' ---
      // get current time
      t = instructions_02Clock.getTime();
      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
      // update/draw components on each frame
      
      // *instruction_part2* updates
      if (t >= 0 && instruction_part2.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        instruction_part2.tStart = t;  // (not accounting for frame time here)
        instruction_part2.frameNStart = frameN;  // exact frame index
        
        instruction_part2.setAutoDraw(true);
      }
      
      
      // if instruction_part2 is active this frame...
      if (instruction_part2.status === PsychoJS.Status.STARTED) {
      }
      
      frameRemains = 0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (instruction_part2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        instruction_part2.tStop = t;  // not accounting for scr refresh
        instruction_part2.frameNStop = frameN;  // exact frame index
        // update status
        instruction_part2.status = PsychoJS.Status.FINISHED;
        instruction_part2.setAutoDraw(false);
      }
      
      
      // *continue_button_3* updates
      if (t >= 3 && continue_button_3.status === PsychoJS.Status.NOT_STARTED) {
        // keep track of start time/frame for later
        continue_button_3.tStart = t;  // (not accounting for frame time here)
        continue_button_3.frameNStart = frameN;  // exact frame index
        
        // keyboard checking is just starting
        psychoJS.window.callOnFlip(function() { continue_button_3.clock.reset(); });  // t=0 on next screen flip
        psychoJS.window.callOnFlip(function() { continue_button_3.start(); }); // start on screen flip
        psychoJS.window.callOnFlip(function() { continue_button_3.clearEvents(); });
      }
      frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
      if (continue_button_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
        // keep track of stop time/frame for later
        continue_button_3.tStop = t;  // not accounting for scr refresh
        continue_button_3.frameNStop = frameN;  // exact frame index
        // update status
        continue_button_3.status = PsychoJS.Status.FINISHED;
        frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (continue_button_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          continue_button_3.tStop = t;  // not accounting for scr refresh
          continue_button_3.frameNStop = frameN;  // exact frame index
          // update status
          continue_button_3.status = PsychoJS.Status.FINISHED;
          continue_button_3.status = PsychoJS.Status.FINISHED;
            }
          
        }
        
        // if continue_button_3 is active this frame...
        if (continue_button_3.status === PsychoJS.Status.STARTED) {
          let theseKeys = continue_button_3.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
          _continue_button_3_allKeys = _continue_button_3_allKeys.concat(theseKeys);
          if (_continue_button_3_allKeys.length > 0) {
            continue_button_3.keys = _continue_button_3_allKeys[0].name;  // just the first key pressed
            continue_button_3.rt = _continue_button_3_allKeys[0].rt;
            continue_button_3.duration = _continue_button_3_allKeys[0].duration;
            // a response ends the routine
            continueRoutine = false;
          }
        }
        
        // check for quit (typically the Esc key)
        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
        }
        
        // check if the Routine should terminate
        if (!continueRoutine) {  // a component has requested a forced-end of Routine
          routineForceEnded = true;
          return Scheduler.Event.NEXT;
        }
        
        continueRoutine = false;  // reverts to True if at least one component still running
        for (const thisComponent of instructions_02Components)
          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
            continueRoutine = true;
            break;
          }
        
        // refresh the screen if continuing
        if (continueRoutine) {
          return Scheduler.Event.FLIP_REPEAT;
        } else {
          return Scheduler.Event.NEXT;
        }
      };
    }
    
    function instructions_02RoutineEnd(snapshot) {
      return async function () {
        //--- Ending Routine 'instructions_02' ---
        for (const thisComponent of instructions_02Components) {
          if (typeof thisComponent.setAutoDraw === 'function') {
            thisComponent.setAutoDraw(false);
          }
        }
        psychoJS.experiment.addData('instructions_02.stopped', globalClock.getTime());
        // update the trial handler
        if (currentLoop instanceof MultiStairHandler) {
          currentLoop.addResponse(continue_button_3.corr, level);
        }
        psychoJS.experiment.addData('continue_button_3.keys', continue_button_3.keys);
        if (typeof continue_button_3.keys !== 'undefined') {  // we had a response
            psychoJS.experiment.addData('continue_button_3.rt', continue_button_3.rt);
            psychoJS.experiment.addData('continue_button_3.duration', continue_button_3.duration);
            routineTimer.reset();
            }
        
        continue_button_3.stop();
        // the Routine "instructions_02" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset();
        
        // Routines running outside a loop should always advance the datafile row
        if (currentLoop === psychoJS.experiment) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        return Scheduler.Event.NEXT;
      }
    }
    
    function instructions_03RoutineBegin(snapshot) {
      return async function () {
        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
        
        //--- Prepare to start Routine 'instructions_03' ---
        t = 0;
        frameN = -1;
        continueRoutine = true; // until we're told otherwise
        // keep track of whether this Routine was forcibly ended
        routineForceEnded = false;
        instructions_03Clock.reset();
        routineTimer.reset();
        instructions_03MaxDurationReached = false;
        // update component parameters for each repeat
        // Run 'Begin Routine' code from instruction_part3_text
        if ((language === "english")) {
            instruction_part3.text = "In each learning trial, you start with the current image\nin the sequence. This image is shown at the bottom of the\nscreen. At the top of the screen, you will see three\ndifferent images. Your task is to choose which of these\nimages comes next in the sequence.\n\nPress any key to continue. ";
        }
        if ((language === "german")) {
            instruction_part3.text = "In jedem Lerndurchgang sehen Sie unten das aktuelle Bild\nder Sequenz. Oben werden drei Bilder angezeigt.\n\nW\u00e4hlen Sie das Bild aus, das als N\u00e4chstes in der Sequenz folgt.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
        }
        
        continue_button_4.keys = undefined;
        continue_button_4.rt = undefined;
        _continue_button_4_allKeys = [];
        psychoJS.experiment.addData('instructions_03.started', globalClock.getTime());
        instructions_03MaxDuration = null
        // keep track of which components have finished
        instructions_03Components = [];
        instructions_03Components.push(instruction_part3);
        instructions_03Components.push(continue_button_4);
        
        for (const thisComponent of instructions_03Components)
          if ('status' in thisComponent)
            thisComponent.status = PsychoJS.Status.NOT_STARTED;
        return Scheduler.Event.NEXT;
      }
    }
    
    function instructions_03RoutineEachFrame() {
      return async function () {
        //--- Loop for each frame of Routine 'instructions_03' ---
        // get current time
        t = instructions_03Clock.getTime();
        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
        // update/draw components on each frame
        
        // *instruction_part3* updates
        if (t >= 0 && instruction_part3.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          instruction_part3.tStart = t;  // (not accounting for frame time here)
          instruction_part3.frameNStart = frameN;  // exact frame index
          
          instruction_part3.setAutoDraw(true);
        }
        
        
        // if instruction_part3 is active this frame...
        if (instruction_part3.status === PsychoJS.Status.STARTED) {
        }
        
        frameRemains = 0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (instruction_part3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          instruction_part3.tStop = t;  // not accounting for scr refresh
          instruction_part3.frameNStop = frameN;  // exact frame index
          // update status
          instruction_part3.status = PsychoJS.Status.FINISHED;
          instruction_part3.setAutoDraw(false);
        }
        
        
        // *continue_button_4* updates
        if (t >= 3 && continue_button_4.status === PsychoJS.Status.NOT_STARTED) {
          // keep track of start time/frame for later
          continue_button_4.tStart = t;  // (not accounting for frame time here)
          continue_button_4.frameNStart = frameN;  // exact frame index
          
          // keyboard checking is just starting
          psychoJS.window.callOnFlip(function() { continue_button_4.clock.reset(); });  // t=0 on next screen flip
          psychoJS.window.callOnFlip(function() { continue_button_4.start(); }); // start on screen flip
          psychoJS.window.callOnFlip(function() { continue_button_4.clearEvents(); });
        }
        frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
        if (continue_button_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
          // keep track of stop time/frame for later
          continue_button_4.tStop = t;  // not accounting for scr refresh
          continue_button_4.frameNStop = frameN;  // exact frame index
          // update status
          continue_button_4.status = PsychoJS.Status.FINISHED;
          frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (continue_button_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            continue_button_4.tStop = t;  // not accounting for scr refresh
            continue_button_4.frameNStop = frameN;  // exact frame index
            // update status
            continue_button_4.status = PsychoJS.Status.FINISHED;
            continue_button_4.status = PsychoJS.Status.FINISHED;
              }
            
          }
          
          // if continue_button_4 is active this frame...
          if (continue_button_4.status === PsychoJS.Status.STARTED) {
            let theseKeys = continue_button_4.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
            _continue_button_4_allKeys = _continue_button_4_allKeys.concat(theseKeys);
            if (_continue_button_4_allKeys.length > 0) {
              continue_button_4.keys = _continue_button_4_allKeys[0].name;  // just the first key pressed
              continue_button_4.rt = _continue_button_4_allKeys[0].rt;
              continue_button_4.duration = _continue_button_4_allKeys[0].duration;
              // a response ends the routine
              continueRoutine = false;
            }
          }
          
          // check for quit (typically the Esc key)
          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
          }
          
          // check if the Routine should terminate
          if (!continueRoutine) {  // a component has requested a forced-end of Routine
            routineForceEnded = true;
            return Scheduler.Event.NEXT;
          }
          
          continueRoutine = false;  // reverts to True if at least one component still running
          for (const thisComponent of instructions_03Components)
            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
              continueRoutine = true;
              break;
            }
          
          // refresh the screen if continuing
          if (continueRoutine) {
            return Scheduler.Event.FLIP_REPEAT;
          } else {
            return Scheduler.Event.NEXT;
          }
        };
      }
      
      function instructions_03RoutineEnd(snapshot) {
        return async function () {
          //--- Ending Routine 'instructions_03' ---
          for (const thisComponent of instructions_03Components) {
            if (typeof thisComponent.setAutoDraw === 'function') {
              thisComponent.setAutoDraw(false);
            }
          }
          psychoJS.experiment.addData('instructions_03.stopped', globalClock.getTime());
          // update the trial handler
          if (currentLoop instanceof MultiStairHandler) {
            currentLoop.addResponse(continue_button_4.corr, level);
          }
          psychoJS.experiment.addData('continue_button_4.keys', continue_button_4.keys);
          if (typeof continue_button_4.keys !== 'undefined') {  // we had a response
              psychoJS.experiment.addData('continue_button_4.rt', continue_button_4.rt);
              psychoJS.experiment.addData('continue_button_4.duration', continue_button_4.duration);
              routineTimer.reset();
              }
          
          continue_button_4.stop();
          // the Routine "instructions_03" was not non-slip safe, so reset the non-slip timer
          routineTimer.reset();
          
          // Routines running outside a loop should always advance the datafile row
          if (currentLoop === psychoJS.experiment) {
            psychoJS.experiment.nextEntry(snapshot);
          }
          return Scheduler.Event.NEXT;
        }
      }
      
      function instructions_04RoutineBegin(snapshot) {
        return async function () {
          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
          
          //--- Prepare to start Routine 'instructions_04' ---
          t = 0;
          frameN = -1;
          continueRoutine = true; // until we're told otherwise
          // keep track of whether this Routine was forcibly ended
          routineForceEnded = false;
          instructions_04Clock.reset();
          routineTimer.reset();
          instructions_04MaxDurationReached = false;
          // update component parameters for each repeat
          // Run 'Begin Routine' code from instruction_part4_text
          if ((language === "english")) {
              instruction_part4.text = "Use the left, right, and up keys to select the image in the left, right, or middle position.\n\nThe position of the images on the screen does not indicate their order in the sequence.\nAny image can appear in any position.\n\nPlease do not write down the associations you learn. Try to keep the sequences in your head.\n\nPress any key to continue.";
          }
          if ((language === "german")) {
              instruction_part4.text = "Verwenden Sie die linke gr\u00fcne, die rechte blaue\nund die obere rote Taste, um das linke, rechte oder mittlere\nBild auszuw\u00e4hlen.\n\nDie Position der Bilder auf dem Bildschirm\nhat keine Bedeutung f\u00fcr die Reihenfolge der Sequenz.\nJedes Bild kann an jeder Position erscheinen.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
          }
          
          continue_button_5.keys = undefined;
          continue_button_5.rt = undefined;
          _continue_button_5_allKeys = [];
          psychoJS.experiment.addData('instructions_04.started', globalClock.getTime());
          instructions_04MaxDuration = null
          // keep track of which components have finished
          instructions_04Components = [];
          instructions_04Components.push(instruction_part4);
          instructions_04Components.push(continue_button_5);
          
          for (const thisComponent of instructions_04Components)
            if ('status' in thisComponent)
              thisComponent.status = PsychoJS.Status.NOT_STARTED;
          return Scheduler.Event.NEXT;
        }
      }
      
      function instructions_04RoutineEachFrame() {
        return async function () {
          //--- Loop for each frame of Routine 'instructions_04' ---
          // get current time
          t = instructions_04Clock.getTime();
          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
          // update/draw components on each frame
          
          // *instruction_part4* updates
          if (t >= 0.0 && instruction_part4.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            instruction_part4.tStart = t;  // (not accounting for frame time here)
            instruction_part4.frameNStart = frameN;  // exact frame index
            
            instruction_part4.setAutoDraw(true);
          }
          
          
          // if instruction_part4 is active this frame...
          if (instruction_part4.status === PsychoJS.Status.STARTED) {
          }
          
          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (instruction_part4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            instruction_part4.tStop = t;  // not accounting for scr refresh
            instruction_part4.frameNStop = frameN;  // exact frame index
            // update status
            instruction_part4.status = PsychoJS.Status.FINISHED;
            instruction_part4.setAutoDraw(false);
          }
          
          
          // *continue_button_5* updates
          if (t >= 3 && continue_button_5.status === PsychoJS.Status.NOT_STARTED) {
            // keep track of start time/frame for later
            continue_button_5.tStart = t;  // (not accounting for frame time here)
            continue_button_5.frameNStart = frameN;  // exact frame index
            
            // keyboard checking is just starting
            psychoJS.window.callOnFlip(function() { continue_button_5.clock.reset(); });  // t=0 on next screen flip
            psychoJS.window.callOnFlip(function() { continue_button_5.start(); }); // start on screen flip
            psychoJS.window.callOnFlip(function() { continue_button_5.clearEvents(); });
          }
          frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
          if (continue_button_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
            // keep track of stop time/frame for later
            continue_button_5.tStop = t;  // not accounting for scr refresh
            continue_button_5.frameNStop = frameN;  // exact frame index
            // update status
            continue_button_5.status = PsychoJS.Status.FINISHED;
            frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
            if (continue_button_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
              // keep track of stop time/frame for later
              continue_button_5.tStop = t;  // not accounting for scr refresh
              continue_button_5.frameNStop = frameN;  // exact frame index
              // update status
              continue_button_5.status = PsychoJS.Status.FINISHED;
              continue_button_5.status = PsychoJS.Status.FINISHED;
                }
              
            }
            
            // if continue_button_5 is active this frame...
            if (continue_button_5.status === PsychoJS.Status.STARTED) {
              let theseKeys = continue_button_5.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
              _continue_button_5_allKeys = _continue_button_5_allKeys.concat(theseKeys);
              if (_continue_button_5_allKeys.length > 0) {
                continue_button_5.keys = _continue_button_5_allKeys[0].name;  // just the first key pressed
                continue_button_5.rt = _continue_button_5_allKeys[0].rt;
                continue_button_5.duration = _continue_button_5_allKeys[0].duration;
                // a response ends the routine
                continueRoutine = false;
              }
            }
            
            // check for quit (typically the Esc key)
            if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
              return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
            }
            
            // check if the Routine should terminate
            if (!continueRoutine) {  // a component has requested a forced-end of Routine
              routineForceEnded = true;
              return Scheduler.Event.NEXT;
            }
            
            continueRoutine = false;  // reverts to True if at least one component still running
            for (const thisComponent of instructions_04Components)
              if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                continueRoutine = true;
                break;
              }
            
            // refresh the screen if continuing
            if (continueRoutine) {
              return Scheduler.Event.FLIP_REPEAT;
            } else {
              return Scheduler.Event.NEXT;
            }
          };
        }
        
        function instructions_04RoutineEnd(snapshot) {
          return async function () {
            //--- Ending Routine 'instructions_04' ---
            for (const thisComponent of instructions_04Components) {
              if (typeof thisComponent.setAutoDraw === 'function') {
                thisComponent.setAutoDraw(false);
              }
            }
            psychoJS.experiment.addData('instructions_04.stopped', globalClock.getTime());
            // update the trial handler
            if (currentLoop instanceof MultiStairHandler) {
              currentLoop.addResponse(continue_button_5.corr, level);
            }
            psychoJS.experiment.addData('continue_button_5.keys', continue_button_5.keys);
            if (typeof continue_button_5.keys !== 'undefined') {  // we had a response
                psychoJS.experiment.addData('continue_button_5.rt', continue_button_5.rt);
                psychoJS.experiment.addData('continue_button_5.duration', continue_button_5.duration);
                routineTimer.reset();
                }
            
            continue_button_5.stop();
            // the Routine "instructions_04" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset();
            
            // Routines running outside a loop should always advance the datafile row
            if (currentLoop === psychoJS.experiment) {
              psychoJS.experiment.nextEntry(snapshot);
            }
            return Scheduler.Event.NEXT;
          }
        }
        
        function instructions_05RoutineBegin(snapshot) {
          return async function () {
            TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
            
            //--- Prepare to start Routine 'instructions_05' ---
            t = 0;
            frameN = -1;
            continueRoutine = true; // until we're told otherwise
            // keep track of whether this Routine was forcibly ended
            routineForceEnded = false;
            instructions_05Clock.reset();
            routineTimer.reset();
            instructions_05MaxDurationReached = false;
            // update component parameters for each repeat
            // Run 'Begin Routine' code from instruction_part5_text
            if ((language === "english")) {
                instruction_part5.text = "After you make a choice, you will receive feedback:\nThe correct next image in the sequence will move down \nand replace the current image.\n\nThe next learning trial then starts from this new current image.\n\nPress any key to continue. ";
            }
            if ((language === "german")) {
                instruction_part5.text = "Nach Ihrer Auswahl erhalten Sie Feedback:\nDas richtige n\u00e4chste Bild bewegt sich nach unten\nund wird zum aktuellen Bild f\u00fcr den n\u00e4chsten Lerndurchgang.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
            }
            
            continue_button_6.keys = undefined;
            continue_button_6.rt = undefined;
            _continue_button_6_allKeys = [];
            psychoJS.experiment.addData('instructions_05.started', globalClock.getTime());
            instructions_05MaxDuration = null
            // keep track of which components have finished
            instructions_05Components = [];
            instructions_05Components.push(instruction_part5);
            instructions_05Components.push(continue_button_6);
            
            for (const thisComponent of instructions_05Components)
              if ('status' in thisComponent)
                thisComponent.status = PsychoJS.Status.NOT_STARTED;
            return Scheduler.Event.NEXT;
          }
        }
        
        function instructions_05RoutineEachFrame() {
          return async function () {
            //--- Loop for each frame of Routine 'instructions_05' ---
            // get current time
            t = instructions_05Clock.getTime();
            frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
            // update/draw components on each frame
            
            // *instruction_part5* updates
            if (t >= 0.0 && instruction_part5.status === PsychoJS.Status.NOT_STARTED) {
              // keep track of start time/frame for later
              instruction_part5.tStart = t;  // (not accounting for frame time here)
              instruction_part5.frameNStart = frameN;  // exact frame index
              
              instruction_part5.setAutoDraw(true);
            }
            
            
            // if instruction_part5 is active this frame...
            if (instruction_part5.status === PsychoJS.Status.STARTED) {
            }
            
            frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
            if (instruction_part5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
              // keep track of stop time/frame for later
              instruction_part5.tStop = t;  // not accounting for scr refresh
              instruction_part5.frameNStop = frameN;  // exact frame index
              // update status
              instruction_part5.status = PsychoJS.Status.FINISHED;
              instruction_part5.setAutoDraw(false);
            }
            
            
            // *continue_button_6* updates
            if (t >= 3 && continue_button_6.status === PsychoJS.Status.NOT_STARTED) {
              // keep track of start time/frame for later
              continue_button_6.tStart = t;  // (not accounting for frame time here)
              continue_button_6.frameNStart = frameN;  // exact frame index
              
              // keyboard checking is just starting
              psychoJS.window.callOnFlip(function() { continue_button_6.clock.reset(); });  // t=0 on next screen flip
              psychoJS.window.callOnFlip(function() { continue_button_6.start(); }); // start on screen flip
              psychoJS.window.callOnFlip(function() { continue_button_6.clearEvents(); });
            }
            frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
            if (continue_button_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
              // keep track of stop time/frame for later
              continue_button_6.tStop = t;  // not accounting for scr refresh
              continue_button_6.frameNStop = frameN;  // exact frame index
              // update status
              continue_button_6.status = PsychoJS.Status.FINISHED;
              frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
              if (continue_button_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                // keep track of stop time/frame for later
                continue_button_6.tStop = t;  // not accounting for scr refresh
                continue_button_6.frameNStop = frameN;  // exact frame index
                // update status
                continue_button_6.status = PsychoJS.Status.FINISHED;
                continue_button_6.status = PsychoJS.Status.FINISHED;
                  }
                
              }
              
              // if continue_button_6 is active this frame...
              if (continue_button_6.status === PsychoJS.Status.STARTED) {
                let theseKeys = continue_button_6.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                _continue_button_6_allKeys = _continue_button_6_allKeys.concat(theseKeys);
                if (_continue_button_6_allKeys.length > 0) {
                  continue_button_6.keys = _continue_button_6_allKeys[0].name;  // just the first key pressed
                  continue_button_6.rt = _continue_button_6_allKeys[0].rt;
                  continue_button_6.duration = _continue_button_6_allKeys[0].duration;
                  // a response ends the routine
                  continueRoutine = false;
                }
              }
              
              // check for quit (typically the Esc key)
              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
              }
              
              // check if the Routine should terminate
              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                routineForceEnded = true;
                return Scheduler.Event.NEXT;
              }
              
              continueRoutine = false;  // reverts to True if at least one component still running
              for (const thisComponent of instructions_05Components)
                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                  continueRoutine = true;
                  break;
                }
              
              // refresh the screen if continuing
              if (continueRoutine) {
                return Scheduler.Event.FLIP_REPEAT;
              } else {
                return Scheduler.Event.NEXT;
              }
            };
          }
          
          function instructions_05RoutineEnd(snapshot) {
            return async function () {
              //--- Ending Routine 'instructions_05' ---
              for (const thisComponent of instructions_05Components) {
                if (typeof thisComponent.setAutoDraw === 'function') {
                  thisComponent.setAutoDraw(false);
                }
              }
              psychoJS.experiment.addData('instructions_05.stopped', globalClock.getTime());
              // update the trial handler
              if (currentLoop instanceof MultiStairHandler) {
                currentLoop.addResponse(continue_button_6.corr, level);
              }
              psychoJS.experiment.addData('continue_button_6.keys', continue_button_6.keys);
              if (typeof continue_button_6.keys !== 'undefined') {  // we had a response
                  psychoJS.experiment.addData('continue_button_6.rt', continue_button_6.rt);
                  psychoJS.experiment.addData('continue_button_6.duration', continue_button_6.duration);
                  routineTimer.reset();
                  }
              
              continue_button_6.stop();
              // the Routine "instructions_05" was not non-slip safe, so reset the non-slip timer
              routineTimer.reset();
              
              // Routines running outside a loop should always advance the datafile row
              if (currentLoop === psychoJS.experiment) {
                psychoJS.experiment.nextEntry(snapshot);
              }
              return Scheduler.Event.NEXT;
            }
          }
          
          function instructions_06RoutineBegin(snapshot) {
            return async function () {
              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
              
              //--- Prepare to start Routine 'instructions_06' ---
              t = 0;
              frameN = -1;
              continueRoutine = true; // until we're told otherwise
              // keep track of whether this Routine was forcibly ended
              routineForceEnded = false;
              instructions_06Clock.reset();
              routineTimer.reset();
              instructions_06MaxDurationReached = false;
              // update component parameters for each repeat
              // Run 'Begin Routine' code from instruction_part6_text
              if ((language === "english")) {
                  instruction_part6.text = "Importantly, the image that moves down is always the correct next image, even if you chose incorrectly.\nIn this way, you will learn the entire sequence step by step through trial and error.\n\nPlease respond as quickly and accurately as possible.\n\nPress any key to continue.";
              }
              if ((language === "german")) {
                  instruction_part6.text = "Wichtig: Auch bei einer falschen Antwort bewegt\nsich immer das richtige n\u00e4chste Bild nach unten.\n\nSo lernen Sie die Sequenz schrittweise durch Versuch\nund Irrtum. Antworten Sie bitte so schnell und genau wie m\u00f6glich.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren";
              }
              
              continue_button_7.keys = undefined;
              continue_button_7.rt = undefined;
              _continue_button_7_allKeys = [];
              psychoJS.experiment.addData('instructions_06.started', globalClock.getTime());
              instructions_06MaxDuration = null
              // keep track of which components have finished
              instructions_06Components = [];
              instructions_06Components.push(instruction_part6);
              instructions_06Components.push(continue_button_7);
              
              for (const thisComponent of instructions_06Components)
                if ('status' in thisComponent)
                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
              return Scheduler.Event.NEXT;
            }
          }
          
          function instructions_06RoutineEachFrame() {
            return async function () {
              //--- Loop for each frame of Routine 'instructions_06' ---
              // get current time
              t = instructions_06Clock.getTime();
              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
              // update/draw components on each frame
              
              // *instruction_part6* updates
              if (t >= 0.0 && instruction_part6.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                instruction_part6.tStart = t;  // (not accounting for frame time here)
                instruction_part6.frameNStart = frameN;  // exact frame index
                
                instruction_part6.setAutoDraw(true);
              }
              
              
              // if instruction_part6 is active this frame...
              if (instruction_part6.status === PsychoJS.Status.STARTED) {
              }
              
              frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
              if (instruction_part6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                // keep track of stop time/frame for later
                instruction_part6.tStop = t;  // not accounting for scr refresh
                instruction_part6.frameNStop = frameN;  // exact frame index
                // update status
                instruction_part6.status = PsychoJS.Status.FINISHED;
                instruction_part6.setAutoDraw(false);
              }
              
              
              // *continue_button_7* updates
              if (t >= 3 && continue_button_7.status === PsychoJS.Status.NOT_STARTED) {
                // keep track of start time/frame for later
                continue_button_7.tStart = t;  // (not accounting for frame time here)
                continue_button_7.frameNStart = frameN;  // exact frame index
                
                // keyboard checking is just starting
                psychoJS.window.callOnFlip(function() { continue_button_7.clock.reset(); });  // t=0 on next screen flip
                psychoJS.window.callOnFlip(function() { continue_button_7.start(); }); // start on screen flip
                psychoJS.window.callOnFlip(function() { continue_button_7.clearEvents(); });
              }
              frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
              if (continue_button_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                // keep track of stop time/frame for later
                continue_button_7.tStop = t;  // not accounting for scr refresh
                continue_button_7.frameNStop = frameN;  // exact frame index
                // update status
                continue_button_7.status = PsychoJS.Status.FINISHED;
                frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                if (continue_button_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                  // keep track of stop time/frame for later
                  continue_button_7.tStop = t;  // not accounting for scr refresh
                  continue_button_7.frameNStop = frameN;  // exact frame index
                  // update status
                  continue_button_7.status = PsychoJS.Status.FINISHED;
                  continue_button_7.status = PsychoJS.Status.FINISHED;
                    }
                  
                }
                
                // if continue_button_7 is active this frame...
                if (continue_button_7.status === PsychoJS.Status.STARTED) {
                  let theseKeys = continue_button_7.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                  _continue_button_7_allKeys = _continue_button_7_allKeys.concat(theseKeys);
                  if (_continue_button_7_allKeys.length > 0) {
                    continue_button_7.keys = _continue_button_7_allKeys[0].name;  // just the first key pressed
                    continue_button_7.rt = _continue_button_7_allKeys[0].rt;
                    continue_button_7.duration = _continue_button_7_allKeys[0].duration;
                    // a response ends the routine
                    continueRoutine = false;
                  }
                }
                
                // check for quit (typically the Esc key)
                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                }
                
                // check if the Routine should terminate
                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                  routineForceEnded = true;
                  return Scheduler.Event.NEXT;
                }
                
                continueRoutine = false;  // reverts to True if at least one component still running
                for (const thisComponent of instructions_06Components)
                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                    continueRoutine = true;
                    break;
                  }
                
                // refresh the screen if continuing
                if (continueRoutine) {
                  return Scheduler.Event.FLIP_REPEAT;
                } else {
                  return Scheduler.Event.NEXT;
                }
              };
            }
            
            function instructions_06RoutineEnd(snapshot) {
              return async function () {
                //--- Ending Routine 'instructions_06' ---
                for (const thisComponent of instructions_06Components) {
                  if (typeof thisComponent.setAutoDraw === 'function') {
                    thisComponent.setAutoDraw(false);
                  }
                }
                psychoJS.experiment.addData('instructions_06.stopped', globalClock.getTime());
                // update the trial handler
                if (currentLoop instanceof MultiStairHandler) {
                  currentLoop.addResponse(continue_button_7.corr, level);
                }
                psychoJS.experiment.addData('continue_button_7.keys', continue_button_7.keys);
                if (typeof continue_button_7.keys !== 'undefined') {  // we had a response
                    psychoJS.experiment.addData('continue_button_7.rt', continue_button_7.rt);
                    psychoJS.experiment.addData('continue_button_7.duration', continue_button_7.duration);
                    routineTimer.reset();
                    }
                
                continue_button_7.stop();
                // the Routine "instructions_06" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset();
                
                // Routines running outside a loop should always advance the datafile row
                if (currentLoop === psychoJS.experiment) {
                  psychoJS.experiment.nextEntry(snapshot);
                }
                return Scheduler.Event.NEXT;
              }
            }
            
            function instructions_replay_breakRoutineBegin(snapshot) {
              return async function () {
                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                
                //--- Prepare to start Routine 'instructions_replay_break' ---
                t = 0;
                frameN = -1;
                continueRoutine = true; // until we're told otherwise
                // keep track of whether this Routine was forcibly ended
                routineForceEnded = false;
                instructions_replay_breakClock.reset();
                routineTimer.reset();
                instructions_replay_breakMaxDurationReached = false;
                // update component parameters for each repeat
                // Run 'Begin Routine' code from instruction_part16_text
                if ((language === "english")) {
                    instructions_part16.text = "After each learning run, there will be short waiting periods, in which you will see a fixation cross.\nThese periods are not a break. Please just wait for a short moment, but don't take a break.\n\nPress any key to start practicing the learning trials";
                }
                if ((language === "german")) {
                    instructions_part16.text = "Nach jedem Lerndurchlauf erscheint f\u00fcr kurze Zeit\nein Fixationskreuz.\n\nDiese Wartezeit ist keine Pause.\nBitte bleiben Sie weiterhin ruhig sitzen und schauen\nSie auf das Fixationskreuz.\n\nDr\u00fccken Sie eine beliebige Taste, um das Lernen zu \u00fcben.";
                }
                
                continue_button_22.keys = undefined;
                continue_button_22.rt = undefined;
                _continue_button_22_allKeys = [];
                psychoJS.experiment.addData('instructions_replay_break.started', globalClock.getTime());
                instructions_replay_breakMaxDuration = null
                // keep track of which components have finished
                instructions_replay_breakComponents = [];
                instructions_replay_breakComponents.push(instructions_part16);
                instructions_replay_breakComponents.push(continue_button_22);
                
                for (const thisComponent of instructions_replay_breakComponents)
                  if ('status' in thisComponent)
                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                return Scheduler.Event.NEXT;
              }
            }
            
            function instructions_replay_breakRoutineEachFrame() {
              return async function () {
                //--- Loop for each frame of Routine 'instructions_replay_break' ---
                // get current time
                t = instructions_replay_breakClock.getTime();
                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                // update/draw components on each frame
                
                // *instructions_part16* updates
                if (t >= 0.0 && instructions_part16.status === PsychoJS.Status.NOT_STARTED) {
                  // keep track of start time/frame for later
                  instructions_part16.tStart = t;  // (not accounting for frame time here)
                  instructions_part16.frameNStart = frameN;  // exact frame index
                  
                  instructions_part16.setAutoDraw(true);
                }
                
                
                // if instructions_part16 is active this frame...
                if (instructions_part16.status === PsychoJS.Status.STARTED) {
                }
                
                frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                if (instructions_part16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                  // keep track of stop time/frame for later
                  instructions_part16.tStop = t;  // not accounting for scr refresh
                  instructions_part16.frameNStop = frameN;  // exact frame index
                  // update status
                  instructions_part16.status = PsychoJS.Status.FINISHED;
                  instructions_part16.setAutoDraw(false);
                }
                
                
                // *continue_button_22* updates
                if (t >= 1 && continue_button_22.status === PsychoJS.Status.NOT_STARTED) {
                  // keep track of start time/frame for later
                  continue_button_22.tStart = t;  // (not accounting for frame time here)
                  continue_button_22.frameNStart = frameN;  // exact frame index
                  
                  // keyboard checking is just starting
                  psychoJS.window.callOnFlip(function() { continue_button_22.clock.reset(); });  // t=0 on next screen flip
                  psychoJS.window.callOnFlip(function() { continue_button_22.start(); }); // start on screen flip
                  psychoJS.window.callOnFlip(function() { continue_button_22.clearEvents(); });
                }
                frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                if (continue_button_22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                  // keep track of stop time/frame for later
                  continue_button_22.tStop = t;  // not accounting for scr refresh
                  continue_button_22.frameNStop = frameN;  // exact frame index
                  // update status
                  continue_button_22.status = PsychoJS.Status.FINISHED;
                  frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (continue_button_22.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    continue_button_22.tStop = t;  // not accounting for scr refresh
                    continue_button_22.frameNStop = frameN;  // exact frame index
                    // update status
                    continue_button_22.status = PsychoJS.Status.FINISHED;
                    continue_button_22.status = PsychoJS.Status.FINISHED;
                      }
                    
                  }
                  
                  // if continue_button_22 is active this frame...
                  if (continue_button_22.status === PsychoJS.Status.STARTED) {
                    let theseKeys = continue_button_22.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                    _continue_button_22_allKeys = _continue_button_22_allKeys.concat(theseKeys);
                    if (_continue_button_22_allKeys.length > 0) {
                      continue_button_22.keys = _continue_button_22_allKeys[0].name;  // just the first key pressed
                      continue_button_22.rt = _continue_button_22_allKeys[0].rt;
                      continue_button_22.duration = _continue_button_22_allKeys[0].duration;
                      // a response ends the routine
                      continueRoutine = false;
                    }
                  }
                  
                  // check for quit (typically the Esc key)
                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                  }
                  
                  // check if the Routine should terminate
                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                    routineForceEnded = true;
                    return Scheduler.Event.NEXT;
                  }
                  
                  continueRoutine = false;  // reverts to True if at least one component still running
                  for (const thisComponent of instructions_replay_breakComponents)
                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                      continueRoutine = true;
                      break;
                    }
                  
                  // refresh the screen if continuing
                  if (continueRoutine) {
                    return Scheduler.Event.FLIP_REPEAT;
                  } else {
                    return Scheduler.Event.NEXT;
                  }
                };
              }
              
              function instructions_replay_breakRoutineEnd(snapshot) {
                return async function () {
                  //--- Ending Routine 'instructions_replay_break' ---
                  for (const thisComponent of instructions_replay_breakComponents) {
                    if (typeof thisComponent.setAutoDraw === 'function') {
                      thisComponent.setAutoDraw(false);
                    }
                  }
                  psychoJS.experiment.addData('instructions_replay_break.stopped', globalClock.getTime());
                  // update the trial handler
                  if (currentLoop instanceof MultiStairHandler) {
                    currentLoop.addResponse(continue_button_22.corr, level);
                  }
                  psychoJS.experiment.addData('continue_button_22.keys', continue_button_22.keys);
                  if (typeof continue_button_22.keys !== 'undefined') {  // we had a response
                      psychoJS.experiment.addData('continue_button_22.rt', continue_button_22.rt);
                      psychoJS.experiment.addData('continue_button_22.duration', continue_button_22.duration);
                      routineTimer.reset();
                      }
                  
                  continue_button_22.stop();
                  // the Routine "instructions_replay_break" was not non-slip safe, so reset the non-slip timer
                  routineTimer.reset();
                  
                  // Routines running outside a loop should always advance the datafile row
                  if (currentLoop === psychoJS.experiment) {
                    psychoJS.experiment.nextEntry(snapshot);
                  }
                  return Scheduler.Event.NEXT;
                }
              }
              
              function practice_learningLoopBegin(practice_learningLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  practice_learning = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: 'sequences/main_trials_prc.xlsx',
                    seed: undefined, name: 'practice_learning'
                  });
                  psychoJS.experiment.addLoop(practice_learning); // add the loop to the experiment
                  currentLoop = practice_learning;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisPractice_learning of practice_learning) {
                    snapshot = practice_learning.getSnapshot();
                    practice_learningLoopScheduler.add(importConditions(snapshot));
                    practice_learningLoopScheduler.add(practice_choice_displayRoutineBegin(snapshot));
                    practice_learningLoopScheduler.add(practice_choice_displayRoutineEachFrame());
                    practice_learningLoopScheduler.add(practice_choice_displayRoutineEnd(snapshot));
                    practice_learningLoopScheduler.add(practice_feedbackRoutineBegin(snapshot));
                    practice_learningLoopScheduler.add(practice_feedbackRoutineEachFrame());
                    practice_learningLoopScheduler.add(practice_feedbackRoutineEnd(snapshot));
                    practice_learningLoopScheduler.add(practice_learningLoopEndIteration(practice_learningLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              async function practice_learningLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(practice_learning);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function practice_learningLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    } else {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              function retrieval_prc_loopLoopBegin(retrieval_prc_loopLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  retrieval_prc_loop = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: 'sequences/retr_trials_prc_03.xlsx',
                    seed: undefined, name: 'retrieval_prc_loop'
                  });
                  psychoJS.experiment.addLoop(retrieval_prc_loop); // add the loop to the experiment
                  currentLoop = retrieval_prc_loop;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisRetrieval_prc_loop of retrieval_prc_loop) {
                    snapshot = retrieval_prc_loop.getSnapshot();
                    retrieval_prc_loopLoopScheduler.add(importConditions(snapshot));
                    const retry_loopLoopScheduler = new Scheduler(psychoJS);
                    retrieval_prc_loopLoopScheduler.add(retry_loopLoopBegin(retry_loopLoopScheduler, snapshot));
                    retrieval_prc_loopLoopScheduler.add(retry_loopLoopScheduler);
                    retrieval_prc_loopLoopScheduler.add(retry_loopLoopEnd);
                    retrieval_prc_loopLoopScheduler.add(retrieval_prc_loopLoopEndIteration(retrieval_prc_loopLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              function retry_loopLoopBegin(retry_loopLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  retry_loop = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 999, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: undefined,
                    seed: undefined, name: 'retry_loop'
                  });
                  psychoJS.experiment.addLoop(retry_loop); // add the loop to the experiment
                  currentLoop = retry_loop;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisRetry_loop of retry_loop) {
                    snapshot = retry_loop.getSnapshot();
                    retry_loopLoopScheduler.add(importConditions(snapshot));
                    retry_loopLoopScheduler.add(retrieval_type1_practiceRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(retrieval_type1_practiceRoutineEachFrame());
                    retry_loopLoopScheduler.add(retrieval_type1_practiceRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(first_image_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(first_image_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(first_image_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(mask_retr1_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(mask_retr1_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(mask_retr1_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(second_image_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(second_image_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(second_image_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(mask_retr2_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(mask_retr2_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(mask_retr2_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(reflection_periodRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(reflection_periodRoutineEachFrame());
                    retry_loopLoopScheduler.add(reflection_periodRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(retr_response_order_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(retr_response_order_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(retr_response_order_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(retr_response_distance_prcRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(retr_response_distance_prcRoutineEachFrame());
                    retry_loopLoopScheduler.add(retr_response_distance_prcRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(retr_response_feedbackRoutineBegin(snapshot));
                    retry_loopLoopScheduler.add(retr_response_feedbackRoutineEachFrame());
                    retry_loopLoopScheduler.add(retr_response_feedbackRoutineEnd(snapshot));
                    retry_loopLoopScheduler.add(retry_loopLoopEndIteration(retry_loopLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              async function retry_loopLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(retry_loop);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function retry_loopLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              async function retrieval_prc_loopLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(retrieval_prc_loop);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function retrieval_prc_loopLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    } else {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              function BlockLoopBegin(BlockLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  Block = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: 'sequences/block_conditions.xlsx',
                    seed: undefined, name: 'Block'
                  });
                  psychoJS.experiment.addLoop(Block); // add the loop to the experiment
                  currentLoop = Block;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisBlock of Block) {
                    snapshot = Block.getSnapshot();
                    BlockLoopScheduler.add(importConditions(snapshot));
                    BlockLoopScheduler.add(reset_rows_to_selectRoutineBegin(snapshot));
                    BlockLoopScheduler.add(reset_rows_to_selectRoutineEachFrame());
                    BlockLoopScheduler.add(reset_rows_to_selectRoutineEnd(snapshot));
                    const miniblocksLoopScheduler = new Scheduler(psychoJS);
                    BlockLoopScheduler.add(miniblocksLoopBegin(miniblocksLoopScheduler, snapshot));
                    BlockLoopScheduler.add(miniblocksLoopScheduler);
                    BlockLoopScheduler.add(miniblocksLoopEnd);
                    BlockLoopScheduler.add(BlockLoopEndIteration(BlockLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              function miniblocksLoopBegin(miniblocksLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  miniblocks = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: n_routes_block, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: undefined,
                    seed: undefined, name: 'miniblocks'
                  });
                  psychoJS.experiment.addLoop(miniblocks); // add the loop to the experiment
                  currentLoop = miniblocks;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisMiniblock of miniblocks) {
                    snapshot = miniblocks.getSnapshot();
                    miniblocksLoopScheduler.add(importConditions(snapshot));
                    miniblocksLoopScheduler.add(set_learning_rowsRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(set_learning_rowsRoutineEachFrame());
                    miniblocksLoopScheduler.add(set_learning_rowsRoutineEnd(snapshot));
                    miniblocksLoopScheduler.add(show_contextRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(show_contextRoutineEachFrame());
                    miniblocksLoopScheduler.add(show_contextRoutineEnd(snapshot));
                    const learning_trialsLoopScheduler = new Scheduler(psychoJS);
                    miniblocksLoopScheduler.add(learning_trialsLoopBegin(learning_trialsLoopScheduler, snapshot));
                    miniblocksLoopScheduler.add(learning_trialsLoopScheduler);
                    miniblocksLoopScheduler.add(learning_trialsLoopEnd);
                    miniblocksLoopScheduler.add(rest_periodRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(rest_periodRoutineEachFrame());
                    miniblocksLoopScheduler.add(rest_periodRoutineEnd(snapshot));
                    miniblocksLoopScheduler.add(instruction_retr_startRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(instruction_retr_startRoutineEachFrame());
                    miniblocksLoopScheduler.add(instruction_retr_startRoutineEnd(snapshot));
                    miniblocksLoopScheduler.add(set_retrieval_rowsRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(set_retrieval_rowsRoutineEachFrame());
                    miniblocksLoopScheduler.add(set_retrieval_rowsRoutineEnd(snapshot));
                    const retrieval_trialsLoopScheduler = new Scheduler(psychoJS);
                    miniblocksLoopScheduler.add(retrieval_trialsLoopBegin(retrieval_trialsLoopScheduler, snapshot));
                    miniblocksLoopScheduler.add(retrieval_trialsLoopScheduler);
                    miniblocksLoopScheduler.add(retrieval_trialsLoopEnd);
                    miniblocksLoopScheduler.add(retr_task_breakRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(retr_task_breakRoutineEachFrame());
                    miniblocksLoopScheduler.add(retr_task_breakRoutineEnd(snapshot));
                    miniblocksLoopScheduler.add(instructions_new_learnRoutineBegin(snapshot));
                    miniblocksLoopScheduler.add(instructions_new_learnRoutineEachFrame());
                    miniblocksLoopScheduler.add(instructions_new_learnRoutineEnd(snapshot));
                    miniblocksLoopScheduler.add(miniblocksLoopEndIteration(miniblocksLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              function learning_trialsLoopBegin(learning_trialsLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  learning_trials = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_learning, selected_rows),
                    seed: undefined, name: 'learning_trials'
                  });
                  psychoJS.experiment.addLoop(learning_trials); // add the loop to the experiment
                  currentLoop = learning_trials;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisLearning_trial of learning_trials) {
                    snapshot = learning_trials.getSnapshot();
                    learning_trialsLoopScheduler.add(importConditions(snapshot));
                    learning_trialsLoopScheduler.add(choice_displayRoutineBegin(snapshot));
                    learning_trialsLoopScheduler.add(choice_displayRoutineEachFrame());
                    learning_trialsLoopScheduler.add(choice_displayRoutineEnd(snapshot));
                    learning_trialsLoopScheduler.add(feedbackRoutineBegin(snapshot));
                    learning_trialsLoopScheduler.add(feedbackRoutineEachFrame());
                    learning_trialsLoopScheduler.add(feedbackRoutineEnd(snapshot));
                    learning_trialsLoopScheduler.add(too_slow_routineRoutineBegin(snapshot));
                    learning_trialsLoopScheduler.add(too_slow_routineRoutineEachFrame());
                    learning_trialsLoopScheduler.add(too_slow_routineRoutineEnd(snapshot));
                    learning_trialsLoopScheduler.add(learning_trialsLoopEndIteration(learning_trialsLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              async function learning_trialsLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(learning_trials);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function learning_trialsLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    } else {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              function retrieval_trialsLoopBegin(retrieval_trialsLoopScheduler, snapshot) {
                return async function() {
                  TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
                  
                  // set up handler to look after randomisation of conditions etc
                  retrieval_trials = new TrialHandler({
                    psychoJS: psychoJS,
                    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
                    extraInfo: expInfo, originPath: undefined,
                    trialList: TrialHandler.importConditions(psychoJS.serverManager, cond_file_retrieval, selected_rows[0:(- 1):2]),
                    seed: undefined, name: 'retrieval_trials'
                  });
                  psychoJS.experiment.addLoop(retrieval_trials); // add the loop to the experiment
                  currentLoop = retrieval_trials;  // we're now the current loop
                  
                  // Schedule all the trials in the trialList:
                  for (const thisRetrieval_trial of retrieval_trials) {
                    snapshot = retrieval_trials.getSnapshot();
                    retrieval_trialsLoopScheduler.add(importConditions(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_ITIRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_ITIRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(retr_ITIRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(first_imageRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(first_imageRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(first_imageRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(mask_retr1RoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(mask_retr1RoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(mask_retr1RoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(second_imageRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(second_imageRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(second_imageRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(mask_retr2RoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(mask_retr2RoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(mask_retr2RoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(reflection_period_retrRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(reflection_period_retrRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(reflection_period_retrRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_response_orderRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_response_orderRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(retr_response_orderRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(too_slow_routine_1RoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(too_slow_routine_1RoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(too_slow_routine_1RoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_response_distanceRoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(retr_response_distanceRoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(retr_response_distanceRoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(too_slow_routine_2RoutineBegin(snapshot));
                    retrieval_trialsLoopScheduler.add(too_slow_routine_2RoutineEachFrame());
                    retrieval_trialsLoopScheduler.add(too_slow_routine_2RoutineEnd(snapshot));
                    retrieval_trialsLoopScheduler.add(retrieval_trialsLoopEndIteration(retrieval_trialsLoopScheduler, snapshot));
                  }
                  
                  return Scheduler.Event.NEXT;
                }
              }
              
              async function retrieval_trialsLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(retrieval_trials);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function retrieval_trialsLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    } else {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              async function miniblocksLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(miniblocks);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function miniblocksLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              async function BlockLoopEnd() {
                // terminate loop
                psychoJS.experiment.removeLoop(Block);
                // update the current loop from the ExperimentHandler
                if (psychoJS.experiment._unfinishedLoops.length>0)
                  currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
                else
                  currentLoop = psychoJS.experiment;  // so we use addData from the experiment
                return Scheduler.Event.NEXT;
              }
              
              function BlockLoopEndIteration(scheduler, snapshot) {
                // ------Prepare for next entry------
                return async function () {
                  if (typeof snapshot !== 'undefined') {
                    // ------Check if user ended loop early------
                    if (snapshot.finished) {
                      // Check for and save orphaned data
                      if (psychoJS.experiment.isEntryEmpty()) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      scheduler.stop();
                    }
                  return Scheduler.Event.NEXT;
                  }
                };
              }
              
              function practice_choice_displayRoutineBegin(snapshot) {
                return async function () {
                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                  
                  //--- Prepare to start Routine 'practice_choice_display' ---
                  t = 0;
                  frameN = -1;
                  continueRoutine = true; // until we're told otherwise
                  // keep track of whether this Routine was forcibly ended
                  routineForceEnded = false;
                  practice_choice_displayClock.reset();
                  routineTimer.reset();
                  practice_choice_displayMaxDurationReached = false;
                  // update component parameters for each repeat
                  // Run 'Begin Routine' code from Init_routeClock
                  
                  window.practice_choice_displayMaxDuration = null; 
                  window.practice_choice_displayComponents = null; 
                  window._key_resp_2_allKeys = null; 
                  window.frameRemains = null;
                  
                  window.routClock = new util.Clock();
                  window.routClock.reset();
                  
                  //if (loop_not_correct.thisN !== 0) {
                  //    practice_errors = 0;
                  //}
                  polygon.setOpacity(0.0);
                  polygon.setPos([0, 0]);
                  prompt_prc.setPos(prompt_pos);
                  prompt_prc.setImage(promptFile);
                  dist_01_prc.setPos(resolve_pos(dist01_pos));
                  dist_01_prc.setImage(dist_01File);
                  dist_02_prc.setPos(resolve_pos(dist02_pos));
                  dist_02_prc.setImage(dist_02File);
                  correct_prc.setPos(resolve_pos(correct_pos));
                  correct_prc.setImage(correctFile);
                  key_resp_2.keys = undefined;
                  key_resp_2.rt = undefined;
                  _key_resp_2_allKeys = [];
                  // Run 'Begin Routine' code from get_response_parameters_3
                  window.responded = false;
                  
                  window.delayClock = null;
                  
                  // Begin Routine
                  window.delayDone = false;
                  window.chosenPos = null;
                  
                  // Run 'Begin Routine' code from set_instructions_choose_2
                  if ((language === "english")) {
                      instructions_choose_2.text = "Choose the next image in the sequence with the keys. ";
                  }
                  if ((language === "german")) {
                      instructions_choose_2.text = "W\u00e4hlen Sie das n\u00e4chste Bild in der Sequenz.";
                  }
                  
                  psychoJS.experiment.addData('practice_choice_display.started', globalClock.getTime());
                  practice_choice_displayMaxDuration = null
                  // keep track of which components have finished
                  practice_choice_displayComponents = [];
                  practice_choice_displayComponents.push(polygon);
                  practice_choice_displayComponents.push(prompt_prc);
                  practice_choice_displayComponents.push(dist_01_prc);
                  practice_choice_displayComponents.push(dist_02_prc);
                  practice_choice_displayComponents.push(correct_prc);
                  practice_choice_displayComponents.push(key_resp_2);
                  practice_choice_displayComponents.push(instructions_choose_2);
                  
                  for (const thisComponent of practice_choice_displayComponents)
                    if ('status' in thisComponent)
                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                  return Scheduler.Event.NEXT;
                }
              }
              
              function practice_choice_displayRoutineEachFrame() {
                return async function () {
                  //--- Loop for each frame of Routine 'practice_choice_display' ---
                  // get current time
                  t = practice_choice_displayClock.getTime();
                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                  // update/draw components on each frame
                  
                  // *polygon* updates
                  if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
                    // update params
                    polygon.setFillColor(new util.Color([0.0, 0.0, 0.0]), false);
                    polygon.setLineColor(new util.Color([0.0039, 0.0039, 0.0039]), false);
                    // keep track of start time/frame for later
                    polygon.tStart = t;  // (not accounting for frame time here)
                    polygon.frameNStart = frameN;  // exact frame index
                    
                    polygon.setAutoDraw(true);
                  }
                  
                  
                  // if polygon is active this frame...
                  if (polygon.status === PsychoJS.Status.STARTED) {
                    // update params
                    polygon.setFillColor(new util.Color([0.0, 0.0, 0.0]), false);
                    polygon.setLineColor(new util.Color([0.0039, 0.0039, 0.0039]), false);
                  }
                  
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    polygon.tStop = t;  // not accounting for scr refresh
                    polygon.frameNStop = frameN;  // exact frame index
                    // update status
                    polygon.status = PsychoJS.Status.FINISHED;
                    polygon.setAutoDraw(false);
                  }
                  
                  
                  // *prompt_prc* updates
                  if (t >= 0.0 && prompt_prc.status === PsychoJS.Status.NOT_STARTED) {
                    // keep track of start time/frame for later
                    prompt_prc.tStart = t;  // (not accounting for frame time here)
                    prompt_prc.frameNStart = frameN;  // exact frame index
                    
                    prompt_prc.setAutoDraw(true);
                  }
                  
                  
                  // if prompt_prc is active this frame...
                  if (prompt_prc.status === PsychoJS.Status.STARTED) {
                  }
                  
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (prompt_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    prompt_prc.tStop = t;  // not accounting for scr refresh
                    prompt_prc.frameNStop = frameN;  // exact frame index
                    // update status
                    prompt_prc.status = PsychoJS.Status.FINISHED;
                    prompt_prc.setAutoDraw(false);
                  }
                  
                  
                  // *dist_01_prc* updates
                  if (t >= 0.0 && dist_01_prc.status === PsychoJS.Status.NOT_STARTED) {
                    // keep track of start time/frame for later
                    dist_01_prc.tStart = t;  // (not accounting for frame time here)
                    dist_01_prc.frameNStart = frameN;  // exact frame index
                    
                    dist_01_prc.setAutoDraw(true);
                  }
                  
                  
                  // if dist_01_prc is active this frame...
                  if (dist_01_prc.status === PsychoJS.Status.STARTED) {
                  }
                  
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (dist_01_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    dist_01_prc.tStop = t;  // not accounting for scr refresh
                    dist_01_prc.frameNStop = frameN;  // exact frame index
                    // update status
                    dist_01_prc.status = PsychoJS.Status.FINISHED;
                    dist_01_prc.setAutoDraw(false);
                  }
                  
                  
                  // *dist_02_prc* updates
                  if (t >= 0.0 && dist_02_prc.status === PsychoJS.Status.NOT_STARTED) {
                    // keep track of start time/frame for later
                    dist_02_prc.tStart = t;  // (not accounting for frame time here)
                    dist_02_prc.frameNStart = frameN;  // exact frame index
                    
                    dist_02_prc.setAutoDraw(true);
                  }
                  
                  
                  // if dist_02_prc is active this frame...
                  if (dist_02_prc.status === PsychoJS.Status.STARTED) {
                  }
                  
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (dist_02_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    dist_02_prc.tStop = t;  // not accounting for scr refresh
                    dist_02_prc.frameNStop = frameN;  // exact frame index
                    // update status
                    dist_02_prc.status = PsychoJS.Status.FINISHED;
                    dist_02_prc.setAutoDraw(false);
                  }
                  
                  
                  // *correct_prc* updates
                  if (t >= 0.0 && correct_prc.status === PsychoJS.Status.NOT_STARTED) {
                    // keep track of start time/frame for later
                    correct_prc.tStart = t;  // (not accounting for frame time here)
                    correct_prc.frameNStart = frameN;  // exact frame index
                    
                    correct_prc.setAutoDraw(true);
                  }
                  
                  
                  // if correct_prc is active this frame...
                  if (correct_prc.status === PsychoJS.Status.STARTED) {
                  }
                  
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (correct_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    correct_prc.tStop = t;  // not accounting for scr refresh
                    correct_prc.frameNStop = frameN;  // exact frame index
                    // update status
                    correct_prc.status = PsychoJS.Status.FINISHED;
                    correct_prc.setAutoDraw(false);
                  }
                  
                  
                  // *key_resp_2* updates
                  if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
                    // keep track of start time/frame for later
                    key_resp_2.tStart = t;  // (not accounting for frame time here)
                    key_resp_2.frameNStart = frameN;  // exact frame index
                    
                    // keyboard checking is just starting
                    key_resp_2.clock.reset();
                    key_resp_2.start();
                    key_resp_2.clearEvents();
                  }
                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                  if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                    // keep track of stop time/frame for later
                    key_resp_2.tStop = t;  // not accounting for scr refresh
                    key_resp_2.frameNStop = frameN;  // exact frame index
                    // update status
                    key_resp_2.status = PsychoJS.Status.FINISHED;
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      key_resp_2.tStop = t;  // not accounting for scr refresh
                      key_resp_2.frameNStop = frameN;  // exact frame index
                      // update status
                      key_resp_2.status = PsychoJS.Status.FINISHED;
                      key_resp_2.status = PsychoJS.Status.FINISHED;
                        }
                      
                    }
                    
                    // if key_resp_2 is active this frame...
                    if (key_resp_2.status === PsychoJS.Status.STARTED) {
                      let theseKeys = key_resp_2.getKeys({keyList: [left_key,right_key,center_key], waitRelease: true});
                      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
                      if (_key_resp_2_allKeys.length > 0) {
                        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
                        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
                        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
                      }
                    }
                    
                    // Run 'Each Frame' code from get_response_parameters_3
                    
                    
                    if (!responded) {
                      //let key_list = key_resp_2.getKeys({ keyList: ["left", "right", "up"], waitRelease: false });
                      
                      if (key_list.length > 0) {
                        responded = true;
                        let thisResp = key_list[0];
                        key_resp_2.keys = thisResp.name;
                        key_resp_2.rt = thisResp.rt;
                        key_resp_2.corr = (thisResp.name === correct_ans) ? 1 : 0;
                    
                        if (thisResp.name === window.left_key)        chosenPos = window.left_pos;
                        else if (thisResp.name === window.right_key)  chosenPos = window.right_pos;
                        else if (thisResp.name === window.center_key) chosenPos = window.center_pos;
                        
                        key_resp_2.stop()
                        polygon.setPos(chosenPos);
                        polygon.setOpacity(1.0);
                        
                        // change color of polygon for correct responses
                        if (key_resp_2.corr === 1) {
                          window.polygonCol = [0, 1, 0];
                          polygon.setFillColor(new util.Color(window.polygonCol));
                          polygon.setLineColor(new util.Color(window.polygonCol));
                        } else if (key_resp_2.corr === 0) {
                          window.polygonCol = [1, -1, -1];
                    
                          polygon.setFillColor(new util.Color(window.polygonCol));
                          polygon.setLineColor(new util.Color(window.polygonCol));
                        } else  {
                          window.polygonCol = [0, 0, 0];
                    
                          polygon.setFillColor(new util.Color(window.polygonCol));
                          polygon.setLineColor(new util.Color(window.polygonCol));
                        }
                            
                        delayClock = new util.Clock();
                      }
                    }
                    
                    if (responded && !delayDone && delayClock !== null && delayClock.getTime() >= 0.1) {
                      delayDone = true;
                      continueRoutine = false;
                    }
                    
                    // *instructions_choose_2* updates
                    if (t >= 0.0 && instructions_choose_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      instructions_choose_2.tStart = t;  // (not accounting for frame time here)
                      instructions_choose_2.frameNStart = frameN;  // exact frame index
                      
                      instructions_choose_2.setAutoDraw(true);
                    }
                    
                    
                    // if instructions_choose_2 is active this frame...
                    if (instructions_choose_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (instructions_choose_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      instructions_choose_2.tStop = t;  // not accounting for scr refresh
                      instructions_choose_2.frameNStop = frameN;  // exact frame index
                      // update status
                      instructions_choose_2.status = PsychoJS.Status.FINISHED;
                      instructions_choose_2.setAutoDraw(false);
                    }
                    
                    // check for quit (typically the Esc key)
                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                    }
                    
                    // check if the Routine should terminate
                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                      routineForceEnded = true;
                      return Scheduler.Event.NEXT;
                    }
                    
                    continueRoutine = false;  // reverts to True if at least one component still running
                    for (const thisComponent of practice_choice_displayComponents)
                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                        continueRoutine = true;
                        break;
                      }
                    
                    // refresh the screen if continuing
                    if (continueRoutine) {
                      return Scheduler.Event.FLIP_REPEAT;
                    } else {
                      return Scheduler.Event.NEXT;
                    }
                  };
                }
                
                function practice_choice_displayRoutineEnd(snapshot) {
                  return async function () {
                    //--- Ending Routine 'practice_choice_display' ---
                    for (const thisComponent of practice_choice_displayComponents) {
                      if (typeof thisComponent.setAutoDraw === 'function') {
                        thisComponent.setAutoDraw(false);
                      }
                    }
                    psychoJS.experiment.addData('practice_choice_display.stopped', globalClock.getTime());
                    // update the trial handler
                    if (currentLoop instanceof MultiStairHandler) {
                      currentLoop.addResponse(key_resp_2.corr, level);
                    }
                    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
                    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
                        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
                        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
                        }
                    
                    key_resp_2.stop();
                    // the Routine "practice_choice_display" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset();
                    
                    // Routines running outside a loop should always advance the datafile row
                    if (currentLoop === psychoJS.experiment) {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function practice_feedbackRoutineBegin(snapshot) {
                  return async function () {
                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                    
                    //--- Prepare to start Routine 'practice_feedback' ---
                    t = 0;
                    frameN = -1;
                    continueRoutine = true; // until we're told otherwise
                    // keep track of whether this Routine was forcibly ended
                    routineForceEnded = false;
                    practice_feedbackClock.reset();
                    routineTimer.reset();
                    practice_feedbackMaxDurationReached = false;
                    // update component parameters for each repeat
                    // Run 'Begin Routine' code from control__polygon
                    polygon_7.setOpacity(0.0)
                    if chosenPos:
                        polygon_7.setPos(chosenPos)
                        polygon_7.setOpacity(1.0)
                        polygon_7.setFillColor(polygonCol)
                        polygon_7.setLineColor(polygonCol)
                    // Run 'Begin Routine' code from animation_control_js
                    // Initialize animation control
                    
                    window.endY = prompt_pos[1];   // end y-coord of moving image
                    window.endX = prompt_pos[0];   // end x-coord of moving image
                    
                    window.maxAnimationDur = Math.round(animation_time * expInfo.frameRate);
                    window.animationTimer = 0;      // initialize variable
                    window.animationDone = false;  // initialize variable
                    window.moveCorrect = false;    // initialize variable
                    
                    prompt_prc_2.setPos(prompt_pos);
                    prompt_prc_2.setImage(promptFile);
                    dist_01_prc_2.setPos(resolve_pos(dist01_pos));
                    dist_01_prc_2.setImage(dist_01File);
                    dist_02_prc_2.setPos(resolve_pos(dist02_pos));
                    dist_02_prc_2.setImage(dist_02File);
                    correct_prc_2.setPos(resolve_pos(correct_pos));
                    correct_prc_2.setImage(correctFile);
                    psychoJS.experiment.addData('practice_feedback.started', globalClock.getTime());
                    practice_feedbackMaxDuration = null
                    // keep track of which components have finished
                    practice_feedbackComponents = [];
                    practice_feedbackComponents.push(polygon_7);
                    practice_feedbackComponents.push(prompt_prc_2);
                    practice_feedbackComponents.push(dist_01_prc_2);
                    practice_feedbackComponents.push(dist_02_prc_2);
                    practice_feedbackComponents.push(correct_prc_2);
                    
                    for (const thisComponent of practice_feedbackComponents)
                      if ('status' in thisComponent)
                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function practice_feedbackRoutineEachFrame() {
                  return async function () {
                    //--- Loop for each frame of Routine 'practice_feedback' ---
                    // get current time
                    t = practice_feedbackClock.getTime();
                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                    // update/draw components on each frame
                    // Run 'Each Frame' code from animation_control_js
                    // Start animation
                    if (!moveCorrect && !animationDone) {
                      moveCorrect = true;
                    }
                    
                    // Run animation
                    if (moveCorrect && !animationDone) {
                      animationTimer += 1;
                    
                      // Current position
                      const [current_x, current_y] = correct_prc_2.pos;
                    
                      // Compute direction toward target
                      const dx = endX - current_x;
                      const dy = endY - current_y;
                    
                      // Move a small fraction toward target
                      const move_fraction = feedback_steps; // fraction of remaining distance each frame
                      const new_x = current_x + dx * move_fraction;
                      const new_y = current_y + dy * move_fraction;
                    
                      // Update position
                      correct_prc_2.setPos([new_x, new_y]);
                    
                      if (is_correct) {
                         polygon_7.setPos([new_x, new_y]);
                        }
                      // Stop when close enough to target (or if max duration exceeded)
                      if (
                        (Math.abs(dx) < rest_jump && Math.abs(dy) < rest_jump) ||
                        animationTimer > maxAnimationDur
                      ) {
                        correct_prc_2.setPos([endX, endY]);
                        if (is_correct) {
                         polygon_7.setPos([new_x, new_y]);
                        }
                        animationDone = true;
                        moveCorrect = false;
                        continueRoutine = false;
                      }
                    }
                    
                    
                    // *polygon_7* updates
                    if (t >= 0.0 && polygon_7.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      polygon_7.tStart = t;  // (not accounting for frame time here)
                      polygon_7.frameNStart = frameN;  // exact frame index
                      
                      polygon_7.setAutoDraw(true);
                    }
                    
                    
                    // if polygon_7 is active this frame...
                    if (polygon_7.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (polygon_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      polygon_7.tStop = t;  // not accounting for scr refresh
                      polygon_7.frameNStop = frameN;  // exact frame index
                      // update status
                      polygon_7.status = PsychoJS.Status.FINISHED;
                      polygon_7.setAutoDraw(false);
                    }
                    
                    
                    // *prompt_prc_2* updates
                    if (t >= 0.0 && prompt_prc_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      prompt_prc_2.tStart = t;  // (not accounting for frame time here)
                      prompt_prc_2.frameNStart = frameN;  // exact frame index
                      
                      prompt_prc_2.setAutoDraw(true);
                    }
                    
                    
                    // if prompt_prc_2 is active this frame...
                    if (prompt_prc_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (prompt_prc_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      prompt_prc_2.tStop = t;  // not accounting for scr refresh
                      prompt_prc_2.frameNStop = frameN;  // exact frame index
                      // update status
                      prompt_prc_2.status = PsychoJS.Status.FINISHED;
                      prompt_prc_2.setAutoDraw(false);
                    }
                    
                    
                    // *dist_01_prc_2* updates
                    if (t >= 0.0 && dist_01_prc_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      dist_01_prc_2.tStart = t;  // (not accounting for frame time here)
                      dist_01_prc_2.frameNStart = frameN;  // exact frame index
                      
                      dist_01_prc_2.setAutoDraw(true);
                    }
                    
                    
                    // if dist_01_prc_2 is active this frame...
                    if (dist_01_prc_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (dist_01_prc_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      dist_01_prc_2.tStop = t;  // not accounting for scr refresh
                      dist_01_prc_2.frameNStop = frameN;  // exact frame index
                      // update status
                      dist_01_prc_2.status = PsychoJS.Status.FINISHED;
                      dist_01_prc_2.setAutoDraw(false);
                    }
                    
                    
                    // *dist_02_prc_2* updates
                    if (t >= 0.0 && dist_02_prc_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      dist_02_prc_2.tStart = t;  // (not accounting for frame time here)
                      dist_02_prc_2.frameNStart = frameN;  // exact frame index
                      
                      dist_02_prc_2.setAutoDraw(true);
                    }
                    
                    
                    // if dist_02_prc_2 is active this frame...
                    if (dist_02_prc_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (dist_02_prc_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      dist_02_prc_2.tStop = t;  // not accounting for scr refresh
                      dist_02_prc_2.frameNStop = frameN;  // exact frame index
                      // update status
                      dist_02_prc_2.status = PsychoJS.Status.FINISHED;
                      dist_02_prc_2.setAutoDraw(false);
                    }
                    
                    
                    // *correct_prc_2* updates
                    if (t >= 0.0 && correct_prc_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      correct_prc_2.tStart = t;  // (not accounting for frame time here)
                      correct_prc_2.frameNStart = frameN;  // exact frame index
                      
                      correct_prc_2.setAutoDraw(true);
                    }
                    
                    
                    // if correct_prc_2 is active this frame...
                    if (correct_prc_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (correct_prc_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      correct_prc_2.tStop = t;  // not accounting for scr refresh
                      correct_prc_2.frameNStop = frameN;  // exact frame index
                      // update status
                      correct_prc_2.status = PsychoJS.Status.FINISHED;
                      correct_prc_2.setAutoDraw(false);
                    }
                    
                    // check for quit (typically the Esc key)
                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                    }
                    
                    // check if the Routine should terminate
                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                      routineForceEnded = true;
                      return Scheduler.Event.NEXT;
                    }
                    
                    continueRoutine = false;  // reverts to True if at least one component still running
                    for (const thisComponent of practice_feedbackComponents)
                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                        continueRoutine = true;
                        break;
                      }
                    
                    // refresh the screen if continuing
                    if (continueRoutine) {
                      return Scheduler.Event.FLIP_REPEAT;
                    } else {
                      return Scheduler.Event.NEXT;
                    }
                  };
                }
                
                function practice_feedbackRoutineEnd(snapshot) {
                  return async function () {
                    //--- Ending Routine 'practice_feedback' ---
                    for (const thisComponent of practice_feedbackComponents) {
                      if (typeof thisComponent.setAutoDraw === 'function') {
                        thisComponent.setAutoDraw(false);
                      }
                    }
                    psychoJS.experiment.addData('practice_feedback.stopped', globalClock.getTime());
                    // the Routine "practice_feedback" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset();
                    
                    // Routines running outside a loop should always advance the datafile row
                    if (currentLoop === psychoJS.experiment) {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function rest_practiceRoutineBegin(snapshot) {
                  return async function () {
                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                    
                    //--- Prepare to start Routine 'rest_practice' ---
                    t = 0;
                    frameN = -1;
                    continueRoutine = true; // until we're told otherwise
                    // keep track of whether this Routine was forcibly ended
                    routineForceEnded = false;
                    rest_practiceClock.reset();
                    routineTimer.reset();
                    rest_practiceMaxDurationReached = false;
                    // update component parameters for each repeat
                    // Run 'Begin Routine' code from set_text_rest_instruction
                    if ((language === "english")) {
                        rest_instruction.text = "Short Break. Please wait,\nthis is not a rest break.";
                    }
                    if ((language === "german")) {
                        rest_instruction.text = "Kurze Pause. Bitte warten Sie.\nDies ist keine Ruhepause";
                    }
                    
                    psychoJS.experiment.addData('rest_practice.started', globalClock.getTime());
                    rest_practiceMaxDuration = null
                    // keep track of which components have finished
                    rest_practiceComponents = [];
                    rest_practiceComponents.push(fix_cross_2);
                    rest_practiceComponents.push(rest_instruction);
                    
                    for (const thisComponent of rest_practiceComponents)
                      if ('status' in thisComponent)
                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function rest_practiceRoutineEachFrame() {
                  return async function () {
                    //--- Loop for each frame of Routine 'rest_practice' ---
                    // get current time
                    t = rest_practiceClock.getTime();
                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                    // update/draw components on each frame
                    
                    // *fix_cross_2* updates
                    if (t >= 0.0 && fix_cross_2.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      fix_cross_2.tStart = t;  // (not accounting for frame time here)
                      fix_cross_2.frameNStart = frameN;  // exact frame index
                      
                      fix_cross_2.setAutoDraw(true);
                    }
                    
                    
                    // if fix_cross_2 is active this frame...
                    if (fix_cross_2.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + replay_break_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (fix_cross_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      fix_cross_2.tStop = t;  // not accounting for scr refresh
                      fix_cross_2.frameNStop = frameN;  // exact frame index
                      // update status
                      fix_cross_2.status = PsychoJS.Status.FINISHED;
                      fix_cross_2.setAutoDraw(false);
                    }
                    
                    
                    // *rest_instruction* updates
                    if (t >= 0.0 && rest_instruction.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      rest_instruction.tStart = t;  // (not accounting for frame time here)
                      rest_instruction.frameNStart = frameN;  // exact frame index
                      
                      rest_instruction.setAutoDraw(true);
                    }
                    
                    
                    // if rest_instruction is active this frame...
                    if (rest_instruction.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + replay_break_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (rest_instruction.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      rest_instruction.tStop = t;  // not accounting for scr refresh
                      rest_instruction.frameNStop = frameN;  // exact frame index
                      // update status
                      rest_instruction.status = PsychoJS.Status.FINISHED;
                      rest_instruction.setAutoDraw(false);
                    }
                    
                    // check for quit (typically the Esc key)
                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                    }
                    
                    // check if the Routine should terminate
                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                      routineForceEnded = true;
                      return Scheduler.Event.NEXT;
                    }
                    
                    continueRoutine = false;  // reverts to True if at least one component still running
                    for (const thisComponent of rest_practiceComponents)
                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                        continueRoutine = true;
                        break;
                      }
                    
                    // refresh the screen if continuing
                    if (continueRoutine) {
                      return Scheduler.Event.FLIP_REPEAT;
                    } else {
                      return Scheduler.Event.NEXT;
                    }
                  };
                }
                
                function rest_practiceRoutineEnd(snapshot) {
                  return async function () {
                    //--- Ending Routine 'rest_practice' ---
                    for (const thisComponent of rest_practiceComponents) {
                      if (typeof thisComponent.setAutoDraw === 'function') {
                        thisComponent.setAutoDraw(false);
                      }
                    }
                    psychoJS.experiment.addData('rest_practice.stopped', globalClock.getTime());
                    // the Routine "rest_practice" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset();
                    
                    // Routines running outside a loop should always advance the datafile row
                    if (currentLoop === psychoJS.experiment) {
                      psychoJS.experiment.nextEntry(snapshot);
                    }
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function instruction_retrieval_trialsRoutineBegin(snapshot) {
                  return async function () {
                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                    
                    //--- Prepare to start Routine 'instruction_retrieval_trials' ---
                    t = 0;
                    frameN = -1;
                    continueRoutine = true; // until we're told otherwise
                    // keep track of whether this Routine was forcibly ended
                    routineForceEnded = false;
                    instruction_retrieval_trialsClock.reset();
                    routineTimer.reset();
                    instruction_retrieval_trialsMaxDurationReached = false;
                    // update component parameters for each repeat
                    // Run 'Begin Routine' code from instruction_part7_text
                    if ((language === "english")) {
                        instruction_part7.text = "Good job!\n\nThe learning phases are interleaved with retrieval phases, in which you will answer questions about the learned sequences.\nIn a retrieval trial, you will always be presented with two images from the sequence.\nOne is presented after the other\n\nPress any key to continue.";
                    }
                    if ((language === "german")) {
                        instruction_part7.text = "Gut gemacht!\n\nDie Lernphasen wechseln sich mit Abrufphasen ab.\nDabei beantworten Sie Fragen zu den gelernten Sequenzen.\n\nIn jedem Abrufdurchgang sehen Sie nacheinander zwei\nBilder aus einer Sequenz.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                    }
                    
                    continue_button_8.keys = undefined;
                    continue_button_8.rt = undefined;
                    _continue_button_8_allKeys = [];
                    psychoJS.experiment.addData('instruction_retrieval_trials.started', globalClock.getTime());
                    instruction_retrieval_trialsMaxDuration = null
                    // keep track of which components have finished
                    instruction_retrieval_trialsComponents = [];
                    instruction_retrieval_trialsComponents.push(instruction_part7);
                    instruction_retrieval_trialsComponents.push(continue_button_8);
                    
                    for (const thisComponent of instruction_retrieval_trialsComponents)
                      if ('status' in thisComponent)
                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                    return Scheduler.Event.NEXT;
                  }
                }
                
                function instruction_retrieval_trialsRoutineEachFrame() {
                  return async function () {
                    //--- Loop for each frame of Routine 'instruction_retrieval_trials' ---
                    // get current time
                    t = instruction_retrieval_trialsClock.getTime();
                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                    // update/draw components on each frame
                    
                    // *instruction_part7* updates
                    if (t >= 0.0 && instruction_part7.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      instruction_part7.tStart = t;  // (not accounting for frame time here)
                      instruction_part7.frameNStart = frameN;  // exact frame index
                      
                      instruction_part7.setAutoDraw(true);
                    }
                    
                    
                    // if instruction_part7 is active this frame...
                    if (instruction_part7.status === PsychoJS.Status.STARTED) {
                    }
                    
                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (instruction_part7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      instruction_part7.tStop = t;  // not accounting for scr refresh
                      instruction_part7.frameNStop = frameN;  // exact frame index
                      // update status
                      instruction_part7.status = PsychoJS.Status.FINISHED;
                      instruction_part7.setAutoDraw(false);
                    }
                    
                    
                    // *continue_button_8* updates
                    if (t >= 3 && continue_button_8.status === PsychoJS.Status.NOT_STARTED) {
                      // keep track of start time/frame for later
                      continue_button_8.tStart = t;  // (not accounting for frame time here)
                      continue_button_8.frameNStart = frameN;  // exact frame index
                      
                      // keyboard checking is just starting
                      psychoJS.window.callOnFlip(function() { continue_button_8.clock.reset(); });  // t=0 on next screen flip
                      psychoJS.window.callOnFlip(function() { continue_button_8.start(); }); // start on screen flip
                      psychoJS.window.callOnFlip(function() { continue_button_8.clearEvents(); });
                    }
                    frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                    if (continue_button_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                      // keep track of stop time/frame for later
                      continue_button_8.tStop = t;  // not accounting for scr refresh
                      continue_button_8.frameNStop = frameN;  // exact frame index
                      // update status
                      continue_button_8.status = PsychoJS.Status.FINISHED;
                      frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                      if (continue_button_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                        // keep track of stop time/frame for later
                        continue_button_8.tStop = t;  // not accounting for scr refresh
                        continue_button_8.frameNStop = frameN;  // exact frame index
                        // update status
                        continue_button_8.status = PsychoJS.Status.FINISHED;
                        continue_button_8.status = PsychoJS.Status.FINISHED;
                          }
                        
                      }
                      
                      // if continue_button_8 is active this frame...
                      if (continue_button_8.status === PsychoJS.Status.STARTED) {
                        let theseKeys = continue_button_8.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                        _continue_button_8_allKeys = _continue_button_8_allKeys.concat(theseKeys);
                        if (_continue_button_8_allKeys.length > 0) {
                          continue_button_8.keys = _continue_button_8_allKeys[0].name;  // just the first key pressed
                          continue_button_8.rt = _continue_button_8_allKeys[0].rt;
                          continue_button_8.duration = _continue_button_8_allKeys[0].duration;
                          // a response ends the routine
                          continueRoutine = false;
                        }
                      }
                      
                      // check for quit (typically the Esc key)
                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                      }
                      
                      // check if the Routine should terminate
                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                        routineForceEnded = true;
                        return Scheduler.Event.NEXT;
                      }
                      
                      continueRoutine = false;  // reverts to True if at least one component still running
                      for (const thisComponent of instruction_retrieval_trialsComponents)
                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                          continueRoutine = true;
                          break;
                        }
                      
                      // refresh the screen if continuing
                      if (continueRoutine) {
                        return Scheduler.Event.FLIP_REPEAT;
                      } else {
                        return Scheduler.Event.NEXT;
                      }
                    };
                  }
                  
                  function instruction_retrieval_trialsRoutineEnd(snapshot) {
                    return async function () {
                      //--- Ending Routine 'instruction_retrieval_trials' ---
                      for (const thisComponent of instruction_retrieval_trialsComponents) {
                        if (typeof thisComponent.setAutoDraw === 'function') {
                          thisComponent.setAutoDraw(false);
                        }
                      }
                      psychoJS.experiment.addData('instruction_retrieval_trials.stopped', globalClock.getTime());
                      // update the trial handler
                      if (currentLoop instanceof MultiStairHandler) {
                        currentLoop.addResponse(continue_button_8.corr, level);
                      }
                      psychoJS.experiment.addData('continue_button_8.keys', continue_button_8.keys);
                      if (typeof continue_button_8.keys !== 'undefined') {  // we had a response
                          psychoJS.experiment.addData('continue_button_8.rt', continue_button_8.rt);
                          psychoJS.experiment.addData('continue_button_8.duration', continue_button_8.duration);
                          routineTimer.reset();
                          }
                      
                      continue_button_8.stop();
                      // the Routine "instruction_retrieval_trials" was not non-slip safe, so reset the non-slip timer
                      routineTimer.reset();
                      
                      // Routines running outside a loop should always advance the datafile row
                      if (currentLoop === psychoJS.experiment) {
                        psychoJS.experiment.nextEntry(snapshot);
                      }
                      return Scheduler.Event.NEXT;
                    }
                  }
                  
                  function instruction_retrievalques1RoutineBegin(snapshot) {
                    return async function () {
                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                      
                      //--- Prepare to start Routine 'instruction_retrievalques1' ---
                      t = 0;
                      frameN = -1;
                      continueRoutine = true; // until we're told otherwise
                      // keep track of whether this Routine was forcibly ended
                      routineForceEnded = false;
                      instruction_retrievalques1Clock.reset();
                      routineTimer.reset();
                      instruction_retrievalques1MaxDurationReached = false;
                      // update component parameters for each repeat
                      // Run 'Begin Routine' code from instruction_part7_text_3
                      if ((language === "english")) {
                          instruction_part10.text = "Retrieval Part 1: Order\n\nAfter seeing the two images, your first task is to indicate\nif the two images were presented in the learned sequence\nin the presented order or not.\n\nPress any key to continue.";
                      }
                      if ((language === "german")) {
                          instruction_part10.text = "Abruf Teil 1: Reihenfolge\n\nNach der Pr\u00e4sentation der beiden Bilder geben Sie an,\nob sie in der gelernten Sequenz in dieser Reihenfolge\nvorkamen.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                      }
                      
                      continue_button_10.keys = undefined;
                      continue_button_10.rt = undefined;
                      _continue_button_10_allKeys = [];
                      psychoJS.experiment.addData('instruction_retrievalques1.started', globalClock.getTime());
                      instruction_retrievalques1MaxDuration = null
                      // keep track of which components have finished
                      instruction_retrievalques1Components = [];
                      instruction_retrievalques1Components.push(instruction_part10);
                      instruction_retrievalques1Components.push(continue_button_10);
                      
                      for (const thisComponent of instruction_retrievalques1Components)
                        if ('status' in thisComponent)
                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                      return Scheduler.Event.NEXT;
                    }
                  }
                  
                  function instruction_retrievalques1RoutineEachFrame() {
                    return async function () {
                      //--- Loop for each frame of Routine 'instruction_retrievalques1' ---
                      // get current time
                      t = instruction_retrievalques1Clock.getTime();
                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                      // update/draw components on each frame
                      
                      // *instruction_part10* updates
                      if (t >= 0.0 && instruction_part10.status === PsychoJS.Status.NOT_STARTED) {
                        // keep track of start time/frame for later
                        instruction_part10.tStart = t;  // (not accounting for frame time here)
                        instruction_part10.frameNStart = frameN;  // exact frame index
                        
                        instruction_part10.setAutoDraw(true);
                      }
                      
                      
                      // if instruction_part10 is active this frame...
                      if (instruction_part10.status === PsychoJS.Status.STARTED) {
                      }
                      
                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                      if (instruction_part10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                        // keep track of stop time/frame for later
                        instruction_part10.tStop = t;  // not accounting for scr refresh
                        instruction_part10.frameNStop = frameN;  // exact frame index
                        // update status
                        instruction_part10.status = PsychoJS.Status.FINISHED;
                        instruction_part10.setAutoDraw(false);
                      }
                      
                      
                      // *continue_button_10* updates
                      if (t >= 3 && continue_button_10.status === PsychoJS.Status.NOT_STARTED) {
                        // keep track of start time/frame for later
                        continue_button_10.tStart = t;  // (not accounting for frame time here)
                        continue_button_10.frameNStart = frameN;  // exact frame index
                        
                        // keyboard checking is just starting
                        psychoJS.window.callOnFlip(function() { continue_button_10.clock.reset(); });  // t=0 on next screen flip
                        psychoJS.window.callOnFlip(function() { continue_button_10.start(); }); // start on screen flip
                        psychoJS.window.callOnFlip(function() { continue_button_10.clearEvents(); });
                      }
                      frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                      if (continue_button_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                        // keep track of stop time/frame for later
                        continue_button_10.tStop = t;  // not accounting for scr refresh
                        continue_button_10.frameNStop = frameN;  // exact frame index
                        // update status
                        continue_button_10.status = PsychoJS.Status.FINISHED;
                        frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                        if (continue_button_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                          // keep track of stop time/frame for later
                          continue_button_10.tStop = t;  // not accounting for scr refresh
                          continue_button_10.frameNStop = frameN;  // exact frame index
                          // update status
                          continue_button_10.status = PsychoJS.Status.FINISHED;
                          continue_button_10.status = PsychoJS.Status.FINISHED;
                            }
                          
                        }
                        
                        // if continue_button_10 is active this frame...
                        if (continue_button_10.status === PsychoJS.Status.STARTED) {
                          let theseKeys = continue_button_10.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                          _continue_button_10_allKeys = _continue_button_10_allKeys.concat(theseKeys);
                          if (_continue_button_10_allKeys.length > 0) {
                            continue_button_10.keys = _continue_button_10_allKeys[0].name;  // just the first key pressed
                            continue_button_10.rt = _continue_button_10_allKeys[0].rt;
                            continue_button_10.duration = _continue_button_10_allKeys[0].duration;
                            // a response ends the routine
                            continueRoutine = false;
                          }
                        }
                        
                        // check for quit (typically the Esc key)
                        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                        }
                        
                        // check if the Routine should terminate
                        if (!continueRoutine) {  // a component has requested a forced-end of Routine
                          routineForceEnded = true;
                          return Scheduler.Event.NEXT;
                        }
                        
                        continueRoutine = false;  // reverts to True if at least one component still running
                        for (const thisComponent of instruction_retrievalques1Components)
                          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                            continueRoutine = true;
                            break;
                          }
                        
                        // refresh the screen if continuing
                        if (continueRoutine) {
                          return Scheduler.Event.FLIP_REPEAT;
                        } else {
                          return Scheduler.Event.NEXT;
                        }
                      };
                    }
                    
                    function instruction_retrievalques1RoutineEnd(snapshot) {
                      return async function () {
                        //--- Ending Routine 'instruction_retrievalques1' ---
                        for (const thisComponent of instruction_retrievalques1Components) {
                          if (typeof thisComponent.setAutoDraw === 'function') {
                            thisComponent.setAutoDraw(false);
                          }
                        }
                        psychoJS.experiment.addData('instruction_retrievalques1.stopped', globalClock.getTime());
                        // update the trial handler
                        if (currentLoop instanceof MultiStairHandler) {
                          currentLoop.addResponse(continue_button_10.corr, level);
                        }
                        psychoJS.experiment.addData('continue_button_10.keys', continue_button_10.keys);
                        if (typeof continue_button_10.keys !== 'undefined') {  // we had a response
                            psychoJS.experiment.addData('continue_button_10.rt', continue_button_10.rt);
                            psychoJS.experiment.addData('continue_button_10.duration', continue_button_10.duration);
                            routineTimer.reset();
                            }
                        
                        continue_button_10.stop();
                        // the Routine "instruction_retrievalques1" was not non-slip safe, so reset the non-slip timer
                        routineTimer.reset();
                        
                        // Routines running outside a loop should always advance the datafile row
                        if (currentLoop === psychoJS.experiment) {
                          psychoJS.experiment.nextEntry(snapshot);
                        }
                        return Scheduler.Event.NEXT;
                      }
                    }
                    
                    function instruction_retrievalques1_02RoutineBegin(snapshot) {
                      return async function () {
                        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                        
                        //--- Prepare to start Routine 'instruction_retrievalques1_02' ---
                        t = 0;
                        frameN = -1;
                        continueRoutine = true; // until we're told otherwise
                        // keep track of whether this Routine was forcibly ended
                        routineForceEnded = false;
                        instruction_retrievalques1_02Clock.reset();
                        routineTimer.reset();
                        instruction_retrievalques1_02MaxDurationReached = false;
                        // update component parameters for each repeat
                        // Run 'Begin Routine' code from instruction_part13_text
                        if ((language === "english")) {
                            instruction_part13.text = "For this, use the left (green) and right (blue) button\n.The assignment of correct / incorrect to left / right can change, so please\ncheck on the screen which side corresponds to correct / incorrect on this trial.\n\nPress any key to continue.";
                        }
                        if ((language === "german")) {
                            instruction_part13.text = "W\u00e4hlen Sie \u201eJa\u201c oder \u201eNein\u201c mit der linken\ngr\u00fcnen oder rechten blauen Taste. Die Zuordnung\nwechselt zwischen den Durchg\u00e4ngen. Beachten Sie daher\ndie Anzeige auf dem Bildschirm.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                        }
                        
                        continue_button_19.keys = undefined;
                        continue_button_19.rt = undefined;
                        _continue_button_19_allKeys = [];
                        psychoJS.experiment.addData('instruction_retrievalques1_02.started', globalClock.getTime());
                        instruction_retrievalques1_02MaxDuration = null
                        // keep track of which components have finished
                        instruction_retrievalques1_02Components = [];
                        instruction_retrievalques1_02Components.push(instruction_part13);
                        instruction_retrievalques1_02Components.push(continue_button_19);
                        
                        for (const thisComponent of instruction_retrievalques1_02Components)
                          if ('status' in thisComponent)
                            thisComponent.status = PsychoJS.Status.NOT_STARTED;
                        return Scheduler.Event.NEXT;
                      }
                    }
                    
                    function instruction_retrievalques1_02RoutineEachFrame() {
                      return async function () {
                        //--- Loop for each frame of Routine 'instruction_retrievalques1_02' ---
                        // get current time
                        t = instruction_retrievalques1_02Clock.getTime();
                        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                        // update/draw components on each frame
                        
                        // *instruction_part13* updates
                        if (t >= 0.0 && instruction_part13.status === PsychoJS.Status.NOT_STARTED) {
                          // keep track of start time/frame for later
                          instruction_part13.tStart = t;  // (not accounting for frame time here)
                          instruction_part13.frameNStart = frameN;  // exact frame index
                          
                          instruction_part13.setAutoDraw(true);
                        }
                        
                        
                        // if instruction_part13 is active this frame...
                        if (instruction_part13.status === PsychoJS.Status.STARTED) {
                        }
                        
                        frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                        if (instruction_part13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                          // keep track of stop time/frame for later
                          instruction_part13.tStop = t;  // not accounting for scr refresh
                          instruction_part13.frameNStop = frameN;  // exact frame index
                          // update status
                          instruction_part13.status = PsychoJS.Status.FINISHED;
                          instruction_part13.setAutoDraw(false);
                        }
                        
                        
                        // *continue_button_19* updates
                        if (t >= 3 && continue_button_19.status === PsychoJS.Status.NOT_STARTED) {
                          // keep track of start time/frame for later
                          continue_button_19.tStart = t;  // (not accounting for frame time here)
                          continue_button_19.frameNStart = frameN;  // exact frame index
                          
                          // keyboard checking is just starting
                          psychoJS.window.callOnFlip(function() { continue_button_19.clock.reset(); });  // t=0 on next screen flip
                          psychoJS.window.callOnFlip(function() { continue_button_19.start(); }); // start on screen flip
                          psychoJS.window.callOnFlip(function() { continue_button_19.clearEvents(); });
                        }
                        frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                        if (continue_button_19.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                          // keep track of stop time/frame for later
                          continue_button_19.tStop = t;  // not accounting for scr refresh
                          continue_button_19.frameNStop = frameN;  // exact frame index
                          // update status
                          continue_button_19.status = PsychoJS.Status.FINISHED;
                          frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                          if (continue_button_19.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                            // keep track of stop time/frame for later
                            continue_button_19.tStop = t;  // not accounting for scr refresh
                            continue_button_19.frameNStop = frameN;  // exact frame index
                            // update status
                            continue_button_19.status = PsychoJS.Status.FINISHED;
                            continue_button_19.status = PsychoJS.Status.FINISHED;
                              }
                            
                          }
                          
                          // if continue_button_19 is active this frame...
                          if (continue_button_19.status === PsychoJS.Status.STARTED) {
                            let theseKeys = continue_button_19.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                            _continue_button_19_allKeys = _continue_button_19_allKeys.concat(theseKeys);
                            if (_continue_button_19_allKeys.length > 0) {
                              continue_button_19.keys = _continue_button_19_allKeys[0].name;  // just the first key pressed
                              continue_button_19.rt = _continue_button_19_allKeys[0].rt;
                              continue_button_19.duration = _continue_button_19_allKeys[0].duration;
                              // a response ends the routine
                              continueRoutine = false;
                            }
                          }
                          
                          // check for quit (typically the Esc key)
                          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                          }
                          
                          // check if the Routine should terminate
                          if (!continueRoutine) {  // a component has requested a forced-end of Routine
                            routineForceEnded = true;
                            return Scheduler.Event.NEXT;
                          }
                          
                          continueRoutine = false;  // reverts to True if at least one component still running
                          for (const thisComponent of instruction_retrievalques1_02Components)
                            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                              continueRoutine = true;
                              break;
                            }
                          
                          // refresh the screen if continuing
                          if (continueRoutine) {
                            return Scheduler.Event.FLIP_REPEAT;
                          } else {
                            return Scheduler.Event.NEXT;
                          }
                        };
                      }
                      
                      function instruction_retrievalques1_02RoutineEnd(snapshot) {
                        return async function () {
                          //--- Ending Routine 'instruction_retrievalques1_02' ---
                          for (const thisComponent of instruction_retrievalques1_02Components) {
                            if (typeof thisComponent.setAutoDraw === 'function') {
                              thisComponent.setAutoDraw(false);
                            }
                          }
                          psychoJS.experiment.addData('instruction_retrievalques1_02.stopped', globalClock.getTime());
                          // update the trial handler
                          if (currentLoop instanceof MultiStairHandler) {
                            currentLoop.addResponse(continue_button_19.corr, level);
                          }
                          psychoJS.experiment.addData('continue_button_19.keys', continue_button_19.keys);
                          if (typeof continue_button_19.keys !== 'undefined') {  // we had a response
                              psychoJS.experiment.addData('continue_button_19.rt', continue_button_19.rt);
                              psychoJS.experiment.addData('continue_button_19.duration', continue_button_19.duration);
                              routineTimer.reset();
                              }
                          
                          continue_button_19.stop();
                          // the Routine "instruction_retrievalques1_02" was not non-slip safe, so reset the non-slip timer
                          routineTimer.reset();
                          
                          // Routines running outside a loop should always advance the datafile row
                          if (currentLoop === psychoJS.experiment) {
                            psychoJS.experiment.nextEntry(snapshot);
                          }
                          return Scheduler.Event.NEXT;
                        }
                      }
                      
                      function instruction_retrievalques2RoutineBegin(snapshot) {
                        return async function () {
                          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                          
                          //--- Prepare to start Routine 'instruction_retrievalques2' ---
                          t = 0;
                          frameN = -1;
                          continueRoutine = true; // until we're told otherwise
                          // keep track of whether this Routine was forcibly ended
                          routineForceEnded = false;
                          instruction_retrievalques2Clock.reset();
                          routineTimer.reset();
                          instruction_retrievalques2MaxDurationReached = false;
                          // update component parameters for each repeat
                          // Run 'Begin Routine' code from instruction_part7_text_4
                          if ((language === "english")) {
                              instruction_part11.text = "Retrieval Part 2: Distance\n\nAfter the order question, indicate\nhow far apart the two images are\nin the sequence.\n\nPossible distances range from 2 to 5.\n\nPress any key to continue.";
                          }
                          if ((language === "german")) {
                              instruction_part11.text = "Abruf Teil 2: Distanz\n\nNach der Frage zur Reihenfolge geben Sie an,\nwie weit die beiden Bilder in der Sequenz voneinander\nentfernt sind.\n\nDie m\u00f6glichen Distanzen reichen von 2 bis 5.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                          }
                          
                          continue_button_11.keys = undefined;
                          continue_button_11.rt = undefined;
                          _continue_button_11_allKeys = [];
                          psychoJS.experiment.addData('instruction_retrievalques2.started', globalClock.getTime());
                          instruction_retrievalques2MaxDuration = null
                          // keep track of which components have finished
                          instruction_retrievalques2Components = [];
                          instruction_retrievalques2Components.push(instruction_part11);
                          instruction_retrievalques2Components.push(continue_button_11);
                          
                          for (const thisComponent of instruction_retrievalques2Components)
                            if ('status' in thisComponent)
                              thisComponent.status = PsychoJS.Status.NOT_STARTED;
                          return Scheduler.Event.NEXT;
                        }
                      }
                      
                      function instruction_retrievalques2RoutineEachFrame() {
                        return async function () {
                          //--- Loop for each frame of Routine 'instruction_retrievalques2' ---
                          // get current time
                          t = instruction_retrievalques2Clock.getTime();
                          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                          // update/draw components on each frame
                          
                          // *instruction_part11* updates
                          if (t >= 0.0 && instruction_part11.status === PsychoJS.Status.NOT_STARTED) {
                            // keep track of start time/frame for later
                            instruction_part11.tStart = t;  // (not accounting for frame time here)
                            instruction_part11.frameNStart = frameN;  // exact frame index
                            
                            instruction_part11.setAutoDraw(true);
                          }
                          
                          
                          // if instruction_part11 is active this frame...
                          if (instruction_part11.status === PsychoJS.Status.STARTED) {
                          }
                          
                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                          if (instruction_part11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                            // keep track of stop time/frame for later
                            instruction_part11.tStop = t;  // not accounting for scr refresh
                            instruction_part11.frameNStop = frameN;  // exact frame index
                            // update status
                            instruction_part11.status = PsychoJS.Status.FINISHED;
                            instruction_part11.setAutoDraw(false);
                          }
                          
                          
                          // *continue_button_11* updates
                          if (t >= 3 && continue_button_11.status === PsychoJS.Status.NOT_STARTED) {
                            // keep track of start time/frame for later
                            continue_button_11.tStart = t;  // (not accounting for frame time here)
                            continue_button_11.frameNStart = frameN;  // exact frame index
                            
                            // keyboard checking is just starting
                            psychoJS.window.callOnFlip(function() { continue_button_11.clock.reset(); });  // t=0 on next screen flip
                            psychoJS.window.callOnFlip(function() { continue_button_11.start(); }); // start on screen flip
                            psychoJS.window.callOnFlip(function() { continue_button_11.clearEvents(); });
                          }
                          frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                          if (continue_button_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                            // keep track of stop time/frame for later
                            continue_button_11.tStop = t;  // not accounting for scr refresh
                            continue_button_11.frameNStop = frameN;  // exact frame index
                            // update status
                            continue_button_11.status = PsychoJS.Status.FINISHED;
                            frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                            if (continue_button_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                              // keep track of stop time/frame for later
                              continue_button_11.tStop = t;  // not accounting for scr refresh
                              continue_button_11.frameNStop = frameN;  // exact frame index
                              // update status
                              continue_button_11.status = PsychoJS.Status.FINISHED;
                              continue_button_11.status = PsychoJS.Status.FINISHED;
                                }
                              
                            }
                            
                            // if continue_button_11 is active this frame...
                            if (continue_button_11.status === PsychoJS.Status.STARTED) {
                              let theseKeys = continue_button_11.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                              _continue_button_11_allKeys = _continue_button_11_allKeys.concat(theseKeys);
                              if (_continue_button_11_allKeys.length > 0) {
                                continue_button_11.keys = _continue_button_11_allKeys[0].name;  // just the first key pressed
                                continue_button_11.rt = _continue_button_11_allKeys[0].rt;
                                continue_button_11.duration = _continue_button_11_allKeys[0].duration;
                                // a response ends the routine
                                continueRoutine = false;
                              }
                            }
                            
                            // check for quit (typically the Esc key)
                            if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                              return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                            }
                            
                            // check if the Routine should terminate
                            if (!continueRoutine) {  // a component has requested a forced-end of Routine
                              routineForceEnded = true;
                              return Scheduler.Event.NEXT;
                            }
                            
                            continueRoutine = false;  // reverts to True if at least one component still running
                            for (const thisComponent of instruction_retrievalques2Components)
                              if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                continueRoutine = true;
                                break;
                              }
                            
                            // refresh the screen if continuing
                            if (continueRoutine) {
                              return Scheduler.Event.FLIP_REPEAT;
                            } else {
                              return Scheduler.Event.NEXT;
                            }
                          };
                        }
                        
                        function instruction_retrievalques2RoutineEnd(snapshot) {
                          return async function () {
                            //--- Ending Routine 'instruction_retrievalques2' ---
                            for (const thisComponent of instruction_retrievalques2Components) {
                              if (typeof thisComponent.setAutoDraw === 'function') {
                                thisComponent.setAutoDraw(false);
                              }
                            }
                            psychoJS.experiment.addData('instruction_retrievalques2.stopped', globalClock.getTime());
                            // update the trial handler
                            if (currentLoop instanceof MultiStairHandler) {
                              currentLoop.addResponse(continue_button_11.corr, level);
                            }
                            psychoJS.experiment.addData('continue_button_11.keys', continue_button_11.keys);
                            if (typeof continue_button_11.keys !== 'undefined') {  // we had a response
                                psychoJS.experiment.addData('continue_button_11.rt', continue_button_11.rt);
                                psychoJS.experiment.addData('continue_button_11.duration', continue_button_11.duration);
                                routineTimer.reset();
                                }
                            
                            continue_button_11.stop();
                            // the Routine "instruction_retrievalques2" was not non-slip safe, so reset the non-slip timer
                            routineTimer.reset();
                            
                            // Routines running outside a loop should always advance the datafile row
                            if (currentLoop === psychoJS.experiment) {
                              psychoJS.experiment.nextEntry(snapshot);
                            }
                            return Scheduler.Event.NEXT;
                          }
                        }
                        
                        function instruction_retrievalques2_02RoutineBegin(snapshot) {
                          return async function () {
                            TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                            
                            //--- Prepare to start Routine 'instruction_retrievalques2_02' ---
                            t = 0;
                            frameN = -1;
                            continueRoutine = true; // until we're told otherwise
                            // keep track of whether this Routine was forcibly ended
                            routineForceEnded = false;
                            instruction_retrievalques2_02Clock.reset();
                            routineTimer.reset();
                            instruction_retrievalques2_02MaxDurationReached = false;
                            // update component parameters for each repeat
                            // Run 'Begin Routine' code from instruction_part14_text
                            if ((language === "english")) {
                                instruction_part14.text = "At distance 2, there is one image in between,\nand at distance 5, there are four images in between.\n\nRespond using the four buttons.\nThe corresponding button assignments will be shown on the screen.\n\nPress any key to continue.";
                            }
                            if ((language === "german")) {
                                instruction_part14.text = "Bei Distanz 2 liegt ein Bild dazwischen,\nbei Distanz 5 liegen vier Bilder dazwischen.\n\nAntworten Sie mit den vier Tasten.\nDie jeweilige Tastenbelegung wird auf dem Bildschirm angezeigt.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                            }
                            
                            continue_button_20.keys = undefined;
                            continue_button_20.rt = undefined;
                            _continue_button_20_allKeys = [];
                            psychoJS.experiment.addData('instruction_retrievalques2_02.started', globalClock.getTime());
                            instruction_retrievalques2_02MaxDuration = null
                            // keep track of which components have finished
                            instruction_retrievalques2_02Components = [];
                            instruction_retrievalques2_02Components.push(instruction_part14);
                            instruction_retrievalques2_02Components.push(continue_button_20);
                            
                            for (const thisComponent of instruction_retrievalques2_02Components)
                              if ('status' in thisComponent)
                                thisComponent.status = PsychoJS.Status.NOT_STARTED;
                            return Scheduler.Event.NEXT;
                          }
                        }
                        
                        function instruction_retrievalques2_02RoutineEachFrame() {
                          return async function () {
                            //--- Loop for each frame of Routine 'instruction_retrievalques2_02' ---
                            // get current time
                            t = instruction_retrievalques2_02Clock.getTime();
                            frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                            // update/draw components on each frame
                            
                            // *instruction_part14* updates
                            if (t >= 0.0 && instruction_part14.status === PsychoJS.Status.NOT_STARTED) {
                              // keep track of start time/frame for later
                              instruction_part14.tStart = t;  // (not accounting for frame time here)
                              instruction_part14.frameNStart = frameN;  // exact frame index
                              
                              instruction_part14.setAutoDraw(true);
                            }
                            
                            
                            // if instruction_part14 is active this frame...
                            if (instruction_part14.status === PsychoJS.Status.STARTED) {
                            }
                            
                            frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                            if (instruction_part14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                              // keep track of stop time/frame for later
                              instruction_part14.tStop = t;  // not accounting for scr refresh
                              instruction_part14.frameNStop = frameN;  // exact frame index
                              // update status
                              instruction_part14.status = PsychoJS.Status.FINISHED;
                              instruction_part14.setAutoDraw(false);
                            }
                            
                            
                            // *continue_button_20* updates
                            if (t >= 3 && continue_button_20.status === PsychoJS.Status.NOT_STARTED) {
                              // keep track of start time/frame for later
                              continue_button_20.tStart = t;  // (not accounting for frame time here)
                              continue_button_20.frameNStart = frameN;  // exact frame index
                              
                              // keyboard checking is just starting
                              psychoJS.window.callOnFlip(function() { continue_button_20.clock.reset(); });  // t=0 on next screen flip
                              psychoJS.window.callOnFlip(function() { continue_button_20.start(); }); // start on screen flip
                              psychoJS.window.callOnFlip(function() { continue_button_20.clearEvents(); });
                            }
                            frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                            if (continue_button_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                              // keep track of stop time/frame for later
                              continue_button_20.tStop = t;  // not accounting for scr refresh
                              continue_button_20.frameNStop = frameN;  // exact frame index
                              // update status
                              continue_button_20.status = PsychoJS.Status.FINISHED;
                              frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                              if (continue_button_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                // keep track of stop time/frame for later
                                continue_button_20.tStop = t;  // not accounting for scr refresh
                                continue_button_20.frameNStop = frameN;  // exact frame index
                                // update status
                                continue_button_20.status = PsychoJS.Status.FINISHED;
                                continue_button_20.status = PsychoJS.Status.FINISHED;
                                  }
                                
                              }
                              
                              // if continue_button_20 is active this frame...
                              if (continue_button_20.status === PsychoJS.Status.STARTED) {
                                let theseKeys = continue_button_20.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                _continue_button_20_allKeys = _continue_button_20_allKeys.concat(theseKeys);
                                if (_continue_button_20_allKeys.length > 0) {
                                  continue_button_20.keys = _continue_button_20_allKeys[0].name;  // just the first key pressed
                                  continue_button_20.rt = _continue_button_20_allKeys[0].rt;
                                  continue_button_20.duration = _continue_button_20_allKeys[0].duration;
                                  // a response ends the routine
                                  continueRoutine = false;
                                }
                              }
                              
                              // check for quit (typically the Esc key)
                              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                              }
                              
                              // check if the Routine should terminate
                              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                routineForceEnded = true;
                                return Scheduler.Event.NEXT;
                              }
                              
                              continueRoutine = false;  // reverts to True if at least one component still running
                              for (const thisComponent of instruction_retrievalques2_02Components)
                                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                  continueRoutine = true;
                                  break;
                                }
                              
                              // refresh the screen if continuing
                              if (continueRoutine) {
                                return Scheduler.Event.FLIP_REPEAT;
                              } else {
                                return Scheduler.Event.NEXT;
                              }
                            };
                          }
                          
                          function instruction_retrievalques2_02RoutineEnd(snapshot) {
                            return async function () {
                              //--- Ending Routine 'instruction_retrievalques2_02' ---
                              for (const thisComponent of instruction_retrievalques2_02Components) {
                                if (typeof thisComponent.setAutoDraw === 'function') {
                                  thisComponent.setAutoDraw(false);
                                }
                              }
                              psychoJS.experiment.addData('instruction_retrievalques2_02.stopped', globalClock.getTime());
                              // update the trial handler
                              if (currentLoop instanceof MultiStairHandler) {
                                currentLoop.addResponse(continue_button_20.corr, level);
                              }
                              psychoJS.experiment.addData('continue_button_20.keys', continue_button_20.keys);
                              if (typeof continue_button_20.keys !== 'undefined') {  // we had a response
                                  psychoJS.experiment.addData('continue_button_20.rt', continue_button_20.rt);
                                  psychoJS.experiment.addData('continue_button_20.duration', continue_button_20.duration);
                                  routineTimer.reset();
                                  }
                              
                              continue_button_20.stop();
                              // the Routine "instruction_retrievalques2_02" was not non-slip safe, so reset the non-slip timer
                              routineTimer.reset();
                              
                              // Routines running outside a loop should always advance the datafile row
                              if (currentLoop === psychoJS.experiment) {
                                psychoJS.experiment.nextEntry(snapshot);
                              }
                              return Scheduler.Event.NEXT;
                            }
                          }
                          
                          function instruction_refl_periodRoutineBegin(snapshot) {
                            return async function () {
                              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                              
                              //--- Prepare to start Routine 'instruction_refl_period' ---
                              t = 0;
                              frameN = -1;
                              continueRoutine = true; // until we're told otherwise
                              // keep track of whether this Routine was forcibly ended
                              routineForceEnded = false;
                              instruction_refl_periodClock.reset();
                              routineTimer.reset();
                              instruction_refl_periodMaxDurationReached = false;
                              // update component parameters for each repeat
                              // Run 'Begin Routine' code from instruction_part7_text_5
                              if ((language === "english")) {
                                  instruction_part12.text = "Retrieval: Reflection Period\n\nBefore answering the order and distance questions,\na fixation cross will briefly appear.\n\nPress any button to continue.";
                              }
                              if ((language === "german")) {
                                  instruction_part12.text = "Abruf: Reflexionsperiode\n\nBevor Sie die Fragen zur Reihenfolge und Distanz\nbeantworten, erscheint kurz ein Fixationskreuz.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                              }
                              
                              continue_button_14.keys = undefined;
                              continue_button_14.rt = undefined;
                              _continue_button_14_allKeys = [];
                              psychoJS.experiment.addData('instruction_refl_period.started', globalClock.getTime());
                              instruction_refl_periodMaxDuration = null
                              // keep track of which components have finished
                              instruction_refl_periodComponents = [];
                              instruction_refl_periodComponents.push(instruction_part12);
                              instruction_refl_periodComponents.push(continue_button_14);
                              
                              for (const thisComponent of instruction_refl_periodComponents)
                                if ('status' in thisComponent)
                                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
                              return Scheduler.Event.NEXT;
                            }
                          }
                          
                          function instruction_refl_periodRoutineEachFrame() {
                            return async function () {
                              //--- Loop for each frame of Routine 'instruction_refl_period' ---
                              // get current time
                              t = instruction_refl_periodClock.getTime();
                              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                              // update/draw components on each frame
                              
                              // *instruction_part12* updates
                              if (t >= 0.0 && instruction_part12.status === PsychoJS.Status.NOT_STARTED) {
                                // keep track of start time/frame for later
                                instruction_part12.tStart = t;  // (not accounting for frame time here)
                                instruction_part12.frameNStart = frameN;  // exact frame index
                                
                                instruction_part12.setAutoDraw(true);
                              }
                              
                              
                              // if instruction_part12 is active this frame...
                              if (instruction_part12.status === PsychoJS.Status.STARTED) {
                              }
                              
                              frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                              if (instruction_part12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                // keep track of stop time/frame for later
                                instruction_part12.tStop = t;  // not accounting for scr refresh
                                instruction_part12.frameNStop = frameN;  // exact frame index
                                // update status
                                instruction_part12.status = PsychoJS.Status.FINISHED;
                                instruction_part12.setAutoDraw(false);
                              }
                              
                              
                              // *continue_button_14* updates
                              if (t >= 3 && continue_button_14.status === PsychoJS.Status.NOT_STARTED) {
                                // keep track of start time/frame for later
                                continue_button_14.tStart = t;  // (not accounting for frame time here)
                                continue_button_14.frameNStart = frameN;  // exact frame index
                                
                                // keyboard checking is just starting
                                psychoJS.window.callOnFlip(function() { continue_button_14.clock.reset(); });  // t=0 on next screen flip
                                psychoJS.window.callOnFlip(function() { continue_button_14.start(); }); // start on screen flip
                                psychoJS.window.callOnFlip(function() { continue_button_14.clearEvents(); });
                              }
                              frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                              if (continue_button_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                // keep track of stop time/frame for later
                                continue_button_14.tStop = t;  // not accounting for scr refresh
                                continue_button_14.frameNStop = frameN;  // exact frame index
                                // update status
                                continue_button_14.status = PsychoJS.Status.FINISHED;
                                frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                if (continue_button_14.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                  // keep track of stop time/frame for later
                                  continue_button_14.tStop = t;  // not accounting for scr refresh
                                  continue_button_14.frameNStop = frameN;  // exact frame index
                                  // update status
                                  continue_button_14.status = PsychoJS.Status.FINISHED;
                                  continue_button_14.status = PsychoJS.Status.FINISHED;
                                    }
                                  
                                }
                                
                                // if continue_button_14 is active this frame...
                                if (continue_button_14.status === PsychoJS.Status.STARTED) {
                                  let theseKeys = continue_button_14.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                  _continue_button_14_allKeys = _continue_button_14_allKeys.concat(theseKeys);
                                  if (_continue_button_14_allKeys.length > 0) {
                                    continue_button_14.keys = _continue_button_14_allKeys[0].name;  // just the first key pressed
                                    continue_button_14.rt = _continue_button_14_allKeys[0].rt;
                                    continue_button_14.duration = _continue_button_14_allKeys[0].duration;
                                    // a response ends the routine
                                    continueRoutine = false;
                                  }
                                }
                                
                                // check for quit (typically the Esc key)
                                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                }
                                
                                // check if the Routine should terminate
                                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                  routineForceEnded = true;
                                  return Scheduler.Event.NEXT;
                                }
                                
                                continueRoutine = false;  // reverts to True if at least one component still running
                                for (const thisComponent of instruction_refl_periodComponents)
                                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                    continueRoutine = true;
                                    break;
                                  }
                                
                                // refresh the screen if continuing
                                if (continueRoutine) {
                                  return Scheduler.Event.FLIP_REPEAT;
                                } else {
                                  return Scheduler.Event.NEXT;
                                }
                              };
                            }
                            
                            function instruction_refl_periodRoutineEnd(snapshot) {
                              return async function () {
                                //--- Ending Routine 'instruction_refl_period' ---
                                for (const thisComponent of instruction_refl_periodComponents) {
                                  if (typeof thisComponent.setAutoDraw === 'function') {
                                    thisComponent.setAutoDraw(false);
                                  }
                                }
                                psychoJS.experiment.addData('instruction_refl_period.stopped', globalClock.getTime());
                                // update the trial handler
                                if (currentLoop instanceof MultiStairHandler) {
                                  currentLoop.addResponse(continue_button_14.corr, level);
                                }
                                psychoJS.experiment.addData('continue_button_14.keys', continue_button_14.keys);
                                if (typeof continue_button_14.keys !== 'undefined') {  // we had a response
                                    psychoJS.experiment.addData('continue_button_14.rt', continue_button_14.rt);
                                    psychoJS.experiment.addData('continue_button_14.duration', continue_button_14.duration);
                                    routineTimer.reset();
                                    }
                                
                                continue_button_14.stop();
                                // the Routine "instruction_refl_period" was not non-slip safe, so reset the non-slip timer
                                routineTimer.reset();
                                
                                // Routines running outside a loop should always advance the datafile row
                                if (currentLoop === psychoJS.experiment) {
                                  psychoJS.experiment.nextEntry(snapshot);
                                }
                                return Scheduler.Event.NEXT;
                              }
                            }
                            
                            function instruction_refl_period_02RoutineBegin(snapshot) {
                              return async function () {
                                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                
                                //--- Prepare to start Routine 'instruction_refl_period_02' ---
                                t = 0;
                                frameN = -1;
                                continueRoutine = true; // until we're told otherwise
                                // keep track of whether this Routine was forcibly ended
                                routineForceEnded = false;
                                instruction_refl_period_02Clock.reset();
                                routineTimer.reset();
                                instruction_refl_period_02MaxDurationReached = false;
                                // update component parameters for each repeat
                                // Run 'Begin Routine' code from instruction_part15_text
                                if ((language === "english")) {
                                    instruction_part15.text = "During this time, already consider whether the images\nappeared in this order and how far apart they are\nin the sequence.\n\nThis is important because the time available for the\nsubsequent responses is short.\n\nPress any key to continue.";
                                }
                                if ((language === "german")) {
                                    instruction_part15.text = "\u00dcberlegen Sie in dieser Zeit bereits, ob die Bilder\nin dieser Reihenfolge vorkamen und wie weit sie in\nder Sequenz voneinander entfernt sind.\n\nDies ist wichtig, da die Zeit f\u00fcr die anschlie\u00dfenden\nAntworten kurz ist.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                                }
                                
                                continue_button_21.keys = undefined;
                                continue_button_21.rt = undefined;
                                _continue_button_21_allKeys = [];
                                psychoJS.experiment.addData('instruction_refl_period_02.started', globalClock.getTime());
                                instruction_refl_period_02MaxDuration = null
                                // keep track of which components have finished
                                instruction_refl_period_02Components = [];
                                instruction_refl_period_02Components.push(instruction_part15);
                                instruction_refl_period_02Components.push(continue_button_21);
                                
                                for (const thisComponent of instruction_refl_period_02Components)
                                  if ('status' in thisComponent)
                                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                return Scheduler.Event.NEXT;
                              }
                            }
                            
                            function instruction_refl_period_02RoutineEachFrame() {
                              return async function () {
                                //--- Loop for each frame of Routine 'instruction_refl_period_02' ---
                                // get current time
                                t = instruction_refl_period_02Clock.getTime();
                                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                // update/draw components on each frame
                                
                                // *instruction_part15* updates
                                if (t >= 0.0 && instruction_part15.status === PsychoJS.Status.NOT_STARTED) {
                                  // keep track of start time/frame for later
                                  instruction_part15.tStart = t;  // (not accounting for frame time here)
                                  instruction_part15.frameNStart = frameN;  // exact frame index
                                  
                                  instruction_part15.setAutoDraw(true);
                                }
                                
                                
                                // if instruction_part15 is active this frame...
                                if (instruction_part15.status === PsychoJS.Status.STARTED) {
                                }
                                
                                frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                if (instruction_part15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                  // keep track of stop time/frame for later
                                  instruction_part15.tStop = t;  // not accounting for scr refresh
                                  instruction_part15.frameNStop = frameN;  // exact frame index
                                  // update status
                                  instruction_part15.status = PsychoJS.Status.FINISHED;
                                  instruction_part15.setAutoDraw(false);
                                }
                                
                                
                                // *continue_button_21* updates
                                if (t >= 3 && continue_button_21.status === PsychoJS.Status.NOT_STARTED) {
                                  // keep track of start time/frame for later
                                  continue_button_21.tStart = t;  // (not accounting for frame time here)
                                  continue_button_21.frameNStart = frameN;  // exact frame index
                                  
                                  // keyboard checking is just starting
                                  psychoJS.window.callOnFlip(function() { continue_button_21.clock.reset(); });  // t=0 on next screen flip
                                  psychoJS.window.callOnFlip(function() { continue_button_21.start(); }); // start on screen flip
                                  psychoJS.window.callOnFlip(function() { continue_button_21.clearEvents(); });
                                }
                                frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                if (continue_button_21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                  // keep track of stop time/frame for later
                                  continue_button_21.tStop = t;  // not accounting for scr refresh
                                  continue_button_21.frameNStop = frameN;  // exact frame index
                                  // update status
                                  continue_button_21.status = PsychoJS.Status.FINISHED;
                                  frameRemains = 3 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                  if (continue_button_21.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                    // keep track of stop time/frame for later
                                    continue_button_21.tStop = t;  // not accounting for scr refresh
                                    continue_button_21.frameNStop = frameN;  // exact frame index
                                    // update status
                                    continue_button_21.status = PsychoJS.Status.FINISHED;
                                    continue_button_21.status = PsychoJS.Status.FINISHED;
                                      }
                                    
                                  }
                                  
                                  // if continue_button_21 is active this frame...
                                  if (continue_button_21.status === PsychoJS.Status.STARTED) {
                                    let theseKeys = continue_button_21.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                    _continue_button_21_allKeys = _continue_button_21_allKeys.concat(theseKeys);
                                    if (_continue_button_21_allKeys.length > 0) {
                                      continue_button_21.keys = _continue_button_21_allKeys[0].name;  // just the first key pressed
                                      continue_button_21.rt = _continue_button_21_allKeys[0].rt;
                                      continue_button_21.duration = _continue_button_21_allKeys[0].duration;
                                      // a response ends the routine
                                      continueRoutine = false;
                                    }
                                  }
                                  
                                  // check for quit (typically the Esc key)
                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                  }
                                  
                                  // check if the Routine should terminate
                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                    routineForceEnded = true;
                                    return Scheduler.Event.NEXT;
                                  }
                                  
                                  continueRoutine = false;  // reverts to True if at least one component still running
                                  for (const thisComponent of instruction_refl_period_02Components)
                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                      continueRoutine = true;
                                      break;
                                    }
                                  
                                  // refresh the screen if continuing
                                  if (continueRoutine) {
                                    return Scheduler.Event.FLIP_REPEAT;
                                  } else {
                                    return Scheduler.Event.NEXT;
                                  }
                                };
                              }
                              
                              function instruction_refl_period_02RoutineEnd(snapshot) {
                                return async function () {
                                  //--- Ending Routine 'instruction_refl_period_02' ---
                                  for (const thisComponent of instruction_refl_period_02Components) {
                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                      thisComponent.setAutoDraw(false);
                                    }
                                  }
                                  psychoJS.experiment.addData('instruction_refl_period_02.stopped', globalClock.getTime());
                                  // update the trial handler
                                  if (currentLoop instanceof MultiStairHandler) {
                                    currentLoop.addResponse(continue_button_21.corr, level);
                                  }
                                  psychoJS.experiment.addData('continue_button_21.keys', continue_button_21.keys);
                                  if (typeof continue_button_21.keys !== 'undefined') {  // we had a response
                                      psychoJS.experiment.addData('continue_button_21.rt', continue_button_21.rt);
                                      psychoJS.experiment.addData('continue_button_21.duration', continue_button_21.duration);
                                      routineTimer.reset();
                                      }
                                  
                                  continue_button_21.stop();
                                  // the Routine "instruction_refl_period_02" was not non-slip safe, so reset the non-slip timer
                                  routineTimer.reset();
                                  
                                  // Routines running outside a loop should always advance the datafile row
                                  if (currentLoop === psychoJS.experiment) {
                                    psychoJS.experiment.nextEntry(snapshot);
                                  }
                                  return Scheduler.Event.NEXT;
                                }
                              }
                              
                              function retrieval_backg_infoRoutineBegin(snapshot) {
                                return async function () {
                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                  
                                  //--- Prepare to start Routine 'retrieval_backg_info' ---
                                  t = 0;
                                  frameN = -1;
                                  continueRoutine = true; // until we're told otherwise
                                  // keep track of whether this Routine was forcibly ended
                                  routineForceEnded = false;
                                  retrieval_backg_infoClock.reset();
                                  routineTimer.reset();
                                  retrieval_backg_infoMaxDurationReached = false;
                                  // update component parameters for each repeat
                                  // Run 'Begin Routine' code from instruction_info_text
                                  if ((language === "english")) {
                                      instruction_info.text = "In the practice of the retrieval trials, you will get some background information on how the sequence of images is structured.\nThis will appear at the bottom.\n\nIn the main trials, there will be no additional information.\nYou should extract this information from the pairwise associations learned.\n\nPress any key to continue.";
                                  }
                                  if ((language === "german")) {
                                      instruction_info.text = "In den \u00dcbungsdurchg\u00e4ngen erhalten Sie unten\nauf dem Bildschirm zus\u00e4tzliche Hinweise zur Struktur\nder Bildsequenz.\n\nIn der Hauptaufgabe werden diese Hinweise nicht\nmehr angezeigt. Dort m\u00fcssen Sie die Struktur aus\nden gelernten Bildpaaren ableiten.\n\nDr\u00fccken Sie eine beliebige Taste, um fortzufahren.";
                                  }
                                  
                                  continue_button_15.keys = undefined;
                                  continue_button_15.rt = undefined;
                                  _continue_button_15_allKeys = [];
                                  psychoJS.experiment.addData('retrieval_backg_info.started', globalClock.getTime());
                                  retrieval_backg_infoMaxDuration = null
                                  // keep track of which components have finished
                                  retrieval_backg_infoComponents = [];
                                  retrieval_backg_infoComponents.push(instruction_info);
                                  retrieval_backg_infoComponents.push(continue_button_15);
                                  
                                  for (const thisComponent of retrieval_backg_infoComponents)
                                    if ('status' in thisComponent)
                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                  return Scheduler.Event.NEXT;
                                }
                              }
                              
                              function retrieval_backg_infoRoutineEachFrame() {
                                return async function () {
                                  //--- Loop for each frame of Routine 'retrieval_backg_info' ---
                                  // get current time
                                  t = retrieval_backg_infoClock.getTime();
                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                  // update/draw components on each frame
                                  
                                  // *instruction_info* updates
                                  if (t >= 0.0 && instruction_info.status === PsychoJS.Status.NOT_STARTED) {
                                    // keep track of start time/frame for later
                                    instruction_info.tStart = t;  // (not accounting for frame time here)
                                    instruction_info.frameNStart = frameN;  // exact frame index
                                    
                                    instruction_info.setAutoDraw(true);
                                  }
                                  
                                  
                                  // if instruction_info is active this frame...
                                  if (instruction_info.status === PsychoJS.Status.STARTED) {
                                  }
                                  
                                  frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                  if (instruction_info.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                    // keep track of stop time/frame for later
                                    instruction_info.tStop = t;  // not accounting for scr refresh
                                    instruction_info.frameNStop = frameN;  // exact frame index
                                    // update status
                                    instruction_info.status = PsychoJS.Status.FINISHED;
                                    instruction_info.setAutoDraw(false);
                                  }
                                  
                                  
                                  // *continue_button_15* updates
                                  if (t >= 0.5 && continue_button_15.status === PsychoJS.Status.NOT_STARTED) {
                                    // keep track of start time/frame for later
                                    continue_button_15.tStart = t;  // (not accounting for frame time here)
                                    continue_button_15.frameNStart = frameN;  // exact frame index
                                    
                                    // keyboard checking is just starting
                                    psychoJS.window.callOnFlip(function() { continue_button_15.clock.reset(); });  // t=0 on next screen flip
                                    psychoJS.window.callOnFlip(function() { continue_button_15.start(); }); // start on screen flip
                                    psychoJS.window.callOnFlip(function() { continue_button_15.clearEvents(); });
                                  }
                                  frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                  if (continue_button_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                    // keep track of stop time/frame for later
                                    continue_button_15.tStop = t;  // not accounting for scr refresh
                                    continue_button_15.frameNStop = frameN;  // exact frame index
                                    // update status
                                    continue_button_15.status = PsychoJS.Status.FINISHED;
                                    frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                    if (continue_button_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                      // keep track of stop time/frame for later
                                      continue_button_15.tStop = t;  // not accounting for scr refresh
                                      continue_button_15.frameNStop = frameN;  // exact frame index
                                      // update status
                                      continue_button_15.status = PsychoJS.Status.FINISHED;
                                      continue_button_15.status = PsychoJS.Status.FINISHED;
                                        }
                                      
                                    }
                                    
                                    // if continue_button_15 is active this frame...
                                    if (continue_button_15.status === PsychoJS.Status.STARTED) {
                                      let theseKeys = continue_button_15.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                      _continue_button_15_allKeys = _continue_button_15_allKeys.concat(theseKeys);
                                      if (_continue_button_15_allKeys.length > 0) {
                                        continue_button_15.keys = _continue_button_15_allKeys[0].name;  // just the first key pressed
                                        continue_button_15.rt = _continue_button_15_allKeys[0].rt;
                                        continue_button_15.duration = _continue_button_15_allKeys[0].duration;
                                        // a response ends the routine
                                        continueRoutine = false;
                                      }
                                    }
                                    
                                    // check for quit (typically the Esc key)
                                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                    }
                                    
                                    // check if the Routine should terminate
                                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                      routineForceEnded = true;
                                      return Scheduler.Event.NEXT;
                                    }
                                    
                                    continueRoutine = false;  // reverts to True if at least one component still running
                                    for (const thisComponent of retrieval_backg_infoComponents)
                                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                        continueRoutine = true;
                                        break;
                                      }
                                    
                                    // refresh the screen if continuing
                                    if (continueRoutine) {
                                      return Scheduler.Event.FLIP_REPEAT;
                                    } else {
                                      return Scheduler.Event.NEXT;
                                    }
                                  };
                                }
                                
                                function retrieval_backg_infoRoutineEnd(snapshot) {
                                  return async function () {
                                    //--- Ending Routine 'retrieval_backg_info' ---
                                    for (const thisComponent of retrieval_backg_infoComponents) {
                                      if (typeof thisComponent.setAutoDraw === 'function') {
                                        thisComponent.setAutoDraw(false);
                                      }
                                    }
                                    psychoJS.experiment.addData('retrieval_backg_info.stopped', globalClock.getTime());
                                    // update the trial handler
                                    if (currentLoop instanceof MultiStairHandler) {
                                      currentLoop.addResponse(continue_button_15.corr, level);
                                    }
                                    psychoJS.experiment.addData('continue_button_15.keys', continue_button_15.keys);
                                    if (typeof continue_button_15.keys !== 'undefined') {  // we had a response
                                        psychoJS.experiment.addData('continue_button_15.rt', continue_button_15.rt);
                                        psychoJS.experiment.addData('continue_button_15.duration', continue_button_15.duration);
                                        routineTimer.reset();
                                        }
                                    
                                    continue_button_15.stop();
                                    // the Routine "retrieval_backg_info" was not non-slip safe, so reset the non-slip timer
                                    routineTimer.reset();
                                    
                                    // Routines running outside a loop should always advance the datafile row
                                    if (currentLoop === psychoJS.experiment) {
                                      psychoJS.experiment.nextEntry(snapshot);
                                    }
                                    return Scheduler.Event.NEXT;
                                  }
                                }
                                
                                function instruction_practice_type1RoutineBegin(snapshot) {
                                  return async function () {
                                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                    
                                    //--- Prepare to start Routine 'instruction_practice_type1' ---
                                    t = 0;
                                    frameN = -1;
                                    continueRoutine = true; // until we're told otherwise
                                    // keep track of whether this Routine was forcibly ended
                                    routineForceEnded = false;
                                    instruction_practice_type1Clock.reset();
                                    routineTimer.reset();
                                    instruction_practice_type1MaxDurationReached = false;
                                    // update component parameters for each repeat
                                    // Run 'Begin Routine' code from instruction_part8_text
                                    if ((language === "english")) {
                                        instruction_part8.text = "You are now ready to practice the retrieval trials.\n\nPlese remember to use the periods after the two images were shown to think\nabout the order and distance questions.\n\nPress any key to start the retrieval practice";
                                    }
                                    if ((language === "german")) {
                                        instruction_part8.text = "Sie sind nun bereit, die Abrufdurchg\u00e4nge zu \u00fcben.\n\nNutzen Sie die kurze Pause nach der Bildpr\u00e4sentation,\num bereits \u00fcber die Reihenfolge und die Distanz nachzudenken.\n\nDr\u00fccken Sie eine beliebige Taste, um die \u00dcbung zu starten.";
                                    }
                                    
                                    continue_button_9.keys = undefined;
                                    continue_button_9.rt = undefined;
                                    _continue_button_9_allKeys = [];
                                    // Run 'Begin Routine' code from initialize_practice_errors
                                    practice_errors = 0;
                                    
                                    psychoJS.experiment.addData('instruction_practice_type1.started', globalClock.getTime());
                                    instruction_practice_type1MaxDuration = null
                                    // keep track of which components have finished
                                    instruction_practice_type1Components = [];
                                    instruction_practice_type1Components.push(instruction_part8);
                                    instruction_practice_type1Components.push(continue_button_9);
                                    
                                    for (const thisComponent of instruction_practice_type1Components)
                                      if ('status' in thisComponent)
                                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                    return Scheduler.Event.NEXT;
                                  }
                                }
                                
                                function instruction_practice_type1RoutineEachFrame() {
                                  return async function () {
                                    //--- Loop for each frame of Routine 'instruction_practice_type1' ---
                                    // get current time
                                    t = instruction_practice_type1Clock.getTime();
                                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                    // update/draw components on each frame
                                    
                                    // *instruction_part8* updates
                                    if (t >= 0.0 && instruction_part8.status === PsychoJS.Status.NOT_STARTED) {
                                      // keep track of start time/frame for later
                                      instruction_part8.tStart = t;  // (not accounting for frame time here)
                                      instruction_part8.frameNStart = frameN;  // exact frame index
                                      
                                      instruction_part8.setAutoDraw(true);
                                    }
                                    
                                    
                                    // if instruction_part8 is active this frame...
                                    if (instruction_part8.status === PsychoJS.Status.STARTED) {
                                    }
                                    
                                    frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                    if (instruction_part8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                      // keep track of stop time/frame for later
                                      instruction_part8.tStop = t;  // not accounting for scr refresh
                                      instruction_part8.frameNStop = frameN;  // exact frame index
                                      // update status
                                      instruction_part8.status = PsychoJS.Status.FINISHED;
                                      instruction_part8.setAutoDraw(false);
                                    }
                                    
                                    
                                    // *continue_button_9* updates
                                    if (t >= 0.5 && continue_button_9.status === PsychoJS.Status.NOT_STARTED) {
                                      // keep track of start time/frame for later
                                      continue_button_9.tStart = t;  // (not accounting for frame time here)
                                      continue_button_9.frameNStart = frameN;  // exact frame index
                                      
                                      // keyboard checking is just starting
                                      psychoJS.window.callOnFlip(function() { continue_button_9.clock.reset(); });  // t=0 on next screen flip
                                      psychoJS.window.callOnFlip(function() { continue_button_9.start(); }); // start on screen flip
                                      psychoJS.window.callOnFlip(function() { continue_button_9.clearEvents(); });
                                    }
                                    frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                    if (continue_button_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                      // keep track of stop time/frame for later
                                      continue_button_9.tStop = t;  // not accounting for scr refresh
                                      continue_button_9.frameNStop = frameN;  // exact frame index
                                      // update status
                                      continue_button_9.status = PsychoJS.Status.FINISHED;
                                      frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (continue_button_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        continue_button_9.tStop = t;  // not accounting for scr refresh
                                        continue_button_9.frameNStop = frameN;  // exact frame index
                                        // update status
                                        continue_button_9.status = PsychoJS.Status.FINISHED;
                                        continue_button_9.status = PsychoJS.Status.FINISHED;
                                          }
                                        
                                      }
                                      
                                      // if continue_button_9 is active this frame...
                                      if (continue_button_9.status === PsychoJS.Status.STARTED) {
                                        let theseKeys = continue_button_9.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                        _continue_button_9_allKeys = _continue_button_9_allKeys.concat(theseKeys);
                                        if (_continue_button_9_allKeys.length > 0) {
                                          continue_button_9.keys = _continue_button_9_allKeys[0].name;  // just the first key pressed
                                          continue_button_9.rt = _continue_button_9_allKeys[0].rt;
                                          continue_button_9.duration = _continue_button_9_allKeys[0].duration;
                                          // a response ends the routine
                                          continueRoutine = false;
                                        }
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of instruction_practice_type1Components)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function instruction_practice_type1RoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'instruction_practice_type1' ---
                                      for (const thisComponent of instruction_practice_type1Components) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('instruction_practice_type1.stopped', globalClock.getTime());
                                      // update the trial handler
                                      if (currentLoop instanceof MultiStairHandler) {
                                        currentLoop.addResponse(continue_button_9.corr, level);
                                      }
                                      psychoJS.experiment.addData('continue_button_9.keys', continue_button_9.keys);
                                      if (typeof continue_button_9.keys !== 'undefined') {  // we had a response
                                          psychoJS.experiment.addData('continue_button_9.rt', continue_button_9.rt);
                                          psychoJS.experiment.addData('continue_button_9.duration', continue_button_9.duration);
                                          routineTimer.reset();
                                          }
                                      
                                      continue_button_9.stop();
                                      // the Routine "instruction_practice_type1" was not non-slip safe, so reset the non-slip timer
                                      routineTimer.reset();
                                      
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function retrieval_type1_practiceRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'retrieval_type1_practice' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      retrieval_type1_practiceClock.reset();
                                      routineTimer.reset();
                                      retrieval_type1_practiceMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      fix_cross_retrbegin.setText('+');
                                      psychoJS.experiment.addData('retrieval_type1_practice.started', globalClock.getTime());
                                      retrieval_type1_practiceMaxDuration = null
                                      // keep track of which components have finished
                                      retrieval_type1_practiceComponents = [];
                                      retrieval_type1_practiceComponents.push(fix_cross_retrbegin);
                                      
                                      for (const thisComponent of retrieval_type1_practiceComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function retrieval_type1_practiceRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'retrieval_type1_practice' ---
                                      // get current time
                                      t = retrieval_type1_practiceClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *fix_cross_retrbegin* updates
                                      if (t >= 0.0 && fix_cross_retrbegin.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        fix_cross_retrbegin.tStart = t;  // (not accounting for frame time here)
                                        fix_cross_retrbegin.frameNStart = frameN;  // exact frame index
                                        
                                        fix_cross_retrbegin.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if fix_cross_retrbegin is active this frame...
                                      if (fix_cross_retrbegin.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + iti_dur_retr - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (fix_cross_retrbegin.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        fix_cross_retrbegin.tStop = t;  // not accounting for scr refresh
                                        fix_cross_retrbegin.frameNStop = frameN;  // exact frame index
                                        // update status
                                        fix_cross_retrbegin.status = PsychoJS.Status.FINISHED;
                                        fix_cross_retrbegin.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of retrieval_type1_practiceComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function retrieval_type1_practiceRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'retrieval_type1_practice' ---
                                      for (const thisComponent of retrieval_type1_practiceComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('retrieval_type1_practice.stopped', globalClock.getTime());
                                      // the Routine "retrieval_type1_practice" was not non-slip safe, so reset the non-slip timer
                                      routineTimer.reset();
                                      
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function first_image_prcRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'first_image_prc' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      first_image_prcClock.reset();
                                      routineTimer.reset();
                                      first_image_prcMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      image_1_prc.setImage(img_first);
                                      info_example_3.setImage(ImageExamplePath);
                                      psychoJS.experiment.addData('first_image_prc.started', globalClock.getTime());
                                      first_image_prcMaxDuration = null
                                      // keep track of which components have finished
                                      first_image_prcComponents = [];
                                      first_image_prcComponents.push(image_1_prc);
                                      first_image_prcComponents.push(info_example_3);
                                      
                                      for (const thisComponent of first_image_prcComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function first_image_prcRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'first_image_prc' ---
                                      // get current time
                                      t = first_image_prcClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *image_1_prc* updates
                                      if (t >= 0.0 && image_1_prc.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        image_1_prc.tStart = t;  // (not accounting for frame time here)
                                        image_1_prc.frameNStart = frameN;  // exact frame index
                                        
                                        image_1_prc.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if image_1_prc is active this frame...
                                      if (image_1_prc.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (image_dur_retr_new + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (image_1_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        image_1_prc.tStop = t;  // not accounting for scr refresh
                                        image_1_prc.frameNStop = frameN;  // exact frame index
                                        // update status
                                        image_1_prc.status = PsychoJS.Status.FINISHED;
                                        image_1_prc.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *info_example_3* updates
                                      if (t >= 0.0 && info_example_3.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        info_example_3.tStart = t;  // (not accounting for frame time here)
                                        info_example_3.frameNStart = frameN;  // exact frame index
                                        
                                        info_example_3.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if info_example_3 is active this frame...
                                      if (info_example_3.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (image_dur_retr_new + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (info_example_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        info_example_3.tStop = t;  // not accounting for scr refresh
                                        info_example_3.frameNStop = frameN;  // exact frame index
                                        // update status
                                        info_example_3.status = PsychoJS.Status.FINISHED;
                                        info_example_3.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of first_image_prcComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function first_image_prcRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'first_image_prc' ---
                                      for (const thisComponent of first_image_prcComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('first_image_prc.stopped', globalClock.getTime());
                                      // the Routine "first_image_prc" was not non-slip safe, so reset the non-slip timer
                                      routineTimer.reset();
                                      
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function mask_retr1_prcRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'mask_retr1_prc' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      mask_retr1_prcClock.reset(routineTimer.getTime());
                                      routineTimer.add(0.250000);
                                      mask_retr1_prcMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      info_example_4.setImage(ImageExamplePath);
                                      psychoJS.experiment.addData('mask_retr1_prc.started', globalClock.getTime());
                                      mask_retr1_prcMaxDuration = null
                                      // keep track of which components have finished
                                      mask_retr1_prcComponents = [];
                                      mask_retr1_prcComponents.push(mask_img1);
                                      mask_retr1_prcComponents.push(info_example_4);
                                      
                                      for (const thisComponent of mask_retr1_prcComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function mask_retr1_prcRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'mask_retr1_prc' ---
                                      // get current time
                                      t = mask_retr1_prcClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *mask_img1* updates
                                      if (t >= 0.0 && mask_img1.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        mask_img1.tStart = t;  // (not accounting for frame time here)
                                        mask_img1.frameNStart = frameN;  // exact frame index
                                        
                                        mask_img1.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if mask_img1 is active this frame...
                                      if (mask_img1.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (mask_img1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        mask_img1.tStop = t;  // not accounting for scr refresh
                                        mask_img1.frameNStop = frameN;  // exact frame index
                                        // update status
                                        mask_img1.status = PsychoJS.Status.FINISHED;
                                        mask_img1.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *info_example_4* updates
                                      if (t >= 0.0 && info_example_4.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        info_example_4.tStart = t;  // (not accounting for frame time here)
                                        info_example_4.frameNStart = frameN;  // exact frame index
                                        
                                        info_example_4.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if info_example_4 is active this frame...
                                      if (info_example_4.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (info_example_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        info_example_4.tStop = t;  // not accounting for scr refresh
                                        info_example_4.frameNStop = frameN;  // exact frame index
                                        // update status
                                        info_example_4.status = PsychoJS.Status.FINISHED;
                                        info_example_4.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of mask_retr1_prcComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine && routineTimer.getTime() > 0) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function mask_retr1_prcRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'mask_retr1_prc' ---
                                      for (const thisComponent of mask_retr1_prcComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('mask_retr1_prc.stopped', globalClock.getTime());
                                      if (routineForceEnded) {
                                          routineTimer.reset();} else if (mask_retr1_prcMaxDurationReached) {
                                          mask_retr1_prcClock.add(mask_retr1_prcMaxDuration);
                                      } else {
                                          mask_retr1_prcClock.add(0.250000);
                                      }
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function second_image_prcRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'second_image_prc' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      second_image_prcClock.reset();
                                      routineTimer.reset();
                                      second_image_prcMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      image_2_prc.setImage(img_second);
                                      info_example_5.setImage(ImageExamplePath);
                                      psychoJS.experiment.addData('second_image_prc.started', globalClock.getTime());
                                      second_image_prcMaxDuration = null
                                      // keep track of which components have finished
                                      second_image_prcComponents = [];
                                      second_image_prcComponents.push(image_2_prc);
                                      second_image_prcComponents.push(info_example_5);
                                      
                                      for (const thisComponent of second_image_prcComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function second_image_prcRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'second_image_prc' ---
                                      // get current time
                                      t = second_image_prcClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *image_2_prc* updates
                                      if (t >= 0.0 && image_2_prc.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        image_2_prc.tStart = t;  // (not accounting for frame time here)
                                        image_2_prc.frameNStart = frameN;  // exact frame index
                                        
                                        image_2_prc.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if image_2_prc is active this frame...
                                      if (image_2_prc.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (image_dur_retr_new + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (image_2_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        image_2_prc.tStop = t;  // not accounting for scr refresh
                                        image_2_prc.frameNStop = frameN;  // exact frame index
                                        // update status
                                        image_2_prc.status = PsychoJS.Status.FINISHED;
                                        image_2_prc.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *info_example_5* updates
                                      if (t >= 0.0 && info_example_5.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        info_example_5.tStart = t;  // (not accounting for frame time here)
                                        info_example_5.frameNStart = frameN;  // exact frame index
                                        
                                        info_example_5.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if info_example_5 is active this frame...
                                      if (info_example_5.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (image_dur_retr_new + 0.5) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (info_example_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        info_example_5.tStop = t;  // not accounting for scr refresh
                                        info_example_5.frameNStop = frameN;  // exact frame index
                                        // update status
                                        info_example_5.status = PsychoJS.Status.FINISHED;
                                        info_example_5.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of second_image_prcComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function second_image_prcRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'second_image_prc' ---
                                      for (const thisComponent of second_image_prcComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('second_image_prc.stopped', globalClock.getTime());
                                      // the Routine "second_image_prc" was not non-slip safe, so reset the non-slip timer
                                      routineTimer.reset();
                                      
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function mask_retr2_prcRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'mask_retr2_prc' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      mask_retr2_prcClock.reset(routineTimer.getTime());
                                      routineTimer.add(0.250000);
                                      mask_retr2_prcMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      info_example_6.setImage(ImageExamplePath);
                                      psychoJS.experiment.addData('mask_retr2_prc.started', globalClock.getTime());
                                      mask_retr2_prcMaxDuration = null
                                      // keep track of which components have finished
                                      mask_retr2_prcComponents = [];
                                      mask_retr2_prcComponents.push(mask_img2);
                                      mask_retr2_prcComponents.push(info_example_6);
                                      
                                      for (const thisComponent of mask_retr2_prcComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function mask_retr2_prcRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'mask_retr2_prc' ---
                                      // get current time
                                      t = mask_retr2_prcClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *mask_img2* updates
                                      if (t >= 0.0 && mask_img2.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        mask_img2.tStart = t;  // (not accounting for frame time here)
                                        mask_img2.frameNStart = frameN;  // exact frame index
                                        
                                        mask_img2.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if mask_img2 is active this frame...
                                      if (mask_img2.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (mask_img2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        mask_img2.tStop = t;  // not accounting for scr refresh
                                        mask_img2.frameNStop = frameN;  // exact frame index
                                        // update status
                                        mask_img2.status = PsychoJS.Status.FINISHED;
                                        mask_img2.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *info_example_6* updates
                                      if (t >= 0.0 && info_example_6.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        info_example_6.tStart = t;  // (not accounting for frame time here)
                                        info_example_6.frameNStart = frameN;  // exact frame index
                                        
                                        info_example_6.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if info_example_6 is active this frame...
                                      if (info_example_6.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (info_example_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        info_example_6.tStop = t;  // not accounting for scr refresh
                                        info_example_6.frameNStop = frameN;  // exact frame index
                                        // update status
                                        info_example_6.status = PsychoJS.Status.FINISHED;
                                        info_example_6.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of mask_retr2_prcComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine && routineTimer.getTime() > 0) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function mask_retr2_prcRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'mask_retr2_prc' ---
                                      for (const thisComponent of mask_retr2_prcComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('mask_retr2_prc.stopped', globalClock.getTime());
                                      if (routineForceEnded) {
                                          routineTimer.reset();} else if (mask_retr2_prcMaxDurationReached) {
                                          mask_retr2_prcClock.add(mask_retr2_prcMaxDuration);
                                      } else {
                                          mask_retr2_prcClock.add(0.250000);
                                      }
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function reflection_periodRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'reflection_period' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      reflection_periodClock.reset();
                                      routineTimer.reset();
                                      reflection_periodMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      psychoJS.experiment.addData('reflection_period.started', globalClock.getTime());
                                      reflection_periodMaxDuration = null
                                      // keep track of which components have finished
                                      reflection_periodComponents = [];
                                      reflection_periodComponents.push(fix_cross_reflretr_2);
                                      reflection_periodComponents.push(text);
                                      
                                      for (const thisComponent of reflection_periodComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function reflection_periodRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'reflection_period' ---
                                      // get current time
                                      t = reflection_periodClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *fix_cross_reflretr_2* updates
                                      if (t >= 0.0 && fix_cross_reflretr_2.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        fix_cross_reflretr_2.tStart = t;  // (not accounting for frame time here)
                                        fix_cross_reflretr_2.frameNStart = frameN;  // exact frame index
                                        
                                        fix_cross_reflretr_2.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if fix_cross_reflretr_2 is active this frame...
                                      if (fix_cross_reflretr_2.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (reflection_win_dur + 2) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (fix_cross_reflretr_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        fix_cross_reflretr_2.tStop = t;  // not accounting for scr refresh
                                        fix_cross_reflretr_2.frameNStop = frameN;  // exact frame index
                                        // update status
                                        fix_cross_reflretr_2.status = PsychoJS.Status.FINISHED;
                                        fix_cross_reflretr_2.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *text* updates
                                      if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        text.tStart = t;  // (not accounting for frame time here)
                                        text.frameNStart = frameN;  // exact frame index
                                        
                                        text.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if text is active this frame...
                                      if (text.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + (reflection_win_dur + 2) - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        text.tStop = t;  // not accounting for scr refresh
                                        text.frameNStop = frameN;  // exact frame index
                                        // update status
                                        text.status = PsychoJS.Status.FINISHED;
                                        text.setAutoDraw(false);
                                      }
                                      
                                      // check for quit (typically the Esc key)
                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                      }
                                      
                                      // check if the Routine should terminate
                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                        routineForceEnded = true;
                                        return Scheduler.Event.NEXT;
                                      }
                                      
                                      continueRoutine = false;  // reverts to True if at least one component still running
                                      for (const thisComponent of reflection_periodComponents)
                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                          continueRoutine = true;
                                          break;
                                        }
                                      
                                      // refresh the screen if continuing
                                      if (continueRoutine) {
                                        return Scheduler.Event.FLIP_REPEAT;
                                      } else {
                                        return Scheduler.Event.NEXT;
                                      }
                                    };
                                  }
                                  
                                  function reflection_periodRoutineEnd(snapshot) {
                                    return async function () {
                                      //--- Ending Routine 'reflection_period' ---
                                      for (const thisComponent of reflection_periodComponents) {
                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                          thisComponent.setAutoDraw(false);
                                        }
                                      }
                                      psychoJS.experiment.addData('reflection_period.stopped', globalClock.getTime());
                                      // the Routine "reflection_period" was not non-slip safe, so reset the non-slip timer
                                      routineTimer.reset();
                                      
                                      // Routines running outside a loop should always advance the datafile row
                                      if (currentLoop === psychoJS.experiment) {
                                        psychoJS.experiment.nextEntry(snapshot);
                                      }
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function retr_response_order_prcRoutineBegin(snapshot) {
                                    return async function () {
                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                      
                                      //--- Prepare to start Routine 'retr_response_order_prc' ---
                                      t = 0;
                                      frameN = -1;
                                      continueRoutine = true; // until we're told otherwise
                                      // keep track of whether this Routine was forcibly ended
                                      routineForceEnded = false;
                                      retr_response_order_prcClock.reset();
                                      routineTimer.reset();
                                      retr_response_order_prcMaxDurationReached = false;
                                      // update component parameters for each repeat
                                      // Run 'Begin Routine' code from clear_clock
                                      window.retr_response_prcMaxDuration = null; 
                                      window.retr_response_prcComponents = null; 
                                      
                                      window._resp_2_allKeys = null; 
                                      resp_2.clearEvents();
                                      
                                      window.retrClock = new util.Clock();
                                      window.retrClock.reset();
                                      yes_txt_3.setPos((leftside_retr if (opt_left == 'yes') else rightside_retr));
                                      no_txt_3.setPos((rightside_retr if (opt_right == 'no') else leftside_retr));
                                      resp_3.keys = undefined;
                                      resp_3.rt = undefined;
                                      _resp_3_allKeys = [];
                                      // Run 'Begin Routine' code from set_option_text
                                      if ((language === "english")) {
                                          yes_txt_3.text = "yes";
                                          no_txt_3.text = "no";
                                      }
                                      if ((language === "german")) {
                                          yes_txt_3.text = "ja";
                                          no_txt_3.text = "nein";
                                      }
                                      if ((language === "french")) {
                                          yes_txt_3.text = "oui";
                                          no_txt_3.text = "non";
                                      }
                                      
                                      // Run 'Begin Routine' code from end_routine_after_resp_2
                                      window.responded_retr = false;
                                      window.delayClock = null;
                                      // Begin Routine
                                      window.delayDone = false;
                                      info_example_7.setImage(ImageExamplePath);
                                      psychoJS.experiment.addData('retr_response_order_prc.started', globalClock.getTime());
                                      retr_response_order_prcMaxDuration = null
                                      // keep track of which components have finished
                                      retr_response_order_prcComponents = [];
                                      retr_response_order_prcComponents.push(yes_txt_3);
                                      retr_response_order_prcComponents.push(no_txt_3);
                                      retr_response_order_prcComponents.push(polygon_9);
                                      retr_response_order_prcComponents.push(resp_3);
                                      retr_response_order_prcComponents.push(info_example_7);
                                      
                                      for (const thisComponent of retr_response_order_prcComponents)
                                        if ('status' in thisComponent)
                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                      return Scheduler.Event.NEXT;
                                    }
                                  }
                                  
                                  function retr_response_order_prcRoutineEachFrame() {
                                    return async function () {
                                      //--- Loop for each frame of Routine 'retr_response_order_prc' ---
                                      // get current time
                                      t = retr_response_order_prcClock.getTime();
                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                      // update/draw components on each frame
                                      
                                      // *yes_txt_3* updates
                                      if (t >= 0.0 && yes_txt_3.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        yes_txt_3.tStart = t;  // (not accounting for frame time here)
                                        yes_txt_3.frameNStart = frameN;  // exact frame index
                                        
                                        yes_txt_3.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if yes_txt_3 is active this frame...
                                      if (yes_txt_3.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (yes_txt_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        yes_txt_3.tStop = t;  // not accounting for scr refresh
                                        yes_txt_3.frameNStop = frameN;  // exact frame index
                                        // update status
                                        yes_txt_3.status = PsychoJS.Status.FINISHED;
                                        yes_txt_3.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *no_txt_3* updates
                                      if (t >= 0.0 && no_txt_3.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        no_txt_3.tStart = t;  // (not accounting for frame time here)
                                        no_txt_3.frameNStart = frameN;  // exact frame index
                                        
                                        no_txt_3.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if no_txt_3 is active this frame...
                                      if (no_txt_3.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (no_txt_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        no_txt_3.tStop = t;  // not accounting for scr refresh
                                        no_txt_3.frameNStop = frameN;  // exact frame index
                                        // update status
                                        no_txt_3.status = PsychoJS.Status.FINISHED;
                                        no_txt_3.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *polygon_9* updates
                                      if (t >= 0.0 && polygon_9.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        polygon_9.tStart = t;  // (not accounting for frame time here)
                                        polygon_9.frameNStart = frameN;  // exact frame index
                                        
                                        polygon_9.setAutoDraw(true);
                                      }
                                      
                                      
                                      // if polygon_9 is active this frame...
                                      if (polygon_9.status === PsychoJS.Status.STARTED) {
                                      }
                                      
                                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (polygon_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        polygon_9.tStop = t;  // not accounting for scr refresh
                                        polygon_9.frameNStop = frameN;  // exact frame index
                                        // update status
                                        polygon_9.status = PsychoJS.Status.FINISHED;
                                        polygon_9.setAutoDraw(false);
                                      }
                                      
                                      
                                      // *resp_3* updates
                                      if (t >= 0.0 && resp_3.status === PsychoJS.Status.NOT_STARTED) {
                                        // keep track of start time/frame for later
                                        resp_3.tStart = t;  // (not accounting for frame time here)
                                        resp_3.frameNStart = frameN;  // exact frame index
                                        
                                        // keyboard checking is just starting
                                        resp_3.clock.reset();
                                        resp_3.start();
                                        resp_3.clearEvents();
                                      }
                                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                      if (resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                        // keep track of stop time/frame for later
                                        resp_3.tStop = t;  // not accounting for scr refresh
                                        resp_3.frameNStop = frameN;  // exact frame index
                                        // update status
                                        resp_3.status = PsychoJS.Status.FINISHED;
                                        frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                        if (resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                          // keep track of stop time/frame for later
                                          resp_3.tStop = t;  // not accounting for scr refresh
                                          resp_3.frameNStop = frameN;  // exact frame index
                                          // update status
                                          resp_3.status = PsychoJS.Status.FINISHED;
                                          resp_3.status = PsychoJS.Status.FINISHED;
                                            }
                                          
                                        }
                                        
                                        // if resp_3 is active this frame...
                                        if (resp_3.status === PsychoJS.Status.STARTED) {
                                          let theseKeys = resp_3.getKeys({keyList: [left_key,right_key], waitRelease: true});
                                          _resp_3_allKeys = _resp_3_allKeys.concat(theseKeys);
                                          if (_resp_3_allKeys.length > 0) {
                                            resp_3.keys = _resp_3_allKeys[_resp_3_allKeys.length - 1].name;  // just the last key pressed
                                            resp_3.rt = _resp_3_allKeys[_resp_3_allKeys.length - 1].rt;
                                            resp_3.duration = _resp_3_allKeys[_resp_3_allKeys.length - 1].duration;
                                          }
                                        }
                                        
                                        // Run 'Each Frame' code from end_routine_after_resp_2
                                        if (retrClock.getTime() >= max_read_dur) {
                                            // Timeout
                                            responded_retr = false;
                                            continueRoutine = false;
                                        } 
                                        
                                        
                                        if (!responded_retr) {
                                            let key_list = resp_3.getKeys({ keyList: [left_key, right_key, "return"], waitRelease: false });
                                          if (key_list.length > 0) {
                                            responded_retr = true;
                                            let thisResp = key_list[0];
                                            chosenPos;
                                            if (thisResp.name === window.left_key)        chosenPos = [-0.06, 0];
                                            else if (thisResp.name === window.right_key)  chosenPos = [0.06, 0];
                                            resp_3.keys = thisResp.name;
                                            resp_3.rt = thisResp.rt;
                                            resp_3.duration = thisResp.duration;
                                            if (thisResp.name === correct_key) {
                                                resp_3.corr = 1;
                                            } else {
                                                resp_3.corr = 0;
                                                practice_errors += 1;
                                            }
                                            polygon_9.setPos(chosenPos);
                                            polygon_9.setOpacity(1.0);
                                            delayClock = new util.Clock();
                                        }
                                        }
                                        
                                        if (responded_retr && !delayDone && delayClock !== null && delayClock.getTime() >= 0.1) {
                                          delayDone = true;
                                          continueRoutine = false;
                                        }
                                          
                                        
                                        
                                        // *info_example_7* updates
                                        if (t >= 0.0 && info_example_7.status === PsychoJS.Status.NOT_STARTED) {
                                          // keep track of start time/frame for later
                                          info_example_7.tStart = t;  // (not accounting for frame time here)
                                          info_example_7.frameNStart = frameN;  // exact frame index
                                          
                                          info_example_7.setAutoDraw(true);
                                        }
                                        
                                        
                                        // if info_example_7 is active this frame...
                                        if (info_example_7.status === PsychoJS.Status.STARTED) {
                                        }
                                        
                                        frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                        if (info_example_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                          // keep track of stop time/frame for later
                                          info_example_7.tStop = t;  // not accounting for scr refresh
                                          info_example_7.frameNStop = frameN;  // exact frame index
                                          // update status
                                          info_example_7.status = PsychoJS.Status.FINISHED;
                                          info_example_7.setAutoDraw(false);
                                        }
                                        
                                        // check for quit (typically the Esc key)
                                        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                        }
                                        
                                        // check if the Routine should terminate
                                        if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                          routineForceEnded = true;
                                          return Scheduler.Event.NEXT;
                                        }
                                        
                                        continueRoutine = false;  // reverts to True if at least one component still running
                                        for (const thisComponent of retr_response_order_prcComponents)
                                          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                            continueRoutine = true;
                                            break;
                                          }
                                        
                                        // refresh the screen if continuing
                                        if (continueRoutine) {
                                          return Scheduler.Event.FLIP_REPEAT;
                                        } else {
                                          return Scheduler.Event.NEXT;
                                        }
                                      };
                                    }
                                    
                                    function retr_response_order_prcRoutineEnd(snapshot) {
                                      return async function () {
                                        //--- Ending Routine 'retr_response_order_prc' ---
                                        for (const thisComponent of retr_response_order_prcComponents) {
                                          if (typeof thisComponent.setAutoDraw === 'function') {
                                            thisComponent.setAutoDraw(false);
                                          }
                                        }
                                        psychoJS.experiment.addData('retr_response_order_prc.stopped', globalClock.getTime());
                                        // update the trial handler
                                        if (currentLoop instanceof MultiStairHandler) {
                                          currentLoop.addResponse(resp_3.corr, level);
                                        }
                                        psychoJS.experiment.addData('resp_3.keys', resp_3.keys);
                                        if (typeof resp_3.keys !== 'undefined') {  // we had a response
                                            psychoJS.experiment.addData('resp_3.rt', resp_3.rt);
                                            psychoJS.experiment.addData('resp_3.duration', resp_3.duration);
                                            }
                                        
                                        resp_3.stop();
                                        if ((trial_type === 1 || trial_type === 2) && !responded_retr) {
                                            practice_errors += 1;
                                            resp_2.corr = 0; 
                                            console.log("No response given, practice_errors:", practice_errors);
                                        }
                                        // the Routine "retr_response_order_prc" was not non-slip safe, so reset the non-slip timer
                                        routineTimer.reset();
                                        
                                        // Routines running outside a loop should always advance the datafile row
                                        if (currentLoop === psychoJS.experiment) {
                                          psychoJS.experiment.nextEntry(snapshot);
                                        }
                                        return Scheduler.Event.NEXT;
                                      }
                                    }
                                    
                                    function retr_response_distance_prcRoutineBegin(snapshot) {
                                      return async function () {
                                        TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                        
                                        //--- Prepare to start Routine 'retr_response_distance_prc' ---
                                        t = 0;
                                        frameN = -1;
                                        continueRoutine = true; // until we're told otherwise
                                        // keep track of whether this Routine was forcibly ended
                                        routineForceEnded = false;
                                        retr_response_distance_prcClock.reset();
                                        routineTimer.reset();
                                        retr_response_distance_prcMaxDurationReached = false;
                                        // update component parameters for each repeat
                                        // Run 'Begin Routine' code from clear_clock_2
                                        window.retr_response_prcMaxDuration = null; 
                                        window.retr_response_prcComponents = null; 
                                        
                                        window._resp_2_allKeys = null; 
                                        resp_2.clearEvents();
                                        
                                        window.retrClock = new util.Clock();
                                        window.retrClock.reset();
                                        resp_2.keys = undefined;
                                        resp_2.rt = undefined;
                                        _resp_2_allKeys = [];
                                        // Run 'Begin Routine' code from controlslider_pos_js_2
                                        
                                        
                                        window.responded_retr_slider = false; 
                                        info_example.setImage(ImageExamplePath);
                                        opt_2_prc.setColor(new util.Color('white'));
                                        opt_3_prc.setColor(new util.Color('white'));
                                        opt_4_prc.setColor(new util.Color('white'));
                                        opt_5_prc.setColor(new util.Color('white'));
                                        psychoJS.experiment.addData('retr_response_distance_prc.started', globalClock.getTime());
                                        retr_response_distance_prcMaxDuration = null
                                        // keep track of which components have finished
                                        retr_response_distance_prcComponents = [];
                                        retr_response_distance_prcComponents.push(resp_2);
                                        retr_response_distance_prcComponents.push(info_example);
                                        retr_response_distance_prcComponents.push(opt_2_prc);
                                        retr_response_distance_prcComponents.push(opt_3_prc);
                                        retr_response_distance_prcComponents.push(opt_4_prc);
                                        retr_response_distance_prcComponents.push(opt_5_prc);
                                        
                                        for (const thisComponent of retr_response_distance_prcComponents)
                                          if ('status' in thisComponent)
                                            thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                        return Scheduler.Event.NEXT;
                                      }
                                    }
                                    
                                    function retr_response_distance_prcRoutineEachFrame() {
                                      return async function () {
                                        //--- Loop for each frame of Routine 'retr_response_distance_prc' ---
                                        // get current time
                                        t = retr_response_distance_prcClock.getTime();
                                        frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                        // update/draw components on each frame
                                        
                                        // *resp_2* updates
                                        if (t >= 0.0 && resp_2.status === PsychoJS.Status.NOT_STARTED) {
                                          // keep track of start time/frame for later
                                          resp_2.tStart = t;  // (not accounting for frame time here)
                                          resp_2.frameNStart = frameN;  // exact frame index
                                          
                                          // keyboard checking is just starting
                                          resp_2.clock.reset();
                                          resp_2.start();
                                          resp_2.clearEvents();
                                        }
                                        frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                        if (resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                          // keep track of stop time/frame for later
                                          resp_2.tStop = t;  // not accounting for scr refresh
                                          resp_2.frameNStop = frameN;  // exact frame index
                                          // update status
                                          resp_2.status = PsychoJS.Status.FINISHED;
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            resp_2.tStop = t;  // not accounting for scr refresh
                                            resp_2.frameNStop = frameN;  // exact frame index
                                            // update status
                                            resp_2.status = PsychoJS.Status.FINISHED;
                                            resp_2.status = PsychoJS.Status.FINISHED;
                                              }
                                            
                                          }
                                          
                                          // if resp_2 is active this frame...
                                          if (resp_2.status === PsychoJS.Status.STARTED) {
                                            let theseKeys = resp_2.getKeys({keyList: [[left_key,right_key,center_key,down_key]], waitRelease: true});
                                            _resp_2_allKeys = _resp_2_allKeys.concat(theseKeys);
                                            if (_resp_2_allKeys.length > 0) {
                                              resp_2.keys = _resp_2_allKeys[_resp_2_allKeys.length - 1].name;  // just the last key pressed
                                              resp_2.rt = _resp_2_allKeys[_resp_2_allKeys.length - 1].rt;
                                              resp_2.duration = _resp_2_allKeys[_resp_2_allKeys.length - 1].duration;
                                            }
                                          }
                                          
                                          
                                          // *info_example* updates
                                          if (t >= 0.0 && info_example.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            info_example.tStart = t;  // (not accounting for frame time here)
                                            info_example.frameNStart = frameN;  // exact frame index
                                            
                                            info_example.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if info_example is active this frame...
                                          if (info_example.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (info_example.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            info_example.tStop = t;  // not accounting for scr refresh
                                            info_example.frameNStop = frameN;  // exact frame index
                                            // update status
                                            info_example.status = PsychoJS.Status.FINISHED;
                                            info_example.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *opt_2_prc* updates
                                          if (t >= 0.0 && opt_2_prc.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            opt_2_prc.tStart = t;  // (not accounting for frame time here)
                                            opt_2_prc.frameNStart = frameN;  // exact frame index
                                            
                                            opt_2_prc.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if opt_2_prc is active this frame...
                                          if (opt_2_prc.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (opt_2_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            opt_2_prc.tStop = t;  // not accounting for scr refresh
                                            opt_2_prc.frameNStop = frameN;  // exact frame index
                                            // update status
                                            opt_2_prc.status = PsychoJS.Status.FINISHED;
                                            opt_2_prc.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *opt_3_prc* updates
                                          if (t >= 0.0 && opt_3_prc.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            opt_3_prc.tStart = t;  // (not accounting for frame time here)
                                            opt_3_prc.frameNStart = frameN;  // exact frame index
                                            
                                            opt_3_prc.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if opt_3_prc is active this frame...
                                          if (opt_3_prc.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (opt_3_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            opt_3_prc.tStop = t;  // not accounting for scr refresh
                                            opt_3_prc.frameNStop = frameN;  // exact frame index
                                            // update status
                                            opt_3_prc.status = PsychoJS.Status.FINISHED;
                                            opt_3_prc.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *opt_4_prc* updates
                                          if (t >= 0.0 && opt_4_prc.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            opt_4_prc.tStart = t;  // (not accounting for frame time here)
                                            opt_4_prc.frameNStart = frameN;  // exact frame index
                                            
                                            opt_4_prc.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if opt_4_prc is active this frame...
                                          if (opt_4_prc.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (opt_4_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            opt_4_prc.tStop = t;  // not accounting for scr refresh
                                            opt_4_prc.frameNStop = frameN;  // exact frame index
                                            // update status
                                            opt_4_prc.status = PsychoJS.Status.FINISHED;
                                            opt_4_prc.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *opt_5_prc* updates
                                          if (t >= 0.0 && opt_5_prc.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            opt_5_prc.tStart = t;  // (not accounting for frame time here)
                                            opt_5_prc.frameNStart = frameN;  // exact frame index
                                            
                                            opt_5_prc.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if opt_5_prc is active this frame...
                                          if (opt_5_prc.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (opt_5_prc.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            opt_5_prc.tStop = t;  // not accounting for scr refresh
                                            opt_5_prc.frameNStop = frameN;  // exact frame index
                                            // update status
                                            opt_5_prc.status = PsychoJS.Status.FINISHED;
                                            opt_5_prc.setAutoDraw(false);
                                          }
                                          
                                          // check for quit (typically the Esc key)
                                          if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                            return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                          }
                                          
                                          // check if the Routine should terminate
                                          if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                            routineForceEnded = true;
                                            return Scheduler.Event.NEXT;
                                          }
                                          
                                          continueRoutine = false;  // reverts to True if at least one component still running
                                          for (const thisComponent of retr_response_distance_prcComponents)
                                            if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                              continueRoutine = true;
                                              break;
                                            }
                                          
                                          // refresh the screen if continuing
                                          if (continueRoutine) {
                                            return Scheduler.Event.FLIP_REPEAT;
                                          } else {
                                            return Scheduler.Event.NEXT;
                                          }
                                        };
                                      }
                                      
                                      function retr_response_distance_prcRoutineEnd(snapshot) {
                                        return async function () {
                                          //--- Ending Routine 'retr_response_distance_prc' ---
                                          for (const thisComponent of retr_response_distance_prcComponents) {
                                            if (typeof thisComponent.setAutoDraw === 'function') {
                                              thisComponent.setAutoDraw(false);
                                            }
                                          }
                                          psychoJS.experiment.addData('retr_response_distance_prc.stopped', globalClock.getTime());
                                          // update the trial handler
                                          if (currentLoop instanceof MultiStairHandler) {
                                            currentLoop.addResponse(resp_2.corr, level);
                                          }
                                          psychoJS.experiment.addData('resp_2.keys', resp_2.keys);
                                          if (typeof resp_2.keys !== 'undefined') {  // we had a response
                                              psychoJS.experiment.addData('resp_2.rt', resp_2.rt);
                                              psychoJS.experiment.addData('resp_2.duration', resp_2.duration);
                                              }
                                          
                                          resp_2.stop();
                                          // Run 'End Routine' code from controlslider_pos_js_2
                                          if (trial_type === 3 && !responded_retr_slider) {
                                              practice_errors += 1;
                                              resp_2.corr = 0; 
                                          }
                                          // the Routine "retr_response_distance_prc" was not non-slip safe, so reset the non-slip timer
                                          routineTimer.reset();
                                          
                                          // Routines running outside a loop should always advance the datafile row
                                          if (currentLoop === psychoJS.experiment) {
                                            psychoJS.experiment.nextEntry(snapshot);
                                          }
                                          return Scheduler.Event.NEXT;
                                        }
                                      }
                                      
                                      function retr_response_feedbackRoutineBegin(snapshot) {
                                        return async function () {
                                          TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                          
                                          //--- Prepare to start Routine 'retr_response_feedback' ---
                                          t = 0;
                                          frameN = -1;
                                          continueRoutine = true; // until we're told otherwise
                                          // keep track of whether this Routine was forcibly ended
                                          routineForceEnded = false;
                                          retr_response_feedbackClock.reset();
                                          routineTimer.reset();
                                          retr_response_feedbackMaxDurationReached = false;
                                          // update component parameters for each repeat
                                          // Run 'Begin Routine' code from set_text_feedback
                                          if (((language === "english") && (resp_2.corr === 1))) {
                                              text_feedback.text = `Good job! You understood the retrieval task.`;
                                          }
                                          if (((language === "german") && (resp_2.corr === 1))) {
                                              text_feedback.text = `Gut gemacht! Sie haben Abruf verstanden.`;
                                          }
                                          if ((resp_2.corr === 0)) {
                                              if ((language === "english")) {
                                                  text_feedback.text = "Your answer was incorrect.\nPlease review the background information again and look at the full image sequence. Determine how many images appear between the two prompted images in that sequence. Only count the images in between them \u2014 do NOT include the two prompted images themselves.";
                                              }
                                              if ((language === "german")) {
                                                  text_feedback.text = "Ihre Antwort war falsch.\nBitte schauen Sie sich die Hintergrundinformationen noch einmal an. Bestimmen Sie, wie weit die Bilder in der gezeigten Sequenz auseinanderliegen.";
                                              }
                                          }
                                          
                                          info_example_2.setImage(ImageExamplePath);
                                          continue_button_16.keys = undefined;
                                          continue_button_16.rt = undefined;
                                          _continue_button_16_allKeys = [];
                                          // Run 'Begin Routine' code from control_retry_loop
                                          
                                          window.prc_fdbackClock = new util.Clock();
                                          window.prc_fdbackClock.reset();
                                          // Run 'Begin Routine' code from set_text_continue
                                          if (((language === "english") && (resp_2.corr === 1))) {
                                              text_continue.text = "Press RETURN to continue.";
                                          }
                                          if (((language === "german") && (resp_2.corr === 1))) {
                                              text_continue.text = "Dr\u00fccken Sie eine beliebige Taste, um weiterzumachen.";
                                          }
                                          if ((resp_2.corr === 0)) {
                                              if ((language === "english")) {
                                                  text_continue.text = "When you know the correct answer, press RETURN to answer the question again.";
                                              }
                                              if ((language === "german")) {
                                                  text_continue.text = "Wenn Sie die richtige Antwort wissen, dr\u00fccken Sie eine beliebige Taste, um die Frage noch einmal zu beantworten.";
                                              }
                                          }
                                          
                                          psychoJS.experiment.addData('retr_response_feedback.started', globalClock.getTime());
                                          retr_response_feedbackMaxDuration = null
                                          // keep track of which components have finished
                                          retr_response_feedbackComponents = [];
                                          retr_response_feedbackComponents.push(text_feedback);
                                          retr_response_feedbackComponents.push(info_example_2);
                                          retr_response_feedbackComponents.push(continue_button_16);
                                          retr_response_feedbackComponents.push(text_continue);
                                          
                                          for (const thisComponent of retr_response_feedbackComponents)
                                            if ('status' in thisComponent)
                                              thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                          return Scheduler.Event.NEXT;
                                        }
                                      }
                                      
                                      function retr_response_feedbackRoutineEachFrame() {
                                        return async function () {
                                          //--- Loop for each frame of Routine 'retr_response_feedback' ---
                                          // get current time
                                          t = retr_response_feedbackClock.getTime();
                                          frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                          // update/draw components on each frame
                                          
                                          // *text_feedback* updates
                                          if (t >= 0.0 && text_feedback.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            text_feedback.tStart = t;  // (not accounting for frame time here)
                                            text_feedback.frameNStart = frameN;  // exact frame index
                                            
                                            text_feedback.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if text_feedback is active this frame...
                                          if (text_feedback.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (text_feedback.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            text_feedback.tStop = t;  // not accounting for scr refresh
                                            text_feedback.frameNStop = frameN;  // exact frame index
                                            // update status
                                            text_feedback.status = PsychoJS.Status.FINISHED;
                                            text_feedback.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *info_example_2* updates
                                          if (((resp_2.corr == 0)) && info_example_2.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            info_example_2.tStart = t;  // (not accounting for frame time here)
                                            info_example_2.frameNStart = frameN;  // exact frame index
                                            
                                            info_example_2.setAutoDraw(true);
                                          }
                                          
                                          
                                          // if info_example_2 is active this frame...
                                          if (info_example_2.status === PsychoJS.Status.STARTED) {
                                          }
                                          
                                          if (info_example_2.status === PsychoJS.Status.STARTED && t >= (info_example_2.tStart + max_read_dur)) {
                                            // keep track of stop time/frame for later
                                            info_example_2.tStop = t;  // not accounting for scr refresh
                                            info_example_2.frameNStop = frameN;  // exact frame index
                                            // update status
                                            info_example_2.status = PsychoJS.Status.FINISHED;
                                            info_example_2.setAutoDraw(false);
                                          }
                                          
                                          
                                          // *continue_button_16* updates
                                          if (t >= 0.5 && continue_button_16.status === PsychoJS.Status.NOT_STARTED) {
                                            // keep track of start time/frame for later
                                            continue_button_16.tStart = t;  // (not accounting for frame time here)
                                            continue_button_16.frameNStart = frameN;  // exact frame index
                                            
                                            // keyboard checking is just starting
                                            psychoJS.window.callOnFlip(function() { continue_button_16.clock.reset(); });  // t=0 on next screen flip
                                            psychoJS.window.callOnFlip(function() { continue_button_16.start(); }); // start on screen flip
                                            psychoJS.window.callOnFlip(function() { continue_button_16.clearEvents(); });
                                          }
                                          frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                          if (continue_button_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                            // keep track of stop time/frame for later
                                            continue_button_16.tStop = t;  // not accounting for scr refresh
                                            continue_button_16.frameNStop = frameN;  // exact frame index
                                            // update status
                                            continue_button_16.status = PsychoJS.Status.FINISHED;
                                            frameRemains = 0.5 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                            if (continue_button_16.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                              // keep track of stop time/frame for later
                                              continue_button_16.tStop = t;  // not accounting for scr refresh
                                              continue_button_16.frameNStop = frameN;  // exact frame index
                                              // update status
                                              continue_button_16.status = PsychoJS.Status.FINISHED;
                                              continue_button_16.status = PsychoJS.Status.FINISHED;
                                                }
                                              
                                            }
                                            
                                            // if continue_button_16 is active this frame...
                                            if (continue_button_16.status === PsychoJS.Status.STARTED) {
                                              let theseKeys = continue_button_16.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                              _continue_button_16_allKeys = _continue_button_16_allKeys.concat(theseKeys);
                                              if (_continue_button_16_allKeys.length > 0) {
                                                continue_button_16.keys = _continue_button_16_allKeys[0].name;  // just the first key pressed
                                                continue_button_16.rt = _continue_button_16_allKeys[0].rt;
                                                continue_button_16.duration = _continue_button_16_allKeys[0].duration;
                                                // a response ends the routine
                                                continueRoutine = false;
                                              }
                                            }
                                            
                                            // Run 'Each Frame' code from control_retry_loop
                                            if (prc_fdbackClock.getTime() >= max_read_dur) {
                                                // Timeout
                                                continueRoutine = false;
                                            } 
                                            
                                            
                                            // *text_continue* updates
                                            if (t >= 0.0 && text_continue.status === PsychoJS.Status.NOT_STARTED) {
                                              // keep track of start time/frame for later
                                              text_continue.tStart = t;  // (not accounting for frame time here)
                                              text_continue.frameNStart = frameN;  // exact frame index
                                              
                                              text_continue.setAutoDraw(true);
                                            }
                                            
                                            
                                            // if text_continue is active this frame...
                                            if (text_continue.status === PsychoJS.Status.STARTED) {
                                            }
                                            
                                            frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                            if (text_continue.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                              // keep track of stop time/frame for later
                                              text_continue.tStop = t;  // not accounting for scr refresh
                                              text_continue.frameNStop = frameN;  // exact frame index
                                              // update status
                                              text_continue.status = PsychoJS.Status.FINISHED;
                                              text_continue.setAutoDraw(false);
                                            }
                                            
                                            // check for quit (typically the Esc key)
                                            if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                              return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                            }
                                            
                                            // check if the Routine should terminate
                                            if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                              routineForceEnded = true;
                                              return Scheduler.Event.NEXT;
                                            }
                                            
                                            continueRoutine = false;  // reverts to True if at least one component still running
                                            for (const thisComponent of retr_response_feedbackComponents)
                                              if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                continueRoutine = true;
                                                break;
                                              }
                                            
                                            // refresh the screen if continuing
                                            if (continueRoutine) {
                                              return Scheduler.Event.FLIP_REPEAT;
                                            } else {
                                              return Scheduler.Event.NEXT;
                                            }
                                          };
                                        }
                                        
                                        function retr_response_feedbackRoutineEnd(snapshot) {
                                          return async function () {
                                            //--- Ending Routine 'retr_response_feedback' ---
                                            for (const thisComponent of retr_response_feedbackComponents) {
                                              if (typeof thisComponent.setAutoDraw === 'function') {
                                                thisComponent.setAutoDraw(false);
                                              }
                                            }
                                            psychoJS.experiment.addData('retr_response_feedback.stopped', globalClock.getTime());
                                            // update the trial handler
                                            if (currentLoop instanceof MultiStairHandler) {
                                              currentLoop.addResponse(continue_button_16.corr, level);
                                            }
                                            psychoJS.experiment.addData('continue_button_16.keys', continue_button_16.keys);
                                            if (typeof continue_button_16.keys !== 'undefined') {  // we had a response
                                                psychoJS.experiment.addData('continue_button_16.rt', continue_button_16.rt);
                                                psychoJS.experiment.addData('continue_button_16.duration', continue_button_16.duration);
                                                routineTimer.reset();
                                                }
                                            
                                            continue_button_16.stop();
                                            // Run 'End Routine' code from control_retry_loop
                                            console.log(resp_2.corr);
                                            if ((resp_2.corr === 1)) {
                                                retry_loop.finished = true;
                                            } else {
                                                retry_loop.finished = false;
                                            }
                                            
                                            // the Routine "retr_response_feedback" was not non-slip safe, so reset the non-slip timer
                                            routineTimer.reset();
                                            
                                            // Routines running outside a loop should always advance the datafile row
                                            if (currentLoop === psychoJS.experiment) {
                                              psychoJS.experiment.nextEntry(snapshot);
                                            }
                                            return Scheduler.Event.NEXT;
                                          }
                                        }
                                        
                                        function instructions_07RoutineBegin(snapshot) {
                                          return async function () {
                                            TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                            
                                            //--- Prepare to start Routine 'instructions_07' ---
                                            t = 0;
                                            frameN = -1;
                                            continueRoutine = true; // until we're told otherwise
                                            // keep track of whether this Routine was forcibly ended
                                            routineForceEnded = false;
                                            instructions_07Clock.reset();
                                            routineTimer.reset();
                                            instructions_07MaxDurationReached = false;
                                            // update component parameters for each repeat
                                            // Run 'Begin Routine' code from instruction_part7_text_2
                                            if ((language === "english")) {
                                                instructions_part7.text = "You finished all the practice trials.\nThe main task starts now.\n\nPlease minimize movement during the main task phases.\n\nReminder: At the beginning, you will not yet know the correct sequence and will learn through trial and error over time.\n\nPress any key to start the main task.";
                                            }
                                            if ((language === "german")) {
                                                instructions_part7.text = "Sie haben alle \u00dcbungsdurchg\u00e4nge beendet.\nNun beginnt die Hauptaufgabe.\n\nBitte bewegen Sie K\u00f6rper und Augen w\u00e4hrend der\nAufgabenphasen so wenig wie m\u00f6glich.\n\nZu Beginn kennen Sie die richtige Sequenz noch nicht.\nSie lernen sie schrittweise durch Versuch und Irrtum.\n\nDr\u00fccken Sie eine beliebige Taste, um die Hauptaufgabe zu starten.";
                                            }
                                            
                                            continue_button_13.keys = undefined;
                                            continue_button_13.rt = undefined;
                                            _continue_button_13_allKeys = [];
                                            psychoJS.experiment.addData('instructions_07.started', globalClock.getTime());
                                            instructions_07MaxDuration = null
                                            // keep track of which components have finished
                                            instructions_07Components = [];
                                            instructions_07Components.push(instructions_part7);
                                            instructions_07Components.push(continue_button_13);
                                            
                                            for (const thisComponent of instructions_07Components)
                                              if ('status' in thisComponent)
                                                thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                            return Scheduler.Event.NEXT;
                                          }
                                        }
                                        
                                        function instructions_07RoutineEachFrame() {
                                          return async function () {
                                            //--- Loop for each frame of Routine 'instructions_07' ---
                                            // get current time
                                            t = instructions_07Clock.getTime();
                                            frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                            // update/draw components on each frame
                                            
                                            // *instructions_part7* updates
                                            if (t >= 0.0 && instructions_part7.status === PsychoJS.Status.NOT_STARTED) {
                                              // keep track of start time/frame for later
                                              instructions_part7.tStart = t;  // (not accounting for frame time here)
                                              instructions_part7.frameNStart = frameN;  // exact frame index
                                              
                                              instructions_part7.setAutoDraw(true);
                                            }
                                            
                                            
                                            // if instructions_part7 is active this frame...
                                            if (instructions_part7.status === PsychoJS.Status.STARTED) {
                                            }
                                            
                                            frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                            if (instructions_part7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                              // keep track of stop time/frame for later
                                              instructions_part7.tStop = t;  // not accounting for scr refresh
                                              instructions_part7.frameNStop = frameN;  // exact frame index
                                              // update status
                                              instructions_part7.status = PsychoJS.Status.FINISHED;
                                              instructions_part7.setAutoDraw(false);
                                            }
                                            
                                            
                                            // *continue_button_13* updates
                                            if (t >= 1 && continue_button_13.status === PsychoJS.Status.NOT_STARTED) {
                                              // keep track of start time/frame for later
                                              continue_button_13.tStart = t;  // (not accounting for frame time here)
                                              continue_button_13.frameNStart = frameN;  // exact frame index
                                              
                                              // keyboard checking is just starting
                                              psychoJS.window.callOnFlip(function() { continue_button_13.clock.reset(); });  // t=0 on next screen flip
                                              psychoJS.window.callOnFlip(function() { continue_button_13.start(); }); // start on screen flip
                                              psychoJS.window.callOnFlip(function() { continue_button_13.clearEvents(); });
                                            }
                                            frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                            if (continue_button_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                              // keep track of stop time/frame for later
                                              continue_button_13.tStop = t;  // not accounting for scr refresh
                                              continue_button_13.frameNStop = frameN;  // exact frame index
                                              // update status
                                              continue_button_13.status = PsychoJS.Status.FINISHED;
                                              frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                              if (continue_button_13.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                // keep track of stop time/frame for later
                                                continue_button_13.tStop = t;  // not accounting for scr refresh
                                                continue_button_13.frameNStop = frameN;  // exact frame index
                                                // update status
                                                continue_button_13.status = PsychoJS.Status.FINISHED;
                                                continue_button_13.status = PsychoJS.Status.FINISHED;
                                                  }
                                                
                                              }
                                              
                                              // if continue_button_13 is active this frame...
                                              if (continue_button_13.status === PsychoJS.Status.STARTED) {
                                                let theseKeys = continue_button_13.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                                _continue_button_13_allKeys = _continue_button_13_allKeys.concat(theseKeys);
                                                if (_continue_button_13_allKeys.length > 0) {
                                                  continue_button_13.keys = _continue_button_13_allKeys[0].name;  // just the first key pressed
                                                  continue_button_13.rt = _continue_button_13_allKeys[0].rt;
                                                  continue_button_13.duration = _continue_button_13_allKeys[0].duration;
                                                  // a response ends the routine
                                                  continueRoutine = false;
                                                }
                                              }
                                              
                                              // check for quit (typically the Esc key)
                                              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                              }
                                              
                                              // check if the Routine should terminate
                                              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                routineForceEnded = true;
                                                return Scheduler.Event.NEXT;
                                              }
                                              
                                              continueRoutine = false;  // reverts to True if at least one component still running
                                              for (const thisComponent of instructions_07Components)
                                                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                  continueRoutine = true;
                                                  break;
                                                }
                                              
                                              // refresh the screen if continuing
                                              if (continueRoutine) {
                                                return Scheduler.Event.FLIP_REPEAT;
                                              } else {
                                                return Scheduler.Event.NEXT;
                                              }
                                            };
                                          }
                                          
                                          function instructions_07RoutineEnd(snapshot) {
                                            return async function () {
                                              //--- Ending Routine 'instructions_07' ---
                                              for (const thisComponent of instructions_07Components) {
                                                if (typeof thisComponent.setAutoDraw === 'function') {
                                                  thisComponent.setAutoDraw(false);
                                                }
                                              }
                                              psychoJS.experiment.addData('instructions_07.stopped', globalClock.getTime());
                                              // update the trial handler
                                              if (currentLoop instanceof MultiStairHandler) {
                                                currentLoop.addResponse(continue_button_13.corr, level);
                                              }
                                              psychoJS.experiment.addData('continue_button_13.keys', continue_button_13.keys);
                                              if (typeof continue_button_13.keys !== 'undefined') {  // we had a response
                                                  psychoJS.experiment.addData('continue_button_13.rt', continue_button_13.rt);
                                                  psychoJS.experiment.addData('continue_button_13.duration', continue_button_13.duration);
                                                  routineTimer.reset();
                                                  }
                                              
                                              continue_button_13.stop();
                                              // the Routine "instructions_07" was not non-slip safe, so reset the non-slip timer
                                              routineTimer.reset();
                                              
                                              // Routines running outside a loop should always advance the datafile row
                                              if (currentLoop === psychoJS.experiment) {
                                                psychoJS.experiment.nextEntry(snapshot);
                                              }
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function reset_rows_to_selectRoutineBegin(snapshot) {
                                            return async function () {
                                              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                              
                                              //--- Prepare to start Routine 'reset_rows_to_select' ---
                                              t = 0;
                                              frameN = -1;
                                              continueRoutine = true; // until we're told otherwise
                                              // keep track of whether this Routine was forcibly ended
                                              routineForceEnded = false;
                                              reset_rows_to_selectClock.reset();
                                              routineTimer.reset();
                                              reset_rows_to_selectMaxDurationReached = false;
                                              // update component parameters for each repeat
                                              // Run 'Begin Routine' code from define_number_trials
                                              
                                                      // add-on: list(s: string): string[]
                                                      function list(s) {
                                                          // if s is a string, we return a list of its characters
                                                          if (typeof s === 'string')
                                                              return s.split('');
                                                          else
                                                              // otherwise we return s:
                                                              return s;
                                                      }
                                              
                                                      if ((Block.thisN === 0)) {
                                                  N_LEARN = (trials_per_run * n_learn_route);
                                                  N_RETR = (n_learn_route * 5);
                                              } else {
                                                  if ((Block.thisN === 1)) {
                                                      N_LEARN = ((trials_per_run * n_learn_route) * 2);
                                                      N_RETR = ((2 * n_learn_route) * 5);
                                                  }
                                              }
                                              learn_pool = list(util.range(N_LEARN));
                                              retr_pool = list(util.range(N_RETR));
                                              learn_ptr = 0;
                                              retr_ptr = 0;
                                              
                                              // Run 'Begin Routine' code from set_conditionFiles_routes
                                              cond_file_learning = condFileLearning.format({"participant_ID": expInfo["participant_ID"]});
                                              cond_file_retrieval = condFileRetrieval.format({"participant_ID": expInfo["participant_ID"]});
                                              
                                              psychoJS.experiment.addData('reset_rows_to_select.started', globalClock.getTime());
                                              reset_rows_to_selectMaxDuration = null
                                              // keep track of which components have finished
                                              reset_rows_to_selectComponents = [];
                                              
                                              for (const thisComponent of reset_rows_to_selectComponents)
                                                if ('status' in thisComponent)
                                                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function reset_rows_to_selectRoutineEachFrame() {
                                            return async function () {
                                              //--- Loop for each frame of Routine 'reset_rows_to_select' ---
                                              // get current time
                                              t = reset_rows_to_selectClock.getTime();
                                              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                              // update/draw components on each frame
                                              // check for quit (typically the Esc key)
                                              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                              }
                                              
                                              // check if the Routine should terminate
                                              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                routineForceEnded = true;
                                                return Scheduler.Event.NEXT;
                                              }
                                              
                                              continueRoutine = false;  // reverts to True if at least one component still running
                                              for (const thisComponent of reset_rows_to_selectComponents)
                                                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                  continueRoutine = true;
                                                  break;
                                                }
                                              
                                              // refresh the screen if continuing
                                              if (continueRoutine) {
                                                return Scheduler.Event.FLIP_REPEAT;
                                              } else {
                                                return Scheduler.Event.NEXT;
                                              }
                                            };
                                          }
                                          
                                          function reset_rows_to_selectRoutineEnd(snapshot) {
                                            return async function () {
                                              //--- Ending Routine 'reset_rows_to_select' ---
                                              for (const thisComponent of reset_rows_to_selectComponents) {
                                                if (typeof thisComponent.setAutoDraw === 'function') {
                                                  thisComponent.setAutoDraw(false);
                                                }
                                              }
                                              psychoJS.experiment.addData('reset_rows_to_select.stopped', globalClock.getTime());
                                              // the Routine "reset_rows_to_select" was not non-slip safe, so reset the non-slip timer
                                              routineTimer.reset();
                                              
                                              // Routines running outside a loop should always advance the datafile row
                                              if (currentLoop === psychoJS.experiment) {
                                                psychoJS.experiment.nextEntry(snapshot);
                                              }
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function set_learning_rowsRoutineBegin(snapshot) {
                                            return async function () {
                                              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                              
                                              //--- Prepare to start Routine 'set_learning_rows' ---
                                              t = 0;
                                              frameN = -1;
                                              continueRoutine = true; // until we're told otherwise
                                              // keep track of whether this Routine was forcibly ended
                                              routineForceEnded = false;
                                              set_learning_rowsClock.reset();
                                              routineTimer.reset();
                                              set_learning_rowsMaxDurationReached = false;
                                              // update component parameters for each repeat
                                              // Run 'Begin Routine' code from take_learn_routes_from_list
                                              [selected_rows, learn_ptr] = take_block(learn_pool, learn_ptr, trials_per_run);
                                              console.log(selected_rows);
                                              
                                              psychoJS.experiment.addData('set_learning_rows.started', globalClock.getTime());
                                              set_learning_rowsMaxDuration = null
                                              // keep track of which components have finished
                                              set_learning_rowsComponents = [];
                                              
                                              for (const thisComponent of set_learning_rowsComponents)
                                                if ('status' in thisComponent)
                                                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function set_learning_rowsRoutineEachFrame() {
                                            return async function () {
                                              //--- Loop for each frame of Routine 'set_learning_rows' ---
                                              // get current time
                                              t = set_learning_rowsClock.getTime();
                                              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                              // update/draw components on each frame
                                              // check for quit (typically the Esc key)
                                              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                              }
                                              
                                              // check if the Routine should terminate
                                              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                routineForceEnded = true;
                                                return Scheduler.Event.NEXT;
                                              }
                                              
                                              continueRoutine = false;  // reverts to True if at least one component still running
                                              for (const thisComponent of set_learning_rowsComponents)
                                                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                  continueRoutine = true;
                                                  break;
                                                }
                                              
                                              // refresh the screen if continuing
                                              if (continueRoutine) {
                                                return Scheduler.Event.FLIP_REPEAT;
                                              } else {
                                                return Scheduler.Event.NEXT;
                                              }
                                            };
                                          }
                                          
                                          function set_learning_rowsRoutineEnd(snapshot) {
                                            return async function () {
                                              //--- Ending Routine 'set_learning_rows' ---
                                              for (const thisComponent of set_learning_rowsComponents) {
                                                if (typeof thisComponent.setAutoDraw === 'function') {
                                                  thisComponent.setAutoDraw(false);
                                                }
                                              }
                                              psychoJS.experiment.addData('set_learning_rows.stopped', globalClock.getTime());
                                              // the Routine "set_learning_rows" was not non-slip safe, so reset the non-slip timer
                                              routineTimer.reset();
                                              
                                              // Routines running outside a loop should always advance the datafile row
                                              if (currentLoop === psychoJS.experiment) {
                                                psychoJS.experiment.nextEntry(snapshot);
                                              }
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function show_contextRoutineBegin(snapshot) {
                                            return async function () {
                                              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                              
                                              //--- Prepare to start Routine 'show_context' ---
                                              t = 0;
                                              frameN = -1;
                                              continueRoutine = true; // until we're told otherwise
                                              // keep track of whether this Routine was forcibly ended
                                              routineForceEnded = false;
                                              show_contextClock.reset(routineTimer.getTime());
                                              routineTimer.add(0.500000);
                                              show_contextMaxDurationReached = false;
                                              // update component parameters for each repeat
                                              scene_image.setImage(context_img_block);
                                              psychoJS.experiment.addData('show_context.started', globalClock.getTime());
                                              show_contextMaxDuration = null
                                              // keep track of which components have finished
                                              show_contextComponents = [];
                                              show_contextComponents.push(scene_image);
                                              
                                              for (const thisComponent of show_contextComponents)
                                                if ('status' in thisComponent)
                                                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function show_contextRoutineEachFrame() {
                                            return async function () {
                                              //--- Loop for each frame of Routine 'show_context' ---
                                              // get current time
                                              t = show_contextClock.getTime();
                                              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                              // update/draw components on each frame
                                              
                                              // *scene_image* updates
                                              if (t >= 0.0 && scene_image.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                scene_image.tStart = t;  // (not accounting for frame time here)
                                                scene_image.frameNStart = frameN;  // exact frame index
                                                
                                                scene_image.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if scene_image is active this frame...
                                              if (scene_image.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                              if (scene_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                // keep track of stop time/frame for later
                                                scene_image.tStop = t;  // not accounting for scr refresh
                                                scene_image.frameNStop = frameN;  // exact frame index
                                                // update status
                                                scene_image.status = PsychoJS.Status.FINISHED;
                                                scene_image.setAutoDraw(false);
                                              }
                                              
                                              // check for quit (typically the Esc key)
                                              if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                              }
                                              
                                              // check if the Routine should terminate
                                              if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                routineForceEnded = true;
                                                return Scheduler.Event.NEXT;
                                              }
                                              
                                              continueRoutine = false;  // reverts to True if at least one component still running
                                              for (const thisComponent of show_contextComponents)
                                                if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                  continueRoutine = true;
                                                  break;
                                                }
                                              
                                              // refresh the screen if continuing
                                              if (continueRoutine && routineTimer.getTime() > 0) {
                                                return Scheduler.Event.FLIP_REPEAT;
                                              } else {
                                                return Scheduler.Event.NEXT;
                                              }
                                            };
                                          }
                                          
                                          function show_contextRoutineEnd(snapshot) {
                                            return async function () {
                                              //--- Ending Routine 'show_context' ---
                                              for (const thisComponent of show_contextComponents) {
                                                if (typeof thisComponent.setAutoDraw === 'function') {
                                                  thisComponent.setAutoDraw(false);
                                                }
                                              }
                                              psychoJS.experiment.addData('show_context.stopped', globalClock.getTime());
                                              if (routineForceEnded) {
                                                  routineTimer.reset();} else if (show_contextMaxDurationReached) {
                                                  show_contextClock.add(show_contextMaxDuration);
                                              } else {
                                                  show_contextClock.add(0.500000);
                                              }
                                              // Routines running outside a loop should always advance the datafile row
                                              if (currentLoop === psychoJS.experiment) {
                                                psychoJS.experiment.nextEntry(snapshot);
                                              }
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function choice_displayRoutineBegin(snapshot) {
                                            return async function () {
                                              TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                              
                                              //--- Prepare to start Routine 'choice_display' ---
                                              t = 0;
                                              frameN = -1;
                                              continueRoutine = true; // until we're told otherwise
                                              // keep track of whether this Routine was forcibly ended
                                              routineForceEnded = false;
                                              choice_displayClock.reset();
                                              routineTimer.reset();
                                              choice_displayMaxDurationReached = false;
                                              // update component parameters for each repeat
                                              scene_image_2.setImage(context_img_block);
                                              // Run 'Begin Routine' code from Init_routeClock_2
                                              
                                              window.practice_choice_displayMaxDuration = null; 
                                              window.practice_choice_displayComponents = null; 
                                              window._key_resp_2_allKeys = null; 
                                              window.frameRemains = null;
                                              
                                              window.routClock = new util.Clock();
                                              window.routClock.reset();
                                              
                                              //if (loop_not_correct.thisN !== 0) {
                                              //    practice_errors = 0;
                                              //}
                                              // Run 'Begin Routine' code from bids_choice_disp
                                              pos2item = {};
                                              pos2item[correct_pos] = "target";
                                              pos2item[dist01_pos] = "distractor_01";
                                              pos2item[dist02_pos] = "distractor_02";
                                              key2pos = {[left_key]: "left", [right_key]: "right", [center_key]: "center"};
                                              
                                              polygon_4.setFillColor(new util.Color([0.0, 0.0, 0.0]));
                                              polygon_4.setLineColor(new util.Color([0.0039, 0.0039, 0.0039]));
                                              prompt.setPos(prompt_pos);
                                              prompt.setImage(promptFile);
                                              dist_01.setPos(resolve_pos(dist01_pos));
                                              dist_01.setImage(dist_01File);
                                              dist_02.setPos(resolve_pos(dist02_pos));
                                              dist_02.setImage(dist_02File);
                                              correct.setPos(resolve_pos(correct_pos));
                                              correct.setImage(correctFile);
                                              // Run 'Begin Routine' code from get_response_parameters
                                              window.responded = false;
                                              
                                              window.delayClock = null;
                                              
                                              // Begin Routine
                                              window.delayDone = false;
                                              window.chosenPos = null;
                                              
                                              chooseNowText.setOpacity(0.0);
                                              key_resp.keys = undefined;
                                              key_resp.rt = undefined;
                                              _key_resp_allKeys = [];
                                              // Run 'Begin Routine' code from set_trigger_response
                                              response_trigger = trigger_dict["image_selected"];
                                              resp_trig_giv = false;
                                              
                                              psychoJS.experiment.addData('choice_display.started', globalClock.getTime());
                                              choice_displayMaxDuration = null
                                              // keep track of which components have finished
                                              choice_displayComponents = [];
                                              choice_displayComponents.push(scene_image_2);
                                              choice_displayComponents.push(polygon_4);
                                              choice_displayComponents.push(prompt);
                                              choice_displayComponents.push(dist_01);
                                              choice_displayComponents.push(dist_02);
                                              choice_displayComponents.push(correct);
                                              choice_displayComponents.push(chooseNowText);
                                              choice_displayComponents.push(key_resp);
                                              
                                              for (const thisComponent of choice_displayComponents)
                                                if ('status' in thisComponent)
                                                  thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                              return Scheduler.Event.NEXT;
                                            }
                                          }
                                          
                                          function choice_displayRoutineEachFrame() {
                                            return async function () {
                                              //--- Loop for each frame of Routine 'choice_display' ---
                                              // get current time
                                              t = choice_displayClock.getTime();
                                              frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                              // update/draw components on each frame
                                              
                                              // *scene_image_2* updates
                                              if (t >= 0.0 && scene_image_2.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                scene_image_2.tStart = t;  // (not accounting for frame time here)
                                                scene_image_2.frameNStart = frameN;  // exact frame index
                                                
                                                scene_image_2.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if scene_image_2 is active this frame...
                                              if (scene_image_2.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              // Run 'Each Frame' code from set_trigger_image
                                              if ((frameN === 0)) {
                                                  bids.trigger(correctTrigNumber, {"stim": correct, "label": "choice_display"});
                                                  core.wait(0.01);
                                              }
                                              
                                              // Run 'Each Frame' code from bids_choice_disp
                                              bids.schedule_onset(prompt, {"type_of_stimulus": "image", "component_label": "current_image", "trial_type": "learn", "concept_label": promptFile.partition("/").slice((- 1))[0], "concept_exemplar": promptFile.partition("/").slice((- 1))[0], "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                              bids.schedule_onset(correct, {"type_of_stimulus": "image", "component_label": "corr_next_image", "trial_type": "learn", "concept_label": correctFile.partition("/").slice((- 1))[0], "concept_exemplar": correctFile.partition("/")[2], "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                              bids.schedule_onset(dist_01, {"type_of_stimulus": "image", "component_label": "distractor 01 (close)", "concept_label": dist_01File.partition("/").slice((- 1))[0], "trial_type": "learn", "concept_exemplar": dist_01File.partition("/").slice((- 1))[0], "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                              bids.schedule_onset(dist_02, {"type_of_stimulus": "image", "component_label": "distractor 02 (far)", "concept_label": dist_02File.partition("/").slice((- 1))[0], "trial_type": "learn", "concept_exemplar": dist_02File.partition("/").slice((- 1))[0], "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                              
                                              
                                              // *polygon_4* updates
                                              if (t >= 0.0 && polygon_4.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                polygon_4.tStart = t;  // (not accounting for frame time here)
                                                polygon_4.frameNStart = frameN;  // exact frame index
                                                
                                                polygon_4.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if polygon_4 is active this frame...
                                              if (polygon_4.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              
                                              // *prompt* updates
                                              if (t >= 0.0 && prompt.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                prompt.tStart = t;  // (not accounting for frame time here)
                                                prompt.frameNStart = frameN;  // exact frame index
                                                
                                                prompt.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if prompt is active this frame...
                                              if (prompt.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              
                                              // *dist_01* updates
                                              if (t >= 0.0 && dist_01.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                dist_01.tStart = t;  // (not accounting for frame time here)
                                                dist_01.frameNStart = frameN;  // exact frame index
                                                
                                                dist_01.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if dist_01 is active this frame...
                                              if (dist_01.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              
                                              // *dist_02* updates
                                              if (t >= 0.0 && dist_02.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                dist_02.tStart = t;  // (not accounting for frame time here)
                                                dist_02.frameNStart = frameN;  // exact frame index
                                                
                                                dist_02.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if dist_02 is active this frame...
                                              if (dist_02.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              
                                              // *correct* updates
                                              if (t >= 0.0 && correct.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                correct.tStart = t;  // (not accounting for frame time here)
                                                correct.frameNStart = frameN;  // exact frame index
                                                
                                                correct.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if correct is active this frame...
                                              if (correct.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              // Run 'Each Frame' code from get_response_parameters
                                              
                                              
                                              if (!responded) {
                                                //let key_list = key_resp_2.getKeys({ keyList: ["left", "right", "up"], waitRelease: false });
                                                
                                                if (key_list.length > 0) {
                                                  responded = true;
                                                  let thisResp = key_list[0];
                                                  key_resp_2.keys = thisResp.name;
                                                  key_resp_2.rt = thisResp.rt;
                                                  key_resp_2.corr = (thisResp.name === correct_ans) ? 1 : 0;
                                              
                                                  if (thisResp.name === window.left_key)        chosenPos = window.left_pos;
                                                  else if (thisResp.name === window.right_key)  chosenPos = window.right_pos;
                                                  else if (thisResp.name === window.center_key) chosenPos = window.center_pos;
                                                  
                                                  key_resp_2.stop()
                                                  polygon.setPos(chosenPos);
                                                  polygon.setOpacity(1.0);
                                                  
                                                  // change color of polygon for correct responses
                                                  if (key_resp_2.corr === 1) {
                                                    window.polygonCol = [0, 1, 0];
                                                    polygon.setFillColor(new util.Color(window.polygonCol));
                                                    polygon.setLineColor(new util.Color(window.polygonCol));
                                                  } else if (key_resp_2.corr === 0) {
                                                    window.polygonCol = [1, -1, -1];
                                              
                                                    polygon.setFillColor(new util.Color(window.polygonCol));
                                                    polygon.setLineColor(new util.Color(window.polygonCol));
                                                  } else  {
                                                    window.polygonCol = [0, 0, 0];
                                              
                                                    polygon.setFillColor(new util.Color(window.polygonCol));
                                                    polygon.setLineColor(new util.Color(window.polygonCol));
                                                  }
                                                      
                                                  delayClock = new util.Clock();
                                                }
                                              }
                                              
                                              if (responded && !delayDone && delayClock !== null && delayClock.getTime() >= 0.1) {
                                                delayDone = true;
                                                continueRoutine = false;
                                              }
                                              
                                              // *chooseNowText* updates
                                              if (t >= 0.0 && chooseNowText.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                chooseNowText.tStart = t;  // (not accounting for frame time here)
                                                chooseNowText.frameNStart = frameN;  // exact frame index
                                                
                                                chooseNowText.setAutoDraw(true);
                                              }
                                              
                                              
                                              // if chooseNowText is active this frame...
                                              if (chooseNowText.status === PsychoJS.Status.STARTED) {
                                              }
                                              
                                              
                                              // *key_resp* updates
                                              if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
                                                // keep track of start time/frame for later
                                                key_resp.tStart = t;  // (not accounting for frame time here)
                                                key_resp.frameNStart = frameN;  // exact frame index
                                                
                                                // keyboard checking is just starting
                                                key_resp.clock.reset();
                                                key_resp.start();
                                                key_resp.clearEvents();
                                              }
                                              frameRemains = 0.0 + max_response_time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                              if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                // keep track of stop time/frame for later
                                                key_resp.tStop = t;  // not accounting for scr refresh
                                                key_resp.frameNStop = frameN;  // exact frame index
                                                // update status
                                                key_resp.status = PsychoJS.Status.FINISHED;
                                                frameRemains = 0.0 + max_response_time - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  key_resp.tStop = t;  // not accounting for scr refresh
                                                  key_resp.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  key_resp.status = PsychoJS.Status.FINISHED;
                                                  key_resp.status = PsychoJS.Status.FINISHED;
                                                    }
                                                  
                                                }
                                                
                                                // if key_resp is active this frame...
                                                if (key_resp.status === PsychoJS.Status.STARTED) {
                                                  let theseKeys = key_resp.getKeys({keyList: [left_key,right_key,center_key], waitRelease: false});
                                                  _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
                                                  if (_key_resp_allKeys.length > 0) {
                                                    key_resp.keys = _key_resp_allKeys[0].name;  // just the first key pressed
                                                    key_resp.rt = _key_resp_allKeys[0].rt;
                                                    key_resp.duration = _key_resp_allKeys[0].duration;
                                                  }
                                                }
                                                
                                                // Run 'Each Frame' code from set_trigger_response
                                                if ((key_resp.keys && (! resp_trig_giv))) {
                                                    bids.trigger(response_trigger, {"label": "image_selected", "on_flip": false, "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                                    trigOn = true;
                                                    resp_trig_giv = true;
                                                    core.wait(0.01);
                                                }
                                                
                                                // check for quit (typically the Esc key)
                                                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                }
                                                
                                                // check if the Routine should terminate
                                                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                  routineForceEnded = true;
                                                  return Scheduler.Event.NEXT;
                                                }
                                                
                                                continueRoutine = false;  // reverts to True if at least one component still running
                                                for (const thisComponent of choice_displayComponents)
                                                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                    continueRoutine = true;
                                                    break;
                                                  }
                                                
                                                // refresh the screen if continuing
                                                if (continueRoutine) {
                                                  return Scheduler.Event.FLIP_REPEAT;
                                                } else {
                                                  return Scheduler.Event.NEXT;
                                                }
                                              };
                                            }
                                            
                                            function choice_displayRoutineEnd(snapshot) {
                                              return async function () {
                                                //--- Ending Routine 'choice_display' ---
                                                for (const thisComponent of choice_displayComponents) {
                                                  if (typeof thisComponent.setAutoDraw === 'function') {
                                                    thisComponent.setAutoDraw(false);
                                                  }
                                                }
                                                psychoJS.experiment.addData('choice_display.stopped', globalClock.getTime());
                                                // Run 'End Routine' code from bids_choice_disp
                                                bids.mark_offset(prompt);
                                                bids.mark_offset(correct);
                                                bids.mark_offset(dist_01);
                                                bids.mark_offset(dist_02);
                                                pressed = key_resp.keys;
                                                if ((pressed instanceof list)) {
                                                    pressed = (pressed ? pressed.slice((- 1))[0] : "m");
                                                }
                                                chosen_pos = key2pos.get(pressed, null);
                                                chosen_item = pos2item.get(chosen_pos, null);
                                                is_correct = ((chosen_item !== null) ? (chosen_item === "target") : null);
                                                
                                                // update the trial handler
                                                if (currentLoop instanceof MultiStairHandler) {
                                                  currentLoop.addResponse(key_resp.corr, level);
                                                }
                                                psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
                                                if (typeof key_resp.keys !== 'undefined') {  // we had a response
                                                    psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
                                                    psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
                                                    }
                                                
                                                key_resp.stop();
                                                // the Routine "choice_display" was not non-slip safe, so reset the non-slip timer
                                                routineTimer.reset();
                                                
                                                // Routines running outside a loop should always advance the datafile row
                                                if (currentLoop === psychoJS.experiment) {
                                                  psychoJS.experiment.nextEntry(snapshot);
                                                }
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function feedbackRoutineBegin(snapshot) {
                                              return async function () {
                                                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                
                                                //--- Prepare to start Routine 'feedback' ---
                                                t = 0;
                                                frameN = -1;
                                                continueRoutine = true; // until we're told otherwise
                                                // keep track of whether this Routine was forcibly ended
                                                routineForceEnded = false;
                                                feedbackClock.reset();
                                                routineTimer.reset();
                                                feedbackMaxDurationReached = false;
                                                // update component parameters for each repeat
                                                scene_image_3.setImage(context_img_block);
                                                // Run 'Begin Routine' code from control__polygon_2
                                                polygon_7.setOpacity(0.0)
                                                if chosenPos:
                                                    polygon_7.setPos(chosenPos)
                                                    polygon_7.setOpacity(1.0)
                                                    polygon_7.setFillColor(polygonCol)
                                                    polygon_7.setLineColor(polygonCol)
                                                // Run 'Begin Routine' code from animation_control_2
                                                // Initialize animation control
                                                
                                                window.endY = prompt_pos[1];   // end y-coord of moving image
                                                window.endX = prompt_pos[0];   // end x-coord of moving image
                                                
                                                window.maxAnimationDur = Math.round(animation_time * expInfo.frameRate);
                                                window.animationTimer = 0;      // initialize variable
                                                window.animationDone = false;  // initialize variable
                                                window.moveCorrect = false;    // initialize variable
                                                
                                                polygon_8.setFillColor(new util.Color([0.0, 0.0, 0.0]));
                                                polygon_8.setLineColor(new util.Color([0.0039, 0.0039, 0.0039]));
                                                prompt_2.setPos(prompt_pos);
                                                prompt_2.setImage(promptFile);
                                                dist_01_2.setPos(resolve_pos(dist01_pos));
                                                dist_01_2.setImage(dist_01File);
                                                dist_02_2.setPos(resolve_pos(dist02_pos));
                                                dist_02_2.setImage(dist_02File);
                                                correct_2.setPos(resolve_pos(correct_pos));
                                                correct_2.setImage(correctFile);
                                                // Run 'Begin Routine' code from trigger_feedback_disp
                                                feedback_trigger_sent = false;
                                                
                                                psychoJS.experiment.addData('feedback.started', globalClock.getTime());
                                                feedbackMaxDuration = null
                                                // keep track of which components have finished
                                                feedbackComponents = [];
                                                feedbackComponents.push(scene_image_3);
                                                feedbackComponents.push(polygon_8);
                                                feedbackComponents.push(prompt_2);
                                                feedbackComponents.push(dist_01_2);
                                                feedbackComponents.push(dist_02_2);
                                                feedbackComponents.push(correct_2);
                                                
                                                for (const thisComponent of feedbackComponents)
                                                  if ('status' in thisComponent)
                                                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function feedbackRoutineEachFrame() {
                                              return async function () {
                                                //--- Loop for each frame of Routine 'feedback' ---
                                                // get current time
                                                t = feedbackClock.getTime();
                                                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                // update/draw components on each frame
                                                
                                                // *scene_image_3* updates
                                                if (t >= 0.0 && scene_image_3.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  scene_image_3.tStart = t;  // (not accounting for frame time here)
                                                  scene_image_3.frameNStart = frameN;  // exact frame index
                                                  
                                                  scene_image_3.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if scene_image_3 is active this frame...
                                                if (scene_image_3.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                // Run 'Each Frame' code from animation_control_2
                                                // Start animation
                                                if (!moveCorrect && !animationDone) {
                                                  moveCorrect = true;
                                                }
                                                
                                                // Run animation
                                                if (moveCorrect && !animationDone) {
                                                  animationTimer += 1;
                                                
                                                  // Current position
                                                  const [current_x, current_y] = correct_prc_2.pos;
                                                
                                                  // Compute direction toward target
                                                  const dx = endX - current_x;
                                                  const dy = endY - current_y;
                                                
                                                  // Move a small fraction toward target
                                                  const move_fraction = feedback_steps; // fraction of remaining distance each frame
                                                  const new_x = current_x + dx * move_fraction;
                                                  const new_y = current_y + dy * move_fraction;
                                                
                                                  // Update position
                                                  correct_prc_2.setPos([new_x, new_y]);
                                                
                                                  if (is_correct) {
                                                     polygon_7.setPos([new_x, new_y]);
                                                    }
                                                  // Stop when close enough to target (or if max duration exceeded)
                                                  if (
                                                    (Math.abs(dx) < rest_jump && Math.abs(dy) < rest_jump) ||
                                                    animationTimer > maxAnimationDur
                                                  ) {
                                                    correct_prc_2.setPos([endX, endY]);
                                                    if (is_correct) {
                                                     polygon_7.setPos([new_x, new_y]);
                                                    }
                                                    animationDone = true;
                                                    moveCorrect = false;
                                                    continueRoutine = false;
                                                  }
                                                }
                                                
                                                
                                                // *polygon_8* updates
                                                if (t >= 0.0 && polygon_8.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  polygon_8.tStart = t;  // (not accounting for frame time here)
                                                  polygon_8.frameNStart = frameN;  // exact frame index
                                                  
                                                  polygon_8.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if polygon_8 is active this frame...
                                                if (polygon_8.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                // Run 'Each Frame' code from bids_feedback_disp
                                                bids.schedule_onset(correct_2, {"type_of_stimulus": "feedback", "component_label": "correct_moving", "trial_type": "learn", "block_name": block, "sequence_name": learningSeq, "route_num": runIndexWithinSeq, "trial_num": currPosInSeq});
                                                
                                                
                                                // *prompt_2* updates
                                                if (t >= 0.0 && prompt_2.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  prompt_2.tStart = t;  // (not accounting for frame time here)
                                                  prompt_2.frameNStart = frameN;  // exact frame index
                                                  
                                                  prompt_2.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if prompt_2 is active this frame...
                                                if (prompt_2.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                
                                                // *dist_01_2* updates
                                                if (t >= 0.0 && dist_01_2.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  dist_01_2.tStart = t;  // (not accounting for frame time here)
                                                  dist_01_2.frameNStart = frameN;  // exact frame index
                                                  
                                                  dist_01_2.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if dist_01_2 is active this frame...
                                                if (dist_01_2.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                
                                                // *dist_02_2* updates
                                                if (t >= 0.0 && dist_02_2.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  dist_02_2.tStart = t;  // (not accounting for frame time here)
                                                  dist_02_2.frameNStart = frameN;  // exact frame index
                                                  
                                                  dist_02_2.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if dist_02_2 is active this frame...
                                                if (dist_02_2.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                
                                                // *correct_2* updates
                                                if (t >= 0.0 && correct_2.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  correct_2.tStart = t;  // (not accounting for frame time here)
                                                  correct_2.frameNStart = frameN;  // exact frame index
                                                  
                                                  correct_2.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if correct_2 is active this frame...
                                                if (correct_2.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                // Run 'Each Frame' code from trigger_feedback_disp
                                                feedback_trigger = trigger_dict["feedback"];
                                                if ((moveCorrect && (! feedback_trigger_sent))) {
                                                    bids.trigger(feedback_trigger, {"stim": correct_2, "label": "feedback"});
                                                    feedback_trigger_sent = true;
                                                }
                                                
                                                // check for quit (typically the Esc key)
                                                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                }
                                                
                                                // check if the Routine should terminate
                                                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                  routineForceEnded = true;
                                                  return Scheduler.Event.NEXT;
                                                }
                                                
                                                continueRoutine = false;  // reverts to True if at least one component still running
                                                for (const thisComponent of feedbackComponents)
                                                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                    continueRoutine = true;
                                                    break;
                                                  }
                                                
                                                // refresh the screen if continuing
                                                if (continueRoutine) {
                                                  return Scheduler.Event.FLIP_REPEAT;
                                                } else {
                                                  return Scheduler.Event.NEXT;
                                                }
                                              };
                                            }
                                            
                                            function feedbackRoutineEnd(snapshot) {
                                              return async function () {
                                                //--- Ending Routine 'feedback' ---
                                                for (const thisComponent of feedbackComponents) {
                                                  if (typeof thisComponent.setAutoDraw === 'function') {
                                                    thisComponent.setAutoDraw(false);
                                                  }
                                                }
                                                psychoJS.experiment.addData('feedback.stopped', globalClock.getTime());
                                                // Run 'End Routine' code from bids_feedback_disp
                                                bids.mark_offset(correct_2);
                                                
                                                // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
                                                routineTimer.reset();
                                                
                                                // Routines running outside a loop should always advance the datafile row
                                                if (currentLoop === psychoJS.experiment) {
                                                  psychoJS.experiment.nextEntry(snapshot);
                                                }
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function too_slow_routineRoutineBegin(snapshot) {
                                              return async function () {
                                                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                
                                                //--- Prepare to start Routine 'too_slow_routine' ---
                                                t = 0;
                                                frameN = -1;
                                                continueRoutine = true; // until we're told otherwise
                                                // keep track of whether this Routine was forcibly ended
                                                routineForceEnded = false;
                                                too_slow_routineClock.reset();
                                                routineTimer.reset();
                                                too_slow_routineMaxDurationReached = false;
                                                // update component parameters for each repeat
                                                // Run 'Begin Routine' code from determine_start
                                                if (responded) {
                                                    continueRoutine = false;
                                                }
                                                
                                                scene_image_4.setImage(context_img_block);
                                                tooSlowtext.setText('');
                                                // Run 'Begin Routine' code from set_slow_msg_text
                                                if ((language === "english")) {
                                                    tooSlowtext.text = "Too slow. You need to respond faster.";
                                                }
                                                if ((language === "german")) {
                                                    tooSlowtext.text = "Zu langsam. Sie m\u00fcssen schneller antworten.";
                                                }
                                                if ((language === "french")) {
                                                    tooSlowtext.text = "";
                                                }
                                                
                                                psychoJS.experiment.addData('too_slow_routine.started', globalClock.getTime());
                                                too_slow_routineMaxDuration = null
                                                // keep track of which components have finished
                                                too_slow_routineComponents = [];
                                                too_slow_routineComponents.push(scene_image_4);
                                                too_slow_routineComponents.push(tooSlowtext);
                                                
                                                for (const thisComponent of too_slow_routineComponents)
                                                  if ('status' in thisComponent)
                                                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function too_slow_routineRoutineEachFrame() {
                                              return async function () {
                                                //--- Loop for each frame of Routine 'too_slow_routine' ---
                                                // get current time
                                                t = too_slow_routineClock.getTime();
                                                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                // update/draw components on each frame
                                                
                                                // *scene_image_4* updates
                                                if (t >= 0.0 && scene_image_4.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  scene_image_4.tStart = t;  // (not accounting for frame time here)
                                                  scene_image_4.frameNStart = frameN;  // exact frame index
                                                  
                                                  scene_image_4.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if scene_image_4 is active this frame...
                                                if (scene_image_4.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                frameRemains = 0.0 + too_slow_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (scene_image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  scene_image_4.tStop = t;  // not accounting for scr refresh
                                                  scene_image_4.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  scene_image_4.status = PsychoJS.Status.FINISHED;
                                                  scene_image_4.setAutoDraw(false);
                                                }
                                                
                                                
                                                // *tooSlowtext* updates
                                                if (t >= 0.0 && tooSlowtext.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  tooSlowtext.tStart = t;  // (not accounting for frame time here)
                                                  tooSlowtext.frameNStart = frameN;  // exact frame index
                                                  
                                                  tooSlowtext.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if tooSlowtext is active this frame...
                                                if (tooSlowtext.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                frameRemains = 0.0 + too_slow_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (tooSlowtext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  tooSlowtext.tStop = t;  // not accounting for scr refresh
                                                  tooSlowtext.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  tooSlowtext.status = PsychoJS.Status.FINISHED;
                                                  tooSlowtext.setAutoDraw(false);
                                                }
                                                
                                                // check for quit (typically the Esc key)
                                                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                }
                                                
                                                // check if the Routine should terminate
                                                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                  routineForceEnded = true;
                                                  return Scheduler.Event.NEXT;
                                                }
                                                
                                                continueRoutine = false;  // reverts to True if at least one component still running
                                                for (const thisComponent of too_slow_routineComponents)
                                                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                    continueRoutine = true;
                                                    break;
                                                  }
                                                
                                                // refresh the screen if continuing
                                                if (continueRoutine) {
                                                  return Scheduler.Event.FLIP_REPEAT;
                                                } else {
                                                  return Scheduler.Event.NEXT;
                                                }
                                              };
                                            }
                                            
                                            function too_slow_routineRoutineEnd(snapshot) {
                                              return async function () {
                                                //--- Ending Routine 'too_slow_routine' ---
                                                for (const thisComponent of too_slow_routineComponents) {
                                                  if (typeof thisComponent.setAutoDraw === 'function') {
                                                    thisComponent.setAutoDraw(false);
                                                  }
                                                }
                                                psychoJS.experiment.addData('too_slow_routine.stopped', globalClock.getTime());
                                                // Run 'End Routine' code from set_slow_msg_text
                                                bids.close_trial();
                                                
                                                // the Routine "too_slow_routine" was not non-slip safe, so reset the non-slip timer
                                                routineTimer.reset();
                                                
                                                // Routines running outside a loop should always advance the datafile row
                                                if (currentLoop === psychoJS.experiment) {
                                                  psychoJS.experiment.nextEntry(snapshot);
                                                }
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function rest_periodRoutineBegin(snapshot) {
                                              return async function () {
                                                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                
                                                //--- Prepare to start Routine 'rest_period' ---
                                                t = 0;
                                                frameN = -1;
                                                continueRoutine = true; // until we're told otherwise
                                                // keep track of whether this Routine was forcibly ended
                                                routineForceEnded = false;
                                                rest_periodClock.reset();
                                                routineTimer.reset();
                                                rest_periodMaxDurationReached = false;
                                                // update component parameters for each repeat
                                                // Run 'Begin Routine' code from set_trigger_rest
                                                replay_endtrig_sent = false;
                                                
                                                psychoJS.experiment.addData('rest_period.started', globalClock.getTime());
                                                rest_periodMaxDuration = null
                                                // keep track of which components have finished
                                                rest_periodComponents = [];
                                                rest_periodComponents.push(fix_cross);
                                                
                                                for (const thisComponent of rest_periodComponents)
                                                  if ('status' in thisComponent)
                                                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function rest_periodRoutineEachFrame() {
                                              return async function () {
                                                //--- Loop for each frame of Routine 'rest_period' ---
                                                // get current time
                                                t = rest_periodClock.getTime();
                                                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                // update/draw components on each frame
                                                // Run 'Each Frame' code from set_trigger_rest
                                                replayTrigger = trigger_dict["replay_break"];
                                                if ((frameN === 0)) {
                                                    bids.trigger(replayTrigger, {"stim": fix_cross, "label": "replay_break"});
                                                }
                                                
                                                // Run 'Each Frame' code from bids_break_logging
                                                bids.schedule_onset(fix_cross, {"type_of_stimulus": "replay_break", "block_name": block, "route_num": runIndexWithinSeq, "component_label": "fix_cross_replay_break", "trial_type": "learn", "sequence_name": learningSeq, "trial_num": currPosInSeq});
                                                
                                                
                                                // *fix_cross* updates
                                                if (t >= 0.0 && fix_cross.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  fix_cross.tStart = t;  // (not accounting for frame time here)
                                                  fix_cross.frameNStart = frameN;  // exact frame index
                                                  
                                                  fix_cross.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if fix_cross is active this frame...
                                                if (fix_cross.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                frameRemains = 0.0 + replay_break_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (fix_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  fix_cross.tStop = t;  // not accounting for scr refresh
                                                  fix_cross.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  fix_cross.status = PsychoJS.Status.FINISHED;
                                                  fix_cross.setAutoDraw(false);
                                                }
                                                
                                                // check for quit (typically the Esc key)
                                                if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                  return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                }
                                                
                                                // check if the Routine should terminate
                                                if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                  routineForceEnded = true;
                                                  return Scheduler.Event.NEXT;
                                                }
                                                
                                                continueRoutine = false;  // reverts to True if at least one component still running
                                                for (const thisComponent of rest_periodComponents)
                                                  if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                    continueRoutine = true;
                                                    break;
                                                  }
                                                
                                                // refresh the screen if continuing
                                                if (continueRoutine) {
                                                  return Scheduler.Event.FLIP_REPEAT;
                                                } else {
                                                  return Scheduler.Event.NEXT;
                                                }
                                              };
                                            }
                                            
                                            function rest_periodRoutineEnd(snapshot) {
                                              return async function () {
                                                //--- Ending Routine 'rest_period' ---
                                                for (const thisComponent of rest_periodComponents) {
                                                  if (typeof thisComponent.setAutoDraw === 'function') {
                                                    thisComponent.setAutoDraw(false);
                                                  }
                                                }
                                                psychoJS.experiment.addData('rest_period.stopped', globalClock.getTime());
                                                // Run 'End Routine' code from set_trigger_rest
                                                endTrigger = trigger_dict["replay_break_end"];
                                                if ((! replay_endtrig_sent)) {
                                                    bids.trigger(endTrigger, {"label": "replay_break_end", "on_flip": false});
                                                    replay_endtrig_sent = true;
                                                }
                                                
                                                // Run 'End Routine' code from bids_break_logging
                                                bids.mark_offset(fix_cross);
                                                
                                                // the Routine "rest_period" was not non-slip safe, so reset the non-slip timer
                                                routineTimer.reset();
                                                
                                                // Routines running outside a loop should always advance the datafile row
                                                if (currentLoop === psychoJS.experiment) {
                                                  psychoJS.experiment.nextEntry(snapshot);
                                                }
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function instruction_retr_startRoutineBegin(snapshot) {
                                              return async function () {
                                                TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                
                                                //--- Prepare to start Routine 'instruction_retr_start' ---
                                                t = 0;
                                                frameN = -1;
                                                continueRoutine = true; // until we're told otherwise
                                                // keep track of whether this Routine was forcibly ended
                                                routineForceEnded = false;
                                                instruction_retr_startClock.reset(routineTimer.getTime());
                                                routineTimer.add(1.000000);
                                                instruction_retr_startMaxDurationReached = false;
                                                // update component parameters for each repeat
                                                // Run 'Begin Routine' code from set_instruction_now_retr_text
                                                if ((language === "english")) {
                                                    instruction_now_retr.text = "You will now retrieve the learned associations.";
                                                }
                                                if ((language === "german")) {
                                                    instruction_now_retr.text = "Sie werden nun die gelernten\nAssoziationen abrufen.";
                                                }
                                                
                                                continue_button_18.keys = undefined;
                                                continue_button_18.rt = undefined;
                                                _continue_button_18_allKeys = [];
                                                psychoJS.experiment.addData('instruction_retr_start.started', globalClock.getTime());
                                                instruction_retr_startMaxDuration = null
                                                // keep track of which components have finished
                                                instruction_retr_startComponents = [];
                                                instruction_retr_startComponents.push(instruction_now_retr);
                                                instruction_retr_startComponents.push(continue_button_18);
                                                
                                                for (const thisComponent of instruction_retr_startComponents)
                                                  if ('status' in thisComponent)
                                                    thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                return Scheduler.Event.NEXT;
                                              }
                                            }
                                            
                                            function instruction_retr_startRoutineEachFrame() {
                                              return async function () {
                                                //--- Loop for each frame of Routine 'instruction_retr_start' ---
                                                // get current time
                                                t = instruction_retr_startClock.getTime();
                                                frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                // update/draw components on each frame
                                                
                                                // *instruction_now_retr* updates
                                                if (t >= 0.0 && instruction_now_retr.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  instruction_now_retr.tStart = t;  // (not accounting for frame time here)
                                                  instruction_now_retr.frameNStart = frameN;  // exact frame index
                                                  
                                                  instruction_now_retr.setAutoDraw(true);
                                                }
                                                
                                                
                                                // if instruction_now_retr is active this frame...
                                                if (instruction_now_retr.status === PsychoJS.Status.STARTED) {
                                                }
                                                
                                                frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (instruction_now_retr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  instruction_now_retr.tStop = t;  // not accounting for scr refresh
                                                  instruction_now_retr.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  instruction_now_retr.status = PsychoJS.Status.FINISHED;
                                                  instruction_now_retr.setAutoDraw(false);
                                                }
                                                
                                                
                                                // *continue_button_18* updates
                                                if (t >= 0.0 && continue_button_18.status === PsychoJS.Status.NOT_STARTED) {
                                                  // keep track of start time/frame for later
                                                  continue_button_18.tStart = t;  // (not accounting for frame time here)
                                                  continue_button_18.frameNStart = frameN;  // exact frame index
                                                  
                                                  // keyboard checking is just starting
                                                  psychoJS.window.callOnFlip(function() { continue_button_18.clock.reset(); });  // t=0 on next screen flip
                                                  psychoJS.window.callOnFlip(function() { continue_button_18.start(); }); // start on screen flip
                                                  psychoJS.window.callOnFlip(function() { continue_button_18.clearEvents(); });
                                                }
                                                frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                if (continue_button_18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                  // keep track of stop time/frame for later
                                                  continue_button_18.tStop = t;  // not accounting for scr refresh
                                                  continue_button_18.frameNStop = frameN;  // exact frame index
                                                  // update status
                                                  continue_button_18.status = PsychoJS.Status.FINISHED;
                                                  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (continue_button_18.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    continue_button_18.tStop = t;  // not accounting for scr refresh
                                                    continue_button_18.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    continue_button_18.status = PsychoJS.Status.FINISHED;
                                                    continue_button_18.status = PsychoJS.Status.FINISHED;
                                                      }
                                                    
                                                  }
                                                  
                                                  // if continue_button_18 is active this frame...
                                                  if (continue_button_18.status === PsychoJS.Status.STARTED) {
                                                    let theseKeys = continue_button_18.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                                    _continue_button_18_allKeys = _continue_button_18_allKeys.concat(theseKeys);
                                                    if (_continue_button_18_allKeys.length > 0) {
                                                      continue_button_18.keys = _continue_button_18_allKeys[0].name;  // just the first key pressed
                                                      continue_button_18.rt = _continue_button_18_allKeys[0].rt;
                                                      continue_button_18.duration = _continue_button_18_allKeys[0].duration;
                                                      // a response ends the routine
                                                      continueRoutine = false;
                                                    }
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of instruction_retr_startComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine && routineTimer.getTime() > 0) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function instruction_retr_startRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'instruction_retr_start' ---
                                                  for (const thisComponent of instruction_retr_startComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('instruction_retr_start.stopped', globalClock.getTime());
                                                  // update the trial handler
                                                  if (currentLoop instanceof MultiStairHandler) {
                                                    currentLoop.addResponse(continue_button_18.corr, level);
                                                  }
                                                  psychoJS.experiment.addData('continue_button_18.keys', continue_button_18.keys);
                                                  if (typeof continue_button_18.keys !== 'undefined') {  // we had a response
                                                      psychoJS.experiment.addData('continue_button_18.rt', continue_button_18.rt);
                                                      psychoJS.experiment.addData('continue_button_18.duration', continue_button_18.duration);
                                                      routineTimer.reset();
                                                      }
                                                  
                                                  continue_button_18.stop();
                                                  if (routineForceEnded) {
                                                      routineTimer.reset();} else if (instruction_retr_startMaxDurationReached) {
                                                      instruction_retr_startClock.add(instruction_retr_startMaxDuration);
                                                  } else {
                                                      instruction_retr_startClock.add(1.000000);
                                                  }
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function set_retrieval_rowsRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'set_retrieval_rows' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  set_retrieval_rowsClock.reset();
                                                  routineTimer.reset();
                                                  set_retrieval_rowsMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  // Run 'Begin Routine' code from take_retr_routes_from_route
                                                  [selected_rows, retr_ptr] = take_block(retr_pool, retr_ptr, (20 * 2));
                                                  console.log(selected_rows);
                                                  
                                                  psychoJS.experiment.addData('set_retrieval_rows.started', globalClock.getTime());
                                                  set_retrieval_rowsMaxDuration = null
                                                  // keep track of which components have finished
                                                  set_retrieval_rowsComponents = [];
                                                  
                                                  for (const thisComponent of set_retrieval_rowsComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function set_retrieval_rowsRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'set_retrieval_rows' ---
                                                  // get current time
                                                  t = set_retrieval_rowsClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of set_retrieval_rowsComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function set_retrieval_rowsRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'set_retrieval_rows' ---
                                                  for (const thisComponent of set_retrieval_rowsComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('set_retrieval_rows.stopped', globalClock.getTime());
                                                  // the Routine "set_retrieval_rows" was not non-slip safe, so reset the non-slip timer
                                                  routineTimer.reset();
                                                  
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function retr_ITIRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'retr_ITI' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  retr_ITIClock.reset();
                                                  routineTimer.reset();
                                                  retr_ITIMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  fix_cross_retrbegin_2.setText('+');
                                                  psychoJS.experiment.addData('retr_ITI.started', globalClock.getTime());
                                                  retr_ITIMaxDuration = null
                                                  // keep track of which components have finished
                                                  retr_ITIComponents = [];
                                                  retr_ITIComponents.push(fix_cross_retrbegin_2);
                                                  
                                                  for (const thisComponent of retr_ITIComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function retr_ITIRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'retr_ITI' ---
                                                  // get current time
                                                  t = retr_ITIClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // Run 'Each Frame' code from bids_retr_question
                                                  bids.schedule_onset(fix_cross_retrbegin_2, {"type_of_stimulus": "fixcross", "component_label": "retrieval_ITIcross", "trial_type": ("retr_" + trial_type.toString()), "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN, "distance_correct": distance_correct});
                                                  
                                                  
                                                  // *fix_cross_retrbegin_2* updates
                                                  if (t >= 0.0 && fix_cross_retrbegin_2.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    fix_cross_retrbegin_2.tStart = t;  // (not accounting for frame time here)
                                                    fix_cross_retrbegin_2.frameNStart = frameN;  // exact frame index
                                                    
                                                    fix_cross_retrbegin_2.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if fix_cross_retrbegin_2 is active this frame...
                                                  if (fix_cross_retrbegin_2.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + iti_dur_retr - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (fix_cross_retrbegin_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    fix_cross_retrbegin_2.tStop = t;  // not accounting for scr refresh
                                                    fix_cross_retrbegin_2.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    fix_cross_retrbegin_2.status = PsychoJS.Status.FINISHED;
                                                    fix_cross_retrbegin_2.setAutoDraw(false);
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of retr_ITIComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function retr_ITIRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'retr_ITI' ---
                                                  for (const thisComponent of retr_ITIComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('retr_ITI.stopped', globalClock.getTime());
                                                  // Run 'End Routine' code from bids_retr_question
                                                  bids.mark_offset(fix_cross_retrbegin_2);
                                                  
                                                  // the Routine "retr_ITI" was not non-slip safe, so reset the non-slip timer
                                                  routineTimer.reset();
                                                  
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function first_imageRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'first_image' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  first_imageClock.reset();
                                                  routineTimer.reset();
                                                  first_imageMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  image_1.setImage(img_first);
                                                  psychoJS.experiment.addData('first_image.started', globalClock.getTime());
                                                  first_imageMaxDuration = null
                                                  // keep track of which components have finished
                                                  first_imageComponents = [];
                                                  first_imageComponents.push(image_1);
                                                  
                                                  for (const thisComponent of first_imageComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function first_imageRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'first_image' ---
                                                  // get current time
                                                  t = first_imageClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // Run 'Each Frame' code from set_trigger_image_1
                                                  ImgTrig = retrIm1Trig;
                                                  if ((frameN === 0)) {
                                                      bids.trigger(ImgTrig, {"stim": image_1, "label": "image_1_retr"});
                                                  }
                                                  
                                                  
                                                  // *image_1* updates
                                                  if (t >= 0.0 && image_1.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    image_1.tStart = t;  // (not accounting for frame time here)
                                                    image_1.frameNStart = frameN;  // exact frame index
                                                    
                                                    image_1.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if image_1 is active this frame...
                                                  if (image_1.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + image_dur_retr_new - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (image_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    image_1.tStop = t;  // not accounting for scr refresh
                                                    image_1.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    image_1.status = PsychoJS.Status.FINISHED;
                                                    image_1.setAutoDraw(false);
                                                  }
                                                  
                                                  // Run 'Each Frame' code from bids_first_retr
                                                  if ((frameN > 0)) {
                                                      bids.schedule_onset(image_1, {"type_of_stimulus": "image", "component_label": "image_1_retr", "trial_type": ("retr_" + trial_type.toString()), "concept_label": img_first.partition("/").slice((- 1))[0], "concept_exemplar": img_first.partition("/").slice((- 1))[0], "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN});
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of first_imageComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function first_imageRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'first_image' ---
                                                  for (const thisComponent of first_imageComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('first_image.stopped', globalClock.getTime());
                                                  // Run 'End Routine' code from bids_first_retr
                                                  bids.mark_offset(image_1);
                                                  
                                                  // the Routine "first_image" was not non-slip safe, so reset the non-slip timer
                                                  routineTimer.reset();
                                                  
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function mask_retr1RoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'mask_retr1' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  mask_retr1Clock.reset(routineTimer.getTime());
                                                  routineTimer.add(0.250000);
                                                  mask_retr1MaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  psychoJS.experiment.addData('mask_retr1.started', globalClock.getTime());
                                                  mask_retr1MaxDuration = null
                                                  // keep track of which components have finished
                                                  mask_retr1Components = [];
                                                  mask_retr1Components.push(mask_img1_2);
                                                  
                                                  for (const thisComponent of mask_retr1Components)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function mask_retr1RoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'mask_retr1' ---
                                                  // get current time
                                                  t = mask_retr1Clock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  
                                                  // *mask_img1_2* updates
                                                  if (t >= 0.0 && mask_img1_2.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    mask_img1_2.tStart = t;  // (not accounting for frame time here)
                                                    mask_img1_2.frameNStart = frameN;  // exact frame index
                                                    
                                                    mask_img1_2.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if mask_img1_2 is active this frame...
                                                  if (mask_img1_2.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (mask_img1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    mask_img1_2.tStop = t;  // not accounting for scr refresh
                                                    mask_img1_2.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    mask_img1_2.status = PsychoJS.Status.FINISHED;
                                                    mask_img1_2.setAutoDraw(false);
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of mask_retr1Components)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine && routineTimer.getTime() > 0) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function mask_retr1RoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'mask_retr1' ---
                                                  for (const thisComponent of mask_retr1Components) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('mask_retr1.stopped', globalClock.getTime());
                                                  if (routineForceEnded) {
                                                      routineTimer.reset();} else if (mask_retr1MaxDurationReached) {
                                                      mask_retr1Clock.add(mask_retr1MaxDuration);
                                                  } else {
                                                      mask_retr1Clock.add(0.250000);
                                                  }
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function second_imageRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'second_image' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  second_imageClock.reset();
                                                  routineTimer.reset();
                                                  second_imageMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  image_2.setImage(img_second);
                                                  psychoJS.experiment.addData('second_image.started', globalClock.getTime());
                                                  second_imageMaxDuration = null
                                                  // keep track of which components have finished
                                                  second_imageComponents = [];
                                                  second_imageComponents.push(image_2);
                                                  
                                                  for (const thisComponent of second_imageComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function second_imageRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'second_image' ---
                                                  // get current time
                                                  t = second_imageClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // Run 'Each Frame' code from set_trigger_image_2
                                                  ImgTrig = retrIm2Trig;
                                                  if ((frameN === 0)) {
                                                      bids.trigger(ImgTrig, {"stim": image_2, "label": "image_2_retr"});
                                                  }
                                                  
                                                  
                                                  // *image_2* updates
                                                  if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    image_2.tStart = t;  // (not accounting for frame time here)
                                                    image_2.frameNStart = frameN;  // exact frame index
                                                    
                                                    image_2.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if image_2 is active this frame...
                                                  if (image_2.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + image_dur_retr_new - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    image_2.tStop = t;  // not accounting for scr refresh
                                                    image_2.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    image_2.status = PsychoJS.Status.FINISHED;
                                                    image_2.setAutoDraw(false);
                                                  }
                                                  
                                                  // Run 'Each Frame' code from bids_second_retr
                                                  if ((frameN > 0)) {
                                                      bids.schedule_onset(image_2, {"type_of_stimulus": "image", "component_label": "image_2_retr", "trial_type": ("retr_" + trial_type.toString()), "concept_label": img_second.partition("/").slice((- 1))[0], "concept_exemplar": img_second.partition("/").slice((- 1))[0], "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN});
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of second_imageComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function second_imageRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'second_image' ---
                                                  for (const thisComponent of second_imageComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('second_image.stopped', globalClock.getTime());
                                                  // Run 'End Routine' code from bids_second_retr
                                                  bids.mark_offset(image_2);
                                                  
                                                  // the Routine "second_image" was not non-slip safe, so reset the non-slip timer
                                                  routineTimer.reset();
                                                  
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function mask_retr2RoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'mask_retr2' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  mask_retr2Clock.reset(routineTimer.getTime());
                                                  routineTimer.add(0.250000);
                                                  mask_retr2MaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  psychoJS.experiment.addData('mask_retr2.started', globalClock.getTime());
                                                  mask_retr2MaxDuration = null
                                                  // keep track of which components have finished
                                                  mask_retr2Components = [];
                                                  mask_retr2Components.push(mask_img2_2);
                                                  
                                                  for (const thisComponent of mask_retr2Components)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function mask_retr2RoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'mask_retr2' ---
                                                  // get current time
                                                  t = mask_retr2Clock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  
                                                  // *mask_img2_2* updates
                                                  if (t >= 0.0 && mask_img2_2.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    mask_img2_2.tStart = t;  // (not accounting for frame time here)
                                                    mask_img2_2.frameNStart = frameN;  // exact frame index
                                                    
                                                    mask_img2_2.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if mask_img2_2 is active this frame...
                                                  if (mask_img2_2.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (mask_img2_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    mask_img2_2.tStop = t;  // not accounting for scr refresh
                                                    mask_img2_2.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    mask_img2_2.status = PsychoJS.Status.FINISHED;
                                                    mask_img2_2.setAutoDraw(false);
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of mask_retr2Components)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine && routineTimer.getTime() > 0) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function mask_retr2RoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'mask_retr2' ---
                                                  for (const thisComponent of mask_retr2Components) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('mask_retr2.stopped', globalClock.getTime());
                                                  if (routineForceEnded) {
                                                      routineTimer.reset();} else if (mask_retr2MaxDurationReached) {
                                                      mask_retr2Clock.add(mask_retr2MaxDuration);
                                                  } else {
                                                      mask_retr2Clock.add(0.250000);
                                                  }
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function reflection_period_retrRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'reflection_period_retr' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  reflection_period_retrClock.reset();
                                                  routineTimer.reset();
                                                  reflection_period_retrMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  // Run 'Begin Routine' code from set_trigger_reflection
                                                  end_trig_send = false;
                                                  
                                                  psychoJS.experiment.addData('reflection_period_retr.started', globalClock.getTime());
                                                  reflection_period_retrMaxDuration = null
                                                  // keep track of which components have finished
                                                  reflection_period_retrComponents = [];
                                                  reflection_period_retrComponents.push(fix_cross_reflretr);
                                                  
                                                  for (const thisComponent of reflection_period_retrComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function reflection_period_retrRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'reflection_period_retr' ---
                                                  // get current time
                                                  t = reflection_period_retrClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // Run 'Each Frame' code from set_trigger_reflection
                                                  ReflTrig = trigger_dict["reflection_per"];
                                                  if ((frameN === 0)) {
                                                      bids.trigger(ReflTrig, {"stim": fix_cross_reflretr, "label": "reflection_start"});
                                                  }
                                                  
                                                  
                                                  // *fix_cross_reflretr* updates
                                                  if (t >= 0.0 && fix_cross_reflretr.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    fix_cross_reflretr.tStart = t;  // (not accounting for frame time here)
                                                    fix_cross_reflretr.frameNStart = frameN;  // exact frame index
                                                    
                                                    fix_cross_reflretr.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if fix_cross_reflretr is active this frame...
                                                  if (fix_cross_reflretr.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + reflection_win_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (fix_cross_reflretr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    fix_cross_reflretr.tStop = t;  // not accounting for scr refresh
                                                    fix_cross_reflretr.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    fix_cross_reflretr.status = PsychoJS.Status.FINISHED;
                                                    fix_cross_reflretr.setAutoDraw(false);
                                                  }
                                                  
                                                  // check for quit (typically the Esc key)
                                                  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                    return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                  }
                                                  
                                                  // check if the Routine should terminate
                                                  if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                    routineForceEnded = true;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                  
                                                  continueRoutine = false;  // reverts to True if at least one component still running
                                                  for (const thisComponent of reflection_period_retrComponents)
                                                    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                      continueRoutine = true;
                                                      break;
                                                    }
                                                  
                                                  // refresh the screen if continuing
                                                  if (continueRoutine) {
                                                    return Scheduler.Event.FLIP_REPEAT;
                                                  } else {
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                };
                                              }
                                              
                                              function reflection_period_retrRoutineEnd(snapshot) {
                                                return async function () {
                                                  //--- Ending Routine 'reflection_period_retr' ---
                                                  for (const thisComponent of reflection_period_retrComponents) {
                                                    if (typeof thisComponent.setAutoDraw === 'function') {
                                                      thisComponent.setAutoDraw(false);
                                                    }
                                                  }
                                                  psychoJS.experiment.addData('reflection_period_retr.stopped', globalClock.getTime());
                                                  // Run 'End Routine' code from set_trigger_reflection
                                                  ReflTrigEnd = trigger_dict["reflection_per_end"];
                                                  if ((! end_trig_send)) {
                                                      bids.trigger(ReflTrigEnd, {"label": "reflection_end", "on_flip": false});
                                                      end_trig_send = true;
                                                      core.wait(0.01);
                                                  }
                                                  
                                                  // the Routine "reflection_period_retr" was not non-slip safe, so reset the non-slip timer
                                                  routineTimer.reset();
                                                  
                                                  // Routines running outside a loop should always advance the datafile row
                                                  if (currentLoop === psychoJS.experiment) {
                                                    psychoJS.experiment.nextEntry(snapshot);
                                                  }
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function retr_response_orderRoutineBegin(snapshot) {
                                                return async function () {
                                                  TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                  
                                                  //--- Prepare to start Routine 'retr_response_order' ---
                                                  t = 0;
                                                  frameN = -1;
                                                  continueRoutine = true; // until we're told otherwise
                                                  // keep track of whether this Routine was forcibly ended
                                                  routineForceEnded = false;
                                                  retr_response_orderClock.reset();
                                                  routineTimer.reset();
                                                  retr_response_orderMaxDurationReached = false;
                                                  // update component parameters for each repeat
                                                  // Run 'Begin Routine' code from clear_clock_3
                                                  window.retr_response_prcMaxDuration = null; 
                                                  window.retr_response_prcComponents = null; 
                                                  
                                                  window._resp_2_allKeys = null; 
                                                  resp_2.clearEvents();
                                                  
                                                  window.retrClock = new util.Clock();
                                                  window.retrClock.reset();
                                                  yes_txt.setPos((leftside_retr if (opt_left == 'yes') else rightside_retr));
                                                  no_txt.setPos((rightside_retr if (opt_right == 'no') else leftside_retr));
                                                  // Run 'Begin Routine' code from set_option_text_2
                                                  if ((language === "english")) {
                                                      yes_txt.text = "yes";
                                                      no_txt.text = "no";
                                                  }
                                                  if ((language === "german")) {
                                                      yes_txt.text = "ja";
                                                      no_txt.text = "nein";
                                                  }
                                                  if ((language === "french")) {
                                                      yes_txt.text = "oui";
                                                      no_txt.text = "non";
                                                  }
                                                  
                                                  // Run 'Begin Routine' code from end_routine_after_resp
                                                  responded_retr = false;
                                                  
                                                  chooseNowText_2.setOpacity(0.0);
                                                  resp.keys = undefined;
                                                  resp.rt = undefined;
                                                  _resp_allKeys = [];
                                                  // Run 'Begin Routine' code from set_trigger_retr_response
                                                  retr_trig_sent = false;
                                                  
                                                  psychoJS.experiment.addData('retr_response_order.started', globalClock.getTime());
                                                  retr_response_orderMaxDuration = null
                                                  // keep track of which components have finished
                                                  retr_response_orderComponents = [];
                                                  retr_response_orderComponents.push(polygon_6);
                                                  retr_response_orderComponents.push(yes_txt);
                                                  retr_response_orderComponents.push(no_txt);
                                                  retr_response_orderComponents.push(chooseNowText_2);
                                                  retr_response_orderComponents.push(resp);
                                                  
                                                  for (const thisComponent of retr_response_orderComponents)
                                                    if ('status' in thisComponent)
                                                      thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                  return Scheduler.Event.NEXT;
                                                }
                                              }
                                              
                                              function retr_response_orderRoutineEachFrame() {
                                                return async function () {
                                                  //--- Loop for each frame of Routine 'retr_response_order' ---
                                                  // get current time
                                                  t = retr_response_orderClock.getTime();
                                                  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                  // update/draw components on each frame
                                                  // Run 'Each Frame' code from set_trigger_opt_onset
                                                  OptTrig = trigger_dict["order_retrieval_options"];
                                                  if ((frameN === 0)) {
                                                      bids.trigger(OptTrig, {"stim": yes_txt, "label": "order_options"});
                                                      core.wait(0.01);
                                                  }
                                                  
                                                  
                                                  // *polygon_6* updates
                                                  if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    polygon_6.tStart = t;  // (not accounting for frame time here)
                                                    polygon_6.frameNStart = frameN;  // exact frame index
                                                    
                                                    polygon_6.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if polygon_6 is active this frame...
                                                  if (polygon_6.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  
                                                  // *yes_txt* updates
                                                  if (t >= 0.0 && yes_txt.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    yes_txt.tStart = t;  // (not accounting for frame time here)
                                                    yes_txt.frameNStart = frameN;  // exact frame index
                                                    
                                                    yes_txt.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if yes_txt is active this frame...
                                                  if (yes_txt.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + retr_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (yes_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    yes_txt.tStop = t;  // not accounting for scr refresh
                                                    yes_txt.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    yes_txt.status = PsychoJS.Status.FINISHED;
                                                    yes_txt.setAutoDraw(false);
                                                  }
                                                  
                                                  
                                                  // *no_txt* updates
                                                  if (t >= 0.0 && no_txt.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    no_txt.tStart = t;  // (not accounting for frame time here)
                                                    no_txt.frameNStart = frameN;  // exact frame index
                                                    
                                                    no_txt.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if no_txt is active this frame...
                                                  if (no_txt.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  frameRemains = 0.0 + retr_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (no_txt.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    no_txt.tStop = t;  // not accounting for scr refresh
                                                    no_txt.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    no_txt.status = PsychoJS.Status.FINISHED;
                                                    no_txt.setAutoDraw(false);
                                                  }
                                                  
                                                  // Run 'Each Frame' code from end_routine_after_resp
                                                  var _pj;
                                                  function _pj_snippets(container) {
                                                      function in_es6(left, right) {
                                                          if (((right instanceof Array) || ((typeof right) === "string"))) {
                                                              return (right.indexOf(left) > (- 1));
                                                          } else {
                                                              if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                                                                  return right.has(left);
                                                              } else {
                                                                  return (left in right);
                                                              }
                                                          }
                                                      }
                                                      container["in_es6"] = in_es6;
                                                      return container;
                                                  }
                                                  _pj = {};
                                                  _pj_snippets(_pj);
                                                  if (_pj.in_es6(trial_type, [1, 2])) {
                                                      if ((resp.keys && (! responded_retr))) {
                                                          responded_retr = true;
                                                          console.log("trial type num", trial_type);
                                                          continueRoutine = false;
                                                      }
                                                  }
                                                  
                                                  
                                                  // *chooseNowText_2* updates
                                                  if (t >= 0.0 && chooseNowText_2.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    chooseNowText_2.tStart = t;  // (not accounting for frame time here)
                                                    chooseNowText_2.frameNStart = frameN;  // exact frame index
                                                    
                                                    chooseNowText_2.setAutoDraw(true);
                                                  }
                                                  
                                                  
                                                  // if chooseNowText_2 is active this frame...
                                                  if (chooseNowText_2.status === PsychoJS.Status.STARTED) {
                                                  }
                                                  
                                                  
                                                  // *resp* updates
                                                  if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
                                                    // keep track of start time/frame for later
                                                    resp.tStart = t;  // (not accounting for frame time here)
                                                    resp.frameNStart = frameN;  // exact frame index
                                                    
                                                    // keyboard checking is just starting
                                                    psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
                                                    psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
                                                    psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
                                                  }
                                                  frameRemains = 0.0 + retr_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                  if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                    // keep track of stop time/frame for later
                                                    resp.tStop = t;  // not accounting for scr refresh
                                                    resp.frameNStop = frameN;  // exact frame index
                                                    // update status
                                                    resp.status = PsychoJS.Status.FINISHED;
                                                    frameRemains = 0.0 + retr_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                      // keep track of stop time/frame for later
                                                      resp.tStop = t;  // not accounting for scr refresh
                                                      resp.frameNStop = frameN;  // exact frame index
                                                      // update status
                                                      resp.status = PsychoJS.Status.FINISHED;
                                                      resp.status = PsychoJS.Status.FINISHED;
                                                        }
                                                      
                                                    }
                                                    
                                                    // if resp is active this frame...
                                                    if (resp.status === PsychoJS.Status.STARTED) {
                                                      let theseKeys = resp.getKeys({keyList: [left_key,right_key], waitRelease: false});
                                                      _resp_allKeys = _resp_allKeys.concat(theseKeys);
                                                      if (_resp_allKeys.length > 0) {
                                                        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
                                                        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
                                                        resp.duration = _resp_allKeys[_resp_allKeys.length - 1].duration;
                                                      }
                                                    }
                                                    
                                                    // Run 'Each Frame' code from set_trigger_retr_response
                                                    RespTrig = trigger_dict["order_retrieval_response"];
                                                    if (((! retr_trig_sent) && resp.keys)) {
                                                        retr_trig_sent = true;
                                                        bids.trigger(RespTrig, {"label": "order_response", "on_flip": false, "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN});
                                                        core.wait(0.01);
                                                    }
                                                    
                                                    // check for quit (typically the Esc key)
                                                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                    }
                                                    
                                                    // check if the Routine should terminate
                                                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                      routineForceEnded = true;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                    
                                                    continueRoutine = false;  // reverts to True if at least one component still running
                                                    for (const thisComponent of retr_response_orderComponents)
                                                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                        continueRoutine = true;
                                                        break;
                                                      }
                                                    
                                                    // refresh the screen if continuing
                                                    if (continueRoutine) {
                                                      return Scheduler.Event.FLIP_REPEAT;
                                                    } else {
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  };
                                                }
                                                
                                                function retr_response_orderRoutineEnd(snapshot) {
                                                  return async function () {
                                                    //--- Ending Routine 'retr_response_order' ---
                                                    for (const thisComponent of retr_response_orderComponents) {
                                                      if (typeof thisComponent.setAutoDraw === 'function') {
                                                        thisComponent.setAutoDraw(false);
                                                      }
                                                    }
                                                    psychoJS.experiment.addData('retr_response_order.stopped', globalClock.getTime());
                                                    // update the trial handler
                                                    if (currentLoop instanceof MultiStairHandler) {
                                                      currentLoop.addResponse(resp.corr, level);
                                                    }
                                                    psychoJS.experiment.addData('resp.keys', resp.keys);
                                                    if (typeof resp.keys !== 'undefined') {  // we had a response
                                                        psychoJS.experiment.addData('resp.rt', resp.rt);
                                                        psychoJS.experiment.addData('resp.duration', resp.duration);
                                                        }
                                                    
                                                    resp.stop();
                                                    // Run 'End Routine' code from bids_retr_response
                                                    pressed = resp.keys;
                                                    if ((pressed instanceof list)) {
                                                        pressed = (pressed ? pressed.slice((- 1))[0] : "m");
                                                    }
                                                    chosen_pos = key2pos.get(pressed, null);
                                                    
                                                    // the Routine "retr_response_order" was not non-slip safe, so reset the non-slip timer
                                                    routineTimer.reset();
                                                    
                                                    // Routines running outside a loop should always advance the datafile row
                                                    if (currentLoop === psychoJS.experiment) {
                                                      psychoJS.experiment.nextEntry(snapshot);
                                                    }
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                }
                                                
                                                function too_slow_routine_1RoutineBegin(snapshot) {
                                                  return async function () {
                                                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                    
                                                    //--- Prepare to start Routine 'too_slow_routine_1' ---
                                                    t = 0;
                                                    frameN = -1;
                                                    continueRoutine = true; // until we're told otherwise
                                                    // keep track of whether this Routine was forcibly ended
                                                    routineForceEnded = false;
                                                    too_slow_routine_1Clock.reset();
                                                    routineTimer.reset();
                                                    too_slow_routine_1MaxDurationReached = false;
                                                    // update component parameters for each repeat
                                                    // Run 'Begin Routine' code from determine_start_4
                                                    if (responded_retr) {
                                                        continueRoutine = false;
                                                    }
                                                    
                                                    tooSlowtext_4.setText('');
                                                    // Run 'Begin Routine' code from set_slow_msg_text_4
                                                    if ((language === "english")) {
                                                        tooSlowtext_4.text = "Too slow. You need to respond faster.";
                                                    }
                                                    if ((language === "german")) {
                                                        tooSlowtext_4.text = "Zu langsam. Sie m\u00fcssen schneller antworten.";
                                                    }
                                                    if ((language === "french")) {
                                                        tooSlowtext_4.text = "Trop lent. Vous devez r\u00e9pondre plus rapidement. ";
                                                    }
                                                    
                                                    psychoJS.experiment.addData('too_slow_routine_1.started', globalClock.getTime());
                                                    too_slow_routine_1MaxDuration = null
                                                    // keep track of which components have finished
                                                    too_slow_routine_1Components = [];
                                                    too_slow_routine_1Components.push(tooSlowtext_4);
                                                    
                                                    for (const thisComponent of too_slow_routine_1Components)
                                                      if ('status' in thisComponent)
                                                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                }
                                                
                                                function too_slow_routine_1RoutineEachFrame() {
                                                  return async function () {
                                                    //--- Loop for each frame of Routine 'too_slow_routine_1' ---
                                                    // get current time
                                                    t = too_slow_routine_1Clock.getTime();
                                                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                    // update/draw components on each frame
                                                    
                                                    // *tooSlowtext_4* updates
                                                    if (t >= 0.0 && tooSlowtext_4.status === PsychoJS.Status.NOT_STARTED) {
                                                      // keep track of start time/frame for later
                                                      tooSlowtext_4.tStart = t;  // (not accounting for frame time here)
                                                      tooSlowtext_4.frameNStart = frameN;  // exact frame index
                                                      
                                                      tooSlowtext_4.setAutoDraw(true);
                                                    }
                                                    
                                                    
                                                    // if tooSlowtext_4 is active this frame...
                                                    if (tooSlowtext_4.status === PsychoJS.Status.STARTED) {
                                                    }
                                                    
                                                    frameRemains = 0.0 + too_slow_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                    if (tooSlowtext_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                      // keep track of stop time/frame for later
                                                      tooSlowtext_4.tStop = t;  // not accounting for scr refresh
                                                      tooSlowtext_4.frameNStop = frameN;  // exact frame index
                                                      // update status
                                                      tooSlowtext_4.status = PsychoJS.Status.FINISHED;
                                                      tooSlowtext_4.setAutoDraw(false);
                                                    }
                                                    
                                                    // check for quit (typically the Esc key)
                                                    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                    }
                                                    
                                                    // check if the Routine should terminate
                                                    if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                      routineForceEnded = true;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                    
                                                    continueRoutine = false;  // reverts to True if at least one component still running
                                                    for (const thisComponent of too_slow_routine_1Components)
                                                      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                        continueRoutine = true;
                                                        break;
                                                      }
                                                    
                                                    // refresh the screen if continuing
                                                    if (continueRoutine) {
                                                      return Scheduler.Event.FLIP_REPEAT;
                                                    } else {
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  };
                                                }
                                                
                                                function too_slow_routine_1RoutineEnd(snapshot) {
                                                  return async function () {
                                                    //--- Ending Routine 'too_slow_routine_1' ---
                                                    for (const thisComponent of too_slow_routine_1Components) {
                                                      if (typeof thisComponent.setAutoDraw === 'function') {
                                                        thisComponent.setAutoDraw(false);
                                                      }
                                                    }
                                                    psychoJS.experiment.addData('too_slow_routine_1.stopped', globalClock.getTime());
                                                    // the Routine "too_slow_routine_1" was not non-slip safe, so reset the non-slip timer
                                                    routineTimer.reset();
                                                    
                                                    // Routines running outside a loop should always advance the datafile row
                                                    if (currentLoop === psychoJS.experiment) {
                                                      psychoJS.experiment.nextEntry(snapshot);
                                                    }
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                }
                                                
                                                function retr_response_distanceRoutineBegin(snapshot) {
                                                  return async function () {
                                                    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                    
                                                    //--- Prepare to start Routine 'retr_response_distance' ---
                                                    t = 0;
                                                    frameN = -1;
                                                    continueRoutine = true; // until we're told otherwise
                                                    // keep track of whether this Routine was forcibly ended
                                                    routineForceEnded = false;
                                                    retr_response_distanceClock.reset();
                                                    routineTimer.reset();
                                                    retr_response_distanceMaxDurationReached = false;
                                                    // update component parameters for each repeat
                                                    // Run 'Begin Routine' code from clear_clock_4
                                                    window.retr_response_prcMaxDuration = null; 
                                                    window.retr_response_prcComponents = null; 
                                                    
                                                    window._resp_2_allKeys = null; 
                                                    resp_2.clearEvents();
                                                    
                                                    window.retrClock = new util.Clock();
                                                    window.retrClock.reset();
                                                    // Run 'Begin Routine' code from controlslider_pos_js
                                                    
                                                    
                                                    window.responded_retr_slider = false; 
                                                    chooseNowText_3.setOpacity(0.0);
                                                    resp_4.keys = undefined;
                                                    resp_4.rt = undefined;
                                                    _resp_4_allKeys = [];
                                                    opt_2.setColor(new util.Color('white'));
                                                    opt_3.setColor(new util.Color('white'));
                                                    opt_4.setColor(new util.Color('white'));
                                                    opt_5.setColor(new util.Color('white'));
                                                    // Run 'Begin Routine' code from set_trigger_retr_response_2
                                                    retr_trig_sent = false;
                                                    
                                                    psychoJS.experiment.addData('retr_response_distance.started', globalClock.getTime());
                                                    retr_response_distanceMaxDuration = null
                                                    // keep track of which components have finished
                                                    retr_response_distanceComponents = [];
                                                    retr_response_distanceComponents.push(chooseNowText_3);
                                                    retr_response_distanceComponents.push(resp_4);
                                                    retr_response_distanceComponents.push(opt_2);
                                                    retr_response_distanceComponents.push(opt_3);
                                                    retr_response_distanceComponents.push(opt_4);
                                                    retr_response_distanceComponents.push(opt_5);
                                                    
                                                    for (const thisComponent of retr_response_distanceComponents)
                                                      if ('status' in thisComponent)
                                                        thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                    return Scheduler.Event.NEXT;
                                                  }
                                                }
                                                
                                                function retr_response_distanceRoutineEachFrame() {
                                                  return async function () {
                                                    //--- Loop for each frame of Routine 'retr_response_distance' ---
                                                    // get current time
                                                    t = retr_response_distanceClock.getTime();
                                                    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                    // update/draw components on each frame
                                                    // Run 'Each Frame' code from set_trigger_opt_onset_2
                                                    OptTrig = trigger_dict["distance_retrieval_options"];
                                                    if ((frameN === 0)) {
                                                        bids.trigger(OptTrig, {"stim": opt_2, "label": "distance_options"});
                                                        core.wait(0.01);
                                                    }
                                                    
                                                    
                                                    // *chooseNowText_3* updates
                                                    if (t >= 0.0 && chooseNowText_3.status === PsychoJS.Status.NOT_STARTED) {
                                                      // keep track of start time/frame for later
                                                      chooseNowText_3.tStart = t;  // (not accounting for frame time here)
                                                      chooseNowText_3.frameNStart = frameN;  // exact frame index
                                                      
                                                      chooseNowText_3.setAutoDraw(true);
                                                    }
                                                    
                                                    
                                                    // if chooseNowText_3 is active this frame...
                                                    if (chooseNowText_3.status === PsychoJS.Status.STARTED) {
                                                    }
                                                    
                                                    frameRemains = 0.0 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                    if (chooseNowText_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                      // keep track of stop time/frame for later
                                                      chooseNowText_3.tStop = t;  // not accounting for scr refresh
                                                      chooseNowText_3.frameNStop = frameN;  // exact frame index
                                                      // update status
                                                      chooseNowText_3.status = PsychoJS.Status.FINISHED;
                                                      chooseNowText_3.setAutoDraw(false);
                                                    }
                                                    
                                                    
                                                    // *resp_4* updates
                                                    if (t >= 0.5 && resp_4.status === PsychoJS.Status.NOT_STARTED) {
                                                      // keep track of start time/frame for later
                                                      resp_4.tStart = t;  // (not accounting for frame time here)
                                                      resp_4.frameNStart = frameN;  // exact frame index
                                                      
                                                      // keyboard checking is just starting
                                                      psychoJS.window.callOnFlip(function() { resp_4.clock.reset(); });  // t=0 on next screen flip
                                                      psychoJS.window.callOnFlip(function() { resp_4.start(); }); // start on screen flip
                                                      psychoJS.window.callOnFlip(function() { resp_4.clearEvents(); });
                                                    }
                                                    frameRemains = 0.5 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                    if (resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                      // keep track of stop time/frame for later
                                                      resp_4.tStop = t;  // not accounting for scr refresh
                                                      resp_4.frameNStop = frameN;  // exact frame index
                                                      // update status
                                                      resp_4.status = PsychoJS.Status.FINISHED;
                                                      frameRemains = 0.5 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        resp_4.tStop = t;  // not accounting for scr refresh
                                                        resp_4.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        resp_4.status = PsychoJS.Status.FINISHED;
                                                        resp_4.status = PsychoJS.Status.FINISHED;
                                                          }
                                                        
                                                      }
                                                      
                                                      // if resp_4 is active this frame...
                                                      if (resp_4.status === PsychoJS.Status.STARTED) {
                                                        let theseKeys = resp_4.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                                        _resp_4_allKeys = _resp_4_allKeys.concat(theseKeys);
                                                        if (_resp_4_allKeys.length > 0) {
                                                          resp_4.keys = _resp_4_allKeys[_resp_4_allKeys.length - 1].name;  // just the last key pressed
                                                          resp_4.rt = _resp_4_allKeys[_resp_4_allKeys.length - 1].rt;
                                                          resp_4.duration = _resp_4_allKeys[_resp_4_allKeys.length - 1].duration;
                                                        }
                                                      }
                                                      
                                                      
                                                      // *opt_2* updates
                                                      if (t >= 0.0 && opt_2.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        opt_2.tStart = t;  // (not accounting for frame time here)
                                                        opt_2.frameNStart = frameN;  // exact frame index
                                                        
                                                        opt_2.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if opt_2 is active this frame...
                                                      if (opt_2.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (opt_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        opt_2.tStop = t;  // not accounting for scr refresh
                                                        opt_2.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        opt_2.status = PsychoJS.Status.FINISHED;
                                                        opt_2.setAutoDraw(false);
                                                      }
                                                      
                                                      
                                                      // *opt_3* updates
                                                      if (t >= 0.0 && opt_3.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        opt_3.tStart = t;  // (not accounting for frame time here)
                                                        opt_3.frameNStart = frameN;  // exact frame index
                                                        
                                                        opt_3.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if opt_3 is active this frame...
                                                      if (opt_3.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (opt_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        opt_3.tStop = t;  // not accounting for scr refresh
                                                        opt_3.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        opt_3.status = PsychoJS.Status.FINISHED;
                                                        opt_3.setAutoDraw(false);
                                                      }
                                                      
                                                      
                                                      // *opt_4* updates
                                                      if (t >= 0.0 && opt_4.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        opt_4.tStart = t;  // (not accounting for frame time here)
                                                        opt_4.frameNStart = frameN;  // exact frame index
                                                        
                                                        opt_4.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if opt_4 is active this frame...
                                                      if (opt_4.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (opt_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        opt_4.tStop = t;  // not accounting for scr refresh
                                                        opt_4.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        opt_4.status = PsychoJS.Status.FINISHED;
                                                        opt_4.setAutoDraw(false);
                                                      }
                                                      
                                                      
                                                      // *opt_5* updates
                                                      if (t >= 0.0 && opt_5.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        opt_5.tStart = t;  // (not accounting for frame time here)
                                                        opt_5.frameNStart = frameN;  // exact frame index
                                                        
                                                        opt_5.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if opt_5 is active this frame...
                                                      if (opt_5.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + retr_dur_slider - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (opt_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        opt_5.tStop = t;  // not accounting for scr refresh
                                                        opt_5.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        opt_5.status = PsychoJS.Status.FINISHED;
                                                        opt_5.setAutoDraw(false);
                                                      }
                                                      
                                                      // Run 'Each Frame' code from set_trigger_retr_response_2
                                                      RespTrig = trigger_dict["distance_retrieval_response"];
                                                      if (((! retr_trig_sent) && resp_4.keys)) {
                                                          retr_trig_sent = true;
                                                          bids.trigger(RespTrig, {"label": "distance_response", "on_flip": false, "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN});
                                                          core.wait(0.01);
                                                      }
                                                      
                                                      // check for quit (typically the Esc key)
                                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                      }
                                                      
                                                      // check if the Routine should terminate
                                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                        routineForceEnded = true;
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                      
                                                      continueRoutine = false;  // reverts to True if at least one component still running
                                                      for (const thisComponent of retr_response_distanceComponents)
                                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                          continueRoutine = true;
                                                          break;
                                                        }
                                                      
                                                      // refresh the screen if continuing
                                                      if (continueRoutine) {
                                                        return Scheduler.Event.FLIP_REPEAT;
                                                      } else {
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                    };
                                                  }
                                                  
                                                  function retr_response_distanceRoutineEnd(snapshot) {
                                                    return async function () {
                                                      //--- Ending Routine 'retr_response_distance' ---
                                                      for (const thisComponent of retr_response_distanceComponents) {
                                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                                          thisComponent.setAutoDraw(false);
                                                        }
                                                      }
                                                      psychoJS.experiment.addData('retr_response_distance.stopped', globalClock.getTime());
                                                      if (trial_type === 3 && !responded_retr_slider) {
                                                          practice_errors += 1;
                                                          resp_2.corr = 0; 
                                                      }
                                                      // update the trial handler
                                                      if (currentLoop instanceof MultiStairHandler) {
                                                        currentLoop.addResponse(resp_4.corr, level);
                                                      }
                                                      psychoJS.experiment.addData('resp_4.keys', resp_4.keys);
                                                      if (typeof resp_4.keys !== 'undefined') {  // we had a response
                                                          psychoJS.experiment.addData('resp_4.rt', resp_4.rt);
                                                          psychoJS.experiment.addData('resp_4.duration', resp_4.duration);
                                                          }
                                                      
                                                      resp_4.stop();
                                                      // Run 'End Routine' code from bids_retr_response_2
                                                      if (resp_4.keys) {
                                                          chosen_num = chosenDis;
                                                          is_correct = (chosen_num === distance_correct);
                                                      }
                                                      bids.add_instant("choice", {"distance_correct": distance_correct, "trial_type": "retr_distance", "block_name": block, "sequence_name": learningSeq, "trial_num": retrieval_trials.thisN, "response": (chosenDis ? chosenDis : "m"), "response_time": (("rt" in resp_4) ? resp_4.rt : null), "correct": is_correct, "expected_response": distance_correct, "response_meaning": chosenDis});
                                                      
                                                      // the Routine "retr_response_distance" was not non-slip safe, so reset the non-slip timer
                                                      routineTimer.reset();
                                                      
                                                      // Routines running outside a loop should always advance the datafile row
                                                      if (currentLoop === psychoJS.experiment) {
                                                        psychoJS.experiment.nextEntry(snapshot);
                                                      }
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function too_slow_routine_2RoutineBegin(snapshot) {
                                                    return async function () {
                                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                      
                                                      //--- Prepare to start Routine 'too_slow_routine_2' ---
                                                      t = 0;
                                                      frameN = -1;
                                                      continueRoutine = true; // until we're told otherwise
                                                      // keep track of whether this Routine was forcibly ended
                                                      routineForceEnded = false;
                                                      too_slow_routine_2Clock.reset();
                                                      routineTimer.reset();
                                                      too_slow_routine_2MaxDurationReached = false;
                                                      // update component parameters for each repeat
                                                      // Run 'Begin Routine' code from determine_start_2
                                                      if (responded_retr_slider) {
                                                          continueRoutine = false;
                                                      }
                                                      
                                                      tooSlowtext_2.setText('');
                                                      // Run 'Begin Routine' code from set_slow_msg_text_2
                                                      if ((language === "english")) {
                                                          tooSlowtext_2.text = "Too slow. You need to respond faster.";
                                                      }
                                                      if ((language === "german")) {
                                                          tooSlowtext_2.text = "Zu langsam. Sie m\u00fcssen schneller antworten.";
                                                      }
                                                      if ((language === "french")) {
                                                          tooSlowtext_2.text = "Trop lent. Vous devez r\u00e9pondre plus rapidement. ";
                                                      }
                                                      
                                                      psychoJS.experiment.addData('too_slow_routine_2.started', globalClock.getTime());
                                                      too_slow_routine_2MaxDuration = null
                                                      // keep track of which components have finished
                                                      too_slow_routine_2Components = [];
                                                      too_slow_routine_2Components.push(tooSlowtext_2);
                                                      
                                                      for (const thisComponent of too_slow_routine_2Components)
                                                        if ('status' in thisComponent)
                                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function too_slow_routine_2RoutineEachFrame() {
                                                    return async function () {
                                                      //--- Loop for each frame of Routine 'too_slow_routine_2' ---
                                                      // get current time
                                                      t = too_slow_routine_2Clock.getTime();
                                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                      // update/draw components on each frame
                                                      
                                                      // *tooSlowtext_2* updates
                                                      if (t >= 0.0 && tooSlowtext_2.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        tooSlowtext_2.tStart = t;  // (not accounting for frame time here)
                                                        tooSlowtext_2.frameNStart = frameN;  // exact frame index
                                                        
                                                        tooSlowtext_2.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if tooSlowtext_2 is active this frame...
                                                      if (tooSlowtext_2.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + too_slow_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (tooSlowtext_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        tooSlowtext_2.tStop = t;  // not accounting for scr refresh
                                                        tooSlowtext_2.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        tooSlowtext_2.status = PsychoJS.Status.FINISHED;
                                                        tooSlowtext_2.setAutoDraw(false);
                                                      }
                                                      
                                                      // check for quit (typically the Esc key)
                                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                      }
                                                      
                                                      // check if the Routine should terminate
                                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                        routineForceEnded = true;
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                      
                                                      continueRoutine = false;  // reverts to True if at least one component still running
                                                      for (const thisComponent of too_slow_routine_2Components)
                                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                          continueRoutine = true;
                                                          break;
                                                        }
                                                      
                                                      // refresh the screen if continuing
                                                      if (continueRoutine) {
                                                        return Scheduler.Event.FLIP_REPEAT;
                                                      } else {
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                    };
                                                  }
                                                  
                                                  function too_slow_routine_2RoutineEnd(snapshot) {
                                                    return async function () {
                                                      //--- Ending Routine 'too_slow_routine_2' ---
                                                      for (const thisComponent of too_slow_routine_2Components) {
                                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                                          thisComponent.setAutoDraw(false);
                                                        }
                                                      }
                                                      psychoJS.experiment.addData('too_slow_routine_2.stopped', globalClock.getTime());
                                                      // Run 'End Routine' code from set_slow_msg_text_2
                                                      bids.close_trial();
                                                      
                                                      // the Routine "too_slow_routine_2" was not non-slip safe, so reset the non-slip timer
                                                      routineTimer.reset();
                                                      
                                                      // Routines running outside a loop should always advance the datafile row
                                                      if (currentLoop === psychoJS.experiment) {
                                                        psychoJS.experiment.nextEntry(snapshot);
                                                      }
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function retr_task_breakRoutineBegin(snapshot) {
                                                    return async function () {
                                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                      
                                                      //--- Prepare to start Routine 'retr_task_break' ---
                                                      t = 0;
                                                      frameN = -1;
                                                      continueRoutine = true; // until we're told otherwise
                                                      // keep track of whether this Routine was forcibly ended
                                                      routineForceEnded = false;
                                                      retr_task_breakClock.reset();
                                                      routineTimer.reset();
                                                      retr_task_breakMaxDurationReached = false;
                                                      // update component parameters for each repeat
                                                      // Run 'Begin Routine' code from determine_break_start
                                                      continueRoutine = (((miniblocks.thisN + 1) % break_after_route) === 0);
                                                      if (continueRoutine) {
                                                          run_break = true;
                                                      } else {
                                                          run_break = false;
                                                      }
                                                      
                                                      // Run 'Begin Routine' code from trigger_long_break_start
                                                      end_trig_send = false;
                                                      
                                                      psychoJS.experiment.addData('retr_task_break.started', globalClock.getTime());
                                                      retr_task_breakMaxDuration = null
                                                      // keep track of which components have finished
                                                      retr_task_breakComponents = [];
                                                      retr_task_breakComponents.push(break_instruction);
                                                      
                                                      for (const thisComponent of retr_task_breakComponents)
                                                        if ('status' in thisComponent)
                                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function retr_task_breakRoutineEachFrame() {
                                                    return async function () {
                                                      //--- Loop for each frame of Routine 'retr_task_break' ---
                                                      // get current time
                                                      t = retr_task_breakClock.getTime();
                                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                      // update/draw components on each frame
                                                      // Run 'Each Frame' code from bids_longbreak_logging
                                                      bids.schedule_onset(break_instruction, {"trial_type": "break", "type_of_stimulus": "long_break_retrieval", "block_name": block, "component_label": "instruction_task_break_ret"});
                                                      
                                                      
                                                      // *break_instruction* updates
                                                      if (t >= 0.0 && break_instruction.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        break_instruction.tStart = t;  // (not accounting for frame time here)
                                                        break_instruction.frameNStart = frameN;  // exact frame index
                                                        
                                                        break_instruction.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if break_instruction is active this frame...
                                                      if (break_instruction.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + break_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (break_instruction.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        break_instruction.tStop = t;  // not accounting for scr refresh
                                                        break_instruction.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        break_instruction.status = PsychoJS.Status.FINISHED;
                                                        break_instruction.setAutoDraw(false);
                                                      }
                                                      
                                                      // Run 'Each Frame' code from trigger_long_break_start
                                                      break_start_trig = trigger_dict["task_break_begin"];
                                                      if ((frameN === 0)) {
                                                          bids.trigger(break_start_trig, {"stim": break_instruction, "label": "task_break_start"});
                                                      }
                                                      
                                                      // check for quit (typically the Esc key)
                                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                      }
                                                      
                                                      // check if the Routine should terminate
                                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                        routineForceEnded = true;
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                      
                                                      continueRoutine = false;  // reverts to True if at least one component still running
                                                      for (const thisComponent of retr_task_breakComponents)
                                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                          continueRoutine = true;
                                                          break;
                                                        }
                                                      
                                                      // refresh the screen if continuing
                                                      if (continueRoutine) {
                                                        return Scheduler.Event.FLIP_REPEAT;
                                                      } else {
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                    };
                                                  }
                                                  
                                                  function retr_task_breakRoutineEnd(snapshot) {
                                                    return async function () {
                                                      //--- Ending Routine 'retr_task_break' ---
                                                      for (const thisComponent of retr_task_breakComponents) {
                                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                                          thisComponent.setAutoDraw(false);
                                                        }
                                                      }
                                                      psychoJS.experiment.addData('retr_task_break.stopped', globalClock.getTime());
                                                      // Run 'End Routine' code from bids_longbreak_logging
                                                      bids.mark_offset(break_instruction);
                                                      
                                                      // Run 'End Routine' code from trigger_long_break_start
                                                      break_end_trig = trigger_dict["task_break_end"];
                                                      if ((run_break && (! end_trig_send))) {
                                                          bids.trigger(break_end_trig, {"label": "task_break_end", "on_flip": false});
                                                          end_trig_send = true;
                                                          core.wait(0.01);
                                                      }
                                                      
                                                      // the Routine "retr_task_break" was not non-slip safe, so reset the non-slip timer
                                                      routineTimer.reset();
                                                      
                                                      // Routines running outside a loop should always advance the datafile row
                                                      if (currentLoop === psychoJS.experiment) {
                                                        psychoJS.experiment.nextEntry(snapshot);
                                                      }
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function instructions_new_learnRoutineBegin(snapshot) {
                                                    return async function () {
                                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                      
                                                      //--- Prepare to start Routine 'instructions_new_learn' ---
                                                      t = 0;
                                                      frameN = -1;
                                                      continueRoutine = true; // until we're told otherwise
                                                      // keep track of whether this Routine was forcibly ended
                                                      routineForceEnded = false;
                                                      instructions_new_learnClock.reset();
                                                      routineTimer.reset();
                                                      instructions_new_learnMaxDurationReached = false;
                                                      // update component parameters for each repeat
                                                      // Run 'Begin Routine' code from set_instruction_newroute
                                                      if ((language === "french")) {
                                                          instruction_text_newroute.text = "Vous allez maintenant r\u00e9apprendre les associations entre les images.";
                                                      }
                                                      if ((language === "english")) {
                                                          instruction_text_newroute.text = "The learning of associations will continue now.";
                                                      }
                                                      if ((language === "german")) {
                                                          instruction_text_newroute.text = "Jetzt geht das Assoziationslernen weiter.";
                                                      }
                                                      
                                                      psychoJS.experiment.addData('instructions_new_learn.started', globalClock.getTime());
                                                      instructions_new_learnMaxDuration = null
                                                      // keep track of which components have finished
                                                      instructions_new_learnComponents = [];
                                                      instructions_new_learnComponents.push(instruction_text_newroute);
                                                      
                                                      for (const thisComponent of instructions_new_learnComponents)
                                                        if ('status' in thisComponent)
                                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function instructions_new_learnRoutineEachFrame() {
                                                    return async function () {
                                                      //--- Loop for each frame of Routine 'instructions_new_learn' ---
                                                      // get current time
                                                      t = instructions_new_learnClock.getTime();
                                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                      // update/draw components on each frame
                                                      
                                                      // *instruction_text_newroute* updates
                                                      if (t >= 0.0 && instruction_text_newroute.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        instruction_text_newroute.tStart = t;  // (not accounting for frame time here)
                                                        instruction_text_newroute.frameNStart = frameN;  // exact frame index
                                                        
                                                        instruction_text_newroute.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if instruction_text_newroute is active this frame...
                                                      if (instruction_text_newroute.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + instr_newroute_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (instruction_text_newroute.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        instruction_text_newroute.tStop = t;  // not accounting for scr refresh
                                                        instruction_text_newroute.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        instruction_text_newroute.status = PsychoJS.Status.FINISHED;
                                                        instruction_text_newroute.setAutoDraw(false);
                                                      }
                                                      
                                                      // check for quit (typically the Esc key)
                                                      if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                        return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                      }
                                                      
                                                      // check if the Routine should terminate
                                                      if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                        routineForceEnded = true;
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                      
                                                      continueRoutine = false;  // reverts to True if at least one component still running
                                                      for (const thisComponent of instructions_new_learnComponents)
                                                        if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                          continueRoutine = true;
                                                          break;
                                                        }
                                                      
                                                      // refresh the screen if continuing
                                                      if (continueRoutine) {
                                                        return Scheduler.Event.FLIP_REPEAT;
                                                      } else {
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                    };
                                                  }
                                                  
                                                  function instructions_new_learnRoutineEnd(snapshot) {
                                                    return async function () {
                                                      //--- Ending Routine 'instructions_new_learn' ---
                                                      for (const thisComponent of instructions_new_learnComponents) {
                                                        if (typeof thisComponent.setAutoDraw === 'function') {
                                                          thisComponent.setAutoDraw(false);
                                                        }
                                                      }
                                                      psychoJS.experiment.addData('instructions_new_learn.stopped', globalClock.getTime());
                                                      // the Routine "instructions_new_learn" was not non-slip safe, so reset the non-slip timer
                                                      routineTimer.reset();
                                                      
                                                      // Routines running outside a loop should always advance the datafile row
                                                      if (currentLoop === psychoJS.experiment) {
                                                        psychoJS.experiment.nextEntry(snapshot);
                                                      }
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function instructions_endRoutineBegin(snapshot) {
                                                    return async function () {
                                                      TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
                                                      
                                                      //--- Prepare to start Routine 'instructions_end' ---
                                                      t = 0;
                                                      frameN = -1;
                                                      continueRoutine = true; // until we're told otherwise
                                                      // keep track of whether this Routine was forcibly ended
                                                      routineForceEnded = false;
                                                      instructions_endClock.reset();
                                                      routineTimer.reset();
                                                      instructions_endMaxDurationReached = false;
                                                      // update component parameters for each repeat
                                                      // Run 'Begin Routine' code from set_trigger_end
                                                      trigNum = trigger_dict["start/end"];
                                                      
                                                      // Run 'Begin Routine' code from set_instructions_end_text
                                                      if ((language === "english")) {
                                                          instructions_end_text.text = "The task is over now. Thank you for your participation.\nPress any key to exit";
                                                      }
                                                      if ((language === "german")) {
                                                          instructions_end_text.text = "Die Aufgabe ist nun vorbei.\nVielen Dank f\u00fcr die Teilnahme. Dr\u00fccken Sie eine beliebige Taste, um das Experiment zu beenden.";
                                                      }
                                                      
                                                      continue_button_2.keys = undefined;
                                                      continue_button_2.rt = undefined;
                                                      _continue_button_2_allKeys = [];
                                                      psychoJS.experiment.addData('instructions_end.started', globalClock.getTime());
                                                      instructions_endMaxDuration = null
                                                      // keep track of which components have finished
                                                      instructions_endComponents = [];
                                                      instructions_endComponents.push(instructions_end_text);
                                                      instructions_endComponents.push(continue_button_2);
                                                      
                                                      for (const thisComponent of instructions_endComponents)
                                                        if ('status' in thisComponent)
                                                          thisComponent.status = PsychoJS.Status.NOT_STARTED;
                                                      return Scheduler.Event.NEXT;
                                                    }
                                                  }
                                                  
                                                  function instructions_endRoutineEachFrame() {
                                                    return async function () {
                                                      //--- Loop for each frame of Routine 'instructions_end' ---
                                                      // get current time
                                                      t = instructions_endClock.getTime();
                                                      frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
                                                      // update/draw components on each frame
                                                      // Run 'Each Frame' code from set_trigger_end
                                                      if ((frameN === 0)) {
                                                          bids.trigger(trigNum, {"stim": instructions_end_text, "label": "exp_end"});
                                                      }
                                                      
                                                      
                                                      // *instructions_end_text* updates
                                                      if (t >= 0.0 && instructions_end_text.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        instructions_end_text.tStart = t;  // (not accounting for frame time here)
                                                        instructions_end_text.frameNStart = frameN;  // exact frame index
                                                        
                                                        instructions_end_text.setAutoDraw(true);
                                                      }
                                                      
                                                      
                                                      // if instructions_end_text is active this frame...
                                                      if (instructions_end_text.status === PsychoJS.Status.STARTED) {
                                                      }
                                                      
                                                      frameRemains = 0.0 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (instructions_end_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        instructions_end_text.tStop = t;  // not accounting for scr refresh
                                                        instructions_end_text.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        instructions_end_text.status = PsychoJS.Status.FINISHED;
                                                        instructions_end_text.setAutoDraw(false);
                                                      }
                                                      
                                                      
                                                      // *continue_button_2* updates
                                                      if (t >= 1 && continue_button_2.status === PsychoJS.Status.NOT_STARTED) {
                                                        // keep track of start time/frame for later
                                                        continue_button_2.tStart = t;  // (not accounting for frame time here)
                                                        continue_button_2.frameNStart = frameN;  // exact frame index
                                                        
                                                        // keyboard checking is just starting
                                                        psychoJS.window.callOnFlip(function() { continue_button_2.clock.reset(); });  // t=0 on next screen flip
                                                        psychoJS.window.callOnFlip(function() { continue_button_2.start(); }); // start on screen flip
                                                        psychoJS.window.callOnFlip(function() { continue_button_2.clearEvents(); });
                                                      }
                                                      frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                      if (continue_button_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                        // keep track of stop time/frame for later
                                                        continue_button_2.tStop = t;  // not accounting for scr refresh
                                                        continue_button_2.frameNStop = frameN;  // exact frame index
                                                        // update status
                                                        continue_button_2.status = PsychoJS.Status.FINISHED;
                                                        frameRemains = 1 + max_read_dur - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
                                                        if (continue_button_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
                                                          // keep track of stop time/frame for later
                                                          continue_button_2.tStop = t;  // not accounting for scr refresh
                                                          continue_button_2.frameNStop = frameN;  // exact frame index
                                                          // update status
                                                          continue_button_2.status = PsychoJS.Status.FINISHED;
                                                          continue_button_2.status = PsychoJS.Status.FINISHED;
                                                            }
                                                          
                                                        }
                                                        
                                                        // if continue_button_2 is active this frame...
                                                        if (continue_button_2.status === PsychoJS.Status.STARTED) {
                                                          let theseKeys = continue_button_2.getKeys({keyList: [left_key,right_key,center_key,down_key], waitRelease: false});
                                                          _continue_button_2_allKeys = _continue_button_2_allKeys.concat(theseKeys);
                                                          if (_continue_button_2_allKeys.length > 0) {
                                                            continue_button_2.keys = _continue_button_2_allKeys[0].name;  // just the first key pressed
                                                            continue_button_2.rt = _continue_button_2_allKeys[0].rt;
                                                            continue_button_2.duration = _continue_button_2_allKeys[0].duration;
                                                            // a response ends the routine
                                                            continueRoutine = false;
                                                          }
                                                        }
                                                        
                                                        // check for quit (typically the Esc key)
                                                        if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
                                                          return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
                                                        }
                                                        
                                                        // check if the Routine should terminate
                                                        if (!continueRoutine) {  // a component has requested a forced-end of Routine
                                                          routineForceEnded = true;
                                                          return Scheduler.Event.NEXT;
                                                        }
                                                        
                                                        continueRoutine = false;  // reverts to True if at least one component still running
                                                        for (const thisComponent of instructions_endComponents)
                                                          if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
                                                            continueRoutine = true;
                                                            break;
                                                          }
                                                        
                                                        // refresh the screen if continuing
                                                        if (continueRoutine) {
                                                          return Scheduler.Event.FLIP_REPEAT;
                                                        } else {
                                                          return Scheduler.Event.NEXT;
                                                        }
                                                      };
                                                    }
                                                    
                                                    function instructions_endRoutineEnd(snapshot) {
                                                      return async function () {
                                                        //--- Ending Routine 'instructions_end' ---
                                                        for (const thisComponent of instructions_endComponents) {
                                                          if (typeof thisComponent.setAutoDraw === 'function') {
                                                            thisComponent.setAutoDraw(false);
                                                          }
                                                        }
                                                        psychoJS.experiment.addData('instructions_end.stopped', globalClock.getTime());
                                                        // update the trial handler
                                                        if (currentLoop instanceof MultiStairHandler) {
                                                          currentLoop.addResponse(continue_button_2.corr, level);
                                                        }
                                                        psychoJS.experiment.addData('continue_button_2.keys', continue_button_2.keys);
                                                        if (typeof continue_button_2.keys !== 'undefined') {  // we had a response
                                                            psychoJS.experiment.addData('continue_button_2.rt', continue_button_2.rt);
                                                            psychoJS.experiment.addData('continue_button_2.duration', continue_button_2.duration);
                                                            routineTimer.reset();
                                                            }
                                                        
                                                        continue_button_2.stop();
                                                        // the Routine "instructions_end" was not non-slip safe, so reset the non-slip timer
                                                        routineTimer.reset();
                                                        
                                                        // Routines running outside a loop should always advance the datafile row
                                                        if (currentLoop === psychoJS.experiment) {
                                                          psychoJS.experiment.nextEntry(snapshot);
                                                        }
                                                        return Scheduler.Event.NEXT;
                                                      }
                                                    }
                                                    
                                                    function importConditions(currentLoop) {
                                                      return async function () {
                                                        psychoJS.importAttributes(currentLoop.getCurrentTrial());
                                                        return Scheduler.Event.NEXT;
                                                        };
                                                    }
                                                    
                                                    async function quitPsychoJS(message, isCompleted) {
                                                      // Check for and save orphaned data
                                                      if (psychoJS.experiment.isEntryEmpty()) {
                                                        psychoJS.experiment.nextEntry();
                                                      }
                                                      psychoJS.window.close();
                                                      psychoJS.quit({message: message, isCompleted: isCompleted});
                                                      
                                                      return Scheduler.Event.QUIT;
                                                    }
