from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from random import choice

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def get_old_insult_click(self, **event_args):
    self.make_old_insult()
      
  def get_insult_click(self, **event_args):
    self.make_insult()
    
  def make_old_insult(self):
    insult1 = ['artless', 'bawdy', 'beslubbering', 'bootless',
        'burly-boned', 'caluminous', 'churlish', 'clouted',
        'cockered', 'craven', 'cullionly', 'currish', 'dankish',
        'dissembling', 'droning', 'errant', 'fawning', 'fishified',
        'fobbing', 'frothy', 'froward', 'fusty', 'gleeking',
        'goatish', 'gorbellied', 'impertinent', 'infectious',
        'jarring', 'loggerheaded', 'lumpish', 'mammering', 'mangled',
        'mewling', 'misbegotten', 'odiferous', 'paunchy', 'poisonous',
        'pribbling', 'puking', 'puny', 'qualling', 'rank', 'reeky',
        'roguish', 'ruttish', 'saucy', 'spleeny', 'spongy', 'surly',
        'tottering', 'unmuzzled', 'vain', 'venomed', 'villainous',
        'warped', 'Wart-necked', 'wayward', 'weedy', 'wimpled',
        'yeasty'
    ]
    insult2 = ['base-court', 'bat-fowling', 'beef-witted',
        'beetle-headed', 'boil-brained', 'brazen-faced',
        "bunch-back'd", 'clapper-clawed', 'clay-brained',
        'common-kissing', 'crook-pated', 'dismal-dreaming',
        'dizzy-eyed', 'doghearted', 'dread-bolted', 'earth-vexing',
        'elf-skinned', 'fat-kidneyed', 'fen-sucked', 'flap-mouthed',
        'fly-bitten', 'folly-fallen', 'fool-born', 'full-gorged',
        'guts-griping', 'half-faced', 'hasty-witted', 'hedge-born',
        'hell-hated', 'idle-headed', 'ill-breeding', 'ill-nurtured',
        'knotty-pated', 'leaden-footed', 'lily-livered',
        'malmsey-nosed', 'milk-livered', 'motley-minded',
        'muddy-mettled', 'onion-eyed', "pigeon-liver'd",
        'plume-plucked', 'pottle-deep', 'pox-marked', 'rampallian',
        'reeling-ripe', 'rough-hewn', 'rude-growing', 'rump-fed',
        'scale-sided', 'scurvy-valiant', 'shard-borne',
        'sheep-biting', 'spur-galled', 'swag-bellied', 'tardy-gaited',
        'tickle-brained', 'toad-spotted', 'unchin-snouted',
        "unwash'd", 'weather-bitten', 'whoreson'
    ]
    insult3 = ['apple-john', 'baggage', 'barnacle', 'Basket-Cockle',
        'bladder', 'blind-worm', 'boar-pig', 'bugbear', 'bum-bailey',
        'canker-blossom', 'clack-dish', 'clotpole', 'codpiece',
        'coxcomb', 'death-token', 'devil-monk', 'dewberry',
        'flap-dragon', 'flax-wench', 'flirt-gill', 'foot-licker',
        'fustilarian', 'giglet', 'gudgeon', 'haggard', 'harpy',
        'hedge-pig', 'horn-beast', 'hugger-mugger', 'joithead',
        'jolt-head', 'knave', 'lewdster', 'lout', 'maggot-pie',
        'malcontent', 'malt-worm', 'mammet', 'measle', 'minnow',
        'miscreant', 'moldwarp', 'mumble-news', 'nut-hook',
        'pigeon-egg', 'pignut', 'popinjay', 'pumpion', 'puttock',
        'rascal', 'ratsbane', 'scullian', 'scut', 'skainsmate',
        'strumpet', 'toad', 'varlot', 'vassal', 'wagtail',
        'whey-face'
    ]
    self.output.text = "Thou art a " + choice(insult1) + " " + choice(insult2) + " " + choice(insult3)
      
  def make_insult(self):
    insult1 = ['animalistic', 'appalling', 'awful', 'bad-looking',
        'beastly', 'deformed', 'disfigured', 'foul', 'frightful',
        'grisly', 'gross', 'grotesque', 'hard-featured', 'hideous',
        'horrid', 'ill-favored', 'loathsome', 'misshapen',
        'monstrous', 'not much to look at', 'repelling', 'repugnant',
        'repulsive', 'revolting', 'unbeautiful', 'uncomely',
        'uninviting', 'unlovely', 'unsightly',
    ]
    insult2 = ['abrupt', 'abusive', 'bad-mannered', 'barbaric',
        'barbarous', 'blunt', 'boorish', 'brusque', 'brutish',
        'cheeky', 'churlish', 'coarse', 'crabbed', 'crude', 'curt',
        'discourteous', 'graceless', 'gross', 'gruff', 'ignorant',
        'illiterate', 'impertinent', 'impolite', 'impudent',
        'inconsiderate', 'insolent', 'insulting', 'intrusive',
        'loutish', 'obscene', 'raw', 'savage', 'scurrilous', 'surly',
        'uncivil', 'uncivilized', 'uncouth', 'uncultured',
        'uneducated', 'ungracious', 'unmannerly', 'unpolished',
        'unrefined', 'vulgar', 'wild',
    ]
    insult3 = ['bad guy', 'bad person', 'baddie', 'baddy',
        'black marketeer', 'blackmailer', 'blockhead', 'bonehead',
        'clodpoll', 'con', 'convict', 'cretin', 'crook', 'culprit',
        'delinquent', 'desperado', 'deuce', 'dimwit', 'dork',
        'dumbbell', 'dunce', 'evildoer', 'ex-con', 'felon', 'fool',
        'fugitive', 'gangster', 'guerilla', 'hood', 'hoodlum',
        'hooligan', 'hustler', 'ignoramus', 'imbecile',
        'inside person', 'jailbird', 'jerk', 'lawbreaker',
        'malefactor', 'mobster', 'moron', 'mug', 'muttonhead',
        'nincompoop', 'ninny', 'nitwit', 'offender', 'outlaw',
        'pinhead', 'racketeer', 'simpleton', 'sinner', 'slippery eel',
        'thug', 'tomfool', 'twit', 'wrongdoer', 'yardbird',
    ]
    self.output.text = "You are a " + choice(insult1) + " " + choice(insult2) + " " + choice(insult3)
    


