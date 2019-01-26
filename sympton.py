import requests
import json
class Sympton(object):
  def getExactSympton(string):
    json=[

  {

    "ID": 188,

    "Name": "Abdominal guarding"

  },

  {

    "ID": 10,

    "Name": "Abdominal pain"

  },

  {

    "ID": 223,

    "Name": "Abdominal pain associated with menstruation"

  },

  {

    "ID": 984,

    "Name": "Absence of a pulse"

  },

  {

    "ID": 974,

    "Name": "Aggressiveness"

  },

  {

    "ID": 981,

    "Name": "Agitation"

  },

  {

    "ID": 996,

    "Name": "Ankle deformity"

  },

  {

    "ID": 147,

    "Name": "Ankle swelling"

  },

  {

    "ID": 238,

    "Name": "Anxiety"

  },

  {

    "ID": 1009,

    "Name": "Arm pain"

  },

  {

    "ID": 971,

    "Name": "Arm swelling"

  },

  {

    "ID": 998,

    "Name": "Back deformity"

  },

  {

    "ID": 104,

    "Name": "Back pain"

  },

  {

    "ID": 180,

    "Name": "Black stools"

  },

  {

    "ID": 57,

    "Name": "Blackening of vision"

  },

  {

    "ID": 24,

    "Name": "Blackhead"

  },

  {

    "ID": 284,

    "Name": "Bleeding from vagina"

  },

  {

    "ID": 176,

    "Name": "Bleeding in the conjunctiva of the eye"

  },

  {

    "ID": 48,

    "Name": "Bloated feeling in the stomach"

  },

  {

    "ID": 190,

    "Name": "Blood in stool"

  },

  {

    "ID": 233,

    "Name": "Bloody cough"

  },

  {

    "ID": 991,

    "Name": "Blue colored skin"

  },

  {

    "ID": 240,

    "Name": "Blue spot on skin"

  },

  {

    "ID": 77,

    "Name": "Blurred vision"

  },

  {

    "ID": 239,

    "Name": "Bold area among hair on the head"

  },

  {

    "ID": 156,

    "Name": "Bone fracture"

  },

  {

    "ID": 250,

    "Name": "Breathing-related pains"

  },

  {

    "ID": 979,

    "Name": "Brittleness of nails"

  },

  {

    "ID": 192,

    "Name": "Bulging abdominal wall"

  },

  {

    "ID": 75,

    "Name": "Burning eyes"

  },

  {

    "ID": 46,

    "Name": "Burning in the throat"

  },

  {

    "ID": 288,

    "Name": "Burning nose"

  },

  {

    "ID": 107,

    "Name": "Burning sensation when urinating"

  },

  {

    "ID": 91,

    "Name": "Changes in the nails"

  },

  {

    "ID": 170,

    "Name": "Cheek swelling"

  },

  {

    "ID": 17,

    "Name": "Chest pain"

  },

  {

    "ID": 31,

    "Name": "Chest tightness"

  },

  {

    "ID": 175,

    "Name": "Chills"

  },

  {

    "ID": 218,

    "Name": "Coarsening of the skin structure"

  },

  {

    "ID": 89,

    "Name": "Cold feet"

  },

  {

    "ID": 978,

    "Name": "Cold hands"

  },

  {

    "ID": 139,

    "Name": "Cold sweats"

  },

  {

    "ID": 15,

    "Name": "Cough"

  },

  {

    "ID": 228,

    "Name": "Cough with sputum"

  },

  {

    "ID": 94,

    "Name": "Cramps"

  },

  {

    "ID": 49,

    "Name": "Cravings"

  },

  {

    "ID": 134,

    "Name": "Crusting"

  },

  {

    "ID": 260,

    "Name": "Curvature of the spine"

  },

  {

    "ID": 108,

    "Name": "Dark urine"

  },

  {

    "ID": 163,

    "Name": "Decreased urine stream"

  },

  {

    "ID": 165,

    "Name": "Delayed start to urination"

  },

  {

    "ID": 50,

    "Name": "Diarrhea"

  },

  {

    "ID": 79,

    "Name": "Difficult defecation"

  },

  {

    "ID": 126,

    "Name": "Difficulty in finding words"

  },

  {

    "ID": 98,

    "Name": "Difficulty in speaking"

  },

  {

    "ID": 93,

    "Name": "Difficulty in swallowing"

  },

  {

    "ID": 53,

    "Name": "Difficulty to concentrate"

  },

  {

    "ID": 1007,

    "Name": "Difficulty to learn"

  },

  {

    "ID": 1005,

    "Name": "Difficulty with gait"

  },

  {

    "ID": 216,

    "Name": "Discoloration of nails"

  },

  {

    "ID": 128,

    "Name": "Disorientation regarding time or place"

  },

  {

    "ID": 989,

    "Name": "Distended abdomen"

  },

  {

    "ID": 207,

    "Name": "Dizziness"

  },

  {

    "ID": 71,

    "Name": "Double vision"

  },

  {

    "ID": 270,

    "Name": "Double vision, acute-onset"

  },

  {

    "ID": 162,

    "Name": "Dribbling after urination"

  },

  {

    "ID": 244,

    "Name": "Drooping eyelid"

  },

  {

    "ID": 43,

    "Name": "Drowsiness"

  },

  {

    "ID": 273,

    "Name": "Dry eyes"

  },

  {

    "ID": 272,

    "Name": "Dry mouth"

  },

  {

    "ID": 151,

    "Name": "Dry skin"

  },

  {

    "ID": 87,

    "Name": "Earache"

  },

  {

    "ID": 92,

    "Name": "Early satiety"

  },

  {

    "ID": 1011,

    "Name": "Elbow pain"

  },

  {

    "ID": 1006,

    "Name": "Enlarged calf"

  },

  {

    "ID": 242,

    "Name": "Eye blinking"

  },

  {

    "ID": 287,

    "Name": "Eye pain"

  },

  {

    "ID": 33,

    "Name": "Eye redness"

  },

  {

    "ID": 208,

    "Name": "Eyelid swelling"

  },

  {

    "ID": 209,

    "Name": "Eyelids sticking together"

  },

  {

    "ID": 219,

    "Name": "Face pain"

  },

  {

    "ID": 246,

    "Name": "Facial paralysis"

  },

  {

    "ID": 970,

    "Name": "Facial swelling"

  },

  {

    "ID": 153,

    "Name": "Fast, deepened breathing"

  },

  {

    "ID": 83,

    "Name": "Fatty defecation"

  },

  {

    "ID": 982,

    "Name": "Feeling faint"

  },

  {

    "ID": 76,

    "Name": "Feeling of foreign body in the eye"

  },

  {

    "ID": 86,

    "Name": "Feeling of pressure in the ear"

  },

  {

    "ID": 164,

    "Name": "Feeling of residual urine"

  },

  {

    "ID": 145,

    "Name": "Feeling of tension in the legs"

  },

  {

    "ID": 11,

    "Name": "Fever"

  },

  {

    "ID": 995,

    "Name": "Finger deformity"

  },

  {

    "ID": 1013,

    "Name": "Finger pain"

  },

  {

    "ID": 1012,

    "Name": "Finger swelling"

  },

  {

    "ID": 214,

    "Name": "Flaking skin"

  },

  {

    "ID": 245,

    "Name": "Flaking skin on the head"

  },

  {

    "ID": 154,

    "Name": "Flatulence"

  },

  {

    "ID": 255,

    "Name": "Foot pain"

  },

  {

    "ID": 1002,

    "Name": "Foot swelling"

  },

  {

    "ID": 125,

    "Name": "Forgetfulness"

  },

  {

    "ID": 62,

    "Name": "Formation of blisters on a skin area"

  },

  {

    "ID": 84,

    "Name": "Foul smelling defecation"

  },

  {

    "ID": 59,

    "Name": "Frequent urination"

  },

  {

    "ID": 110,

    "Name": "Genital warts"

  },

  {

    "ID": 152,

    "Name": "Hair loss"

  },

  {

    "ID": 976,

    "Name": "Hallucination"

  },

  {

    "ID": 72,

    "Name": "Halo"

  },

  {

    "ID": 186,

    "Name": "Hand pain"

  },

  {

    "ID": 148,

    "Name": "Hand swelling"

  },

  {

    "ID": 80,

    "Name": "Hard defecation"

  },

  {

    "ID": 184,

    "Name": "Hardening of the skin"

  },

  {

    "ID": 9,

    "Name": "Headache"

  },

  {

    "ID": 206,

    "Name": "Hearing loss"

  },

  {

    "ID": 985,

    "Name": "Heart murmur"

  },

  {

    "ID": 45,

    "Name": "Heartburn"

  },

  {

    "ID": 122,

    "Name": "Hiccups"

  },

  {

    "ID": 993,

    "Name": "Hip deformity"

  },

  {

    "ID": 196,

    "Name": "Hip pain"

  },

  {

    "ID": 121,

    "Name": "Hoarseness"

  },

  {

    "ID": 149,

    "Name": "Hot flushes"

  },

  {

    "ID": 197,

    "Name": "Immobilization"

  },

  {

    "ID": 120,

    "Name": "Impaired balance"

  },

  {

    "ID": 90,

    "Name": "Impaired hearing"

  },

  {

    "ID": 70,

    "Name": "Impaired light-dark adaptation"

  },

  {

    "ID": 113,

    "Name": "Impairment of male potency"

  },

  {

    "ID": 81,

    "Name": "Incomplete defecation"

  },

  {

    "ID": 131,

    "Name": "Increased appetite"

  },

  {

    "ID": 262,

    "Name": "Increased drive"

  },

  {

    "ID": 204,

    "Name": "Increased salivation"

  },

  {

    "ID": 40,

    "Name": "Increased thirst"

  },

  {

    "ID": 220,

    "Name": "Increased touch sensitivity"

  },

  {

    "ID": 39,

    "Name": "Increased urine quantity"

  },

  {

    "ID": 257,

    "Name": "Involuntary movements"

  },

  {

    "ID": 986,

    "Name": "Irregular heartbeat"

  },

  {

    "ID": 65,

    "Name": "Irregular mole"

  },

  {

    "ID": 73,

    "Name": "Itching eyes"

  },

  {

    "ID": 88,

    "Name": "Itching in the ear"

  },

  {

    "ID": 973,

    "Name": "Itching in the mouth or throat"

  },

  {

    "ID": 96,

    "Name": "Itching in the nose"

  },

  {

    "ID": 21,

    "Name": "Itching of skin"

  },

  {

    "ID": 999,

    "Name": "Itching of the anus"

  },

  {

    "ID": 247,

    "Name": "Itching on head"

  },

  {

    "ID": 268,

    "Name": "Itching or burning in the genital area"

  },

  {

    "ID": 194,

    "Name": "Joint effusion"

  },

  {

    "ID": 198,

    "Name": "Joint instability"

  },

  {

    "ID": 27,

    "Name": "Joint pain"

  },

  {

    "ID": 230,

    "Name": "Joint redness"

  },

  {

    "ID": 193,

    "Name": "Joint swelling"

  },

  {

    "ID": 47,

    "Name": "Joylessness"

  },

  {

    "ID": 994,

    "Name": "Knee deformity"

  },

  {

    "ID": 256,

    "Name": "Knee pain"

  },

  {

    "ID": 146,

    "Name": "Leg cramps"

  },

  {

    "ID": 1010,

    "Name": "Leg pain"

  },

  {

    "ID": 231,

    "Name": "Leg swelling"

  },

  {

    "ID": 143,

    "Name": "Leg ulcer"

  },

  {

    "ID": 82,

    "Name": "Less than 3 defecations per week"

  },

  {

    "ID": 992,

    "Name": "Limited mobility of the ankle"

  },

  {

    "ID": 167,

    "Name": "Limited mobility of the back"

  },

  {

    "ID": 178,

    "Name": "Limited mobility of the fingers"

  },

  {

    "ID": 1000,

    "Name": "Limited mobility of the hip"

  },

  {

    "ID": 195,

    "Name": "Limited mobility of the leg"

  },

  {

    "ID": 35,

    "Name": "Lip swelling"

  },

  {

    "ID": 205,

    "Name": "Lockjaw"

  },

  {

    "ID": 210,

    "Name": "Loss of eye lashes"

  },

  {

    "ID": 174,

    "Name": "Lower abdominal pain"

  },

  {

    "ID": 263,

    "Name": "Lower-back pain"

  },

  {

    "ID": 261,

    "Name": "Lump in the breast"

  },

  {

    "ID": 266,

    "Name": "Malposition of the testicles"

  },

  {

    "ID": 232,

    "Name": "Marked veins"

  },

  {

    "ID": 235,

    "Name": "Memory gap"

  },

  {

    "ID": 112,

    "Name": "Menstruation disorder"

  },

  {

    "ID": 123,

    "Name": "Missed period"

  },

  {

    "ID": 215,

    "Name": "Moist and softened skin"

  },

  {

    "ID": 85,

    "Name": "Mood swings"

  },

  {

    "ID": 983,

    "Name": "Morning stiffness"

  },

  {

    "ID": 135,

    "Name": "Mouth pain"

  },

  {

    "ID": 97,

    "Name": "Mouth ulcers"

  },

  {

    "ID": 177,

    "Name": "Muscle pain"

  },

  {

    "ID": 119,

    "Name": "Muscle stiffness"

  },

  {

    "ID": 987,

    "Name": "Muscle weakness"

  },

  {

    "ID": 252,

    "Name": "Muscular atrophy in the leg"

  },

  {

    "ID": 202,

    "Name": "Muscular atrophy of the arm"

  },

  {

    "ID": 168,

    "Name": "Muscular weakness in the arm"

  },

  {

    "ID": 253,

    "Name": "Muscular weakness in the leg"

  },

  {

    "ID": 44,

    "Name": "Nausea"

  },

  {

    "ID": 136,

    "Name": "Neck pain"

  },

  {

    "ID": 234,

    "Name": "Neck stiffness"

  },

  {

    "ID": 114,

    "Name": "Nervousness"

  },

  {

    "ID": 133,

    "Name": "Night cough"

  },

  {

    "ID": 1004,

    "Name": "Night sweats"

  },

  {

    "ID": 63,

    "Name": "Non-healing skin wound"

  },

  {

    "ID": 38,

    "Name": "Nosebleed"

  },

  {

    "ID": 221,

    "Name": "Numbness in the arm"

  },

  {

    "ID": 254,

    "Name": "Numbness in the leg"

  },

  {

    "ID": 200,

    "Name": "Numbness of the hands"

  },

  {

    "ID": 137,

    "Name": "Oversensitivity to light"

  },

  {

    "ID": 157,

    "Name": "Overweight"

  },

  {

    "ID": 155,

    "Name": "Pain in the bones"

  },

  {

    "ID": 142,

    "Name": "Pain in the calves"

  },

  {

    "ID": 12,

    "Name": "Pain in the limbs"

  },

  {

    "ID": 990,

    "Name": "Pain of the anus"

  },

  {

    "ID": 203,

    "Name": "Pain on swallowing"

  },

  {

    "ID": 251,

    "Name": "Pain radiating to the arm"

  },

  {

    "ID": 103,

    "Name": "Pain radiating to the leg"

  },

  {

    "ID": 286,

    "Name": "Pain when chewing"

  },

  {

    "ID": 189,

    "Name": "Painful defecation"

  },

  {

    "ID": 109,

    "Name": "Painful urination"

  },

  {

    "ID": 150,

    "Name": "Pallor"

  },

  {

    "ID": 37,

    "Name": "Palpitations"

  },

  {

    "ID": 140,

    "Name": "Paralysis"

  },

  {

    "ID": 118,

    "Name": "Physical inactivity"

  },

  {

    "ID": 129,

    "Name": "Problems with the sense of touch in the face"

  },

  {

    "ID": 130,

    "Name": "Problems with the sense of touch in the feet"

  },

  {

    "ID": 258,

    "Name": "Protrusion of the eyes"

  },

  {

    "ID": 172,

    "Name": "Purulent discharge from the urethra"

  },

  {

    "ID": 173,

    "Name": "Purulent discharge from the vagina"

  },

  {

    "ID": 191,

    "Name": "Rebound tenderness"

  },

  {

    "ID": 54,

    "Name": "Reduced appetite"

  },

  {

    "ID": 78,

    "Name": "Ringing in the ear"

  },

  {

    "ID": 14,

    "Name": "Runny nose"

  },

  {

    "ID": 975,

    "Name": "Sadness"

  },

  {

    "ID": 269,

    "Name": "Scalp redness"

  },

  {

    "ID": 1001,

    "Name": "Scar"

  },

  {

    "ID": 60,

    "Name": "Sensitivity to cold"

  },

  {

    "ID": 69,

    "Name": "Sensitivity to glare"

  },

  {

    "ID": 102,

    "Name": "Sensitivity to noise"

  },

  {

    "ID": 264,

    "Name": "Shiny red tongue"

  },

  {

    "ID": 29,

    "Name": "Shortness of breath"

  },

  {

    "ID": 183,

    "Name": "Side pain"

  },

  {

    "ID": 26,

    "Name": "Skin lesion"

  },

  {

    "ID": 25,

    "Name": "Skin nodules"

  },

  {

    "ID": 124,

    "Name": "Skin rash"

  },

  {

    "ID": 61,

    "Name": "Skin redness"

  },

  {

    "ID": 217,

    "Name": "Skin thickening"

  },

  {

    "ID": 34,

    "Name": "Skin wheal"

  },

  {

    "ID": 241,

    "Name": "Sleepiness with spontaneous falling asleep"

  },

  {

    "ID": 52,

    "Name": "Sleeplessness"

  },

  {

    "ID": 95,

    "Name": "Sneezing"

  },

  {

    "ID": 13,

    "Name": "Sore throat"

  },

  {

    "ID": 64,

    "Name": "Sputum"

  },

  {

    "ID": 179,

    "Name": "Stomach burning"

  },

  {

    "ID": 185,

    "Name": "Stress-related leg pain"

  },

  {

    "ID": 28,

    "Name": "Stuffy nose"

  },

  {

    "ID": 138,

    "Name": "Sweating"

  },

  {

    "ID": 236,

    "Name": "Swelling in the genital area"

  },

  {

    "ID": 267,

    "Name": "Swelling of the testicles"

  },

  {

    "ID": 248,

    "Name": "Swollen glands in the armpit"

  },

  {

    "ID": 249,

    "Name": "Swollen glands in the groin"

  },

  {

    "ID": 169,

    "Name": "Swollen glands in the neck"

  },

  {

    "ID": 211,

    "Name": "Tears"

  },

  {

    "ID": 222,

    "Name": "Testicular pain"

  },

  {

    "ID": 243,

    "Name": "Tic"

  },

  {

    "ID": 201,

    "Name": "Tingling"

  },

  {

    "ID": 16,

    "Name": "Tiredness"

  },

  {

    "ID": 997,

    "Name": "Toe deformity"

  },

  {

    "ID": 1003,

    "Name": "Toe swelling"

  },

  {

    "ID": 980,

    "Name": "Tongue burning"

  },

  {

    "ID": 977,

    "Name": "Tongue swelling"

  },

  {

    "ID": 1008,

    "Name": "Toothache"

  },

  {

    "ID": 115,

    "Name": "Tremor at rest"

  },

  {

    "ID": 132,

    "Name": "Tremor on movement"

  },

  {

    "ID": 988,

    "Name": "Trouble understanding speech"

  },

  {

    "ID": 144,

    "Name": "Unconsciousness, short"

  },

  {

    "ID": 265,

    "Name": "Uncontrolled defecation"

  },

  {

    "ID": 116,

    "Name": "Underweight"

  },

  {

    "ID": 160,

    "Name": "Urge to urinate"

  },

  {

    "ID": 161,

    "Name": "Urination during the night"

  },

  {

    "ID": 68,

    "Name": "Vision impairment"

  },

  {

    "ID": 213,

    "Name": "Vision impairment for far objects"

  },

  {

    "ID": 166,

    "Name": "Vision impairment for near objects"

  },

  {

    "ID": 66,

    "Name": "Visual field loss"

  },

  {

    "ID": 101,

    "Name": "Vomiting"

  },

  {

    "ID": 181,

    "Name": "Vomiting blood"

  },

  {

    "ID": 972,

    "Name": "Weakness or numbness on right or left side of body"

  },

  {

    "ID": 23,

    "Name": "Weight gain"

  },

  {

    "ID": 22,

    "Name": "Weight loss"

  },

  {

    "ID": 30,

    "Name": "Wheezing"

  },

  {

    "ID": 187,

    "Name": "Wound"

  },

  {

    "ID": 105,

    "Name": "Yellow colored skin"

  },

  {

    "ID": 106,

    "Name": "Yellowish discoloration of the white part of the eye"

  }
    ]
    st="";

    for i in json:
      if string in i["Name"]:
        if string==i["Name"]:
          return i["ID"]
        st=st+i["Name"]+"\n";
    return st
  def getIssueId(symptoms,gender,dob):
    print(symptoms,gender,dob);
    url="https://healthservice.priaid.ch/diagnosis?symptoms=["+str(symptoms)+"]&gender="+str(gender)+"&year_of_birth="+str(dob)+"&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuaWtldDQ2OGtyQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTgzNyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjEwOCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiIxMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJCYXNpYyIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTktMDEtMjUiLCJpc3MiOiJodHRwczovL2F1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1NDg0ODYyODEsIm5iZiI6MTU0ODQ3OTA4MX0.qEYfcLozk1YdmiJnJxHW2YC8-sN1LVQI7w-b4b9ej1U&format=json&language=en-gb"
    results=requests.get(url);
    results=results.json()
    id=results[0]["Issue"]["ID"];
    url1="https://healthservice.priaid.ch/issues/"+str(id)+"/info?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFuaWtldDQ2OGtyQGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiaHR0cDovL3NjaGVtYXMueG1sc29hcC5vcmcvd3MvMjAwNS8wNS9pZGVudGl0eS9jbGFpbXMvc2lkIjoiMTgzNyIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvdmVyc2lvbiI6IjEwOCIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGltaXQiOiIxMDAiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXAiOiJCYXNpYyIsImh0dHA6Ly9leGFtcGxlLm9yZy9jbGFpbXMvbGFuZ3VhZ2UiOiJlbi1nYiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvZXhwaXJhdGlvbiI6IjIwOTktMTItMzEiLCJodHRwOi8vZXhhbXBsZS5vcmcvY2xhaW1zL21lbWJlcnNoaXBzdGFydCI6IjIwMTktMDEtMjUiLCJpc3MiOiJodHRwczovL2F1dGhzZXJ2aWNlLnByaWFpZC5jaCIsImF1ZCI6Imh0dHBzOi8vaGVhbHRoc2VydmljZS5wcmlhaWQuY2giLCJleHAiOjE1NDg0ODYyODEsIm5iZiI6MTU0ODQ3OTA4MX0.qEYfcLozk1YdmiJnJxHW2YC8-sN1LVQI7w-b4b9ej1U&format=json&language=en-gb"
    answer=requests.get(url1);
    answer=answer.json();
    #print(answer)
    #print(answer["Description"],answer["PossibleSymptoms"])
    string_answer="Description--------------------\n\n"+str(answer["Description"])+"\n\n"+"Medical Condition-----------------\n\n"+str(answer["MedicalCondition"])+"\n\n"+"Possible Symptoms------------------------------\n\n"+str(answer["PossibleSymptoms"])+"\n\n"+"Treatment Description-------------------------\n\n"+str(answer["TreatmentDescription"]);
    return string_answer;
