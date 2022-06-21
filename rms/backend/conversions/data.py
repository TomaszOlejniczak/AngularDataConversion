COLUMN_CONVERSIONS = {
    'CITY': ["City/Town", "CITY", "City", "*City"],
    'YEARUPGRAD': ['Year Upgraded', 'Year Renovated', 'Yr Bldg updated (Mand if >25 yrs)'],
    'ROOFSYS': ['Roofing Material ', 'Roof Covering', '**Type of Roof Covering', 'Roof Cover', 'ROOFSYS'],
    'ROOFAGE': ['ROOFAGE', 'Roof Age', "Yr. Roof Updated", "Yr. Roof \nUpdated", "Age Of Roof"],
    'NUMSTORIES': ['Number of Stories', '# Stories', '# of Stories', 'Stories',
                   '# Of Stories', '*# of Stories', 'Num of Stories', 'Num Stories',
                   'No. ofStories'],
    'NUMBLDGS': ["Number of Buildings", "# of Buildings", "*# of Bldgs", 'Num Buildings', '# Bldgs',
                 'numbldgs', 'No. ofBldgs'],
    'FRFIREALARM': ['Fire Alarm'],
    'BLDGSCHEME': ['Construction Scheme', 'BLDGSCHEME'],
    'BLDGCLASS': ["BLDGCLASS", "Construction Description", "Construction Type", "ISO Fire Const Code",
                  "ISO Construction ", "Class", "Construction", "Construction Type",
                  "Construction Class(Schemes - "
                  "RMS, "
                  "ISO FIRE "
                  "or "
                  "INDUSTRIAL FACILITY, Choose one scheme only).  Click on cell Q9 and the other subsequent cells, "
                  "select from the drop-down list by clicking on the arrow to the right of the cell.See Construction Class tab for detailed explanations.",
                  "*ISO Const",
                  "Construction Class", 'Constr Class', 'ConstructionClass'
                  ],
    'LOCNAME': ["COMPANY", "Name", "Location name", "Building Name",
                             "Description", "Property Name", "Name / Code", "Locationm Name",
                             "Location Name", "Airport Name", "Location", 'LOCNAME'],
    'LOCNUM': ["Location #", "Loc. #", "Structure #", "Locnum", "Location Number", "Location Numbe",
               "* Bldg No.", "Location #", "Building Number", "Building #"],
    'FRSPRINKLERSYS': ["Sprinklered", "Sprinkler Prot", "Fire Sprinklers (yes/no)",
                             "Sprinkler %", "Percent Sprinklered", 'Sprinklers', 'Automatic Sprrinklers'],
    'YEARBUILT': ["Year Built", "*Orig Year Built", 'YearBuilt', 'Year'],
    'EQSLSUSCEPTIBILITY': ['EQSL Susceptibility'],
    'TANK': ['Tank'],
    'POUNDING': ['Pounding'],
    'FRAMEBOLT': ['Frame Bolted to Foundation', 'Frame Bolted'],
    'ORNAMENT': ['External Ornamentation', 'Ornamentation'],
    'URMCHIMNEY': ['URM Chimney/Partition'],
    'SHORTCOL': ['Short Column'],
    'BLDGEXT': ['Building Exterior'],
    'SHAPECONF': ['Shape Configuration'],
    'TORSION': ['Torsion'],
    'REDUND': ['Redundancy'],
    'ROOFMAINT': ['Roof Maintenance', 'Building Maintenance'],
    'VULNWIND': ['Contents Vulnerability Due To Wind'],
    'VULNFLOOD': ['Contents Vulnerability Due To Water'],
    'RESISTDOOR': ['Resistance - Doors'],
    'ROOFGEOM': ['Roof Geometry', '**Shape of roof', 'RoofGeom', 'Roof Geom', 'Roof Shape'],
    'FLZONE': ['Flood Zone', 'Flood Zone (if Flood reqst"d)', 'FLZONE'],
    'RESISTOPEN': ['Opening Protection', 'RESISTOPEN', 'Wind Resistance-Windows'],
    'CLADDING': ['**Exterior Cladding', 'Cladding Type', 'Claddingzjadlem'],
    'FLOORAREA': ["Total Square Footage", "SQ Ft", "GLA", "Sq Ft", "Square Footage",
                  "*Square Footage", "SQ m", "Floor Area", "Square Feet", "Building SQ FT"],
    'LONGITUDE': ['LONGINTUDE', 'Lon', 'Long', 'lngtude', 'lng'],
    'LATITUDE': ['LAtituDe', 'lat', 'latt'],
    'CNTRYCODE': ['Country Code', 'COUNTRY', 'Country'],
    'POSTALCODE': ['ZIP', 'ZIP Code', 'Postal Code', 'Postcode'],
    'STATECODE': ["St", "State", "State code", "*State Code"],
    'COUNTY': ['County', 'Cnty'],
    'SLOPE': ['SLOPE'],
    'ENGFOUND': ['Engineered Foundations', 'Engineered Foundation'],
    'OCCSCHEME': ['Occupancy Scheme', 'OCCSCHEME'],
    'OCCTYPE': ['Occupancy', 'Occupancy Type', 'Occtype', 'Occupancy Des.'],
    'STREETNAME': ['Street Address', 'Address', 'Street', 'Building Address', "Location Address"],
    'ARCHITECT': ['Residential Appurtenant Structures', 'Architectural Elements'],
    'ROOFFRAME': ['Roof Framing Type', 'Roof Frame', 'Roof Framing'],
    'BASEISOL': ['Base Isolation', 'BASEISOL'],
    'SPNKLRTYPE': ['Sprinkler Type'],
    'URMPROV': ['URM Retrofit'],
    'TILTUPRET': ['Tilt-Up Retrofit'],
    'WALLSBRACD': ['Cripple Walls'],
    'DURESS': ['Equipment Support Maintenance', 'Fatigue/Maintenance', 'Fatigue / Maintenance'],
    'STRUCTUP': ['Structural Upgrade'],
    'OVERPROF': ['Vertical Irregularity', 'Setbacks and Overhangs'],
    'STORYPROF': ['soft story'],
    'ROOFPARAPT': ['Roof parapets', 'Parapets'],
    'ROOFEQUIP': ['Roof Equipment Hurricane Bracing', 'Mech./Elec. Equipment - Roof'],
    'MECHSIDE': ['Mechanical/Electrical Equipment (Side of Building)',
                 'Mech./Elec. Equipment - Side of Building',
                 'Mech/Elec Equipment - Side of Building'],
    'MECHGROUND': ['Ground Level Equipment', 'Mech/Elec Equip–Ground Level', 'Mech./Elec. Equip–Ground Level'],
    'CLADRATE': ['Roof Sheathing Attachment', 'Cladding Rating'],
    'EXTORN': ['External Ornamentation', 'Commercial Appurtenant Structures'],
    'FOUNDSYS': ['Foundation System', 'Frame-Foundation Connection'],
    'FLASHING': ['Flashing'],
    'BASEMENT': ['Basement'],
    'ROOFANCH': ['Roof Anchor'],
    'CONSTQUALI': ['Construction quality'],
    'REDUNDANCY': ['BI Redundancy', 'Business Interruption Redundancy'],
    'PREPAREDNESS': ['BI Preparedness', 'Business Interruption Preparedness'],
    'CV1VAL': ['Building Value', 'Real Property', "CV1VAL"],
    'CV2VAL': ['Personal Property', 'Business Personal Property', 'Contents', "CV2VAL"],
    'CV3VAL': ['Rents', 'BI', 'BI/EE', "PREVIOUS YEAR GROSS RENTS (B)", "CV3VAL", "12 Months Rents / Business Income",
               "Business Income"],
    'CNTRYSCHEME': ['Country scheme', 'CNTRYSCHEME'],
    'IFMSTRUCTCONDITION': ['IFMSTRUCTCONDITION'],
    'IFMEQUIPBRACING': ['IFMEQUIPBRACING'],
    'IFMMISSILEEXP': ['IFMMISSILEEXP'],
    'IFMVERTICALEXPDIST': ['IFMVERTICALEXPDIST'],
    'EQSLINS': ['EQSLINS']
}

