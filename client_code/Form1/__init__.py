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
    
  def make_insult(self):
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
  
  def get_insult_click(self, **event_args):
      self.make_insult()





