# Just for testing

bad = {'Abstract': '',
 'AbstractSource': '',
 'AbstractText': '',
 'AbstractURL': '',
 'Answer': '',
 'AnswerType': '',
 'Definition': '',
 'DefinitionSource': '',
 'DefinitionURL': '',
 'Entity': '',
 'Heading': '',
 'Image': '',
 'ImageHeight': '',
 'ImageIsLogo': '',
 'ImageWidth': '',
 'Infobox': '',
 'Redirect': '',
 'RelatedTopics': [],
 'Results': [],
 'Type': '',
 'meta': None}


good = {'Abstract': '',
 'AbstractSource': 'Wikipedia',
 'AbstractText': '',
 'AbstractURL': 'https://en.wikipedia.org/wiki/Napoleon_(disambiguation)',
 'Answer': '',
 'AnswerType': '',
 'Definition': '',
 'DefinitionSource': '',
 'DefinitionURL': '',
 'Entity': '',
 'Heading': 'Napoleon',
 'Image': '',
 'ImageHeight': 0,
 'ImageIsLogo': 0,
 'ImageWidth': 0,
 'Infobox': '',
 'Redirect': '',
 'RelatedTopics': [{'FirstURL': 'https://duckduckgo.com/Napoleon',
                    'Icon': {'Height': '',
                             'URL': 'https://duckduckgo.com/i/d8609064.jpg',
                             'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/Napoleon">Napoleon</a> '
                              'A French statesman and military leader who rose '
                              'to prominence during the French Revolution...',
                    'Text': 'Napoleon A French statesman and military leader '
                            'who rose to prominence during the French '
                            'Revolution...'},
                   {'FirstURL': 'https://duckduckgo.com/Napoleon_III',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/Napoleon_III">Napoleon '
                              'III</a>The President of France from 1848 to '
                              '1852 and, as Napoleon III, the Emperor of the '
                              'French from...',
                    'Text': 'Napoleon III The President of France from 1848 to '
                            '1852 and, as Napoleon III, the Emperor of the '
                            'French from...'},
                   {'FirstURL': 'https://duckduckgo.com/Mille-feuille',
                    'Icon': {'Height': '',
                             'URL': 'https://duckduckgo.com/i/cf7f194d.jpg',
                             'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/Mille-feuille">Napoleon '
                              '(pastry)</a>A French pastry whose exact origin '
                              'is unknown.',
                    'Text': 'Napoleon (pastry) A French pastry whose exact '
                            'origin is unknown.'},
                   {'FirstURL': 'https://duckduckgo.com/Napoleone',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/Napoleone">Napoleone</a> '
                              'An Italian male given name.',
                    'Text': 'Napoleone An Italian male given name.'},
                   {'Name': 'People',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napoleon_II',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/b7a58b65.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_II">Napoleon '
                                          'II</a>The son of Napoleon I, '
                                          'Emperor of the French, and his '
                                          'second wife, Archduchess Marie '
                                          'Louise of...',
                                'Text': 'Napoleon II The son of Napoleon I, '
                                        'Emperor of the French, and his second '
                                        'wife, Archduchess Marie Louise of...'},
                               {'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on%2C_Prince_Imperial',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/d65d42bd.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on%2C_Prince_Imperial">Napoléon, '
                                          'Prince Imperial</a>The only child '
                                          'of Emperor Napoleon III and his '
                                          'Empress consort, Eugénie de '
                                          'Montijo.',
                                'Text': 'Napoléon, Prince Imperial The only '
                                        'child of Emperor Napoleon III and his '
                                        'Empress consort, Eugénie de Montijo.'},
                               {'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on%2C_comte_Daru',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/290a2701.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on%2C_comte_Daru">Napoléon, '
                                          'comte Daru</a> A French soldier and '
                                          'politician.',
                                'Text': 'Napoléon, comte Daru A French soldier '
                                        'and politician.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(actor)',
                                'Icon': {'Height': 16,
                                         'URL': 'https://duckduckgo.com/i/www.actornapoleon.com.ico',
                                         'Width': 16},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(actor)">Napoleon '
                                          '(actor)</a>An Indian film actor, '
                                          'politician and the founder and '
                                          'chairman of the Jeevan '
                                          'Technologies.',
                                'Text': 'Napoleon (actor) An Indian film '
                                        'actor, politician and the founder and '
                                        'chairman of the Jeevan Technologies.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(rapper)',
                                'Icon': {'Height': 16,
                                         'URL': 'https://duckduckgo.com/i/www.napoleonoutlawed.com.ico',
                                         'Width': 16},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(rapper)">Napoleon '
                                          '(rapper)</a>A former member of '
                                          "Tupac Shakur's rap group Outlawz.",
                                'Text': 'Napoleon (rapper) A former member of '
                                        "Tupac Shakur's rap group Outlawz."}]},
                   {'Name': 'Places',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napoleons%2C_Victoria',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/4f60e7cd.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleons%2C_Victoria">Napoleons</a>A '
                                          'town in Victoria, Australia in the '
                                          'Golden Plains Shire local '
                                          'government area, west of the '
                                          'state...',
                                'Text': 'Napoleons A town in Victoria, '
                                        'Australia in the Golden Plains Shire '
                                        'local government area, west of the '
                                        'state...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Silesian_Voivodeship',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Silesian_Voivodeship">Napoleon, '
                                          'Silesian Voivodeship</a>A village '
                                          'in the administrative district of '
                                          'Gmina Lipie, within Kłobuck County, '
                                          'Silesian...',
                                'Text': 'Napoleon, Silesian Voivodeship A '
                                        'village in the administrative '
                                        'district of Gmina Lipie, within '
                                        'Kłobuck County, Silesian...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Arkansas',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Arkansas">Napoleon, '
                                          'Arkansas</a>A "drowned town" in '
                                          'Desha County, Arkansas, United '
                                          'States, near the confluence of the '
                                          'Arkansas...',
                                'Text': 'Napoleon, Arkansas A "drowned town" '
                                        'in Desha County, Arkansas, United '
                                        'States, near the confluence of the '
                                        'Arkansas...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Indiana',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/cabf59f9.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Indiana">Napoleon, '
                                          'Indiana</a>A town in Jackson '
                                          'Township, Ripley County, in the '
                                          'U.S. state of Indiana.',
                                'Text': 'Napoleon, Indiana A town in Jackson '
                                        'Township, Ripley County, in the U.S. '
                                        'state of Indiana.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Kentucky',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Kentucky">Napoleon, '
                                          'Kentucky</a> An unincorporated '
                                          'community located in Gallatin '
                                          'County, Kentucky, United States.',
                                'Text': 'Napoleon, Kentucky An unincorporated '
                                        'community located in Gallatin County, '
                                        'Kentucky, United States.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Michigan',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Michigan">Napoleon, '
                                          'Michigan</a>An unincorporated '
                                          'community in Napoleon Township of '
                                          'Jackson County in the U.S. state of '
                                          'Michigan.',
                                'Text': 'Napoleon, Michigan An unincorporated '
                                        'community in Napoleon Township of '
                                        'Jackson County in the U.S. state of '
                                        'Michigan.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Mississippi',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Mississippi">Napoleon, '
                                          'Mississippi</a> An unincorporated '
                                          'community in Hancock County, '
                                          'Mississippi, United States.',
                                'Text': 'Napoleon, Mississippi An '
                                        'unincorporated community in Hancock '
                                        'County, Mississippi, United States.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Missouri',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/b27f2c9e.png',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Missouri">Napoleon, '
                                          'Missouri</a>A city in Lafayette '
                                          'County, Missouri, United States.',
                                'Text': 'Napoleon, Missouri A city in '
                                        'Lafayette County, Missouri, United '
                                        'States.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_North_Dakota',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/403d9a43.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_North_Dakota">Napoleon, '
                                          'North Dakota</a>A city in Logan '
                                          'County, North Dakota, United '
                                          'States. It is the county seat of '
                                          'Logan County.',
                                'Text': 'Napoleon, North Dakota A city in '
                                        'Logan County, North Dakota, United '
                                        'States. It is the county seat of '
                                        'Logan County.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%2C_Ohio',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/c50024ee.png',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%2C_Ohio">Napoleon, '
                                          'Ohio</a>A city in and the county '
                                          'seat of Henry County, Ohio, United '
                                          'States, along the Maumee River '
                                          '44...',
                                'Text': 'Napoleon, Ohio A city in and the '
                                        'county seat of Henry County, Ohio, '
                                        'United States, along the Maumee River '
                                        '44...'}]},
                   {'Name': 'Fictional characters',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napoleon_(Animal_Farm)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(Animal_Farm)">Napoleon '
                                          '(Animal Farm)</a> A fictional '
                                          'character and the main antagonist '
                                          "in George Orwell's Animal Farm.",
                                'Text': 'Napoleon (Animal Farm) A fictional '
                                        'character and the main antagonist in '
                                        "George Orwell's Animal Farm."}]},
                   {'Name': 'Gaming',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napoleon_(card_game)',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/7e083eba.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(card_game)">Napoleon '
                                          '(card game)</a>A straightforward '
                                          'trick-taking game in which players '
                                          'receive five cards each; whoever '
                                          'bids the...',
                                'Text': 'Napoleon (card game) A '
                                        'straightforward trick-taking game in '
                                        'which players receive five cards '
                                        'each; whoever bids the...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(game)',
                                'Icon': {'Height': 16,
                                         'URL': 'https://duckduckgo.com/i/www.columbiagames.com.ico',
                                         'Width': 16},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(game)">Napoleon '
                                          '(game)</a>A strategic-level board '
                                          'wargame designed by Tom Dalgliesh '
                                          'covering the Waterloo Campaign of '
                                          'the...',
                                'Text': 'Napoleon (game) A strategic-level '
                                        'board wargame designed by Tom '
                                        'Dalgliesh covering the Waterloo '
                                        'Campaign of the...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(video_game)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(video_game)">Napoleon '
                                          '(GBA game)</a>A real-time strategy '
                                          'video game for the Game Boy Advance '
                                          'developed by Genki and published '
                                          'by...',
                                'Text': 'Napoleon (GBA game) A real-time '
                                        'strategy video game for the Game Boy '
                                        'Advance developed by Genki and '
                                        'published by...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon%3A_Total_War',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/c50aa0db.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon%3A_Total_War">Napoleon: '
                                          'Total War</a> A turn-based strategy '
                                          'and real-time tactics video game '
                                          'developed by The Creative Assembly '
                                          'and...',
                                'Text': 'Napoleon: Total War A turn-based '
                                        'strategy and real-time tactics video '
                                        'game developed by The Creative '
                                        'Assembly and...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_Opening',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_Opening">Napoleon '
                                          'Opening</a> An irregular chess '
                                          'opening starting with the moves...',
                                'Text': 'Napoleon Opening An irregular chess '
                                        'opening starting with the moves...'},
                               {'FirstURL': 'https://duckduckgo.com/Scotch_Game',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Scotch_Game">Napoleon '
                                          'Gambit</a> A chess opening that '
                                          'begins with the moves...',
                                'Text': 'Napoleon Gambit A chess opening that '
                                        'begins with the moves...'}]},
                   {'Name': 'Music',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napoleonic_(EP)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleonic_(EP)">Napoleonic '
                                          '(EP)</a> The title of The Four '
                                          "Hundred's first EP. The EP was "
                                          'released independently in 2006.',
                                'Text': 'Napoleonic (EP) The title of The Four '
                                        "Hundred's first EP. The EP was "
                                        'released independently in 2006.'}]},
                   {'Name': 'Stage and screen',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on_(1927_film)',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/26bedaa4.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on_(1927_film)">Napoléon '
                                          '(1927 film)</a>A 1927 silent French '
                                          'epic film written, produced, and '
                                          'directed by Abel Gance that tells '
                                          'the story...',
                                'Text': 'Napoléon (1927 film) A 1927 silent '
                                        'French epic film written, produced, '
                                        'and directed by Abel Gance that tells '
                                        'the story...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(1951_film)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(1951_film)">Napoleon '
                                          '(1951 film)</a>A 1951 Italian '
                                          'comedy film directed by Carlo '
                                          'Borghesio and starring Renato '
                                          'Rascel in the title role.',
                                'Text': 'Napoleon (1951 film) A 1951 Italian '
                                        'comedy film directed by Carlo '
                                        'Borghesio and starring Renato Rascel '
                                        'in the title role.'},
                               {'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on_(1955_film)',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/dfa52c66.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on_(1955_film)">Napoléon '
                                          '(1955 film)</a>A 1955 French '
                                          'historical epic film directed by '
                                          'Sacha Guitry that depicts major '
                                          'events in the life...',
                                'Text': 'Napoléon (1955 film) A 1955 French '
                                        'historical epic film directed by '
                                        'Sacha Guitry that depicts major '
                                        'events in the life...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(1995_film)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(1995_film)">Napoleon '
                                          '(1995 film)</a>A 1995 Australian '
                                          'family film directed by Mario '
                                          'Andreacchio, and written by Michael '
                                          'Bourchier...',
                                'Text': 'Napoleon (1995 film) A 1995 '
                                        'Australian family film directed by '
                                        'Mario Andreacchio, and written by '
                                        'Michael Bourchier...'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(2007_film)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(2007_film)">Napoleon '
                                          '(2007 film)</a>A 2007 United '
                                          'Kingdom television film first '
                                          'broadcast on BBC One on 12 November '
                                          '2007.',
                                'Text': 'Napoleon (2007 film) A 2007 United '
                                        'Kingdom television film first '
                                        'broadcast on BBC One on 12 November '
                                        '2007.'},
                               {'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on_(miniseries)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on_(miniseries)">Napoléon '
                                          '(miniseries)</a>A historical '
                                          'miniseries which explored the life '
                                          'of Napoleon Bonaparte.',
                                'Text': 'Napoléon (miniseries) A historical '
                                        'miniseries which explored the life of '
                                        'Napoleon Bonaparte.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_(musical)',
                                'Icon': {'Height': 16,
                                         'URL': 'https://duckduckgo.com/i/napoleonsoundtrack.com.ico',
                                         'Width': 16},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_(musical)">Napoleon '
                                          '(musical)</a> A musical by Timothy '
                                          'Williams and Andrew Sabiston.',
                                'Text': 'Napoleon (musical) A musical by '
                                        'Timothy Williams and Andrew '
                                        'Sabiston.'}]},
                   {'Name': 'Ships',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on_(ship)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on_(ship)">Napoléon '
                                          '(ship)</a>A 90-gun ship of the line '
                                          'of the French Navy, and the first '
                                          'purpose-built steam battleship in '
                                          'the...',
                                'Text': 'Napoléon (ship) A 90-gun ship of the '
                                        'line of the French Navy, and the '
                                        'first purpose-built steam battleship '
                                        'in the...'},
                               {'FirstURL': 'https://duckduckgo.com/Corse_(ship)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Corse_(ship)">Corse '
                                          '(ship)</a> A sail and steam '
                                          'experimental schooner, initially '
                                          'commissioned as a mail steamer.',
                                'Text': 'Corse (ship) A sail and steam '
                                        'experimental schooner, initially '
                                        'commissioned as a mail steamer.'},
                               {'FirstURL': 'https://duckduckgo.com/MV_Napoleon',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/MV_Napoleon">MV '
                                          'Napoleon</a> A British ship.',
                                'Text': 'MV Napoleon A British ship.'}]},
                   {'Name': 'Other uses',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Napol%C3%A9on_(coin)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napol%C3%A9on_(coin)">Napoléon '
                                          '(coin)</a>The colloquial term for a '
                                          'former French gold coin.',
                                'Text': 'Napoléon (coin) The colloquial term '
                                        'for a former French gold coin.'},
                               {'FirstURL': 'https://duckduckgo.com/Mille-feuille',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/cf7f194d.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Mille-feuille">Napoleon '
                                          '(pastry)</a>A French pastry whose '
                                          'exact origin is unknown.',
                                'Text': 'Napoleon (pastry) A French pastry '
                                        'whose exact origin is unknown.'},
                               {'FirstURL': 'https://duckduckgo.com/Canon_obusier_de_12',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/181a7fe0.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Canon_obusier_de_12">12-pounder '
                                          'Napoleon</a>A type of canon-obusier '
                                          'developed by France in 1853.',
                                'Text': '12-pounder Napoleon A type of '
                                        'canon-obusier developed by France in '
                                        '1853.'},
                               {'FirstURL': 'https://duckduckgo.com/Humphead_wrasse',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/8c2e2267.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Humphead_wrasse">Humphead '
                                          'wrasse</a>A species of wrasse '
                                          'mainly found on coral reefs in the '
                                          'Indo-Pacific region.',
                                'Text': 'Humphead wrasse A species of wrasse '
                                        'mainly found on coral reefs in the '
                                        'Indo-Pacific region.'}]},
                   {'Name': 'See also',
                    'Topics': [{'FirstURL': 'https://duckduckgo.com/Age_of_Napoleon_(board_game)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Age_of_Napoleon_(board_game)">Age '
                                          'of Napoleon (board game)</a>A 2003 '
                                          'war and strategy board game created '
                                          'in collaboration between Mayfair '
                                          'Games and Phalanx Games.',
                                'Text': 'Age of Napoleon (board game) A 2003 '
                                        'war and strategy board game created '
                                        'in collaboration between Mayfair '
                                        'Games and Phalanx Games.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_and_Uncle_Elby',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/0b3ffa48.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_and_Uncle_Elby">Napoleon '
                                          'and Uncle Elby</a>A popular '
                                          'syndicated newspaper comic strip '
                                          'created by Clifford McBride.',
                                'Text': 'Napoleon and Uncle Elby A popular '
                                        'syndicated newspaper comic strip '
                                        'created by Clifford McBride.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_Bunny-Part',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_Bunny-Part">Napoleon '
                                          'Bunny-Part</a> A Warner Bros. '
                                          'animated cartoon of the Merrie '
                                          'Melodies series, directed by Friz '
                                          'Freleng.',
                                'Text': 'Napoleon Bunny-Part A Warner Bros. '
                                        'animated cartoon of the Merrie '
                                        'Melodies series, directed by Friz '
                                        'Freleng.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_complex',
                                'Icon': {'Height': '',
                                         'URL': 'https://duckduckgo.com/i/5b8b23be.jpg',
                                         'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_complex">Napoleon '
                                          'complex</a>A theorised condition '
                                          'occurring in people of short '
                                          'stature.',
                                'Text': 'Napoleon complex A theorised '
                                        'condition occurring in people of '
                                        'short stature.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleon_XIV',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleon_XIV">Napoleon '
                                          'XIV</a>An American singer, '
                                          'songwriter and record producer.',
                                'Text': 'Napoleon XIV An American singer, '
                                        'songwriter and record producer.'},
                               {'FirstURL': 'https://duckduckgo.com/Napoleonite',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/Napoleonite">Napoleonite</a> '
                                          'A variety of diorite.',
                                'Text': 'Napoleonite A variety of diorite.'},
                               {'FirstURL': 'https://duckduckgo.com/d/Napoleon_(given_name)',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/d/Napoleon_(given_name)">Napoleon '
                                          '(given name) Meanings</a>  A given '
                                          'name (and list of people with the '
                                          'name).',
                                'Text': 'Napoleon (given name) Meanings A '
                                        'given name (and list of people with '
                                        'the name).'},
                               {'FirstURL': 'https://duckduckgo.com/d/Napoleon_Bonaparte',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/d/Napoleon_Bonaparte">Napoleon '
                                          'Bonaparte Meanings</a>  See related '
                                          "meanings for the phrase 'Napoleon "
                                          "Bonaparte'.",
                                'Text': 'Napoleon Bonaparte Meanings See '
                                        'related meanings for the phrase '
                                        "'Napoleon Bonaparte'."},
                               {'FirstURL': 'https://duckduckgo.com/d/Prince_Napol%C3%A9on',
                                'Icon': {'Height': '', 'URL': '', 'Width': ''},
                                'Result': '<a '
                                          'href="https://duckduckgo.com/d/Prince_Napol%C3%A9on">Prince '
                                          'Napoléon Meanings</a>  See related '
                                          "meanings for the phrase 'Prince "
                                          "Napoléon'.",
                                'Text': 'Prince Napoléon Meanings See related '
                                        "meanings for the phrase 'Prince "
                                        "Napoléon'."}]}],
 'Results': [],
 'Type': 'D',
 'meta': {'attribution': None,
          'blockgroup': None,
          'created_date': None,
          'description': 'Wikipedia',
          'designer': None,
          'dev_date': None,
          'dev_milestone': 'live',
          'developer': [{'name': 'DDG Team',
                         'type': 'ddg',
                         'url': 'http://www.duckduckhack.com'}],
          'example_query': 'nikola tesla',
          'id': 'wikipedia_fathead',
          'is_stackexchange': None,
          'js_callback_name': 'wikipedia',
          'live_date': None,
          'maintainer': {'github': 'duckduckgo'},
          'name': 'Wikipedia',
          'perl_module': 'DDG::Fathead::Wikipedia',
          'producer': None,
          'production_state': 'online',
          'repo': 'fathead',
          'signal_from': 'wikipedia_fathead',
          'src_domain': 'en.wikipedia.org',
          'src_id': 1,
          'src_name': 'Wikipedia',
          'src_options': {'directory': '',
                          'is_fanon': 0,
                          'is_mediawiki': 1,
                          'is_wikipedia': 1,
                          'language': 'en',
                          'min_abstract_length': '20',
                          'skip_abstract': 0,
                          'skip_abstract_paren': 0,
                          'skip_end': '0',
                          'skip_icon': 0,
                          'skip_image_name': 0,
                          'skip_qr': '',
                          'source_skip': '',
                          'src_info': ''},
          'src_url': None,
          'status': 'live',
          'tab': 'About',
          'topic': ['productivity'],
          'unsafe': 0}}