VALUES_CONVERSIONS = {
    'ROOFSYS': {'': '0',
                   '1-Concrete Fill': '1',
                   'Metal/Composition': '1',
                   'Built up': '3',
                   'wood framed steel': '6',
                   'Rubber': '8',
                   'Steel/Sheet Metal': '1',
                   'Steel/Flat Roof': '1',
                   'Canvas': '3',
                   '(5) metal; (2) flat modified membrane w/aggregate ': '1',
                   'built up steel': '3',
                   'Wood Frame/Asphalt Shingles': '6',
                   'TPO': '',
                   'Built-up': '3',
                   'Membrane': '3',
                   'Metal/Comp': '1',
                   'Steel / Composition': '1',
                   'Frame': '6',
                   ' Metal Canopy Roof': '1',
                   'Non-Combustible': '1',
                   'Built Up': '3',
                   'Frame w/Rubber Membrane': '8',
                   'Steel': '2',
                   'Tin': '3',
                   'Steel Roof': '2',
                   'Flat, modified membrane': '4',
                   'Sealed Flat': '2',
                   'Modified Fire Resistive': '2',
                   ' ': '0',
                   'Metal': '1',
                   'Flat Roof / Tar Paper': '0',
                   'Composite': '0',
                   'Metal Sheeting': '2',
                   'Metal/rubber membrane': '10',
                   'Build-up': '3',
                   'Steel ': '2',
                   'Metal / Flat rubber': '1',
                   'metal': '1',
                   'Metal ': '1',
                   'rolled asphalt': '5',
                   'Metal Panels': '1',
                   'Flat rubber': '0',
                   'Build up': '3',
                   'Composition Roof': '0',
                   'Sheet Metal': '1',
                   'Metal (airport responsible)': '2',
                   'COMPOSITION': '0',
                   'Composition': '0',
                },

    'FRFIREALARM': {'': 0, 'Yes': 1, 'No': 2, 'y': 1, 'n': 2, 'unknown': 0, '?': 0},
    'ENGFOUND': {'': 0, 'Yes': 1, 'No': 2, 'y': 1, 'n': 2, 'unknown': 0, '?': 0, 'NaN': 0},
    'BLDGCLASS': {"Wood Frame- ISO FIRE Type V-A": "1",
                            "Masonry Non Combustible- ISO FIRE 4": "2",
                            "Masonry Non Combustile- ISO FIRE 4": "2",
                            "Masonry Non-Combustile- ISO FIRE 4": "2",
                            "ISO-2": "2",
                            "ISO-2 ": "2",
                            "Wood Frame- ISO FIRE": "1",
                            "Masonry Non-Combustile- ISO FIRE": "2",
                            "na": "0",
                            "Masonry Non-Combustile- ISO FIRE 4 & Fire Resistive - ISO FIRE 6": "3",
                            "Masonry Superior Non-Combustible- ISO FIRE": "2",
                            "FIRE RESISTIVE": "3",
                            "FRAME": "1",
                            "MASONRY-NON COMBUS": "2",
                            "NON-COMBUSTIBLE": "4A",
                            "MOD FIRE RESISTIVE": "4A",
                            "JOISTED MASONRY": "2",
                            '': '0',
                            'Wood Frame': '1',
                            '(Brick/Stucco Veneer)': '2',
                            'Joisted Masonry': '2',
                            'Joisted Mas': '2',
                            'Masonry Non-Combustible': '2',
                            'Wood Frame & Post Tension Concrete': '1A2',
                            'All Metal': '4A',
                            'Masonry NC': '2',
                            '(Brick Veneer)': '2',
                            'Fire Resistive': '3',
                            'JM': '2',
                            'Frame': '1',
                            'Masonry Non Combustible': '2',
                            'MNC': '2',
                            'Non Combustible': '4A',
                            'NC': '4A',
                            'FR': '3',
                            'Modified Fire Resistive': '4A',
                            'MFR': '4A',
                            'SFR': '4A',
                            'Stone/Wood Frame': '2',
                            'N/A': '0',
                            'Steel/Concrete': '3A6',
                            'Masonry & Frame': '2',
                            'Masonry Brick': '2',
                            'Metal': '4B',
                            '0': '0',
                            '4B': '4B',
                            # '2': '2',
                            # '3': '3',
                            'Concrete, Masonry, Steel': '2',
                            'Combustible': '1',
                            'Steel, Concrete': '3A6',
                            'Steel / NC': '4A',
                            'Concrete/ Steel': '3A6',
                            'Frame/Siding': '1',
                            'Wood frame with stucco': '1',
                            'Non - Combustible': '4A',
                            'Concrete/Dirt': '3',
                            'SteelFabric': '4A',
                            'Cement/Asphalt': '50D',
                            'Pre-enginered Steel': '4A1',
                            'Concrete/Metal': '3A6',
                            "40' Office Trailer": '0',
                            'WOOD': '1',
                            'Brick /  Masonry': '2B',
                            'Asphalt': '50D',
                            'Concrete': '3',
                            'Office- Frame  Hangar - Non Combust': '4B1',
                            'Brick / Steel': '4A3',
                            'Concrete, Metal': '3A6',
                            'Steel w metal clading': '4',
                            '2010': '0',
                            'Block/Masonry Steel': '4A3',
                            'Masonry/Non-Combustible': '2',
                            'concrete/steel': '3A6',
                            'Steel Butler Bldg.': '4',
                            'Joisted masonry': '2',
                            'Pre-engineered Metal': '4A1',
                            'Steel Building': '4',
                            '2017': '0',
                            'Modified fire resistive': '4A',
                            'Metal with Metal Framing': '4A2',
                            'Sheet Metal/Steel Frame': '4B',
                            'Built Up/Steel': '4',
                            'Metal/Concrete': '4A',
                            'Concrete and Steel': '4A',
                            'Non-Combustible hangar Fire Resistive office': '2',
                            'METAL': '4B',
                            'Concrete/Steel': '3A6',
                            'Sheet Metal/Steel': '4B',
                            'Non combustible': '4A',
                            'Steel w/CMU wall facade': '4C',
                            'wood/metal': '4B2',
                            'concrete/Steel': '3A6',
                            'Non-Combustible hangar Masonary office': '2',
                            'Fire-Resistant': '3',
                            'Non-combustible': '2',
                            'Steel/Brick': '4A6',
                            'Concrete Block': '3',
                            'Steel Structure, Metal Siding': '4B1',
                            'Brick': '2',
                            'Steel/Stucco': '4C',
                            'Metal/Masonry': '4A6',
                            ' ': '0',
                            'Masonry': '2',
                            'Steel/Fabric': '4A',
                            'Concrete/curtain-wall': '3',
                            'Concrete, Steel': '3A6',
                            'Metal frame and siding': '4B1',
                            'Masonry / Steel': '4A',
                            'Class S Steel': '4',
                            'Jointed Masonry': '2',
                            'STI-P3': '16',  # cathodically protected double or single wall
                            # underground liquid storage steel tank
                            'II-B': '4B',
                            'Fiberglass': '0',
                            'Concrete/Aluminum': '3A6',
                            'Concrete tilt-up': '3B4',
                            'Office-Frame  Hangar-Non Combust': '4B',
                            'Masonry/Non comb': '2',
                            'Concrete & Steel': '3A6',
                            'V-B': '1',
                            'Modified fire': '4A',
                            'Non-Combustible': '2',
                            'Concrete Steel': '3A6',
                            'Masonry ': '2',
                            'Steel': '4A',
                            'Office - Frame  Hangar - Non Combust': '4B',
                            '2015': '0',
                            'Joisted Masonary': '2',
                            'Concrete/Steel/Glass': '3A6',
                            'Concrete/Asphalt': '3',
                            'Non Combustable': '2',
                            'Cement': '50D',
                            '3A-Cast-in-Place Reinforced Concrete with Concrete Roof Deck': '3A'
                  },
    'FRSPRINKLERSYS': {'': 0,
                       '?': 0,
                       'NaN': 0,
                       'na': 0,
                        'NONSPRINKLERED': 2,
                        'SPRINKLERED': 1,
                        'PARTIAL SPRINKLE': 1,
                        'NON-SPRINKLERED': 2,
                        'Y': 1,
                        'N': 2,
                        'Yes': 1,
                        'No 0': 2,
                        'No': 2},

    'STATECODE': {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nan': '',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
},
    'OCCTYPE': {'': '0',
                   'na': '0',
                   'Section 8 Apartments/Tax Credit': '8800',
                   'Section 8 High Rise Senior Independent Apartments': '8800',
                   'Tax Credit, PBRA & Market Value Apt Housing & Community Center, business '
                   'center, clubhouse': '8611',
                   'Market Value High Rise Apartments Going Condo.  Structure covered by HOA '
                   'policy.  143 total units; 4 unsold units. & Parking Garage': '8800',
                   'Tax Credit & Section 8 Low-Rise Garden Apartments': '8800',
                   'Gifted to Non-Profit': '8641',
                   'Office for Utility': '7300',
                   'CVS Pharmacy Retail Store & Family Dollar Retail Store': '5912',
                   'Oreilly Auto Parts Retail Store & Subway Restaurant': '5531',
                   'Tax Credit & Section 8 Garden Apartments': '8800',
                   'Book Store': '5192',
                   'Market Value Apartments Going Condo.  Structure covered by HOA policy.  56 '
                   'total units; 3 unsold units.': '8800',
                   'Market Value Apartments & Parking Deck': '8800',
                   'Warehouse': '1541',
                   'Mini Storage Warehouses (308 units)': '1541',
                   'Market Value apartments & Retail Space & Parking Deck': '8800',
                   'Local Community Development Corporation': '8641',
                   'Office (Tenant:  Aphiliates)': '7300',
                   'Office, Warehouse & Test Kitchen': '1541',
                   'Tax Credit, Market Rate, PBRA and RAD': '9300',
                   "Conventional Apartment Housing, Retail & Restaurant Space [Wendy's, Chan Lee's "
                   "Chinese, Subway Sandwich, Out Takes Sandwich Shop, US Army Recruiting Station "
                   "& Vacant] located below Midtown Commons": '8800',
                   'Market Value Apartments.': '8800',
                   'Restaurant & Banquet Hall': '5800',
                   'Conventional Townhomes': '8800',
                   'Town House': '8800',
                   'Market Value Apartments': '8800',
                   'Section 8 Apartments': '8800',
                   'Market Value Apartments, 1 underground parking deck and one stand alone '
                   'parking deck.   Note:  garage sq. ft. and garage cost carried in total.': '8800',
                   'Condominiums with 6 units of retail space.  Condo HOA insures '
                   'structure/building.': '8800',
                   'Shopping Center': '5900',
                   'Office': '7300',
                   'Section 8 Garden Apartments': '8800',
                   'Hotel & Spa': '7021',
                   'UNKNOWN': '',
                   'PERMANENT DWELLING (SINGLE-FAMILY HOUSING)': '8800',
                   'PERMANENT DWELLING (MULTI-FAMILY HOUSING)': '8800',
                   'TEMPORARY LODGING': '',
                   'GROUP INSTITUTIONAL HOUSING': '9531',
                   'RETAIL TRADE': '5900',
                   'WHOLESALE TRADE': '5000',
                   'PERSONAL AND REPAIR SERVICES': '7200',
                   'PROFESSIONAL, TECHNICAL, AND BUSINESS SERVICES': '7300',
                   'HEALTH CARE SERVICE': '8000',
                   'ENTERTAINMENT AND RECREATION': '7900',
                   'PARKING': '7521',
                   'HEAVY FABRICATION AND ASSEMBLY': '3531',
                   'LIGHT FABRICATION AND ASSEMBLY': '3800',
                   'FOOD AND DRUGS PROCESSING': '2000',
                   'CHEMICALS PROCESSING': '2800',
                   'METAL AND MINERALS PROCESSING': '3300',
                   'HIGH TECHNOLOGY': '3599',
                   'CONSTRUCTION': '1500',
                   'PETROLEUM': '2900',
                   'AGRICULTURE': '100',
                   'MINING': '1000',
                   'RELIGION AND NONPROFIT': '6732',
                   'GENERAL SERVICES': '9100',
                   'EMERGENCY RESPONSE SERVICES': '9200',
                   'EDUCATION': '8200',
                   'HIGHWAY': '4100',
                   'RAILROAD': '4000',
                   'AIR': '4500',
                   'SEA/WATER': '4400',
                   'ELECTRICAL': '4911',
                   'WATER': '4941',
                   'SANITARY SEWER': '4952',
                   'NATURAL GAS': '4923',
                   'TELEPHONE & TELEGRAPH': '4813',
                   'COMMUNICATION (RADIO AND TV)': '4833',
                   'FLOOD CONTROL': '4900',
                   'GENERAL COMMERCIAL': '9900',
                   'GENERAL INDUSTRIAL': '3569',
                   'MISCELLANEOUS': '9999',
                   'MORTGAGE-BACKED DWELLING (PUERTO RICO ONLY)': '8800',
                   'GENERAL RESIDENTIAL': '8800',
                   'HOMEOWNER': '8800',
                   'MULTI-FAMILY DWELLING– HOMEOWNERS ASSOCIATION': '8800',
                   'MULTI - FAMILY DWELLING– CONDOMINIUM UNIT OWNER': '8800',
                   'GASOLINE SERVICE STATION': '5541',
                   'RESTAURANTS': '5800',
                   'CASINOS': '7993',
                   'ACUTE CARE SERVICES HOSPITAL': '8069',
                   'OSHPD ACUTE CARE SERVICES HOSPITALS (CALIFORNIA ONLY)': '8062',
                   'HOTELS-LARGE': '7011',
                   'HOTELS-SMALL AND MEDIUM': '7021',
                   'RENTAL -GENERAL COMMERCIAL': '6531',
                   'UNIVERSITIES AND COLLEGES': '8221',
                   'UNKNOWN 0': '0',
                   'PERMANENT DWELLING (SINGLE-FAMILY HOUSING) 1': '8800',
                   'PERMANENT DWELLING (MULTI-FAMILY HOUSING) 2': '8800',
                   'TEMPORARY LODGING 3': '7000',
                   'GROUP INSTITUTIONAL HOUSING 4': '9531',
                   'RETAIL TRADE 5': '5900',
                   'WHOLESALE TRADE 6': '5000',
                   'PERSONAL AND REPAIR SERVICES 7': '7200',
                   'PROFESSIONAL, TECHNICAL, AND BUSINESS SERVICES 8': '7300',
                   'HEALTH CARE SERVICE 9': '8000',
                   'ENTERTAINMENT AND RECREATION 10': '7900',
                   'PARKING 11': '7521',
                   'HEAVY FABRICATION AND ASSEMBLY 12': '3531',
                   'LIGHT FABRICATION AND ASSEMBLY 13': '3800',
                   'FOOD AND DRUGS PROCESSING 14': '2000',
                   'CHEMICALS PROCESSING 15': '2800',
                   'METAL AND MINERALS PROCESSING 16': '3300',
                   'HIGH TECHNOLOGY 17': '3599',
                   'CONSTRUCTION 18': '1500',
                   'PETROLEUM 19': '2900',
                   'AGRICULTURE 20': '100',
                   'MINING 21': '1000',
                   'RELIGION AND NONPROFIT 22': '6732',
                   'GENERAL SERVICES 23': '9100',
                   'EMERGENCY RESPONSE SERVICES 24': '9200',
                   'EDUCATION 25': '8200',
                   'HIGHWAY 26': '4100',
                   'RAILROAD 27': '4000',
                   'AIR 28': '4500',
                   'SEA/WATER 29': '4400',
                   'ELECTRICAL 30': '4911',
                   'WATER 31': '4941',
                   'SANITARY SEWER 32': '4952',
                   'NATURAL GAS 33': '4923',
                   'TELEPHONE & TELEGRAPH 34': '4813',
                   'COMMUNICATION (RADIO AND TV) 35': '4833',
                   'FLOOD CONTROL 36': '4900',
                   'GENERAL COMMERCIAL 37': '9900',
                   'GENERAL INDUSTRIAL 38': '3569',
                   'MISCELLANEOUS 39': '9999',
                   'MORTGAGE-BACKED DWELLING (PUERTO RICO ONLY) 40': '8800',
                   'GENERAL RESIDENTIAL 40': '8800',
                   'HOMEOWNER 41': '8800',
                   'MULTI-FAMILY DWELLING– HOMEOWNERS ASSOCIATION 42': '8800',
                   'MULTI - FAMILY DWELLING– CONDOMINIUM UNIT OWNER 43': '8800',
                   'GASOLINE SERVICE STATION 44': '5541',
                   'RESTAURANTS 47': '5800',
                   'CASINOS 48': '7993',
                   'ACUTE CARE SERVICES HOSPITAL 49': '8069',
                   'OSHPD ACUTE CARE SERVICES HOSPITALS (CALIFORNIA ONLY) 50': '8062',
                   'HOTELS-LARGE 51': '7011',
                   'HOTELS-SMALL AND MEDIUM 52': '7021',
                   'RENTAL -GENERAL COMMERCIAL 53': '6531',
                   'UNIVERSITIES AND COLLEGES 54': '8221',
                   'NA': '0',
                   'APARTMENT': '8800',
                   'WAREHOUSE - OTH': '1541',
                   'COMMUNITY CENTER': '9532',
                   'INN': '7021',
                   'ENTERTAINMNT & REC': '7900',
                   'SCHOOL ATHLETICS': '8299',
                   'BOWLING CENTER': '7933',
                   'GOLF': '7992',
                   'VETERINARY CLINIC': '741',
                   'HOTEL': '7000',
                   'CLUBHOUSE': '7997',
                   'FOOD SERVICES': '5800',
                   'PERS & REPAIR SVC': '7500',
                   'CINEMA': '7800',
                   'HEALTH CLUB': '8000',
                   'DWELLING': '8800',
                   'APARTMENTLOWRISE': '8800',
                   'FARM ANIMALS': '291',
                   'UKNOWN': '0',
                   'GYMNASIUM': '8211',
                   'MARINA': '4493',
                   'RESTAURANT': '5800',
                   'COMMUNITY BUILDING': '9532',
                   'UTILITY BLDG': '4939',
                   'LAUNDRY PLANT': '7219',
                   'DAY CARE CENTER': '8351',
                   'AUDITORIUM': '7900',
                   'LIBRARY': '5942',
                   'STORAGE': '4225',
                   'PARK': '7900',
                   'NATATORIUM': '7900',
                   'SERVICE - OTHER': '8900',
                   'CHURCH - SANC': '8661',
                   'AUTO REPAIR CENTER': '7500',
                   'MANUFACTURING, LIGHT': '3648',
                   'OFFICE - GENERAL': '7300',
                   'STORE OR SHOP': '5900',
                   'LEARNING CENTER': '8331',
                   'PARKING STRUCT': '7521',
                   'STADIUM': '7900',
                   'Church': '8661',
                   'Classroom': '8299',
                   'Permanent Dwelling (single-family housing)': '8800',
                   'Permanent Dwelling (multi-family housing)': '8800',
                   'Temporary Lodging': '7000',
                   'Group Institutional Housing': '9531',
                   'Retail Trade': '5900',
                   'Wholesale Trade': '5000',
                   'Personal and Repair Services': '7200',
                   'Professional, Technical, and Business Services': '7300',
                   'Health Care Service': '8000',
                   'Entertainment and Recreation': '7900',
                   'Parking': '7521',
                   'Heavy Fabrication and Assembly': '3531',
                   'Light Fabrication and Assembly': '3800',
                   'Food and Drugs Processing': '2000',
                   'Chemicals Processing': '2800',
                   'Metal and Minerals Processing': '3300',
                   'High Technology': '3599',
                   'Construction': '1500',
                   'Petroleum': '2900',
                   'Agriculture': '100',
                   'Mining': '1000',
                   'Religion and Nonprofit': '6732',
                   'General Services': '9100',
                   'Emergency Response Services': '9200',
                   'Education': '8200',
                   'Highway': '4100',
                   'Railroad': '4000',
                   'Air': '4500',
                   'Sea/Water': '4400',
                   'Electrical': '4911',
                   'Water': '4941',
                   'Sanitary Sewer': '4952',
                   'Natural Gas': '4923',
                   'Telephone & Telegraph': '4813',
                   'Communication (Radio and TV)': '4833',
                   'Flood Control': '4900',
                   'General Commercial': '9900',
                   'General Industrial': '3569',
                   'Miscellaneous': '9999',
                   'Mortgage-backed Dwelling (Puerto Rico only)': '8800',
                   'General Residential': '8800',
                   'Homeowner': '8800',
                   'Multi-Family Dwelling– Homeowners Association': '8800',
                   'Multi - Family Dwelling– Condominium Unit Owner': '8800',
                   'Gasoline Service Station': '5541',
                   'Restaurants': '5800',
                   'Casinos': '7993',
                   'Acute Care Services Hospital': '8069',
                   'OSHPD Acute Care Services Hospitals (California ONLY)': '8062',
                   'Hotels-Large': '7011',
                   'Hotels-Small and Medium': '7021',
                   'Rental -General Commercial': '6531',
                   'Universities and Colleges': '8221',
                   'Unknown 0': '0',
                   'Permanent Dwelling (single-family housing) 1': '8800',
                   'Permanent Dwelling (multi-family housing) 2': '8800',
                   'Temporary Lodging 3': '7000',
                   'Group Institutional Housing 4': '9531',
                   'Retail Trade 5': '5900',
                   'Wholesale Trade 6': '5000',
                   'Personal and Repair Services 7': '7200',
                   'Professional, Technical, and Business Services 8': '7300',
                   'Health Care Service 9': '8000',
                   'Entertainment and Recreation 10': '7900',
                   'Parking 11': '7521',
                   'Heavy Fabrication and Assembly 12': '3531',
                   'Light Fabrication and Assembly 13': '3800',
                   'Food and Drugs Processing 14': '2000',
                   'Chemicals Processing 15': '2800',
                   'Metal and Minerals Processing 16': '3300',
                   'High Technology 17': '3599',
                   'Construction 18': '1500',
                   'Petroleum 19': '2900',
                   'Agriculture 20': '100',
                   'Mining 21': '1000',
                   'Religion and Nonprofit 22': '6732',
                   'General Services 23': '9100',
                   'Emergency Response Services 24': '9200',
                   'Education 25': '8200',
                   'Highway 26': '4100',
                   'Railroad 27': '4000',
                   'Air 28': '4500',
                   'Sea/Water 29': '4400',
                   'Electrical 30': '4911',
                   'Water 31': '4941',
                   'Sanitary Sewer 32': '4952',
                   'Natural Gas 33': '4923',
                   'Telephone & Telegraph 34': '4813',
                   'Communication (Radio and TV) 35': '4833',
                   'Flood Control 36': '4900',
                   'General Commercial 37': '9900',
                   'General Industrial 38': '3569',
                   'Miscellaneous 39': '9999',
                   'Mortgage-backed Dwelling (Puerto Rico only) 40': '8800',
                   'General Residential 40': '8800',
                   'Homeowner 41': '8800',
                   'Multi-Family Dwelling– Homeowners Association 42': '8800',
                   'Multi - Family Dwelling– Condominium Unit Owner 43': '8800',
                   'Gasoline Service Station 44': '5541',
                   'Restaurants 47': '5800',
                   'Casinos 48': '7993',
                   'Acute Care Services Hospital 49': '8069',
                   'OSHPD Acute Care Services Hospitals (California ONLY) 50': '8062',
                   'Hotels-Large 51': '7011',
                   'Hotels-Small and Medium 52': '7021',
                   'Rental -General Commercial 53': '6531',
                   'Universities and Colleges 54': '8221',
                   'Productiong': '1541',
                   'SubtOfficetal:': '7300',
                   'Warehouse/Office': '4225',
                   'TOfficetal:': '7300',
                   'Production': '1541',
                   'Office, Warehouse': '4225',
                   'Office, R&Warehouse': '4225',
                   'R&Warehouse': '9803',
                   'Office I&B': '7300',
                   'Retail': '5900',
                   'Retail/Offices': '5900',
                   'Garage': '7500',
                   'Duplex': '8800'
                },
    'SPNKLRTYPE': {'Wet 100%': 1,
                   'Dry': 2,
                   'Wet': 1,
                   'Unknown': 0, 'na': 0, '': 0, 'NA': 0}
}