better = {'Abstract': 'Old Navy is an American clothing and accessories retailing '
             'company owned by American multinational corporation Gap Inc. It '
             'has corporate operations in the Mission Bay neighborhood of San '
             'Francisco. The largest of the Old Navy stores are its flagship '
             'stores, located in New York City, Seattle, Chicago, San '
             'Francisco, and Mexico City.',
 'AbstractSource': 'Wikipedia',
 'AbstractText': 'Old Navy is an American clothing and accessories retailing '
                 'company owned by American multinational corporation Gap Inc. '
                 'It has corporate operations in the Mission Bay neighborhood '
                 'of San Francisco. The largest of the Old Navy stores are its '
                 'flagship stores, located in New York City, Seattle, Chicago, '
                 'San Francisco, and Mexico City.',
 'AbstractURL': 'https://en.wikipedia.org/wiki/Old_Navy',
 'Answer': '',
 'AnswerType': '',
 'Definition': '',
 'DefinitionSource': '',
 'DefinitionURL': '',
 'Entity': 'company',
 'Heading': 'Old Navy',
 'Image': 'https://duckduckgo.com/i/75ba196b.png',
 'ImageHeight': 200,
 'ImageIsLogo': 1,
 'ImageWidth': 550,
 'Infobox': {'content': [{'data_type': 'string',
                          'label': 'Type',
                          'sort_order': '1000',
                          'value': 'Division',
                          'wiki_order': 0},
                         {'data_type': 'string',
                          'label': 'Industry',
                          'sort_order': '1001',
                          'value': 'Retail',
                          'wiki_order': 1},
                         {'data_type': 'string',
                          'label': 'Founded',
                          'sort_order': '1',
                          'value': '11, 1994',
                          'wiki_order': 2},
                         {'data_type': 'string',
                          'label': 'Number of locations',
                          'sort_order': '2',
                          'value': '1,106',
                          'wiki_order': 3},
                         {'data_type': 'string',
                          'label': 'Key people',
                          'sort_order': '2',
                          'value': 'Sonia Syngal (CEO and Global President)',
                          'wiki_order': 4},
                         {'data_type': 'string',
                          'label': 'Products',
                          'sort_order': '1002',
                          'value': 'Clothing',
                          'wiki_order': 5},
                         {'data_type': 'string',
                          'label': 'Parent',
                          'sort_order': '3',
                          'value': 'Gap Inc. (1994–present)',
                          'wiki_order': 6},
                         {'data_type': 'string',
                          'label': 'Website',
                          'sort_order': '1003',
                          'value': 'OldNavy.com',
                          'wiki_order': 7},
                         {'data_type': 'instance',
                          'label': 'Instance of',
                          'value': {'entity-type': 'item',
                                    'id': 'Q4830453',
                                    'numeric-id': 4830453},
                          'wiki_order': '207'}],
             'meta': [{'data_type': 'string',
                       'label': 'article_title',
                       'value': 'Old Navy'},
                      {'data_type': 'string',
                       'label': 'template_name',
                       'value': 'infobox company'},
                      {'data_type': 'string',
                       'label': 'formatting_rules',
                       'value': 'company'}]},
 'Redirect': '',
 'RelatedTopics': [{'FirstURL': 'https://duckduckgo.com/c/Gap_brands',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Gap_brands">Gap '
                              'brands</a>',
                    'Text': 'Gap brands'},
                   {'FirstURL': 'https://duckduckgo.com/c/Online_clothing_retailers',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Online_clothing_retailers">Online '
                              'clothing retailers</a>',
                    'Text': 'Online clothing retailers'},
                   {'FirstURL': 'https://duckduckgo.com/c/Underwear_brands',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Underwear_brands">Underwear '
                              'brands</a>',
                    'Text': 'Underwear brands'},
                   {'FirstURL': 'https://duckduckgo.com/c/Retail_companies_based_in_California',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Retail_companies_based_in_California">Retail '
                              'companies based in California</a>',
                    'Text': 'Retail companies based in California'},
                   {'FirstURL': 'https://duckduckgo.com/c/Fashion_accessory_brands',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Fashion_accessory_brands">Fashion '
                              'accessory brands</a>',
                    'Text': 'Fashion accessory brands'},
                   {'FirstURL': 'https://duckduckgo.com/c/Clothing_retailers_of_the_United_States',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Clothing_retailers_of_the_United_States">Clothing '
                              'retailers of the United States</a>',
                    'Text': 'Clothing retailers of the United States'},
                   {'FirstURL': 'https://duckduckgo.com/c/Clothing_brands_of_the_United_States',
                    'Icon': {'Height': '', 'URL': '', 'Width': ''},
                    'Result': '<a '
                              'href="https://duckduckgo.com/c/Clothing_brands_of_the_United_States">Clothing '
                              'brands of the United States</a>',
                    'Text': 'Clothing brands of the United States'}],
 'Results': [],
 'Type': 'A',
 'meta': {'attribution': None,
          'blockgroup': None,
          'created_date': None,
          'description': 'Wikipedia',
          'designer': None,
          'dev_date': None,
          'dev_milestone': 'live',
          'developer': [{'name': 'DDG Team',
                         'type': 'ddg',
                         'url': 'http://www.duckduckhack.com'}],
          'example_query': 'nikola tesla',
          'id': 'wikipedia_fathead',
          'is_stackexchange': None,
          'js_callback_name': 'wikipedia',
          'live_date': None,
          'maintainer': {'github': 'duckduckgo'},
          'name': 'Wikipedia',
          'perl_module': 'DDG::Fathead::Wikipedia',
          'producer': None,
          'production_state': 'online',
          'repo': 'fathead',
          'signal_from': 'wikipedia_fathead',
          'src_domain': 'en.wikipedia.org',
          'src_id': 1,
          'src_name': 'Wikipedia',
          'src_options': {'directory': '',
                          'is_fanon': 0,
                          'is_mediawiki': 1,
                          'is_wikipedia': 1,
                          'language': 'en',
                          'min_abstract_length': '20',
                          'skip_abstract': 0,
                          'skip_abstract_paren': 0,
                          'skip_end': '0',
                          'skip_icon': 0,
                          'skip_image_name': 0,
                          'skip_qr': '',
                          'source_skip': '',
                          'src_info': ''},
          'src_url': None,
          'status': 'live',
          'tab': 'About',
          'topic': ['productivity'],
          'unsafe': 0}}
